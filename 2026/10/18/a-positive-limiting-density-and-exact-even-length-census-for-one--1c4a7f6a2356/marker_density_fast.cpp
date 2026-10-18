#include <cstdio>
#include <cstdint>
#include <cmath>
#include <cassert>
using u64 = std::uint64_t;

int main() {
    const u64 expected25 = 1298518439058409ULL;
    for (int J = 0; J <= 25; ++J) {
        const u64 total_r = 1ULL << (J + 2);
        const u64 all_l = 1ULL << J;
        u64 good = 0;
        for (u64 right = 0; right < total_r; ++right) {
            u64 available = all_l;
            for (int j = 0; j <= J; ++j) {
                // Zero bit is letter A. Bit j+1 is the (j+2)-th
                // letter in the reversed right tail.
                if (((right >> (j + 1)) & 1ULL) != 0) continue;
                bool subsumed = false;
                for (int i = 0; i < j; ++i) {
                    if (((right >> (i + 1)) & 1ULL) != 0) continue;
                    const u64 mask = (1ULL << i) - 1ULL;
                    if ((right & mask) == ((right >> (j - i)) & mask)) {
                        subsumed = true;
                        break;
                    }
                }
                if (!subsumed) available -= 1ULL << (J - j);
                if (available == 0) break;
            }
            good += available;
        }
        if (J == 25) assert(good == expected25);
        std::printf("J=%d numerator=%llu denominator=2^%d\n", J,
                    static_cast<unsigned long long>(good), 2*J+2);
    }
    std::puts("PASS: exact J=25 numerator");
    return 0;
}
