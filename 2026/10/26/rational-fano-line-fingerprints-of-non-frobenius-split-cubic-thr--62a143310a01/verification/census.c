#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#define N (1u<<25)
static uint8_t *seen;
static uint32_t *queue;
static uint32_t swap01(uint32_t a){
 uint32_t b=0;
 int p[5]={1,0,2,3,4};
 for(int i=0;i<5;i++){
   uint32_t r=(a>>(5*p[i]))&31u;
   uint32_t s=(r&28u)|((r&1u)<<1)|((r&2u)>>1);
   b|=(s<<(5*i));
 }
 return b;
}
static uint32_t cyc(uint32_t a){
 uint32_t b=0;
 for(int i=0;i<5;i++){
  uint32_t r=(a>>(5*((i+1)%5)))&31u;
  r=((r>>1)|((r&1)<<4));
  b|=r<<(5*i);
 }
 return b;
}
static uint32_t shear01(uint32_t a){
 uint32_t r[5];
 for(int i=0;i<5;i++){
  r[i]=(a>>(5*i))&31u;
  if(r[i]&1u)r[i]^=2u;
 }
 r[1]^=r[0];
 uint32_t b=0;
 for(int i=0;i<5;i++)b|=r[i]<<(5*i);
 return b;
}
static int invertible(uint32_t a){
 uint32_t bs[5]={0};
 for(int i=0;i<5;i++){
  uint32_t x=(a>>(5*i))&31u;
  while(x){
   int j=31-__builtin_clz(x);
   if(bs[j])x^=bs[j];
   else{bs[j]=x;break;}
  }
  if(!x)return 0;
 }
 return 1;
}
static int pointcount(uint32_t a){
 int n=0;
 for(int x=1;x<32;x++){
  int p=0;
  for(int i=0;i<5;i++)if(x&(1<<i))p^=__builtin_parity((a>>(5*i))&x&31u);
  n+=(p==0);
 }
 return n;
}
int main(){
 seen=calloc(N,1);queue=malloc((size_t)10000000*4+128);
 if(!seen||!queue){perror("calloc");return 2;}
 uint64_t sum=0;int cl=0, spectra[32]={0};
 printf("BEGIN census of non-Frobenius split smooth cubic threefolds over F2 (matrix congruence).\n");fflush(stdout);
 for(uint32_t a=0;a<N;a++){
  if(seen[a])continue;
  if(!invertible(a))continue;
  uint32_t tail=1, head=0;queue[0]=a;seen[a]=1;
  while(head<tail){
   uint32_t x=queue[head++];
   uint32_t t[3]={swap01(x),cyc(x),shear01(x)};
   for(int j=0;j<3;j++)if(!seen[t[j]]){
     seen[t[j]]=1;
     if(tail>=10000000){fprintf(stderr,"oversized orbit\n");return 3;}
     queue[tail++]=t[j];
   }
  }
  int num=pointcount(a);
  printf("class=%d representative=%u size=%u N1=%d stabilizer=%u\n",++cl,a,tail,num,9999360u/tail);
  if(9999360u%tail){fprintf(stderr,"bad orbit %u\n",tail);return 4;}
  spectra[num]+=tail;sum+=tail;
 }
 printf("TOTAL classes=%d matrices=%"PRIu64"\n",cl,sum);
 for(int i=0;i<32;i++)if(spectra[i])printf("N1=%d matrices=%d\n",i,spectra[i]);
 if(sum!=9999360u){fprintf(stderr,"bad sum\n");return 5;}
 free(queue);free(seen);return 0;
}
