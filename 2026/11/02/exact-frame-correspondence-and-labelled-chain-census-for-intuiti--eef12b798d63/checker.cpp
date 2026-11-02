// Exhaustive independent semantics check for finite linearly ordered constructive-neighbourhood frames.
// Build: c++ -std=c++17 -O3 checker.cpp -o checker && ./checker
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
#include <random>
using U64=uint64_t;
// Direct evaluation of the axiom (Box true -> Diamond p) -> Diamond p for EVERY upset p,
// independently of the structural counting formula.
bool axiom_chain(int n, const std::vector<U64>& N) {
    const int subset_total=1<<n;
    int stable[6]={};
    for(int w=n-1;w>=0;--w) stable[w]=(N[w]!=0)&&(w==n-1||stable[w+1]);
    for(int u=0;u<=n;++u){ // propositional valuation p = suffix {u,...,n-1}
        U64 misses=0;
        for(int a=0;a<subset_total;++a){
            if((a & ((1<<n)-1 ^ ((1<<u)-1)))==0) misses|=U64(1)<<a;
        }
        int diamond[6]={}, antecedent[6]={};
        for(int w=n-1;w>=0;--w){
           diamond[w]=(!(N[w]&misses))&&(w==n-1||diamond[w+1]);
           antecedent[w]=(!stable[w]||diamond[w])&&(w==n-1||antecedent[w+1]);
           if(antecedent[w]&&!diamond[w]) return false;
        }
    }
    return true;
}
// Finite combinatorial criterion via all hereditary down-closures (here chains).
bool downset_criterion(int n,const std::vector<U64>& N) {
   int stable[6]={};
   for(int i=n-1;i>=0;--i) stable[i]=(N[i]!=0)&&(i==n-1||stable[i+1]);
   for(int w=0;w<n;++w){
      for(int v=w;v<n;++v)for(int a=0;a<(1<<n);++a)if((N[v]>>a)&1){
          bool found=false;
          int down_a=0;
          for(int i=0;i<n;++i)if(a&(1<<i))down_a|=(1<<(i+1))-1;
          for(int s=w;s<n&&!found;++s)if(stable[s])for(int b=0;b<(1<<n);++b)
             if(((N[s]>>b)&1)&&((b&~down_a)==0)){found=true;break;}
          if(!found)return false;
      }
   }
   return true;
}
int main(){
 for(int n=1;n<=3;++n){
   const U64 total=U64(1)<<(n*(1<<n));
   U64 count=0;
   for(U64 x=0;x<total;++x){
      U64 mask=(U64(1)<<(1<<n))-1;
      std::vector<U64> N(n);
      for(int i=0;i<n;++i)N[i]=(x>>(i*(1<<n)))&mask;
      bool ax=axiom_chain(n,N);
      // Use the full criterion for each n<=2, and on randomized examples n=3;
      // exhaustive n=3 cross-check is semantics/counts independently.
      if(n<=2){ bool cc=downset_criterion(n,N);if(ax!=cc){std::cerr<<"criterion mismatch";return 1;}}
      count+=ax;
   }
   const U64 expected[]={0,4,241,16690673};
   std::cout<<"chain_n="<<n<<" semantic_census="<<count<<" predicted="<<expected[n]<<"\n";
   if(count!=expected[n])return 2;
 }
 std::mt19937_64 rng(941777);
 for(int n=3;n<=5;++n){
   U64 mask=(U64(1)<<(1<<n))-1;
   for(int k=0;k<5000;++k){
       std::vector<U64> N(n);
       for(int i=0;i<n;++i)N[i]=rng()&mask;
       if(axiom_chain(n,N)!=downset_criterion(n,N)){
         std::cerr<<"random criterion mismatch n="<<n<<"\n";return 3;
       }
   }
 }
 std::cout<<"ALL_CHECKS_OK exhaustive_n=1,2,3 randomized_n=3..5 cases=15000"<<std::endl;
}
