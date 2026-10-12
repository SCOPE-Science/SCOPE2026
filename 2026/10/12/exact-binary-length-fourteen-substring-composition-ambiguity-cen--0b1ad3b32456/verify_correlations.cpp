// Independent, exact reconstruction by all prefix-sum-difference vectors.
// Build: c++ -std=c++17 -O2 verify_correlations.cpp -o verify_correlations
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int main() {
  constexpr int n=14;
  map<vector<int>, vector<string>> classes;
  for (int x=0; x<(1<<n); ++x) {
    array<int,n+1> prefix{};
    string w;
    for(int i=0; i<n; ++i) {
      int b=(x>>(n-1-i))&1;
      w += static_cast<char>('0'+b);
      prefix[i+1] = prefix[i] + b;
    }
    vector<int> sig((n+1)*(n+1),0);
    for(int left=0; left<n; ++left)
      for(int right=left+1; right<=n; ++right) {
        const int length=right-left;
        const int ones=prefix[right]-prefix[left];
        ++sig[length*(n+1)+ones];
      }
    classes[move(sig)].push_back(w);
  }
  map<int,int> histogram;
  vector<vector<string>> big;
  for (auto &kv: classes) {
    ++histogram[(int)kv.second.size()];
    if(kv.second.size()==4) {
      sort(kv.second.begin(),kv.second.end());
      big.push_back(kv.second);
    }
  }
  sort(big.begin(),big.end());
  assert(histogram.size()==3 && histogram[1]==128 && histogram[2]==8104 && histogram[4]==12);
  assert(classes.size()==8244 && big.size()==12);
  int words=0;
  for(auto &kv:classes) words+=(int)kv.second.size();
  assert(words==(1<<n));
  cout << "n=14 words=" << words << " profiles=" << classes.size()
       << " histogram=1:128,2:8104,4:12\n";
  for(auto &row:big) {
    for(size_t i=0;i<row.size();++i) cout << (i?" ":"") << row[i];
    cout << "\n";
  }
  return 0;
}
