#include <cstdint>
#include <cstdio>
#include <algorithm>
using U=uint64_t;
int main(){
 long long connectedTotal=0,chiZeroTotal=0,passTotal=0;
 for(int n=1;n<=7;n++){
  const int N=1<<n, all=N-1, e=n*(n-1)/2;
  const U graphs=U(1)<<e;
  int eu[21],ev[21],pos=0;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){eu[pos]=i;ev[pos]=j;pos++;}
  int counts[128],cd[128],indices[128],sizes[128];
  for(int s=0;s<N;s++)counts[s]=__builtin_popcount((unsigned)s);
  long long con=0,zeros=0,valid=0;U witness=0;
  for(U g=0;g<graphs;g++){
   int adj[7]={};
   for(int t=0;t<e;t++)if((g>>t)&1){adj[eu[t]]|=1<<ev[t];adj[ev[t]]|=1<<eu[t];}
   int reached=1,old=0;
   while(reached!=old){old=reached;for(int i=0;i<n;i++)if(reached&(1<<i))reached|=adj[i];}
   if(reached!=all)continue;
   con++;
   std::fill(sizes,sizes+N,0);
   int chi=0;
   for(int s=1;s<N;s++){
    int nb=s,vertices=s;
    while(vertices){int b=__builtin_ctz((unsigned)vertices); vertices&=vertices-1;nb|=adj[b];}
    if(nb!=all){cd[s]=0;continue;}
    int walk=s&-s,was=0;
    while(walk!=was){was=walk;int m=walk;while(m){int b=__builtin_ctz((unsigned)m);m&=m-1;walk|=adj[b]&s;}}
    if(walk!=s){cd[s]=0;continue;}
    cd[s]=1;int k=counts[s];sizes[k]++;chi+=(k%2)?-1:1;
   }
   if(chi!=0)continue;
   zeros++;
   int rprev=0,nonzero=0; int beta2=0,beta3=0,others=0;
   for(int k=1;k<=n;k++){
    std::fill(indices,indices+N,-1);
    int idx=0;
    for(int s=1;s<N;s++)if(counts[s]==k+1&&cd[s])indices[s]=idx++;
    U piv[64]={};int rank=0;
    if(k<n)for(int s=1;s<N;s++)if(counts[s]==k&&cd[s]){
       U v=0;int complement=all^s;
       while(complement){int b=__builtin_ctz((unsigned)complement);complement&=complement-1;int rr=indices[s|(1<<b)];if(rr>=0)v^=U(1)<<rr;}
       while(v){int lead=63-__builtin_clzll(v);if(piv[lead])v^=piv[lead];else {piv[lead]=v;rank++;break;}}
    }
    int betti=sizes[k]-rank-rprev;
    if(betti<0){std::printf("INVALID rank graph=%llu k=%d beta=%d\n",(unsigned long long)g,k,betti);return 2;}
    nonzero|=(betti>0);
    if(k==2)beta2=betti; else if(k==3)beta3=betti;else others+=betti;
    rprev=rank;
   }
   if(nonzero){
     valid++;witness=g;
     if(beta2!=1||beta3!=1||others!=0){std::printf("UNEXPECTED_BETTI n=%d g=%llu beta2=%d beta3=%d others=%d\n",n,(unsigned long long)g,beta2,beta3,others);return 6;}
     // Expected unique class: two nonadjacent degree-5 vertices, remaining five form a chordless C5.
     int ap=0;
     for(int i=0;i<n;i++)if(__builtin_popcount((unsigned)adj[i])==5)ap|=1<<i;
     if(n!=7 || __builtin_popcount((unsigned)ap)!=2){std::printf("UNEXPECTED_ORDER_OR_APICES n=%d g=%llu\n",n,(unsigned long long)g);return 3;}
     int rim=all^ap;
     for(int i=0;i<n;i++){
      if(ap&(1<<i)){if((adj[i]&ap)!=0||(adj[i]&rim)!=rim){std::printf("BAD_APEX\n");return 4;}}
      else if((adj[i]&ap)!=ap||__builtin_popcount((unsigned)(adj[i]&rim))!=2){std::printf("BAD_RIM\n");return 5;}
     }
   }
  }
  connectedTotal+=con;chiZeroTotal+=zeros;passTotal+=valid;
  std::printf("n=%d labeled=%llu connected=%lld euler_zero=%lld euler_zero_nonacyclic=%lld witness_bitmask=%llu\n",n,(unsigned long long)graphs,con,zeros,valid,(unsigned long long)witness);
  std::fflush(stdout);
 }
 std::printf("ALL_GRAPHS_EXHAUSTED connected=%lld chi_zero=%lld positive=%lld\n",connectedTotal,chiZeroTotal,passTotal);
 return 0;
}
