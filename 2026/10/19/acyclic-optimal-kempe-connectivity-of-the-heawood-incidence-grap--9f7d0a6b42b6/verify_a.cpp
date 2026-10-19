#include <bits/stdc++.h>
using namespace std;
int edgeU[21],edgeV[21], deg[14], incident[14][3],used[14],color[21];
long long valid=0, proper=0;
vector<uint64_t> states;
uint64_t encode(){uint64_t x=0;for(int e=0;e<21;e++)x|=uint64_t(color[e])<<(2*e);return x;}
bool has_alternating_path(int s,int t,int c,int d){
 int stack[14], top=0;bool vis[14]={false};stack[top++]=s;vis[s]=true;
 while(top){int v=stack[--top]; if(v==t)return true;
  for(int h=0;h<deg[v];h++){int e=incident[v][h];if(color[e]!=c&&color[e]!=d)continue;int w=edgeU[e]^edgeV[e]^v;if(!vis[w]){vis[w]=true;stack[top++]=w;}}
 }return false;
}
void dfs(int a){
 if(a==21){valid++;states.push_back(encode());return;}
 int best=-1,mn=5, mx=-1;for(int e=0;e<21;e++)if(color[e]<0){int av=4-__builtin_popcount((unsigned)(used[edgeU[e]]|used[edgeV[e]]));int sc=__builtin_popcount((unsigned)(used[edgeU[e]]|used[edgeV[e]]));if(av<mn||(av==mn&&sc>mx)){best=e;mn=av;mx=sc;}}
 if(mn==0)return;
 int u=edgeU[best],v=edgeV[best];
 for(int c=0;c<4;c++)if(!((used[u]|used[v])&(1<<c))){
  bool bad=false;
  for(int d=0;d<4;d++)if(d!=c&&(used[u]&(1<<d))&&(used[v]&(1<<d))){if(has_alternating_path(u,v,c,d)){bad=true;break;}}
  if(bad)continue;
  color[best]=c;used[u]|=1<<c;used[v]|=1<<c; dfs(a+1);used[u]^=1<<c;used[v]^=1<<c;color[best]=-1;
 }
}
int main(){
 // vertices 0..6 point; 7..13 lines; incidence to j,j+1,j+3 mod 7.
 int edge=0;for(int j=0;j<7;j++)for(int k:{0,1,3}){int a=(j+k)%7,b=7+j; edgeU[edge]=a;edgeV[edge]=b;incident[a][deg[a]++]=edge;incident[b][deg[b]++]=edge;edge++;}
 memset(color,-1,sizeof(color));
 // Root point0, assign incident edges distinct 0,1,2 to normalize
 for(int k=0;k<3;k++){int e=incident[0][k];color[e]=k;used[0]|=1<<k;int v=edgeU[e]^edgeV[e];used[v]|=1<<k;}
 auto t=chrono::steady_clock::now();dfs(3);
 cout<<"normalized_valid "<<valid<<" labeled_valid "<<valid*24<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"\n";
 
 unordered_map<uint64_t,int> idx;idx.reserve(states.size()*2);
 for(size_t i=0;i<states.size();i++)idx[states[i]]=i;
 if(idx.size()!=states.size()){cerr<<"DUPLICATES! "<<idx.size()<<"\n";return 1;}
 vector<vector<int>> adj(states.size());long long missing=0,self=0, attempted=0;
 for(size_t i=0;i<states.size();i++){
  auto z=states[i];for(int e=0;e<21;e++)color[e]=(z>>(2*e))&3;
  for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){
   int seen[14]={};
   for(int e0=0;e0<21;e0++) if(color[e0]==a||color[e0]==b){
    int start=edgeU[e0];if(seen[start])continue;
    int stack[14],nn=0,top=0,part[21]={};stack[top++]=start;seen[start]=1;
    while(top){int u=stack[--top];for(int k=0;k<deg[u];k++){
      int e=incident[u][k]; if(color[e]!=a&&color[e]!=b)continue;
      part[e]=1;int v=edgeU[e]^edgeV[e]^u; if(!seen[v]){seen[v]=1;stack[top++]=v;}
    }}
    // omit no-edge components and try swapping one connected alternating component
    uint64_t y=z;for(int e=0;e<21;e++)if(part[e]){int c=color[e]==a?b:a;y=(y&(~(uint64_t(3)<<(2*e))))|(uint64_t(c)<<(2*e));}
    int trans[4]={-1,-1,-1,-1};for(int k=0;k<3;k++){int c=(y>>(2*incident[0][k]))&3;trans[c]=k;}
    for(int c=0;c<4;c++)if(trans[c]<0)trans[c]=3;
    uint64_t canon=0;int modcolors[21],umask[14]={};
    for(int e=0;e<21;e++){int c=trans[(y>>(2*e))&3];modcolors[e]=c;canon|=uint64_t(c)<<(2*e);}
    attempted++;
    if(canon==z){self++;continue;}
    bool ac=true;
    for(int c=0;c<4&&ac;c++)for(int d=c+1;d<4&&ac;d++){
      int p[14];for(int x=0;x<14;x++)p[x]=x;
      auto root=[&](int x){while(x!=p[x])x=p[x]=p[p[x]];return x;};
      for(int e=0;e<21;e++)if(modcolors[e]==c||modcolors[e]==d){int u=root(edgeU[e]),v=root(edgeV[e]);if(u==v){ac=false;break;}p[u]=v;}
    }
    if(!ac)continue;
    auto it=idx.find(canon);if(it==idx.end()){missing++;continue;}
    adj[i].push_back(it->second);
   }
  }
  sort(adj[i].begin(),adj[i].end());adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
 }
 long long degree_sum=0,arcs=0;map<int,int> hist;for(auto &v:adj){hist[v.size()]++;degree_sum+=v.size();}
 vector<int> comp(states.size(),-1), compsize;queue<int>q;
 for(int i=0;i<(int)states.size();i++)if(comp[i]<0){int z=compsize.size(),s=0;comp[i]=z;q.push(i);while(!q.empty()){int u=q.front();q.pop();s++;for(int w:adj[u])if(comp[w]<0){comp[w]=z;q.push(w);}}compsize.push_back(s);}
 map<int,int> chist;for(int s:compsize)chist[s]++;
 cout<<"moves_attempted "<<attempted<<" self "<<self<<" absent "<<missing<<" directed_edges "<<degree_sum<<" undirected_edges "<<degree_sum/2<<"\n";
 cout<<"components "<<compsize.size()<<" distribution:";for(auto [s,k]:chist)cout<<" ("<<s<<","<<k<<")";cout<<"\n";
 cout<<"degrees:";for(auto [d,k]:hist)cout<<" ("<<d<<","<<k<<")";cout<<"\n";
 long long asym=0;for(int i=0;i<(int)states.size();i++)for(int j:adj[i])if(!binary_search(adj[j].begin(),adj[j].end(),i))asym++;
 cout<<"asymmetric "<<asym<<"\n";
 
}
