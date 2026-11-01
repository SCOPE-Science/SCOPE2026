// Exact modular linear-algebra checks for two-token cocktail-party graphs.
// C++17: c++ -std=c++17 -O2 verify_modular.cpp -o verify_modular && ./verify_modular
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
ll pw(ll a,ll b,ll p){ll t=1;while(b){if(b&1)t=t*a%p;a=a*a%p;b>>=1;}return t;}
int rank_mod(vector<vector<ll>> a,ll p){
 int h=a.size(),w=a[0].size(),r=0;
 for(int c=0;c<w && r<h;++c){int piv=r;while(piv<h && a[piv][c]==0)++piv;
  if(piv==h)continue;swap(a[piv],a[r]);ll inv=pw(a[r][c],p-2,p);
  for(int j=c;j<w;++j)a[r][j]=a[r][j]*inv%p;
  for(int i=r+1;i<h;++i){ll t=a[i][c];if(!t)continue;
    for(int j=c;j<w;++j){a[i][j]=(a[i][j]-t*a[r][j]%p+p)%p;}}
  ++r;
 }
 return r;
}
ll det_mod(vector<vector<ll>> a,ll p){
 int n=a.size();ll d=1;
 for(int c=0;c<n;++c){int piv=c;while(piv<n && a[piv][c]==0)++piv;
  if(piv==n)return 0;
  if(piv!=c){swap(a[piv],a[c]);d=(p-d)%p;}
  ll v=a[c][c];d=d*v%p;ll inv=pw(v,p-2,p);
  for(int i=c+1;i<n;++i){ll t=a[i][c]*inv%p;
    if(!t)continue;
    for(int j=c;j<n;++j)a[i][j]=(a[i][j]-t*a[c][j]%p+p)%p;}
 }
 return d;
}
int main(){
 const ll primes[]={1000003,1000033};
 for(int m=2;m<=8;++m){
  int n=2*m;vector<pair<int,int>> state;
  vector<vector<int>> idx(n,vector<int>(n,-1));
  for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){int z=state.size();idx[i][j]=idx[j][i]=z;state.push_back({i,j});}
  int N=state.size();vector<vector<ll>> L(N,vector<ll>(N,0));
  for(int x=0;x<N;++x){auto [a,b]=state[x];
   for(int c=0;c<n;++c){
    if(c!=a && c!=b && c/2!=a/2){int y=idx[c][b];L[x][y]=-1;L[x][x]++;}
    if(c!=a && c!=b && c/2!=b/2){int y=idx[a][c];L[x][y]=-1;L[x][x]++;}
   }
  }
  map<int,int> expected;
  int k=m*(m-1)/2;
  vector<pair<int,int>> groups={{0,1},{2*m,m-1},{2*m-2,m},{4*m-4,m*(m-2)},{4*m-6,k},{4*m-2,k}};
  for(auto [e,mult]:groups)expected[e]+=mult;
  assert(accumulate(expected.begin(),expected.end(),0,[](int s, auto x){return s+x.second;})==N);
  for(int x=0;x<N;++x){ll rowsum=0;for(int y=0;y<N;++y){assert(L[x][y]==L[y][x]);rowsum+=L[x][y];}assert(!rowsum);}
  for(ll p:primes){
   for(auto [e,mult]:expected){auto M=L;
    for(int x=0;x<N;++x)for(int y=0;y<N;++y)M[x][y]=(M[x][y]%p+p)%p;
    for(int x=0;x<N;++x)M[x][x]=(M[x][x]+p-(e%p))%p;
    int nul=N-rank_mod(move(M),p);if(nul!=mult){cerr<<"NULLITY_FAIL m="<<m<<" eigen="<<e<<" expected="<<mult<<" got="<<nul<<"\n";return 1;}
   }
   vector<vector<ll>> K(N-1,vector<ll>(N-1));
   for(int i=0;i<N-1;++i)for(int j=0;j<N-1;++j)K[i][j]=(L[i][j]%p+p)%p;
   ll actual=det_mod(move(K),p),prod=1;
   for(auto [e,mult]:expected)if(e){prod=prod*pw(e,mult,p)%p;}
   ll predicted=prod*pw(N,p-2,p)%p;
   if(predicted!=actual){cerr<<"TREE_FAIL "<<m<<"\n";return 1;}
  }
  cout<<"MODULAR_PASS m="<<m<<" vertices="<<N<<" edges="
      <<([&](){ll t=0;for(int i=0;i<N;++i)t+=L[i][i];return t/2;})()
      <<" eigenvalues="<<expected.size()<<" primes=2\n";
 }
 cout<<"INDEPENDENT_MODULAR_ALL_PASS\n";
}
