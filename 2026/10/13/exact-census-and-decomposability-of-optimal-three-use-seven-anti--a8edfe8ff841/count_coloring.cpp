// Independent greedy-coloring exact clique census through the origin.
// Edges are built as the complement of the strong product of three copies of
// the seven-antihole, using confusability rather than the direct distinction test.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

constexpr int N = 343;
constexpr int blocks = 6;
using U64 = std::uint64_t;
struct Bits {
    std::array<U64, blocks> b{};
    void set(int i) { b[i / 64] |= 1ULL << (i % 64); }
    void erase(int i) { b[i / 64] &= ~(1ULL << (i % 64)); }
    bool empty() const { for (const auto x : b) if (x) return false; return true; }
    int size() const { int c = 0; for (const auto x : b) c += __builtin_popcountll(x); return c; }
    Bits operator&(const Bits& other) const {
        Bits ans;
        for (int k = 0; k < blocks; ++k) ans.b[k] = b[k] & other.b[k];
        return ans;
    }
};
Bits neighbors[N];
U64 rooted8 = 0;
U64 rooted9 = 0;

// One-coordinate confusability in the seven-antihole: distances 0,+/-2,+/-3.
bool confusable(int x, int y) {
    for (int j = 0; j < 3; ++j) {
        int d = (x % 7 - y % 7 + 7) % 7;
        if (d == 1 || d == 6) return false;
        x /= 7;
        y /= 7;
    }
    return true;
}

void color_sort(Bits available, std::vector<int>& order,
                std::vector<int>& upper_colors) {
    int color = 0;
    while (!available.empty()) {
        ++color;
        Bits same_color = available;
        while (!same_color.empty()) {
            int v = -1;
            for (int k = 0; k < blocks; ++k) {
                if (same_color.b[k]) {
                    v = 64*k + __builtin_ctzll(same_color.b[k]);
                    break;
                }
            }
            order.push_back(v);
            upper_colors.push_back(color);
            available.erase(v);
            same_color.erase(v);
            // Keep only vertices nonadjacent to v in the next color class.
            for (int k = 0; k < blocks; ++k)
                same_color.b[k] &= ~neighbors[v].b[k];
        }
    }
}

// The reverse-color ordering partitions cliques uniquely according to the
// first selected vertex. The color bound is an admissible clique-size bound.
void enumerate(Bits candidates, int chosen) {
    if (chosen == 8) ++rooted8;
    if (chosen == 9) { ++rooted9; return; }
    if (chosen + candidates.size() < 8) return;
    std::vector<int> order, bound;
    color_sort(candidates, order, bound);
    for (int k = static_cast<int>(order.size()) - 1; k >= 0; --k) {
        if (chosen + bound[k] < 8) return;
        const int v = order[k];
        enumerate(candidates & neighbors[v], chosen + 1);
        candidates.erase(v);
    }
}

int main() {
    for (int x = 0; x < N; ++x)
        for (int y = 0; y < N; ++y)
            if (x != y && !confusable(x, y)) neighbors[x].set(y);
    enumerate(neighbors[0], 1);
    std::cout << "COLORING rooted_eight=" << rooted8
              << " rooted_nine=" << rooted9 << '\n';
    if (rooted8 != 38259704ULL || rooted9 != 0ULL) return 1;
    return 0;
}
