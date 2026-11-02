// Standalone independent full-matrix census for indexed cyclic binary words.
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
using namespace std;
static uint64_t choose(int n,int k){
  if(k<0||k>n)return 0;
  if(k>n-k)k=n-k;
  uint64_t r=1;
  for(int i=1;i<=k;i++)r=r*(n-i+1)/i;
  return r;
}
static uint64_t max_formula(int n){
 if(n<=5)return uint64_t(n);
 int k=n/4;
 switch(n%4){
 case 0:return choose(2*k,k)*choose(2*k,k);
 case 1:return (4*k+1)*choose(2*k-1,k-1)*choose(2*k,k-1)/k;
 case 2:return (4*k+2)*choose(2*k,k)*choose(2*k,k)/(k+1);
 default:return (4*k+3)*choose(2*k,k)*choose(2*k+1,k)/(k+1);
 }
}
static set<array<int,4>> predicted_matrices(int n){
 set<array<int,4>> s;
 auto add=[&](int z,int t){ s.insert({z-t,t,t,n-z-t}); };
 if(n==1){add(0,0);add(1,0);return s;}
 if(n<=5){
  for(int z=1;z<n;z++)add(z,1);
  if(n==5){add(2,2);add(3,2);}
  return s;
 }
 int k=n/4;
 switch(n%4){
 case 0:add(2*k,k);break;
 case 1:for(int z:{2*k,2*k+1})for(int t:{k,k+1})add(z,t);break;
 case 2:add(2*k+1,k+1);break;
 default:add(2*k+1,k+1);add(2*k+2,k+1);break;
 }
 return s;
}
int main(){
 for(int n=1;n<=20;n++){
  map<array<int,4>,uint32_t> fibers;
  uint32_t limit=uint32_t(1)<<n;
  for(uint32_t word=0;word<limit;word++){
   array<int,4> f={0,0,0,0};
   for(int i=0;i<n;i++){
    int a=(word>>i)&1;
    int b=(word>>((i+1)%n))&1;
    f[2*a+b]++;
   }
   fibers[f]++;
  }
  uint32_t m=0;
  for(auto const& p:fibers)if(p.second>m)m=p.second;
  set<array<int,4>> winners;
  for(auto const& p:fibers)if(p.second==m)winners.insert(p.first);
  if(m!=max_formula(n)||winners!=predicted_matrices(n)){
   cerr<<"MISMATCH at n="<<n<<" max="<<m<<"\n";
   return 1;
  }
 }
 cout<<"CROSSCHECK_OK\n";
}
