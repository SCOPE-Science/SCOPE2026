// Exhaustive independent bitwise update implementation for left-to-right bi-threshold sweeps.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

static unsigned iterate(unsigned mask, int n) {
    unsigned state = mask;
    for (int i = 0; i < n; ++i) {
        const unsigned bit = 1u << i;
        const bool was_on = (state & bit) != 0;
        const int neighbors = int(i > 0 && (state & (1u << (i - 1))) != 0)
                            + int(i + 1 < n && (state & (1u << (i + 1))) != 0);
        const bool now_on = (neighbors + int(was_on)) >= (was_on ? 3 : 1);
        state = now_on ? (state | bit) : (state & ~bit);
    }
    return state;
}

static int expected_time(unsigned m, int n) {
    int rightmost_ascent = -1;
    for (int i = 0; i + 1 < n; ++i) {
        if (!(m & (1u << i)) && (m & (1u << (i+1)))) rightmost_ascent = i;
    }
    return rightmost_ascent >= 0 ? rightmost_ascent + 2 : (m != 0);
}

int main() {
    unsigned long long total = 0;
    for (int n = 2; n <= 20; ++n) {
        std::vector<unsigned long long> counts(n + 1, 0);
        const unsigned limit = 1u << n;
        for (unsigned m = 0; m < limit; ++m) {
            unsigned cur = m;
            int t = 0;
            while (cur != 0 && t <= n) {
                cur = iterate(cur, n);
                ++t;
            }
            assert(cur == 0 && t == expected_time(m, n));
            counts[t]++;
        }
        assert(counts[0] == 1 && counts[1] == unsigned(n));
        for (int t = 2; t <= n; ++t) {
            assert(counts[t] == (unsigned long long)(n - t + 1) * (1ull << (t - 2)));
        }
        total += limit;
        std::cout << "n=" << n << " states=" << limit << " maximal_time_states=" << counts[n] << "\n";
    }
    std::cout << "PASS: 2<=n<=20; total_states=" << total << "; independent per-update bitwise sweep\n";
}
