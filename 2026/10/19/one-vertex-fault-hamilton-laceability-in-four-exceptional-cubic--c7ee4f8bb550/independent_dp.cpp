// Independent subset dynamic programming for Hamilton path counts.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using Matrix=vector<vector<int>>;

static Matrix gp(int n,int k){Matrix a(2*n);auto edge=[&](int u,int v){a[u].push_back(v);a[v].push_back(u);};for(int i=0;i<n;i++){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+k)%n);}return a;}
static Matrix pappus(){Matrix a(18);for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int m=0;m<3;m++){int u=3*x+y, b=((y-m*x)%3+3)%3,v=9+3*m+b;a[u].push_back(v);a[v].push_back(u);}return a;}
static Matrix heawood(){Matrix a(14);for(int j=0;j<7;j++)for(int k:{0,1,3}){int u=(j+k)%7,v=7+j;a[u].push_back(v);a[v].push_back(u);}return a;}
static vector<int> bipartite_distance(const Matrix&a){vector<int>d(a.size(),-1);queue<int>q;q.push(0);d[0]=0;while(!q.empty()){int v=q.front();q.pop();for(int w:a[v]){if(d[w]==-1){d[w]=d[v]+1;q.push(w);}else if((d[w]-d[v])%2==0)throw runtime_error("not bipartite");}}return d;}
static vector<uint64_t> hamilton_from(const Matrix&a,int start,int removed){
 const int n=a.size();vector<int>map(n,-1),inv;
 for(int v=0;v<n;v++)if(v!=removed){map[v]=(int)inv.size();inv.push_back(v);}
 int m=inv.size();if(m>20)throw runtime_error("size");
 vector<vector<int>> edges(m);for(int u=0;u<m;u++)for(int v:a[inv[u]])if(map[v]>=0)edges[u].push_back(map[v]);
 size_t rows=size_t(1)<<m;
 vector<uint64_t>dp(rows*m,0),result(n,0);
 int s=map[start];dp[(size_t(1)<<s)*m+s]=1;
 for(size_t mask=0;mask<rows;mask++){
  if(((mask>>s)&1)==0)continue;
  for(int u=0;u<m;u++){
   uint64_t ways=dp[mask*m+u];if(!ways)continue;
   for(int v:edges[u])if(((mask>>v)&1)==0)dp[((mask|(size_t(1)<<v))*m)+v]+=ways;
  }
 }
 for(int v=0;v<n;v++)if(map[v]>=0)result[v]=dp[(rows-1)*m+map[v]];
 return result;
}
static void exercise(const string&name,const Matrix&a){
 auto d=bipartite_distance(a);vector<int>B;for(int v=0;v<(int)a.size();v++)if(d[v]%2==1)B.push_back(v);
 auto complete=hamilton_from(a,0,-1);for(int t:B)if(!complete[t])throw runtime_error("not Hamilton-laceable from 0");
 uint64_t min_positive=UINT64_MAX,max_count=0;int zero=0;vector<pair<int,int>> bad;
 for(int i=0;i<(int)B.size();i++){
  auto r=hamilton_from(a,B[i],0);
  for(int j=i+1;j<(int)B.size();j++){
   uint64_t cnt=r[B[j]];
   if(cnt==0){bad.emplace_back(B[i],B[j]);zero++;}
   else{min_positive=min(min_positive,cnt);max_count=max(max_count,cnt);}
  }
 }
 cout<<name<<" vertices="<<a.size()<<" hamilton_laceable=yes punctured_missing="<<zero;
 for(auto [u,v]:bad)cout<<" ["<<u<<","<<v<<"]";
 cout<<" positive_min="<<min_positive<<" positive_max="<<max_count<<"\n";
 if((name=="Mobius-Kantor")!=(bad==vector<pair<int,int>>{{10,14}}))throw runtime_error("unexpected missing pairs");
}
int main(){exercise("Heawood",heawood());exercise("Mobius-Kantor",gp(8,3));exercise("Pappus",pappus());exercise("Desargues",gp(10,3));}
