// Exact vertex-bipartition enumeration of cycle-separating edge cuts
// in the 24-vertex cubic graph with LCF [-12,7,-7]^8.
// Build: g++ -O3 -std=c++17 verify_cuts.cpp -o verify_cuts
// Run: ./verify_cuts (writes cut_masks.csv in current directory).
#include <bits/stdc++.h>
using namespace std;
static constexpr int N=24;
static constexpr uint32_t ALL=(1u<<N)-1;
static vector<pair<int,int>> E;
static array<uint32_t,N> adj{};
static vector<pair<int,int>> components(uint32_t mask){
 vector<pair<int,int>> out;
 while(mask){
  int start=__builtin_ctz(mask);uint32_t reached=0,fringe=1u<<start;
  int nv=0, twice_ne=0;
  while(fringe){
   int u=__builtin_ctz(fringe);fringe&=fringe-1;
   uint32_t bit=1u<<u;if(reached&bit)continue;
   reached|=bit;++nv;twice_ne+=__builtin_popcount(adj[u]&mask);
   fringe|=adj[u]&mask&~reached;
  }
  out.push_back({nv,twice_ne/2});mask&=~reached;
 }
 return out;
}
static bool has_cycle(uint32_t mask){
 for(auto [v,e]:components(mask))if(e>=v)return true;
 return false;
}
static string side_type(uint32_t mask){
 const int nv=__builtin_popcount(mask);
 int ne=0;vector<int> degrees;
 for(int i=0;i<N;i++)if((mask>>i)&1){int d=__builtin_popcount(adj[i]&mask);degrees.push_back(d);ne+=d;}
 ne/=2;sort(degrees.begin(),degrees.end());
 if(nv==7&&ne==7&&degrees==vector<int>(7,2))return "C7";
 if(nv==8&&ne==8){
  if(degrees==vector<int>(8,2))return "C8";
  if(degrees==vector<int>({1,2,2,2,2,2,2,3}))return "C7+leaf";
 }
 if(nv==10&&ne==11&&degrees==vector<int>({2,2,2,2,2,2,2,2,3,3}))return "theta(3,4,4)";
 if(nv==12&&ne==14&&degrees==vector<int>({2,2,2,2,2,2,2,2,3,3,3,3}))return "K4-subdivision";
 throw runtime_error("unexpected side topology");
}
int main(){
 set<pair<int,int>> s;auto add=[&](int u,int v){if(u>v)swap(u,v);s.insert({u,v});};
 int step[3]={-12,7,-7};
 for(int i=0;i<N;i++){add(i,(i+1)%N);add(i,(i+N+step[i%3])%N);}
 E.assign(s.begin(),s.end());if(E.size()!=36)throw runtime_error("edge count");
 for(auto [u,v]:E){adj[u]|=1u<<v;adj[v]|=1u<<u;}
 for(int u=0;u<N;u++)if(__builtin_popcount(adj[u])!=3)throw runtime_error("not cubic");
 ofstream out("cut_masks.csv",ios::binary);out<<"mask,cut,small_size,small_edges,components_small,components_large\n";
 map<int,int> cuts;map<string,int> types;long long tested=0;
 for(uint32_t m=1;m<ALL;m+=2){ // Include vertex 0: one side per unordered partition.
  ++tested;int boundary=0;
  for(auto [u,v]:E)boundary+= ((m>>u)^(m>>v))&1;
  if(boundary>8)continue;
  uint32_t other=ALL^m;
  if(!has_cycle(m)||!has_cycle(other))continue;
  uint32_t small;
  int sm=__builtin_popcount(m),so=__builtin_popcount(other);
  if(sm<so)small=m;else if(sm>so)small=other;else small=min(m,other);
  auto ca=components(small),cb=components(ALL^small);
  if(ca.size()!=1||cb.size()!=1)throw runtime_error("cut with >2 components");
  int sz=__builtin_popcount(small),edges=ca[0].second;
  string t=side_type(small);cuts[boundary]++;types[to_string(boundary)+"/"+t]++;
  out<<small<<","<<boundary<<","<<sz<<","<<edges<<","<<ca.size()<<","<<cb.size()<<"\n";
 }
 out.close();
 if(tested!=8388607LL)throw runtime_error("partition count");
 if(cuts.size()!=2||cuts[7]!=32||cuts[8]!=362)throw runtime_error("cut census mismatch");
 map<string,int> goal={{"7/C7",32},{"8/C8",34},{"8/C7+leaf",224},{"8/theta(3,4,4)",80},{"8/K4-subdivision",24}};
 if(types!=goal)throw runtime_error("topology census mismatch");
 cout<<"VERIFY_ENUM_OK tested_unordered_partitions="<<tested<<" cut7="<<cuts[7]<<" cut8="<<cuts[8]<<"\n";
 cout<<"VERIFY_ENUM_OK cut8_types=C8:34,C7+leaf:224,theta(3,4,4):80,K4-subdivision:24\n";
}
