// Exact independent census: batch propagation by eligible white-neighbor counts.
// All graph models and claims are specified in RESULT.md. C++17 standard library.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
using Edge=pair<int,int>;

vector<Edge> gp(int n,int k){
 vector<Edge> e;
 for(int i=0;i<n;i++){
  e.push_back({i,(i+1)%n});e.push_back({i,n+i});e.push_back({n+i,n+(i+k)%n});
 }
 return e;
}
vector<Edge> heawood(){vector<Edge> e;for(int j=0;j<7;j++)for(int off:{0,1,3})e.push_back({(j+off)%7,7+j});return e;}
vector<Edge> pappus(){vector<Edge> e;for(int m=0;m<3;m++)for(int b=0;b<3;b++)for(int x=0;x<3;x++)for(int y=0;y<3;y++)if((y-m*x-b+9)%3==0)e.push_back({9+3*m+b,3*x+y});return e;}
void synthemes_rec(vector<int> left,vector<Edge> current,vector<vector<Edge>>& out){
 if(left.empty()){sort(current.begin(),current.end());out.push_back(current);return;}
 int a=left[0];for(int j=1;j<(int)left.size();j++){
  vector<int> next;
  for(int i=1;i<(int)left.size();i++)if(i!=j)next.push_back(left[i]);
  auto copy=current;copy.push_back({a,left[j]});synthemes_rec(next,copy,out);
 }
}
vector<Edge> tutte(){
 vector<Edge> edges,duads;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)duads.push_back({i,j});
 vector<vector<Edge>> synthemes;synthemes_rec({0,1,2,3,4,5},{},synthemes);
 assert(duads.size()==15&&synthemes.size()==15);
 for(int i=0;i<15;i++)for(int j=0;j<15;j++)for(auto p:synthemes[j])if(p==duads[i])edges.push_back({i,j+15});
 return edges;
}
struct Graph{int n;vector<U> adj;Graph(int N,vector<Edge> e):n(N),adj(N,0){for(auto [a,b]:e){assert(a!=b);adj[a]|=U(1)<<b;adj[b]|=U(1)<<a;}}};

bool power(const Graph& g,U seed){
 U blue=seed;
 for(int i=0;i<g.n;i++)if(seed>>i&1)blue|=g.adj[i];
 while(true){
  U changed=0;
  for(int i=0;i<g.n;i++)if(blue>>i&1){
   U white=g.adj[i]&~blue;
   if(white && !(white&(white-1)))changed|=white;
  }
  if(!changed)return blue==((U(1)<<g.n)-1);
  blue|=changed;
 }
}
vector<U> good_of_size(const Graph& g,int k){
 vector<U> good;
 // Use Gosper's construction to enumerate every k-subset, increasing by mask.
 U comb=(U(1)<<k)-1,lim=U(1)<<g.n;
 while(comb<lim){if(power(g,comb))good.push_back(comb);
  U low=comb&-comb,t=comb+low;
  if(t==0)break;
  comb=t+(((t^comb)/low)>>2);
 }
 return good;
}
struct Ans{
 long long edges=0; int components=0; map<int,int> degrees,ecc;int radius=INT_MAX,diam=0;
};
Ans analyse(const Graph &g,const vector<U>& good,bool slide){
 int N=good.size();unordered_map<U,int> ID;ID.reserve(N*2);
 for(int i=0;i<N;i++)ID[good[i]]=i;
 vector<vector<int>> adj(N);
 for(int i=0;i<N;i++){
  U a=good[i];
  for(int x=0;x<g.n;x++)if(a>>x&1){
   for(int y=0;y<g.n;y++)if(!(a>>y&1) && (!slide || (g.adj[x]>>y&1))){
    auto it=ID.find(a^(U(1)<<x)^(U(1)<<y));
    if(it!=ID.end())adj[i].push_back(it->second);
   }
  }
 }
 Ans ans;for(auto& a:adj){ans.edges+=a.size();ans.degrees[(int)a.size()]++;}ans.edges/=2;
 vector<int> seen(N,0),dist(N,-1),q(N);
 for(int s=0;s<N;s++){
  if(!seen[s]){
   ans.components++;int f=0,r=0;seen[s]=1;q[r++]=s;
   while(f<r){int u=q[f++];for(int v:adj[u])if(!seen[v]){seen[v]=1;q[r++]=v;}}
  }
  // Exact all-pairs eccentricity: full breadth-first search from each vertex.
  fill(dist.begin(),dist.end(),-1);
  int f=0,r=0;q[r++]=s;dist[s]=0;int maximum=0;
  while(f<r){int u=q[f++];maximum=max(maximum,dist[u]);for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;q[r++]=v;}}
  ans.ecc[maximum]++;ans.radius=min(ans.radius,maximum);ans.diam=max(ans.diam,maximum);
 }
 return ans;
}
void show(string name,string kind,Ans a){
 cout<<name<<' '<<kind<<" edges="<<a.edges<<" components="<<a.components<<" radius="<<a.radius<<" diameter="<<a.diam<<" ecc=";
 for(auto [e,c]:a.ecc)cout<<e<<':'<<c<<',';
 cout<<" degrees=";for(auto [d,c]:a.degrees)cout<<d<<':'<<c<<',';
 cout<<'\n';
}
int main(){
 vector<tuple<string,Graph>> graphs;
 graphs.emplace_back("H",Graph(14,heawood()));graphs.emplace_back("MK",Graph(16,gp(8,3)));
 graphs.emplace_back("P",Graph(18,pappus()));graphs.emplace_back("D",Graph(20,gp(10,3)));
 graphs.emplace_back("T",Graph(30,tutte()));
 for(auto& [name,g]:graphs){
  int k=0;vector<U> good;
  for(k=1;k<=5;k++){good=good_of_size(g,k);if(!good.empty())break;}
  cout<<name<<" gamma="<<k<<" minima="<<good.size()<<'\n'<<flush;
  show(name,"J",analyse(g,good,false));
  show(name,"S",analyse(g,good,true));
  cout<<flush;
 }
}
