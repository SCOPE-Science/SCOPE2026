// Exhaustive pairwise verification of short alternating-cycle exchanges of cyclic four-bit Gray codes.
// Compile: c++ -std=c++17 -O2 q4_verify_alt.cpp -o q4_verify_alt && ./q4_verify_alt
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using U=uint64_t;
int main(){
 vector<pair<int,int>> edges;int idx[16][16];fill(&idx[0][0],&idx[0][0]+256,-1);
 vector<vector<int>> adj(16);
 for(int u=0;u<16;u++)for(int v=u+1;v<16;v++)if(__builtin_popcount(u^v)==1){idx[u][v]=idx[v][u]=edges.size();edges.emplace_back(u,v);adj[u].push_back(v);adj[v].push_back(u);}
 assert(edges.size()==32);
 vector<U> ham;
 vector<int> path{0};
 auto dfs=[&](auto&& self,int mask)->void{
   if(path.size()==16){
    if(idx[path.back()][0]>=0 && path[1]<path.back()){
     U h=0;for(int k=0;k<16;k++){int a=path[k],b=path[(k+1)%16];h|=U(1)<<idx[a][b];}ham.push_back(h);
    }return;
   }
   for(int w:adj[path.back()])if(!(mask&(1<<w))){path.push_back(w);self(self,mask|(1<<w));path.pop_back();}
 };
 dfs(dfs,1);sort(ham.begin(),ham.end());assert(ham.size()==1344);
 const int N=ham.size();vector<vector<int>> g4(N),g6(N),g46(N);
 int e4=0,e6=0;
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  U z=ham[i]^ham[j];int len=__builtin_popcountll(z);
  if(len!=4&&len!=6)continue;
  int d[16]={0};vector<int> va;
  for(int k=0;k<32;k++)if((z>>k)&1){auto [u,v]=edges[k];d[u]++;d[v]++;}
  bool valid=true;for(int k=0;k<16;k++)if(d[k]!=0&&d[k]!=2)valid=false;
  if(!valid)continue;
  int root=-1;for(int k=0;k<16;k++)if(d[k]){root=k;break;}
  bool seen[16]={0};int cnt=0;queue<int> q;q.push(root);seen[root]=true;
  while(!q.empty()){int u=q.front();q.pop();cnt++;for(int v:adj[u])if(!seen[v] && ((z>>idx[u][v])&1)){seen[v]=true;q.push(v);}}
  if(cnt!=len)continue;
  g46[i].push_back(j);g46[j].push_back(i);
  auto &g=len==4?g4:g6;g[i].push_back(j);g[j].push_back(i);
  (len==4?e4:e6)++;
 }
 assert(e4==1920&&e6==9408);
 auto components=[&](const vector<vector<int>>& g){vector<char> seen(N);map<int,int> comps;for(int i=0;i<N;i++)if(!seen[i]){int sz=0;vector<int> st{i};seen[i]=1;for(int u=0;u<(int)st.size();u++){int v=st[u];sz++;for(int w:g[v])if(!seen[w]){seen[w]=1;st.push_back(w);}}comps[sz]++;}return comps;};
 auto c4=components(g4),c6=components(g6),c46=components(g46);
 assert((c4==map<int,int>{{1,240},{1104,1}}));assert((c6==map<int,int>{{1344,1}}));assert((c46==map<int,int>{{1344,1}}));
 auto eccentricities=[&](const vector<vector<int>>& g){map<int,int> ecc;for(int s=0;s<N;s++){vector<int> d(N,-1),q{s};d[s]=0;int e=0;for(int k=0;k<(int)q.size();k++){int v=q[k];for(int w:g[v])if(d[w]<0){d[w]=d[v]+1;q.push_back(w);e=max(e,d[w]);}}assert(q.size()==N);ecc[e]++;}return ecc;};
 auto e6c=eccentricities(g6),e46=eccentricities(g46);
 assert((e6c==map<int,int>{{5,432},{6,912}}));assert(e6c==e46);
 cout<<"HAMILTON_CYCLES_OK 1344\n";
 cout<<"PAIRWISE_SQUARE_OK edges=1920 components=240x1+1x1104\n";
 cout<<"PAIRWISE_HEXAGON_OK edges=9408 connected=1 eccentricities=5:432,6:912\n";
 cout<<"PAIRWISE_COMBINED_OK edges=11328 connected=1 eccentricities=5:432,6:912\n";
 cout<<"INDEPENDENT_VERIFY_OK\n";
}
