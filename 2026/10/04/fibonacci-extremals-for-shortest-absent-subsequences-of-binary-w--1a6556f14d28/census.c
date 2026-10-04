#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static int universality(uint64_t x,int n){
  int seen=0,k=0;
  for(int i=0;i<n;i++){
    int b=(x>>(n-1-i))&1ULL;
    seen|=1<<b;
    if(seen==3){k++;seen=0;}
  }
  return k;
}
// number of distinct subsequences of exact length L in binary word x length n.
static uint32_t distinct_len(uint64_t x,int n,int L){
  uint32_t dp[32]={0}; dp[0]=1;
  uint32_t last[2][32]; memset(last,0,sizeof(last));
  for(int i=0;i<n;i++){
    int b=(x>>(n-1-i))&1ULL;
    uint32_t old[32]; memcpy(old,dp,sizeof(dp));
    for(int l=1;l<=L;l++){
      uint32_t add=old[l-1];
      dp[l]=old[l]+add-last[b][l];
      last[b][l]=add;
    }
  }
  return dp[L];
}
static uint64_t revbits(uint64_t x,int n){uint64_t y=0;for(int i=0;i<n;i++)y=(y<<1)|((x>>i)&1ULL);return y;}
static uint64_t canon(uint64_t x,int n){
 uint64_t mask=(n==64)?~0ULL:((1ULL<<n)-1), c=x^mask, r=revbits(x,n), rc=revbits(c,n), m=x;
 if(c<m)m=c;if(r<m)m=r;if(rc<m)m=rc;return m;
}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):22;
 for(int n=1;n<=N;n++){
   uint64_t total=1ULL<<n; uint32_t best=0; uint64_t num=0; int bestL=0; uint64_t *ext=NULL; size_t cap=0;
   for(uint64_t x=0;x<total;x++){
     int k=universality(x,n); int L=k+1; uint32_t d=distinct_len(x,n,L); uint32_t c=(1U<<L)-d;
     if(c>best){best=c;num=1;bestL=L;if(cap<1){cap=16;ext=realloc(ext,cap*sizeof(*ext));}ext[0]=x;}
     else if(c==best){ if(num>=cap){cap=cap?2*cap:16;ext=realloc(ext,cap*sizeof(*ext));}ext[num++]=x; }
   }
   uint64_t orbits=0;
   for(uint64_t i=0;i<num;i++) if(canon(ext[i],n)==ext[i]) orbits++;
   printf("%d %u %d %llu %llu",n,best,bestL,(unsigned long long)num,(unsigned long long)orbits);
   for(uint64_t i=0;i<num && i<16;i++){printf(" ");for(int j=n-1;j>=0;j--)putchar(((ext[i]>>j)&1)+'0');}
   putchar('\n'); free(ext);
 }
}
