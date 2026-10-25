#include <array>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;
struct Field {
 int r,q; vector<int> c; vector<vector<int>> add,sub,mul; vector<int> inv;
 Field(int r_,vector<int> c_):r(r_),q(1),c(c_){
  for(int i=0;i<r;i++) q*=3;
  add.assign(q, vector<int>(q)); sub=add;mul=add;inv.assign(q,0);
  vector<vector<int>> d(q,vector<int>(r));
  for(int a=0;a<q;a++){int t=a;for(int i=0;i<r;i++){d[a][i]=t%3;t/=3;}}
  auto encode=[&](const vector<int>& v){int t=0,m=1;for(int i=0;i<r;i++){int z=((v[i]%3)+3)%3;t+=z*m;m*=3;}return t;};
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   vector<int> u(r),v(2*r-1);
   for(int i=0;i<r;i++){u[i]=d[a][i]+d[b][i];}
   add[a][b]=encode(u);
   for(int i=0;i<r;i++){u[i]=d[a][i]-d[b][i];}
   sub[a][b]=encode(u);
   for(int i=0;i<r;i++)for(int j=0;j<r;j++)v[i+j]+=d[a][i]*d[b][j];
   for(int k=2*r-2;k>=r;k--){int z=((v[k]%3)+3)%3;for(int i=0;i<r;i++)v[k-r+i]-=z*c[i];}
   mul[a][b]=encode(v);
  }
  for(int a=1;a<q;a++)for(int b=1;b<q;b++)if(mul[a][b]==1){inv[a]=b;break;}
  for(int a=1;a<q;a++)assert(inv[a]!=0);
 }
 int A(int a,int b)const{return add[a][b];} int S(int a,int b)const{return sub[a][b];} int M(int a,int b)const{return mul[a][b];}
 int P(int a,int e)const{int v=1;for(;e;e>>=1,a=M(a,a))if(e&1)v=M(v,a);return v;}
 int E(int x,int y)const { // Homogenization of Y^4-(X^3+X)+(Y^2-2X)^2 on z=1.
  int k=S(M(y,y),M(2,x));return A(S(S(P(y,4),P(x,3)),x),M(k,k));
 }
};
struct Point{int x,y,z;};
int main(){
 for(auto [r,poly]:vector<pair<int,vector<int>>>{{3,{1,0,2}},{4,{1,0,1,1}}}){
  Field f(r,poly); int q=f.q;
  vector<Point> points; 
  for(int x=0;x<q;x++) for(int y=0;y<q;y++) if(f.E(x,y)==0)points.push_back({x,y,1});
  points.push_back({1,0,0});
  int K=points.size(), freq[5]={};
  vector<Point> lines;vector<int> hits;
  for(int a=0;a<q;a++)for(int b=0;b<q;b++)lines.push_back({a,b,1});
  for(int b=0;b<q;b++)lines.push_back({1,b,0});
  lines.push_back({0,1,0});
  auto on=[&](const Point &l, const Point &p){return f.A(f.A(f.M(l.x,p.x),f.M(l.y,p.y)),f.M(l.z,p.z))==0;};
  vector<Point> maxlines;
  for(auto &l:lines){int hit=0;for(auto &p:points)if(on(l,p))hit++;
   if(hit>4){cerr<<"Line exceeds degree 4\n";return 1;}
   freq[hit]++;
   if(hit==4)maxlines.push_back(l);
  }
  assert((int)lines.size()==q*q+q+1);
  vector<Point> ambient=lines;
  int oncurveuncovered=0,offuncovered=0;
  map<int,int> distOn;
  map<int,int> dist,distOff;
  for(auto &p:ambient){
   int nc=0;for(auto &l:maxlines)if(on(l,p))nc++;
   dist[nc]++;
   bool oncurve=false;for(auto &x:points)if(x.x==p.x&&x.y==p.y&&x.z==p.z)oncurve=true;
   if(!oncurve)distOff[nc]++;else distOn[nc]++;
   if(nc==0){if(oncurve)oncurveuncovered++;else offuncovered++;}
  }
  cout<<"r="<<r<<" q="<<q<<" K="<<K<<" line-character:";
  for(int i=0;i<5;i++)cout<<" "<<i<<":"<<freq[i];
  cout<<" four_secants="<<maxlines.size()<<" uncovered_on="<<oncurveuncovered<<" uncovered_off="<<offuncovered<<"\n";
  cout<<"coverage_distribution:";for(auto [x,n]:dist)cout<<" "<<x<<":"<<n;cout<<"\n";
  cout<<"on_curve_distribution:";for(auto [x,n]:distOn)cout<<" "<<x<<":"<<n;cout<<"\n";
  cout<<"off_curve_distribution:";for(auto [x,n]:distOff)cout<<" "<<x<<":"<<n;cout<<"\n";
  assert(r!=3||(K==31&&(int)maxlines.size()==24&&offuncovered==282));
  assert(r!=4||(K==79&&(int)maxlines.size()==204&&offuncovered==108));
 }
 cout<<"VERIFY_OK\n";
}
