// Exact exhaustive independent verifier: Petersen GP(5,2), path-edge masks.
// Compile: c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt
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
using Path=array<int,10>;
int main(){
  array<array<bool,10>,10> adj{};
  vector<pair<int,int>> edges;
  auto add=[&](int a,int b){if(a>b) swap(a,b); assert(!adj[a][b]); adj[a][b]=adj[b][a]=true; edges.push_back({a,b});};
  for(int i=0;i<5;++i){add(i,(i+1)%5); add(i,i+5);add(i+5,5+(i+2)%5);}
  assert(edges.size()==15);
  map<pair<int,int>,int> label;
  for(int k=0;k<15;++k)label[edges[k]]=k;
  set<Path> all;
  Path path{};
  auto dfs=[&](auto&& self,int depth,int used)->void{
    if(depth==10){Path rev=path;reverse(rev.begin(),rev.end());all.insert(min(path,rev));return;}
    for(int x=0;x<10;++x){if((used&(1<<x))==0 && (depth==0 || adj[path[depth-1]][x])){
      path[depth]=x;self(self,depth+1,used|(1<<x));
    }}
  };
  dfs(dfs,0,0);
  vector<Path> states(all.begin(),all.end());
  assert(states.size()==120);
  vector<uint16_t> masks;
  for(auto& p:states){uint16_t mask=0;
    for(int i=0;i<9;++i){int a=p[i], b=p[i+1];if(a>b)swap(a,b);mask |= (1u<<label.at({a,b}));}
    assert(__builtin_popcount((unsigned)mask)==9);masks.push_back(mask);
  }
  vector<vector<int>> graph(states.size());int num_edges=0;
  // Edge-flip criterion for Hamilton paths: symmetric difference has two edges.
  // No move generation from Posa rotations is used here.
  for(int i=0;i<(int)states.size();++i)for(int j=i+1;j<(int)states.size();++j){
    if(__builtin_popcount((unsigned)(masks[i]^masks[j]))==2){
      graph[i].push_back(j);graph[j].push_back(i);++num_edges;
    }
  }
  assert(num_edges==240);
  for(auto& nbrs:graph) assert(nbrs.size()==4);
  vector<int> shells_expected={1,4,11,25,39,29,11};
  for(int src=0;src<(int)states.size();++src){
    vector<int> d(states.size(),-1);queue<int> Q;d[src]=0;Q.push(src);
    while(!Q.empty()){int u=Q.front();Q.pop();for(int v:graph[u])if(d[v]<0){d[v]=d[u]+1;Q.push(v);}}
    vector<int> shells(7,0);
    for(int x:d){assert(x>=0 && x<=6); ++shells[x];}
    assert(shells==shells_expected);
  }
  // Another numerical check: every nonadjacent endpoint pair supports 4 paths.
  map<pair<int,int>,int> endpoint_counts;
  for(auto &p:states){int a=p[0],b=p[9];if(a>b)swap(a,b);assert(!adj[a][b]);++endpoint_counts[{a,b}];}
  assert(endpoint_counts.size()==30);
  for(auto &kv:endpoint_counts)assert(kv.second==4);
  cout<<"INDEPENDENT_GP_ENUMERATION_OK paths="<<states.size()<<" endpoint_pairs="<<endpoint_counts.size()<<"\n";
  cout<<"INDEPENDENT_EDGE_FLIP_OK edges="<<num_edges<<" degree=4\n";
  cout<<"INDEPENDENT_METRIC_OK shells=1,4,11,25,39,29,11 diameter=6\n";
  cout<<"ALTERNATE_CERTIFICATE_OK\n";
}
