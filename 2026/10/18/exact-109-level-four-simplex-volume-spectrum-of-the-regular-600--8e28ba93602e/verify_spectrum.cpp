// Exact 4-simplex determinant spectrum for the circumradius-one regular 600-cell.
// Usage: c++ -std=c++17 -O2 verify_spectrum.cpp -o verify_spectrum
//        ./verify_spectrum --emit spectrum.csv
//        ./verify_spectrum --check spectrum.csv
// The arithmetic ring is Z[phi], phi^2=phi+1, phi=(1+sqrt(5))/2.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using ll = long long;
struct Z { ll a,b; Z(ll x=0,ll y=0):a(x),b(y){} };
Z operator+(Z x,Z y){return {x.a+y.a,x.b+y.b};}
Z operator-(Z x,Z y){return {x.a-y.a,x.b-y.b};}
Z operator-(Z x){return {-x.a,-x.b};}
Z operator*(Z x,Z y){return {x.a*y.a+x.b*y.b, x.a*y.b+x.b*y.a+x.b*y.b};}
bool operator==(Z x,Z y){return x.a==y.a && x.b==y.b;}
// Exact sign: for r>0, r>phi iff r^2-r-1>0.
int sign(Z x) {
 ll a=x.a,b=x.b;
 if(a==0)return (b>0)-(b<0);
 if(b==0)return (a>0)-(a<0);
 if(a>0&&b>0)return 1;
 if(a<0&&b<0)return -1;
 __int128 A=llabs(a),B=llabs(b),poly=A*A-A*B-B*B;
 return (a>0) ? ((poly>0)?1:-1) : ((poly<0)?1:-1);
}
Z absolute(Z x){return sign(x)<0?-x:x;}
bool lessz(Z x,Z y){return sign(x-y)<0;}
using Point=array<Z,4>;
using Biv=array<Z,6>;
Point sub(Point x,Point y){Point z;for(int i=0;i<4;i++)z[i]=x[i]-y[i];return z;}
Biv wedge(Point a,Point b){Biv c;int k=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)c[k++]=a[i]*b[j]-a[j]*b[i];return c;}
Z wedge4(const Biv &a,const Biv &b) {
 return a[0]*b[5]-a[1]*b[4]+a[2]*b[3]+a[3]*b[2]-a[4]*b[1]+a[5]*b[0];
}
vector<Point> vertices(){
 vector<Point> v;
 for(int j=0;j<4;j++)for(int s:{-1,1}){Point p{};p[j]={2*s,0};v.push_back(p);}
 for(int mask=0;mask<16;mask++){Point p;for(int j=0;j<4;j++)p[j]={(mask&(1<<j))?-1:1,0};v.push_back(p);}
 Point base{Z(0),Z(1),Z(0,1),Z(-1,1)};
 array<int,4> perm{0,1,2,3};
 do{
  int inversions=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(perm[i]>perm[j])inversions++;
  if(inversions%2)continue;
  for(int mask=0;mask<8;mask++){
   Point p{};int k=0;
   for(int j=0;j<4;j++)if(perm[j]!=0){Z z=base[perm[j]];if(mask&(1<<k))z=-z;p[j]=z;k++;}
   v.push_back(p);
  }
 }while(next_permutation(perm.begin(),perm.end()));
 return v;
}
struct Result{
 map<pair<ll,ll>,unsigned long long> counts;
 Z maximum,second;
 unsigned long long winning=0,second_winning=0,total=0;
 vector<array<int,4>> maximizing_fourtuples;
};
Result enumerate(const vector<Point>&v,int anchor){
 const int N=119;
 vector<Point>d;for(int i=0;i<120;i++)if(i!=anchor)d.push_back(sub(v[i],v[anchor]));
 vector<Biv>w(N*N);
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)w[i*N+j]=wedge(d[i],d[j]);
 Result r;
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  const Biv &p=w[i*N+j];
  for(int k=j+1;k<N;k++)for(int l=k+1;l<N;l++){
   Z z=absolute(wedge4(p,w[k*N+l]));
   ++r.counts[{z.a,z.b}];++r.total;
   if(lessz(r.maximum,z)){
    r.second=r.maximum;r.second_winning=r.winning;
    r.maximum=z;r.winning=1;r.maximizing_fourtuples.clear();r.maximizing_fourtuples.push_back({i,j,k,l});
   }else if(r.maximum==z){++r.winning;r.maximizing_fourtuples.push_back({i,j,k,l});}
   else if(lessz(r.second,z)){r.second=z;r.second_winning=1;}
   else if(r.second==z){++r.second_winning;}
  }
 }
 return r;
}
string csv(const Result&r){
 vector<pair<Z,unsigned long long>> levels;
 for(auto &q:r.counts)levels.push_back({{q.first.first,q.first.second},q.second});
 sort(levels.begin(),levels.end(),[](auto x,auto y){return lessz(x.first,y.first);});
 ostringstream s;s<<"det_a,det_b,count_through_vertex,total_count\n";
 for(auto &q:levels)s<<q.first.a<<','<<q.first.b<<','<<q.second<<','<<24*q.second<<'\n';
 return s.str();
}
int main(int argc,char **argv){
 if(argc!=3||(string(argv[1])!="--emit"&&string(argv[1])!="--check")){cerr<<"Usage: --emit/--check spectrum.csv\n";return 2;}
 auto v=vertices();
 if(v.size()!=120){cerr<<"point count\n";return 3;}
 set<array<ll,8>> distinct;
 for(auto x:v){array<ll,8>key;Z len;for(int j=0;j<4;j++){
   key[2*j]=x[j].a;key[2*j+1]=x[j].b;len=len+x[j]*x[j];
  }distinct.insert(key);
  if(!(len==Z(4))){cerr<<"coordinate norm\n";return 3;}
 }
 if(distinct.size()!=120){cerr<<"duplicate\n";return 3;}
 auto r=enumerate(v,0);
 if(r.total!=7940751 || r.counts.size()!=109 || r.counts.at({0,0})!=687241 ||
   !(r.maximum==Z(12,24)) || r.winning!=100 ||
   !(r.second==Z(16,20)) || r.second_winning!=450){cerr<<"spectrum invariant mismatch\n";return 4;}

 if(r.maximizing_fourtuples.size()!=100){cerr<<"maximizer storage mismatch\n";return 4;}
 for(auto ids:r.maximizing_fourtuples){
  vector<Point> five={v[0],v[ids[0]+1],v[ids[1]+1],v[ids[2]+1],v[ids[3]+1]};
  map<pair<ll,ll>,int> edges;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){
   Point d=sub(five[i],five[j]);Z l;
   for(int k=0;k<4;k++)l=l+d[k]*d[k];
   ++edges[{l.a,l.b}];
  }
  if(edges.size()!=3 || edges[{4,4}]!=6 || edges[{8,0}]!=3 || edges[{12,0}]!=1){
    cerr<<"maximal simplex edge signature mismatch\n";return 4;
  }
 }

 auto body=csv(r);
 if(string(argv[1])=="--emit"){
  ofstream f(argv[2],ios::binary);f<<body;
  if(!f){cerr<<"file output failure\n";return 5;}
 }else{
  ifstream f(argv[2],ios::binary);string text((istreambuf_iterator<char>(f)),istreambuf_iterator<char>());
  if(text!=body){cerr<<"table mismatch\n";return 6;}
 }
 // The three icosian coordinate classes give an additional independent symmetry check.
 for(int anchor: {8,24}){
  auto s=enumerate(v,anchor);
  if(s.counts!=r.counts || !(s.maximum==r.maximum) || s.winning!=r.winning){cerr<<"anchor mismatch "<<anchor<<"\n";return 7;}
 }
 cout<<"VERIFY_OK vertices=120 fixed_quintuples="<<r.total
     <<" total_quintuples="<<(24*r.total)<<" levels="<<r.counts.size()
     <<" zero_quintuples="<<(24*r.counts.at({0,0}))
     <<" max_det_scaled=12+24phi max_count="<<(24*r.winning)
     <<" next_det_scaled=16+20phi next_count="<<(24*r.second_winning)<<"\n";
}
