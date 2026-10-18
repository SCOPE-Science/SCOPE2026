/* Exhaustive independent labeled-graph computation of the sharp bold-homology threshold.
   Compile: cc -O3 -std=c11 census_labeled.c -o census_labeled
   Run: ./census_labeled
   Mathematical definitions and checks are in RESULT.md.
*/
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
static int N, F, e_u[21],e_v[21],m;
static unsigned short adj[7],unu[128];
static int bad[128],counts[8],face[8][128],position[128],ranks[8];
static unsigned long long connected_count[8],zero_count[8],witness_count[8],bad_pattern=0;

static int connectivity(int M){
  int reached=M&(-M);
  while(1){
    int expanded=reached;
    for(int i=0;i<N;i++) if(reached&(1<<i)) expanded|=adj[i]&M;
    if(expanded==reached)return reached==M;
    reached=expanded;
  }
}
static int is_target_graph(void){
  int apex=0,others=0;
  for(int i=0;i<N;i++){
    int degree=__builtin_popcount((unsigned)adj[i]);
    if(degree==5)apex|=1<<i;
    else if(degree==4)others|=1<<i;
    else return 0;
  }
  if(__builtin_popcount((unsigned)apex)!=2 || __builtin_popcount((unsigned)others)!=5)return 0;
  for(int i=0;i<N;i++)if(apex&(1<<i)){
    if((adj[i]&apex)!=0 || (adj[i]&others)!=others)return 0;
  }
  for(int i=0;i<N;i++)if(others&(1<<i))
    if(__builtin_popcount((unsigned)(adj[i]&others))!=2)return 0;
  return connectivity(others);
}
static int rank64(const uint64_t *vecs,int num){
  uint64_t pivot[64]={0};int r=0;
  for(int i=0;i<num;i++){
    uint64_t x=vecs[i];
    while(x){
      int b=63-__builtin_clzll(x);
      if(!pivot[b]){pivot[b]=x;r++;break;}
      x^=pivot[b];
    }
  }
  return r;
}
static int nonzero_betti(void){
  memset(counts,0,sizeof(counts));
  memset(ranks,0,sizeof(ranks));
  for(int S=0;S<=F;S++)if(bad[S]){
    int k=__builtin_popcount((unsigned)S);
    face[k][counts[k]++]=S;
  }
  for(int k=1;k<=N;k++){
    memset(position,-1,sizeof(position));
    for(int i=0;i<counts[k-1];i++)position[face[k-1][i]]=i;
    uint64_t cols[128];
    for(int i=0;i<counts[k];i++){
      int S=face[k][i];uint64_t x=0;
      for(int b=S;b;b&=b-1){
        int B=b&-b;
        int rem=S^B;
        if(position[rem]<0){fprintf(stderr,"not simplicial!\n");exit(3);}
        x^=1ULL<<position[rem];
      }
      cols[i]=x;
    }
    ranks[k]=rank64(cols,counts[k]);
  }
  for(int k=0;k<=N;k++){
    int betti=counts[k] - ranks[k] - (k<N?ranks[k+1]:0);
    if(betti<0){fprintf(stderr,"negative betti!\n");exit(4);}
    if(betti)return 1;
  }
  return 0;
}
static void work_graph(unsigned int graphmask){
  memset(adj,0,sizeof(adj));
  for(int j=0;j<m;j++)if(graphmask&(1U<<j)){
    adj[e_u[j]]|=1<<e_v[j];adj[e_v[j]]|=1<<e_u[j];
  }
  if(!connectivity(F))return;
  connected_count[N]++;
  unu[0]=0;int chi=0;
  for(int S=0;S<=F;S++){
    if(S){int bit=S&-S;int v=__builtin_ctz((unsigned)bit);unu[S]=unu[S^bit]|adj[v];}
    int cd=(S!=0 && (S|unu[S])==F && connectivity(S));
    bad[S]=!cd;
    if(cd)chi+=(__builtin_popcount((unsigned)S)&1)?-1:1;
  }
  if(chi!=0)return;
  zero_count[N]++;
  if(!nonzero_betti())return;
  witness_count[N]++;
  if(!is_target_graph()){
    bad_pattern++;
    printf("UNEXPECTED n=%d mask=%u\n",N,graphmask);
  }
}
int main(void){
  for(N=1;N<=7;N++){
    F=(1<<N)-1;m=0;
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
      e_u[m]=i;e_v[m]=j;m++;
    }
    unsigned int lim=1U<<m;
    for(unsigned int mask=0;mask<lim;mask++)work_graph(mask);
    printf("n=%d connected_labeled=%llu zero_euler_labeled=%llu nonzero_zero_euler_labeled=%llu\n",N,connected_count[N],zero_count[N],witness_count[N]);
    fflush(stdout);
  }
  printf("unexpected_witness_patterns=%llu\n",bad_pattern);
  if(witness_count[7]!=252 || bad_pattern) return 1;
  for(int n=1;n<7;n++)if(witness_count[n])return 1;
  return 0;
}
