// Exhaustive Hamiltonian-cycle exchange enumeration for a 12-vertex graph.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
constexpr int N=12;
const int edges[][2]={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},
{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},
{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}};
int edge_index[N][N], neighbor[N][N],deg[N];
set<uint32_t> cycles;
array<int,N> path;
void enumerate(int at, uint16_t used) {
 if(at==N) {
  if(edge_index[path[N-1]][0]<0 || path[1]>path[N-1])return;
  uint32_t mask=0;
  for(int i=0;i<N;i++) mask |= (1u<<edge_index[path[i]][path[(i+1)%N]]);
  assert(__builtin_popcount(mask)==N);
  cycles.insert(mask);return;
 }
 int v=path[at-1];
 for(int j=0;j<deg[v];j++) {
  int w=neighbor[v][j];
  if(!(used&(1u<<w))){path[at]=w;enumerate(at+1,used|(1u<<w));}
 }
}
int main() {
 for(auto &r:edge_index)for(int &x:r)x=-1;
 for(int k=0;k<24;k++){
  int a=edges[k][0],b=edges[k][1];edge_index[a][b]=edge_index[b][a]=k;
  neighbor[a][deg[a]++]=b;neighbor[b][deg[b]++]=a;
 }
 for(int v=0;v<N;v++)assert(deg[v]==4);
 path[0]=0;enumerate(1,1u);assert(cycles.size()==185);
 vector<uint32_t> cs(cycles.begin(),cycles.end());
 vector<vector<int>> adj(cs.size());
 for(int i=0;i<(int)cs.size();i++) for(int j=0;j<i;j++){
  uint32_t diff=cs[i]^cs[j];
  if(__builtin_popcount(diff)==4){
   assert(__builtin_popcount(cs[i]&~cs[j])==2);
   adj[i].push_back(j);adj[j].push_back(i);
  }
 }
 long long sumdeg=0;map<int,int> dh,eh,ph;int diameter=0,rad=99;
 for(int i=0;i<(int)cs.size();i++){
  dh[adj[i].size()]++;sumdeg+=adj[i].size();
  vector<int> dist(cs.size(),-1);queue<int> q;
  dist[i]=0;q.push(i);int found=0,ex=0;
  while(!q.empty()){
   int u=q.front();q.pop();found++;ex=max(ex,dist[u]);
   for(int v:adj[u])if(dist[v]==-1){dist[v]=dist[u]+1;q.push(v);}
  }
  assert(found==(int)cs.size());
  eh[ex]++;diameter=max(diameter,ex);rad=min(rad,ex);
  for(int j=i+1;j<(int)cs.size();j++)ph[dist[j]]++;
 }
 assert(sumdeg==764 && diameter==9 && rad==6);
 const map<int,int> expectedD={{2,21},{3,48},{4,60},{5,28},{6,6},{7,18},{9,4}};
 const map<int,int> expectedE={{6,12},{7,104},{8,53},{9,16}};
 const map<int,int> expectedP={{1,382},{2,1129},{3,2694},{4,4116},{5,4876},{6,2992},{7,713},{8,110},{9,8}};
 assert(dh==expectedD && eh==expectedE && ph==expectedP);
 cout<<"GRAPH_OK vertices=12 edges=24 degree=4\n";
 cout<<"HAMILTONIAN_OK undirected_cycles="<<cs.size()<<" directed_oriented_cycles="<<2*cs.size()<<"\n";
 cout<<"SWITCH_OK vertices="<<cs.size()<<" edges="<<sumdeg/2<<" connected=1 diameter="<<diameter<<" radius="<<rad<<"\n";
 cout<<"DEGREE_PROFILE_OK";for(auto [d,n]:dh)cout<<" "<<d<<":"<<n;cout<<"\n";
 cout<<"ECCENTRICITY_PROFILE_OK";for(auto [d,n]:eh)cout<<" "<<d<<":"<<n;cout<<"\n";
 cout<<"ALL_PAIRS_OK";for(auto [d,n]:ph)cout<<" "<<d<<":"<<n;cout<<"\n";
 cout<<"ALL_VERIFY_OK\n";
}
