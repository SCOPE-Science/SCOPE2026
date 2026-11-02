// Independent finite-field and adjacency-pattern census using quartic characters.
// Usage: c++ -std=c++17 -O3 independent_peisert.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
struct Field {
 int p,t,n,gen;
 Field(int p_,int t_,int gen_):p(p_),t(t_),n(p*p),gen(gen_){}
 int mul(int a,int b) const {
   int u=a%p,v=a/p,w=b%p,z=b/p;
   return ((u*w+t*v*z)%p)+p*((u*z+v*w)%p);
 }
 int pow(int a,int e) const {
  int r=1; for (;e;e>>=1,a=mul(a,a)) if(e&1)r=mul(r,a);return r;
 }
 int sub(int a,int b) const {
  return (a%p-b%p+p)%p + p*((a/p-b/p+p)%p);
 }
 bool check() const {
  for(int a=0;a<n;a++) if(pow(a,n)!=a) return false; // Frobenius.
  if(pow(gen,n-1)!=1) return false;
  for(int l=2;l<=n-1;l++) if((n-1)%l==0){
   bool prime=true;for(int f=2;f*f<=l;f++)if(l%f==0)prime=false;
   if(prime && pow(gen,(n-1)/l)==1) return false;
  }
  return true;
 }
 vector<vector<uint8_t>> graph(bool peisert) const {
  vector<vector<uint8_t>> a(n,vector<uint8_t>(n));
  int i=pow(gen,(n-1)/4);
  for(int x=0;x<n;x++) for(int y=0;y<n;y++) {
   if(x==y)continue;
   int z=sub(x,y), h=pow(z,peisert?(n-1)/4:(n-1)/2);
   a[x][y]=peisert?(h==1||h==i):(h==1);
  }
  for(int x=0;x<n;x++) {
   int d=0;for(int y=0;y<n;y++) {if(a[x][y]!=a[y][x])throw runtime_error("not symmetric");d+=a[x][y];}
   if(d!=(n-1)/2)throw runtime_error("degree wrong");
  }
  return a;
 }
};
struct Census{bool ec=true; int minimum=1000000; int64_t tested=0,failures=0,atminimum=0;array<int,4>witness={-1,-1,-1,-1};int missing=-1;};
Census triples(const vector<vector<uint8_t>>& a,bool orbit,int gen,const Field& fld){
 int n=a.size();Census res;
 vector<int>bs;
 if(orbit) {int z=1;for(int j=0;j<4;j++){bs.push_back(z);z=fld.mul(z,gen);}}
 else {for(int z=1;z<n;z++)bs.push_back(z);}
 for(int b:bs)for(int c=1;c<n;c++){
  if(c==b || (!orbit && c<b))continue;
  for(int d=c+1;d<n;d++){
   if(d==b)continue;
   array<int,4> v={0,b,c,d};int cnt[16]={};
   for(int z=0;z<n;z++){
    if(z==0||z==b||z==c||z==d)continue;
    int mask=(int)a[z][0]+2*(int)a[z][b]+4*(int)a[z][c]+8*(int)a[z][d];
    ++cnt[mask];
   }
   res.tested++;int mn=cnt[0];int ix=0;
   for(int i=1;i<16;i++)if(cnt[i]<mn){mn=cnt[i];ix=i;}
   if(mn<res.minimum){res.minimum=mn;res.witness=v;res.missing=ix;res.atminimum=0;}
   if(mn==res.minimum)res.atminimum++;
   if(mn==0){res.ec=false;res.failures++;}
  }
 }
 return res;
}
Census pairs3(const vector<vector<uint8_t>>& a){
 int n=a.size();Census r;
 for(int b=1;b<n;b++)for(int c=b+1;c<n;c++){
  array<int,3>v={0,b,c};int cnt[8]={};
  for(int z=0;z<n;z++){
   if(z==0||z==b||z==c)continue;
   ++cnt[(int)a[z][0]+2*(int)a[z][b]+4*(int)a[z][c]];
  }
  int mn=*min_element(cnt,cnt+8);r.tested++;
  if(mn<r.minimum){r.minimum=mn;r.witness={0,b,c,-1};}
  if(mn==0){r.ec=false;r.failures++;}
 }
 return r;
}
int main(){
 for(auto param:vector<array<int,3>>{{11,2,13},{19,2,21}}){
  Field f(param[0],param[1],param[2]);if(!f.check())throw runtime_error("not a finite field primitive element");
  for(bool peisert:{false,true}){
   if(f.p==19&&!peisert)continue;
   auto g=f.graph(peisert);
   int q=f.n;
   int minlambda=q,maxlambda=0,minmu=q,maxmu=0;
   for(int a=0;a<q;a++)for(int b=a+1;b<q;b++){
     int cc=0;for(int z=0;z<q;z++)cc+=g[a][z]&&g[b][z];
     if(g[a][b]){minlambda=min(minlambda,cc);maxlambda=max(maxlambda,cc);}
     else{minmu=min(minmu,cc);maxmu=max(maxmu,cc);}
   }
   cout<<(peisert?"Peisert":"Paley")<<"("<<q<<") srg=("<<q<<","<<(q-1)/2<<","<<minlambda<<","<<minmu<<") ranges=("<<minlambda<<".."<<maxlambda<<","<<minmu<<".."<<maxmu<<")\n";
   if(minlambda!=(q-5)/4||maxlambda!=minlambda||minmu!=(q-1)/4||maxmu!=minmu)throw runtime_error("unexpected common-neighbor parameters");
   if(q==121){auto t3=pairs3(g);cout<<(peisert?"Peisert":"Paley")<<"("<<q<<") 3ec="<<t3.ec<<" all_0bc="<<t3.tested<<" min="<<t3.minimum<<"\n";}
   auto r=triples(g,q==361,f.gen,f);
   cout<<(peisert?"Peisert":"Paley")<<"("<<q<<") 4ec="<<r.ec<<" triples="<<r.tested<<" failing="<<r.failures<<" min="<<r.minimum<<" min_count="<<r.atminimum
       <<" witness=("<<r.witness[0]<<","<<r.witness[1]<<","<<r.witness[2]<<","<<r.witness[3]<<") pattern="<<r.missing<<"\n";
   if(q==121&&peisert&&r.ec)throw runtime_error("unexpected positive 121 Peisert");
   if(q==121&&!peisert&&!r.ec)throw runtime_error("unexpected negative 121 Paley");
   if(q==361&&peisert&&(!r.ec||r.minimum!=10||r.tested!=257044))throw runtime_error("unexpected 361 Peisert");
   if(q==121&&r.tested!=280840)throw runtime_error("unexpected 121 census count");
  }
 }
}
