// Exact enumeration of perfect Roman dominating functions on M(K_{2,n}).
// Vertices: a0,a1,b0,...,b(n-1),e(0,0),...,e(1,n-1).
// Compile: g++ -O3 -std=c++17 verify_middle_K2n.cpp -o verifier
// Run: ./verifier
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
#include <limits>
using namespace std;
struct Graph {int n,N; vector<uint64_t> adj;};
Graph make_graph(int n){
 Graph g{n,3*n+2,vector<uint64_t>(3*n+2,0)};
 auto add=[&](int u,int v){g.adj[u]|=uint64_t(1)<<v;g.adj[v]|=uint64_t(1)<<u;};
 for(int i=0;i<2;++i)for(int j=0;j<n;++j){
  int e=2+n+i*n+j; add(i,e);add(2+j,e);
  for(int jj=0;jj<j;++jj)add(e,2+n+i*n+jj);
  if(i==1)add(e,2+n+j);
 }
 return g;
}
pair<int,uint64_t> by_two_support(const Graph&g){
 int best=numeric_limits<int>::max();uint64_t num=0;
 uint64_t total=uint64_t(1)<<g.N;
 for(uint64_t t=0;t<total;++t){
  uint64_t one=0,many=0;
  for(uint64_t bits=t;bits;bits&=bits-1){
   int v=__builtin_ctzll(bits);
   uint64_t next_many=one & g.adj[v];
   one^=g.adj[v];many|=next_many;one&=~many;
  }
  int weight=g.N+__builtin_popcountll(t)-__builtin_popcountll(one&~t);
  if(weight<best){best=weight;num=0;}
  if(weight==best)++num;
 }
 return {best,num};
}
pair<int,uint64_t> by_ternary_labels(const Graph&g){
 int best=numeric_limits<int>::max();uint64_t num=0,tot=1;
 for(int v=0;v<g.N;++v)tot*=3;
 vector<int> f(g.N);
 for(uint64_t code=0;code<tot;++code){
  uint64_t x=code,two=0;int w=0;
  for(int v=0;v<g.N;++v){f[v]=x%3;x/=3;w+=f[v];if(f[v]==2)two|=uint64_t(1)<<v;}
  if(w>best)continue;
  bool valid=true;
  for(int v=0;v<g.N;++v)if(f[v]==0 && __builtin_popcountll(g.adj[v]&two)!=1){valid=false;break;}
  if(valid){if(w<best){best=w;num=0;}if(w==best)++num;}
 }
 return {best,num};
}
int main(){uint64_t total_masks=0;
 for(int n=1;n<=8;++n){
  Graph g=make_graph(n); auto found=by_two_support(g);
  int exp_weight=n==1?3:n==2?5:n+4;
  uint64_t exp_count=n==1?2:n==2?4:n==3?22:uint64_t(n+1)*(n+1);
  if(found.first!=exp_weight || found.second!=exp_count){cerr<<"FAILED n="<<n<<" got "<<found.first<<","<<found.second<<"\n";return 1;}
  if(n<=4){auto independent=by_ternary_labels(g);if(independent!=found){cerr<<"TERNARY_MISMATCH n="<<n<<"\n";return 2;}}
  total_masks+=uint64_t(1)<<g.N;
  cout<<"n="<<n<<" optimum="<<found.first<<" optimal_labelings="<<found.second<<"\n";
 }
 cout<<"VERIFICATION_OK n=1..8 total_two_support_subsets="<<total_masks<<" ternary_crosscheck=1..4\n";
}
