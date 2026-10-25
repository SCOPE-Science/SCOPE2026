// Independent root-based enumeration for the Hermitian quartic over F_{729}.
// For lines y=m*x+b, count the roots of x^4-m^3*x^3-m*x=b^3+b.
// This implementation does not use point-pair secants or curve-point line enumeration.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
constexpr int q=729, q2=q*q, plane=q2+q+1;
using shortfield=uint16_t;
shortfield plus_[q*q], prod[q*q], inv_[q], neg_[q], cub[q], fourth[q], tr[q];
array<int,6> digits(int a){array<int,6>d;for(int i=0;i<6;i++){d[i]=a%3;a/=3;}return d;}
int encode(array<int,6> d){int a=0,m=1;for(int i=0;i<6;i++){a+=d[i]*m;m*=3;}return a;}
int add_slow(int a,int b){auto u=digits(a),v=digits(b);for(int i=0;i<6;i++)u[i]=(u[i]+v[i])%3;return encode(u);}
int shift_t(int a){auto u=digits(a);array<int,6>v={u[5],(u[0]+2*u[5])%3,u[1],u[2],u[3],u[4]};return encode(v);}
int mul_slow(int a,int b){auto v=digits(b);int ans=0,cur=a;for(int i=0;i<6;i++){if(v[i]>=1)ans=add_slow(ans,cur);if(v[i]==2)ans=add_slow(ans,cur);cur=shift_t(cur);}return ans;}
inline int ad(int a,int b){return plus_[a*q+b];}
inline int mul(int a,int b){return prod[a*q+b];}
inline int minus_(int a){return neg_[a];}
int fieldpow(int a,int n){int r=1;while(n){if(n&1)r=mul(r,a);a=mul(a,a);n>>=1;}return r;}
void init(){
 for(int i=0;i<q;i++)for(int j=0;j<q;j++){plus_[i*q+j]=add_slow(i,j);prod[i*q+j]=mul_slow(i,j);}
 for(int a=0;a<q;a++){
  auto d=digits(a);for(auto&x:d)x=(3-x)%3;
  neg_[a]=encode(d);
  if(a)inv_[a]=fieldpow(a,q-2);
  cub[a]=fieldpow(a,3);
  fourth[a]=fieldpow(a,4);
  tr[a]=ad(cub[a],a);
 }
 for(int a=1;a<q;a++)assert(mul(a,inv_[a])==1);
}
inline void markline(vector<uint16_t>&N,int A,int B,int C){
 // On affine z=1, A*x+B*y+C=0.
 if(B){for(int x=0;x<q;x++){
  int y=mul(minus_(ad(mul(A,x),C)),inv_[B]);N[x*q+y]++;
 }
 N[q2+mul(minus_(A),inv_[B])]++;
 }else if(A){int x=mul(minus_(C),inv_[A]);for(int y=0;y<q;y++)N[x*q+y]++;N[plane-1]++;}
 else {for(int y=0;y<q;y++)N[q2+y]++;N[plane-1]++;}
}
int main(){
 init();
 vector<uint16_t>N(plane,0);
 map<int,int> linehist;
 int n4=0;
 // First 729^2 lines, all affine nonvertical y=m*x+b.
 for(int m=0;m<q;m++){
  int m3=cub[m];
  uint16_t roots[q]={};
  for(int x=0;x<q;x++){
   int rhs=ad(ad(fourth[x],minus_(mul(m3,cub[x]))),minus_(mul(m,x)));
   roots[rhs]++;
  }
  for(int b=0;b<q;b++){
   int k=roots[tr[b]];
   assert(k==0||k==1||k==2||k==4);
   linehist[k]++;
   if(k==4){n4++;markline(N,minus_(m),1,minus_(b));}
  }
 }
 // The 729 verticals x=a have one point at infinity and 0 or 3 affine points.
 for(int x=0;x<q;x++){
  int n=1;
  for(int y=0;y<q;y++)if(tr[y]==fourth[x])n++;
  assert(n==1||n==4);
  linehist[n]++;
  if(n==4){n4++;markline(N,1,0,minus_(x));}
 }
 // line at infinity meets curve only at (0:1:0).
 linehist[1]++;
 map<int,int> ext,curve;
 int cpoints=0;
 for(int x=0;x<q;x++)for(int y=0;y<q;y++){
  if(tr[y]==fourth[x]){cpoints++;curve[N[x*q+y]]++;}
  else ext[N[x*q+y]]++;
 }
 for(int y=0;y<q;y++)ext[N[q2+y]]++;
 curve[N[plane-1]]++;cpoints++;
 assert(cpoints==892 && n4==39879);
 assert(linehist[0]==158760 && linehist[1]==175420 && linehist[2]==158112 && linehist[4]==39879);
 assert(ext[25]==1512 && ext[222]==63 && ext.count(0)==0);
 assert(curve[175]==864 && curve[297]==28);
 printf("LINE_CLASS_COUNTS");for(auto [k,v]:linehist)printf(" %d:%d",k,v);puts("");
 printf("EXTERIOR_SPECTRUM");for(auto [k,v]:ext)printf(" %d:%d",k,v);puts("");
 printf("CURVE_SPECTRUM");for(auto [k,v]:curve)printf(" %d:%d",k,v);puts("");
 puts("DIRECT_VERIFY_OK");
}
