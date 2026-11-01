// Exhaustive consistency checks for the recurrent-state criterion of edge majority.
// This program establishes only its stated finite test instances; the general proof
// appears in RESULT.md. Standard C++17, no external dependencies.
#include <iostream>
#include <vector>
#include <utility>
#include <cassert>
#include <algorithm>
#include <cstdint>
using namespace std;
using Edge=pair<int,int>;
struct G {int n;vector<Edge> edges;};
G complete(int n){G g{n,{}};for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)g.edges.emplace_back(a,b);return g;}
G bowtie(){return {5,{{0,1},{1,2},{2,0},{0,3},{3,4},{4,0}}};}
G cube(){G g{8,{}};for(int a=0;a<8;a++)for(int j=0;j<3;j++){int b=a^(1<<j);if(a<b)g.edges.emplace_back(a,b);}return g;}
G petersen(){G g{10,{}};for(int i=0;i<5;i++){g.edges.emplace_back(i,(i+1)%5);g.edges.emplace_back(i,5+i);g.edges.emplace_back(5+i,5+(i+2)%5);}return g;}
void verify(const char* label, const G&g){
 int m=g.edges.size();assert(m<=21);
 vector<int> degree(g.n,0);
 for(auto [a,b]:g.edges){degree[a]++;degree[b]++;}
 for(auto [a,b]:g.edges)assert((degree[a]&1)==(degree[b]&1));
 vector<uint64_t> nei(m,0);for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){auto [a,b]=g.edges[i];auto [c,d]=g.edges[j];if(a==c||a==d||b==c||b==d)nei[i]|=1ULL<<j;}
 int64_t fixed=0,two_states=0;
 for(uint64_t s=0;s<(1ULL<<m);s++){
  auto step=[&](uint64_t x){uint64_t y=0;for(int j=0;j<m;j++){int ones=__builtin_popcountll(x&nei[j]),N=__builtin_popcountll(nei[j]);int bit=(x>>j)&1;if(2*ones>N)bit=1;else if(2*ones<N)bit=0;y|=(uint64_t)bit<<j;}return y;};
  uint64_t t=step(s);
  bool actual=(step(t)==s);
  vector<int> h(g.n,0),ht(g.n,0),dgz(g.n,0),dgp(g.n,0);
  bool structural=true;uint64_t expected=0;
  for(int j=0;j<m;j++){auto [a,b]=g.edges[j];h[a]+=(s>>j)&1;h[b]+=(s>>j)&1;ht[a]+=(t>>j)&1;ht[b]+=(t>>j)&1;}
  for(int j=0;j<m;j++){
   auto [a,b]=g.edges[j];int s0=(degree[a]+degree[b])/2;int q=h[a]+h[b];int bit=(s>>j)&1;
   if(q>s0){dgp[a]++;dgp[b]++;if(!bit)structural=false;expected|=1ULL<<j;}
   else if(q<s0){if(bit)structural=false;}
   else {dgz[a]++;dgz[b]++;expected|=(uint64_t)(1-bit)<<j;}
  }
  for(int v=0;v<g.n;v++){if(2*(h[v]-dgp[v])!=dgz[v])structural=false;}
  if(actual!=structural){cerr<<"FAILED "<<label<<" state "<<s<<" actual "<<actual<<" structural "<<structural<<"\n";abort();}
  if(actual){assert(expected==t);assert(h==ht);if(s==t)fixed++;else two_states++;}
 }
 assert(two_states%2==0);
 cout<<label<<" states="<<(1ULL<<m)<<" fixed="<<fixed<<" primitive_2_orbits="<<two_states/2<<" criterion=verified\n";
}
int main(){for(int n=3;n<=7;n++){auto g=complete(n);string label="K"+to_string(n);verify(label.c_str(),g);}verify("CUBE_Q3",cube());verify("PETERSEN",petersen());verify("TWO_TRIANGLES_SHARED_VERTEX",bowtie());
 // On P3, line graph is K2. An edge-bit configuration (1,0) swaps to (0,1).
 G g{3,{{0,1},{1,2}}};vector<int>d={1,2,1};assert((d[0]&1)!=(d[1]&1));
 cout<<"MIXED_PARITY_COUNTEREXAMPLE P3: edge_bits_10 <-> edge_bits_01, incidence_counts_change\n";
 cout<<"VERIFICATION_OK\n";
}
