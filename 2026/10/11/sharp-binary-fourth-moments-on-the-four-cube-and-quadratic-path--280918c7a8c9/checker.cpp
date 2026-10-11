// Exact finite checks for binary hypercube Fourier fourth moments.
// Build: g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <climits>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

static int tcode(int x, int y, int d) {
    int t=0, power=1;
    for(int i=0;i<d;i++) {
        t += (((x>>i)&1)+((y>>i)&1))*power;
        power*=3;
    }
    return t;
}
static int direct4(uint32_t mask) {
    int conv[81] = {};
    for(int x=0;x<16;x++) for(int y=0;y<16;y++) {
        int ax = ((mask>>x)&1) ? -1 : 1;
        int ay = ((mask>>y)&1) ? -1 : 1;
        conv[tcode(x,y,4)] += ax*ay;
    }
    int value=0;
    for(int s : conv) value += s*s;
    return value;
}
static uint32_t phase_mask(int n, const vector<pair<int,int>>& edges) {
    uint32_t mask=0;
    assert(n<=4);
    for(int x=0;x<(1<<n);x++) {
        int parity=0;
        for(auto [u,v]:edges) parity ^= ((x>>u)&1)*((x>>v)&1);
        if(parity) mask |= (uint32_t(1)<<x);
    }
    return mask;
}
static set<uint32_t> path_signs4() {
    set<uint32_t> signs;
    array<int,4> p={0,1,2,3};
    do {
        vector<pair<int,int>> edges;
        for(int j=0;j<3;j++) edges.emplace_back(p[j],p[j+1]);
        signs.insert(phase_mask(4,edges));
    } while(next_permutation(p.begin(),p.end()));
    return signs;
}
static void unrestricted_binary_four_cube() {
    // Every signed coefficient set is uniquely reducible under global sign
    // and coordinate-sign modulations to 0 and the four unit vectors positive.
    vector<int> free_indices;
    for(int x=0;x<16;x++)
        if(x!=0 && x!=1 && x!=2 && x!=4 && x!=8) free_indices.push_back(x);
    assert(free_indices.size()==11);
    set<uint32_t> optimizers;
    int minimum=1000000;
    for(int b=0;b<(1<<11);b++) {
        uint32_t mask=0;
        for(int j=0;j<11;j++) if((b>>j)&1) mask|=uint32_t(1)<<free_indices[j];
        int m=direct4(mask);
        if(m<minimum) {minimum=m; optimizers.clear();}
        if(m==minimum) optimizers.insert(mask);
    }
    assert(minimum==336);
    assert(optimizers.size()==12);
    assert(optimizers==path_signs4());
    // The gauge action is free, with 2^(4+1) elements.
    cout << "ALL_BINARY_DIM4 minimum="<<minimum
         <<" normalized_extremizers="<<optimizers.size()
         <<" total_extremizers="<<optimizers.size()*32<<"\n";
}
static uint64_t weighted_eulerian(int n, const array<unsigned,8>& adj) {
    uint64_t total=0;
    for(unsigned S=0; S<(1u<<n);S++) {
        bool all_even=true;
        unsigned remaining=S;
        while(remaining) {
            unsigned v=__builtin_ctz(remaining);remaining &=remaining-1;
            if(__builtin_parity(adj[v] & S)) {all_even=false;break;}
        }
        if(all_even) total+=1ULL<<__builtin_popcount(S);
    }
    return total;
}
static uint64_t formula_path(int n) {
    uint64_t numerator=(1ULL<<(n+2)) + (n%2 ? 1 : -1);
    return numerator/3;
}
static set<unsigned> path_graphs(int n, const vector<pair<int,int>>& edge_ids) {
    set<unsigned> out;
    vector<int> p(n);
    for(int i=0;i<n;i++) p[i]=i;
    do {
        unsigned mask=0;
        for(int k=0;k<n-1;k++){
            int u=min(p[k],p[k+1]),v=max(p[k],p[k+1]);
            for(int e=0;e<(int)edge_ids.size();e++)
                if(edge_ids[e].first==u && edge_ids[e].second==v)
                    {mask|=1u<<e;break;}
        }
        out.insert(mask);
    } while(next_permutation(p.begin(),p.end()));
    return out;
}
static void quadratic_census(int n) {
    vector<pair<int,int>> ed;
    for(int u=0;u<n;u++)for(int v=u+1;v<n;v++) ed.emplace_back(u,v);
    assert(ed.size()<=21);
    array<unsigned,8> adj={};
    uint64_t minval=ULLONG_MAX;
    set<unsigned> minimizers;
    uint32_t total_graphs=1u<<ed.size();
    // Graph mask at iteration b is b XOR (b >> 1); flip ctz(b).
    for(uint32_t b=0;b<total_graphs;b++) {
        if(b) {
            int e=__builtin_ctz(b),u=ed[e].first,v=ed[e].second;
            adj[u]^=1u<<v;adj[v]^=1u<<u;
        }
        uint64_t f=weighted_eulerian(n,adj);
        unsigned gray=b^(b>>1);
        if(f<minval){minval=f;minimizers.clear();}
        if(f==minval)minimizers.insert(gray);
    }
    auto paths=path_graphs(n,ed);
    assert(minval==formula_path(n));
    assert(minimizers==paths);
    // Each labeled Hamiltonian path is counted twice by reversal.
    size_t factorial=1;for(int k=2;k<=n;k++)factorial*=k;
    assert(paths.size()==factorial/2);
    cout << "QUADRATIC_DIM"<<n<<" graphs="<<total_graphs
         <<" minimum="<<(minval<<n)<<" path_minimizers="<<minimizers.size()<<"\n";
}
int main(){
    unrestricted_binary_four_cube();
    for(int n=2;n<=7;n++)quadratic_census(n);
    cout << "CHECK_PASS\n";
}
