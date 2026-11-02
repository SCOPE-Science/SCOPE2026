#!/usr/bin/env python3
"""Exact rational verification of a divisor-set GCD/LCM denominator formula.

Run: python3 verify.py
Uses only Python's standard library; no external network or data files.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divs(n):
    ds = [1]
    for p, a in factor(n).items():
        ds = [d * (p**k) for d in ds for k in range(a + 1)]
    return sorted(ds)


def theoretical(n, removed_primes, e):
    f = factor(n)
    primes = tuple(removed_primes)
    if not primes or len(f) == 1:
        return 1
    if len(f) == 2 and all(a == 1 for a in f.values()) and len(primes) == 2:
        return 1
    d = {p: (p**e if f[p] >= 2 else p**e - 1) for p in primes}
    D = lcm(*d.values())
    T = D + sum(D // dp for dp in d.values())
    gens = [(D // d[p] if f[p] >= 2 else p**e * (D // d[p])) for p in primes]
    return T // gcd(T, *gens)


def direct(n, removed_primes, e):
    omit = {n // p for p in removed_primes}
    S = [d for d in divs(n) if d not in omit]
    k = len(S)
    # In-place exact Gauss-Jordan elimination of G * Q = L, with rational arithmetic.
    A = [[Fraction(gcd(a, b) ** e) for b in S] +
         [Fraction(lcm(a, b) ** e) for b in S] for a in S]
    for j in range(k):
        pivot = next(i for i in range(j, k) if A[i][j])
        A[j], A[pivot] = A[pivot], A[j]
        d = A[j][j]
        A[j] = [z / d for z in A[j]]
        for i in range(k):
            if i != j and A[i][j]:
                c = A[i][j]
                A[i] = [x - c * y for x, y in zip(A[i], A[j])]
    Q = [row[k:] for row in A]
    den = lcm(*(v.denominator for row in Q for v in row))
    return den, S, Q


def jordan(n, e):
    r = n**e
    for p in factor(n):
        r = r // (p**e) * (p**e - 1)
    return r


def F(d, y, e):
    # Independent divisor-Mobius convolution, by enumerating every divisor.
    factors = factor(d)
    total = 0
    for t in divs(d):
        h = d // t
        if any(a > 1 for a in factor(h).values()):
            continue
        mu = -1 if len(factor(h)) % 2 else 1
        total += mu * lcm(t, y)**e
    return total


def run():
    cases = 0
    coatom_row_cases = 0
    nontrivial = 0
    examples = {}
    for n in range(2, 100):
        if len(divs(n)) > 18:
            continue
        ps = tuple(factor(n))
        for count in range(len(ps) + 1):
            for subset in combinations(ps, count):
                for e in (1, 2, 3):
                    observed, S, Q = direct(n, subset, e)
                    expected = theoretical(n, subset, e)
                    assert observed == expected, (n, subset, e, observed, expected)
                    if observed > 1:
                        nontrivial += 1
                    if len(ps) >= 2:
                        delta = jordan(n, e) + sum(jordan(n // p, e) for p in subset)
                        for j, y in enumerate(S):
                            numerator = F(n, y, e) + sum(F(n // p, y, e) for p in subset)
                            assert Q[-1][j] == Fraction(numerator, delta), (n, subset, e, y)
                            coatom_row_cases += 1
                    cases += 1
                    if (n, subset, e) in [
                        (12, (2,), 1), (12, (2,), 2),
                        (30, (2, 3), 1), (30, (2, 3, 5), 1),
                        (60, (2,), 1), (60, (3,), 1),
                        (6, (2, 3), 2),
                    ]:
                        examples[str((n, subset, e))] = observed
    print('VERIFY_OK', 'matrix_cases=', cases,
          'nonintegral_cases=', nontrivial,
          'mobius_row_entries=', coatom_row_cases,
          'examples=', examples)

if __name__ == '__main__':
    run()
