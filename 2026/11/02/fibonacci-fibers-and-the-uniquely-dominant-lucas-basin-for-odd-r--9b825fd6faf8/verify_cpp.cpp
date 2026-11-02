#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static uint32_t step(uint32_t x,int n){
 uint32_t y=0;
 for(int i=0;i<n;++i){
   int a=(x>>((i+n-1)%n))&1, b=(x>>((i+1)%n))&1;
   if(!a&&!b)y|=(1u<<i);
 }
 return y;
}
static uint64_t fib(int n){uint64_t a=0,b=1;for(int i=0;i<n;++i){auto c=a+b;a=b;b=c;}return a;}
static uint64_t perrin(int n){if(n==0)return 3;if(n==1)return 0;if(n==2)return 2;uint64_t a=3,b=0,c=2;for(int j=3;j<=n;++j){auto d=a+b;a=b;b=c;c=d;}return c;}
static uint64_t fiber_formula(uint32_t y,int n){
 vector<int> v(n);int ones=0;
 for(int j=0;j<n;++j){v[j]=(y>>((2*j)%n))&1;ones+=v[j];}
 if(ones==0) return fib(n-1)+fib(n+1);
 if(ones==n)return 1;
 uint64_t ans=1;
 for(int j=0;j<n;++j){
   if(v[j]&&!v[(j+1)%n]){
      int k=(j+1)%n,len=0;
      while(!v[k]){++len;k=(k+1)%n;}
      if(len==1)return 0;
      ans*=fib(len-1);
   }
 }
 return ans;
}
int main(){
 for(int n=3;n<=21;n+=2){
   uint32_t all=(1u<<n)-1u;
   vector<uint32_t> cnt(1u<<n,0);
   for(uint32_t x=0;x<=all;++x)++cnt[step(x,n)];
   uint64_t periodic=0,fixed=0,orbits=0,maximum=0;uint32_t maxfirst=0,maxsecond=0;
   for(uint32_t y=0;y<=all;++y){
      if(cnt[y] != fiber_formula(y,n)) {cerr<<"fiber mismatch"<<n<<" "<<y<<"\n";return 1;}
      if(cnt[y]==0)continue;
      ++periodic;auto z=step(y,n);
      if(step(z,n)!=y){cerr<<"not recurrent";return 2;}
      if(z==y)++fixed;
      if(y>z)continue;
      ++orbits;
      uint64_t bas=cnt[y]+(z==y?0:cnt[z]);
      if(bas>maximum){maximum=bas;maxfirst=y;maxsecond=z;}
   }
   assert(periodic==perrin(2*n));
   assert(fixed==perrin(n));
   assert(orbits==(periodic+fixed)/2);
   assert(maximum==fib(n-1)+fib(n+1)+1);
   assert(maxfirst==0 && maxsecond==all);
   cout<<"n="<<n<<" inputs="<<(1u<<n)<<" recurrent="<<periodic<<" fixed="<<fixed<<" two_cycles="<<(periodic-fixed)/2<<" max_basin="<<maximum<<" PASS\n";
 }
}
