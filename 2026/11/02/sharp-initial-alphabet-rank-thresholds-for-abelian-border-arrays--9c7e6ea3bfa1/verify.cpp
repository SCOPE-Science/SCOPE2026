#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>

using Word = std::vector<int>;

// Compare the Parikh vectors of each proper prefix and suffix directly.
Word borders_direct(const Word& w) {
    const int n = static_cast<int>(w.size());
    Word a(n, 0);
    for (int t = 2; t <= n; ++t) {
        for (int len = 1; len < t; ++len) {
            int delta[12] = {};
            for (int j = 0; j < len; ++j) {
                ++delta[w[j]];
                --delta[w[t - len + j]];
            }
            bool equal = true;
            for (int c = 0; c < n; ++c) {
                if (delta[c] != 0) { equal = false; break; }
            }
            if (equal) a[t - 1] = len;
        }
    }
    return a;
}

// Independent streaming computation of the same border array.
Word borders_streaming(const Word& w) {
    const int n = static_cast<int>(w.size());
    Word a(n, 0);
    for (int t = 2; t <= n; ++t) {
        int left[12] = {}, right[12] = {};
        for (int len = 1; len < t; ++len) {
            ++left[w[len - 1]];
            ++right[w[t - len]];
            bool equal = true;
            for (int c = 0; c < n; ++c) {
                if (left[c] != right[c]) { equal = false; break; }
            }
            if (equal) a[t - 1] = len;
        }
    }
    return a;
}

// Each restricted-growth word corresponds to exactly one set partition.
// A word 0,w_1,... satisfies 0 <= w_i <= 1+max(w_0,...,w_{i-1}).
class Census {
public:
    explicit Census(int n) : n_(n), w_(n, 0) {}
    void visit(int i, int maximum) {
        if (i == n_) {
            ++visited_;
            Word profile = borders_direct(w_);
            if (profile != borders_streaming(w_)) {
                std::cerr << "Independent border routines disagree\n";
                std::exit(2);
            }
            int rank = maximum + 1;
            auto it = minimum_rank_.find(profile);
            if (it == minimum_rank_.end() || rank < it->second.first)
                minimum_rank_[profile] = {rank, w_};
            return;
        }
        for (int c = 0; c <= maximum + 1; ++c) {
            w_[i] = c;
            visit(i + 1, std::max(maximum, c));
        }
    }
    void check() {
        static const long long bell[12] =
            {0,1,2,5,15,52,203,877,4140,21147,115975,678570};
        static const int expected[12][5] = {
            {0,0,0,0,0},
            {1,0,0,0,0}, {1,1,0,0,0}, {1,3,0,0,0},
            {1,7,1,0,0}, {1,15,4,0,0}, {1,31,17,0,0},
            {1,63,55,0,0}, {1,127,180,3,0},
            {1,255,539,23,0}, {1,511,1658,134,0},
            {1,1023,4880,608,4}
        };
        if (visited_ != bell[n_]) {
            std::cerr << "Partition count mismatch\n";
            std::exit(3);
        }
        std::array<int, 5> by_rank{};
        for (const auto& [profile, data] : minimum_rank_) {
            if (data.first > 5 || data.first < 1) {
                std::cerr << "Rank outside expected range\n";
                std::exit(4);
            }
            ++by_rank[data.first - 1];
            if (borders_direct(data.second) != profile) {
                std::cerr << "Witness does not realize profile\n";
                std::exit(5);
            }
        }
        for (int k = 0; k < 5; ++k)
            if (by_rank[k] != expected[n_][k]) {
                std::cerr << "Rank census mismatch\n";
                std::exit(6);
            }
        std::cout << n_ << ',' << visited_;
        for (int k = 0; k < 5; ++k) std::cout << ',' << by_rank[k];
        std::cout << '\n';
        if (n_ == 4 || n_ == 8 || n_ == 11) {
            int maximum_rank = (n_ == 4 ? 3 : n_ == 8 ? 4 : 5);
            std::cout << "RANK " << maximum_rank << " MINIMUM WITNESSES\n";
            for (const auto& [profile, data] : minimum_rank_) {
                if (data.first == maximum_rank) {
                    for (int b : profile) std::cout << b << ' ';
                    std::cout << ": ";
                    for (int b : data.second) std::cout << b;
                    std::cout << '\n';
                }
            }
        }
    }
private:
    int n_;
    Word w_;
    long long visited_ = 0;
    std::map<Word, std::pair<int, Word>> minimum_rank_;
};

int main() {
    for (int n = 1; n <= 11; ++n) {
        Census census(n);
        census.visit(1, 0);
        census.check();
    }
    std::cout << "VERIFY_OK\n";
    return 0;
}
