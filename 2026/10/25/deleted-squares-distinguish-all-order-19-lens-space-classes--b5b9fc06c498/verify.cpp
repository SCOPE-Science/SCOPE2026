#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

// Exact F_2 linear algebra for the triple-Massey obstruction in deleted
// squares of three-dimensional lens spaces.  All vectors are bit masks.
static int P, D, Q, Qp;
static uint32_t MASK;
static uint32_t T[2][19][18][18][18];

static uint32_t mul_t(uint32_t x) {
    const uint32_t top = (x >> (D - 1)) & 1u;
    return ((x << 1) & MASK) ^ (top ? MASK : 0u);
}
static uint32_t shift_t(uint32_t x, int k) {
    k %= P;
    while (k-- > 0) x = mul_t(x);
    return x;
}
static uint32_t monomial(int k) { return shift_t(1u, k); }
static uint32_t sum_range(int a, int b) {
    uint32_t x = 0;
    for (int i = a; i <= b; ++i) x ^= monomial(i);
    return x;
}
static bool in_open_interval(int r, int q) { return r >= 1 && r <= q - 1; }
static bool interloper(int k, int j, int q) {
    const int r = (j * q) % P;
    const int rn = (P - r) % P;
    return (in_open_interval(r, q) && k >= j) ||
           (in_open_interval(rn, q) && k <= j);
}

// Representative for <t^a,1,t^b>, using Theorem 7.1 of Evans-Lee--Saveliev.
static uint32_t M(int a, int b, int q) {
    a %= P; b %= P;
    if (a == 0 && b == 0) return 0; // zero is an allowed representative modulo indeterminacy
    if (a == 0) {
        const int r = (b * q) % P, rn = (P - r) % P;
        if (in_open_interval(rn, q)) return sum_range(1, b);
        if (in_open_interval(r, q)) return sum_range(b, P - 1);
        return 0;
    }
    if (b == 0) {
        const int r = (a * q) % P, rn = (P - r) % P;
        if (in_open_interval(rn, q)) return sum_range(1, a);
        if (in_open_interval(r, q)) return sum_range(a, P - 1);
        return 0;
    }
    const bool ab = interloper(a, b, q), ba = interloper(b, a, q);
    if (ab && ba) return monomial(a) ^ monomial(b);
    if (ab) return monomial(a);
    if (ba) return monomial(b);
    return 0;
}

