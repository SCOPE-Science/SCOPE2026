// Exhaustive finite certificate for the order-eleven prime-power zero-sum theorem.
// C++17, with no nonstandard libraries or network access.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify
// Run: ./verify
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using i64 = std::int64_t;
using i128 = __int128_t;

static i64 power_mod(i64 x, i64 e, i64 mod) {
    i64 out = 1;
    while (e) {
        if (e & 1) out = static_cast<i64>((i128)out * x % mod);
        x = static_cast<i64>((i128)x * x % mod);
        e >>= 1;
    }
    return out;
}

static i64 inverse_mod(i64 a, i64 p) {
    // The modulus p is prime and a is nonzero modulo p.
    // Fermat inversion avoids dependence on any external library.
    return power_mod(a, p - 2, p);
}

static i64 root_of_order_eleven(int p, int exponent) {
    i64 a = 0;
    for (int x = 2; x < p; ++x) {
        if (power_mod(x, 11, p) == 1) { a = x; break; }
    }
    if (a == 0) throw "missing root modulo prime";
    i64 q = a, mod = p;
    for (int j = 1; j < exponent; ++j) {
        const i64 higher = mod * p;
        const i64 f = (power_mod(q, 11, higher) - 1 + higher) % higher;
        if (f % mod != 0) throw "Hensel divisibility failed";
        const i64 digit = f / mod;
        const i64 derivative = (11 * power_mod(q, 10, p)) % p;
        const i64 correction = (p - (digit * inverse_mod(derivative, p)) % p) % p;
        q += correction * mod;
        mod = higher;
    }
    if (q % p != a || power_mod(q, 11, mod) != 1 || q == 1)
        throw "root certification failed";
    return q;
}

struct Exhaustive {
    i64 mod = 1;
    std::array<i64, 11> powers{};
    std::array<int, 11> coefficients{};
    std::array<int, 11> witness{};
    std::uint64_t tested = 0;
    int shortest = 11;

    void enumerate(int i, int t, i64 sum) {
        if (i == 11) {
            if (t > 0) {
                ++tested;
                if (sum == 0 && t < shortest) {
                    shortest = t;
                    witness = coefficients;
                }
            }
            return;
        }
        for (int c = 0; c <= 10 - t; ++c) {
            coefficients[i] = c;
            enumerate(i + 1, t + c, (sum + c * powers[i]) % mod);
        }
    }

    Exhaustive(int p, int exponent) {
        for (int j = 0; j < exponent; ++j) mod *= p;
        i64 q = root_of_order_eleven(p, exponent);
        powers[0] = 1;
        for (int j = 1; j < 11; ++j)
            powers[j] = static_cast<i64>((i128)powers[j-1] * q % mod);
        if (static_cast<i64>((i128)powers[10] * q % mod) != 1)
            throw "incorrect cyclic subgroup";
        enumerate(0, 0, 0);
        // C(21,11)-1, all nonzero weak 11-compositions with sum at most 10.
        if (tested != 352715) throw "enumeration incomplete";
        if (shortest < 11) {
            int t = 0;
            i64 sum = 0;
            for (int i = 0; i < 11; ++i) {
                t += witness[i];
                sum = (sum + witness[i] * powers[i]) % mod;
            }
            if (sum != 0 || t != shortest) throw "incorrect witness";
        }
    }
};

static void check(int p, int exponent, int expected) {
    Exhaustive e(p, exponent);
    if (e.shortest != expected) {
        std::cerr << "Incorrect minimum at " << p << ", " << exponent
                  << ": " << e.shortest << " != " << expected << "\n";
        throw "classification mismatch";
    }
}

int main() {
    try {
        constexpr int bound = 100000;
        std::vector<bool> prime(bound + 1, true);
        prime[0] = prime[1] = false;
        for (int d = 2; d * d <= bound; ++d)
            if (prime[d])
                for (int j = d * d; j <= bound; j += d) prime[j] = false;
        int primes_checked = 0, exceptions = 0;
        constexpr std::array<int,4> special_p{23,67,89,683};
        constexpr std::array<int,4> special_m{5,8,9,9};
        for (int p = 2; p <= bound; ++p) {
            if (!prime[p] || p % 11 != 1) continue;
            ++primes_checked;
            int expected = 11;
            for (int j=0;j<4;++j)
                if (special_p[j] == p) expected = special_m[j];
            if (expected < 11) ++exceptions;
            check(p, 2, expected);
        }
        if (primes_checked != 945 || exceptions != 4)
            throw "prime census mismatch";
        check(23, 3, 9);
        check(23, 4, 9);
        check(23, 5, 11);
        check(67, 3, 11);
        check(89, 3, 11);
        check(683, 3, 11);
        // The known upper bound of 11 follows from the full geometric sum.
        std::cout << "VERIFY_OK primes=945 vectors_per_prime=352715 "
                  << "exceptions=23,67,89,683 deeper_checks=6\n";
        return 0;
    } catch (const char* message) {
        std::cerr << "VERIFY_FAILED: " << message << "\n";
        return 1;
    }
}
