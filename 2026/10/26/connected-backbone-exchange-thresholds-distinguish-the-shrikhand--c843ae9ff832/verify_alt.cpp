// Exhaustive independent checker for fixed-size connected-dominating-set exchanges.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra -o verify_alt verify_alt.cpp
// Run: ./verify_alt
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int N=16, ALL=(1<<N)-1;
using Adjacency=array<int,N>;
Adjacency make_graph(bool shrikhande) {
 Adjacency adj{};
 for(int x=0;x<4;x++) for(int y=0;y<4;y++){
  int u=4*x+y;
  for(int a=0;a<4;a++) for(int b=0;b<4;b++){
   int dx=(a-x+4)%4, dy=(b-y+4)%4;
   bool edge=shrikhande ?
     (dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||
     (dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3)
     : ((a==x || b==y) && u!=4*a+b);
   if(edge) adj[u] |= (1<<(4*a+b));
  }
 }
 return adj;
}
bool cds(int mask, const Adjacency &adj) {
 int neighborhood=mask;
 for(int u=0;u<N;u++) if(mask&(1<<u)) neighborhood |= adj[u];
 if(neighborhood!=ALL) return false;
 int reached=mask&-mask;
 while(true){
  int grow=reached;
  for(int u=0;u<N;u++) if(reached&(1<<u)) grow |= (adj[u]&mask);
  if(grow==reached) return grow==mask;
  reached=grow;
 }
}
struct Reconf {vector<int> states;vector<vector<int>> links;};
Reconf build(const Adjacency &adj,int k) {
 Reconf h;
 for(int mask=1;mask<=ALL;mask++)
  if(__builtin_popcount((unsigned)mask)==k && cds(mask,adj)) h.states.push_back(mask);
 unordered_map<int,int> index;
 for(int i=0;i<(int)h.states.size();i++) index[h.states[i]]=i;
 h.links.resize(h.states.size());
 for(int i=0;i<(int)h.states.size();i++) {
  int s=h.states[i];
  for(int a=0;a<N;a++) if(s&(1<<a))
   for(int b=0;b<N;b++) if(!(s&(1<<b))) {
    int t=s^(1<<a)^(1<<b);
    auto it=index.find(t);
    if(it!=index.end()) h.links[i].push_back(it->second);
   }
  sort(h.links[i].begin(),h.links[i].end());
  h.links[i].erase(unique(h.links[i].begin(),h.links[i].end()),h.links[i].end());
 }
 return h;
}
int main() {
 for(int mode=0;mode<2;mode++) {
  bool is_sh=(mode==0);string tag=is_sh?"SHRIKHANDE":"ROOK";
  Adjacency a=make_graph(is_sh);
  for(int u=0;u<N;u++)assert(__builtin_popcount((unsigned)a[u])==6);
  for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)
    assert(__builtin_popcount((unsigned)(a[u]&a[v]))==2);
  for(int k=1;k<=6;k++) {
   Reconf h=build(a,k);
   int expected_count=is_sh ? (k==4?32:k==5?672:k==6?4064:0)
                            : (k==4?8:k==5?384:k==6?3744:0);
   assert((int)h.states.size()==expected_count);
   if(k<4) continue;
   int n=h.states.size(), edges=0;
   for(auto &p:h.links)edges+=(int)p.size();
   assert(edges%2==0);edges/=2;
   int expected_edges=is_sh ? (k==4?0:k==5?5136:74304)
                            : (k==4?0:k==5?2112:63024);
   assert(edges==expected_edges);
   vector<int> comp(n,-1),comps;
   for(int i=0;i<n;i++)if(comp[i]<0){
    int id=comps.size(),size=0;
    queue<int> q;q.push(i);comp[i]=id;
    while(!q.empty()){
     int u=q.front();q.pop();size++;
     for(int v:h.links[u])if(comp[v]<0){comp[v]=id;q.push(v);}
    }
    comps.push_back(size);
   }
   sort(comps.begin(),comps.end());
   if(k==4)assert((int)comps.size()==expected_count && comps[0]==1);
   if(k==5 && is_sh)assert(comps==vector<int>{672});
   if(k==5 && !is_sh)assert((comps==vector<int>{192,192}));
   if(k==6)assert(comps==vector<int>{expected_count});
   if(k==5) {
    array<int,32> freq{};
    for(int s=0;s<n;s++){
     vector<int> dist(n,-1);queue<int> q;q.push(s);dist[s]=0;int ecc=0;
     while(!q.empty()){
      int u=q.front();q.pop();
      for(int v:h.links[u])if(dist[v]<0){dist[v]=dist[u]+1;
         ecc=max(ecc,dist[v]);q.push(v);}
     }
     freq[ecc]++;
    }
    if(is_sh)assert(freq[5]==672);
    else assert(freq[6]==96 && freq[7]==288);
    for(int d=0;d<32;d++)if(d!=5 && (is_sh || (d!=6 && d!=7)))
      assert(freq[d]==0);
   }
   cout<<tag<<" SIZE="<<k<<" STATES="<<n<<" EDGES="<<edges
       <<" COMPONENTS="<<comps.size()<<"\n";
  }
 }
 cout<<"INDEPENDENT_VERIFY_OK\n";
}
