"""Finite reproducibility checks of the tower-height shift-correlation formulas.

Usage: python3 tower_height_pair_verifier.py
Uses only the Python standard library. Finite tests supplement, not replace, proofs.
"""
from fractions import Fraction
from math import isclose


def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, int(limit ** .5) + 1):
        if spf[p] == p:
            for j in range(p * p, limit + 1, p):
                if spf[j] == j:
                    spf[j] = p
    return spf


def heights(limit, spf):
    h = [0] * (limit + 1)
    for n in range(2, limit + 1):
        m = n
        maximum = 0
        while m > 1:
            p = spf[m]
            a = 0
            while m % p == 0:
                m //= p
                a += 1
            maximum = max(maximum, h[a])
        h[n] = 1 + maximum
    return h


def local_model(p, forbidden, r):
    q = lambda a: Fraction(p - 1, p ** (a + 1))
    beta = sum((q(a) for a in forbidden), Fraction(0))
    gamma = sum((q(a) for a in forbidden if a < r), Fraction(0))
    if r in forbidden:
        gamma += q(r) * Fraction(p - 2, p - 1)
        gamma += 2 * sum((q(a) for a in forbidden if a > r), Fraction(0))
    return beta, gamma, 1 - 2 * beta + gamma


def valuation_mod(n, p, L):
    a = 0
    while a < L and n % p == 0:
        a += 1
        n //= p
    return a


def local_exact_tests(h):
    checks = 0
    for k in (1, 2):
        for p, L in ((2, 13), (3, 9)):
            modulus = p ** L
            forbidden = frozenset(a for a in range(1, L) if h[a] >= k)
            for r in (0, 1, 2, 3, 4, 5):
                t = p ** r
                both_bad = sum(
                    valuation_mod(n, p, L) in forbidden
                    and valuation_mod((n + t) % modulus, p, L) in forbidden
                    for n in range(modulus)
                )
                _, model_gamma, _ = local_model(p, forbidden, r)
                assert abs(Fraction(both_bad, modulus) - model_gamma) <= Fraction(2, modulus), (k, p, r)
                checks += 1
    print(f"LOCAL_EXACT_CHECKS={checks}")


def product_test(h, spf):
    limit = len(h) - 1
    primes = [p for p in range(2, 1001) if spf[p] == p]
    tested = 0
    for k in (1, 2):
        forbidden = frozenset(a for a in range(1, 25) if h[a] >= k)
        for t in (1, 2, 4, 8, 16, 32, 81):
            pred = 1.0
            for p in primes:
                r = 0
                z = t
                while z % p == 0:
                    r += 1
                    z //= p
                _, _, good = local_model(p, forbidden, r)
                pred *= float(good)
            count = sum(h[n] <= k and h[n + t] <= k for n in range(1, limit - t))
            freq = count / (limit - t - 1)
            assert abs(freq - pred) < 0.012, (k, t, freq, pred)
            tested += 1
    print(f"FINITE_PAIR_COMPARISONS={tested}")


def minimum_exponent_test(h):
    for k, expected in ((1, 2), (2, 4), (3, 16)):
        assert min(a for a in range(2, 500) if h[a] >= k) == expected
    print("MINIMUM_FORBIDDEN_EXPONENT_CHECKS=3")


def main():
    limit = 100010
    spf = smallest_prime_factors(limit)
    h = heights(limit, spf)
    minimum_exponent_test(h)
    local_exact_tests(h)
    product_test(h, spf)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
