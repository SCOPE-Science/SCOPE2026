#include <bits/stdc++.h>
using namespace std;
long long formula(int n, const vector<pair<int,int>>& E){
 vector<vector<int>> adj(n); vector<int>d(n);
 for(auto [u,v]:E){adj[u].push_back(v);adj[v].push_back(u);d[u]++;d[v]++;}
 bool unic=(int)E.size()==n;
 if(!unic){long long a=3;for(int x:d)a*=((1LL<<x)-1);return a;}
 vector<int>alive(n,1),dd=d; queue<int>q;for(int i=0;i<n;i++)if(dd[i]==1)q.push(i);
 while(!q.empty()){int u=q.front();q.pop();alive[u]=0;for(int v:adj[u])if(alive[v]&&--dd[v]==1)q.push(v);}
 map<int,long long> coef{{0,1}};
 long long prod=3;
 for(int v=0;v<n;v++)if(!alive[v])prod*=(1LL<<d[v])-1;
 for(int v=0;v<n;v++)if(alive[v]){
  int r=d[v]-2;long long a=(1LL<<(r+1))-1,b=1LL<<r;
  map<int,long long>t;
  for(auto [k,x]:coef){t[k]+=a*x;t[k-1]+=b*x;t[k+1]+=b*x;}
  coef.swap(t);
 }
 return prod*coef[0];
}
long long brute(int n,const vector<pair<int,int>>&E){
 int m=E.size();vector<vector<int>>nb(m);
 for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){
 auto [a,b]=E[i];auto [c,d]=E[j];if(a==c||a==d||b==c||b==d)nb[i].push_back(j);
 }
 long long r=0,states=1;for(int i=0;i<m;i++)states*=3;
 for(int mask=0;mask<states;mask++){
  vector<int>x(m),y(m);int z=mask;for(int i=0;i<m;i++){x[i]=z%3;z/=3;}
  for(int t=0;t<=n+1;t++){
   bool same=true;for(int i=1;i<m;i++)if(x[i]!=x[0]){same=false;break;}
   if(same){r++;break;}
   if(t==n+1)break;
   for(int i=0;i<m;i++){
    int want=(x[i]+1)%3;bool adv=false;
    for(int j:nb[i])if(x[j]==want){adv=true;break;}
    y[i]=adv?want:x[i];
   }
   x.swap(y);
  }
 }
 return r;
}
int main(){long long ngraphs=0,nstates=0,unun=0;
 for(int n=2;n<=6;n++){
  vector<pair<int,int>> possible;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)possible.push_back({i,j});
  int nt=possible.size();
  for(int mask=0;mask<(1<<nt);mask++){
   int m=__builtin_popcount((unsigned)mask);if(m!=n-1&&m!=n)continue;
   vector<pair<int,int>>E;vector<int>parent(n);iota(parent.begin(),parent.end(),0);
   auto root=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
   for(int k=0;k<nt;k++)if(mask>>k&1){auto [u,v]=possible[k];E.push_back({u,v});parent[root(u)]=root(v);}
   bool connected=true;for(int i=1;i<n;i++)if(root(i)!=root(0)){connected=false;break;}
   if(!connected)continue;
   auto a=formula(n,E),b=brute(n,E);
   if(a!=b){cerr<<"FAIL n="<<n<<" mask="<<mask<<" formula="<<a<<" brute="<<b<<"\n";return 1;}
   ngraphs++;long long count=1;for(int k=0;k<m;k++)count*=3;nstates+=count;if(m==n)unun++;
  }
 }
 cout<<"PASS labelled_graphs="<<ngraphs<<" unicyclic_graphs="<<unun<<" initial_states="<<nstates<<" n_le_6\n";
}
