// Exact subspace enumeration for the binary affine Grassmann code on 2x3 matrices.
// Compile: g++ -O3 -std=c++17 verify_affine_higher.cpp -o verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;

array<uint64_t, 1024> support{};
array<unsigned long long, 11> expected_total{{1ULL,1023ULL,174251ULL,6347715ULL,53743987ULL,109221651ULL,53743987ULL,6347715ULL,174251ULL,1023ULL,1ULL}};
array<unsigned long long, 11> expected_ties{{1ULL,112ULL,448ULL,64ULL,28ULL,1120ULL,24ULL,1456ULL,2016ULL,64ULL,1ULL}};
array<int, 11> expected_min{{0,24,36,42,48,54,56,60,62,63,64}};
int r, best;
unsigned long long checked, tied;
vector<int> pivots, basis, certificate;

void enumerate_free(int pos, const vector<pair<int,int>>& free_entries) {
    if (pos == (int)free_entries.size()) {
        uint64_t union_mask = 0;
        for (int c : basis) union_mask |= support[c];
        int w = __builtin_popcountll(union_mask);
        ++checked;
        if (w < best) {
            best = w; tied = 1; certificate = basis;
        } else if (w == best) {
            ++tied;
        }
        return;
    }
    enumerate_free(pos + 1, free_entries);
    auto [row, col] = free_entries[pos];
    basis[row] ^= 1 << col;
    enumerate_free(pos + 1, free_entries);
    basis[row] ^= 1 << col;
}
void enumerate_pivots(int i, int last) {
    if (i == r) {
        bool pivot[10]{};
        for (int c : pivots) pivot[c] = true;
        basis.clear();
        vector<pair<int,int>> free_entries;
        for (int row = 0; row < r; ++row) {
            basis.push_back(1 << pivots[row]);
            for (int col = pivots[row] + 1; col < 10; ++col) {
                if (!pivot[col]) free_entries.emplace_back(row,col);
            }
        }
        enumerate_free(0, free_entries);
        return;
    }
    for (int p = last+1; p <= 10-(r-i); ++p) {
        pivots.push_back(p);
        enumerate_pivots(i+1,p);
        pivots.pop_back();
    }
}
int evaluate(int a, int x) {
    int value = a & 1;
    for (int k = 0; k < 6; ++k) value ^= ((a >> (1+k)) & 1) & ((x >> k) & 1);
    int t = 7;
    for (int i=0; i<3; ++i) for (int j=i+1; j<3; ++j) {
        int minor = (((x>>i)&1) & ((x>>(3+j))&1)) ^ (((x>>j)&1) & ((x>>(3+i))&1));
        value ^= ((a >> t++) & 1) & minor;
    }
    return value;
}
int main() {
    for (int a=0; a<1024; ++a) {
        for (int x=0; x<64; ++x) if (evaluate(a,x)) support[a] |= 1ULL << x;
    }
    if (set<uint64_t>(support.begin(), support.end()).size() != 1024) return 1;
    for (r=1; r<=10; ++r) {
        best=65; checked=0; tied=0; pivots.clear(); basis.clear(); certificate.clear();
        enumerate_pivots(0,-1);
        if (best != expected_min[r] || tied != expected_ties[r] || checked != expected_total[r]) {
            cerr << "FAIL r=" << r << " best=" << best << " ties=" << tied << " total=" << checked << "\n";
            return 1;
        }
        cout << "r=" << r << " d=" << best << " minimizers=" << tied << " subspaces=" << checked << " witness=";
        for (int c:certificate) cout << c << ',';
        cout << '\n';
    }
    cout << "VERIFY_OK\n";
    return 0;
}
