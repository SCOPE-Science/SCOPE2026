#include <bits/stdc++.h>
using namespace std;
struct S {int k, n; vector<int> verts; vector<vector<int>> cycles; vector<vector<int>> edges; vector<char> gone,vis; vector<int> dist; int cyc=0,longest=0; long long checked=0,good=0; map<int,long long> hist; vector<pair<vector<int>,int>> records;
 bool dfs(int u){vis[u]=1;int m=1;for(int v:edges[u])if(!gone[v]){if(vis[v]==1)return false;if(vis[v]==0 && !dfs(v))return false;m=max(m,1+dist[v]);}vis[u]=2;dist[u]=m;longest=max(longest,m);return true;}
 void evaluate(const vector<int>& sel){checked++;fill(vis.begin(),vis.end(),0);fill(dist.begin(),dist.end(),0);longest=0;bool ok=1;for(int v:verts){if(!gone[v] && vis[v]==0){if(!dfs(v)){ok=0;break;}}}if(ok){good++;hist[longest]++;records.emplace_back(sel,longest);}}
 void go(int d,vector<int>&s){if(d==(int)cycles.size()){evaluate(s);return;}for(int x:cycles[d]){gone[x]=1;s.push_back(x);go(d+1,s);s.pop_back();gone[x]=0;}}
 void run(int kk){k=kk;n=1<<k;verts.clear();cycles.clear();edges.assign(n,{});gone.assign(n,0);vis.assign(n,0);dist.assign(n,0);checked=good=0;hist.clear();records.clear();vector<char> allowed(n,0),seen(n,0);for(int x=0;x<n;x++){bool ok=true;for(int p=1;p<k;p++)if((x&(1<<p)) && (x&(1<<(p-1))))ok=false;if(ok){allowed[x]=1;verts.push_back(x);}}for(int x:verts){for(int b=0;b<2;b++){int y=((x<<1)&(n-1))|b;if(allowed[y])edges[x].push_back(y);}}for(int x:verts)if(!seen[x]){vector<int> path;int y=x;do{path.push_back(y);seen[y]=1;y=((y<<1)&(n-1))|(y>>(k-1));}while(y!=x);bool ok=1;for(int p:path)if(!allowed[p])ok=0;if(ok)cycles.push_back(path);}
 vector<int>sel;go(0,sel);sort(records.begin(),records.end(),[](auto&a,auto&b){return a.first<b.first;});
 cout<<"n="<<k<<" allowed="<<verts.size()<<" cycles="<<cycles.size()<<" cand="<<checked<<" accepted="<<good<<" hist=";for(auto[p,v]:hist)cout<<p<<":"<<v<<",";cout<<"\n";

 }
};
int main(){S s;for(int k=2;k<=8;k++)s.run(k);}
