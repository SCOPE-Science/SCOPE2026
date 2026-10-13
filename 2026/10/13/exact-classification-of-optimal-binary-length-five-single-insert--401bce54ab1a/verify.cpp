#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

// Exact finite search for length-five binary single-insertion coverings.
// Every binary length-six word must have a selected length-five subsequence.
using u64 = std::uint64_t;
using u32 = std::uint32_t;
constexpr int WORDS = 32;
constexpr int TARGETS = 64;
constexpr u64 UNIVERSE = ~u64{0};
std::array<u64, WORDS> ball{};
std::array<std::vector<int>, TARGETS> parents{};
std::set<u32> optimal;
std::uint64_t nodes = 0;

std::string bits(int x, int length) {
    std::string result(length, '0');
    for (int j = 0; j < length; ++j) result[j] = char('0' + ((x >> (length - 1 - j)) & 1));
    return result;
}
int codeword_from_target(int word, int removed) {
    int result = 0;
    for (int j = 0; j < 6; ++j) {
        if (j == removed) continue;
        result = (result << 1) | ((word >> (5-j)) & 1);
    }
    return result;
}
void search(u64 covered, u32 chosen, int remaining, bool collect) {
    ++nodes;
    if (covered == UNIVERSE) {
        if (collect) optimal.insert(chosen);
        else throw std::logic_error("unexpected covering below twelve");
        return;
    }
    if (remaining == 0) return;
    u64 uncovered = ~covered;
    if (std::popcount(uncovered) > 7 * remaining) return;
    int best = -1, least = WORDS + 1;
    for (int y = 0; y < TARGETS; ++y) {
        if ((uncovered & (u64{1} << y)) == 0) continue;
        int options = 0;
        for (int x : parents[y]) {
            if ((chosen & (u32{1} << x)) == 0) ++options;
        }
        if (options < least) { least = options; best = y; }
        if (least == 1) break;
    }
    if (best < 0 || least == 0) return;
    for (int x : parents[best]) {
        if (chosen & (u32{1} << x)) continue;
        search(covered | ball[x], chosen | (u32{1} << x), remaining - 1, collect);
    }
}
u32 transformed(u32 code, bool invert, bool reverse) {
    u32 ans = 0;
    for (int x = 0; x < WORDS; ++x) if (code & (u32{1} << x)) {
        int y = 0;
        for (int j = 0; j < 5; ++j) {
            int shift = reverse ? j : 4-j;
            y = (y << 1) | (((x >> shift) & 1) ^ int(invert));
        }
        ans |= u32{1} << y;
    }
    return ans;
}
int main() {
    for (int y = 0; y < TARGETS; ++y) {
        std::set<int> pred;
        for (int pos = 0; pos < 6; ++pos) pred.insert(codeword_from_target(y, pos));
        parents[y].assign(pred.begin(), pred.end());
        for (int x : pred) ball[x] |= u64{1} << y;
    }
    for (int x = 0; x < WORDS; ++x)
        if (std::popcount(ball[x]) != 7) throw std::logic_error("insertion ball size");
    for (int limit = 0; limit <= 11; ++limit) search(0, 0, limit, false);
    search(0, 0, 12, true);
    if (optimal.size() != 6) throw std::logic_error("optimal code enumeration");
    for (u32 code : optimal) {
        if (std::popcount(code) != 12) throw std::logic_error("wrong cardinality");
        u64 covered = 0;
        for (int x = 0; x < WORDS; ++x) if (code & (u32{1} << x)) covered |= ball[x];
        if (covered != UNIVERSE) throw std::logic_error("uncovered target");
    }
    std::set<u32> remaining = optimal;
    int orbits = 0;
    while (!remaining.empty()) {
        u32 rep = *remaining.begin();
        std::set<u32> orbit;
        for (bool invert : {false, true}) for (bool reverse : {false, true})
            orbit.insert(transformed(rep, invert, reverse));
        if (orbit.size() != 2) throw std::logic_error("orbit size");
        for (u32 code : orbit) {
            if (!remaining.erase(code)) throw std::logic_error("orbit closure");
        }
        ++orbits;
        std::cout << "representative";
        for (int x = 0; x < WORDS; ++x) if (rep & (u32{1} << x))
            std::cout << ' ' << bits(x, 5);
        std::cout << '\n';
    }
    if (orbits != 3) throw std::logic_error("orbit count");
    std::cout << "optimal_size=12 labeled_optima=6 complement_reversal_orbits=3 nodes="
              << nodes << " VERIFY_OK\n";
}
