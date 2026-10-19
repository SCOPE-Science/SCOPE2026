// Independent verification using selected-vertex-set dynamic programming.
// Vertex 4*r+c is the pair (r,c) in Z_4 x Z_4.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
constexpr int n = 16, full = (1<<n)-1;
using U = unsigned long long;

int main() {
 for (const string g: {"rook", "shrikhande"}) {
  array<int,n> adj{};
  for (int u=0;u<n;u++) for (int v=0;v<n;v++) if (u!=v) {
   int a=u/4,b=u%4,c=v/4,d=v%4;
   int x=(c-a+4)%4,y=(d-b+4)%4;
   bool edge = g=="rook" ? ((a==c)||(b==d))
       : ((x==1&&y==0)||(x==3&&y==0)||(x==0&&y==1)||
          (x==0&&y==3)||(x==1&&y==1)||(x==3&&y==3));
   if(edge) adj[u]|=(1<<v);
  }
  int num_edges=0;
  for(int u=0;u<n;u++) {
   assert(__builtin_popcount((unsigned)adj[u])==6);
   for(int v=u+1;v<n;v++){
    assert(bool(adj[u]&(1<<v))==bool(adj[v]&(1<<u)));
    assert(__builtin_popcount((unsigned)(adj[u]&adj[v]))==2);
    if(adj[u]&(1<<v))num_edges++;
   }
  }
  assert(num_edges==48);
  for (const string kind: {"closed","open"}) {
   array<int,n> nb{};
   for(int i=0;i<n;i++)nb[i]=adj[i] | (kind=="closed" ? (1<<i) : 0);
   vector<int> covered(1<<n,0);
   for(int mask=1;mask<=full;mask++){
    int low=mask&(-mask),i=__builtin_ctz((unsigned)low);
    covered[mask]=covered[mask^low]|nb[i];
   }
   // Every legal ordering of a selected set reaches the same neighborhood union.
   // dp[mask][k] counts legal length-k orderings of the selected set mask.
   vector<U> dp(1<<n,0);
   dp[0]=1;
   map<int,U> terminal;
   size_t reachable=0;
   for(int mask=0;mask<=full;mask++){
    U c=dp[mask];
    if(!c)continue;
    reachable++;
    if(covered[mask]==full){terminal[__builtin_popcount((unsigned)mask)]+=c;continue;}
    for(int v=0;v<n;v++)if(!(mask&(1<<v)) && ((covered[mask]|nb[v])!=covered[mask]))
       dp[mask|(1<<v)]+=c;
   }
   cout<<g<<" "<<kind<<" selected_states "<<reachable<<" spectrum";
   for(auto [k,c]:terminal)cout<<" "<<k<<":"<<c;
   cout<<"\n";
  }
 }
}
