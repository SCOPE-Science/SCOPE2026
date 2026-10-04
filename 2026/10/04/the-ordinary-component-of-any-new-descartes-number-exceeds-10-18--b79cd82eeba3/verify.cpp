#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static std::string dec(u128 x) {
    if (x == 0) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    const u64 ROOT_MAX = 1000000000ULL;
    const u64 SEG_ODD_COUNT = 1000000ULL;
    const int PRIME_LIMIT = 31623;

    std::vector<bool> composite(PRIME_LIMIT + 1, false);
    std::vector<int> primes;
    for (int i = 2; i <= PRIME_LIMIT; ++i) {
        if (!composite[i]) {
            primes.push_back(i);
            if (1LL * i * i <= PRIME_LIMIT)
                for (long long j = 1LL * i * i; j <= PRIME_LIMIT; j += i)
                    composite[(std::size_t)j] = true;
        }
    }

    std::vector<std::uint32_t> remainder;
    std::vector<u128> sigma_square;
    std::vector<std::tuple<u64,u64,u64>> odd_parameter_hits;
    u64 square_members = 0;

    for (u64 L = 1; L <= ROOT_MAX; L += 2 * SEG_ODD_COUNT) {
        u64 H = std::min(ROOT_MAX, L + 2 * SEG_ODD_COUNT - 2);
        if ((L & 1ULL) == 0) ++L;
        const std::size_t count = (std::size_t)((H - L) / 2 + 1);
        remainder.resize(count);
        sigma_square.assign(count, 1);
        for (std::size_t i = 0; i < count; ++i)
            remainder[i] = (std::uint32_t)(L + 2 * i);

        for (int p : primes) {
            if (p == 2) continue;
            if ((u64)p * (u64)p > H) break;
            u64 start = ((L + p - 1) / p) * (u64)p;
            if ((start & 1ULL) == 0) start += p;
            for (u64 v = start; v <= H; v += 2ULL * (u64)p) {
                const std::size_t idx = (std::size_t)((v - L) / 2);
                if (remainder[idx] % (std::uint32_t)p != 0) continue;
                int e = 0;
                while (remainder[idx] % (std::uint32_t)p == 0) {
                    remainder[idx] /= (std::uint32_t)p;
                    ++e;
                }
                u128 power = 1, geom = 1;
                for (int j = 0; j < 2 * e; ++j) {
                    power *= (u64)p;
                    geom += power;
                }
                sigma_square[idx] *= geom;
            }
        }

        for (std::size_t i = 0; i < count; ++i) {
            const u64 m = L + 2 * i;
            const u64 r = remainder[i];
            if (r > 1)
                sigma_square[i] *= (u128)1 + r + (u128)r * r;

            const u128 q = (u128)m * m;
            const u128 sig = sigma_square[i];
            if (sig >= 2 * q) continue;
            const u128 deficiency = 2 * q - sig;
            if (sig % deficiency != 0) continue;
            const u128 x128 = sig / deficiency;
            ++square_members;
            if ((x128 & 1) == 0) continue;
            if (q > (u128)UINT64_MAX || x128 > (u128)UINT64_MAX) {
                std::cerr << "unexpected width\n";
                return 2;
            }
            odd_parameter_hits.emplace_back((u64)q, (u64)x128, m);
        }
    }

    if (square_members != 2) return 3;
    if (odd_parameter_hits.size() != 2) return 4;
    if (odd_parameter_hits[0] != std::make_tuple(1ULL,1ULL,1ULL)) return 5;
    if (odd_parameter_hits[1] != std::make_tuple(9018009ULL,22021ULL,3003ULL)) return 6;
    if (22021ULL != 19ULL * 19ULL * 61ULL) return 7;

    std::cout << "VERIFY_OK\n";
    std::cout << "root_range=1..1000000000 odd roots\n";
    std::cout << "q_range=1..1000000000000000000 squares\n";
    std::cout << "square_members=2\n";
    std::cout << "q=1 root=1 x=1\n";
    std::cout << "q=9018009 root=3003 x=22021=19^2*61\n";
    return 0;
}
