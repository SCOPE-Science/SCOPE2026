#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
using u64=unsigned long long;
int det3(const int a[3][3]) {return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);}
u64 choose(int n,int k){if (k<0 || k>n) return 0;u64 v=1;for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v;}
int main(){for(int d=3;d<=4;d++){
 const int N=1<<d;std::vector<std::array<int,4>> sets;for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int e=c+1;e<N;e++)sets.push_back({a,b,c,e});
 u64 rank[5]={}, det8=0,det16=0, plane_r=0,tetra_r=0;
 for(auto &R:sets){bool plane=(R[0]^R[1]^R[2]^R[3])==0; (plane?plane_r:tetra_r)++;
  for(auto &C:sets){int a[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++) a[i][j]=__builtin_parity((R[i+1]^R[0])&(C[j+1]^C[0]));
   int determinant=det3(a),k=0;
   if(determinant!=0)k=3;
   else { for(int i=0;i<3;i++)for(int j=0;j<3;j++)for(int ii=i+1;ii<3;ii++)for(int jj=j+1;jj<3;jj++)if(a[i][j]*a[ii][jj]-a[i][jj]*a[ii][j])k=2;
    if(k==0)for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(a[i][j])k=1;
   }
   rank[k+1]++;
   if(determinant<0)determinant=-determinant;
   if(determinant==1) det8++;
   if(determinant==2) det16++;
   if(determinant>2){puts("Bad determinant");return 1;}
  }
 }
 u64 P=(u64)N*(N-1)*(N-2)/24,T=choose(N,4)-P;
 u64 u=N/4,v=N/8;
 std::array<u64,5> expected={0, P*4*choose(u,4)+T*8*choose(v,4),P*6*(2*u*choose(u,3)+choose(u,2)*choose(u,2))+T*28*(2*v*choose(v,3)+choose(v,2)*choose(v,2)),P*12*choose(u,2)*u*u+T*(168*choose(v,2)*v*v+12*v*v*v*v),P*u*u*u*u+T*58*v*v*v*v};
 if(plane_r!=P||tetra_r!=T){puts("type mismatch");return 1;}
 for(int j=1;j<=4;j++)if(rank[j]!=expected[j]){printf("rank mismatch n=%d k=%d observed=%llu expected=%llu\n",N,j,rank[j],expected[j]);return 1;}
 if(det8!=T*56*v*v*v*v || det16!=P*u*u*u*u+T*2*v*v*v*v){puts("det mismatch");return 1;}
 printf("PASS: N=%d, row_types=(%llu,%llu), rank=(%llu,%llu,%llu,%llu), |det|8=%llu, |det|16=%llu\n",N,P,T,rank[1],rank[2],rank[3],rank[4],det8,det16);
}return 0;}
