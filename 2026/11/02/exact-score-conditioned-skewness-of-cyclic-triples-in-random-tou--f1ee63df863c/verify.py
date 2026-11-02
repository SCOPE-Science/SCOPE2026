#!/usr/bin/env python3
"""Exact independent enumeration of conditional cyclic-triad moments.

No external packages required.  Edge signs are enumerated directly and cyclic
three-vertex sets are counted from their three observed orientations.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def prediction(n, d):
    m = n - 1
    q = d * (m - d)
    N = comb(m, 3) if m >= 3 else 0
    mu = Fraction(N, 4) + Fraction(q, 2)
    var = Fraction(3 * N, 16) + Fraction(q, 4)
    third = Fraction(3 * (4-m) * N, 32) - Fraction(3 * q * (m-2), 16)
    return mu, var, third


def enumerate_law(n, d):
    m = n - 1
    edges = tuple(combinations(range(m), 2))
    triples = tuple(combinations(range(m), 3))
    hist = Counter()
    # Relabeling symmetry permits fixing the outneighborhood of the marked
    # vertex to {0,...,d-1}.  Every remaining orientation is independent.
    for mask in range(1 << len(edges)):
        sign = [[0] * m for _ in range(m)]
        for e, (i, j) in enumerate(edges):
            sign[i][j] = 1 if mask & (1 << e) else -1
            sign[j][i] = -sign[i][j]
        count = sum(sign[i][j] == sign[j][k] == sign[k][i]
                    for i, j, k in triples)
        count += sum(sign[i][j] == 1
                     for i in range(d) for j in range(d, m))
        hist[count] += 1
    return hist


def main():
    total_laws = 0
    for n in range(3, 8):
        for d in range(n):
            hist = enumerate_law(n, d)
            total_laws += 1
            size = sum(hist.values())
            check(size == 1 << comb(n-1, 2), f"mass {n} {d}")
            check(all(k >= 0 and c > 0 for k, c in hist.items()),
                  f"support {n} {d}")
            mean = sum((Fraction(k*c, size) for k, c in hist.items()),
                       Fraction())
            var = sum((Fraction((k-mean)**2*c, size)
                       for k, c in hist.items()), Fraction())
            third = sum((Fraction((k-mean)**3*c, size)
                         for k, c in hist.items()), Fraction())
            mu0, var0, third0 = prediction(n,d)
            check(mean == mu0, f"mean {n} {d}: {mean}!={mu0}")
            check(var == var0, f"variance {n} {d}: {var}!={var0}")
            check(third == third0, f"third {n} {d}: {third}!={third0}")
            if n >= 6:
                check(third < 0, f"sign {n} {d}")
            elif n == 5:
                check((third < 0) == (0 < d < n-1), f"sign {n} {d}")
            elif n == 4:
                check((third > 0) == (d in (0,n-1)), f"sign {n} {d}")
    # Independent exact rational inequality for the maximum skewness
    # after differentiating its squared normalized magnitude with respect
    # to q=d(m-d), for all relevant integer parameters.
    for m in range(4, 301):
        N = comb(m,3)
        A = Fraction(3*(m-4)*N, 32)
        B = Fraction(3*(m-2), 16)
        v0 = Fraction(3*N, 16)
        qcritical = 8*v0 - Fraction(3*A, B)
        check(qcritical == Fraction(m*(m-1),2), f"critical {m}")
        check(Fraction(m*m,4) < qcritical, f"domain {m}")
        for d in range(m):
            q=d*(m-d)
            derivator = B*(v0+Fraction(q,4)) - Fraction(3,8)*(A+B*q)
            check(derivator>0, f"skew derivative {m} {d}")
    print(f"PASS: {ASSERTIONS} exact assertions; {total_laws} exhaustive conditional laws (n=3..7); analytic parameter inequalities through m=300.")


if __name__ == '__main__':
    main()
