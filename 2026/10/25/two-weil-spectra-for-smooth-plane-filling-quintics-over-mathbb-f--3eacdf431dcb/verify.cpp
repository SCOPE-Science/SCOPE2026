#include <cstdio>
#include <vector>
#include <array>
#include <algorithm>
#include <cassert>
using namespace std;
const int modpoly[7][7]={{},{0,1},{1,0,1},{1,0,2,1},{1,0,1,1,1},{1,0,0,0,2,1},{1,0,0,0,1,1,1}};
const int coefs[8][3]={{0,2,1},{0,2,2},{1,0,2},{1,1,2},{1,2,1},{2,0,1},{2,1,1},{2,2,2}};
int main(){
 const long long expected[6][8]={
  {13,13,13,13,13,13,13,13},
  {13,13,13,13,13,13,13,13},
  {55,55,16,16,16,16,16,16},
  {13,13,117,117,117,117,117,117},
  {208,208,273,273,273,273,273,273},
  {913,913,640,640,640,640,640,640}
 };
 for(int n=1;n<=6;n++){
  int q=1;for(int i=0;i<n;i++)q*=3;
  vector<array<int,6>> ds(q);for(int k=0;k<q;k++){int v=k;for(int i=0;i<n;i++){ds[k][i]=v%3;v/=3;}}
  vector<int> pw(n+1,1);for(int i=1;i<=n;i++)pw[i]=pw[i-1]*3;
  vector<int> add(q*q), mul(q*q);
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int aa=0;for(int i=0;i<n;i++) aa +=((ds[a][i]+ds[b][i])%3)*pw[i];add[a*q+b]=aa;
   int tmp[12]={0};for(int i=0;i<n;i++)for(int j=0;j<n;j++)tmp[i+j]=(tmp[i+j]+ds[a][i]*ds[b][j])%3;
   for(int d=2*n-2;d>=n;d--){int z=tmp[d];if(!z)continue;for(int j=0;j<n;j++)tmp[d-n+j]=(tmp[d-n+j]+3-z*modpoly[n][j]%3)%3;}
   int mm=0;for(int i=0;i<n;i++)mm+=tmp[i]*pw[i];mul[a*q+b]=mm;
  }
  auto A=[&](int x,int y){return add[x*q+y];};
  auto M=[&](int x,int y){return mul[x*q+y];};
  auto N=[&](int x){return A(x,x);};
  auto S=[&](int x,int y){return A(x,N(y));};
  vector<int> p2(q),p3(q),p4(q),ys(q),xs(q);
  for(int a=0;a<q;a++){p2[a]=M(a,a);p3[a]=M(p2[a],a);p4[a]=M(p3[a],a);ys[a]=S(p4[a],p2[a]);xs[a]=S(a,p3[a]);}
  long long counts[8];fill(counts,counts+8,4);
  for(int y=0;y<q;y++)for(int x=0;x<q;x++){
    int xy=S(M(p3[x],y),M(x,p3[y]));
    int base=A(ys[y],xs[x]);
    for(int j=0;j<8;j++){
      int c0=coefs[j][2],c1=coefs[j][1],c2=coefs[j][0];
      int coef=c2;
      for(int z=0;z<c0;z++)coef=A(coef,x);
      for(int z=0;z<c1;z++)coef=A(coef,y);
      if(base==M(coef,xy))counts[j]++;
    }
  }
  for(int j=0;j<8;j++)assert(counts[j]==expected[n-1][j]);
  printf("n=%d q=%d ",n,q);for(int j=0;j<8;j++)printf("%lld%s",counts[j],j==7?"":" ");printf("\n");
 }
  printf("VERIFY_OK\n");
}
