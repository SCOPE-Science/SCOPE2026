#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <unordered_map>
#include <vector>

constexpr int LIMIT = 16;
using Signature = std::uint64_t;
std::array<std::unordered_map<Signature, std::uint32_t>, LIMIT + 1> frequencies;
std::array<std::array<int, 3>, LIMIT + 1> prefix{};

void visit(int length, int highest_letter, Signature signature) {
    ++frequencies[length][signature];
    if (length == LIMIT) return;
    for (int letter = 0; letter <= std::min(2, highest_letter + 1); ++letter) {
        for (int a = 0; a < 3; ++a)
            prefix[length + 1][a] = prefix[length][a] + (a == letter);
        int border = 0;
        for (int k = length; k >= 1; --k) {
            bool equal = true;
            for (int a = 0; a < 3; ++a)
                if (prefix[k][a] != prefix[length + 1][a] - prefix[length + 1 - k][a])
                    equal = false;
            if (equal) { border = k; break; }
        }
        visit(length + 1, std::max(highest_letter, letter),
              signature | (Signature(border) << (4 * length)));
    }
}

int main(int argc, char** argv) {
    if (argc != 3) { std::cerr << "usage: executable table.csv histogram.csv\n"; return 2; }
    prefix[1][0] = 1;
    visit(1, 0, 0);
    std::ofstream table(argv[1]);
    std::ofstream histogram(argv[2]);
    if (!table || !histogram) throw std::runtime_error("file creation failed");
    table << "n,distinct_arrays,letter_equivalence_classes,singleton_arrays,max_canonical_fiber\n";
    histogram << "canonical_fiber_size,number_of_arrays\n";
    for (int n = 1; n <= LIMIT; ++n) {
        std::uint64_t classes = 0;
        std::map<std::uint32_t, std::uint64_t> hist;
        for (const auto& it : frequencies[n]) {
            classes += it.second;
            ++hist[it.second];
        }
        table << n << ',' << frequencies[n].size() << ',' << classes << ','
              << hist[1] << ',' << hist.rbegin()->first << '\n';
        if (n == LIMIT)
            for (const auto& it : hist)
                histogram << it.first << ',' << it.second << '\n';
    }
    if (!table || !histogram) throw std::runtime_error("file output failed");
}
