// Standalone finite modular cross-check: edge-based construction rather than token moves.
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using ll=long long;
static const ll P=1000000007LL;
ll modpow(ll a,ll e){ll r=1; for(;e;e>>=1,a=a*a%P)if(e&1)r=r*a%P;return r;}
int rank_mod(vector<vector<ll>> a){int N=a.size(),C=a[0].size(),r=0;for(int j=0;j<C&&r<N;j++){
 int i=r;while(i<N&&a[i][j]==0)i++;if(i==N)continue;swap(a[i],a[r]);
 ll q=modpow(a[r][j],P-2);for(int k=j;k<C;k++)a[r][k]=a[r][k]*q%P;
 for(int h=r+1;h<N;h++)if(a[h][j]){ll w=a[h][j];for(int k=j;k<C;k++)a[h][k]=(a[h][k]-w*a[r][k]%P+P)%P;}
 r++;}
 return r;}
ll determinant(vector<vector<ll>> a){int N=a.size();ll result=1;for(int j=0;j<N;j++){
 int i=j;while(i<N&&!a[i][j])i++;if(i==N)return 0;if(i!=j){swap(a[i],a[j]);result=(P-result)%P;}
 ll pivot=a[j][j];result=result*pivot%P;ll inv=modpow(pivot,P-2);
 for(int h=j+1;h<N;h++)if(a[h][j]){ll w=a[h][j]*inv%P;for(int k=j;k<N;k++)a[h][k]=(a[h][k]-w*a[j][k]%P+P)%P;}}
 return result;}
void check(int m,int n){int t=m+n;int N=t*(t-1)/2;vector<pair<int,int>> pairs;map<pair<int,int>,int> index;
 for(int u=0;u<t;u++)for(int v=u+1;v<t;v++){index[{u,v}]=pairs.size();pairs.push_back({u,v});}
 vector<vector<ll>> L(N,vector<ll>(N,0));int E=0;
 // Construct through edges of the base graph, choosing a stationary third vertex.
 for(int a=0;a<m;a++)for(int b=m;b<t;b++)for(int c=0;c<t;c++)if(c!=a&&c!=b){
  int x=index[{min(a,c),max(a,c)}],y=index[{min(b,c),max(b,c)}];
  L[x][x]++;L[y][y]++;L[x][y]=P-1;L[y][x]=P-1;E++;}
 if(E!=(t-2)*m*n)throw runtime_error("bad edge census");
 map<int,int> expect;
 auto add=[&](int e,int count){expect[e]+=count;};
 add(0,1);add(t,1);add(2*t-2,1);
 add(2*n,m*(m-3)/2);add(2*m,n*(n-3)/2);add(t-2,(m-1)*(n-1));
 add(n,m-1);add(m+2*n-2,m-1);add(m,n-1);add(2*m+n-2,n-1);
 int counted=0;
 for(auto [ev,mult]:expect){if(!mult)continue; auto A=L;for(int i=0;i<N;i++)A[i][i]=(A[i][i]-ev+P)%P;
  int nullity=N-rank_mod(A);if(nullity!=mult){cerr<<m<<','<<n<<" ev="<<ev<<" got="<<nullity<<" expected="<<mult<<'\n';throw runtime_error("wrong multiplicity");}
  counted+=mult;
 }
 if(counted!=N)throw runtime_error("wrong total dimension");
 ll tau=4;
 auto factor=[&](ll base,int exponent){tau=tau*modpow(base,exponent)%P;};
 factor(2*n,m*(m-3)/2);factor(2*m,n*(n-3)/2);factor(t-2,(m-1)*(n-1));
 factor(ll(n)*(m+2*n-2),m-1);factor(ll(m)*(2*m+n-2),n-1);
 auto A=L;A.pop_back();for(auto &r:A)r.pop_back();if(determinant(A)!=tau)throw runtime_error("tree cofactor mismatch");
 cout<<"ALTERNATE_MODULAR_OK m="<<m<<" n="<<n<<" N="<<N<<" edges="<<E<<" distinct_eigenvalues="<<expect.size()<<'\n';
}
int main(){try{for(auto [m,n]:vector<pair<int,int>>{{3,3},{3,4},{3,5},{4,4},{4,5},{5,5},{5,6},{6,7}})check(m,n);cout<<"ALTERNATE_CERTIFICATE_OK\n";}catch(exception&e){cerr<<e.what()<<'\n';return 1;}}
