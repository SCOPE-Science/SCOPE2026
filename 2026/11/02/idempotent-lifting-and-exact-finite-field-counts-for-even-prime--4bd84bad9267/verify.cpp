// Independent direct-definition enumeration for small dihedral quandle algebras.
// Build: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
static uint64_t count_idempotents(int n,int q){
 uint64_t total=1; for(int i=0;i<n;i++)total*=q;
 vector<int> a(n,0), accum(n,0);
 uint64_t count=0;
 for(uint64_t z=0;z<total;z++){
  fill(accum.begin(),accum.end(),0);
  for(int j=0;j<n;j++)if(a[j]){
    for(int i=0;i<n;i++)if(a[i])accum[(2*j-i+n)%n]+=a[i]*a[j];
  }
  bool ok=true;for(int k=0;k<n;k++)if(accum[k]%q !=a[k]){ok=false;break;}
  if(ok)++count;
  for(int i=0;i<n;i++){if(++a[i]!=q)break;a[i]=0;}
 }
 return count;
}
int main(){
 const struct {int p,q; uint64_t expected;} checks[]={
 {3,3,28},{3,5,96},{3,7,176},{5,3,184},{5,5,626},{7,3,760}
 };
 for(auto c:checks){auto got=count_idempotents(2*c.p,c.q);cout<<"R_"<<2*c.p<<" F_"<<c.q<<" "<<got<<" expected "<<c.expected<<"\n";if(got!=c.expected)return 1;}
 cout<<"VERIFY_OK\n";
}
