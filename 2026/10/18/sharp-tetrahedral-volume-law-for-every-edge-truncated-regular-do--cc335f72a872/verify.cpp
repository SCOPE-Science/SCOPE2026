// Exact finite certificate for the maximal contained tetrahedron in uniformly truncated dodecahedra.
// Arithmetic is in Z[phi], where phi^2=phi+1; no floating point is used.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct A { long long a,b; };
A operator+(A x,A y){return {x.a+y.a,x.b+y.b};}
A operator-(A x,A y){return {x.a-y.a,x.b-y.b};}
A operator-(A x){return {-x.a,-x.b};}
A operator*(A x,A y){return {x.a*y.a+x.b*y.b,x.a*y.b+x.b*y.a+x.b*y.b};}
A operator*(long long k,A x){return {k*x.a,k*x.b};}
A divi(A x,long long k){assert(x.a%k==0 && x.b%k==0);return {x.a/k,x.b/k};}
bool operator==(A x,A y){return x.a==y.a && x.b==y.b;}
// Exact sign of a+b*phi; phi=(1+sqrt(5))/2.
int cmp0(A x){
 long long X=2*x.a+x.b, Y=x.b;
 if(Y==0)return (X>0)-(X<0);
 if(X==0)return (Y>0)-(Y<0);
 if(X>0 && Y>0)return 1;
 if(X<0 && Y<0)return -1;
 __int128 q=(__int128)X*X-5*(__int128)Y*Y;
 if(X>0)return (q>0)?1:-1;
 return (q<0)?1:-1;
}
using Vec=array<A,3>;
Vec operator+(Vec x,Vec y){Vec z;for(int i=0;i<3;i++)z[i]=x[i]+y[i];return z;}
Vec operator-(Vec x,Vec y){Vec z;for(int i=0;i<3;i++)z[i]=x[i]-y[i];return z;}
Vec operator*(long long k,Vec x){Vec z;for(int i=0;i<3;i++)z[i]=k*x[i];return z;}
A dot(Vec x,Vec y){return x[0]*y[0]+x[1]*y[1]+x[2]*y[2];}
A det(Vec x,Vec y,Vec z){return dot(x,Vec{y[1]*z[2]-y[2]*z[1],y[2]*z[0]-y[0]*z[2],y[0]*z[1]-y[1]*z[0]});}
A sqdist(Vec x,Vec y){Vec z=x-y;return dot(z,z);}
struct Aff {Vec u,v;};
Vec at(Aff x,int t){return (1-t)*x.u+t*x.v;}
A det4(const array<Aff,4>& q,int t){auto a=at(q[0],t), b=at(q[1],t), c=at(q[2],t), d=at(q[3],t);return det(a-d,b-d,c-d);}
using Poly=array<A,4>;
Poly polynomial(const array<Aff,4>& q){
 A v0=det4(q,0),v1=det4(q,1),vneg=det4(q,-1),v2=det4(q,2);
 A c2=divi(v1+vneg-2*v0,2);
 A c3=divi(v2-v0-4*c2-v1+vneg,6);
 A c1=divi(v1-vneg,2)-c3;
 return Poly{v0,c1,c2,c3};
}
bool eq(Poly x,Poly y){for(int i=0;i<4;i++)if(!(x[i]==y[i]))return false;return true;}
Poly scale(int sign,Poly x){for(auto &a:x)a=sign*a;return x;}
// Sign of four scaled Bernstein coefficients for t in [0,1/2].
bool bernstein_nonnegative(Poly F,Poly P,int sign){
 A c[4];for(int i=0;i<4;i++)c[i]=F[i]-sign*P[i];
 A b[4]={24*c[0],24*c[0]+4*c[1],24*c[0]+8*c[1]+2*c[2],24*c[0]+12*c[1]+6*c[2]+3*c[3]};
 for(auto &x:b)if(cmp0(x)<0)return false;
 return true;
}
int main(){
 const A one{1,0},zero{0,0},phi{0,1},invphi{-1,1};
 vector<Vec> V;
 for(int sx:{-1,1})for(int sy:{-1,1})for(int sz:{-1,1})V.push_back({sx*one,sy*one,sz*one});
 for(int i=0;i<3;i++)for(int s:{-1,1})for(int t:{-1,1}){
  Vec u{zero,zero,zero};u[(i+1)%3]=s*invphi;u[(i+2)%3]=t*phi;V.push_back(u);
 }
 assert(V.size()==20);
 vector<pair<int,int>> edges;
 const A edge2{8,-4};
 for(int i=0;i<20;i++)for(int j=i+1;j<20;j++)if(sqdist(V[i],V[j])==edge2)edges.emplace_back(i,j);
 assert(edges.size()==30);
 vector<Aff> W;
 for(auto [i,j]:edges)W.push_back({V[i],V[j]});
 for(auto [i,j]:edges)W.push_back({V[j],V[i]});
 assert(W.size()==60);
 array<Aff,4> witness{W[0],W[10],W[15],W[20]};
 Poly F=polynomial(witness);
 // Choose positive orientation at t=1/4 using the scaled exact evaluation.
 if(cmp0(64*F[0]+16*F[1]+4*F[2]+F[3])<0) F=scale(-1,F);
 long long count=0,eq_positive=0,eq_negative=0;
 long long eq_t0=0,eq_thalf=0;
 map<array<int,3>,vector<pair<int,int>>> winners_by_triple;
 for(int i=0;i<60;i++)for(int j=i+1;j<60;j++)for(int k=j+1;k<60;k++)for(int l=k+1;l<60;l++){
  Poly P=polynomial({W[i],W[j],W[k],W[l]});
  if(!bernstein_nonnegative(F,P,+1)||!bernstein_nonnegative(F,P,-1)){
    cerr<<"FAIL for indices "<<i<<" "<<j<<" "<<k<<" "<<l<<"\n";return 1;
  }
  ++count;
  int orient=0;
  if(eq(P,F)){++eq_positive;orient=1;}
  if(eq(P,scale(-1,F))){++eq_negative;orient=-1;}
  if(orient){
   int w[4]={i,j,k,l};
   for(int r=0;r<4;r++){
    array<int,3> tri{};int n=0;
    for(int q=0;q<4;q++)if(q!=r)tri[n++]=w[q];
    int oriented_sign=((3-r)%2)?-orient:orient;
    winners_by_triple[tri].push_back({w[r],oriented_sign});
   }
  }
  A s0=P[0];if(cmp0(s0)<0)s0=-s0;
  if(s0==F[0])++eq_t0;
  A s1=8*P[0]+4*P[1]+2*P[2]+P[3];if(cmp0(s1)<0)s1=-s1;
  A target=8*F[0]+4*F[1]+2*F[2]+F[3];
  if(s1==target)++eq_thalf;
 }
 assert(count==487635);
 assert(eq_positive+eq_negative==120);
 assert(eq_t0==810);
 assert(eq_thalf==960);
 int moving=0,unique=0;
 for(const auto& [tri, apexes]:winners_by_triple){
  if(apexes.size()==1){++unique;continue;}
  assert(apexes.size()==3);++moving;
  for(int k=1;k<3;k++){
   assert(apexes[k].second==apexes[0].second);
   for(int c=0;c<3;c++)assert(W[apexes[k].first].u[c]==W[apexes[0].first].u[c]);
  }
 }
 assert(moving==40 && unique==360);
 cout<<"PASS: "<<count<<" four-vertex configurations checked; 8 signed Bernstein inequalities each.\n";
 cout<<"F polynomial coefficients in Z[phi] (a,b):";
 for(auto x:F)cout<<" ("<<x.a<<","<<x.b<<")";
 cout<<"\nInterior maximizing quadruples: "<<(eq_positive+eq_negative)<<"; endpoint raw counts: "<<eq_t0<<", "<<eq_thalf<<"\n";
 cout<<"Movable-apex triangle families: "<<moving<<"; solitary triple incidences: "<<unique<<"\n";
}
