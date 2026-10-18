// Standalone finite-field verification of idempotent derivation rank spectra.
// C++17; build: g++ -O2 -std=c++17 verify_idempotent.cpp -o verify && ./verify
#include <iostream>
#include <vector>
#include <map>
#include <stdexcept>
#include <cstdint>
using namespace std;
using Mat=vector<vector<int>>;
int mod(int x,int q){x%=q;return x<0?x+q:x;}
Mat mul(const Mat&A,const Mat&B,int q){int n=A.size();Mat C(n,vector<int>(n));for(int i=0;i<n;i++)for(int j=0;j<n;j++)for(int k=0;k<n;k++) C[i][j]=mod(C[i][j]+A[i][k]*B[k][j],q);return C;}
int rankm(Mat A,int q){int n=A.size(),r=0;for(int j=0;j<n;j++){int p=r;while(p<n&&!A[p][j])p++;if(p==n)continue;swap(A[r],A[p]);int inv=1;while(mod(inv*A[r][j],q)!=1) inv++;for(int k=j;k<n;k++)A[r][k]=mod(A[r][k]*inv,q);for(int i=0;i<n;i++)if(i!=r&&A[i][j]){int c=A[i][j];for(int k=j;k<n;k++)A[i][k]=mod(A[i][k]-c*A[r][k],q);}r++;}return r;}
long long binom(int a,int b){if(b<0||b>a)return 0;long long z=1;for(int i=1;i<=b;i++)z=z*(a-i+1)/i;return z;}
long long gauss(int n,int r,int q){if(r<0||r>n)return 0;if(r==0||r==n)return 1;return gauss(n-1,r-1,q)+([&](){long long b=1;for(int i=0;i<r;i++)b*=q;return b*gauss(n-1,r,q);}()); }
long long pw(int q,int e){long long z=1;while(e-->0)z*=q;return z;}
map<int,long long> predicted(int n,int q){map<int,long long> v;for(int r=0;r<=n;r++){if(q%2&&r>1)continue;int s=n-r;int e=r*s+(q%2 ? r*(int(binom(s,2))+s*s) : r*(int(binom(r,2)+binom(s,2))+s*s));v[r*(s+1)]+=gauss(n,r,q)*pw(q,e);}return v;}
map<int,long long> check(int n,int q){int k=n*(n-1)/2,N=n+k; long long limA=pw(q,n*n),limF=pw(q,k*n);map<int,long long> res;vector<pair<int,int>> ij;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ij.emplace_back(i,j);
 for(long long a=0;a<limA;a++){Mat A(n,vector<int>(n));long long z=a;for(int i=0;i<n;i++)for(int j=0;j<n;j++){A[i][j]=z%q;z/=q;}Mat B(k,vector<int>(k));for(int t=0;t<k;t++){auto [i,j]=ij[t];for(int u=0;u<k;u++){auto [v,w]=ij[u];B[t][u]=mod(A[i][v]*(j==w)-A[j][v]*(i==w)+A[j][w]*(i==v)-A[i][w]*(j==v),q);}}
 // B[u] expresses D(e_v wedge e_w); coefficient of e_i wedge e_j
 // Equal formula A[i][v]1_{j=w}-A[j][v]1_{i=w}+A[j][w]1_{i=v}-A[i][w]1_{j=v}.
 Mat AA=mul(A,A,q), BB=mul(B,B,q); bool aok=AA==A && BB==B; if(!aok)continue;
 for(long long f=0;f<limF;f++){Mat D(N,vector<int>(N));for(int i=0;i<n;i++)for(int j=0;j<n;j++)D[i][j]=A[i][j];for(int i=0;i<k;i++)for(int j=0;j<k;j++)D[n+i][n+j]=B[i][j];long long x=f;for(int i=0;i<k;i++)for(int j=0;j<n;j++){D[n+i][j]=x%q;x/=q;}
 if(mul(D,D,q)==D)res[rankm(D,q)]++;
 }
 }
 return res;}
int main(){for(auto [n,q]:vector<pair<int,int>>{{2,2},{2,3},{2,5},{3,2},{3,3}}){auto got=check(n,q), exp=predicted(n,q);cout<<"n="<<n<<" q="<<q<<" observed:";for(auto [r,x]:got)cout<<" "<<r<<":"<<x;cout<<" expected:";for(auto [r,x]:exp)cout<<" "<<r<<":"<<x;cout<<"\n";if(got!=exp)throw runtime_error("Mismatch!");}cout<<"VERIFY_OK_IDEMPOTENT_FREE_CLASS2\n";}
