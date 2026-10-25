#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <cassert>
#include <map>
#include <numeric>
using namespace std;
int n; vector<pair<int,int>> edges; int eidx[16][16]; vector<uint64_t> states;
void triples(vector<int> remaining,uint64_t mask){
 if(remaining.empty()){states.push_back(mask);return;}
 int x=remaining[0];
 for(int j=1;j<(int)remaining.size();++j)for(int k=j+1;k<(int)remaining.size();++k){
  int y=remaining[j],z=remaining[k];
  vector<int> r;
  for(int t=1;t<(int)remaining.size();++t) if(t!=j&&t!=k)r.push_back(remaining[t]);
  int a[3]={x,y,z};
  for(int c=0;c<3;++c){
   uint64_t add=0;
   for(int h=0;h<3;++h) if(h!=c) add|=1ULL<<eidx[a[c]][a[h]];
   triples(r,mask|add);
  }
 }
}
void go(int order){
 n=order;edges.clear();states.clear();
 for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){eidx[a][b]=eidx[b][a]=edges.size(); edges.push_back({a,b});}
 for(int hole=0;hole<n;++hole){vector<int> r;for(int i=0;i<n;++i)if(i!=hole)r.push_back(i);triples(r,0);}
 sort(states.begin(),states.end());
 assert(unique(states.begin(),states.end())==states.end());
 unordered_map<uint64_t,int> ids;ids.reserve(states.size()*2);
 for(int i=0;i<(int)states.size();++i)ids[states[i]]=i;
 vector<vector<int>> adj(states.size());
 for(int i=0;i<(int)states.size();++i){
  uint64_t s=states[i];
  for(int e=0;e<(int)edges.size();++e)if(s&(1ULL<<e)){
   for(int f=0;f<(int)edges.size();++f)if(!(s&(1ULL<<f))){
    auto [a,b]=edges[e];auto [c,d]=edges[f];
    if(a!=c && a!=d && b!=c && b!=d)continue;
    uint64_t t=(s&~(1ULL<<e))|(1ULL<<f);
    auto it=ids.find(t);if(it!=ids.end())adj[i].push_back(it->second);
   }
  }
  sort(adj[i].begin(),adj[i].end());
  adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
  assert(adj[i].size()==static_cast<size_t>(4*(n-1)/3));
 }
 long long twice_edges=0,triangles_times3=0;
 for(int i=0;i<(int)adj.size();++i){
  twice_edges+=adj[i].size();
  for(int a=0;a<(int)adj[i].size();++a)for(int b=a+1;b<(int)adj[i].size();++b){
   int u=adj[i][a],v=adj[i][b];
   if(binary_search(adj[u].begin(),adj[u].end(),v))++triangles_times3;
  }
 }
 vector<int> dist(states.size(),-1);dist[0]=0;queue<int> Q;Q.push(0);
 map<int,int> hist;
 while(!Q.empty()){
  int x=Q.front();Q.pop();++hist[dist[x]];
  for(int y:adj[x])if(dist[y]==-1){dist[y]=dist[x]+1;Q.push(y);}
 }
 assert(hist.size() && (int)states.size()==accumulate(hist.begin(),hist.end(),0,[](int a,const auto &p){return a+p.second;}));
 cout<<"order "<<n<<" states "<<states.size()<<" edges "<<twice_edges/2<<" degree "<<adj[0].size()<<" triangles "<<triangles_times3/3<<" diameter "<<hist.rbegin()->first<<" profile";
 for(auto [d,c]:hist)cout<<" "<<d<<":"<<c;
 cout<<"\n";
}
int main(){go(4);go(7);go(10);}
