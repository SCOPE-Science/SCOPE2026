// Deterministic exhaustive generator of nonextendible 12-multisets modulo 36.
// Compile: c++ -std=c++17 -O2 sun6_enumerate.cpp -o sun6_enumerate
// Run: ./sun6_enumerate > sun6_extremals.txt
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
using U = std::uint64_t;
constexpr U MODMASK = (U{1} << 36) - 1;
constexpr U FORBIDDEN = (U{1} << 6) | (U{1} << 12) |
                       (U{1} << 18) | (U{1} << 24) | (U{1} << 30);
constexpr std::array<int,30> VALUES = {
  1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,
  19,20,21,22,23,25,26,27,28,29,31,32,33,34,35
};
std::array<std::uint64_t,13> levels{};
std::array<int,12> sequence{};
U count = 0;
inline U shift(U bits, int x) {
  return x == 0 ? bits : ((bits << x) | (bits >> (36-x))) & MODMASK;
}
void visit(int first, int depth, const std::array<U,7>& sums) {
  ++levels[depth];
  if (depth == 12) {
    // Any new six-sum must contain the appended element, hence must use
    // one of the five-term sums from this twelve-element multiset.
    for (int x: VALUES) {
      if ((shift(sums[5],x) & FORBIDDEN) == 0) {
        std::cerr << "Unexpected admissible extension\n";
        std::exit(2);
      }
    }
    ++count;
    for (int j=0;j<12;++j)
      std::cout << (j ? " " : "") << sequence[j];
    std::cout << '\n';
    return;
  }
  for (int j=first;j<30;++j) {
    int x=VALUES[j];
    auto next=sums;
    for (int k=std::min(depth+1,6);k>=1;--k)
      next[k] |= shift(sums[k-1],x);
    // This forbidden subset will persist under all further extensions.
    if ((next[6] & FORBIDDEN)!=0) continue;
    sequence[depth]=x;
    visit(j,depth+1,next);
  }
}
int main() {
  std::array<U,7> initial{};
  initial[0]=1;
  visit(0,0,initial);
  constexpr std::array<U,13> expected = {
    1,30,465,4960,40920,278256,1397210,
    3565140,3172686,1271740,500586,156528,23970
  };
  if (count!=23970 || levels!=expected) return 3;
  std::cerr << "GENERATOR_OK width12=" << count
            << " nonextendible=23970\n";
}
