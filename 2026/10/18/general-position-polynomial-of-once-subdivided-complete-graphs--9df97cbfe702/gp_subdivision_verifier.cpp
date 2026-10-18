// Independent shortest-path and combinatorial classification checks.
// Build: c++ -O3 -std=c++17 gp_subdivision_verifier.cpp -o verifier && ./verifier
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
long long binom(int n,int k){if(k<0||k>n)return 0; long long a=1;for(int i=1;i<=k;i++)a=a*(n-k+i)/i;return a;}
long long factorial(int n){long long r=1;for(int i=2;i<=n;i++)r*=i;return r;}
int main(){long long examined=0,accepted=0;for(int n=3;n<=6;n++){
 vector<pair<int,int>> ed;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ed.push_back({i,j});
 int m=ed.size(),N=n+m;vector<vector<int>> adj(N);
 for(int e=0;e<m;e++){int a=ed[e].first,b=ed[e].second;adj[a].push_back(n+e);adj[b].push_back(n+e);adj[n+e].push_back(a);adj[n+e].push_back(b);}
 vector<vector<int>> d(N,vector<int>(N,999));for(int a=0;a<N;a++){queue<int> q;q.push(a);d[a][a]=0;while(!q.empty()){int v=q.front();q.pop();for(int w:adj[v])if(d[a][w]==999){d[a][w]=d[a][v]+1;q.push(w);}}}
 vector<vector<U>> prohibitedPairs(N);for(int i=0;i<N;i++)for(int j=0;j<i;j++)for(int k=0;k<j;k++)if(d[i][j]+d[j][k]==d[i][k] || d[i][k]+d[k][j]==d[i][j] || d[j][i]+d[i][k]==d[j][k])prohibitedPairs[i].push_back((U(1)<<j)|(U(1)<<k));
 vector<char> p4free(1<<m,1);int motifs=0;
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(b!=a)for(int c=0;c<n;c++)if(c!=a&&c!=b)for(int f=0;f<n;f++)if(f!=a&&f!=b&&f!=c){
  U motif=0;for(int e=0;e<m;e++)if(ed[e]==make_pair(min(a,b),max(a,b))||ed[e]==make_pair(min(b,c),max(b,c))||ed[e]==make_pair(min(c,f),max(c,f)))motif|=U(1)<<e;
  if(__builtin_popcount(motif)!=3)abort();motifs++;
  for(int x=0;x<(1<<m);x++)if((x&motif)==motif)p4free[x]=0;
 }
 vector<char> valid(1<<N,0);valid[0]=1;vector<long long> count(N+1,0);count[0]=1;
 for(U mask=1;mask<(U(1)<<N);mask++){
  int i=31-__builtin_clz(mask);U prev=mask^(U(1)<<i);bool good=valid[prev];
  if(good)for(U pp:prohibitedPairs[i])if((prev&pp)==pp){good=false;break;}
  valid[mask]=good;
  U om=mask&((U(1)<<n)-1),fm=mask>>n;
  bool predicted=false;
  if(__builtin_popcount(om)==1 && __builtin_popcount(fm)==1){int u=__builtin_ctz(om),e=__builtin_ctz(fm);if(ed[e].first==u||ed[e].second==u)predicted=true;}
  if(!predicted){bool touch=false;for(int e=0;e<m;e++)if((fm>>e)&1)if((om>>ed[e].first&1)||(om>>ed[e].second&1)){touch=true;break;}predicted=!touch&&p4free[fm];}
  if(good!=predicted){cerr<<"MISMATCH n="<<n<<" mask="<<mask<<" direct="<<good<<" structural="<<predicted<<"\n";return 2;}
  if(good)count[__builtin_popcount(mask)]++;
 }
 // Use repeated integer multiplication instead of floating computation for result.
 long long max2=0;for(int t=0;3*t<=n;t++){long long den=factorial(n-3*t)*factorial(t);for(int j=0;j<t;j++)den*=6;max2+=factorial(n)/den;}
 if(count[n]!=max2){cerr<<"MAX MISMATCH n="<<n<<" count="<<count[n]<<" predicted="<<max2<<"\n";return 3;}
 for(int k=n+1;k<=N;k++)if(count[k]){cerr<<"ABOVE_MAX n="<<n;return 4;}
 long long subtotal=0;for(long long a:count)subtotal+=a;
 examined+=(1LL<<N);accepted+=subtotal;
 cout<<"n="<<n<<" vertices="<<N<<" tested="<<(1LL<<N)<<" accepted="<<subtotal<<" max="<<n<<" maximum_count="<<max2<<" coefficients:";
 for(int k=0;k<=n;k++)cout<<" "<<count[k];cout<<"\n";
 }
 cout<<"VERIFICATION_OK graph_cases=4 examined_subsets="<<examined<<" accepted="<<accepted<<"\n";
}
