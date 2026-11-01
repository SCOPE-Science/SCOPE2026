// Direct state-space checker, independent of the proof's coordinate transformation.
// Compile: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <numeric>
using namespace std;
static unsigned sweep(unsigned state, int n, int k) {
  for (int i=0; i<n; ++i) {
    unsigned nextbit = __builtin_parity(state);
    if (i<2*k) nextbit ^= ((state >> (i^1)) & 1u);
    state = (state & ~(1u<<i)) | (nextbit<<i);
  }
  return state;
}
static unsigned fixed_exponent(int n,int k,int t) {
  int m=n-2*k, g=gcd(m+1,t);
  return (unsigned)(g-1+(t%2==0?2*k:k+(k&1)));
}
int main() {
  uint64_t total=0;
  for (int n=4;n<=16;n+=2) for(int k=0;k<=n/2;++k) {
    int order=(n-2*k+1)*(k>=2?2:1);
    unsigned N=1u<<n;
    vector<unsigned> next(N);
    for(unsigned state=0;state<N;++state) next[state]=sweep(state,n,k);
    map<int,uint64_t> periods;
    for(unsigned initial=0;initial<N;++initial) {
      unsigned x=initial;
      int period=0;
      do {x=next[x];++period;assert(period<=order);} while(x!=initial);
      assert(order%period==0);
      ++periods[period];
      ++total;
    }
    int max_seen=periods.rbegin()->first;
    assert(max_seen==order);
    for (int t=1;t<=order;++t) if(order%t==0){
      uint64_t actual=0;
      for (const auto &z:periods) if(t%z.first==0)actual+=z.second;
      uint64_t expected=1ull<<fixed_exponent(n,k,t);
      if(actual!=expected){cerr<<"FAIL "<<n<<" "<<k<<" "<<t<<"\n";return 2;}
    }
    cout << "n="<<n<<" k="<<k<<" period="<<order<<" exact=";
    for(auto z:periods)cout<<z.first<<":"<<z.second<<",";
    cout<<"\n";
  }
  cout<<"VERIFIED direct evolution of "<<total<<" labelled GF(2) configurations across every even order 4..16 and every matching size.\n";
}
