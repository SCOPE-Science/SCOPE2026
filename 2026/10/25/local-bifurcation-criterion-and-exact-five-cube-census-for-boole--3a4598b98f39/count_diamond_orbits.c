#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

/* Exact enumeration of labelled surjective bounded morphisms from
   a Boolean inclusion poset to the four-point Boolean diamond. */
static uint64_t *functions[6];
static int nf[6];
static uint32_t supersets[32], covers[32];
static uint32_t transform[120][7581];
static int permset[120][5], nperm;

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


static void permute_rec(int n, int depth, int *a, int *used) {
    if(depth==n){
       for(int i=0;i<n;i++) permset[nperm][i]=a[i];
       nperm++;return;
    }
    for(int i=0;i<n;i++) if(!used[i]) {
      used[i]=1; a[depth]=i; permute_rec(n,depth+1,a,used);used[i]=0;
    }
}
static int get_permutations(int n) {
    nperm=0;int a[5]={0},used[5]={0};permute_rec(n,0,a,used);
    int sz=1<<n;
    for(int p=0;p<nperm;p++) {
      unsigned xmap[32];
      for(unsigned x=0;x<(unsigned)sz;x++) {
        unsigned target=0;
        for(int i=0;i<n;i++)if(x&(1u<<i))target|=1u<<permset[p][i];
        xmap[x]=target;
      }
      for(int i=0;i<nf[n];i++){
        uint32_t f=(uint32_t)functions[n][i];
        uint32_t g=0;
        for(int x=0;x<sz;x++)if(f&(1u<<x))g|=1u<<xmap[x];
        transform[p][i]=g;
      }
    }
    return nperm;
}
static void exact_count_and_orbits(int n, uint64_t *raw, uint64_t *orbit) {
  set_masks(n);
  int sz=1<<n;
  uint32_t all=(sz==32)?0xffffffffu:((1u<<sz)-1);
  int pn=get_permutations(n);
  uint64_t count=0, fixed_sum=0;
  for(int i=0;i<nf[n];i++) {
    uint32_t F=(uint32_t)functions[n][i];
    if ((F&1)!=0 || !(F & (1u<<(sz-1)))) continue;
    for(int j=0;j<nf[n];j++) {
      uint32_t G=(uint32_t)functions[n][j];
      if((G&1)!=0 || !(G&(1u<<(sz-1)))) continue;
      uint32_t A=F&~G, B=G&~F;
      if(!A || !B)continue;
      uint32_t Z=(~(F|G))&all;
      int good=1;
      while (Z) {
        int x=__builtin_ctz(Z);Z&=Z-1;
        if((covers[x] & (~(F|G)) & all)==0) {
          if(!(A&supersets[x]) || !(B&supersets[x])) {good=0;break;}
        }
      }
      if(!good)continue;
      count++;
      for(int p=0;p<pn;p++){
         uint32_t h=transform[p][i],l=transform[p][j];
         fixed_sum+=(h==F && l==G);
         fixed_sum+=(h==G && l==F);
      }
    }
  }
  *raw=count;
  if(fixed_sum%(2*pn)!=0){fprintf(stderr,"Burnside divisibility failed\n");exit(2);}
  *orbit=fixed_sum/(2*pn);
}

int main(void){
 for(int n=0;n<=5;n++)build_functions(n);
 for(int n=1;n<=5;n++) {
   uint64_t raw=0, orbit=0;
   exact_count_and_orbits(n,&raw,&orbit);
   printf("n=%d monotone_functions=%d bounded_surjections=%"PRIu64" symmetry_orbits=%"PRIu64"\n",n,nf[n],raw,orbit);
   fflush(stdout);
 }
 return 0;
}
