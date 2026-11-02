// Second bit-mask enumeration for binary synchronous open-neighborhood NOR.
// Build: c++ -O2 -std=c++17 check_independent.cpp -o check_independent
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

uint32_t step(uint32_t state, const vector<uint32_t>& nb) {
    uint32_t out = 0;
    for (size_t i=0; i<nb.size(); ++i)
        if ((state & nb[i]) == 0) out |= uint32_t(1) << i;
    return out;
}

void verify(unsigned p, unsigned q, unsigned k, uint64_t& states) {
    const unsigned n=p+q, N=1u<<n;
    vector<uint32_t> nb(n,0);
    for (unsigned i=0;i<p;i++) for (unsigned j=0;j<q;j++) {
        if (i==j && i<k) continue;
        nb[i] |= 1u<<(p+j);
        nb[p+j] |= 1u<<i;
    }
    vector<uint32_t> nxt(N);
    for (unsigned s=0;s<N;s++) nxt[s]=step(s,nb);
    map<pair<unsigned,unsigned>, unsigned> basin;
    unsigned periodic=0;
    for (unsigned s=0;s<N;s++) {
        unsigned a=nxt[s],b=nxt[a];
        assert(nxt[b]==a);
        if (s==a || s==b) periodic++;
        if (b<a) swap(a,b);
        basin[{a,b}]++;
    }
    assert(periodic == (k+2)*(k+2));
    assert(basin.size() == (k+2)*(k+3)/2);
    map<unsigned,unsigned> actual, expected;
    unsigned fixed = 0, two = 0;
    for (auto &entry: basin) {
        actual[entry.second]++;
        if (entry.first.first==entry.first.second) fixed++;
        else two++;
    }
    const unsigned hp=(1u<<p)-1-k, hq=(1u<<q)-1-k;
    expected[hp]++;
    expected[hq]++;
    expected[1]+=k;
    expected[hp*hq+1]++;
    expected[hp+1]+=k;
    expected[hq+1]+=k;
    expected[2]+=k*(k-1)/2;
    for (auto it=expected.begin();it!=expected.end();) {
        if (!it->second) it=expected.erase(it); else ++it;
    }
    assert(actual==expected);
    assert(fixed==k+2);
    assert(two==(k+1)*(k+2)/2);
    unsigned giant=0;
    uint32_t all = N-1;
    pair<unsigned,unsigned> universal={0,all};
    if (p+q==0) assert(false);
    giant=basin.at(universal);
    assert(giant==hp*hq+1);
    states+=N;
}

int main(){
    uint64_t configurations=0;
    unsigned cases=0;
    for (unsigned p=2;p<=8;p++) for (unsigned q=2;q<=8;q++) {
        if (p+q>14) continue;
        for (unsigned k=0;k<=min(p,q);k++){
            verify(p,q,k,configurations);cases++;
        }
    }
    cout << "PASS bit-mask enumeration: " << cases << " graph parameters and "
         << configurations << " complete state trajectories\n";
    cout << "All periodic/one-step, fixed/two-cycle, individual basin profiles and universal basin checks passed.\n";
}
