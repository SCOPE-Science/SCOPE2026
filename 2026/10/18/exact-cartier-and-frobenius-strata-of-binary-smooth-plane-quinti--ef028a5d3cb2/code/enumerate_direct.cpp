// Exhaustive independent coefficient-space verification over the field of two elements.
#include <array>
#include <vector>
#include <map>
#include <tuple>
#include <cstdint>
#include <cstdio>
#include <chrono>
using namespace std;
using U=__uint128_t;
struct E {int a,b,c;};
static vector<E> M[11];
static int ind[11][11][11];
static int DD[3][21], shiftindex[28][15], Hpos[6][6];
static int pointpoly[7][21];
static int rk6(const array<unsigned,6>& R){
 unsigned basis[6]{};int rank=0;
 for(unsigned row:R){for(int j=5;j>=0;j--){if(!(row & (1u<<j)))continue;if(basis[j])row^=basis[j];else {basis[j]=row;++rank;break;}}}return rank;
}
static array<unsigned,6> prod(const array<unsigned,6>& X,const array<unsigned,6>& Y){
 array<unsigned,6>Z{};for(int i=0;i<6;i++)for(int j=0;j<6;j++)if(X[i]>>j&1)Z[i]^=Y[j];return Z;
}
int main(){auto start=chrono::steady_clock::now();
 for(int d=0;d<=10;d++)for(int a=d;a>=0;--a)for(int b=d-a;b>=0;--b){int c=d-a-b;ind[d][a][b]=M[d].size();M[d].push_back({a,b,c});}
 for(int t=0;t<21;t++){auto e=M[5][t];DD[0][t]=e.a%2?ind[4][e.a-1][e.b]:-1;DD[1][t]=e.b%2?ind[4][e.a][e.b-1]:-1;DD[2][t]=e.c%2?ind[4][e.a][e.b]:-1;}
 for(int i=0;i<28;i++)for(int j=0;j<15;j++){auto e=M[6][i],h=M[4][j];shiftindex[i][j]=ind[10][e.a+h.a][e.b+h.b];}
 vector<E> interior;for(int a=1;a<5;a++)for(int b=1;b<5-a;b++){int c=5-a-b;if(c>=1)interior.push_back({a,b,c});}
 if(interior.size()!=6)return 10;
 for(int i=0;i<6;i++)for(int j=0;j<6;j++){
 auto x=interior[i],y=interior[j];int a=2*x.a-y.a,b=2*x.b-y.b,c=2*x.c-y.c;Hpos[i][j]=(a>=0&&b>=0&&c>=0)?ind[5][a][b]:-1;}
 for(int P=1;P<8;P++)for(int m=0;m<21;m++){
 auto e=M[5][m];pointpoly[P-1][m]=((e.a==0)||((P&1)!=0)) && ((e.b==0)||((P&2)!=0)) && ((e.c==0)||((P&4)!=0));}
 map<pair<int,int>,long long> C; long long smooth=0;
 for(unsigned F=1;F<(1u<<21);F++){
  unsigned deriv[3]={0,0,0};unsigned q=F;
  while(q){int k=__builtin_ctz(q);q&=q-1;for(int v=0;v<3;v++)if(DD[v][k]>=0)deriv[v]^=(1u<<DD[v][k]);}
  U basis[66]{};int rank=0;
  for(int v=0;v<3;v++){
   if(rank==66)break;
   for(int j=0;j<28;j++){
     U w=0;unsigned r=deriv[v];
     while(r){int k=__builtin_ctz(r);r&=r-1;w^=((U)1<<shiftindex[j][k]);}
     for(int k=65;k>=0;k--){if(!(w & ((U)1<<k)))continue;if(basis[k])w^=basis[k];else {basis[k]=w;rank++;break;}}
     if(rank==66)break;
   }
  }
  if(rank!=66)continue;
  smooth++;
  array<unsigned,6>H{};
  for(int i=0;i<6;i++)for(int j=0;j<6;j++){int t=Hpos[i][j];if(t>=0&&(F&(1u<<t)))H[i]^=1u<<j;}
  int a=6-rk6(H);array<unsigned,6>P=H;
  for(int t=1;t<6;t++)P=prod(P,H);
  int p=rk6(P);
  C[{p,a}]++;
 }
 printf("direct_smooth=%lld\n",smooth);
 for(auto c:C)printf("p=%d a=%d count=%lld\n",c.first.first,c.first.second,c.second);
 auto ss=chrono::duration<double>(chrono::steady_clock::now()-start).count();fprintf(stderr,"direct_seconds=%.3f\n",ss);
}
