// Exact exhaustive cyclic-window-weight census for a binary degree-15 cyclic code.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr int N = 31, K = 16;
constexpr uint32_t G = 0x8FAFU; // x^15+x^11+x^10+x^9+x^8+x^7+x^5+x^3+x^2+x+1
uint32_t multiply(uint32_t a,uint32_t b) {
  uint32_t c=0;
  while(b){if(b&1u)c^=a; a<<=1; b>>=1;}
  return c;
}
uint32_t rotate_left_31(uint32_t x){return ((x<<1)&0x7fffffffU)|(x>>30);}
int main(){
  array<array<uint32_t,32>,32> tab{};
  int codes=0;
  for(uint32_t m=0; m<(1u<<K); ++m){
    uint32_t c=multiply(m,G); assert((c>>N)==0);++codes;
    uint32_t mask=0, shifted=c;
    for(int b=1;b<=N;++b){
      mask |= shifted;
      int weight=__builtin_popcount(mask);
      ++tab[b][weight];
      shifted=rotate_left_31(shifted);
    }
  }
  assert(codes==65536);
  for(int b=1;b<=N;++b){
    uint32_t sum=0;
    cout<<b<<":";
    for(int w=0;w<=N;++w){
      uint32_t x=tab[b][w]; sum+=x;
      if(x) cout<<w<<"="<<x<<",";
    }
    cout<<"\n";
    assert(sum==65536 && tab[b][0]==1);
  }
  cerr<<"POLYNOMIAL_CENSUS_OK words="<<codes<<" generator="<<hex<<G<<dec<<"\n";
}
