// Independent exact census of shortest crucial Abelian-square-free words.
// Compile: g++ -O2 -std=c++17 independent_census.cpp -o independent_census
// Run: ./independent_census
#include <array>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cassert>
using namespace std;
constexpr int Q = 5, N = 13;
array<int,N+1> w{};
long long nodes=0, full=0, accepted=0;
map<vector<int>,int> signatures;
vector<string> representatives;

bool ends_square(int len) {
    for (int h=1;2*h<=len;++h) {
        array<int,Q> delta{};
        for (int i=len-2*h;i<len-h;++i) ++delta[w[i]];
        for (int i=len-h;i<len;++i) --delta[w[i]];
        bool equal=true;
        for (int c:delta) if (c != 0) equal=false;
        if (equal) return true;
    }
    return false;
}

void dfs(int len, int largest) {
    ++nodes;
    if (len==N) {
        if (largest!=Q-1) return;
        ++full;
        vector<int> witness;
        for (int x=0;x<Q;++x) {
            w[N]=x;
            vector<int> found;
            for (int h=1;2*h<=N+1;++h) {
                array<int,Q> delta{};
                for (int i=N+1-2*h;i<N+1-h;++i) ++delta[w[i]];
                for (int i=N+1-h;i<N+1;++i) --delta[w[i]];
                if (all_of(delta.begin(),delta.end(),[](int z){return z==0;}))
                    found.push_back(h);
            }
            if (found.size()!=1) return;
            witness.push_back(found[0]);
        }
        sort(witness.begin(), witness.end());
        ++signatures[witness];
        ++accepted;
        string s;
        for (int i=0;i<N;++i) s.push_back(char('0'+w[i]));
        representatives.push_back(s);
        return;
    }
    for (int x=0;x<=min(Q-1,largest+1);++x) {
        w[len]=x;
        if (!ends_square(len+1)) dfs(len+1,max(largest,x));
    }
}

int main() {
    dfs(1,0);
    const map<vector<int>,int> target = {
        {{1,2,3,5,7},3}, {{1,2,3,6,7},8},
        {{1,2,5,6,7},1}, {{1,4,5,6,7},2}
    };
    assert(nodes==297588 && full==205424 && accepted==14);
    assert(signatures==target);
    for (const auto &s:representatives) cout<<s<<'\n';
    cerr << "PASS nodes=" << nodes << " full=" << full << " orbits=" << accepted << "\n";
}
