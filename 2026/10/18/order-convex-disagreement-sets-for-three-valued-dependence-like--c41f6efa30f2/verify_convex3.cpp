// Exhaustive count of order-convex subsets of the information cube K^3
// avoiding the all-unknown point. This verifies one finite consequence,
// not the all-arity theorem.
#include <cstdint>
#include <iostream>
#include <vector>

struct Interval { uint32_t a, b, middle; };
int digit(int x, int i) { return i==0 ? x/9 : (i==1 ? (x/3)%3 : x%3); }
bool leq(int a, int b) {
  for (int i=0; i<3; ++i) {
    int x=digit(a,i), y=digit(b,i);
    if (x!=1 && x!=y) return false;
  }
  return true;
}
int main() {
  constexpr int center = 13; // (unknown,unknown,unknown)
  std::vector<Interval> intervals;
  for(int a=0; a<27; ++a) for(int b=0; b<27; ++b) {
    if(a==b || !leq(a,b)) continue;
    uint32_t between=0;
    for(int m=0; m<27; ++m) {
      if (m!=a && m!=b && leq(a,m) && leq(m,b)) between |= (1u<<m);
    }
    if(between) intervals.push_back({1u<<a,1u<<b,between});
  }
  uint64_t count=0;
  for(uint32_t S=0; S<(1u<<27); ++S) {
    if(S & (1u<<center)) continue;
    bool convex=true;
    for(const auto &I: intervals) {
      if ((S & I.a) && (S & I.b) && (S & I.middle)!=I.middle) {
        convex=false; break;
      }
    }
    if(convex) ++count;
  }
  std::cout << "three_variable_convex_disagreement_sets=" << count << '\n';
  if(count!=3886222ull) return 1;
  std::cout << "TERNARY_CONVEX_CENSUS_OK\n";
}
