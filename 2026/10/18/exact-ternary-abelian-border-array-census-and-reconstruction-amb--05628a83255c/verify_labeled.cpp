#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <unordered_map>

constexpr int WIDTH = 16;
using Key = std::uint64_t;
std::array<std::unordered_map<Key, std::uint32_t>, WIDTH + 1> counts;
std::array<std::array<int, 3>, WIDTH + 1> prefix{};

void grow(int m, Key code) {
    counts[m][code] += 1;
    if (m == WIDTH) return;
    for (int symbol = 0; symbol != 3; ++symbol) {
        for (int a = 0; a != 3; ++a)
            prefix[m + 1][a] = prefix[m][a] + (a == symbol);
        int answer = 0;
        for (int size = 1; size < m + 1; ++size) {
            const bool is_border =
                prefix[size][0] == prefix[m + 1][0] - prefix[m + 1 - size][0] &&
                prefix[size][1] == prefix[m + 1][1] - prefix[m + 1 - size][1] &&
                prefix[size][2] == prefix[m + 1][2] - prefix[m + 1 - size][2];
            if (is_border) answer = size;
        }
        grow(m + 1, code | (Key(answer) << (4 * m)));
    }
}

int main(int argc, char** argv) {
    if (argc != 3) { std::cerr << "usage: executable table.csv histogram.csv\n"; return 2; }
    prefix[1][0] = 1;
    grow(1, 0);
    std::ofstream table(argv[1]);
    std::ofstream histogram(argv[2]);
    if (!table || !histogram) throw std::runtime_error("file creation failed");
    table << "n,distinct_arrays,letter_equivalence_classes,singleton_arrays,max_canonical_fiber\n";
    histogram << "canonical_fiber_size,number_of_arrays\n";
    for (int n = 1; n <= WIDTH; ++n) {
        std::map<std::uint32_t, std::uint64_t> hist;
        std::uint64_t classes = 0;
        for (auto const& item : counts[n]) {
            const bool constant_word = item.first == [&]() {
                Key signature = 0;
                for (int j = 1; j < n; ++j)
                    signature |= Key(j) << (4 * j);
                return signature;
            }();
            if (constant_word) {
                if (item.second != 1) throw std::runtime_error("constant-word multiplicity");
                ++hist[1]; ++classes;
            } else {
                if (item.second % 2 != 0) throw std::runtime_error("odd nonconstant orbit");
                const std::uint32_t count = item.second / 2;
                ++hist[count]; classes += count;
            }
        }
        table << n << ',' << counts[n].size() << ',' << classes << ','
              << hist[1] << ',' << hist.rbegin()->first << '\n';
        if (n == WIDTH)
            for (const auto& it : hist)
                histogram << it.first << ',' << it.second << '\n';
    }
    if (!table || !histogram) throw std::runtime_error("file output failed");
}
