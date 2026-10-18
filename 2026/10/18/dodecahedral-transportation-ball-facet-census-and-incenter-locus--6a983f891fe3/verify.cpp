#include <bits/stdc++.h>
using namespace std;
constexpr int N=20;
int E[30][2],adj[N][N],f[N],ord[N],k=0;
long long countAll=0,facets=0,tight_hist[31]={},contact=0,otherMax=0;
int maxT=0;
set<array<int,20>> maximizing;
void enumerate(int d){
 if(d==N){
  countAll++;
  int used[N]={};int q[N],h=0,t=0;q[t++]=0;used[0]=1;
  while(h<t){int u=q[h++];for(int v=0;v<N;v++)if(adj[u][v]&&!used[v]&&abs(f[u]-f[v])==1){used[v]=1;q[t++]=v;}}
  if(t<N)return;
  facets++;
  int s=0,s2=0,te=0;for(int i=0;i<N;i++){s+=f[i];s2+=f[i]*f[i];}for(auto &e:E)te+=(abs(f[e[0]]-f[e[1]])==1);
  tight_hist[te]++;
  int T=N*s2-s*s;
  if(T>maxT){maxT=T;contact=1;maximizing.clear();array<int,N>a;copy(f,f+N,a.begin());maximizing.insert(a);}
  else if(T==maxT){contact++;array<int,N>a;copy(f,f+N,a.begin());maximizing.insert(a);}
  return;
 }
 int v=ord[d],lo=-100,hi=100;
 for(int j=0;j<d;j++)if(adj[v][ord[j]]){lo=max(lo,f[ord[j]]-1);hi=min(hi,f[ord[j]]+1);}
 for(int a=lo;a<=hi;a++){f[v]=a;enumerate(d+1);}
}
int main(){
 auto add=[&](int a,int b){if(a>b)swap(a,b);E[k][0]=a;E[k++][1]=b;adj[a][b]=adj[b][a]=1;};
 for(int i=0;i<10;i++){add(i,(i+1)%10);add(i,10+i);add(10+i,10+(i+2)%10);}
 bool used[N]={};used[0]=true;ord[0]=0;
 for(int d=1;d<N;d++){
  int best=-1,score=-1;
  for(int u=0;u<N;u++)if(!used[u]){
   int j=0;for(int i=0;i<d;i++)j+=adj[u][ord[i]];
   if(j>score||(j==score&&(best<0||u>best))){score=j;best=u;}
  }
  ord[d]=best;used[best]=1;
 }
 f[0]=0;enumerate(1);
 cout<<"COMPLETE_INTEGER_LIPSCHITZ_FUNCTIONS="<<countAll<<"\nFACETS="<<facets<<"\n";
 cout<<"FACET_VERTEX_HIST=";for(int i=0;i<31;i++)if(tight_hist[i])cout<<i<<":"<<tight_hist[i]<<" ";cout<<"\n";
 cout<<"MAX_CENTERED_QUADRATIC_NUMERATOR="<<maxT<<"\nMAXIMIZERS="<<contact<<"\n";
 int dist[N][N];for(int v=0;v<N;v++){
  for(int u=0;u<N;u++)dist[v][u]=99;dist[v][v]=0;
  for(int j=0;j<N;j++)for(auto &e:E){dist[v][e[0]]=min(dist[v][e[0]],dist[v][e[1]]+1);dist[v][e[1]]=min(dist[v][e[1]],dist[v][e[0]]+1);}
 }
 set<array<int,N>> distance_profiles;
 for(int v=0;v<N;v++){array<int,N>a;for(int u=0;u<N;u++)a[u]=dist[v][u]-dist[v][0];distance_profiles.insert(a);}
 cout<<"MAXIMIZERS_ARE_DISTANCE_PROFILES="<<(maximizing==distance_profiles?1:0)<<"\n";
 assert(countAll==14607387LL && facets==3678208LL && maxT==580 && contact==20 && maximizing==distance_profiles);
 assert(tight_hist[19]==411840 && tight_hist[20]==934968 && tight_hist[21]==1103600 && tight_hist[22]==801000 && tight_hist[23]==352440 && tight_hist[24]==74360);
 cout<<"ALL EXACT CHECKS PASSED\n";
}
