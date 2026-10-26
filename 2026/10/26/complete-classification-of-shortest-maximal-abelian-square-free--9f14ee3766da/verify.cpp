// Exact enumeration of five-symbol, two-sided maximal Abelian-square-free words.
// Build: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Newly created Abelian squares necessarily end at the appended character.
bool has_square_suffix(const vector<int>& w) {
  int n = static_cast<int>(w.size());
  for (int h = 1; 2*h <= n; ++h) {
    int diff[5] = {};
    for (int j = n-2*h; j < n-h; ++j) ++diff[w[j]];
    for (int j = n-h; j < n; ++j) --diff[w[j]];
    bool zero=true;
    for (int x : diff) if (x != 0) { zero=false; break; }
    if (zero) return true;
  }
  return false;
}

bool has_square_prefix(const vector<int>& w) {
  int n = static_cast<int>(w.size());
  for (int h = 1; 2*h <= n; ++h) {
    int diff[5] = {};
    for (int j = 0; j < h; ++j) ++diff[w[j]];
    for (int j = h; j < 2*h; ++j) --diff[w[j]];
    bool zero=true;
    for (int x : diff) if (x != 0) { zero=false; break; }
    if (zero) return true;
  }
  return false;
}

bool maximal_on_both_sides(vector<int>& w) {
  for (int x=0; x<5; ++x) {
    w.push_back(x);
    bool right=has_square_suffix(w);
    w.pop_back();
    if (!right) return false;
    w.insert(w.begin(),x);
    bool left=has_square_prefix(w);
    w.erase(w.begin());
    if (!left) return false;
  }
  return true;
}

struct Enumerator {
  vector<int> w = {0};
  long long nodes[17] = {};
  long long bicrucial[17] = {};
  vector<string> witnesses;

  void visit(int max_seen) {
    int n=static_cast<int>(w.size());
    ++nodes[n];
    // An unused alphabet symbol can be adjoined without forming a square.
    if (max_seen==4 && maximal_on_both_sides(w)) {
      ++bicrucial[n];
      if (n==16) {
        string s;
        for (int x : w) s.push_back(static_cast<char>('0'+x));
        witnesses.push_back(s);
      }
    }
    if (n==16) return;
    // First-occurrence normalization gives a unique representative per orbit.
    for (int x=0; x<=min(4,max_seen+1); ++x) {
      w.push_back(x);
      if (!has_square_suffix(w)) visit(max(max_seen,x));
      w.pop_back();
    }
  }
};

int main() {
  Enumerator e;
  e.visit(0);
  for (int n=1;n<=15;++n)
    if (e.bicrucial[n]!=0) { cerr << "unexpected shorter word" << '\n'; return 1; }
  if (e.bicrucial[16]!=4) { cerr << "unexpected count" << '\n'; return 2; }
  if (e.nodes[13]!=209190 || e.nodes[14]!=690853 ||
      e.nodes[15]!=2278400 || e.nodes[16]!=7421303) {
    cerr << "unexpected search cardinalities" << '\n'; return 3;
  }
  sort(e.witnesses.begin(),e.witnesses.end());
  vector<string> expected={
    "0102134031201343", "0102134031210343",
    "0102342031024323", "0102343021034232"
  };
  if (e.witnesses!=expected) { cerr << "unexpected witnesses" << '\n'; return 4; }
  cout << "VERIFY_OK length=16 canonical_count=4 labeled_count=480" << '\n';
  cout << "CANONICAL_SQUAREFREE_DEPTH_COUNTS"
       << " n13=" << e.nodes[13] << " n14=" << e.nodes[14]
       << " n15=" << e.nodes[15] << " n16=" << e.nodes[16] << '\n';
  for (const string& s : e.witnesses) cout << s << '\n';
}
