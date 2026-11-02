#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define HTSIZE (1<<22)
static uint64_t *slots, *queue;
static uint64_t mult[7][29];
static uint64_t witness[7][29];
static int q[64], odd[28];
static inline int bil(int x,int y){unsigned z=((x&0x15)<<1)^((x&0x2a)>>1);return __builtin_parity((unsigned)z&y);}
static inline uint64_t mcode(const int c[6]){uint64_t a=0;for(int i=0;i<6;i++)a|=(uint64_t)c[i]<<(6*i);return a;}
static inline uint64_t hash(uint64_t x){ x^=x>>23; x*=0x2127599bf4325c37ULL; x^=x>>47;return x&(HTSIZE-1);}
static int push(uint64_t code,size_t *len){uint64_t h=hash(code);while(slots[h]){if(slots[h]==code)return 0;h=(h+1)&(HTSIZE-1);}slots[h]=code;queue[(*len)++]=code;return 1;}
static void analyze(uint64_t code){
 int c[6]; for(int i=0;i<6;i++)c[i]=(code>>(6*i))&63;
 int bit=0;for(int k=0;k<28;k++){
  int t=odd[k],good=1;
  for(int i=0;i<6;i++)if(q[c[i]]!=bil(t,c[i]^(1<<i))){good=0;break;}
  bit+=good;
 }
 int rows[6]={0};for(int i=0;i<6;i++)for(int j=0;j<6;j++)if((c[j]>>i)&1)rows[i]|=1<<j;
 for(int i=0;i<6;i++)rows[i]^=1<<i;
 int rank=0;for(int j=0;j<6;j++){int pivot=rank;while(pivot<6&&!(rows[pivot]&(1<<j)))pivot++;if(pivot==6)continue;int t=rows[pivot];rows[pivot]=rows[rank];rows[rank]=t;for(int i=0;i<6;i++)if(i!=rank&&(rows[i]&(1<<j)))rows[i]^=rows[rank];rank++;}
 int r=6-rank;mult[r][bit]++;if(!witness[r][bit])witness[r][bit]=code;
}
int main(){for(int a=0,j=0;a<64;a++){for(int i=0;i<6;i+=2)q[a]^=((a>>i)&1)&((a>>(i+1))&1);if(q[a])odd[j++]=a;}
 slots=calloc(HTSIZE,sizeof(uint64_t));queue=malloc(1500000*sizeof(uint64_t));
 int c[6];for(int i=0;i<6;i++)c[i]=1<<i;
 uint64_t ident=mcode(c);size_t len=0;push(ident,&len);
 const int gens[8]={1,2,4,8,16,32,5,20};
 for(size_t n=0;n<len;n++){
  uint64_t a=queue[n];analyze(a);
  for(int j=0;j<8;j++){
   int v=gens[j],cols[6];for(int i=0;i<6;i++){int x=(a>>(i*6))&63;cols[i]=x^(bil(x,v)?v:0);}
   if(len>=1500000){fprintf(stderr,"TOO MANY\n");return 1;}
   push(mcode(cols),&len);
  }
 }
 printf("GROUP_SIZE=%zu\n",len);
 for(int i=0;i<7;i++)for(int j=0;j<29;j++)if(mult[i][j])printf("%d,%d,%llu,%09llx\n",i,j,(unsigned long long)mult[i][j],(unsigned long long)witness[i][j]);
 free(slots);free(queue);
}
