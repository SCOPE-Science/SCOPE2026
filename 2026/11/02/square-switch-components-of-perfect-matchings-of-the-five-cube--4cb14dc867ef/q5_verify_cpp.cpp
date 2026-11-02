// Exact five-dimensional hypercube perfect-matching square-flip census.
// Standalone C++17; every perfect matching is generated exactly once.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using U = uint64_t;
static vector<int> even_vertices, odd_vertices;
static bool adjacent[16][16] = {};
static vector<U> matchings;
static unordered_map<U,int> index_of;
static void enumerate(int i, uint16_t used_odd, U code) {
    if (i == 16) { matchings.push_back(code); return; }
    for (int j = 0; j < 16; ++j)
        if (adjacent[i][j] && !(used_odd & (uint16_t(1) << j)))
            enumerate(i + 1, uint16_t(used_odd | (uint16_t(1) << j)), code | (U(j) << (4*i)));
}
struct DSU {
    vector<int> p, sz;
    explicit DSU(int n): p(n), sz(n,1) { iota(p.begin(),p.end(),0); }
    int root(int x) { while (p[x] != x) { p[x] = p[p[x]]; x=p[x]; } return x; }
    void unite(int a, int b) {
        a=root(a); b=root(b); if (a==b) return;
        if (sz[a] < sz[b]) swap(a,b);
        p[b]=a; sz[a]+=sz[b];
    }
};
static U replace_two(U code, int i, int j, int partner_i, int partner_j) {
    const U mask = (U(15) << (4*i)) | (U(15) << (4*j));
    return (code & ~mask) | (U(partner_j) << (4*i)) | (U(partner_i) << (4*j));
}
int main() {
    for (int v = 0; v < 32; ++v)
        (__builtin_popcount((unsigned)v)&1 ? odd_vertices : even_vertices).push_back(v);
    assert(even_vertices.size()==16 && odd_vertices.size()==16);
    for (int i=0;i<16;++i) for (int j=0;j<16;++j)
        adjacent[i][j] = (__builtin_popcount((unsigned)(even_vertices[i]^odd_vertices[j])) == 1);
    enumerate(0,0,0);
    const int N = int(matchings.size());
    assert(N == 589185);
    index_of.reserve(size_t(N)*2);
    for (int i=0;i<N;++i) {
        bool newly_inserted = index_of.emplace(matchings[i],i).second;
        assert(newly_inserted);
    }
    assert(index_of.size()==size_t(N));
    DSU dsu(N);
    long long edge_count=0;
    vector<int> degrees(N);
    for (int k=0;k<N;++k) {
        const U code=matchings[k];
        int p[16]; for (int i=0;i<16;++i) p[i]=int((code>>(4*i))&15);
        for (int i=0;i<16;++i) for (int j=i+1;j<16;++j)
            if (adjacent[i][p[j]] && adjacent[j][p[i]]) {
                const U other=replace_two(code,i,j,p[i],p[j]);
                auto it=index_of.find(other);
                assert(it != index_of.end());
                ++degrees[k];
                if (it->second>k) {
                    ++edge_count;
                    dsu.unite(k,it->second);
                }
            }
    }
    assert(edge_count == 3219360);
    map<int,int> component_count;
    map<int,long long> degree_sum_in_component;
    for (int k=0;k<N;++k) {
        int root=dsu.root(k), size=dsu.sz[root];
        if (root==k) component_count[size]++;
        degree_sum_in_component[size] += degrees[k];
        if (size==1) assert(degrees[k]==0);
        if (size==4) assert(degrees[k]==2);
    }
    const map<int,int> expected={{1,120},{4,80},{99280,1},{489465,1}};
    const map<int,long long> expected_degree_sums={{1,0},{4,640},{99280,719360},{489465,5718720}};
    assert(component_count == expected);
    assert(degree_sum_in_component == expected_degree_sums);
    long long deg_sum=0; for (int d:degrees) deg_sum+=d;
    assert(deg_sum==2*edge_count);
    cout << "Q5_BIPARTITE_PARTNER_EXHAUSTIVE_PASS\n";
    cout << "Q5_202_COMPONENTS_AND_EXACT_EDGES_PASS\n";
    cout << "matchings=" << N << " flip_edges=" << edge_count << " components=";
    for (auto [s,c]:component_count) cout << s << "x" << c << " ";
    cout << "\n";
    return 0;
}
