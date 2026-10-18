// Exact modular arithmetic checks for the even-color odd-part overpartition congruence.
// Finite tests support but cannot replace the all-index proof.
#include <cstdint>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
using std::uint64_t;
int main() {
  constexpr int N=2048;
  constexpr uint64_t MASK=(uint64_t(1)<<35)-1;
  uint64_t comparisons=0, square_witnesses=0;
  for (int m : {2,4,6,8,10,12,14,16,20,24,32,48}) {
    std::vector<uint64_t> a(N+1,0); a[0]=1;
    for(int j=1;j<=N;j+=2) for(int color=0;color<m;color++) {
      // 1/(1-q^j), followed by (1+q^j), for each color.
      for(int n=j;n<=N;n++) a[n]=(a[n]+a[n-j])&MASK;
      for(int n=N;n>=j;n--) a[n]=(a[n]+a[n-j])&MASK;
    }
    int t=0; for(int w=m;(w&1)==0;w>>=1) ++t;
    for(int i=(t==1?3:2);i<=7;i++) {
      const int e=(t==1?3*i-4:3*i+2*t-5);
      if(e+1>35) {std::cerr<<"invalid modulus\n";return 2;}
      const uint64_t mod=(uint64_t(1)<<(e+1)), residue=(uint64_t(1)<<e);
      for(int n=0; n<=N/(1<<i);n++) {
        int root=(int)std::sqrt((double)n);
        while((root+1)*(root+1)<=n) root++;
        while(root*root>n) root--;
        bool odd_square=(root%2==1 && root*root==n);
        uint64_t actual=(a[n*(1<<i)]-a[n*(1<<(i-1))])&(mod-1);
        uint64_t expected=odd_square?residue:0;
        if(actual!=expected) {
          std::cerr<<"FAIL m="<<m<<" i="<<i<<" n="<<n<<" actual="<<actual<<" expected="<<expected<<"\n";
          return 1;
        }
        comparisons++; if(odd_square) square_witnesses++;
      }
    }
  }
  std::cout<<"VERIFY_OK cases="<<comparisons<<" odd_square_witnesses="<<square_witnesses
    <<" colors=12 range_max=2048\n";
  return 0;
}
