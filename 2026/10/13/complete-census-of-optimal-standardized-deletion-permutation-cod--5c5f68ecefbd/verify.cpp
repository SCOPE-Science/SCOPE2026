// Exact independent computation for the finite standardized-deletion code.
// Requires only a C++17 compiler: g++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

using P5 = array<int, 5>;
using P4 = array<int, 4>;
static vector<P5> words;
static vector<uint32_t> shadows;
static uint64_t visited[10], tally;

static P4 delete_and_rank(const P5& p, int deleted) {
    P4 result{};
    int k = 0;
    for (int j = 0; j < 5; ++j) {
        if (j == deleted) continue;
        int rank = 0;
        for (int i = 0; i < 5; ++i)
            if (i != deleted && p[i] < p[j]) ++rank;
        result[k++] = rank;
    }
    return result;
}

static void search(const vector<int>& available, int depth, int target) {
    ++visited[depth];
    if (depth == target) {++tally; return;}
    const int needed = target - depth;
    if (int(available.size()) < needed) return;
    for (int z = 0; z <= int(available.size()) - needed; ++z) {
        const int x = available[z];
        vector<int> remaining;
        remaining.reserve(available.size() - z);
        for (int j = z + 1; j < int(available.size()); ++j)
            if ((shadows[x] & shadows[available[j]]) == 0u)
                remaining.push_back(available[j]);
        if (int(remaining.size()) + 1 < needed) continue;
        search(remaining, depth + 1, target);
    }
}

int main() {
    P4 small = {0,1,2,3};
    map<P4, int> rank4;
    int ix = 0;
    do {rank4[small] = ix++;}
    while(next_permutation(small.begin(), small.end()));
    assert(ix == 24);
    P5 p = {0,1,2,3,4};
    do {
        words.push_back(p);
        uint32_t mask = 0;
        for (int j = 0; j < 5; ++j)
            mask |= (uint32_t(1) << rank4.at(delete_and_rank(p, j)));
        shadows.push_back(mask);
    } while(next_permutation(p.begin(),p.end()));
    assert(words.size() == 120);
    int total = 0;
    for (uint32_t x : shadows) total += __builtin_popcount(x);
    assert(total == 408);
    vector<int> candidates(120);
    iota(candidates.begin(), candidates.end(), 0);
    tally = 0;
    search(candidates, 0, 8);
    assert(tally == 1568);
    tally = 0;
    search(candidates, 0, 9);
    assert(tally == 0);
    assert(visited[9] == 0);
    cout << "INDEPENDENT_VERIFY_OK n=5 maximum=8 labeled_optimal_codes=1568 "
         << "nine_word_codes=0 five_letter_permutations=120 "
         << "four_letter_outputs=24\n";
}
