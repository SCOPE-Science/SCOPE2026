#include <bits/stdc++.h>
using namespace std;
struct T{int n;array<uint16_t,10> e{};};
uint64_t canon(T const&t,bool rootlast=false){int n=t.n;vector<int> deg(n);for(int i=0;i<n;i++)deg[i]=__builtin_popcount((unsigned)t.e[i]);
 vector<int> a(n);iota(a.begin(),a.end(),0);
 sort(a.begin(),a.end(),[&](int x,int y){return make_pair(rootlast && x==n-1?1:0,deg[x])<make_pair(rootlast&&y==n-1?1:0,deg[y]);});
 vector<pair<int,int>> blocks;for(int i=0;i<n;){int j=i+1;while(j<n && deg[a[j]]==deg[a[i]] && (!rootlast || ((a[i]==n-1)==(a[j]==n-1))))j++;blocks.push_back({i,j});i=j;}
 uint64_t best=~0ULL;
 function<void(int)> rec=[&](int b){if(b==(int)blocks.size()){uint64_t z=0;int p=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,p++)if((t.e[a[i]]>>a[j])&1)z|=(1ULL<<p);best=min(best,z);return;} auto [l,r]=blocks[b];sort(a.begin()+l,a.begin()+r);do{rec(b+1);}while(next_permutation(a.begin()+l,a.begin()+r));};rec(0);return best;}
T fromCanon(int n,uint64_t z){T t;t.n=n;int p=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,p++){if((z>>p)&1)t.e[i]|=(1<<j);else t.e[j]|=(1<<i);}return t;}
T extend(T const& old,uint64_t m){T t=old;int n=old.n;t.n=n+1;for(int i=0;i<n;i++)if((m>>i)&1)t.e[i]|=(1<<n);else t.e[n]|=(1<<i);return t;}
struct Res{bool bad;vector<int>c,o;};
Res rootwl(T const&t){int n=t.n;int c[10]={};c[n-1]=1;
 for(int it=0;it<=n;it++){map<vector<int>,int> sig;int nc[10];for(int i=0;i<n;i++){vector<int> v(1+n);v[0]=c[i];for(int j=0;j<n;j++)if((t.e[i]>>j)&1)v[1+c[j]]++;sig[v]=0;}int x=0;for(auto &kv:sig)kv.second=x++;for(int i=0;i<n;i++){vector<int>v(1+n);v[0]=c[i];for(int j=0;j<n;j++)if((t.e[i]>>j)&1)v[1+c[j]]++;nc[i]=sig[v];}
 bool stable=1;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if((c[i]==c[j])!=(nc[i]==nc[j]))stable=0;copy(nc,nc+n,c);if(stable)break;}
 int pid[10];iota(pid,pid+n,0);
 auto leader=[&](int a){while(pid[a]!=a)a=pid[a];return a;};
 bool used[10]={};int f[10];
 function<void(int)> dfs=[&](int i){if(i==n){for(int j=0;j<n;j++){int a=leader(j), b=leader(f[j]);pid[b]=a;}return;}
 for(int j=0;j<n;j++){if(used[j]||c[i]!=c[j])continue;bool ok=1;for(int h=0;h<i;h++)if(((t.e[i]>>h)&1)!=((t.e[j]>>f[h])&1)){ok=0;break;}if(ok){f[i]=j;used[j]=1;dfs(i+1);used[j]=0;}}};dfs(0);
 vector<int> orbit(n);for(int i=0;i<n;i++)orbit[i]=leader(i);bool bad=0;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(c[i]==c[j] && orbit[i]!=orbit[j])bad=1;
 return {bad,vector<int>(c,c+n),orbit};}
int main(int argc,char**argv){int maxn=argc>1?atoi(argv[1]):8;T one;one.n=1;vector<T> repr{one};for(int n=2;n<=maxn;n++){unordered_set<uint64_t> classes;vector<T> nxt;uint64_t checked=0,bad=0;set<uint64_t> failtypes;vector<pair<uint64_t,Res>> first;
 for(auto const&g:repr)for(uint64_t mask=0;mask<(1ULL<<(n-1));mask++){T h=extend(g,mask);checked++;auto r=rootwl(h);if(r.bad){bad++;uint64_t k=canon(h,true);if(failtypes.insert(k).second)first.push_back({k,r});}
 if(n<maxn){uint64_t code=canon(h);if(classes.insert(code).second)nxt.push_back(fromCanon(n,code));}}
 cout<<"n="<<n<<" base_tournament_classes="<<repr.size()<<" extensions="<<checked<<" root_failure_extensions="<<bad<<" unique_rooted_failures="<<failtypes.size()<<" new_unrooted_classes="<<nxt.size()<<""<<"\n";
 for(auto [z,r]:first){cout<<"WITNESS canonical-rooted="<<z<<" colors=";for(int k:r.c)cout<<k<<",";cout<<" orbits=";for(int k:r.o)cout<<k<<",";cout<<"\n";}cout.flush();repr=move(nxt);}}
