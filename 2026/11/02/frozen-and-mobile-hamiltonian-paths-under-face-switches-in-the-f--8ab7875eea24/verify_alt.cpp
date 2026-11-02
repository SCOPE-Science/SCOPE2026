#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int eid[16][16];vector<array<int,4>> sq;unordered_set<U> seen;long long dfs_end=0;
void walk(int u,int used,U mask){if(used==65535){seen.insert(mask);dfs_end++;return;}for(int d=0;d<4;d++){int v=u^(1<<d);if(!(used&(1<<v)))walk(v,used|(1<<v),mask|(U(1)<<eid[u][v]));}}
int main(){memset(eid,-1,sizeof eid);int ne=0;for(int u=0;u<16;u++)for(int d=0;d<4;d++){int v=u^(1<<d);if(u<v)eid[u][v]=eid[v][u]=ne++;}
 for(int x=0;x<16;x++)for(int a=0;a<4;a++)for(int b=a+1;b<4;b++){int y=x^(1<<a),z=x^(1<<b),w=x^(1<<a)^(1<<b);if(x<min({y,z,w}))sq.push_back({eid[x][y],eid[y][w],eid[w][z],eid[z][x]});}
 for(int x=0;x<16;x++)walk(x,1<<x,0);if(seen.size()!=45696)throw runtime_error("count mismatch");vector<U> v(seen.begin(),seen.end());unordered_map<U,int> ix;for(int i=0;i<(int)v.size();i++)ix[v[i]]=i;vector<vector<int>> adj(v.size());
 for(int i=0;i<(int)v.size();i++)for(auto f:sq){bool a=(v[i]>>f[0])&1,b=(v[i]>>f[1])&1,c=(v[i]>>f[2])&1,d=(v[i]>>f[3])&1;if(a&&c&&!b&&!d||b&&d&&!a&&!c){U m=v[i];for(int j:f)m^=U(1)<<j;auto it=ix.find(m);if(it!=ix.end())adj[i].push_back(it->second);}}
 map<int,int> deg,comp;int edges=0;for(auto &r:adj){deg[r.size()]++;edges+=r.size();}edges/=2;vector<char> visit(v.size());for(int i=0;i<(int)v.size();i++)if(!visit[i]){int cnt=0;queue<int> q;q.push(i);visit[i]=1;while(!q.empty()){int x=q.front();q.pop();cnt++;for(int y:adj[x])if(!visit[y])visit[y]=1,q.push(y);}comp[cnt]++;}
 cout<<"ALT count="<<v.size()<<" edges="<<edges<<" degree=";for(auto [a,b]:deg)cout<<a<<":"<<b<<",";cout<<" components=";for(auto[a,b]:comp)cout<<a<<":"<<b<<",";cout<<"\n";
 if(v.size()!=45696||edges!=69120||comp!=map<int,int>{{1,5184},{528,32},{738,32}})return 1;
 cout<<"ALT_PASS\n";
}
