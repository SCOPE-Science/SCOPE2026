// Exhaustive endpoint-induced-star verification for rectangular two-rail ladders.
// Compile: c++ -std=c++17 -O3 verify.cpp -o verify && ./verify
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;

int main() {
    unsigned long long total_masks = 0;
    for (int n = 2; n <= 11; ++n) {
        const int N = 2*n;
        vector<uint32_t> adj(N, 0);
        auto add_edge = [&](int a, int b) {
            adj[a] |= (uint32_t(1) << b);
            adj[b] |= (uint32_t(1) << a);
        };
        for (int j=0; j<n; ++j) {
            add_edge(j,n+j);
            if (j+1<n) {
                add_edge(j,j+1);
                add_edge(n+j,n+j+1);
            }
        }
        int maximum=0;
        uint64_t number=0;
        for(uint32_t mask=1; mask<(uint32_t(1)<<N); ++mask) {
            int degree[24]={0};
            bool all_nonisolated=true;
            int degree_sum=0;
            for(int v=0; v<N; ++v) if(mask & (uint32_t(1)<<v)) {
                degree[v]=__builtin_popcount(adj[v]&mask);
                if(degree[v]==0) {all_nonisolated=false; break;}
                degree_sum+=degree[v];
            }
            if(!all_nonisolated) continue;
            // An isolate-free graph is a disjoint union of stars iff
            // no edge has both endpoints of degree at least two.
            bool stars=true;
            for(int u=0; u<N && stars; ++u) if((mask&(uint32_t(1)<<u)) && degree[u]>1)
                for(int v=u+1; v<N; ++v)
                    if((mask&(uint32_t(1)<<v)) && degree[v]>1 &&
                       (adj[u]&(uint32_t(1)<<v))) {stars=false; break;}
            if(!stars) continue;
            int edges=degree_sum/2;
            if(edges>maximum) {maximum=edges;number=0;}
            if(edges==maximum) ++number;
        }
        total_masks += (uint64_t(1)<<N)-1;
        uint64_t predicted = (n%3==2) ? 4 : 2;
        if (maximum!=n || number!=predicted) {
            cerr << "FAIL n=" << n << " found=" << maximum
                 << " count=" << number << " expected=" << predicted << '\n';
            return 1;
        }
        cout << "n=" << n << " optimum=" << maximum
             << " number_of_optima=" << number << " OK\n";
    }
    cout << "all_cases=10 masks_tested=" << total_masks << " VERIFY_OK\n";
    return 0;
}
