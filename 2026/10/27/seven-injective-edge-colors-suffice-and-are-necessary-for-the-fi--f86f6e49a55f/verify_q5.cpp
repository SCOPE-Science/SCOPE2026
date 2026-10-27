#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U = uint64_t;
struct Edge {int a,b;};
vector<Edge> edges;
vector<int> cand;
vector<U> comp;
long long calls=0,branches=0;
int max_seen=0;
static int low(U b){return __builtin_ctzll(b);}
static bool linked(int a,int b){return __builtin_popcount((unsigned)(a^b))==1;}
static bool conflict(Edge e,Edge f){
    if(e.a==f.a||e.a==f.b||e.b==f.a||e.b==f.b) return false; // Q_5 has no triangles.
    return linked(e.a,f.a)||linked(e.a,f.b)||linked(e.b,f.a)||linked(e.b,f.b);
}
// Enumerate color classes of compatibility graph. Each class is an independent
// set, so any clique takes at most one vertex from each class.
void greedy_colors(U P,vector<int>& order,vector<int>& bound){
    int c=0;
    while(P){
      ++c; U avail=P;
      while(avail){
         int v=low(avail); U bit=U(1)<<v;
         order.push_back(v);bound.push_back(c);
         P &= ~bit; avail &= ~bit;
         avail &= ~comp[v];
      }
    }
}
// Searches for any clique of size >=12 in the compatibility graph on edges
// allowed alongside a canonical selected edge. A found clique would give an
// open edge packing of size at least 13 in Q_5.
bool has_clique_12(U P,int depth){
   ++calls;max_seen=max(max_seen,depth);
   if(depth>=12)return true;
   if(!P)return false;
   vector<int> ord,col;greedy_colors(P,ord,col);
   for(int i=(int)ord.size()-1;i>=0;--i){
      if(depth+col[i]<12) return false;
      int v=ord[i];U bit=U(1)<<v;
      if(P&bit){
         ++branches;
         if(has_clique_12(P&comp[v],depth+1)) return true;
         P &= ~bit;
      }
   }
   return false;
}
int main(){
  constexpr int n=5;
  for(int a=0;a<(1<<n);++a)
   for(int i=0;i<n;++i){int b=a^(1<<i);if(a<b)edges.push_back({a,b});}
  assert(edges.size()==80);
  Edge anchor={0,1};
  for(int k=0;k<(int)edges.size();++k){Edge e=edges[k];if(e.a==0&&e.b==1)continue;if(!conflict(anchor,e))cand.push_back(k);}
  int m=cand.size();assert(m<=64);
  comp.assign(m,0);
  for(int a=0;a<m;++a)
    for(int b=0;b<m;++b)
       if(a!=b&&!conflict(edges[cand[a]],edges[cand[b]])) comp[a] |= U(1)<<b;
  U all=(U(1)<<m)-1;
  bool thirteen=has_clique_12(all,0);
  cout<<"Q5_vertices=32 Q5_edges="<<edges.size()<<" compatible_with_anchor="<<m<<"\n";
  cout<<"clique_search_calls="<<calls<<" branches="<<branches<<" max_depth="<<max_seen<<"\n";
  cout<<"packing_of_13_exists="<<(thirteen?"YES":"NO")<<"\n";
  // Construct a lower-bound certificate, independent of the clique search.
  vector<Edge> witness={{0,16},{3,7},{5,7},{7,23},{9,25},{10,14},{12,14},{14,30},
                        {16,18},{16,20},{25,27},{25,29}};
  assert(witness.size()==12);
  for(auto e:witness)assert(linked(e.a,e.b));
  for(int i=0;i<12;++i)for(int j=i+1;j<12;++j)assert(!conflict(witness[i],witness[j]));
  cout<<"witness_size="<<witness.size()<<" all_edges_valid_and_pairwise_unconflicted=YES\n";
  return thirteen?1:0;
}
