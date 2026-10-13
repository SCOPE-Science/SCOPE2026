// Finite-field verification of the rank-two square-zero anticommuting fiber.
// Build: g++ -O3 -std=c++17 -o verify verify.cpp
#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <stdexcept>
#include <vector>
using namespace std;

static int Q=2;
inline int add(int a,int b){return Q==4 ? (a^b) : (a+b)%Q;}
inline int neg(int a){return Q==4 ? a : (Q-a)%Q;}
inline int mul(int a,int b){
 if(Q!=4) return (a*b)%Q;
 int z=0;
 for(int i=0;i<2;++i){if(b&1)z^=a; b>>=1; a<<=1; if(a&4)a^=7;}
 return z;
}

static int rankmat(const int M[6][6],int n){
 int a[6][6]={};
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=M[i][j];
 int r=0;
 for(int c=0;c<n;c++){
  int piv=r;
  while(piv<n&&!a[piv][c])++piv;
  if(piv==n)continue;
  for(int j=c;j<n;j++)swap(a[piv][j],a[r][j]);
  int inv=0;
  for(int k=1;k<Q;k++)if(mul(k,a[r][c])==1){inv=k;break;}
  if(!inv)throw runtime_error("No inverse");
  for(int j=c;j<n;j++)a[r][j]=mul(a[r][j],inv);
  for(int i=r+1;i<n;i++){
   int fact=a[i][c];
   if(fact)for(int j=c;j<n;j++)a[i][j]=add(a[i][j],neg(mul(fact,a[r][j])));
  }
  ++r;
  if(r==n)break;
 }
 return r;
}
static void verify_case(int q,int n){
 Q=q;int s=n-4;
 int exponents=8+4*s+s*s;
 uint64_t possibilities=1;
 for(int i=0;i<exponents;i++)possibilities*=q;
 int X[6][6]={};for(int i=0;i<2;i++)X[i][2+i]=1;
 uint64_t c0=0,c1=0,other=0,valid=0;
 for(uint64_t id=0;id<possibilities;id++){
  uint64_t v=id; int P[2][2]={},B[2][2]={},R[2][2]={},W[2][2]={},Z[2][2]={};
  for(int i=0;i<2;i++)for(int j=0;j<2;j++){P[i][j]=v%q;v/=q;}
  for(int i=0;i<2;i++)for(int j=0;j<2;j++){B[i][j]=v%q;v/=q;}
  for(int i=0;i<2;i++)for(int j=0;j<s;j++){R[i][j]=v%q;v/=q;}
  for(int i=0;i<s;i++)for(int j=0;j<2;j++){W[i][j]=v%q;v/=q;}
  for(int i=0;i<s;i++)for(int j=0;j<s;j++){Z[i][j]=v%q;v/=q;}
  int Y[6][6]={};
  for(int i=0;i<2;i++)for(int j=0;j<2;j++){
   Y[i][j]=P[i][j];Y[i][2+j]=B[i][j];Y[2+i][2+j]=neg(P[i][j]);
  }
  for(int i=0;i<2;i++)for(int j=0;j<s;j++)Y[i][4+j]=R[i][j];
  for(int i=0;i<s;i++)for(int j=0;j<2;j++)Y[4+i][2+j]=W[i][j];
  for(int i=0;i<s;i++)for(int j=0;j<s;j++)Y[4+i][4+j]=Z[i][j];
  bool sq0=true;
  for(int i=0;i<n&&sq0;i++)for(int j=0;j<n&&sq0;j++){
   int z=0;for(int k=0;k<n;k++)z=add(z,mul(Y[i][k],Y[k][j]));
   if(z)sq0=false;
  }
  if(!sq0)continue;
  valid++;
  int XY[6][6]={};
  for(int i=0;i<n;i++)for(int j=0;j<n;j++){
   int yx=0;
   for(int k=0;k<n;k++){
    XY[i][j]=add(XY[i][j],mul(X[i][k],Y[k][j]));
    yx=add(yx,mul(Y[i][k],X[k][j]));
   }
   if(add(XY[i][j],yx))throw runtime_error("Anti-commutation failure");
  }
  int k=rankmat(XY,n);
  if(k==0)c0++;else if(k==1)c1++;else other++;
 }
 printf("GF(%d), n=%d: checked=%llu, valid=%llu, rank(XY)=0:%llu, rank(XY)=1:%llu, other:%llu\n",
 q,n,(unsigned long long)possibilities,(unsigned long long)valid,
 (unsigned long long)c0,(unsigned long long)c1,(unsigned long long)other);
 if(other)throw runtime_error("Unexpected product rank");
 // Independent formula: for n=4,5,6 the nonzero-product sums simplify.
 uint64_t wanted=0;
 if(n==4)wanted=(uint64_t)(q*q-1)*q*q;
 if(n==5)wanted=(uint64_t)(q*q-1)*q*q*q*q;
 if(n==6)wanted=(uint64_t)(q*q-1)*q*q*q*q*q*q*q*q;
 if(c1!=wanted){printf("Expected %llu\n",(unsigned long long)wanted); throw runtime_error("Count disagrees with formula");}
}
int main(){
 verify_case(2,4);
 verify_case(3,4);
 verify_case(4,4);
 verify_case(5,4);
 verify_case(2,5);
 verify_case(3,5);
 verify_case(2,6);
 puts("VERIFY_OK_ANTI_RANK2_NONZERO_PRODUCT");
}
