// Exact enumeration by pairs of downsets, independent of ternary-map recursion.
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
vector<uint64_t> ideals(int n){
 vector<uint64_t> v={0,1};
 for(int k=1;k<=n;k++){
  vector<uint64_t> w; int shift=1<<(k-1);
  for(uint64_t a:v)for(uint64_t b:v)if((a&b)==b)w.push_back(a|(b<<shift));
  v.swap(w);
 }
 return v;
}
uint64_t solve(int n){
 auto v=ideals(n);int N=1<<n;const uint64_t FULL=(1ull<<N)-1;
 uint64_t total=0;
 for(uint64_t I:v){
  if(I==0 || I==FULL)continue;
  vector<uint64_t> req;
  for(int a=0;a<N;a++)if((I>>a)&1){
   uint64_t cov=0;
   for(int j=0;j<n;j++)if(!(a&(1<<j)))cov |= 1ull<<(a|(1<<j));
   if((I&cov)==0)req.push_back(cov);
  }
  for(uint64_t J:v){
   if(J==FULL || J==I || (J&I)!=I)continue;
   bool ok=true;
   for(uint64_t cov:req)if(!(cov&J)){ok=false;break;}
   if(ok)total++;
  }
 }
 cout<<"n="<<n<<" ideals="<<v.size()<<" bounded_morphisms="<<total<<"\n";
 return total;
}
int main(){for(int n=1;n<=5;n++)solve(n);}
