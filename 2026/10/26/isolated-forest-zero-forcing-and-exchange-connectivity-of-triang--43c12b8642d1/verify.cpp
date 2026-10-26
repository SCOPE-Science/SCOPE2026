// Reproducible finite checks for the zero-forcing forest correspondence
// on triangular graphs, using only the C++17 standard library.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
using u64 = unsigned long long;
struct DSU {
 vector<int> p;
 DSU(int n):p(n){iota(p.begin(),p.end(),0);}
 int root(int x){return p[x]==x?x:p[x]=root(p[x]);}
 bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}
};
u64 choose(int n,int k){if(k<0||k>n)return 0;u64 c=1;for(int i=1;i<=k;i++)c=c*(n+1-i)/i;return c;}
u64 treecount(int n){if(n<=1)return 1;u64 ans=1;for(int i=0;i<n-2;i++)ans*=n;return ans;}
// Acyclicity and presence of an isolated vertex in the graph of white edges.
bool forest_isolate(uint32_t white,int n,const vector<pair<int,int>>& ed){
 DSU d(n);int degree[10]={};bool cycle=false;
 for(int e=0;e<(int)ed.size();e++)if((white>>e)&1u){auto [a,b]=ed[e];degree[a]++;degree[b]++;if(!d.join(a,b))cycle=true;}
 bool isolated=false;for(int i=0;i<n;i++)if(degree[i]==0)isolated=true;
 return isolated && !cycle;
}
// Standard line-graph zero forcing, all simultaneously available forces per round.
bool zero_force_round(uint32_t white,const vector<uint32_t>& adj,uint32_t all){
 uint32_t blue=all^white;
 while(white){uint32_t add=0,bs=blue;
  while(bs){int v=__builtin_ctz(bs);bs&=bs-1;uint32_t w=adj[v]&white;if(w && !(w&(w-1)))add|=w;}
  if(!add)return false;
  blue|=add;white&=~add;
 }
 return true;
}
// Chronological forcing, with one legal move at a time and a different schedule.
bool zero_force_serial(uint32_t white,const vector<uint32_t>& adj,uint32_t all){
 uint32_t blue=all^white;
 while(white){bool moved=false;
  for(int v=(int)adj.size()-1;v>=0;v--)if((blue>>v)&1u){
   uint32_t w=adj[v]&white;if(w && !(w&(w-1))){white^=w;blue|=w;moved=true;break;}
  }
  if(!moved)return false;
 }
 return true;
}
vector<vector<u64>> forest_counts(int maxn,bool allow_singletons){
 vector<vector<u64>> f(maxn+1,vector<u64>(maxn+1));f[0][0]=1;
 for(int n=1;n<=maxn;n++)for(int s=allow_singletons?1:2;s<=n;s++){
  u64 part=choose(n-1,s-1)*treecount(s);
  for(int k=s-1;k<=n-1;k++)f[n][k]+=part*f[n-s][k-s+1];
 }
 return f;
}
int main(){
 auto all_f=forest_counts(7,true),no_iso_f=forest_counts(7,false);
 for(int n=3;n<=7;n++){
  vector<pair<int,int>> edges;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edges.push_back({a,b});
  const int N=edges.size();const uint32_t all=(1u<<N)-1;
  vector<uint32_t> adj(N);
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){
   auto [a,b]=edges[i];auto [c,d]=edges[j];
   if(a==c||a==d||b==c||b==d)adj[i]|=1u<<j;
  }
  vector<u64> counted(N+1,0);int max_white=-1;
  vector<uint32_t> opt;
  for(uint32_t w=0;w<=all;w++){
   bool predicted=forest_isolate(w,n,edges);
   bool observed=zero_force_round(w,adj,all);
   if(observed!=predicted){cerr<<"Mismatch n="<<n<<" white="<<w<<"\n";return 1;}
   if(n<=6){bool chronological=zero_force_serial(w,adj,all);if(chronological!=observed)return 2;}
   if(observed){int k=__builtin_popcount(w);counted[k]++;
     if(k>max_white){max_white=k;opt.clear();}
     if(k==max_white)opt.push_back(w);
   }
  }
  if(max_white!=n-2 || opt.size()!=n*treecount(n-1))return 3;
  for(int k=0;k<=N;k++)if(counted[k]!=(k<=n-1?all_f[n][k]-no_iso_f[n][k]:0)){
   cerr<<"EGF coefficient mismatch n="<<n<<" k="<<k<<"\n";return 4;
  }
  cout<<"n="<<n<<" vertices="<<N<<" minimum="<<N-(n-2)
    <<" minima="<<opt.size()<<" white_edge_coefficients=";
  for(int k=0;k<=n-2;k++)cout<<(k?",":"")<<counted[k];
  cout<<" VERIFY_OK\n";
  if(n<=6){
   set<uint32_t> states(opt.begin(),opt.end());
   auto isolated_label=[&](uint32_t w){
     int degrees[10]={};for(int e=0;e<N;e++)if((w>>e)&1u){degrees[edges[e].first]++;degrees[edges[e].second]++;}
     int iso=-1;for(int v=0;v<n;v++)if(!degrees[v]){if(iso>=0)return -2;iso=v;}
     return iso;
   };
   u64 cross_edges=0;
   vector<uint32_t> que;
   set<uint32_t> seen;que.push_back(opt.front());seen.insert(opt.front());
   for(size_t head=0;head<que.size();head++){
    uint32_t w=que[head];
    for(int e=0;e<N;e++)if(w>>e&1u)for(int f=0;f<N;f++)if(!(w>>f&1u)){
      uint32_t t=(w^(1u<<e))|(1u<<f);
      if(states.count(t)&&seen.insert(t).second)que.push_back(t);
    }
   }
   if(seen.size()!=states.size())return 5;
   for(auto w:opt)for(int e=0;e<N;e++)if(w>>e&1u)for(int f=0;f<N;f++)if(!(w>>f&1u)){
     uint32_t t=(w^(1u<<e))|(1u<<f);
     if(w<t && states.count(t) && isolated_label(w)!=isolated_label(t))cross_edges++;
   }
   u64 expected_cross=choose(n,2);for(int k=0;k<n-2;k++)expected_cross*=n-2;
   if(cross_edges!=expected_cross){cerr<<"Cross-fibre mismatch "<<n<<" "<<cross_edges<<" vs "<<expected_cross<<"\n";return 6;}
   cout<<"  reconfiguration_connected="<<seen.size()<<" cross_fibre_edges="<<cross_edges<<" VERIFY_OK\n";
  }
 }
 cout<<"ALL_VERIFY_OK\n";
}
