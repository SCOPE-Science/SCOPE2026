#include <iostream>
#include <cstdint>
#include <vector>
#include <map>
#include <stdexcept>
using namespace std;
// Exact exhaustive cubic root and maximizing-coefficient check modulo 3^4.
static int roots(int p,int a,int b,int c){
  int mod=p*p*p*p,ans=0;
  for(int x=0;x<mod;++x){
    if((((((int64_t)x+a)*x+b)*x+c)%mod)==0)++ans;
  }
  return ans;
}
static bool predicted(int p,int a,int b,int c){
  int mod=p*p*p*p;
  for(int z=0;z<p;++z){
    int A=(a+3*z)%mod;
    int B=(b+2*a*z+3*z*z)%mod;
    int C=(c+b*z+a*z*z+z*z*z)%mod;
    if(A%p||B%(p*p)||C%(p*p*p)) continue;
    int seen=0;
    for(int y=0;y<p;++y){
      if(( ( ( (y+(A/p)) *y + B/(p*p) )*y + C/(p*p*p))%p)==0)++seen;
    }
    if(seen==3)return true;
  }
  return false;
}
int main(){
  for(int p: {3}){
    int mod=p*p*p*p, maxr=0, observed=0, predicted_count=0;
    long long examined=0; map<int,long long> hist;
    for(int a=0;a<mod;++a) for(int b=0;b<mod;++b) for(int c=0;c<mod;++c){
      int r=roots(p,a,b,c);++examined;hist[r]++;
      if(r>maxr)maxr=r;
      bool eq=predicted(p,a,b,c);
      if(r==3*p*p) ++observed;
      if(eq)++predicted_count;
      if(eq!=(r==3*p*p)) throw runtime_error("classification mismatch");
    }
    if(maxr!=3*p*p||observed!=p*p*p*p||predicted_count!=observed)throw runtime_error("maximum/count mismatch");
    cout<<"VERIFY_OK p="<<p<<" cubics="<<examined<<" max="<<maxr<<" extremizers="<<observed<<" classification=exact";for(auto kv:hist)cout<<" "<<kv.first<<":"<<kv.second; cout<<"\n";
  }
  for(int p:{5,7,11}){
    int r=roots(p,0,-p*p,0);
    if(r!=3*p*p)throw runtime_error("sharpness witness failed");
    cout<<"VERIFY_OK witness_p="<<p<<" roots="<<r<<"\n";
  }
  return 0;
}
