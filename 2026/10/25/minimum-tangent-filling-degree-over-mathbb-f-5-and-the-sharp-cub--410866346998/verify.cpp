// Exact finite-field incidence verifier for plane forms of degrees 1,2,3 over F_5.
// Build: g++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int q=5;
struct Triple { int a,b,c; };
int power(int a,int b){int out=1;for(int i=0;i<b;++i)out=out*a%q;return out;}
int val(Triple t,int x,int y,int z){return power(x,t.a)*power(y,t.b)%q*power(z,t.c)%q;}
int dot(Triple u,Triple v){return (u.a*v.a+u.b*v.b+u.c*v.c)%q;}
int inv(int a){for(int b=1;b<q;b++)if(a*b%q==1)return b;assert(false);return 0;}
Triple canonical(Triple g){int f=g.a?g.a:(g.b?g.b:g.c);assert(f!=0);int r=inv(f);return {g.a*r%q,g.b*r%q,g.c*r%q};}
int main(){
 vector<Triple> pts;
 for(int y=0;y<q;y++)for(int z=0;z<q;z++)pts.push_back({1,y,z});
 for(int z=0;z<q;z++)pts.push_back({0,1,z});pts.push_back({0,0,1});
 assert(pts.size()==31);
 uint64_t lines[125]={};
 for(int k=0;k<31;k++){
  auto l=pts[k];auto c=canonical(l);
  auto code=(c.a*q+c.b)*q+c.c;
  assert(lines[code]==0);
  for(int i=0;i<31;i++)if(dot(l,pts[i])==0) lines[code] |= (uint64_t(1)<<i);
  assert(__builtin_popcountll(lines[code])==6);
 }
 const uint64_t full=(uint64_t(1)<<31)-1;
 for(int degree=1;degree<=3;degree++){
  vector<Triple> mon;
  for(int a=degree;a>=0;a--)for(int b=degree-a;b>=0;b--)mon.push_back({a,b,degree-a-b});
  const int m=mon.size();
  int E[31][10]={},Dx[31][10]={},Dy[31][10]={},Dz[31][10]={};
  for(int i=0;i<31;i++) for(int j=0;j<m;j++){
   Triple e=mon[j],p=pts[i];E[i][j]=val(e,p.a,p.b,p.c);
   Dx[i][j]=e.a?e.a*val({e.a-1,e.b,e.c},p.a,p.b,p.c)%q:0;
   Dy[i][j]=e.b?e.b*val({e.a,e.b-1,e.c},p.a,p.b,p.c)%q:0;
   Dz[i][j]=e.c?e.c*val({e.a,e.b,e.c-1},p.a,p.b,p.c)%q:0;
  }
  uint64_t examined=0,accepted=0;
  int maximum_covered=0;
  for(int first=0;first<m;first++){
   uint64_t n=1;for(int j=first+1;j<m;j++)n*=q;
   for(uint64_t code=0;code<n;code++){
    int c[10]={};c[first]=1;uint64_t v=code;
    for(int j=first+1;j<m;j++){c[j]=v%q;v/=q;}
    uint64_t cover=0;
    for(int i=0;i<31;i++){
     int f=0,gx=0,gy=0,gz=0;
     for(int j=first;j<m;j++) f+=c[j]*E[i][j];
     if(f%q!=0)continue;
     for(int j=first;j<m;j++){
      gx+=c[j]*Dx[i][j];gy+=c[j]*Dy[i][j];gz+=c[j]*Dz[i][j];
     }
     Triple g={gx%q,gy%q,gz%q};
     if(g.a==0&&g.b==0&&g.c==0)continue;
     auto l=canonical(g);cover|=lines[(l.a*q+l.b)*q+l.c];
    }
    maximum_covered=max(maximum_covered,__builtin_popcountll(cover));
    ++examined;if(cover==full)++accepted;
   }
  }
  uint64_t check=0,term=1;for(int i=0;i<m;i++){check+=term;term*=q;}
  assert(examined==check);
  assert(accepted==0);
  cout<<"DEGREE="<<degree<<" SCALAR_CLASSES="<<examined
      <<" FILLING="<<accepted<<" MAX_COVERAGE="<<maximum_covered<<"/31\n";
 }
 // Explicit quartic with six tangent lines forming the complete pencil through (1:1:0).
 auto F=[](Triple p){int x=p.a,y=p.b,z=p.c;return (power(x,4)+power(x,3)*y+power(y,3)*z-power(z,4)+q)%q;};
 auto grad=[](Triple p){int x=p.a,y=p.b,z=p.c;
  return Triple{(4*power(x,3)+3*power(x,2)*y)%q,(power(x,3)+3*power(y,2)*z)%q,(power(y,3)-4*power(z,3)+4*q)%q};};
 vector<Triple> witnesses;
 for(int z=1;z<=4;z++)witnesses.push_back({1,0,z});
 witnesses.push_back({1,1,4}); witnesses.push_back({0,1,0});
 uint64_t cover=0,all=0;
 for(auto p:witnesses){
  assert(F(p)==0);auto g=canonical(grad(p));
  assert(dot(g,{1,1,0})==0);
  cover|=lines[(g.a*q+g.b)*q+g.c];
 }
 assert(cover==full);
 int count_on_curve=0;
 for(auto p:pts)if(F(p)==0){count_on_curve++;auto g=grad(p);assert(g.a||g.b||g.c);}
 assert(count_on_curve==11);
 cout<<"QUARTIC_POINTS="<<count_on_curve<<" SIX_TANGENTS_PENCIL=YES COVERED=31/31\n";
 cout<<"VERIFY_OK\n";
}
