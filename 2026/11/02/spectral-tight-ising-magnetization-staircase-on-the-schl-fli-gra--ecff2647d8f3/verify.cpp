// Finite certificate for the 27-vertex Schlaefli skew-line graph.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
constexpr int N=27;
constexpr uint32_t LIMIT=(1u<<N);
struct Graph {array<uint32_t,N> adj{};vector<pair<int,int>> edges;};
Graph make_graph(){
  vector<pair<int,int>> pairs;
  for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)pairs.emplace_back(i,j);
  // 0..5: E_i, 6..11: B_i, 12..26: C_ij in increasing pairs i<j.
  // Two line classes meet according to the corresponding intersection products.
  auto meet=[&](int u,int v)->bool{
    int cu=u<6?0:u<12?1:2;
    int cv=v<6?0:v<12?1:2;
    if(cu<2 && cv<2) return cu!=cv && u%6!=v%6;
    if(cu<2 && cv==2){auto p=pairs.at(v-12);return p.first==u%6 || p.second==u%6;}
    if(cu==2 && cv<2){auto p=pairs.at(u-12);return p.first==v%6 || p.second==v%6;}
    auto p=pairs.at(u-12),q=pairs.at(v-12);
    return p.first!=q.first && p.first!=q.second && p.second!=q.first && p.second!=q.second;
  };
  Graph g;
  for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
    if(!meet(i,j)){g.adj[i] |=1u<<j;g.adj[j]|=1u<<i;g.edges.emplace_back(i,j);}
  }
  return g;
}
int direct_cut(const Graph&g,uint32_t mask){
 int count=0;
 for(auto [u,v]:g.edges)count+=((mask>>u)^(mask>>v))&1u;
 return count;
}
struct Profile {
 array<int,N+1> best{};
 array<uint64_t,N+1> count{};
 array<uint64_t,N+1> sectors{};
 array<uint32_t,N+1> witness{};
 Profile(){best.fill(-1);}
 void add(int k,int cut,uint32_t mask){
   ++sectors[k];
   if(cut>best[k]){best[k]=cut;count[k]=1;witness[k]=mask;}
   else if(cut==best[k])++count[k];
 }
};
Profile by_gray(const Graph&g){
 Profile out;uint32_t mask=0;int cut=0,k=0;
 for(uint32_t t=0;t<LIMIT;t++){
  if(t){
   int v=__builtin_ctz(t);
   int neigh=__builtin_popcount(g.adj[v]&mask);
   if(mask & (1u<<v)){cut-=16-2*neigh;mask^=1u<<v;--k;}
   else{cut+=16-2*neigh;mask^=1u<<v;++k;}
  }
  if((t%8191)==0 && direct_cut(g,mask)!=cut)throw runtime_error("direct cut mismatch");
  if(__builtin_popcount(mask)!=k)throw runtime_error("Gray weight mismatch");
  out.add(k,cut,mask);
 }
 return out;
}
void visit_recursive(const Graph&g,int i,uint32_t mask,int k,int cut,Profile&out){
 if(i==N){out.add(k,cut,mask);return;}
 visit_recursive(g,i+1,mask,k,cut,out);
 int neigh=__builtin_popcount(mask&g.adj[i]);
 visit_recursive(g,i+1,mask | (1u<<i),k+1,cut+16-2*neigh,out);
}
Profile by_recursion(const Graph&g){Profile out;visit_recursive(g,0,0,0,0,out);return out;}
uint64_t choose(int n,int k){uint64_t c=1;for(int j=1;j<=k;j++)c=c*(n-j+1)/j;return c;}
int ceil_div_signed(int a,int b){assert(b>0);return a>=0?(a+b-1)/b:-((-a)/b);}
int spectral_bound(int k){int t=min(k,N-k);return 16*t-2*ceil_div_signed(t*(t-3),3);}
int main(){
 try{
  auto g=make_graph();
  if(g.edges.size()!=216)throw runtime_error("edge count");
  for(int u=0;u<N;u++){
   if(__builtin_popcount(g.adj[u])!=16 || ((g.adj[u]>>u)&1u))throw runtime_error("degree/loop");
   for(int v=u+1;v<N;v++){
    if(((g.adj[u]>>v)&1u)!=((g.adj[v]>>u)&1u))throw runtime_error("symmetry");
    int com=__builtin_popcount(g.adj[u]&g.adj[v]);
    int required=((g.adj[u]>>v)&1u)?10:8;
    if(com!=required)throw runtime_error("SRG parameters");
   }
  }
  auto a=by_gray(g);
  auto b=by_recursion(g);
  constexpr int expected_best[]={0,16,32,48,60,72,84,92,100,108,112,116,120,120};
  constexpr uint64_t expected_count[]={1,27,135,45,2160,6750,1080,42120,86400,8400,247860,351216,22968,495720};
  constexpr uint32_t certificate[]={0x0000000,0x0000001,0x0000060,0x0001081,0x00000cc,0x00000dc,0x00001f8,0x00001f9,0x00003f3,0x00019db,0x00007ef,0x00007ff,0x0000fff,0x0001fff};
  for(int k=0;k<=N;k++){
    if(a.best[k]!=b.best[k] || a.count[k]!=b.count[k] || a.sectors[k]!=b.sectors[k])throw runtime_error("enumeration disagreement");
    if(a.sectors[k]!=choose(N,k))throw runtime_error("incomplete enumeration");
    if(a.best[k]!=spectral_bound(k))throw runtime_error("spectral sharpness");
    if(a.best[k]!=a.best[N-k] || a.count[k]!=a.count[N-k])throw runtime_error("spin-flip symmetry");
    if(k<=13){
       if(a.best[k]!=expected_best[k] || a.count[k]!=expected_count[k])throw runtime_error("ground counts changed");
       if(__builtin_popcount(certificate[k])!=k || direct_cut(g,certificate[k])!=a.best[k])throw runtime_error("witness check failed");
    }
  }
  // Exact ground-state sectors and coexistence counts for nonnegative h/J.
  auto mass=[&](int lo,int hi){uint64_t s=0;for(int k=lo;k<=hi;k++)s+=a.count[k];return s;};
  if(mass(12,15)!=1037376 || mass(9,12)!=630444 || mass(6,9)!=138000 || mass(3,6)!=10035 || mass(0,3)!=208)
    throw runtime_error("coexistence counts");
  for(int H: {1,5,9,13,17}){
    long e_best=INT64_MAX;int kopt=-1;
    for(int k=0;k<=N;k++){
      long E=216-2*a.best[k]-H*(27-2*k);
      if(E<e_best){e_best=E;kopt=k;}
    }
    int expect=H==1?12:H==5?9:H==9?6:H==13?3:0;
    if(kopt!=expect)throw runtime_error("plateau error");
  }
  cout << "VERIFY_OK vertices=27 edges=216 subsets_per_graph=134217728 independent_enumerations=2\n";
  cout << "k,max_cut,degeneracy,witness_hex\n";
  for(int k=0;k<=13;k++){
   cout << k << "," << a.best[k] << "," << a.count[k] << "," << hex << certificate[k] << dec << "\n";
  }
  cout<<"zero_field=1037376 critical_4=630444 critical_8=138000 critical_12=10035 critical_16=208\n";
 }catch(const exception&e){cerr<<"VERIFY_FAIL "<<e.what()<<"\n";return 1;}
}
