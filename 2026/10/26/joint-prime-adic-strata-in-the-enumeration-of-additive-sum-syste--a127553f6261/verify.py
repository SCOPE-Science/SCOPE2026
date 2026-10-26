#!/usr/bin/env python3
"""Exact finite checks of the marked factorization identity for sum-system counts.

This checks the algebraic coefficient identity in bounded degrees, not the
unbounded Delange asymptotics, which are proved analytically in RESULT.md.
"""
from functools import lru_cache
from math import factorial


def divisors_ge_two(n):
    return [d for d in range(2, n + 1) if n % d == 0]


@lru_cache(None)
def direct_words(n, m, previous=-1, mask=0):
    if n == 1:
        return int(mask == (1 << m) - 1)
    return sum(direct_words(n // d, m, c, mask | (1 << c))
               for d in divisors_ge_two(n)
               for c in range(m) if c != previous)


@lru_cache(None)
def proper_factorizations(n):
    if n == 1:
        return {0: 1}
    ans = {}
    for d in divisors_ge_two(n):
        for length, amount in proper_factorizations(n // d).items():
            ans[length + 1] = ans.get(length + 1, 0) + amount
    return ans


def stirling(n, k):
    a = [0] * (k + 1)
    a[0] = 1
    for i in range(1, n + 1):
        b = [0] * (k + 1)
        for j in range(1, min(i, k) + 1):
            b[j] = j * a[j] + a[j-1]
        a = b
    return a[k]


def valuation(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def convolve(a, b, N):
    c = [0] * (N + 1)
    for i in range(1, N + 1):
        if not a[i]:
            continue
        for j in range(1, N // i + 1):
            if b[j]:
                c[i*j] += a[i] * b[j]
    return c


def main():
    N = 112
    for m in range(2, 5):
        for n in range(1, N + 1):
            expected = sum(factorial(m) * stirling(L - 1, m - 1) * count
                           for L, count in proper_factorizations(n).items() if L >= m)
            observed = direct_words(n, m)
            assert observed == expected, (m, n, observed, expected)
        # Independently expand H_m(T) as a finite Dirichlet polynomial,
        # with T(n)=1 for n>=2 and T(1)=0. All products <=N are exact.
        t = [0] + [0] + [1] * (N - 1)
        power = [0] * (N + 1)
        power[1] = 1
        expansion = [0] * (N + 1)
        for L in range(1, 8):
            power = convolve(power, t, N)
            weight = factorial(m) * stirling(L - 1, m - 1) if L >= m else 0
            for n in range(1, N + 1):
                expansion[n] += weight * power[n]
        for n in range(1, N + 1):
            assert expansion[n] == direct_words(n, m), ('series', m, n)
    # The marking by (u,v) does not alter coefficients: extract each
    # exact 2-,3-adic stratum from the independent series and word counts.
    for m in range(2, 5):
        for e2 in range(4):
            for e3 in range(4):
                a = sum(direct_words(n, m) for n in range(1, N+1)
                        if valuation(n, 2) == e2 and valuation(n, 3) == e3)
                b = sum(expansion[n] for n in range(1, N+1)
                        if valuation(n, 2) == e2 and valuation(n, 3) == e3)
                # Rebuild marked series for each m (avoid previous m's power).
                t = [0, 0] + [1]*(N-1)
                power = [0]*(N+1); power[1] = 1
                b = 0
                for L in range(1, 8):
                    power = convolve(power, t, N)
                    b += factorial(m) * (stirling(L-1, m-1) if L >= m else 0) * sum(
                        power[n] for n in range(1, N+1)
                        if valuation(n,2) == e2 and valuation(n,3) == e3)
                assert a == b, (m, e2, e3, a, b)
    print('VERIFY_OK: independent factorization words and finite Dirichlet series; m=2..4, n<=112, valuations 2 and 3')


if __name__ == '__main__':
    main()
