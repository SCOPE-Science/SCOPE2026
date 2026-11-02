// Exact strict-ranking census for two agents, seven goods, and one market order.
// Compile: g++ -O2 -std=c++17 independent_full.cpp -o independent_full
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
using namespace std;

static bool prefix_sd_ef1(const array<int,7>& ranking, int own) {
    int own_count = 0, other_count = 0;
    for(int item: ranking) {
        if(own & (1<<item)) ++own_count;
        else ++other_count;
        if (own_count < other_count - 1) return false;
    }
    return true;
}
int main() {
    array<int,7> ranking = {0,1,2,3,4,5,6};
    array<int,16> market_alloc{};
    for(int code=0;code<16;code++) {
        int mask = ((code >> 3) & 1) << 6;
        for (int p=0;p<3;p++) mask |= 1 << (2*p + ((code >> p)&1));
        market_alloc[code] = mask;
        assert(prefix_sd_ef1(ranking,mask));
        assert(prefix_sd_ef1(ranking,mask^127));
    }
    array<uint16_t,5040> agent1{},agent2{};
    int ix=0;
    do {
        for(int j=0;j<16;j++) {
            const int mask=market_alloc[j];
            if(prefix_sd_ef1(ranking,mask)) agent1[ix] |= uint16_t(1u<<j);
            if(prefix_sd_ef1(ranking,mask^127)) agent2[ix] |= uint16_t(1u<<j);
        }
        ++ix;
    }while(next_permutation(ranking.begin(),ranking.end()));
    assert(ix==5040);
    array<uint64_t,17> histogram{};
    for(int a=0;a<5040;a++) for(int b=0;b<5040;b++) {
        int compatible = __builtin_popcount(unsigned(agent1[a]&agent2[b]));
        ++histogram[compatible];
    }
    uint64_t total=0, incidence=0;
    for(int z=0;z<=16;z++) {
        total+=histogram[z];
        incidence+=uint64_t(z)*histogram[z];
    }
    assert(total==uint64_t(5040)*5040);
    assert(histogram[0]==6144);
    assert(incidence==130056192);
    printf("number of strict-ranking pairs: %llu\n",(unsigned long long)total);
    printf("no compatible allocation: %llu\n",(unsigned long long)histogram[0]);
    printf("sum of compatible allocation counts: %llu\n",(unsigned long long)incidence);
    for(int z=0;z<=16;z++)if(histogram[z])
        printf("compatible=%d pairs=%llu\n",z,(unsigned long long)histogram[z]);
    return 0;
}
