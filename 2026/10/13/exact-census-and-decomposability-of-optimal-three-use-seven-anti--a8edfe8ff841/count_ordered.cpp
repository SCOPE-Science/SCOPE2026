// Exact ascending-order clique enumeration for a three-use seven-symbol channel.
// A pair of length-three words is distinguishable when at least one coordinate
// differs by +1 or -1 modulo seven. Every code counted contains word (0,0,0).
#include <array>
#include <cstdint>
#include <iostream>

constexpr int alphabet = 7;
constexpr int uses = 3;
constexpr int vertex_count = 343;
constexpr int blocks = 6;
using Bits = std::array<std::uint64_t, blocks>;

Bits adjacency[vertex_count]{};
std::uint64_t count8 = 0;
std::uint64_t count9 = 0;

bool distinguishable(int x, int y) {
    for (int j = 0; j < uses; ++j) {
        const int a = x % alphabet, b = y % alphabet;
        const int d = (a - b + alphabet) % alphabet;
        if (d == 1 || d == 6) return true;
        x /= alphabet;
        y /= alphabet;
    }
    return false;
}

int cardinality(const Bits& b) {
    int size = 0;
    for (const auto x : b) size += __builtin_popcountll(x);
    return size;
}

// The mutable candidate mask contains only vertices larger than every vertex
// already chosen. Thus each clique through zero is generated exactly once.
void enumerate(Bits candidates, int chosen) {
    if (chosen == 8) ++count8;
    if (chosen == 9) {
        ++count9;
        return;
    }
    if (chosen + cardinality(candidates) < 8) return;
    for (int k = 0; k < blocks; ++k) {
        while (candidates[k] != 0) {
            const auto least = candidates[k] & (~candidates[k] + 1ULL);
            const int vertex = 64 * k + __builtin_ctzll(least);
            candidates[k] ^= least;
            Bits next{};
            for (int l = 0; l < blocks; ++l)
                next[l] = candidates[l] & adjacency[vertex][l];
            enumerate(next, chosen + 1);
        }
    }
}

int main() {
    for (int x = 0; x < vertex_count; ++x)
        for (int y = 0; y < vertex_count; ++y)
            if (x != y && distinguishable(x, y))
                adjacency[x][y / 64] |= 1ULL << (y % 64);

    enumerate(adjacency[0], 1);
    std::cout << "ORDERED rooted_eight=" << count8
              << " rooted_nine=" << count9 << '\n';
    if (count8 != 38259704ULL || count9 != 0ULL) return 1;
    return 0;
}
