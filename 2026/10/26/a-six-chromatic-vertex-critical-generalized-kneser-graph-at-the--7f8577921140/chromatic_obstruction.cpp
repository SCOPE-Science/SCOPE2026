// Exact coloring obstruction for the Kneser graph of independent triples of C9 plus K1.
// No external libraries beyond the standard C++17 library.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static constexpr int N = 57;
array<uint64_t, N> adj{};
array<int, N> col{};
uint64_t visited = 0;

bool five_colorable(int depth, int used) {
    ++visited;
    if (depth == N) return true;
    int best = -1, best_sat = -1, best_uncolored_degree = -1;
    unsigned excluded = 0;
    for (int v = 0; v < N; ++v) if (col[v] == -1) {
        unsigned mask = 0;
        int degree = 0;
        for (uint64_t m = adj[v]; m; m &= m - 1) {
            int w = 0;
            for (uint64_t bit = m & (~m + 1); (bit >>= 1); ) ++w;
            if (col[w] == -1) ++degree;
            else mask |= (1u << col[w]);
        }
        int sat = 0;
        for (unsigned t = mask; t; t &= t - 1) ++sat;
        if (sat > best_sat || (sat == best_sat && degree > best_uncolored_degree)) {
            best = v; best_sat = sat; best_uncolored_degree = degree; excluded = mask;
        }
    }
    if (best < 0) return false;
    // Color permutations allow only one unused color name per step.
    for (int c = 0; c < min(5, used + 1); ++c) if (!(excluded & (1u << c))) {
        col[best] = c;
        bool solved = five_colorable(depth + 1, max(used, c + 1));
        col[best] = -1;
        if (solved) return true;
    }
    return false;
}
int main() {
    vector<unsigned> sets;
    for (int a=0; a<10; ++a) for (int b=a+1; b<10; ++b) for (int c=b+1; c<10; ++c) {
        unsigned x=(1u<<a)|(1u<<b)|(1u<<c);
        bool independent = true;
        for (int i=0; i<9; ++i)
            if ((x & (1u<<i)) && (x & (1u<<((i+1)%9)))) independent=false;
        if (independent) sets.push_back(x);
    }
    if (sets.size() != N) return 1;
    int edge_count = 0;
    for (int v=0; v<N; ++v) for (int w=0; w<v; ++w)
        if (!(sets[v] & sets[w])) {
            adj[v] |= 1ull<<w; adj[w] |= 1ull<<v; ++edge_count;
        }
    if (edge_count != 498) return 2;
    col.fill(-1);
    if (five_colorable(0,0)) return 3;
    if (visited != 122153) return 4;
    cout << "VERIFY_OK vertices=57 edges=498 canonical_search_nodes=" << visited << '\n';
}