static void prepare(int p, int q, int qp) {
    P = p; D = p - 1; Q = q; Qp = qp;
    MASK = (1u << D) - 1u;
    for (int qi = 0; qi < 2; ++qi) {
        const int qq = qi == 0 ? Q : Qp;
        for (int i = 0; i < D; ++i)
            for (int j = 0; j < D; ++j)
                for (int k = 0; k < D; ++k)
                    T[qi][0][i][j][k] = shift_t(M((i - j + P) % P,
                                                    (k - j + P) % P, qq), j);
    }
}
static uint32_t mu(int qi, uint32_t x, uint32_t y, uint32_t z) {
    uint32_t out = 0;
    while (x) {
        const int i = __builtin_ctz(x); x &= x - 1;
        uint32_t yy = y;
        while (yy) {
            const int j = __builtin_ctz(yy); yy &= yy - 1;
            uint32_t zz = z;
            while (zz) {
                const int k = __builtin_ctz(zz); zz &= zz - 1;
                out ^= T[qi][0][i][j][k];
            }
        }
    }
    return out;
}
static uint32_t induced_map(uint32_t v, uint32_t c, int beta) {
    uint32_t out = 0;
    for (int i = 0; i < D; ++i)
        if ((v >> i) & 1u) out ^= shift_t(c, (beta * i) % P);
    return out;
}
static bool in_span(uint32_t d, uint32_t x, uint32_t z) {
    return d == 0 || d == x || d == z || d == (x ^ z);
}
static bool preserves_massey(uint32_t c, int beta) {
    uint32_t xp[19], zp[19];
    for (int k = 0; k < P; ++k)
        xp[k] = zp[k] = shift_t(c, (beta * k) % P);
    for (int k = 0; k < P; ++k) for (int l = 0; l < P; ++l) {
        const uint32_t lhs = mu(1, xp[k], c, zp[l]);
        const uint32_t rhs = induced_map(M(k, l, Q), c, beta);
        if (!in_span(lhs ^ rhs, xp[k], zp[l])) return false;
    }
    return true;
}
static int inverse_mod(int a, int p) {
    for (int b = 1; b < p; ++b) if ((a * b) % p == 1) return b;
    return 0;
}
static int norm_lens_parameter(int a, int p) {
    a %= p; if (a < 0) a += p;
    return std::min(a, p - a);
}
static bool homotopy_equivalent_lens_spaces(int q, int qp, int p) {
    for (int a = 1; a < p; ++a) {
        const int z = (q * a * a) % p;
        if (z == qp || z == (p - qp) % p) return true;
    }
    return false;
}
static bool homeomorphic_lens_spaces(int q, int qp, int p) {
    return qp == q || qp == norm_lens_parameter(inverse_mod(q, p), p);
}
static std::vector<std::pair<int, uint64_t>> run_pair(int p, int q, int qp) {
    prepare(p, q, qp);
    std::vector<int> betas;
    for (int a = 1; a < p; ++a) {
        const int z = (q * a * a) % p;
        if (z == qp || z == (p - qp) % p) betas.push_back(inverse_mod(a, p));
    }
    std::sort(betas.begin(), betas.end());
    betas.erase(std::unique(betas.begin(), betas.end()), betas.end());
    std::vector<std::pair<int, uint64_t>> out;
    for (int beta : betas) {
        uint64_t survivors = 0;
        for (uint32_t c = 1; c <= MASK; ++c)
            if (preserves_massey(c, beta)) ++survivors;
        out.push_back({beta, survivors});
    }
    return out;
}
int main() {
    // Unit tests against the published p=5, q=2 examples in Section 7.2.
    P = 5; D = 4; Q = 2; Qp = 2; MASK = (1u << D) - 1u;
    if (M(0, 2, 2) != (monomial(1) ^ monomial(2)) ||
        M(0, 3, 2) != (monomial(3) ^ monomial(4)) ||
        M(1, 2, 2) != monomial(1) || M(4, 3, 2) != monomial(4)) {
        std::cerr << "published p=5 Massey-formula control failed\n";
        return 2;
    }
    std::cout << "control p=5 published Massey representatives: PASS\n";

    // Published-formula controls: one known homeomorphic pair and two known
    // non-homeomorphic pairs whose deleted squares are distinguished by Massey products.
    auto control_homeo = run_pair(19, 2, 9);
    auto control_11 = run_pair(11, 2, 3);
    auto control_7 = run_pair(7, 1, 2);
    std::cout << "control p=19 pair=(2,9) survivors:";
    for (auto [b,n] : control_homeo) std::cout << " " << b << ":" << n;
    std::cout << "\ncontrol p=11 pair=(2,3) survivors:";
    for (auto [b,n] : control_11) std::cout << " " << b << ":" << n;
    std::cout << "\ncontrol p=7 pair=(1,2) survivors:";
    for (auto [b,n] : control_7) std::cout << " " << b << ":" << n;
    std::cout << "\n";

    int tested = 0, with_survivor = 0;
    for (int q = 1; q <= 9; ++q) for (int qp = q + 1; qp <= 9; ++qp) {
        if (!homotopy_equivalent_lens_spaces(q, qp, 19) ||
            homeomorphic_lens_spaces(q, qp, 19)) continue;
        const auto out = run_pair(19, q, qp);
        bool any = false;
        std::cout << "pair (" << q << "," << qp << ")";
        for (auto [b,n] : out) { std::cout << " beta=" << b << ":" << n; if (n) any = true; }
        std::cout << (any ? " SURVIVOR\n" : " NONE\n");
        ++tested; if (any) ++with_survivor;
    }
    std::cout << "SUMMARY p=19 nonhomeomorphic homotopy-equivalent pairs=" << tested
              << " pairs with a Massey-compatible module isomorphism=" << with_survivor << "\n";
    return (tested == 32 && with_survivor == 0 && control_homeo.size() == 2 &&
            control_homeo[0].second == 19 && control_homeo[1].second == 19 &&
            control_11.size() == 2 && control_11[0].second == 0 && control_11[1].second == 0 &&
            control_7.size() == 2 && control_7[0].second == 0 && control_7[1].second == 0) ? 0 : 1;
}
