#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct Edge {int u,v;};
vector<Edge>E; vector<int>inc[14];int col[21],maskv[14];vector<U> valid_states;long long proper_normalized=0;
int pop(int x){return __builtin_popcount((unsigned)x);}
bool valid_acyclic(const int c[21]){
 for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
  int p[14];iota(p,p+14,0);
  auto rt=[&](int x){while(p[x]!=x)x=p[x]=p[p[x]];return x;};
  for(int e=0;e<21;e++)if(c[e]==a||c[e]==b){int u=rt(E[e].u),v=rt(E[e].v);if(u==v)return false;p[u]=v;}
 }return true;
}
U pack(const int c[21]){U x=0;for(int e=0;e<21;e++)x|=U(c[e])<<(2*e);return x;}
void dfs(int t){
 if(t==21){proper_normalized++;if(valid_acyclic(col))valid_states.push_back(pack(col));return;}
 int best=-1,avail=5;for(int e=0;e<21;e++)if(col[e]==-1){int left=4-pop(maskv[E[e].u]|maskv[E[e].v]);if(left<avail){avail=left;best=e;}}
 if(avail==0)return;
 int u=E[best].u,v=E[best].v;
 for(int k=0;k<4;k++)if(!((maskv[u]|maskv[v])>>k&1)){
  col[best]=k;maskv[u]|=1<<k;maskv[v]|=1<<k;dfs(t+1);maskv[u]^=1<<k;maskv[v]^=1<<k;col[best]=-1;
 }
}
int main(){
 // Fano plane as seven nonzero GF(2)^3 vectors: point a and line b incident when a.b=0.
 for(int a=1;a<=7;a++)for(int b=1;b<=7;b++)if(pop(a&b)%2==0){int id=E.size();E.push_back({a-1,7+b-1});inc[a-1].push_back(id);inc[7+b-1].push_back(id);}
 assert(E.size()==21);for(int v=0;v<14;v++)assert(inc[v].size()==3);
 fill(col,col+21,-1);int root=0;
 for(int k=0;k<3;k++){int e=inc[root][k],v=E[e].u^E[e].v^root;col[e]=k;maskv[root]|=1<<k;maskv[v]|=1<<k;}
 dfs(3);
 unordered_map<U,int> loc;loc.reserve(valid_states.size()*2);for(int i=0;i<(int)valid_states.size();i++)loc[valid_states[i]]=i;
 assert(loc.size()==valid_states.size());
 vector<vector<int>> adj(valid_states.size());int diff_missing=0;
 for(int z=0;z<(int)valid_states.size();z++){
  U st=valid_states[z];int c[21];for(int e=0;e<21;e++)c[e]=int(st>>(2*e))&3;
  for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
   bool seen[21]={0};
   for(int e0=0;e0<21;e0++)if((c[e0]==a||c[e0]==b)&&!seen[e0]){
    vector<int>part;queue<int>q;q.push(e0);seen[e0]=true;
    while(!q.empty()){
     int e=q.front();q.pop();part.push_back(e);
     for(int v:{E[e].u,E[e].v})for(int f:inc[v])if(!seen[f]&&(c[f]==a||c[f]==b)){seen[f]=true;q.push(f);}
    }
    int nc[21];copy(c,c+21,nc);for(int e:part)nc[e]=(nc[e]==a?b:a);
    if(!valid_acyclic(nc))continue;
    int ren[4]={-1,-1,-1,-1};for(int k=0;k<3;k++)ren[nc[inc[root][k]]]=k;
    for(int k=0;k<4;k++)if(ren[k]==-1)ren[k]=3;
    for(int e=0;e<21;e++)nc[e]=ren[nc[e]];
    U dst=pack(nc);if(dst==st)continue;
    auto it=loc.find(dst);if(it==loc.end()){diff_missing++;continue;}
    adj[z].push_back(it->second);
   }
  }
  sort(adj[z].begin(),adj[z].end());adj[z].erase(unique(adj[z].begin(),adj[z].end()),adj[z].end());
 }
 map<int,int> degrees,component_sizes;long long arcs=0;
 for(auto& v:adj){degrees[v.size()]++;arcs+=v.size();}
 vector<char> visited(adj.size());int ncomps=0;queue<int>q;
 for(int i=0;i<(int)adj.size();i++)if(!visited[i]){
  int sz=0;visited[i]=1;q.push(i);while(!q.empty()){int u=q.front();q.pop();sz++;for(int v:adj[u])if(!visited[v]){visited[v]=1;q.push(v);}}
  component_sizes[sz]++;ncomps++;
 }
 long long asym=0;for(int u=0;u<(int)adj.size();u++)for(int v:adj[u])if(!binary_search(adj[v].begin(),adj[v].end(),u))asym++;
 cout<<"model dot-products root="<<root<<" vertices=14 edges="<<E.size()<<"\n";
 cout<<"proper normalized="<<proper_normalized<<" acyclic normalized="<<valid_states.size()<<" labeled="<<valid_states.size()*24<<"\n";
 cout<<"edges="<<arcs/2<<" components="<<ncomps<<" absent="<<diff_missing<<" asym="<<asym<<"\n";
 cout<<"degrees:";for(auto [d,k]:degrees)cout<<" ("<<d<<","<<k<<")";cout<<"\n";
 cout<<"components:";for(auto [d,k]:component_sizes)cout<<" ("<<d<<","<<k<<")";cout<<"\n";
}
