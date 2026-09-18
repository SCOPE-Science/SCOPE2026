#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>

using i64 = long long;

static i64 icbrt(i64 n) {
    i64 r = (i64)std::cbrt((long double)n);
    while ((__int128)(r + 1) * (r + 1) * (r + 1) <= n) ++r;
    while ((__int128)r * r * r > n) --r;
    return r;
}

static i64 isqrt(i64 n) {
    i64 r = (i64)std::sqrt((long double)n);
    while ((__int128)(r + 1) * (r + 1) <= n) ++r;
    while ((__int128)r * r > n) --r;
    return r;
}

struct Counts {
    unsigned long long pairs = 0;
    unsigned long long first_equalities = 0;
    unsigned long long floor_admissible = 0;
    unsigned long long triples = 0;
};

static Counts pair_search(i64 T) {
    const i64 Amax = icbrt(3*T*T + 3*T);
    const i64 Bmax = icbrt(6*T*T + 1);
    std::vector<i64> cube(Bmax + 1);
    for (i64 j = 0; j <= Bmax; ++j) cube[j] = j*j*j;

    Counts out;
    for (i64 a = 0; a <= Amax; ++a) {
        const i64 a3 = cube[a];
        for (i64 b = a + 1; b <= Bmax; ++b) {
            ++out.pairs;
            const i64 D = cube[b] - a3;
            const i64 disc = 12*D - 3;
            const i64 s = isqrt(disc);
            if (s*s != disc || s % 6 != 3) continue;
            const i64 t = (s + 3)/6;
            if (t < 1 || t > T) continue;
            ++out.first_equalities;

            // t=floor(n^(1/3)) with n=t^3+a^3.
            if (a3 >= 3*t*t + 3*t + 1) continue;
            ++out.floor_admissible;

            // n-(t-2)^3.
            const i64 c3 = a3 + 6*t*t - 12*t + 8;
            const i64 c = icbrt(c3);
            if (c*c*c == c3) ++out.triples;
        }
    }
    return out;
}

static unsigned long long direct_first_pair_count(i64 T) {
    unsigned long long out = 0;
    for (i64 t = 1; t <= T; ++t) {
        const i64 Amax = icbrt(3*t*t + 3*t);
        for (i64 a = 0; a <= Amax; ++a) {
            const i64 a3 = a*a*a;
            const i64 b3 = a3 + 3*t*t - 3*t + 1;
            const i64 b = icbrt(b3);
            if (b*b*b == b3) ++out;
        }
    }
    return out;
}

int main() {
    const i64 T = 333333;
    const i64 bound = (T + 1)*(T + 1)*(T + 1);
    const i64 alpha2_upper = 9*T*T - 9*T + 9;
    const i64 source_N3 = 1000000000000LL;

    Counts full = pair_search(T);
    Counts small_pair = pair_search(10000);
    unsigned long long small_direct = direct_first_pair_count(10000);

    std::cout << "T=" << T << "\n";
    std::cout << "Amax=" << icbrt(3*T*T + 3*T) << "\n";
    std::cout << "Bmax=" << icbrt(6*T*T + 1) << "\n";
    std::cout << "pair_checks=" << full.pairs << "\n";
    std::cout << "first_equalities_before_floor=" << full.first_equalities << "\n";
    std::cout << "floor_admissible_first_pairs=" << full.floor_admissible << "\n";
    std::cout << "triple_cube_obstructions=" << full.triples << "\n";
    std::cout << "small_direct_first_pairs=" << small_direct << "\n";
    std::cout << "small_pair_first_pairs=" << small_pair.floor_admissible << "\n";
    std::cout << "alpha2_upper_at_T=" << alpha2_upper << "\n";
    std::cout << "source_N3=" << source_N3 << "\n";
    std::cout << "representation_bound=" << bound << "\n";

    bool ok = true;
    ok = ok && (full.pairs == 36531779ULL);
    ok = ok && (full.first_equalities == 7683ULL);
    ok = ok && (full.floor_admissible == 579ULL);
    ok = ok && (full.triples == 0ULL);
    ok = ok && (small_direct == 110ULL);
    ok = ok && (small_pair.floor_admissible == small_direct);
    ok = ok && (alpha2_upper == 999995000013LL);
    ok = ok && (alpha2_upper < source_N3);
    ok = ok && (6LL*333334LL*333334LL < source_N3 - 2);

    std::cout << "verification=" << (ok ? "PASS" : "FAIL") << "\n";
    return ok ? 0 : 1;
}
