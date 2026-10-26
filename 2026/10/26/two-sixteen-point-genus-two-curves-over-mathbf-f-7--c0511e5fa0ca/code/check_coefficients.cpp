// Independent exact enumeration with raw binary-sextic coefficients over F_7.
// Build: c++ -std=c++17 -O2 code/check_coefficients.cpp -o check_coefficients
#include <array>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;
using Vec=array<int,8>;
using Mat=array<int,4>;
using Poly=vector<int>;
int mod(int x){x%=7;return x<0?x+7:x;}
int inv(int x){for(int y=1;y<7;y++)if(mod(x*y)==1)return y;return -1;}
Poly tr(Poly x){while(!x.empty()&&x.back()==0)x.pop_back();return x;}
Poly rem(Poly a,Poly b){a=tr(a);b=tr(b);while(a.size()>=b.size()&&!a.empty()){
 int c=mod(a.back()*inv(b.back()));int d=(int)a.size()-(int)b.size();
 for(int j=0;j<(int)b.size();j++)a[d+j]=mod(a[d+j]-c*b[j]);a=tr(a);
 }return a;}
Poly gcd(Poly a,Poly b){a=tr(a);b=tr(b);while(!b.empty()){
 auto c=rem(a,b);a=b;b=c;
 }return a;}
int polyeval(const array<int,7>&a,int x){int v=0;for(int i=6;i>=0;i--)v=mod(v*x+a[i]);return v;}
bool sq(int x){return x==1||x==2||x==4;}
Vec values(const array<int,7>& a){Vec z;for(int x=0;x<7;x++)z[x]=polyeval(a,x);z[7]=a[6];return z;}
int main(){
 set<Vec> smooth;
 int split=0;
 array<int,7>a{};
 for(int n=0;n<823543;n++){
  int j=n;for(int i=0;i<7;i++){a[i]=j%7;j/=7;}
  Vec v=values(a);
  bool good=true;for(int x:v)good=good&&sq(x);
  if(!good)continue;split++;
  Poly der;for(int k=1;k<=6;k++)der.push_back(mod(k*a[k]));
  if(gcd(Poly(a.begin(),a.end()),der).size()==1)smooth.insert(v);
 }
 if(split!=924||smooth.size()!=588){cerr<<"Enumeration mismatch\n";return 1;}
 set<Mat> matrices;
 for(int n=0;n<2401;n++){
  int j=n;Mat m;for(int i=0;i<4;i++){m[i]=j%7;j/=7;}
  if(mod(m[0]*m[3]-m[1]*m[2])==0)continue;
  int t=-1;for(int x:m)if(x){t=x;break;}
  int ti=inv(t);for(int &x:m)x=mod(x*ti);matrices.insert(m);
 }
 if(matrices.size()!=336){cerr<<"PGL order mismatch\n";return 2;}
 set<Vec> remaining=smooth;vector<int> sizes;
 vector<array<int,7>> reps={{{1,0,0,0,0,0,1}},{{4,0,3,0,3,0,1}}};
 for(auto a:reps){
  Vec v=values(a);set<Vec> orb;
  for(Mat m:matrices){
   Vec perm;
   for(int x=0;x<8;x++){
    int xx=x<7?x:1,zz=x<7?1:0;
    int u=mod(m[0]*xx+m[1]*zz),w=mod(m[2]*xx+m[3]*zz);
    int point=w?mod(u*inv(w)):7;
    perm[x]=v[point];
   }
   for(int s:{1,2,4}){
    Vec t=perm;for(int &e:t)e=mod(s*e);orb.insert(t);
   }
  }
  for(auto o:orb)if(!smooth.count(o)){cerr<<"Unexpected orbit member\n";return 3;}
  for(auto o:orb)remaining.erase(o);
  sizes.push_back((int)orb.size());
 }
 if(!remaining.empty()||sizes[0]!=84||sizes[1]!=504){cerr<<"Orbit mismatch\n";return 4;}
 cout<<"split_polynomials=924\nsmooth_polynomials=588\nPGL2_order=336\n"
     <<"isomorphism_classes=2\norbit_sizes=84,504\n"
     <<"automorphism_orders=24,4\n";
}
