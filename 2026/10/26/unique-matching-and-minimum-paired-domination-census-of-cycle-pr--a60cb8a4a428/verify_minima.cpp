#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using U = std::uint64_t;
int n, N, K;
U adj[40], full;
std::uint64_t count_sets;

bool perfect_matching(U s) {
    if (!s) return true;
    int v = __builtin_ctzll(s);
    U rest = s ^ (U(1) << v);
    U opts = rest & adj[v];
    while (opts) {
        U b = opts & -opts;
        opts ^= b;
        if (perfect_matching(rest ^ b)) return true;
    }
    return false;
}
void enumerate(int next, int need, U selected, U covered) {
    if (!need) {
        if (covered == full && perfect_matching(selected)) ++count_sets;
        return;
    }
    for (int i=next; i<=N-need; ++i)
        enumerate(i+1,need-1,selected|(U(1)<<i),covered|adj[i]|(U(1)<<i));
}
int main() {
    for (int test_n : {5,8,11,14,17}) {
        n = test_n;
        N=2*n; K=2*((n+1)/3); full=(U(1)<<N)-1;
        for(int c=0;c<n;++c) for(int row=0;row<2;++row) {
            int v=2*c+row;
            adj[v]=(U(1)<<(2*((c+n-1)%n)+row))
                   |(U(1)<<(2*((c+1)%n)+row))
                   |(U(1)<<(2*c+(1-row)));
        }
        count_sets=0;
        enumerate(0,K,0,0);
        const std::uint64_t expected = std::uint64_t(n)*(2*n+5)/3;
        if(count_sets!=expected){std::cerr<<"FAIL "<<n<<" "<<count_sets<<" "<<expected<<"\n";return 1;}
        std::cout<<"n="<<n<<" cardinality="<<K<<" count="<<count_sets<<"\n";
    }
    std::cout<<"VERIFY_OK\n";
}
