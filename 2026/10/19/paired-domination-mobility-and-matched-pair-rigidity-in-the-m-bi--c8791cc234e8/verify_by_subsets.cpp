// Exhaustive verification by vertex subsets and recursive perfect matching.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
 const int n=16, FULL=(1<<n)-1;
 array<int,n> adj{};
 vector<pair<int,int>> edges;
 auto add=[&](int a,int b){if(a>b)swap(a,b);if(adj[a]&(1<<b))return;adj[a]|=1<<b;adj[b]|=1<<a;edges.emplace_back(a,b);};
 for(int i=0;i<8;i++){add(i,(i+1)%8);add(i,8+i);add(8+i,8+(i+3)%8);}
 sort(edges.begin(),edges.end());
 array<int,n> cl{};for(int i=0;i<n;i++)cl[i]=adj[i]|(1<<i);
 vector<int> pm(1<<n,-1);pm[0]=1;
 auto has_pm=[&](auto&& self,int m)->bool{
  if(pm[m]>=0)return pm[m];
  int u=__builtin_ctz((unsigned)m);int rest=m^(1<<u);int choices=rest&adj[u];
  while(choices){int v=__builtin_ctz((unsigned)choices);choices&=choices-1;
    if(self(self,rest^(1<<v)))return pm[m]=1;}
  return pm[m]=0;
 };
 vector<int> mins; map<int,int> cnt;
 for(int mask=1;mask<=FULL;mask++){
  int k=__builtin_popcount((unsigned)mask);
  if(k>8 || (k&1))continue;
  int cov=0;for(int v=0;v<n;v++)if(mask>>v&1)cov|=cl[v];
  if(cov==FULL && has_pm(has_pm,mask)){cnt[k]++;if(k==8)mins.push_back(mask);}
 }
 sort(mins.begin(),mins.end());assert(cnt[2]==0&&cnt[4]==0&&cnt[6]==0&&cnt[8]==684);
 int z=mins.size();
 vector<vector<int>> TJ(z),PE(z),STRICT(z);
 long long edgesTJ=0,edgesPE=0,edgesStrict=0;vector<int> induced(z,0);
 int slideEdges=0;
 for(int i=0;i<z;i++)for(auto [u,v]:edges)if((mins[i]&(1<<u))&&(mins[i]&(1<<v)))induced[i]++;
 for(int i=0;i<z;i++)for(int j=i+1;j<z;j++){
  int left=mins[i]&~mins[j],right=mins[j]&~mins[i];int s=__builtin_popcount((unsigned)left);
  if(s==1 && __builtin_popcount((unsigned)right)==1){
   TJ[i].push_back(j);TJ[j].push_back(i);edgesTJ++;
   int u=__builtin_ctz((unsigned)left),v=__builtin_ctz((unsigned)right);
   if(adj[u]>>v&1)slideEdges++;
  }
  if(s==2 && __builtin_popcount((unsigned)right)==2 && has_pm(has_pm,left) && has_pm(has_pm,right)){
   PE[i].push_back(j);PE[j].push_back(i);edgesPE++;
   int remaining=mins[i]&mins[j];
   if(has_pm(has_pm,remaining)){STRICT[i].push_back(j);STRICT[j].push_back(i);edgesStrict++;}
  }
 }
 auto graph_stats=[&](const vector<vector<int>>& G){
  map<int,int> compSizes,eccs; vector<bool> visited(z,false);
  for(int a=0;a<z;a++)if(!visited[a]){
   vector<int> queue={a};visited[a]=true;
   for(size_t at=0;at<queue.size();at++)for(int b:G[queue[at]])if(!visited[b]){visited[b]=true;queue.push_back(b);}
   compSizes[(int)queue.size()]++;
  }
  for(int a=0;a<z;a++){
   vector<int> dist(z,-1),q={a};dist[a]=0;
   for(size_t at=0;at<q.size();at++)for(int b:G[q[at]])if(dist[b]<0){dist[b]=dist[q[at]]+1;q.push_back(b);}
   int ecc=-1;if(q.size()>1)ecc=*max_element(dist.begin(),dist.end());eccs[ecc]++;
  }
  return make_pair(compSizes,eccs);
 };
 auto component_profile=[&](const vector<vector<int>>& G){
  map<int,map<int,int>> profiles;
  vector<int> visited(z,0);
  for(int a=0;a<z;a++)if(!visited[a]){
    vector<int> C={a};visited[a]=1;
    for(size_t idx=0;idx<C.size();idx++)for(int v:G[C[idx]])if(!visited[v]){visited[v]=1;C.push_back(v);}
    for(int start:C){
      vector<int> dist(z,-1),q={start};dist[start]=0;
      for(size_t idx=0;idx<q.size();idx++)for(int v:G[q[idx]])if(dist[v]<0){dist[v]=dist[q[idx]]+1;q.push_back(v);}
      int e=C.size()==1?-1:*max_element(dist.begin(),dist.end());
      profiles[(int)C.size()][e]++;
    }
  }
  return profiles;
 };
 auto [jC,jE]=graph_stats(TJ);auto[pC,pE]=graph_stats(PE);auto[sC,sE]=graph_stats(STRICT);
 assert((component_profile(TJ)==map<int,map<int,int>>{{684,{{6,216},{7,432},{8,36}}}}));
 assert((component_profile(PE)==map<int,map<int,int>>{{1,{{-1,54}}},{630,{{6,630}}}}));
 assert((component_profile(STRICT)==map<int,map<int,int>>{{1,{{-1,54}}},{30,{{4,30}}},{168,{{9,96},{10,72}}},{432,{{9,192},{10,240}}}}));
 assert(edgesTJ==3504&&edgesPE==2016&&edgesStrict==1392&&slideEdges==0);
 assert((jC==map<int,int>{{684,1}}));
 assert((jE==map<int,int>{{6,216},{7,432},{8,36}}));
 assert((pC==map<int,int>{{1,54},{630,1}}));
 assert((pE==map<int,int>{{-1,54},{6,630}}));
 assert((sC==map<int,int>{{1,54},{30,1},{168,1},{432,1}}));
 assert((sE==map<int,int>{{-1,54},{4,30},{9,288},{10,312}}));
 for(int i=0;i<z;i++)assert((induced[i]==4)==PE[i].empty());
 // Detect the bipartition independently by breadth-first coloring.
 array<int,n> c; c.fill(-1);vector<int> q={0}; c[0]=0;
 for(size_t x=0;x<q.size();x++)for(int v=0;v<n;v++)if(adj[q[x]]>>v&1){
  if(c[v]<0){c[v]=c[q[x]]^1;q.push_back(v);}else assert(c[v]!=(c[q[x]]));
 }
 assert(q.size()==16);
 for(int m:mins){int num=0;for(int i=0;i<n;i++)if((m>>i&1)&&c[i]==1)num++;assert(num==4);}
 cout<<"vertices=16 edges=24 gamma_pr=8 optima=684 sizes2_4_6=0\n";
 cout<<"jump_edges=3504 jump_component_sizes=684 jump_eccentricities=6:216,7:432,8:36\n";
 cout<<"slides=0 pair_edges=2016 pair_component_sizes=630,1x54 pair_eccentricities=6:630,isolated:54\n";
 cout<<"strict_partner_relocation_edges=1392 components=432,168,30,1x54 eccentricities=4:30,9:288,10:312,isolated:54\n";
 cout<<"exactly_54_induced_4K2_optima_are_pair_relocation_isolates=YES\n";
 cout<<"VERIFY_OK\n";
}
