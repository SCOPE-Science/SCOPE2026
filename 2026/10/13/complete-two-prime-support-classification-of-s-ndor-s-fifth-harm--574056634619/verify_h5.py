#!/usr/bin/env python3
"""Exact finite checks for the two-prime fifth harmonic quotient classification."""

from math import isqrt, prod


def sigma_bi_prime_power(p: int, a: int) -> int:
    assert p >= 2 and a >= 1
    total = sum(p ** j for j in range(a + 1))
    return total - (p ** (a // 2) if a % 2 == 0 else 0)


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for z in range(p * p, limit + 1, p):
                if spf[z] == z:
                    spf[z] = p
    return spf


def factors(n: int, spf: list[int]):
    pairs = []
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            n //= p
            a += 1
        pairs.append((p, a))
    return pairs


def run(limit: int = 1000000) -> None:
    spf = smallest_prime_factors(limit)
    qualifying = []
    support_hist = [0, 0, 0]
    for n in range(1, limit + 1):
        fs = factors(n, spf)
        if len(fs) > 2:
            continue
        support_hist[len(fs)] += 1
        assert n == prod(p ** a for p, a in fs)
        den = prod(sigma_bi_prime_power(p,a) for p,a in fs)
        if (n * (1 << len(fs))) % den == 0:
            qualifying.append(n)
    assert qualifying == [1, 6, 45], qualifying
    assert 4 * 45 // (sigma_bi_prime_power(3, 2)*sigma_bi_prime_power(5, 1)) == 3
    assert 4 * 6 // (sigma_bi_prime_power(2, 1)*sigma_bi_prime_power(3, 1)) == 2
    # Prime-power formula and dyadic obstruction are checked on many exponents.
    tests = 0
    for p in [3,5,7,11,13,17,19,23,29,31,37,41]:
        for a in range(2, 101):
            B=sigma_bi_prime_power(p,a)
            assert B & (B-1) != 0, (p,a)
            tests += 1
    print(f"VERIFY_OK limit={limit} support_hist={support_hist} qualifying={qualifying} odd_prime_exponent_tests={tests}")


if __name__ == '__main__':
    run()
