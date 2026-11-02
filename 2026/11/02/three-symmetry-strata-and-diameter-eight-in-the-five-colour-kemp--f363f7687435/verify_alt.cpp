#include <bits/stdc++.h>
using namespace std;
using State=array<unsigned char,15>;
struct Hash {size_t operator()(State const &a)const noexcept {size_t h=1469598103934665603ULL;for(int x:a){h^=(x+1);h*=1099511628211ULL;}return h;}};
vector<array<int,5>> perms;
vector<State> states;
unordered_map<State,int,Hash> loc;
State normalize(State a){int mp[5];for(int i=0;i<5;i++)mp[a[i]]=i;for(auto &x:a)x=mp[x];return a;}
int main(){array<int,5> v={0,1,2,3,4};do {perms.push_back(v);}while(next_permutation(v.begin(),v.end()));
for(auto const &r0:perms)for(auto const &r1:perms){bool ok=true;for(int j=0;j<5;j++)if(r0[j]==r1[j])ok=false;if(!ok)continue;
for(auto const&r2:perms){bool valid=true;State s{};for(int j=0;j<5;j++){if(r0[j]==r2[j]||r1[j]==r2[j])valid=false;s[j]=r0[j];s[5+j]=r1[j];s[10+j]=r2[j];}if(valid){loc[s]=states.size();states.push_back(s);}}}
if(states.size()!=66240)abort();
vector<vector<int>> adj(states.size());long long twos=0;
for(int si=0;si<(int)states.size();si++){
 auto s=states[si];vector<int> nbr;
 for(int a=0;a<5;a++)for(int b=a+1;b<5;b++){
  // Components on 8 incidence vertices; for each present color, draw its bipartite graph edge.
  vector<pair<int,int>> colored;vector<vector<int>> g(8);
  for(int i=0;i<3;i++)for(int j=0;j<5;j++)if(s[5*i+j]==a||s[5*i+j]==b){colored.push_back({i,j});g[i].push_back(3+j);g[3+j].push_back(i);}
  if(colored.size()!=6)abort();
  array<int,8> comp;comp.fill(-1);int nc=0;
  for(int u=0;u<8;u++)if(comp[u]<0){queue<int>q;q.push(u);comp[u]=nc;while(!q.empty()){int x=q.front();q.pop();for(int y:g[x])if(comp[y]<0){comp[y]=nc;q.push(y);}}nc++;}
  set<int> components;
  for(auto [i,j]:colored)components.insert(comp[i]);
  for(int c:components){State t=s;for(auto [i,j]:colored)if(comp[i]==c)t[5*i+j]=(a+b)-t[5*i+j];auto it=loc.find(t);if(it==loc.end())abort();if(it->second!=si)nbr.push_back(it->second);}
 }
 sort(nbr.begin(),nbr.end());nbr.erase(unique(nbr.begin(),nbr.end()),nbr.end());adj[si]=move(nbr);twos+=adj[si].size();
}
if(twos!=1094400)abort();for(int i=0;i<(int)states.size();i++)for(int x:adj[i])if(!binary_search(adj[x].begin(),adj[x].end(),i))abort();
map<int,int> deg;for(auto&a:adj)deg[a.size()]++;
if(deg!=map<int,int>{{15,8640},{16,14400},{17,43200}})abort();
// Restrict to first row (0..4); enumerate all normalized states and their group orbit representatives.
map<State,int> canoncount;
map<State,int> represent;
array<int,3> rows={0,1,2};
for(auto const &s:states){if(!equal(s.begin(),s.begin()+5,v.begin()))continue;
 State best=s;auto rr=rows;
 do {for(auto cp:perms){State t;for(int i=0;i<3;i++)for(int j=0;j<5;j++)t[5*i+j]=s[5*rr[i]+cp[j]];t=normalize(t);if(t<best)best=t;}}while(next_permutation(rr.begin(),rr.end()));
 canoncount[best]++; represent[best]=loc.at(best);
}
map<int,int> orbitsizes;map<int,int> radial;
if(canoncount.size()!=3)abort();
for(auto &[rep,normnum]:canoncount){int u=represent[rep];vector<int> dist(states.size(),-1);queue<int> q;q.push(u);dist[u]=0;map<int,int> prof;prof[0]++;
 while(!q.empty()){int x=q.front();q.pop();for(int y:adj[x])if(dist[y]<0){dist[y]=dist[x]+1;prof[dist[y]]++;q.push(y);}}
 if(count(dist.begin(),dist.end(),-1)!=0)abort();int ecc=*max_element(dist.begin(),dist.end());int degree=adj[u].size();
 cout<<"ORBIT normalized="<<normnum<<" full="<<120*normnum<<" degree="<<degree<<" eccentricity="<<ecc<<" profile=";
 for(auto [d,c]:prof)cout<<d<<":"<<c<<",";cout<<"\n";
 orbitsizes[degree]=120*normnum;radial[degree]=ecc;
}
if(orbitsizes!=map<int,int>{{15,8640},{16,14400},{17,43200}})abort();
if(radial!=map<int,int>{{15,8},{16,7},{17,7}})abort();
cout<<"ALTERNATE_COMPLETE_OK states=66240 edges="<<twos/2<<" radius=7 diameter=8\n";
}
