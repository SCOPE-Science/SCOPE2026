// Reproducible exact arithmetic verification for a theorem on degree-six places.
// Compile: g++ -O2 -std=c++17 verify_quadrics.cpp -o verify_quadrics
// Run: ./verify_quadrics
// Enumerates all cubic sections modulo the quadric equation, for all
// three rational canonical-quadric types over F_2.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

// F_64 = F_2[u]/(u^6+u+1), represented by six-bit integers.
int mul(int a,int b) { int r=0; while(b){ if(b&1)r^=a; b>>=1; a<<=1; if(a&64)a^=0x43; } return r; }
int power(int a,int n) { int r=1; while(n){if(n&1)r=mul(r,a);a=mul(a,a);n>>=1;} return r; }
const array<array<int,4>,16> exps=[](){
 array<array<int,4>,16> ans{};int z=0;
 for(int i=3;i>=0;--i)for(int j=3-i;j>=0;--j)
  for(int k=3-i-j;k>=0;--k){int l=3-i-j-k;if(i&&j)continue;ans[z++]={i,j,k,l};}
 assert(z==16);return ans;
}();
int quad(int type,const array<int,4>&x) {
 int v=mul(x[0],x[1]);
 if(type==0)return v^mul(x[2],x[3]);              // split
 if(type==1)return v^mul(x[2],x[2])^mul(x[2],x[3])^mul(x[3],x[3]); // nonsplit
 return v^mul(x[2],x[2]);                           // rank-three cone
}
// Check an explicitly indicated F_2-rational singularity of Q=F=0.
bool singular(int type,int mask,array<int,4> x){
 assert(type==1);
 int F=0,grad[4]={},gradQ[4]={x[1],x[0],x[3],x[2]};
 for(int k=0;k<16;k++)if((mask>>k)&1){
  int t=1;
  for(int j=0;j<4;j++)for(int r=0;r<exps[k][j];r++)t*=x[j];
  F^=t;
  for(int j=0;j<4;j++)if(exps[k][j]&1){
   int p=1;
   for(int a=0;a<4;a++)for(int r=0;r<exps[k][a]-(a==j);r++)p*=x[a];
   grad[j]^=p;
  }
 }
 if(F||quad(type,x))return false;
 for(int j=0;j<4;j++)for(int k=j+1;k<4;k++)
  if((grad[j]*gradQ[k])^(grad[k]*gradQ[j]))return false;
 return true;
}

void test_type(int type){
 vector<int> N1(65536),N2(65536),N3(65536),N6(65536);
 int pts[4]={},powers[64][3];
 for(int a=0;a<64;a++){powers[a][0]=power(a,2);powers[a][1]=power(a,4);powers[a][2]=power(a,8);}
 auto point=[&](array<int,4>x){
  if(quad(type,x))return;
  bool in1=true,in2=true,in3=true;
  for(int a:x){if(powers[a][0]!=a)in1=false;if(powers[a][1]!=a)in2=false;if(powers[a][2]!=a)in3=false;}
  ++pts[3]; if(in1)++pts[0];if(in2)++pts[1];if(in3)++pts[2];
  int p[4][4]={};
  for(int j=0;j<4;j++){p[j][0]=1;for(int k=1;k<=3;k++)p[j][k]=mul(p[j][k-1],x[j]);}
  int val[16];for(int k=0;k<16;k++){int r=1;for(int j=0;j<4;j++)r=mul(r,p[j][exps[k][j]]);val[k]=r;}
  int v=0;
  for(int step=1;step<65536;step++){
   v^=val[__builtin_ctz((unsigned)step)];
   if(v==0){int mask=step^(step>>1);++N6[mask];if(in1)++N1[mask];if(in2)++N2[mask];if(in3)++N3[mask];}
  }
 };
 point({1,0,0,0});
 for(int a=0;a<64;a++)point({a,1,0,0});
 for(int a=0;a<64;a++)for(int b=0;b<64;b++)point({a,b,1,0});
 for(int a=0;a<64;a++)for(int b=0;b<64;b++)for(int c=0;c<64;c++)point({a,b,c,1});
 const int expected[3][4]={{9,25,81,4225},{5,25,65,4225},{7,21,73,4161}};
 for(int i=0;i<4;i++)assert(pts[i]==expected[type][i]);
 int minimum=10000,zeros=0,zero_masks[5]={},z=0;
 for(int mask=1;mask<65536;mask++){
  int d=N6[mask]-N3[mask]-N2[mask]+N1[mask];
  assert(d>=0 && d%6==0); int b=d/6;
  if(b<minimum)minimum=b;
  if(b==0){++zeros;assert(z<5);zero_masks[z++]=mask;}
 }
 const int min_expected[]={1,0,2};const int zeros_expected[]={0,5,0};
 assert(minimum==min_expected[type]&&zeros==zeros_expected[type]);
 if(type==1){
  const int m[5]={28217,28280,29387,39919,59749};
  const array<int,4> P[5]={{0,1,0,0},{1,0,0,0},{1,1,0,1},{1,1,1,1},{1,1,1,0}};
  for(int k=0;k<5;k++){assert(zero_masks[k]==m[k]);assert(singular(type,m[k],P[k]));}
 }
 cout << (type==0?"split":type==1?"nonsplit":"cone") << " cubic_classes=65535 minimum_B6="
      << minimum << " zero_B6=" << zeros << " all_smooth_sections_have_B6_positive=yes\n";
}
int main(){test_type(0);test_type(1);test_type(2);cout<<"QUADRIC_VERIFY_OK\n";}
