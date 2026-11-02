// Exhaustive exact finite-field census of a specified order-83 obstruction.
// Build: g++ -O3 -std=c++17 census.cpp -o census && ./census
#include <cassert>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
static constexpr int p=41;
struct E {
  int a,b;
  E(int x=0,int y=0):a((x%p+p)%p),b((y%p+p)%p){}
  bool operator==(E t)const {return a==t.a && b==t.b;}
  bool operator!=(E t)const {return !(*this==t);}
  E operator+(E t)const{return E(a+t.a,b+t.b);}
  E operator-(E t)const{return E(a-t.a,b-t.b);}
  E operator*(E t)const{return E(a*t.a+3*b*t.b,a*t.b+b*t.a);}
};
E fieldpow(E a,int n){E s(1);for(;n;n>>=1,a=a*a)if(n&1)s=s*a;return s;}
using Poly=std::vector<E>;
Poly polymul(const Poly &a,const Poly &b,E lambda){
  Poly c(2*p-1);
  for(int i=0;i<p;i++)if(a[i]!=E())
    for(int j=0;j<p;j++)if(b[j]!=E()) c[i+j]=c[i+j]+a[i]*b[j];
  for(int k=2*p-2;k>=p;k--)if(c[k]!=E()){
    E v=c[k];c[k-p+1]=c[k-p+1]-v;c[k-p]=c[k-p]-v*lambda;
  }
  c.resize(p);return c;
}
Poly polypow(Poly a,cpp_int n,E lambda){
  Poly s(p);s[0]=E(1);
  for(;n>0;n>>=1){if((n&1)!=0)s=polymul(s,a,lambda);if(n>1)a=polymul(a,a,lambda);}
  return s;
}
int main(){
  assert(fieldpow(E(3),20)==E(40)); // 3 is nonsquare modulo 41
  cpp_int q=1681,n=1;
  for(int j=0;j<41;j++)n*=q;
  n-=1;assert(n%83==0);
  const cpp_int e=n/83;
  Poly x(p);x[1]=E(1);
  int primitive_count=0, obstruction_count=0;
  for(int a=0;a<p;a++)for(int b=0;b<p;b++){
    E lambda(a,b);
    if(lambda==E())continue;
    bool prim=true;
    for(int ell:{2,3,5,7})if(fieldpow(lambda,1680/ell)==E(1))prim=false;
    if(!prim)continue;
    ++primitive_count;
    Poly y=polypow(x,e,lambda);
    bool is_one=(y[0]==E(1));
    for(int k=1;k<p;k++)if(y[k]!=E())is_one=false;
    if(is_one)++obstruction_count;
  }
  assert(primitive_count==384 && obstruction_count==64);
  std::cout<<"CENSUS_OK primitive_constants="<<primitive_count
           <<" order_83_obstructions="<<obstruction_count<<"\n";
}
