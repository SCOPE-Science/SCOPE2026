// Exact two-player open-neighborhood game on two twenty-vertex cubic graphs.
// C++17: g++ -O2 -std=c++17 verify_exact.cpp -o verify_exact && ./verify_exact
#include <bits/stdc++.h>
using namespace std;
struct Graph {vector<uint32_t> N; vector<vector<int>> adj;};
void add(Graph &g, int u,int v){g.N[u]|=1u<<v;g.N[v]|=1u<<u;g.adj[u].push_back(v);g.adj[v].push_back(u);}
Graph dodecahedron(){
 Graph g{vector<uint32_t>(20,0),vector<vector<int>>(20)};
 const pair<int,int> e[]={{0,1},{0,10},{0,19},{1,2},{1,8},{2,3},{2,6},{3,4},{3,19},{4,5},{4,17},{5,6},{5,15},{6,7},{7,8},{7,14},{8,9},{9,10},{9,13},{10,11},{11,12},{11,18},{12,13},{12,16},{13,14},{14,15},{15,16},{16,17},{17,18},{18,19}};
 for(auto [a,b]:e){add(g,a,b);}
 return g;
}
Graph desargues(){
 Graph g{vector<uint32_t>(20,0),vector<vector<int>>(20)};
 vector<int> sub;
 for(int sz=2;sz<=3;sz++)for(int x=0;x<32;x++)if(__builtin_popcount((unsigned)x)==sz)sub.push_back(x);
 assert(sub.size()==20);
 for(int i=0;i<10;i++)for(int j=10;j<20;j++)if((sub[i]&sub[j])==sub[i])add(g,i,j);
 return g;
}
// Independent fixed relabelings from G(10,2) and G(10,3), respectively.
void graph_identity(const Graph&g,int k,const vector<int>& p){
 assert(p.size()==20);set<int> s(p.begin(),p.end());assert(s.size()==20&&*s.begin()==0&&*s.rbegin()==19);
 vector<uint32_t> a(20,0);auto link=[&](int x,int y){a[x]|=1u<<y;a[y]|=1u<<x;};
 for(int i=0;i<10;i++){link(i,(i+1)%10);link(i,i+10);link(i+10,10+(i+k)%10);}
 for(int i=0;i<20;i++)for(int j=0;j<20;j++)assert(bool(a[i]&(1u<<j))==bool(g.N[p[i]]&(1u<<p[j])));
}
vector<int> distances(const Graph&g,int start){
 vector<int> d(20,-1);queue<int> q;d[start]=0;q.push(start);
 while(!q.empty()){int v=q.front();q.pop();for(int w:g.adj[v])if(d[w]<0){d[w]=d[v]+1;q.push(w);}}
 return d;
}
void check(const string &name,const Graph &g,int k, const vector<int>& mapping,int wantD,int wantS,const vector<pair<int,int>>& shells){
 graph_identity(g,k,mapping);
 for(int i=0;i<20;i++)assert(g.adj[i].size()==3);
 const int ALL=(1<<20)-1;
 vector<unsigned char>D(1<<20,0),S(1<<20,0);
 // Every proper transition strictly increases the mask: descending-mask DP is exact.
 for(int m=ALL-1;m>=0;m--){int mn=127,mx=0;for(uint32_t nb:g.N){if(nb&~(uint32_t)m){int nx=m|nb;mn=min(mn,1+(int)S[nx]);mx=max(mx,1+(int)D[nx]);}}
 assert(mn!=127);D[m]=(unsigned char)mn;S[m]=(unsigned char)mx;}
 assert((int)D[0]==wantD&&(int)S[0]==wantS);
 for(int a=0;a<20;a++){assert(1+(int)S[g.N[a]]==wantD);assert(1+(int)D[g.N[a]]==wantS);}
 cout<<name<<" D="<<(int)D[0]<<" S="<<(int)S[0]<<"\n";
 for(int d=1;d<=5;d++){
  int total=0,baseD=-1,baseS=-1;
  for(int a=0;a<20;a++){
   auto dd=distances(g,a);int local=0;
   for(int b=0;b<20;b++)if(dd[b]==d){
    uint32_t pairmask=g.N[a]|g.N[b];assert((g.N[b]&~g.N[a])!=0);
    int afterD=2+(int)D[pairmask],afterS=2+(int)S[pairmask];
    if(baseD<0){baseD=afterD;baseS=afterS;}else assert(baseD==afterD&&baseS==afterS);
    local++;
   }
   assert(local==shells[d-1].first);total+=local;
  }
  assert(baseD==shells[d-1].second/100&&baseS==shells[d-1].second%100);
  cout<<"distance "<<d<<" count_per_first="<<total/20<<" forced_Dstart="<<baseD<<" forced_Sstart="<<baseS<<"\n";
 }
 // Conditioned opening-pair outcomes are symmetric under exchanging their order.
 for(int a=0;a<20;a++)for(int b=0;b<20;b++)if(a!=b){
  assert((g.N[b]&~g.N[a])!=0);
  uint32_t m=g.N[a]|g.N[b];assert(D[m]<=20&&S[m]<=20);
 }
 cout<<name<<" ALL_380_ORDERED_PAIRS_CHECKED\n";
}
int main(){
 check("DODECAHEDRON",dodecahedron(),2,{0,1,8,7,14,15,16,17,18,19,10,2,9,6,13,5,12,4,11,3},11,10,{{3,1011},{6,1111},{6,1011},{3,1011},{1,1010}});
 check("DESARGUES",desargues(),3,{0,10,2,13,5,19,9,17,6,14,11,1,16,4,12,8,18,3,15,7},10,10,{{3,1010},{6,1010},{6,1010},{3,1010},{1,1010}});
 cout<<"VERIFY_OK\n";
}
