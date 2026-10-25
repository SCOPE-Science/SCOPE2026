// Standalone exact check of the FirstFit distribution on crown graphs.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using i64 = long long;

static i64 factorial(int n) {
    i64 v = 1;
    for (int j = 2; j <= n; ++j) v *= j;
    return v;
}
static i64 falling(int n, int t) {
    i64 v = 1;
    for (int j = 0; j < t; ++j) v *= n-j;
    return v;
}
static i64 pow3(int t) {
    i64 v = 1;
    for (int j = 0; j < t; ++j) v *= 3;
    return v;
}
static i64 expected_extensions(int n, int t) {
    assert(1 <= t && t <= n-2);
    int s = n-t+1;
    assert(factorial(2*s) % (s*s) == 0);
    return pow3(t-1) * (factorial(2*s)/(s*s));
}
static i64 expected_tail(int n, int k) {
    if (k == 2) return factorial(2*n);
    if (k == n+1) return 0;
    assert(3 <= k && k <= n);
    int t = k-2;
    return falling(n,t) * expected_extensions(n,t);
}
static int greedy_crown(int n, const std::vector<int>& order) {
    int color[20] = {};
    int max_color=0;
    for (int v: order) {
        unsigned seen=0;
        for (int u=0; u<2*n; ++u)
            if (color[u] != 0 && u/n != v/n && u%n != v%n)
                seen |= (1u << (color[u]-1));
        int c=1;
        while ((seen>>(c-1))&1u) ++c;
        color[v]=c;
        if (c>max_color) max_color=c;
    }
    return max_color;
}
static i64 count_extensions_independently(int n, int t) {
    // Explicitly count topological orders of the poset P_{n,t}.
    int size=2*n;
    std::vector<int> prerequisites(size,0);
    for (int j=0;j<n;++j)
        for (int i=0;i<std::min(t,j);++i) {
            prerequisites[j] |= (1 << (n+i));
            prerequisites[n+j] |= (1 << i);
        }
    int states=(1<<size);
    std::vector<i64> ways(states,0);
    ways[0]=1;
    for (int mask=0; mask<states; ++mask) {
        if (!ways[mask]) continue;
        for (int v=0;v<size;++v)
            if (!(mask&(1<<v)) &&
                (prerequisites[v]&mask)==prerequisites[v])
                ways[mask|(1<<v)] += ways[mask];
    }
    return ways.back();
}
int main() {
    i64 brute_orders=0;
    for (int n=2;n<=5;++n) {
        std::vector<int> ord(2*n);
        std::iota(ord.begin(),ord.end(),0);
        std::vector<i64> histogram(n+1,0);
        do {
            int k=greedy_crown(n,ord);
            assert(k>=2 && k<=n);
            histogram[k]++;
        } while(std::next_permutation(ord.begin(),ord.end()));
        i64 summed=0;
        for (int k=2;k<=n;++k) {
            i64 predicted=expected_tail(n,k)-expected_tail(n,k+1);
            if (histogram[k]!=predicted) {
                std::cerr << "FAIL exhaustive n=" << n << " k=" << k << " actual="
                          << histogram[k] << " predicted=" << predicted << "\n";
                return 1;
            }
            summed+=histogram[k];
        }
        assert(summed==factorial(2*n));
        brute_orders+=summed;
    }
    int poset_cases=0;
    for (int n=3;n<=9;++n) {
        for (int t=1;t<=n-2;++t) {
            i64 actual=count_extensions_independently(n,t);
            i64 predicted=expected_extensions(n,t);
            if (actual!=predicted) {
                std::cerr << "FAIL poset n=" << n << " t=" << t << " actual="
                          << actual << " predicted=" << predicted << "\n";
                return 1;
            }
            ++poset_cases;
        }
    }
    std::cout << "VERIFY_OK exhaustive_crown_orders=" << brute_orders
              << " poset_cases=" << poset_cases
              << " maximal_order_count_n5=" << expected_tail(5,5) << "\n";
}
