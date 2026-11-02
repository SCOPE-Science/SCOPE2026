// Exact all-support census for balanced tournament orientation traces.
// For an edge subset E, score-prescribed orientation extendability
// gives shattering iff every vertex cut contains at most half its possible edges.
// This implementation checks all 2^21 subsets independently of the tree certificate.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
int main() {
    constexpr int n=7;
    vector<pair<int,int>> edges;
    for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)edges.emplace_back(u,v);
    assert(edges.size()==21);
    vector<pair<uint32_t,int>> cuts;
    for(int S=1;S<(1<<(n-1));S++) {
        int s=__builtin_popcount(unsigned(S));
        uint32_t cutmask=0;
        for(int e=0;e<21;e++) {
            auto [u,v]=edges[e];
            if(((S>>u)&1)!=((S>>v)&1))cutmask|=uint32_t(1)<<e;
        }
        cuts.emplace_back(cutmask,s*(n-s)/2);
    }
    array<uint64_t,22> counts{};
    uint32_t max_count=0;
    for(uint32_t E=0;E<(uint32_t(1)<<21);E++) {
        bool valid=true;
        for(auto [mask,limit]:cuts) {
            if(__builtin_popcount(E&mask)>limit){valid=false;break;}
        }
        if(!valid)continue;
        int k=__builtin_popcount(E);
        counts[k]++;
        if(k==9) {
            int degree[n]={};
            for(int e=0;e<21;e++)if((E>>e)&1){
                auto [u,v]=edges[e];degree[u]++;degree[v]++;
            }
            int deg3=0,deg2=0;
            for(int d:degree){if(d==3)deg3++;else if(d==2)deg2++;else assert(false);}
            assert(deg3==4 && deg2==3);
            max_count++;
        }
    }
    const array<uint64_t,22> expected={
        1,21,210,1330,5880,18732,40502,32490,315,35,
        0,0,0,0,0,0,0,0,0,0,0,0
    };
    assert(counts==expected);
    assert(max_count==35);
    cout<<"EXHAUSTIVE_CUT_CENSUS_PASS supports=2097152 maximal_size=9 extremizers=35\n";
    cout<<"SHATTER_POLYNOMIAL:";
    for(int i=0;i<=9;i++)cout<<" "<<i<<":"<<counts[i];
    cout<<"\n";
}
