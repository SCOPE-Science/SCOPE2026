// Original-graph exhaustive check: all set partitions for q=1,2,3.
// Compile: g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static long long checked;
static int best;
static vector<uint16_t> blocks;
static vector<unsigned char> gd;
static int q, N;

static bool direct_global(uint16_t mask) {
    for (int v=0;v<N;v++) {
        if (mask & (1u << v)) continue;
        bool in_g=false, in_comp=false;
        for (int w=0;w<N;w++) if (mask & (1u << w)) {
            if (v/q != w/q) in_g=true;
            else in_comp=true;
        }
        if (!(in_g && in_comp)) return false;
    }
    return true;
}
static bool good_partition() {
    for (size_t i=0;i<blocks.size();i++) {
        if (gd[blocks[i]]) return false;
        bool partner=false;
        for (size_t j=0;j<blocks.size();j++) if (i!=j) {
            if (gd[blocks[i] | blocks[j]]) {partner=true;break;}
        }
        if (!partner) return false;
    }
    return true;
}
static void visit(int v) {
    if (v==N) {
        checked++;
        if ((int)blocks.size()>best && good_partition()) best=blocks.size();
        return;
    }
    uint16_t bit = (uint16_t)(1u<<v);
    for (size_t i=0;i<blocks.size();i++) {
        blocks[i] |= bit;
        visit(v+1);
        blocks[i] ^= bit;
    }
    blocks.push_back(bit);
    visit(v+1);
    blocks.pop_back();
}
static int predicted(int x) {return max(2*x,max(3*x-3,4*x-8));}
int main() {
    for (q=1;q<=3;q++) {
        N=4*q;
        gd.assign(1u<<N,0);
        for (int mask=0;mask<(1<<N);mask++) gd[mask]=direct_global((uint16_t)mask);
        blocks={1}; checked=0; best=0;
        visit(1);
        assert(best==predicted(q));
        cout << "EXHAUSTIVE_ORIGINAL_GRAPH_PARTITIONS_OK " << q << ' ' << checked << ' ' << best << '\n';
    }
    cout << "EXHAUSTIVE_VERIFY_OK\n";
}
