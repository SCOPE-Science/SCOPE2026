#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    const int N = 100000000;
    std::vector<int> least_prime(N + 1, 0);
    std::vector<int> L2(N + 1, 0);
    std::vector<std::int64_t> D2(N + 1, 0);
    std::vector<int> primes;
    primes.reserve(6000000);

    least_prime[1] = 1;
    L2[1] = 1;
    D2[1] = 0;

    // Linear sieve: least_prime[n] is the least prime divisor of n.
    for (int n = 2; n <= N; ++n) {
        if (least_prime[n] == 0) {
            least_prime[n] = n;
            primes.push_back(n);
        }
        for (int p : primes) {
            const std::int64_t v = static_cast<std::int64_t>(n) * p;
            if (v > N || p > least_prime[n]) break;
            least_prime[static_cast<int>(v)] = p;
        }
    }

    if (primes.size() != 5761455) {
        std::cerr << "PRIME_COUNT_FAIL count=" << primes.size() << "\n";
        return 4;
    }

    std::vector<int> fixed_points;
    std::int64_t max_D2 = 0;
    int argmax_D2 = 0;

    for (int n = 2; n <= N; ++n) {
        if ((n & 1) == 0) {
            // The least prime divisor is <=2, so L_2(n)=0 and D_2(n)=0.
            L2[n] = 0;
            D2[n] = 0;
        } else {
            const int p = least_prime[n];
            const int m = n / p;
            if (m % p == 0) {
                // p already divides m: increasing its exponent by one multiplies L_2 by p.
                L2[n] = static_cast<int>(static_cast<std::int64_t>(p) * L2[m]);
            } else {
                // p is a new prime factor: multiplicativity contributes L_2(p)=p-2.
                L2[n] = static_cast<int>(static_cast<std::int64_t>(p - 2) * L2[m]);
            }
            if (!(0 <= L2[n] && L2[n] < n)) {
                std::cerr << "L2_RANGE_FAIL n=" << n << " L2=" << L2[n] << "\n";
                return 2;
            }
            D2[n] = static_cast<std::int64_t>(L2[n]) + D2[L2[n]];
        }

        if (D2[n] > max_D2) {
            max_D2 = D2[n];
            argmax_D2 = n;
        }
        if (D2[n] == n) fixed_points.push_back(n);
    }

    const std::vector<int> expected{37147, 53290831};
    if (fixed_points != expected) {
        std::cerr << "FIXED_POINT_SET_FAIL count=" << fixed_points.size() << "\n";
        for (int n : fixed_points) std::cerr << n << " ";
        std::cerr << "\n";
        return 3;
    }

    std::cout << "VERIFY_OK cutoff=" << N
              << " fixed_points=37147,53290831"
              << " pi_count=" << primes.size()
              << " max_D2=" << max_D2
              << " argmax_D2=" << argmax_D2
              << "\n";
    return 0;
}
