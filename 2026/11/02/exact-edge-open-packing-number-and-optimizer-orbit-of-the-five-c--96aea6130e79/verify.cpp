// Exhaustive certificate for edge-open packings of the five-dimensional cube.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Mask = unsigned __int128;
using Edge = std::pair<int,int>;
static std::vector<Edge> edges;
static std::array<Mask,80> compatible{};
static std::array<int,13> path{};
static std::set<std::string> optimal_sets;
static std::uint64_t nodes = 0;
static std::uint64_t solution_count = 0;
static std::uint64_t by_center_parity[2] = {0,0};
static bool property_ok = true;

static int popcount(Mask s) {
    return __builtin_popcountll((std::uint64_t)s)
         + __builtin_popcountll((std::uint64_t)(s >> 64));
}
static int least_bit(Mask s) {
    std::uint64_t lo = (std::uint64_t)s;
    return lo ? __builtin_ctzll(lo) : 64 + __builtin_ctzll((std::uint64_t)(s >> 64));
}
static std::string code(const std::vector<int>& ids) {
    std::string bits(80,'0');
    for (int i : ids) bits[i] = '1';
    return bits;
}
static int edge_index(int a, int b) {
    Edge p{std::min(a,b), std::max(a,b)};
    auto it = std::find(edges.begin(),edges.end(),p);
    return it == edges.end() ? -1 : (int)(it - edges.begin());
}
// Greedy proper coloring of the *compatibility* graph induced by P.
// Each color class is an independent set, hence any clique uses at most
// one vertex from each color class. This is a provable pruning bound.
static int coloring_upper_bound(Mask P) {
    int colors = 0;
    while (P) {
        ++colors;
        Mask Q = P;
        while (Q) {
            int v = least_bit(Q);
            Mask b = Mask(1) << v;
            P &= ~b;
            Q &= ~b;
            Q &= ~compatible[v];
        }
    }
    return colors;
}
static void analyze_optimum() {
    std::array<int,32> degree{};
    std::vector<int> ids;
    ids.reserve(12);
    for (int i=0;i<12;++i) {
        int e = path[i]; ids.push_back(e);
        ++degree[edges[e].first]; ++degree[edges[e].second];
    }
    if (!optimal_sets.insert(code(ids)).second) property_ok = false;
    std::vector<int> centers;
    for (int v=0;v<32;++v) {
        if (degree[v] > 1) {
            if (degree[v] != 3) property_ok = false;
            centers.push_back(v);
        } else if (degree[v] > 0 && degree[v] != 1) property_ok = false;
    }
    if (centers.size() != 4) { property_ok = false; return; }
    int par = __builtin_popcount((unsigned)centers[0]) & 1;
    for (int c : centers)
        if ((__builtin_popcount((unsigned)c) & 1) != par) property_ok = false;
    ++by_center_parity[par];
    std::vector<int> distances;
    for (int i=0;i<4;++i)
        for (int j=i+1;j<4;++j)
            distances.push_back(__builtin_popcount((unsigned)(centers[i]^centers[j])));
    std::sort(distances.begin(),distances.end());
    if (distances != std::vector<int>({2,2,4,4,4,4})) property_ok = false;
}
// At each recursion node P contains only candidate edge-indices larger
// than the previously chosen index. Branches therefore enumerate each
// clique of the chosen size exactly once, with no repeated sets.
static void enumerate(Mask P, int depth, int target) {
    ++nodes;
    if (depth == target) {
        ++solution_count;
        if (target == 12) analyze_optimum();
        return;
    }
    if (popcount(P) < target-depth) return;
    if (coloring_upper_bound(P) < target-depth) return;
    while (P) {
        int v = least_bit(P);
        P &= ~(Mask(1) << v);
        path[depth] = v;
        enumerate(P & compatible[v],depth+1,target);
    }
}
int main() {
    for (int u=0;u<32;++u)
        for (int k=0;k<5;++k) {
            int v = u ^ (1 << k);
            if (u<v) edges.emplace_back(u,v);
        }
    if (edges.size()!=80) return 1;
    int conflicts=0;
    for (int i=0;i<80;++i)
        for (int j=0;j<i;++j) {
            auto [a,b]=edges[i]; auto [c,d]=edges[j];
            bool bad=false;
            for (int u : {a,b}) for (int v : {c,d}) {
                if (u == v || __builtin_popcount((unsigned)(u^v)) != 1) continue;
                Edge third{std::min(u,v), std::max(u,v)};
                if (third!=edges[i] && third!=edges[j]) bad=true;
            }
            if (bad) ++conflicts;
            else {
                compatible[i] |= Mask(1) << j;
                compatible[j] |= Mask(1) << i;
            }
        }
    if (conflicts!=1120) return 2;
    Mask all=(Mask(1)<<80)-1;
    enumerate(all,0,12);
    std::uint64_t twelves=solution_count;
    std::uint64_t nodes12=nodes;
    if (twelves!=80 || by_center_parity[0]!=40 ||
        by_center_parity[1]!=40 || !property_ok || optimal_sets.size()!=80)
        return 3;
    solution_count=0; nodes=0;
    enumerate(all,0,13);
    std::uint64_t thirteens=solution_count;
    std::uint64_t nodes13=nodes;
    if (thirteens!=0) return 4;

    // Construct all candidate extremizers independently from four centers.
    // a has weight 2; b has weight 4; their supports meet in exactly one bit.
    std::set<std::string> constructed;
    for (int x=0;x<32;++x)
        for (int a=0;a<32;++a) if (__builtin_popcount((unsigned)a)==2)
            for (int b=0;b<32;++b)
                if (__builtin_popcount((unsigned)b)==4 &&
                    __builtin_popcount((unsigned)(a&b))==1) {
                    std::array<int,4> C{x,x^a,x^b,x^a^b};
                    std::vector<int> pack;
                    for (int c : C)
                        for (int k=0;k<5;++k) {
                            int v=c^(1<<k), neighbors=0;
                            for (int t : C)
                                neighbors += (__builtin_popcount((unsigned)(v^t))==1);
                            if (neighbors == 1) {
                                int idx=edge_index(c,v);
                                if (idx<0) return 5;
                                pack.push_back(idx);
                            }
                        }
                    if (pack.size()!=12) return 6;
                    std::sort(pack.begin(),pack.end());
                    for (int i=0;i<12;++i)
                        for (int j=0;j<i;++j)
                            if (!(compatible[pack[i]] & (Mask(1)<<pack[j]))) return 7;
                    constructed.insert(code(pack));
                }
    if (constructed.size()!=80 || constructed!=optimal_sets) return 8;
    std::cout << "Q5 edge-open packing: maximum=12; extremizers=80; "
              << "parity_split=40+40; one affine-coordinate orbit.\n"
              << "conflicting_pairs=" << conflicts
              << "; 12_cliques=" << twelves << "; 13_cliques=" << thirteens
              << "; nodes_12=" << nodes12 << "; nodes_13=" << nodes13 << "\n"
              << "VERIFY_OK\n";
    return 0;
}
