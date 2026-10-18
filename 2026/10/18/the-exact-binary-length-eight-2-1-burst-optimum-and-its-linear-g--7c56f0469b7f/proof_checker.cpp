// Exact finite check for the length-eight binary (2,1)-burst code problem.
// Build: g++ -std=c++17 -O2 proof_checker.cpp -o proof_checker
// Run:   ./proof_checker
#include <array>
#include <bitset>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

constexpr int N=8, INPUTS=1<<N, OUTPUTS=1<<(N-1);
using Mask=bitset<INPUTS>;
array<bitset<OUTPUTS>,INPUTS> balls;
array<Mask,INPUTS> adjacent;
uint64_t visited=0;
constexpr int TARGET=15;

int first_set(const Mask& mask) {
  for (int j=0;j<INPUTS;j++) if (mask.test(j)) return j;
  abort(); // Called only for a nonempty mask.
}

// Returns true if a clique of size at least TARGET extends prefix.
// Every possible extension lies in P and is compatible with the prefix.
bool search(Mask P, int prefix_size) {
  ++visited;
  if (prefix_size>=TARGET) return true;
  if (P.none()) return false;
  vector<int> order, colors;
  Mask left=P;
  int color=0;
  // Proper greedy vertex coloring of the graph induced by P.
  while (left.any()) {
    ++color;
    Mask eligible=left;
    while (eligible.any()) {
      const int v=first_set(eligible);
      order.push_back(v);
      colors.push_back(color);
      left.reset(v);
      eligible.reset(v);
      eligible &= ~adjacent[v]; // Vertices in a color class are nonadjacent.
    }
  }
  // All remaining vertices at iteration j have color at most colors[j].
  for (int j=int(order.size())-1;j>=0;--j) {
    if (prefix_size+colors[j]<TARGET) return false;
    int v=order[j];
    if (prefix_size+1>=TARGET) return true;
    Mask next=P&adjacent[v];
    if (next.any() && search(next,prefix_size+1)) return true;
    P.reset(v); // Exclude this vertex from all remaining branches.
  }
  return false;
}

void require(bool valid, const char* reason) {
  if (!valid) {cerr << "FAIL " << reason << '\n';exit(1);}
}

bool disjoint_balls(const vector<int>& words) {
  for (int i=0;i<int(words.size());i++)
    for (int j=i+1;j<int(words.size());j++)
      if ((balls[words[i]]&balls[words[j]]).any()) return false;
  return true;
}

int main() {
  // In an eight-bit word, replacing input bits i and i+1 by one arbitrary
  // bit leaves a seven-bit word; i=0,...,6 indexes from the left.
  for (int x=0;x<INPUTS;x++) {
    for (int i=0;i<N-1;i++) for (int bit=0;bit<=1;bit++) {
      const int prefix=x>>(N-i);
      const int suffix=x&((1<<(N-i-2))-1);
      const int y=(prefix<<(N-i-1))|(bit<<(N-i-2))|suffix;
      require(y>=0 && y<OUTPUTS, "received-word range");
      balls[x].set(y);
    }
    require(balls[x].count()==N,"each distinct received ball has size eight");
  }
  // In the compatibility graph, an edge means the channel output sets are
  // disjoint, so a correcting code is precisely a clique.
  for (int x=0;x<INPUTS;x++) for (int y=0;y<INPUTS;y++)
    if (x!=y && (balls[x]&balls[y]).none()) adjacent[x].set(y);
  for(int x=0;x<INPUTS;x++) for(int y=0;y<INPUTS;y++)
    require(adjacent[x].test(y)==adjacent[y].test(x),"adjacency symmetry");

  // Concrete non-linear code of size 14, represented by decimal integers
  // with their usual eight-bit binary expansions.
  const vector<int> construction={12,21,34,51,72,87,126,129,178,187,207,212,237,240};
  require(construction.size()==14,"nonlinear witness size");
  require(disjoint_balls(construction),"nonlinear witness overlap");

  // The indicated three vectors span a dimension-three linear code.
  const int basis[3]={21,79,164};
  vector<int> linear;
  for(int mask=0;mask<8;mask++) {
    int x=0;
    for (int k=0;k<3;k++) if ((mask>>k)&1) x^=basis[k];
    linear.push_back(x);
  }
  for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)
    require(linear[i]!=linear[j],"basis linear independence");
  require(disjoint_balls(linear),"linear witness overlap");

  Mask all;
  all.set();
  require(!search(all,0),"a correcting code of size at least fifteen exists");
  // A binary linear code's size is a power of two, hence <=8 once <=14.
  cout << "VERIFIED maximum size 14, maximum linear size 8, "
       << "packing bound 16, search nodes " << visited << '\n';
  return 0;
}
