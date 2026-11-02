// Self-contained exact-integer tests for the high-first, first-low-anchor algorithm.
// Compile: g++ -std=c++17 -O3 -Wall -Wextra verify_bivalued_online.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>
using namespace std;

// Returns false on either a prefix EF1 failure or a failure of the anchor lemma.
static bool check(int n, const vector<int>& low, const vector<int>& high,
                  const vector<vector<unsigned char>>& type, uint64_t& prefixes) {
    const int m = int(type[0].size());
    vector<vector<int>> alloc(n);
    int first_low = -1;
    auto val = [&](int i,int t)->int { return type[i][t] ? high[i] : low[i]; };
    for (int t = 0; t < m; ++t) {
        int chosen = -1;
        if (t < n) {
            for (int i = 0; i < n; ++i)
                if (alloc[i].empty() && type[i][t]) {chosen=i; break;}
            if (chosen < 0) for (int i = 0; i < n; ++i)
                if (alloc[i].empty()) {chosen=i; break;}
            if (chosen < 0) return false;
            if (!type[chosen][t] && first_low < 0) first_low = chosen;
        } else {
            chosen = first_low < 0 ? 0 : first_low;
        }
        alloc[chosen].push_back(t);
        for (int i = 0; i < n; ++i) {
            int own = 0;
            for (int g : alloc[i]) own += val(i,g);
            for (int j = 0; j < n; ++j) {
                int other = 0, largest = 0;
                for (int g : alloc[j]) {
                    other += val(i,g);
                    largest = max(largest,val(i,g));
                }
                if (own < other-largest) return false;
            }
        }
        ++prefixes;
    }
    if (m == n+1 && first_low >= 0) {
        int anchor_good=alloc[first_low][0];
        for (int i = 0; i < n; ++i)
            if (i != first_low && val(i,alloc[i][0]) < val(i,anchor_good))
                return false;
    }
    return true;
}

int main() {
    uint64_t cases=0, prefixes=0;
    for (int n=2; n<=4; ++n) {
        const int m=n+1, bits=n*m;
        for (int palette=0; palette<3; ++palette) {
            vector<int> low(n),high(n);
            for (int i=0; i<n; ++i) {
                if (palette==0) {low[i]=1;high[i]=2;}
                else if (palette==1) {low[i]=i+1;high[i]=100000+i;}
                else {low[i]=10*(i+1);high[i]=20*(i+1)+1;}
            }
            for (uint64_t mask=0; mask<(1ULL<<bits); ++mask) {
                vector<vector<unsigned char>> type(n,vector<unsigned char>(m));
                for (int i=0;i<n;++i) for (int t=0;t<m;++t)
                    type[i][t] = (mask>>(i*m+t))&1ULL;
                if (!check(n,low,high,type,prefixes)) {
                    cerr<<"FAIL n="<<n<<" palette="<<palette<<" mask="<<mask<<'\n';return 1;
                }
                ++cases;
            }
        }
    }
    mt19937_64 rng(0x5d729ab94316ULL);
    for (int n=5;n<=9;++n) {
        int m=n+1;
        for (int rep=0;rep<150000;++rep) {
            vector<int> low(n),high(n);
            vector<vector<unsigned char>> type(n,vector<unsigned char>(m));
            for(int i=0;i<n;++i) {
                low[i]=1+int(rng()%100);
                high[i]=low[i]+1+int(rng()%100000);
                for(int t=0;t<m;++t) type[i][t]=rng()&1ULL;
            }
            if (!check(n,low,high,type,prefixes)) {
                cerr<<"FAIL n="<<n<<" rep="<<rep<<'\n';return 1;
            }
            ++cases;
        }
    }
    cout<<"VERIFY_OK cases="<<cases<<" prefix_checks="<<prefixes<<'\n';
    return 0;
}
