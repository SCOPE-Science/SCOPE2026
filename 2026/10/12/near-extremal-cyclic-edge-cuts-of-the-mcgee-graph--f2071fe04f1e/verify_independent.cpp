// Independent census: O(2^24) boundary recurrence and disjoint-set cycle tests.
// Build: g++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
// Run: ./verify_independent (reads cut_masks.csv produced by verify_cuts).
#include <bits/stdc++.h>
using namespace std;
static const int N=24;static const uint32_t ALL=(1u<<N)-1;
int main(){
 vector<pair<int,int>> edges;int shifts[]={-12,7,-7};
 set<pair<int,int>> unique_edges;
 for(int v=0;v<N;v++)for(int u:{(v+1)%N,(v+N+shifts[v%3])%N}){
  unique_edges.insert({min(u,v),max(u,v)});
 }
 edges.assign(unique_edges.begin(),unique_edges.end());
 array<uint32_t,N> adj{};for(auto [u,v]:edges){adj[u]|=1u<<v;adj[v]|=1u<<u;}
 // Adding a new vertex changes the cut by degree minus twice its old neighbors.
 vector<uint8_t> boundary(1u<<N,0);
 for(uint32_t m=1;m<=ALL;m++){
  int v=__builtin_ctz(m);uint32_t q=m&(m-1);
  int b=(int)boundary[q]+3-2*__builtin_popcount(q&adj[v]);
  if(b<0||b>36)throw runtime_error("invalid recurrence");
  boundary[m]=(uint8_t)b;
 }
 // DSU component cycle test, independent of DFS used by verify_cuts.
 auto cyclic=[&](uint32_t mask)->bool{
  array<int,N> parent{}, nv{}, ne{};
  for(int i=0;i<N;i++){parent[i]=i;nv[i]=(mask>>i)&1;}
  auto root=[&](int x){while(parent[x]!=x)x=parent[x]=parent[parent[x]];return x;};
  for(auto [u,v]:edges)if((mask>>u&1)&&(mask>>v&1)){
   int a=root(u),b=root(v);
   if(a!=b){parent[b]=a;nv[a]+=nv[b];ne[a]+=ne[b];}
   ne[a]++;
  }
  for(int i=0;i<N;i++)if(parent[i]==i&&nv[i]&&ne[i]>=nv[i])return true;
  return false;
 };
 set<uint32_t> found;map<int,int> counts;map<int,map<int,int>> partition;
 for(uint32_t m=1;m<ALL;m+=2){
  int b=boundary[m];if(b>8)continue;
  if(!cyclic(m)||!cyclic(ALL^m))continue;
  uint32_t other=ALL^m;
  uint32_t small=__builtin_popcount(m)<__builtin_popcount(other)?m:(__builtin_popcount(m)>__builtin_popcount(other)?other:min(m,other));
  if(!found.insert(small).second)throw runtime_error("duplicate unordered cut");
  counts[b]++;partition[b][__builtin_popcount(small)]++;
 }
 map<int,int> expected={{7,32},{8,362}};
 if(counts!=expected||partition[8]!=map<int,int>({{8,258},{10,80},{12,24}}))throw runtime_error("independent counts failed");
 ifstream f("cut_masks.csv");string line;getline(f,line);set<uint32_t> written;
 while(getline(f,line)){
  if(line.empty())continue;int pos=line.find(',');
  uint32_t m=(uint32_t)stoul(line.substr(0,pos));
  if(!written.insert(m).second)throw runtime_error("duplicate certificate");
 }
 if(found!=written)throw runtime_error("enumerators disagree on cut masks");
 cout<<"VERIFY_INDEPENDENT_OK recurrence_masks="<<(1u<<N)<<" cut7=32 cut8=362\n";
 cout<<"VERIFY_INDEPENDENT_OK cut8_partition=8+16:258,10+14:80,12+12:24 exact_mask_equality=true\n";
}
