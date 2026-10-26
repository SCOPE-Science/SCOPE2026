// Exhaustive finite verification for minimum identifying-code exchanges in two Kneser graphs.
// C++17; compile with c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using M = uint64_t;
struct Graph {
 int n,m; vector<pair<int,int>> edges; vector<M> closed;
 Graph(int nn):n(nn){
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edges.push_back({a,b});
  m=edges.size();closed.resize(m,0);
  for(int a=0;a<m;a++)for(int b=0;b<m;b++){
   const auto [x,y]=edges[a]; const auto [u,v]=edges[b];
   if(a==b || (x!=u&&x!=v&&y!=u&&y!=v))closed[a]|=M(1)<<b;
  }
 }
 bool code(M selected)const{
  M seen[50];
  for(int a=0;a<m;a++){
   M signature=closed[a]&selected;
   if(!signature)return false;
   for(int b=0;b<a;b++)if(seen[b]==signature)return false;
   seen[a]=signature;
  }
  return true;
 }
 int number(int a,int b)const{
  if(a>b)swap(a,b);
  return int(lower_bound(edges.begin(),edges.end(),make_pair(a,b))-edges.begin());
 }
 vector<M> codes_at_size(int k)const{
  vector<M> out;
  M s=(M(1)<<k)-1,limit=M(1)<<m;
  while(s<limit){
   if(code(s))out.push_back(s);
   M c=s&-s, r=s+c;
   if(!r)break;
   s=(((r^s)>>2)/c)|r;
  }
  return out;
 }
};
void require(bool a,const char*message){if(!a){cerr<<"FAIL: "<<message<<"\n";exit(1);}}
struct Profile{long long edges=0; map<int,int> degree;vector<int> components;};
Profile profile(const Graph& g, const vector<M>& states){
 unordered_map<M,int>index;index.reserve(states.size()*2);
 for(int i=0;i<int(states.size());i++)index.emplace(states[i],i);
 vector<vector<int>>adj(states.size());Profile p;
 for(int i=0;i<int(states.size());i++){
  M x=states[i];
  for(int a=0;a<g.m;a++)if((x>>a)&1)
   for(int b=0;b<g.m;b++)if(!((x>>b)&1)){
    auto it=index.find(x^(M(1)<<a)^(M(1)<<b));
    if(it!=index.end())adj[i].push_back(it->second);
   }
  p.degree[int(adj[i].size())]++;
  p.edges+=adj[i].size();
 }
 require(p.edges%2==0,"even graph-degree sum");p.edges/=2;
 vector<char>vis(states.size(),0);
 for(int i=0;i<int(states.size());i++)if(!vis[i]){
  queue<int>q;q.push(i);vis[i]=1;int count=0;
  while(!q.empty()){
   int u=q.front();q.pop();count++;
   for(int v:adj[u])if(!vis[v]){vis[v]=1;q.push(v);}
  }
  p.components.push_back(count);
 }
 sort(p.components.begin(),p.components.end());
 return p;
}
int main(){
 Graph eight(8),nine(9);
 for(const Graph* g:{&eight,&nine}){
  for(int k=1;k<6;k++){
   auto lower=g->codes_at_size(k);
   require(lower.empty(),"no identifying codes below size six");
  }
  cout<<"LOWER_BOUND_OK n="<<g->n<<"\n";
 }
 auto a=eight.codes_at_size(6);
 require(a.size()==141120,"K(8,2) code count");
 auto pa=profile(eight,a);
 require(pa.edges==4730880,"K(8,2) exchange edges");
 require(pa.components==vector<int>{141120},"K(8,2) exchange connectivity");
 require(pa.degree==map<int,int>{{56,3360},{58,10080},{64,20160},{66,67200},{72,10080},{74,30240}},"K(8,2) degree profile");
 cout<<"K8_OK codes="<<a.size()<<" edges="<<pa.edges<<" components="<<pa.components.size()<<"\n";
 auto b=nine.codes_at_size(6);
 require(b.size()==7560,"K(9,2) code count");
 auto pb=profile(nine,b);
 require(pb.edges==22680,"K(9,2) exchange edges");
 require(pb.degree==map<int,int>{{6,7560}},"K(9,2) degrees");
 require(pb.components.size()==280,"K(9,2) components");
 for(int size:pb.components)require(size==27,"K(9,2) all components size 27");
 // Independent constructive characterization. Every triple partition produces 27 path choices.
 unordered_set<M> gener;gener.reserve(16000);
 // Enumerate partitions by choosing lex-first remaining vertex in each new triple.
 auto rec=[&](auto&&self,vector<vector<int>>&blocks, vector<int>rem)->void{
  if(rem.empty()){
   for(int c0=0;c0<3;c0++)for(int c1=0;c1<3;c1++)for(int c2=0;c2<3;c2++){
    int centers[3]={c0,c1,c2};M s=0;
    for(int j=0;j<3;j++)for(int k=0;k<3;k++)if(k!=centers[j])
     s|=M(1)<<nine.number(blocks[j][centers[j]],blocks[j][k]);
    require(nine.code(s),"each spanning 3P3 is identifying");gener.insert(s);
   }
   return;
  }
  int x=rem.front();
  for(int i=1;i<int(rem.size());i++)for(int j=i+1;j<int(rem.size());j++){
   vector<int>rest;for(int k=1;k<int(rem.size());k++)if(k!=i&&k!=j)rest.push_back(rem[k]);
   blocks.push_back({x,rem[i],rem[j]});self(self,blocks,rest);blocks.pop_back();
  }
 };
 vector<vector<int>>blocks;rec(rec,blocks,{0,1,2,3,4,5,6,7,8});
 require(gener.size()==7560,"three-path factors count");
 for(M s:b)require(gener.count(s)==1,"every minimum code is three disjoint paths");
 cout<<"K9_OK codes="<<b.size()<<" edges="<<pb.edges<<" components="<<pb.components.size()<<" Hamming_factors=K3xK3xK3\n";
 cout<<"ALL_VERIFY_OK\n";
}
