/* Independent finite checks of four relational confluences and their endpoint normal form.
 * Compile: cc -O2 -std=c99 -Wall -Wextra four_confluence_verification.c -o check && ./check
 */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
static uint64_t counts[7], visits[7];
static int n, masks[64], lo[64], hi[64], rcount;

static int endpoints(uint64_t R, int q) {
  if (!R) return 1;
  int prev_min=-1, prev_max=-1;
  for(int i=0;i<q;i++) {
    int mini=-1, maxi=-1;
    for(int j=0;j<q;j++) if(R & (1ULL << (i*q+j))) {
      if (mini < 0) mini=j;
      maxi=j;
    }
    if (mini < 0 || (i && (mini<prev_min || maxi<prev_max))) return 0;
    prev_min=mini; prev_max=maxi;
  }
  prev_min=-1; prev_max=-1;
  for(int j=0;j<q;j++) {
    int mini=-1, maxi=-1;
    for(int i=0;i<q;i++) if(R & (1ULL << (i*q+j))) {
      if (mini < 0) mini=i;
      maxi=i;
    }
    if (mini < 0 || (j && (mini<prev_min || maxi<prev_max))) return 0;
    prev_min=mini; prev_max=maxi;
  }
  return 1;
}

/* Raw relational conditions, directly quantified over all three vertices. */
static int four_relations(uint64_t R,int q) {
  #define EDGE(a,b) ((R>>( (a)*q+(b) ))&1ULL)
  for(int a=0;a<q;a++) for(int b=0;b<q;b++) for(int c=0;c<q;c++) {
    int witness=0;
    if(a>=b && EDGE(b,c)) {
      witness=0; for(int d=0;d<q;d++) if(EDGE(a,d) && d>=c) witness=1;
      if(!witness) return 0;
    }
    if(a<=b && EDGE(b,c)) {
      witness=0; for(int d=0;d<q;d++) if(EDGE(a,d) && d<=c) witness=1;
      if(!witness) return 0;
    }
    if(EDGE(a,b) && b<=c) {
      witness=0; for(int d=0;d<q;d++) if(d>=a && EDGE(d,c)) witness=1;
      if(!witness) return 0;
    }
    if(EDGE(a,b) && b>=c) {
      witness=0; for(int d=0;d<q;d++) if(d<=a && EDGE(d,c)) witness=1;
      if(!witness) return 0;
    }
  }
  return 1;
  #undef EDGE
}

static void dfs(int row, int pmin, int pmax, uint64_t R) {
  if(row==n) { visits[n]++; counts[n]+=endpoints(R,n); return; }
  for(int k=0;k<rcount;k++) if(lo[k]>=pmin && hi[k]>=pmax)
    dfs(row+1,lo[k],hi[k],R|((uint64_t)masks[k]<<(row*n)));
}
static uint64_t count_by_endpoints(int q){
  n=q;rcount=0;counts[n]=0;visits[n]=0;
  for(int b=1;b<(1<<n);b++){
    masks[rcount]=b;int l=0,h=n-1;
    while(!((b>>l)&1))l++;
    while(!((b>>h)&1))h--;
    lo[rcount]=l;hi[rcount]=h;rcount++;
  }
  dfs(0,0,0,0);
  return 1+counts[n];
}
static void edge_spectrum_check(int q) {
  uint64_t R=0;
  for(int i=0;i<q;i++) R|=1ULL<<(i*q+i);
  if(!endpoints(R,q))exit(3);
  for(int d=1;d<q;d++) for(int i=0;i+d<q;i++) {
    R|=1ULL<<(i*q+i+d);
    if(!endpoints(R,q))exit(3);
  }
  for(int d=1;d<q;d++) for(int i=d;i<q;i++) {
    R|=1ULL<<(i*q+i-d);
    if(!endpoints(R,q))exit(3);
  }
  if(__builtin_popcountll(R)!=q*q)exit(3);
}
int main(void){
  const uint64_t reference[7]={0,2,5,34,538,23415,3567130};
  for(int q=1;q<=4;q++){
    uint64_t count=0, total=1ULL<<(q*q);
    for(uint64_t R=0;R<total;R++){
      int direct=four_relations(R,q), normal=endpoints(R,q);
      if(direct!=normal){fprintf(stderr,"Mismatch q=%d relation=%llu\n",q,(unsigned long long)R);return 1;}
      count+=direct;
    }
    if(count!=reference[q])return 2;
    printf("DIRECT_CONFLUENCE_OK %d %llu\n",q,(unsigned long long)count);
  }
  for(int q=1;q<=6;q++){
    uint64_t count=count_by_endpoints(q);
    printf("ENDPOINT_ENUMERATION_OK %d %llu explored=%llu\n",q,
           (unsigned long long)count,(unsigned long long)visits[q]);
    if(count!=reference[q])return 2;
  }
  for(int q=1;q<=7;q++)edge_spectrum_check(q);
  puts("FOUR_WAY_CONFLUENCE_VERIFICATION_OK");
  return 0;
}
