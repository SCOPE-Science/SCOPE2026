/* Independent full labeled enumeration of four-agent random serial dictatorship.
   Compile: c++ -std=c++17 -O2 verify_full.cpp -o verify_full
   Run: ./verify_full
   No third-party libraries are needed. */
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int main() {
    using Order = array<int, 4>;
    vector<Order> ranks;
    Order p = {0, 1, 2, 3};
    do { ranks.push_back(p); } while (next_permutation(p.begin(), p.end()));
    assert(ranks.size() == 24);
    int code[4][4][4][4] = {};
    for (int i = 0; i < 24; ++i) {
        auto r = ranks[i];
        code[r[0]][r[1]][r[2]][r[3]] = i;
    }
    map<vector<int>, long long> shape_hist;
    map<int, long long> support_hist;
    for (const auto &a : ranks) for (const auto &b : ranks)
    for (const auto &c : ranks) for (const auto &d : ranks) {
        Order preferences[4] = {a, b, c, d};
        int multiplicities[24] = {};
        for (const Order &priority : ranks) {
            Order assigned = {-1, -1, -1, -1};
            int occupied = 0;
            for (int agent : priority) {
                for (int item : preferences[agent]) {
                    if (!(occupied & (1 << item))) {
                        assigned[agent] = item;
                        occupied |= 1 << item;
                        break;
                    }
                }
            }
            assert(occupied == 15);
            ++multiplicities[code[assigned[0]][assigned[1]][assigned[2]][assigned[3]]];
        }
        vector<int> signature;
        for (int n : multiplicities) if (n) signature.push_back(n);
        sort(signature.begin(), signature.end(), greater<int>());
        assert(accumulate(signature.begin(), signature.end(), 0) == 24);
        ++support_hist[(int)signature.size()];
        ++shape_hist[signature];
    }
    map<int, long long> expected = {
        {1,31104},{2,20736},{3,20736},{4,53856},
        {5,48384},{6,40032},{7,45504},{8,26568},
        {9,12672},{10,15120},{11,6336},{12,5880},
        {14,4032},{16,216},{18,576},{24,24}
    };
    assert(support_hist == expected && shape_hist.size() == 57);
    long long total = 0;
    for (const auto &kv : shape_hist) total += kv.second;
    assert(total == 331776);
    for (const auto &kv : shape_hist) {
        for (size_t j = 0; j < kv.first.size(); ++j) {
            if (j) cout << ';';
            cout << kv.first[j];
        }
        cout << ',' << kv.second << '\n';
    }
    cerr << "VERIFY_OK full_labeled_profiles=" << total
         << " spectra=" << shape_hist.size() << " support_sizes=" << support_hist.size() << '\n';
}
