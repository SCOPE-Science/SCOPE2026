#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

/* Exact enumeration of labelled surjective bounded morphisms from
   a Boolean inclusion poset to the four-point Boolean diamond. */
static uint64_t *functions[6];
static int nf[6];
static uint32_t supersets[32], covers[32];

void build_functions(int n) {
  if(n==0) {
    functions[0]=malloc(2*sizeof(uint64_t));
    functions[0][0]=0;functions[0][1]=1; nf[0]=2;return;
  }
  int m=1<<(n-1), prev=nf[n-1];
  functions[n]=malloc((size_t)prev*prev*sizeof(uint64_t));
  int count=0;
  uint64_t lower_mask=(1ULL<<m)-1ULL;
  for(int i=0;i<prev;i++) for(int j=0;j<prev;j++) {
    uint64_t low=functions[n-1][i], high=functions[n-1][j];
    if((low & ~high)==0) functions[n][count++]=(low&lower_mask)|(high<<m);
  }
  nf[n]=count;
}

void set_masks(int n) {
  int sz=1<<n;
  for(int x=0;x<sz;x++) {
    supersets[x]=0;covers[x]=0;
    for(int y=0;y<sz;y++)if((x&y)==x)supersets[x]|=(1u<<y);
    for(int i=0;i<n;i++)if(!(x&(1<<i)))covers[x]|=1u<<(x|(1<<i));
  }
}

uint64_t exact_count(int n) {
  set_masks(n);
  int m=1<<n;
  uint32_t all=(m==32)?0xffffffffu:((1u<<m)-1);
  uint64_t count=0;
  for(int i=0;i<nf[n];i++) {
    uint32_t F=(uint32_t)functions[n][i];
    if ((F&1)!=0 || !(F & (1u<<(m-1)))) continue;
    for(int j=0;j<nf[n];j++) {
      uint32_t G=(uint32_t)functions[n][j];
      if((G&1)!=0 || !(G&(1u<<(m-1)))) continue;
      uint32_t A=F&~G, B=G&~F;
      if(!A || !B)continue;
      uint32_t Z=(~(F|G))&all;
      int good=1;
      while (Z) {
        int x=__builtin_ctz(Z);
        Z&=Z-1;
        if((covers[x] & (~(F|G)) & all)==0) {
          if(!(A&supersets[x]) || !(B&supersets[x])) {good=0;break;}
        }
      }
      count+=good;
    }
  }
  return count;
}

int main(void){
 for(int n=0;n<=5;n++)build_functions(n);
 for(int n=1;n<=5;n++) {
   printf("n=%d monotone_functions=%d bounded_surjections=%"PRIu64"\n",n,nf[n],exact_count(n));
   fflush(stdout);
 }
 return 0;
}
