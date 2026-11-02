// Independent exhaustive count via all two-letter prefix sets, without using the A,T family formula.
#include <cstdio>
#include <cstdint>
#include <cassert>
int main(){
 for(int q=2;q<=5;q++){
  const uint32_t total=1u<<(q*q);uint32_t row[5]={}, col[5]={};
  for(int i=0;i<q;i++)for(int j=0;j<q;j++){row[i]|=1u<<(i*q+j);col[j]|=1u<<(i*q+j);}
  uint32_t best=0; uint64_t count=0;
  for(uint32_t p=1;p<total;p++){
   uint32_t acol=0, allowed=(1u<<(q*q))-1u;
   for(int i=0;i<q;i++)if(p&row[i]){acol|=1u<<i;allowed &=~col[i];}
   uint32_t s=allowed &~p;
   unsigned val=__builtin_popcount(p)*__builtin_popcount(s);
   if(val>best){best=val;count=1;}
   else if(val==best)count++;
  }
  std::printf("q=%d max_size_at_n4=%u number_of_labeled_maxima=%llu\n",q,best,(unsigned long long)count);
 }
}
