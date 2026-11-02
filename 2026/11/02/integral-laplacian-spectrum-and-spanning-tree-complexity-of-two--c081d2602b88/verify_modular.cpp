// Independent modular-rank and matrix-tree checks of two-token friendship graphs.
// Build: g++ -O2 -std=c++17 verify_modular.cpp -o verify_modular
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const ll P=1000000007LL;
ll power(ll a, ll b) {ll r=1; for(; b; b>>=1,a=a*a%P)if(b&1)r=r*a%P;return r;}
ll det(vector<vector<ll>> a) {
 int n=a.size();ll v=1;
 for(int c=0;c<n;c++) {
  int p=c;while(p<n && a[p][c]==0)p++;
  if(p==n)return 0;
  if(p!=c){swap(a[p],a[c]); v=(P-v)%P;}
  ll w=a[c][c];v=v*w%P;ll iw=power(w,P-2);
  for(int i=c+1;i<n;i++){
   ll f=a[i][c]*iw%P;
   if(!f)continue;
   for(int j=c+1;j<n;j++) a[i][j]=(a[i][j]-f*a[c][j]%P+P)%P;
   a[i][c]=0;
  }
 }
 return v;
}
int rankmod(vector<vector<ll>> a) {
 int n=a.size(),r=0;
 for(int c=0;c<n && r<n;c++) {
  int p=r;while(p<n && a[p][c]==0)p++;
  if(p==n)continue;
  swap(a[p],a[r]);ll iw=power(a[r][c],P-2);
  for(int i=r+1;i<n;i++){
   ll f=a[i][c]*iw%P;
   if(!f)continue;
   for(int j=c+1;j<n;j++) a[i][j]=(a[i][j]-f*a[r][j]%P+P)%P;
   a[i][c]=0;
  }
  r++;
 }
 return r;
}
int main(){
 for(int m=2;m<=9;m++){
  int v=2*m+1;
  vector<pair<int,int>> base;
  for(int i=0;i<m;i++){
   int a=2*i+1,b=a+1;
   base.push_back({0,a});base.push_back({0,b});base.push_back({a,b});
  }
  vector<pair<int,int>> pairs;map<pair<int,int>,int> index;
  for(int a=0;a<v;a++)for(int b=a+1;b<v;b++){
   index[{a,b}]=(int)pairs.size();pairs.push_back({a,b});
  }
  int N=pairs.size();vector<vector<ll>> L(N,vector<ll>(N,0));ll arc=0;
  for(int i=0;i<N;i++){
   auto [a,b]=pairs[i];
   for(auto [u,w]:base){
    int t=-1,z=-1;
    if(a==u && b!=w){t=w;z=b;}
    else if(a==w && b!=u){t=u;z=b;}
    else if(b==u && a!=w){t=w;z=a;}
    else if(b==w && a!=u){t=u;z=a;}
    if(t<0)continue;
    if(z>t)swap(z,t);
    int j=index.at({z,t});
    if(i==j || L[i][j] != 0) return 2;
    L[i][j]=P-1;L[i][i]++;arc++;
   }
  }
  if(arc != 6LL*m*(2*m-1)) return 3;
  map<int,int> mult;
  int q=m*(m-1)/2;
  auto add=[&](int lambda,int count){if(count)mult[lambda]+=count;};
  add(0,1);add(1,m-1);add(2,q);add(3,m);add(4,m*(m-2));add(6,q);
  add(2*m,m-1);add(2*m+1,1);add(2*m+2,m);
  int sum=0; for(auto [w,k]:mult){sum+=k;
   auto M=L;
   for(int i=0;i<N;i++) M[i][i]=(M[i][i]-w+P)%P;
   int nullity=N-rankmod(std::move(M));
   if(nullity!=k){cerr<<"EIGEN_NULLITY_FAIL "<<m<<" "<<w<<" "<<nullity<<" "<<k<<"\n";return 4;}
  }
  if(sum!=N)return 5;
  auto M=L;M.pop_back();for(auto &row:M)row.pop_back();
  ll t=det(std::move(M));
  ll wanted=power(2,3*m*m-3*m-1)*power(3,m+q)%P;
  wanted=wanted*power(m,m-2)%P*power(m+1,m)%P;
  if(t!=wanted){cerr<<"TREE_FAIL "<<m<<" "<<t<<" "<<wanted<<"\n";return 6;}
  cout<<"MODULAR_OK "<<m<<" "<<N<<" "<<arc/2<<" "<<mult.size()<<"\n";
 }
 cout<<"MODULAR_ALL_PASS\n";
}
