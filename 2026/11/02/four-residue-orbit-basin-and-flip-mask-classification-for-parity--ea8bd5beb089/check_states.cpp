// Independent exhaustive update of binary neighbor parity on KG(n,2).
#include <cstdio>
#include <vector>
#include <utility>
#include <cstdint>
using U = uint64_t;
using Pair = std::pair<int,int>;
static U update(U x, const std::vector<U>& masks) {
    U y=0;
    for (size_t i=0;i<masks.size();++i) {
        if (__builtin_parityll(x & masks[i])) y |= U(1)<<i;
    }
    return y;
}
int main() {
    for (int n=5;n<=7;++n) {
        std::vector<Pair> edges;
        for (int a=0;a<n;++a)for(int b=a+1;b<n;++b)edges.emplace_back(a,b);
        int N=edges.size();
        std::vector<U> masks(N,0);
        for (int i=0;i<N;++i) for (int j=0;j<N;++j) {
            if (edges[i].first!=edges[j].first && edges[i].first!=edges[j].second &&
                edges[i].second!=edges[j].first && edges[i].second!=edges[j].second)
                masks[i] |= U(1)<<j;
        }
        U fixed=0, periodicTwoStates=0, entryOne=0;
        U count=U(1)<<N;
        for(U x=0;x<count;++x) {
            U y=update(x,masks);
            U z=update(y,masks);
            U w=update(z,masks);
            if(n%4==0) {
                if(z!=x) { std::puts("INCORRECT_A2"); return 1; }
            } else if(n%4==3) {
                if(z!=y) { std::puts("INCORRECT_IDEMPOTENT"); return 1; }
            } else if(w!=y) { std::puts("INCORRECT_A3"); return 1; }
            if(y==x) ++fixed;
            else if(z==x) ++periodicTwoStates;
            else ++entryOne;
        }
        U F=U(1)<<(N-n+(n%2==0));
        U P=U(1)<<(n%4==0 ? N : (n%4==1 ? N-n+1 : n%4==2 ? N-1 : N-n));
        if(fixed!=F || periodicTwoStates!=P-F || entryOne!=count-P) {
            std::puts("INCORRECT_COUNTS"); return 1;
        }
        std::printf("n=%d N=%d total=%llu fixed=%llu primitive_two_states=%llu two_orbits=%llu entry_one=%llu\n",
            n,N,(unsigned long long)count,(unsigned long long)fixed,
            (unsigned long long)periodicTwoStates,(unsigned long long)(periodicTwoStates/2),
            (unsigned long long)entryOne);
    }
    std::puts("STATES_VERIFY_OK");
}
