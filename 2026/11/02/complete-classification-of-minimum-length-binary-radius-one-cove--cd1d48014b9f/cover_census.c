/* Exact enumeration of binary cyclic radius-one de Bruijn covering codes of window order 7. */
#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#define N 7
#define L 22
#define FULL ((1u<<L)-1u)
static uint64_t cover0[128],cover1[128];
static unsigned popcount(unsigned x) {unsigned r=0; while(x){r+=(x&1u);x>>=1;}return r;}
static uint32_t reverse22(uint32_t x){uint32_t y=0;for(int i=0;i<L;i++){y=(y<<1)|(x&1);x>>=1;}return y;}
static uint32_t rotate22(uint32_t x){return ((x<<1)&FULL)|(x>>(L-1));}
static uint32_t canon(uint32_t x) {uint32_t b=FULL;
 for(int t=0;t<4;t++) {uint32_t y = ((t&2)?reverse22(x):x)^((t&1)?FULL:0);
 for(int j=0;j<L;j++){if(y<b)b=y;y=rotate22(y);} }
 return b;}
static int good(uint32_t x,int m){uint64_t a=0,b=0;
 if(m>=N){uint64_t z=x|((uint64_t)x<<m);
   for(int j=0;j<m;j++) {uint32_t w=(z>>j)&127u;a|=cover0[w];b|=cover1[w];}
 } else {
   for(int j=0;j<m;j++) {uint32_t w=0;
      for(int k=0;k<N;k++)w|=((x>>((j+k)%m))&1u)<<k;
      a|=cover0[w];b|=cover1[w]; }
 }
 return a==UINT64_MAX&&b==UINT64_MAX;}
int main(){
 for(int w=0;w<128;w++)for(int z=0;z<128;z++)if(popcount((unsigned)(w^z))<=1){if(z<64)cover0[w]|=1ull<<z;else cover1[w]|=1ull<<(z-64);}
 uint32_t reps[10];unsigned nreps=0;uint64_t counts[23]={0};unsigned hist[23]={0};
 FILE *f=fopen("solutions.txt","w");if(!f)return 7;
 for(int m=1;m<=L;m++)for(uint32_t x=0;x<(1u<<m);x++){
   if(good(x,m)){
    counts[m]++;
    if(m==L){hist[popcount(x)]++; fprintf(f,"%u\n",x);
     if(x==canon(x)){if(nreps>=10)return 8;reps[nreps++]=x;}
    }
   }
 }
 fclose(f);
 for(int m=1;m<=L;m++)printf("length %d: %" PRIu64 "\n",m,counts[m]);
 for(int m=1;m<L;m++)if(counts[m]!=0)return 10;
 printf("reps %u\n",nreps);
 for(unsigned i=0;i<nreps;i++){printf("representative %u ",reps[i]);for(int k=0;k<L;k++)putchar((reps[i]>>k&1u)+'0');printf(" weight %u\n",popcount(reps[i]));}
 for(int j=0;j<=L;j++)if(hist[j])printf("weight %d: %u\n",j,hist[j]);
 return (counts[L]==132&&nreps==2&&hist[11]==132)?0:9;
}
