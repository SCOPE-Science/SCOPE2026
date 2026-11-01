// Independent exhaustive verification of one-leaf corona open-neighborhood NOR dynamics.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct Point {int a,l; bool operator==(const Point& z) const{return a==z.a && l==z.l;}};
static Point advance(Point x,const vector<int>& neigh){
 int n=neigh.size(),mask=(1<<n)-1, y=0;
 for(int i=0;i<n;i++)if(!(x.l&(1<<i))&&!(x.a&neigh[i]))y|=(1<<i);
 return {y,mask^x.a};
}
static bool across(int a,int b,const vector<int>& adj){
 for(size_t i=0;i<adj.size();i++)if((a>>i)&1)if(adj[i]&b)return false;
 return true;
}
static int neighboring(int a,const vector<int>& adj){
 int z=0;for(size_t i=0;i<adj.size();i++)if((a>>i)&1)z|=adj[i];return __builtin_popcount((unsigned)z);
}
int main(){
 uint64_t graphs=0, configs=0, periodic_states=0;
 for(int n=1;n<=5;n++){
  vector<pair<int,int>> edges; for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.emplace_back(i,j);
  for(int em=0;em<(1<<(int)edges.size());em++){
   vector<int> adj(n,0);for(size_t k=0;k<edges.size();k++)if((em>>k)&1){auto [u,v]=edges[k];adj[u]|=1<<v;adj[v]|=1<<u;}
   int N=1<<n;vector<int> fibers(N*N,0);
   for(int a=0;a<N;a++)for(int l=0;l<N;l++){
    Point x{a,l},y=advance(x,adj),z=advance(y,adj),w=advance(z,adj);
    assert(w==y);
    assert(across(y.a,N-1-y.l,adj));
    fibers[y.a*N+y.l]++; configs++;
   }
   uint64_t fixed_basins=0, periodic=0, fixed=0, all_basin=0;
   for(int a=0;a<N;a++)for(int b=0;b<N;b++)if(across(a,b,adj)){
    Point p{a,N-1-b},q{b,N-1-a};
    assert(advance(p,adj)==q);
    assert(advance(q,adj)==p);
    assert(fibers[p.a*N+p.l] == (1<<neighboring(b,adj)));
    periodic++;
    if(a==b){fixed++;fixed_basins+=fibers[p.a*N+p.l];}
    all_basin+=fibers[p.a*N+p.l];
   }
   assert(all_basin==(uint64_t)N*N);
   uint64_t weighted=0;for(int a=0;a<N;a++)if(across(a,a,adj))weighted+=1<<neighboring(a,adj);
   assert(weighted==fixed_basins);
   assert((periodic-fixed)%2==0);
   graphs++;periodic_states+=periodic;
  }
 }
 cout<<"All labelled simple base graphs with n=1..5: PASS graphs="<<graphs
     <<" configurations="<<configs<<" periodic-pair-states="<<periodic_states<<"\n";
}
