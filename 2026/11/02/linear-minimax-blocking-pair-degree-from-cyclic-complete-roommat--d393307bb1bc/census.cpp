#include <bits/stdc++.h>
using namespace std;
constexpr int MAXN=5;
int n,rk[MAXN][MAXN],adj[MAXN][MAXN];
vector<array<int,MAXN>> matchings;
vector<vector<int>> prefs[MAXN];
unsigned long long total=0,no_one=0,no_zero=0,by_edges[11]={},bad_edges[11]={},fullbad=0;
int firstbad[5][5],best_minmax=0;
void matchgen(array<int,MAXN>&p,vector<int>v){if(v.empty()){matchings.push_back(p);return;}int a=v[0];v.erase(v.begin());p[a]=a;matchgen(p,v);for(int j=0;j<(int)v.size();j++){int b=v[j];auto rem=v;rem.erase(rem.begin()+j);p[a]=b;p[b]=a;matchgen(p,rem);}}
int minmax(){int best=MAXN;
 for(auto &M:matchings){bool valid=true;
  for(int i=0;i<n;i++)if(M[i]!=i && !adj[i][M[i]]){valid=false;break;}
  if(!valid)continue;
  int deg[MAXN]{};int md=0;
  for(int i=0;i<n&&md<best;i++)for(int j=i+1;j<n;j++) if(M[i]!=j && adj[i][j] && rk[i][j]<rk[i][M[i]] && rk[j][i]<rk[j][M[j]]){md=max(md,++deg[i]);md=max(md,++deg[j]);if(md>=best)break;}
  best=min(best,md);if(best==0)break;
 }
 return best;
}
void profgen(int i,int ne){if(i==n){int ans=minmax();total++;by_edges[ne]++;if(ans>0)no_zero++;if(ans>1){no_one++;bad_edges[ne]++;if(no_one==1){for(int k=0;k<n;k++)for(int j=0;j<n;j++)firstbad[k][j]=rk[k][j];}}if(ans>2){cerr<<"Found >2!\n";exit(4);}return;}
 for(auto &v:prefs[i]){for(int j=0;j<n;j++)rk[i][j]=n+1;rk[i][i]=n;for(int k=0;k<(int)v.size();k++)rk[i][v[k]]=k;profgen(i+1,ne);}
}
int main(){for(n=1;n<=5;n++){
  total=no_one=no_zero=0;fill(begin(by_edges),end(by_edges),0);fill(begin(bad_edges),end(bad_edges),0);
  matchings.clear();array<int,MAXN>p{};vector<int>v;for(int i=0;i<n;i++)v.push_back(i);matchgen(p,v);
  vector<pair<int,int>>edges;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  for(int mask=0;mask<(1<<(int)edges.size());mask++){
   memset(adj,0,sizeof(adj));int ne=__builtin_popcount((unsigned)mask);
   for(int k=0;k<(int)edges.size();k++)if(mask>>k&1){auto [i,j]=edges[k];adj[i][j]=adj[j][i]=1;}
   for(int i=0;i<n;i++){
    vector<int>w;for(int j=0;j<n;j++)if(adj[i][j])w.push_back(j);
    prefs[i].clear();do{prefs[i].push_back(w);}while(next_permutation(w.begin(),w.end()));
   }
   profgen(0,ne);
  }
  cout<<"n="<<n<<" total="<<total<<" no_zero="<<no_zero<<" minmax_at_least_two="<<no_one<<"\n";
  if(n==5){for(int i=0;i<11;i++)if(by_edges[i])cout<<"edges="<<i<<" profiles="<<by_edges[i]<<" need_two="<<bad_edges[i]<<"\n";cout<<"first witness raw ranks:";for(int i=0;i<n;i++){cout<<"\n";for(int j=0;j<n;j++)cout<<firstbad[i][j]<<" ";}cout<<"\n";}
 }
}
