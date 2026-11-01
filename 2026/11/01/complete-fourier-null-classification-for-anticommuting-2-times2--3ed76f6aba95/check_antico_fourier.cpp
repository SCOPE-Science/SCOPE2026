// Exact character orthogonality checks for the finite-field anti-commuting locus.
// Build: c++ -O3 -std=c++17 check_antico_fourier.cpp -o check && ./check
#include <array>
#include <cassert>
#include <cstdio>
#include <cstdint>
#include <vector>
using namespace std;
using V3=array<int,3>; using M4=array<int,4>;
int md(int a,int p){a%=p;return a<0?a+p:a;}
int chi(int a,int p){a=md(a,p);if(!a)return 0;for(int z=1;z<p;z++)if(z*z%p==a)return 1;return -1;}
int qf(V3 x,int p){return (x[0]*x[0]+x[1]*x[2])%p;}
int dot(V3 x,V3 y,int p){int h=(p+1)/2;return (x[0]*y[0]+h*(x[1]*y[2]+x[2]*y[1]))%p;}
bool anticomm(M4 X,M4 Y,int p){
 auto a=[&](int i,int j){return md(X[i]*Y[j]+X[(i/2)*2+1]*Y[(j%2)+2]+Y[i]*X[j]+Y[(i/2)*2+1]*X[(j%2)+2],p);};
 // Direct entrywise formula, independent of the scalar/traceless parametrization.
 for(int i=0;i<2;i++)for(int j=0;j<2;j++){
  int s=0;for(int k=0;k<2;k++)s+=X[2*i+k]*Y[2*k+j]+Y[2*i+k]*X[2*k+j];
  if(s%p)return false;
 }return true;
}
M4 matrix(int a,V3 x,int p){return {md(a+x[0],p),x[1],x[2],md(a-x[0],p)};}
long long explicit_multiplier(int p,int a,int b,int i,int j,
 const vector<V3>&w,const vector<V3>&sphere,const vector<vector<unsigned char>>&d){
 int c=dot(w[i],w[j],p);int h1=0,h2=0,h12=0;
 for(size_t z=0;z<sphere.size();z++){
  bool f=(a+d[i][z])%p==0, g=(b+p-d[j][z])%p==0;
  h1+=f;h2+=g;h12+=(f&&g);
 }
 long long base=(i==0&&j==0?1LL*p*p*p*p*p:0)+(c==0?1LL*p*p*p:0)-p*p;
 long long axes=(i==0?1LL*p*p*p*(a==0?p-1:-1):0)+(j==0?1LL*p*p*p*(b==0?p-1:-1):0);
 return base+axes+1LL*p*p*h12-p*(h1+h2)+(int)sphere.size();
}
bool predicted_zero(int p,int a,int b,V3 P,V3 R){
 int u=qf(P,p),v=qf(R,p),c=dot(P,R,p);
 if(!c)return false;
 if(P!=V3{0,0,0} && !u && chi(v,p)==-1 && a && chi(c*c+2*c*a*b+v*a*a,p)==1)return true;
 if(R!=V3{0,0,0} && !v && chi(u,p)==-1 && b && chi(c*c+2*c*a*b+u*b*b,p)==1)return true;
 return false;
}
void run(int p){
 vector<V3>w,sphere;
 for(int x=0;x<p;x++)for(int y=0;y<p;y++)for(int z=0;z<p;z++){
  V3 v{x,y,z};w.push_back(v);if(qf(v,p)==1)sphere.push_back(v);
 }
 assert((int)sphere.size()==p*p+p);
 vector<vector<unsigned char>> d(w.size(),vector<unsigned char>(sphere.size()));
 for(size_t i=0;i<w.size();i++)for(size_t z=0;z<sphere.size();z++)d[i][z]=dot(w[i],sphere[z],p);
 vector<pair<M4,M4>> pairs;
 if(p<=5){
  vector<M4>matrices;
  for(int x=0;x<p;x++)for(int y=0;y<p;y++)for(int z=0;z<p;z++)for(int t=0;t<p;t++)matrices.push_back({x,y,z,t});
  for(const auto& X: matrices)for(const auto& Y:matrices)if(anticomm(X,Y,p))pairs.push_back({X,Y});
  assert((long long)pairs.size()==1LL*p*p*p*p*p+p*p*p-p*p+2LL*(p-1)*p*p*p+1LL*(p-1)*(p-1)*(p*p+p));
 }
 long long nzero=0,nfreq=0,ndirect=0;
 for(size_t i=0;i<w.size();i++)for(size_t j=0;j<w.size();j++)for(int a=0;a<p;a++)for(int b=0;b<p;b++){
  long long v=explicit_multiplier(p,a,b,i,j,w,sphere,d);
  bool zz=predicted_zero(p,a,b,w[i],w[j]);
  if(p>=5)assert((v==0)==zz);
  if(v==0)nzero++;nfreq++;
  // Every frequency for p=3; a reproducible stratified subset for p=5.
  if(p==3 || (p==5 && ((i*757+j*31+a*7+b*11)%1133==0 || (i==1&&j<3)))){
   M4 A=matrix(a,w[i],p), B=matrix(b,w[j],p);
   int counts[7]={};
   for(const auto& pr:pairs){const M4&X=pr.first,&Y=pr.second;
    int e=0;for(int t=0;t<4;t++){
     int it=(t%2)*2+(t/2); // transpose-position when evaluating tr(A X)
     e+=A[t]*X[it]+B[t]*Y[it];
    }
    counts[md(e,p)]++;
   }
   for(int k=2;k<p;k++)assert(counts[k]==counts[1]);
   assert(counts[0]-counts[1]==v);ndirect++;
  }
 }
 if(p>=5){long long expected=1LL*p*(p*p-1)*(p-1)*(p-1)*(p-1)*(p-1)/2;assert(nzero==expected);}
 printf("EXACT_ANTICOMMUTATOR_OK p=%d frequencies=%lld zeros=%lld direct_checked=%lld\n",p,nfreq,nzero,ndirect);
}
int main(){run(3);run(5);run(7);puts("ANTICOMMUTING_FOURIER_NULLITY_ALL_CHECKS_OK");}
