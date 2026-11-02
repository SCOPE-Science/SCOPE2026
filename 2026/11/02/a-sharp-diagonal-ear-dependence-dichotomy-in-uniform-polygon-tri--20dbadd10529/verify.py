#!/usr/bin/env python3
"""Exact independent checks for diagonal-conditioned ears in Catalan triangulations.

Requires Python 3 standard library only. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb

ASSERTIONS = 0


def check(condition, description):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(description)


@lru_cache(None)
def catalan(k):
    return comb(2 * k, k) // (k + 1)


def law_from_binomial_moments(moments):
    """If m[k]=E[binom(X,k)], extract P(X=j) from E[z^X]."""
    ans = [Fraction(0)] * len(moments)
    for k, moment in enumerate(moments):
        for j in range(k + 1):
            ans[j] += moment * comb(k, j) * (-1) ** (k - j)
    return ans


def free_ear_law(n):
    """Uniform triangulation of an (n+2)-gon: all polygon ears."""
    N = n + 2
    moments = [Fraction(0)] * (N // 2 + 1)
    for k in range(N // 2 + 1):
        moments[k] = Fraction(
            N * comb(N - k, k) * catalan(n - k),
            (N - k) * catalan(n),
        )
    return law_from_binomial_moments(moments)


def protected_ear_law(a):
    """Uniform triangulation of an (a+2)-gon: ears avoiding two fixed adjacent vertices."""
    moments = [Fraction(0)] * ((a + 1) // 2 + 1)
    for k in range(len(moments)):
        moments[k] = Fraction(comb(a - k + 1, k) * catalan(a - k), catalan(a))
    return law_from_binomial_moments(moments)


def multiply_laws(a, b):
    ans = [Fraction(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            ans[j + k] += x * y
    return ans


@lru_cache(None)
def triangulations(vertices):
    """Independent recursive Catalan enumeration of noncrossing diagonals."""
    m = len(vertices)
    if m == 2:
        return (frozenset(),)
    if m == 3:
        return (frozenset(),)
    answer = []
    v0, ve = vertices[0], vertices[-1]
    for k in range(1, m - 1):
        mid = vertices[k]
        fixed = set()
        if k > 1:
            fixed.add(tuple(sorted((v0, mid))))
        if k < m - 2:
            fixed.add(tuple(sorted((mid, ve))))
        for L, R in product(triangulations(vertices[:k + 1]),
                            triangulations(vertices[k:])):
            answer.append(frozenset(L | R | fixed))
    return tuple(answer)


def is_diagonal(u, v, N):
    d = abs(u - v)
    return 1 < d < N - 1


def count_ears(edges, N):
    return sum(tuple(sorted(((i - 1) % N, (i + 1) % N))) in edges
               for i in range(N))


def law_from_enumeration(tris, N, diagonal=None):
    counts = Counter(count_ears(T, N) for T in tris
                     if diagonal is None or diagonal in T)
    den = sum(counts.values())
    return [Fraction(counts.get(k, 0), den) for k in range(N + 1)]


def padded_equal(a, b):
    return all((a[k] if k < len(a) else 0) ==
               (b[k] if k < len(b) else 0)
               for k in range(max(len(a), len(b))))


def main():
    # Formula normalization and conditional mean, with exact rational arithmetic.
    for n in range(2, 81):
        p = free_ear_law(n)
        check(sum(p) == 1 and all(x >= 0 for x in p), f"unconditioned law n={n}")
        expected = sum(i * v for i, v in enumerate(p))
        check(expected == Fraction((n + 2) * (n + 1), 2 * (2*n - 1)),
              f"mean n={n}")
        for a in range(1, n):
            b = n - a
            cond = multiply_laws(protected_ear_law(a), protected_ear_law(b))
            check(sum(cond) == 1 and all(x >= 0 for x in cond),
                  f"conditional law n={n} a={a}")
            mean = sum(i * v for i, v in enumerate(cond))
            check(mean == Fraction(a * (a + 1), 2*(2*a - 1)) +
                  Fraction(b * (b + 1), 2*(2*b - 1)),
                  f"conditional mean n={n} a={a}")
            delta = mean - expected
            numer = 2*n*n + n - 1 - (n + 7)*a*b
            predicted = Fraction(numer, (2*a-1)*(2*b-1)*(2*n-1))
            check(delta == predicted, f"gap formula n={n} a={a}")
            sign = 0 if numer == 0 else 1 if numer > 0 else -1
            should = (0 if n <= 3 else 1 if min(a,b) == 1 else -1)
            check(sign == should, f"sign classification n={n} a={a}")

    # Independent enumeration in the original sample space (no PGF formula).
    total_triangulations = 0
    for N in range(4, 12):
        tris = triangulations(tuple(range(N)))
        total_triangulations += len(tris)
        check(len(tris) == catalan(N-2), f"Catalan count N={N}")
        check(len(tris) == len(set(tris)), f"duplicate triangulations N={N}")
        check(padded_equal(law_from_enumeration(tris, N), free_ear_law(N-2)),
              f"unconditioned enumerated PGF N={N}")
        n = N-2
        for u in range(N):
            for v in range(u+1, N):
                if not is_diagonal(u, v, N):
                    continue
                edge = (u, v)
                a = v-u-1
                b = n-a
                subset = [T for T in tris if edge in T]
                check(len(subset) == catalan(a)*catalan(b),
                      f"diagonal count N={N}, edge={edge}")
                predicted = multiply_laws(protected_ear_law(a), protected_ear_law(b))
                check(padded_equal(law_from_enumeration(tris, N, edge), predicted),
                      f"conditional enumerated law N={N}, edge={edge}")
    # Octagon (N=8; n=6) diagonal with a=b=3.
    p = free_ear_law(6)
    q = multiply_laws(protected_ear_law(3), protected_ear_law(3))
    check(padded_equal(p, [0, 0, Fraction(16,33), Fraction(16,33), Fraction(1,33)]),
          "octagon unconditional law")
    check(padded_equal(q, [0, 0, Fraction(16,25), Fraction(8,25), Fraction(1,25)]),
          "octagon conditional law")
    check(sum(q[3:]) < sum(p[3:]), "octagon lower tail")
    check(sum(q[4:]) > sum(p[4:]), "octagon upper tail")
    print(f"PASS {ASSERTIONS} exact assertions; {total_triangulations} triangulations explicitly enumerated")


if __name__ == '__main__':
    main()
