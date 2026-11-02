// Independent direct-subset validator for the exact 12-term certificate.
// Compile: c++ -std=c++17 -O2 sun6_crosscheck.cpp -o sun6_crosscheck
// Run: ./sun6_crosscheck < sun6_extremals.txt
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
using Row = std::array<int,12>;
using Pattern = std::array<int,5>;
const std::array<int,30> allowed = {
  1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,
  19,20,21,22,23,25,26,27,28,29,31,32,33,34,35
};
std::set<int> six, five;
void choose(const Row& row,int position,int left,int sum,int k) {
  if (left==0) { (k==6 ? six : five).insert(sum%36); return; }
  for (int j=position;j<=12-left;++j)
    choose(row,j+1,left-1,sum+row[j],k);
}
int main() {
  std::set<Row> remaining;
  std::map<Pattern,int> patterns;
  Row row, previous{};
  bool first=true;
  std::size_t checked=0;
  while (std::cin >> row[0]) {
    for (int j=1;j<12;++j) if (!(std::cin >> row[j])) return 1;
    if (!std::is_sorted(row.begin(),row.end())) return 2;
    for (int x:row) if (x<=0||x>=36||x%6==0) return 3;
    if (!first && !(previous<row)) return 4;
    previous=row;first=false;
    six.clear(); five.clear();
    choose(row,0,6,0,6);
    choose(row,0,5,0,5);
    for (int t=6;t<=30;t+=6)
      if (six.count(t)) return 5;
    for (int x:allowed) {
      bool blocked=false;
      for (int s:five) if ((s+x)%6==0 && (s+x)%36!=0) {
        blocked=true;break;
      }
      if (!blocked) return 6;
    }
    Pattern p{};
    for (int x:row) ++p[x%6-1];
    ++patterns[p];
    remaining.insert(row);
    ++checked;
  }
  if (checked!=23970 || remaining.size()!=checked) return 7;
  std::map<int,int> orbit_sizes;
  int orbits=0;
  while (!remaining.empty()) {
    const Row representative=*remaining.begin();
    std::set<Row> orbit;
    for (int u=1;u<36;++u) if (std::gcd(u,36)==1) {
      for (int t=0;t<6;++t) {
        Row transformed{};
        for (int j=0;j<12;++j)
          transformed[j]=(u*representative[j]+6*t)%36;
        std::sort(transformed.begin(),transformed.end());
        orbit.insert(transformed);
      }
    }
    for (const Row& item:orbit)
      if (remaining.erase(item)!=1) return 8;
    ++orbit_sizes[static_cast<int>(orbit.size())];
    ++orbits;
  }
  if (orbits!=361 || orbit_sizes!=std::map<int,int>{{12,13},{18,1},{36,33},{72,314}})
    return 9;
  const std::map<Pattern,int> expected = {
    {{{0,6,6,0,0}},5928}, {{{0,0,6,6,0}},5928},
    {{{6,6,0,0,0}},5850}, {{{0,0,0,6,6}},5850},
    {{{5,1,0,1,5}},108}, {{{1,5,0,5,1}},108},
    {{{0,5,2,5,0}},54},
    {{{5,5,0,1,1}},36}, {{{1,5,5,1,0}},36},
    {{{1,1,0,5,5}},36}, {{{0,1,5,5,1}},36}
  };
  if (patterns!=expected) return 10;
  std::cout << "CROSSCHECK_OK rows="<<checked << " orbits="<<orbits
            << " patterns="<<patterns.size()<<"\n";
}
