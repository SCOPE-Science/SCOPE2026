// Direct full-state exhaustive check for majority on untwisted and twisted cyclic ladders.
// Build: g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
#include <cstdint>
#include <iostream>
#include <stdexcept>
using namespace std;
static uint64_t lucas(int n){uint64_t a=2,b=1;for(int i=0;i<n;i++){auto c=a+b;a=b;b=c;}return a;}
static int eps(int n){const int e[6]={2,1,-1,-2,-1,1};return e[n%6];}
static int delta(int n){const int d[3]={2,-1,-1};return d[n%3];}
static uint64_t fixed_formula(int n,int twist){return lucas(n)+eps(n)+2*(twist==0);}
static uint64_t allflip_formula(int n,int twist){return lucas(n)+(twist?-delta(n):delta(n))+2*(n%2==0);}
static uint64_t twice_formula(int n,int twist){
 if((n+twist)%2==0){uint64_t a=fixed_formula(n,twist);return a*a;}
 return fixed_formula(2*n,0);
}
static uint32_t evolve(uint32_t x,int n,int twist){
 uint32_t y=0;
 for(int i=0;i<n;i++)for(int layer=0;layer<2;layer++){
  int lo=(i+n-1)%n,hi=(i+1)%n;
  int leftlayer=layer^((i==0)?twist:0);
  int rightlayer=layer^((i==n-1)?twist:0);
  int a=(x>>(lo+n*leftlayer))&1;
  int b=(x>>(hi+n*rightlayer))&1;
  int c=(x>>(i+n*(1-layer)))&1;
  if(a+b+c>=2)y|=uint32_t(1)<<(i+n*layer);
 }
 return y;
}
int main(){
 for(int n=3;n<=12;n++)for(int twist=0;twist<=1;twist++){
  uint64_t f=0,p=0,a=0;
  uint32_t count=uint32_t(1)<<(2*n),all=count-1;
  for(uint32_t x=0;x<count;x++){
   uint32_t y=evolve(x,n,twist);
   f+=(x==y);
   p+=(evolve(y,n,twist)==x);
   a+=(y==(x^all));
  }
  if(f!=fixed_formula(n,twist)||p!=twice_formula(n,twist)||a!=allflip_formula(n,twist)){
   cerr<<"FAIL n="<<n<<" twist="<<twist<<" counts="<<f<<","<<p<<","<<a<<"\n";return 1;
  }
  cout<<"n="<<n<<" twist="<<twist<<" fixed="<<f<<" fixed_two="<<p<<" fullflip="<<a<<" cycles_two="<<(p-f)/2<<" checked_states="<<count<<" OK\n";
 }
 cout<<"PASS direct exhaustive all 20 instances\n";
}
