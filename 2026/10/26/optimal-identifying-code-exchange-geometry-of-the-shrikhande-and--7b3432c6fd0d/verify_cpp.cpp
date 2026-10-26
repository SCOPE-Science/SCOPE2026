#include <bits/stdc++.h>
using namespace std;
// Exact closed-neighborhood identifying-code and exchange-graph enumeration.
// Vertices (x,y) of Z_4^2 have index 4*x+y. No external graph database.
using M=uint32_t;
struct Graph {array<M,16> closed{};};
Graph build(bool shrikhande){
 Graph g;
 for(int x=0;x<4;x++)for(int y=0;y<4;y++){
  int p=4*x+y; M mask=0;
  for(int a=0;a<4;a++)for(int b=0;b<4;b++){
   int dx=(a-x+4)%4,dy=(b-y+4)%4;
   bool adjacent=shrikhande ? ((dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||(dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3)) : (x==a || y==b);
   if(p==4*a+b || adjacent)mask |= M(1)<<(4*a+b);
  }
  g.closed[p]=mask;
 }
 return g;
}
bool is_code(const Graph&g,M m){
 bool seen[1<<16]={};
 for(int v=0;v<16;v++){
  M sig = g.closed[v]&m;
  if(!sig || seen[sig])return false;
  seen[sig]=true;
 }
 return true;
}
void check_srg(const Graph&g){
 for(int i=0;i<16;i++){
  if(__builtin_popcount(g.closed[i])!=7)throw runtime_error("degree");
  for(int j=i+1;j<16;j++){
   bool a=(g.closed[i]>>j)&1, b=(g.closed[j]>>i)&1;
   if(a!=b || __builtin_popcount((g.closed[i] & ~(M(1)<<i))&(g.closed[j] & ~(M(1)<<j)))!=2)
     throw runtime_error("srg common neighbors");
  }
 }
}
struct Stats { vector<M> codes; long edges=0;vector<int> components;map<int,int> degrees,ecc; };
Stats check(bool sh){
 Graph g=build(sh);check_srg(g);
 Stats st; int cutoff=sh?5:6; vector<long> counts(cutoff+1);
 for(M m=0;m<1u<<16;m++)if(__builtin_popcount(m)<=cutoff && is_code(g,m)){
  ++counts[__builtin_popcount(m)]; if(__builtin_popcount(m)==cutoff)st.codes.push_back(m);
 }
 cout<<(sh?"shrikhande":"rook")<<" checked_all_subsets_up_to_size="<<cutoff<<" counts=";
 for(int k=0;k<=cutoff;k++){cout<<(k?",":"")<<k<<":"<<counts[k];}
 cout<<"\n";
 if(st.codes.size()!=(sh?96u:2208u))throw runtime_error("unexpected minimum census");
 map<M,int> idx;
 for(int i=0;i<(int)st.codes.size();i++)idx[st.codes[i]]=i;
 vector<vector<int>> a(st.codes.size());
 for(int u=0;u<(int)st.codes.size();u++){
  M m=st.codes[u];
  for(int i=0;i<16;i++)if(m&(M(1)<<i))for(int j=0;j<16;j++)if(!(m&(M(1)<<j))){
   auto it=idx.find(m^(M(1)<<i)^(M(1)<<j));
   if(it!=idx.end() && u<it->second){int v=it->second;a[u].push_back(v);a[v].push_back(u);st.edges++;}
  }
 }
 vector<char> vis(a.size());
 for(int u=0;u<(int)a.size();u++)if(!vis[u]){
  int count=0;queue<int> q;q.push(u);vis[u]=1;
  while(!q.empty()){
   int w=q.front();q.pop();count++;
   for(int v:a[w])if(!vis[v])vis[v]=1,q.push(v);
  }
  st.components.push_back(count);
 }
 sort(st.components.begin(),st.components.end());
 for(auto const &v:a)st.degrees[v.size()]++;
 for(int u=0;u<(int)a.size();u++){
  vector<int> dist(a.size(),-1);queue<int> q;q.push(u);dist[u]=0;
  while(!q.empty()){
   int w=q.front();q.pop();
   for(int v:a[w])if(dist[v]<0)dist[v]=dist[w]+1,q.push(v);
  }
  int ecc=*max_element(dist.begin(),dist.end());st.ecc[ecc]++;
 }
 cout<<(sh?"shrikhande":"rook")<<" codes="<<st.codes.size()<<" exchange_edges="<<st.edges<<" components="<<st.components.size()<<" sizes=";
 for(auto [size,n]:[&]{map<int,int> c;for(int z:st.components)c[z]++;return c;}())cout<<size<<":"<<n<<" ";
 cout<<"degrees=";for(auto [d,n]:st.degrees)cout<<d<<":"<<n<<" ";
 cout<<"eccentricities=";for(auto [d,n]:st.ecc)cout<<d<<":"<<n<<" ";cout<<"\n";
 if(sh){
  set<M> templ;
  for(int q=0;q<16;q++){
   int x=q/4,y=q%4;M quad=0;
   for(int xx=0;xx<4;xx++)for(int yy=0;yy<4;yy++)if(xx%2==x%2&&yy%2==y%2)quad|=M(1)<<(4*xx+yy);
   if(__builtin_popcount(quad)!=4 || !(quad&(M(1)<<q)))throw runtime_error("bad coset");
   M core=quad^(M(1)<<q);
   for(int i=0;i<16;i++)for(int j=i+1;j<16;j++){
    if(i!=q && j!=q && (g.closed[q]&(M(1)<<i)) && (g.closed[q]&(M(1)<<j)) && (g.closed[i]&(M(1)<<j)))
      templ.insert(core|(M(1)<<i)|(M(1)<<j));
   }
  }
  if(templ.size()!=96u || set<M>(st.codes.begin(),st.codes.end())!=templ)throw runtime_error("geometric classification failed");
  if(st.edges!=96 || st.components!=vector<int>(16,6) || st.degrees!=map<int,int>{{2,96}} || st.ecc!=map<int,int>{{3,96}})throw runtime_error("exchange graph mismatch");
  cout<<"shrikhande geometric_coset_and_neighbor_edge_classification=EXACT 16 cores x 6 local edges\n";
 } else {
  if(st.edges!=28800 || st.components!=vector<int>{2208} || st.ecc!=map<int,int>{{6,2208}})throw runtime_error("rook graph mismatch");
  cout<<"rook connected_exchange_diameter=6\n";
 }
 return st;
}
int main(){try{check(true);check(false);cout<<"PASS\n";}catch(exception const&e){cerr<<"FAIL "<<e.what()<<"\n";return 1;}}
