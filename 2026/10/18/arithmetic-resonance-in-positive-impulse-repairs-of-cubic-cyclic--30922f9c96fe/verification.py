#!/usr/bin/env python3
"""Finite checks of the stated cyclic cubic-window formulas.

Numerical comparisons corroborate, but do not prove, the universal theorem.
Requires only the Python standard library.
"""
import cmath
import math


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def quadratic_character(x, p):
    return 1 if pow(x % p, (p - 1) // 2, p) == 1 else -1


def phase_root(p, n):
    return cmath.exp(2j * math.pi * (n % p) / p)


def positive_resonances(p):
    if p % 4 == 3:
        return []
    i = next(k for k in range(1, p) if (k * k) % p == p - 1)
    inv2 = pow(2, -1, p)
    rows = []
    for a in range(1, p):
        for b in sorted({(3 * i * a * a) % p, (-3 * i * a * a) % p}):
            r = a * b * inv2 % p
            positive_cosine = 4 * r < p or 4 * r > 3 * p
            ch = quadratic_character(-3 * a, p)
            if ch * (1 if positive_cosine else -1) < 0:
                c = math.cos(2 * math.pi * r / p)
                rows.append((a, b, math.sqrt(p) / (2 * abs(c))))
    return rows


def direct_ambiguity(p, t, a, b):
    w = [phase_root(p, pow(j, 3, p)) + (t if j == 0 else 0) for j in range(p)]
    return sum(w[(j - a) % p] * w[j].conjugate() * phase_root(p, b * j) for j in range(p))


def gauss_formula(p, t, a, b):
    if a == 0:
        return p + 2 * t + t * t if b == 0 else 2 * t + t * t
    A = -3 * a
    B = 3 * a * a + b
    inv = pow((12 * a) % p, -1, p)
    chi = quadratic_character(A, p)
    eps = 1 if p % 4 == 1 else 1j
    s = (eps * chi * math.sqrt(p) * phase_root(p, B * B * inv)
         + t * (1 + phase_root(p, a * b)))
    return phase_root(p, -a * a * a) * s


def main():
    comparisons = 0
    checks = [(5, 0.125), (7, 0.125), (11, 1.0), (13, 0.75),
              (17, 1.0), (19, 1.5), (23, 0.5), (29, 1.0), (37, 2.0)]
    assert all(prime(p) for p, _ in checks)
    assert len(positive_resonances(5)) == 0
    assert len(positive_resonances(13)) == 0
    assert len(positive_resonances(17)) == 8
    for p, t in checks:
        for a in range(p):
            for b in range(p):
                z = direct_ambiguity(p, t, a, b)
                expected = gauss_formula(p, t, a, b)
                assert abs(z - expected) < 1e-7 * (1 + abs(expected)), (p, t, a, b, z, expected)
                assert abs(z) > 1e-6, (p, t, a, b)
                comparisons += 1
        for a, b, tr in positive_resonances(p)[:8]:
            assert abs(direct_ambiguity(p, tr, a, b)) < 1e-7, (p, a, b, tr)
            comparisons += 1
    p = 17
    candidates = positive_resonances(p)
    unique_tr = sorted(set(round(t, 9) for _, _, t in candidates))
    assert len(unique_tr) == 2
    for t in unique_tr:
        direct_zeros = {(a, b) for a in range(p) for b in range(p)
                        if abs(direct_ambiguity(p, t, a, b)) < 1e-6}
        predicted_zeros = {(a, b) for a, b, z in candidates if abs(z - t) < 1e-6}
        assert direct_zeros == predicted_zeros
        assert len(direct_zeros) == 4
        comparisons += p * p
    print('VERIFY_OK', comparisons, 'finite comparisons; p=5,7,11,13,17,19,23,29,37;',
          'p=17 has two resonant amplitudes, each with four ambiguity zeros')

if __name__ == '__main__':
    main()
