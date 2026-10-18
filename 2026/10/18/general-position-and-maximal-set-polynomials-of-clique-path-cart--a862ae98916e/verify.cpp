#include <bits/stdc++.h>
using namespace std;
using ll=long long;
static ll choose(int a,int b){if(b<0||b>a)return 0;ll x=1;for(int j=1;j<=b;j++)x=x*(a-j+1)/j;return x;}
static ll power(int a,int b){ll x=1;while(b--)x*=a;return x;}
static vector<ll> predicted(int m,int n){
 vector<ll> c(m+2);c[0]=1;
 for(int k=1;k<=m;k++)c[k]+=choose(m,k)*power(n,k);
 for(int k=2;k<=m+1;k++)for(int p=0;p<n;p++)for(int q=p+1;q<n;q++)
  c[k]+=m*choose(m-1,k-2)*power(q-p-1,k-2);
 return c;
}
static bool classified(int mask,int m,int n){
 vector<vector<int>> positions(m);
 for(int v=0;v<m*n;v++)if(mask&(1<<v))positions[v/n].push_back(v%n);
 int repeated=-1;
 for(int a=0;a<m;a++)if(positions[a].size()>1){
  if(positions[a].size()!=2||repeated!=-1)return false;
  repeated=a;
 }
 if(repeated==-1)return true;
 int p=positions[repeated][0],q=positions[repeated][1];
 for(int a=0;a<m;a++)if(a!=repeated)for(int x:positions[a])if(x<=p||x>=q)return false;
 return true;
}
int main(){long long cases=0,subsetMasks=0,matchedValid=0,checkedTwo=0;
for(int m=1;m<=5;m++)for(int n=1;n<=8;n++)if(m*n<=19){
 int N=m*n;vector<vector<int>> adj(N);
 for(int a=0;a<m;a++)for(int i=0;i<n;i++){
  int v=a*n+i;
  for(int b=0;b<m;b++)if(b!=a)adj[v].push_back(b*n+i);
  if(i>0)adj[v].push_back(v-1);
  if(i+1<n)adj[v].push_back(v+1);
 }
 vector<vector<int>> dist(N,vector<int>(N,999));
 for(int s=0;s<N;s++){
  queue<int>q;q.push(s);dist[s][s]=0;
  while(!q.empty()){
   int v=q.front();q.pop();
   for(int w:adj[v])if(dist[s][w]>dist[s][v]+1){dist[s][w]=dist[s][v]+1;q.push(w);}
  }
 }
 vector<vector<pair<int,int>>> bad(N);
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){
  if(dist[a][b]+dist[b][c]==dist[a][c] || dist[a][c]+dist[c][b]==dist[a][b] || dist[b][a]+dist[a][c]==dist[b][c]){
   bad[a].push_back({b,c});bad[b].push_back({a,c});bad[c].push_back({a,b});
  }
 }
 int U=1<<N;vector<uint8_t>gp(U);gp[0]=1;vector<ll> counts(N+1);
 for(int mask=0;mask<U;mask++){
  if(mask){
   int v=__builtin_ctz((unsigned)mask);int rest=mask^(1<<v);
   if(gp[rest]){
    gp[mask]=1;
    for(auto [a,b]:bad[v])if((rest&(1<<a))&&(rest&(1<<b))){gp[mask]=0;break;}
   }
  }
  bool shape=classified(mask,m,n);
  if((bool)gp[mask]!=shape){cerr<<"SHAPE_MISMATCH m="<<m<<" n="<<n<<" mask="<<mask<<"\n";return 1;}
  if(gp[mask]){counts[__builtin_popcount((unsigned)mask)]++;matchedValid++;}
 }
 auto expected=predicted(m,n);
 int largest=0;
 for(int k=0;k<=N;k++){
  if(counts[k]!=(k<(int)expected.size()?expected[k]:0)){
   cerr<<"COEFF_MISMATCH m="<<m<<" n="<<n<<" k="<<k<<" actual="<<counts[k]<<" predicted="<<(k<(int)expected.size()?expected[k]:0)<<"\n";return 1;
  }
  if(counts[k])largest=k;
 }
 if(largest!=(n>=3?m+1:(n==2?max(2,m):m))){cerr<<"MAX_MISMATCH"<<m<<" "<<n<<"\n";return 1;}
 if(m>=3&&n>=3){
  vector<ll> maximal(N+1,0);
  for(int mask=0;mask<U;mask++)if(gp[mask]){
   bool inclusionMaximal=true;
   for(int v=0;v<N;v++)if(!(mask&(1<<v))&&gp[mask|(1<<v)]){inclusionMaximal=false;break;}
   if(inclusionMaximal)maximal[__builtin_popcount((unsigned)mask)]++;
  }
  ll A=m*(n-1),B=power(n,m),C=0;
  for(int h=1;h<=n-2;h++)B-=2LL*m*power(h,m-1);
  for(int h=1;h<=n-4;h++)B+=1LL*m*(m-1)*(n-h-3)*power(h,m-2);
  for(int h=1;h<=n-2;h++)C+=1LL*m*(n-h-1)*power(h,m-1);
  for(int k=0;k<=N;k++){
   ll expectedFacet=(k==2?A:0)+(k==m?B:0)+(k==m+1?C:0);
   if(maximal[k]!=expectedFacet){cerr<<"FACET_MISMATCH m="<<m<<" n="<<n<<" k="<<k<<" got="<<maximal[k]<<" expected="<<expectedFacet<<"\n";return 1;}
  }
  checkedTwo++;
 }
 cases++;subsetMasks+=U;
}
cout<<"VERIFICATION_OK graph_cases="<<cases<<" subsets_tested="<<subsetMasks<<" feasible_subsets="<<matchedValid<<" maximal_pair_cases="<<checkedTwo<<"\n";
}
