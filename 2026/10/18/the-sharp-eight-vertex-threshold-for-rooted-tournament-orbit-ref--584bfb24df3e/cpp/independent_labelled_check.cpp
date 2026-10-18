#include <bits/stdc++.h>
using namespace std;
struct Result{bool bad; vector<int> col,orbit;};
Result check(int n, uint64_t z){int e[9][9]={};int p=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int b=(z>>p++)&1; e[i][j]=b;e[j][i]=1-b;}
 int c[9]={}; c[0]=1;for(int t=0;t<=n;t++){map<vector<int>,int> keys; int nc[9];for(int i=0;i<n;i++){vector<int> v(1+n);v[0]=c[i];for(int j=0;j<n;j++)if(i!=j && e[i][j])v[c[j]+1]++; keys.emplace(v,0); }int k=0;for(auto &pr:keys)pr.second=k++;for(int i=0;i<n;i++){vector<int> v(1+n);v[0]=c[i];for(int j=0;j<n;j++)if(i!=j && e[i][j])v[c[j]+1]++;nc[i]=keys[v];}bool same=true;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if((c[i]==c[j])!=(nc[i]==nc[j]))same=false;copy(nc,nc+n,c);if(same)break;}
 vector<int> col(c,c+n);vector<vector<int>> cell(n);for(int i=0;i<n;i++)cell[c[i]].push_back(i);bool any=false;for(auto &v:cell)if(v.size()>1)any=true;if(!any)return {false,col,col};
 int par[9];iota(par,par+n,0);
 int pid[9];iota(pid,pid+n,0);
 function<int(int)> leader=[&](int a){while(pid[a]!=a)a=pid[a];return a;};
 function<void(int,int)> join=[&](int a,int b){a=leader(a);b=leader(b);pid[b]=a;};
 // enumerate mappings by ordered assignment with WL classes and adjacency constraints
 bool used[9]={}; int f[9]; int total=0;
 function<void(int)> dfs=[&](int dep){if(dep==n){total++;for(int i=0;i<n;i++)join(i,f[i]);return;}int i=dep;for(int j=0;j<n;j++){if(used[j]||c[i]!=c[j])continue;bool ok=true;for(int h=0;h<dep;h++)if(e[i][h]!=e[j][f[h]]){ok=false;break;}if(!ok)continue;f[i]=j;used[j]=1;dfs(dep+1);used[j]=0;}};
 dfs(0);
 vector<int> orbit(n);for(int i=0;i<n;i++)orbit[i]=leader(i);
 bool bad=false;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(c[i]==c[j] && leader(i)!=leader(j))bad=true;
 return {bad,col,orbit};}
int main(int argc,char**argv){int maxn=argc>1?atoi(argv[1]):7;for(int n=2;n<=maxn;n++){uint64_t total=1ULL<<(n*(n-1)/2);uint64_t fail=0;uint64_t witness=0; vector<int> c,o;for(uint64_t z=0;z<total;z++){auto r=check(n,z);if(r.bad){if(!fail){witness=z;c=r.col;o=r.orbit;}fail++;}}cout<<"n="<<n<<" labeled_with_root0="<<total<<" bad="<<fail<<"\n";if(fail){cout<<"first mask="<<witness<<" col=";for(int x:c)cout<<x<<",";cout<<" orbit=";for(int x:o)cout<<x<<",";cout<<"\n";}cout.flush();}}
