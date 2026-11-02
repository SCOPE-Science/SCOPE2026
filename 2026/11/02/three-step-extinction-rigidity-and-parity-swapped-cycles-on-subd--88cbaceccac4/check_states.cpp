#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct System {
 int n,N; vector<uint64_t> adj;
 System(int k):n(k),N(k+k*(k-1)/2),adj(N,0) {
   int e=n;
   for(int u=0;u<n;u++)for(int v=u+1;v<n;v++,e++){
     adj[e]=(1ULL<<u)|(1ULL<<v);
     adj[u] |= 1ULL<<e;
     adj[v] |= 1ULL<<e;
   }
 }
 uint64_t step(uint64_t x)const {
   uint64_t y=0;
   for(int i=0;i<N;i++)
     if(__builtin_parityll(x&adj[i]))y|=1ULL<<i;
   return y;
 }
};
int main(){
 for(int n=2;n<=6;n++){
  System g(n); assert(g.N<=21);
  uint64_t total=1ULL<<g.N;
  map<int,uint64_t> entry,period;
  for(uint64_t x=0;x<total;x++){
   uint64_t y=g.step(x),z=g.step(y),w=g.step(z);
   if(n%2==0){
     assert(w==0);
     int t=x==0?0:y==0?1:z==0?2:3;
     entry[t]++;period[1]++;
   }else{
     assert(w==y);
     int t=(z==x)?0:1; // if F^2 x = x then periodic (F^2 identity on image)
     entry[t]++;
     // eventually cycle is fixed iff F(y)=y: z=y.
     period[z==y?1:2]++;
   }
  }
  uint64_t r0=total;
  uint64_t r1=1ULL<<(g.N-2*(n-1));
  uint64_t r2=1ULL<<(g.N-(n-1));
  if(n%2==0){
    assert(entry[0]==1 && entry[1]==r1-1 && entry[2]==r2-r1 && entry[3]==r0-r2);
    assert(period[1]==total);
  }else{
    assert(entry[0]==(1ULL<<(2*(n-1))));
    assert(entry[1]==total-entry[0]);
    assert(period[1]==(1ULL<<(g.N-(n-1))));
    assert(period[2]==total-period[1]);
  }
  cout << "n="<<n<<" N="<<g.N<<" states="<<total<<" entry=";
  for(auto [i,v]:entry)cout<<i<<":"<<v<<",";
  cout<<" eventual_period=";
  for(auto [p,v]:period)cout<<p<<":"<<v<<",";
  cout<<" OK\n";
 }
 cout<<"CPLUSPLUS_VERIFICATION_OK\n";
}
