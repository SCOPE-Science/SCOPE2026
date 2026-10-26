// Complete ordinal certificate for three fixed couples and four indivisible goods.
// Compile: c++ -std=c++17 -O2 verify_four_goods.cpp -o verify_four_goods
// Run: ./verify_four_goods
// Uses only standard C++ and exact integer arithmetic.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

struct Allocation {
  array<int,4> group_of_good;
  int pair_group;
  array<int,2> pair_goods;
  array<int,3> singleton_good; // -1 for the pair group
};

int main() {
  // An entry in an order lists the goods from highest to lowest value.
  vector<array<int,4>> orders;
  array<int,4> order = {0,1,2,3};
  do { orders.push_back(order); } while (next_permutation(order.begin(), order.end()));
  assert(orders.size() == 24);

  // All 36 labeled balanced allocations: one pair and two singletons.
  vector<Allocation> allocations;
  for (int pair_group=0; pair_group<3; ++pair_group)
    for (int x=0; x<4; ++x)
      for (int y=x+1; y<4; ++y) {
        array<int,2> other_groups;
        int n=0;
        for (int g=0; g<3; ++g)
          if (g != pair_group) other_groups[n++] = g;
        array<int,2> remaining;
        n=0;
        for (int good=0; good<4; ++good)
          if (good!=x && good!=y) remaining[n++] = good;
        for (int flip=0; flip<2; ++flip) {
          Allocation a;
          a.pair_group = pair_group;
          a.pair_goods = {x,y};
          a.singleton_good = {-1,-1,-1};
          a.singleton_good[other_groups[0]] = remaining[flip];
          a.singleton_good[other_groups[1]] = remaining[1-flip];
          a.group_of_good = {-1,-1,-1,-1};
          a.group_of_good[x] = a.group_of_good[y] = pair_group;
          for (int g:other_groups) a.group_of_good[a.singleton_good[g]] = g;
          allocations.push_back(a);
        }
      }
  assert(allocations.size()==36);

  // For a singleton-group agent, EF1 fails iff her singleton is below
  // both goods in the pair. Agents in the pair group cannot violate EF1
  // because all other bundles are singletons and values are nonnegative.
  // Therefore ranking, not cardinal magnitude, decides EF1.
  uint64_t bad[3][24] = {};
  for (int group=0; group<3; ++group)
    for (int k=0; k<24; ++k) {
      array<int,4> position;
      for (int j=0; j<4; ++j) position[orders[k][j]]=j;
      for (int a=0; a<36; ++a) {
        const Allocation& z=allocations[a];
        if (z.pair_group==group) continue;
        int b=z.singleton_good[group];
        int x=z.pair_goods[0], y=z.pair_goods[1];
        if (position[b]>position[x] && position[b]>position[y])
          bad[group][k] |= (uint64_t(1)<<a);
      }
      assert(__builtin_popcountll(bad[group][k])==8);
    }

  // Simultaneously relabeling goods does not change the EF1 count.
  // The first member of the first couple can therefore be normalized
  // to order (0,1,2,3). The other five members range independently over
  // ALL 24 strict orders: 24^5 exhaustive normalized profiles.
  const uint64_t full=(uint64_t(1)<<36)-1;
  array<uint64_t,37> histogram{};
  uint64_t profile_count=0;
  int minimum=37, maximum=-1;
  array<int,5> minimum_witness={-1,-1,-1,-1,-1};
  for (int p1=0; p1<24; ++p1)
    for (int p2=0; p2<24; ++p2)
      for (int p3=0; p3<24; ++p3)
        for (int p4=0; p4<24; ++p4)
          for (int p5=0; p5<24; ++p5) {
            uint64_t eliminated = bad[0][0] | bad[0][p1] |
               bad[1][p2] | bad[1][p3] | bad[2][p4] | bad[2][p5];
            int valid=__builtin_popcountll(full & ~eliminated);
            ++histogram[valid];
            ++profile_count;
            if (valid<minimum) {
              minimum=valid;
              minimum_witness={p1,p2,p3,p4,p5};
            }
            if (valid>maximum) maximum=valid;
          }

  assert(profile_count == 7962624ULL); // 24^5, no sampling
  assert(minimum == 2 && maximum == 18);
  assert(histogram[0]==0 && histogram[1]==0);
  assert(histogram[2] == 6912); // 1/1152 of all strict profiles
  // Independent expectation check: each of the four agents in singleton
  // groups passes with probability 2/3, so E[count]=36*(2/3)^4=64/9.
  uint64_t weighted_sum=0;
  for (int k=0; k<=36; ++k) weighted_sum+=uint64_t(k)*histogram[k];
  assert(9*weighted_sum==64*profile_count);

  cout << "normalized_profiles " << profile_count << "\n";
  cout << "minimum " << minimum << " maximum " << maximum << "\n";
  cout << "witness_order_indices ";
  for (int k: minimum_witness) cout << k << ' ';
  cout << "\n";
  cout << "number_of_fair_allocations normalized_profile_count\n";
  for (int k=0; k<=36; ++k)
    if (histogram[k]) cout << k << ' ' << histogram[k] << "\n";
  cout << "expected_number 64/9\n";
}
