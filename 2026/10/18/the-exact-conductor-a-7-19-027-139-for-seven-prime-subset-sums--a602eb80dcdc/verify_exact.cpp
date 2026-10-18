// Exact finite certificate for a seven-prime-product subset-sum conductor.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_exact.cpp -o verify_exact
// Run: ./verify_exact
// No external libraries, tables, or downloads.
#include <cstdint>
#include <cstdio>
#include <vector>

int main() {
    constexpr int SIEVE_LIMIT = 19120000;
    constexpr int SUBSET_SUM_LIMIT = 40000000;
    constexpr int TERMS = 3100;
    constexpr int EXPECTED_GAP = 19027139;
    constexpr int EXPECTED_LAST_USED = 19111638;
    constexpr int EXPECTED_NEXT = 19114095;

    // Distinct prime divisor count and indicator of a repeated prime factor.
    std::vector<std::uint8_t> omega(SIEVE_LIMIT + 1, 0);
    std::vector<std::uint8_t> squareful(SIEVE_LIMIT + 1, 0);
    for (int p = 2; p <= SIEVE_LIMIT; ++p) {
        if (omega[p] != 0) continue;  // p is composite
        for (int j = p; j <= SIEVE_LIMIT; j += p) ++omega[j];
        if (static_cast<std::int64_t>(p) * p <= SIEVE_LIMIT) {
            int pp = p*p;
            for (int j = pp; j <= SIEVE_LIMIT; j += pp) squareful[j] = 1;
        }
    }
    std::vector<int> coins;
    for (int v = 2; v <= SIEVE_LIMIT; ++v) {
        if (omega[v] == 7 && !squareful[v]) coins.push_back(v);
    }
    if (coins.size() <= TERMS || coins.front() != 510510 ||
        coins[TERMS - 1] != EXPECTED_LAST_USED ||
        coins[TERMS] != EXPECTED_NEXT ||
        coins[TERMS-1] <= EXPECTED_GAP) return 1;

    // One bit per represented sum, using each coin zero or one times.
    // Descending updates ensure the newly added coin is not reused.
    std::vector<std::uint64_t> reachable(SUBSET_SUM_LIMIT/64 + 1, 0);
    reachable[0] = 1;
    for (int h = 0; h < TERMS; ++h) {
        const int s = coins[h], q = s/64, r = s%64;
        for (int j = static_cast<int>(reachable.size()) - 1; j >= q; --j) {
            std::uint64_t shifted = reachable[j-q] << r;
            if (r != 0 && j > q) shifted |= reachable[j-q-1] >> (64-r);
            reachable[j] |= shifted;
        }
    }
    auto present = [&](int n) -> bool {
        return (reachable[n / 64] & (std::uint64_t(1) << (n % 64))) != 0;
    };
    int largest_missing = -1;
    for (int n = SUBSET_SUM_LIMIT; n >= 0; --n) {
        if (!present(n)) { largest_missing = n; break; }
    }
    const int width = SUBSET_SUM_LIMIT-largest_missing;
    if (largest_missing != EXPECTED_GAP || present(EXPECTED_GAP) ||
        !present(EXPECTED_GAP + 1) || !present(SUBSET_SUM_LIMIT) ||
        width < coins[TERMS]) return 2;

    std::printf("terms=%d first=%d last_used=%d next=%d\n", TERMS,
        coins.front(), coins[TERMS-1], coins[TERMS]);
    std::printf("largest_missing=%d represented_interval=[%d,%d] width=%d\n",
        largest_missing, largest_missing+1, SUBSET_SUM_LIMIT, width);
    std::puts("VERIFY_OK");
    return 0;
}
