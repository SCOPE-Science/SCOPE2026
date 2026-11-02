// Exhaustive independent verifier for binary order-five cyclic palindromic lengths.
// Compile: c++ -O2 -std=c++17 verify_circular_pal_lengths.cpp -o verify_pal
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
using namespace std;

static const map<int,int> expected_roots = {{4,384},{5,3554},{6,18266},
    {7,29118},{8,12138},{9,2030},{10,46}};
static const map<int,int> expected_best = {{4,48},{5,534},{6,942},
    {7,416},{8,106},{9,2}};
static const map<pair<int,int>,int> expected_joint = {
    {{4,7},48}, {{5,7},120},{{5,8},350},{{5,9},64},
    {{6,7},118},{{6,8},742},{{6,9},74},{{6,10},8},
    {{7,8},254},{{7,9},154},{{7,10},8},
    {{8,9},92},{{8,10},14},{{9,10},2}
};
static const set<string> expected_hard = {
    "00000110100111110110001010111001",
    "00000100111010100011011111001011"
};

int palindrome_length(const string& w) {
    const int n = int(w.size());
    array<array<char,32>,32> pal{};
    for (int i=n-1; i>=0; --i)
        for (int j=i; j<n; ++j)
            pal[i][j] = (w[i]==w[j] && (j-i<2 || pal[i+1][j-1]));
    array<int,33> dp{};
    for (int j=1; j<=n; ++j) {
        dp[j]=33;
        for (int i=0; i<j; ++i)
            if (pal[i][j-1]) dp[j]=min(dp[j], dp[i]+1);
    }
    return dp[n];
}

struct Statistics {
    map<int,int> roots, best;
    map<pair<int,int>,int> joint;
    set<string> hard, cycles;
    void record(const string& w) {
        assert(w.size()==32 && w.substr(0,5)=="00000");
        assert(cycles.insert(w).second);
        set<string> factors;
        for (int r=0;r<32;++r) factors.insert((w+w).substr(r,5));
        assert(factors.size()==32);
        int lo=33,hi=0;
        for (int r=0;r<32;++r) {
            int v=palindrome_length(w.substr(r)+w.substr(0,r));
            roots[v]++;
            lo=min(lo,v);hi=max(hi,v);
        }
        best[lo]++;
        joint[{lo,hi}]++;
        if(lo==9) hard.insert(w);
    }
};

void euler(int vertex, uint32_t used, string& w, Statistics& stats) {
    if(w.size()==32) {
        if(vertex==0) stats.record(w);
        return;
    }
    for(int bit=0;bit<=1;++bit) {
        const int edge=(vertex<<1)|bit;
        if(!(used&(uint32_t(1)<<edge))) {
            w.push_back(char('0'+(vertex>>3)));
            euler(edge&15,used|(uint32_t(1)<<edge),w,stats);
            w.pop_back();
        }
    }
}

int main() {
    Statistics stats;
    string word="0";
    euler(0,1,word,stats);
    assert(stats.cycles.size()==2048);
    assert(stats.roots==expected_roots);
    assert(stats.best==expected_best);
    assert(stats.joint==expected_joint);
    assert(stats.hard==expected_hard);
    const auto canonical = [](const string& w) {
        string best = w;
        for(int k=1;k<32;++k) best=min(best,w.substr(k)+w.substr(0,k));
        return best;
    };
    string a=*stats.hard.begin();
    string b=*stats.hard.rbegin();
    string reversed=a;
    reverse(reversed.begin(),reversed.end());
    assert(canonical(reversed)==b);
    string complemented=a;
    for(char& c:complemented)c=(c=='0'?'1':'0');
    assert(canonical(complemented)==b);
    cout << "VERIFY_OK\n";
    cout << "cycles=2048 roots=65536 joint_profiles=" << stats.joint.size() << "\n";
}
