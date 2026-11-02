// Independent target-first exact exhaustive verifier; C++17.
// No ball unions, no 64-bit bitset coverage table: direct Hamming comparisons.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
static int distance(unsigned a,unsigned b){int h=0;for(unsigned z=a^b;z;z&=z-1)++h;return h;}
static string readword(uint32_t x,int L){string s;for(int i=0;i<L;++i)s.push_back('0'+((x>>i)&1u));return s;}
static string normal(string s){string best=s;for(size_t k=0;k<s.size();++k){rotate(s.begin(),s.begin()+1,s.end());if(s<best)best=s;}return best;}
static bool test(unsigned n,unsigned L,uint32_t x){
 vector<unsigned> windows(L,0);
 for(unsigned start=0;start<L;++start)
  for(unsigned j=0;j<n;++j)windows[start]|=((x>>((start+j)%L))&1u)<<j;
 for(unsigned target=0;target<(1u<<n);++target){
   bool hit=false;
   for(unsigned w:windows)if(distance(target,w)<=2){hit=true;break;}
   if(!hit)return false;
 }
 return true;
}
int main(){
 for(unsigned n=7;n<=9;++n){
  unsigned L=(n==7?10:n==8?14:20);
  for(unsigned ell=1;ell<=L;++ell){
   unsigned long long count=0;set<string> reps;
   for(uint32_t x=0;x<(1u<<ell);++x)
    if(test(n,ell,x)){++count;reps.insert(normal(readword(x,ell)));}
   cout<<"length,"<<n<<","<<ell<<","<<count<<","<<reps.size()<<"\n";
   if(ell==L)for(auto& rep:reps)cout<<"orbit,"<<n<<","<<ell<<","<<rep<<"\n";
  }
 }
}
