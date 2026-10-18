"""Exact finite-state checks for conditional rare-switch domain-extreme theorem.

The infinite point-process convergence is proved analytically in RESULT.md;
this program only tests independent finite combinatorial identities and the
uniform Bessel comparison used in the proof. Python 3, standard library only.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction


def comp(m, r, cap):
    """Number of positive r-compositions of m with every part <= cap."""
    if r == 0:
        return int(m == 0)
    v = [0] * (m + 1)
    v[0] = 1
    for _ in range(r):
        v2 = [0] * (m + 1)
        for n, count in enumerate(v):
            if count:
                for z in range(1, min(cap, m - n) + 1):
                    v2[n + z] += count
        v = v2
    return v[m]


def types_for(k):
    # k is number of changes; k+1 alternating runs.
    r = k + 1
    if r % 2 == 0:
        return [(r // 2, r // 2), (r // 2, r // 2)]
    return [(r // 2 + 1, r // 2), (r // 2, r // 2 + 1)]


def formula(n, k, threshold):
    m = n // 2
    return sum(comp(m, a, threshold) * comp(m, b, threshold)
               for a, b in types_for(k))


def brute(n):
    counts = Counter()
    for word in itertools.product((0, 1), repeat=n):
        if sum(word) != n // 2:
            continue
        k = sum(x != y for x, y in zip(word[:-1], word[1:]))
        cur = 1
        mx = 1
        for x, y in zip(word[:-1], word[1:]):
            if x == y:
                cur += 1
            else:
                mx = max(mx, cur)
                cur = 1
        mx = max(mx, cur)
        counts[k, mx] += 1
    return counts


def bessel_F(x):
    # Direct positive-coefficient series; no numerical libraries.
    i0 = 1.0
    i1 = 0.0
    term0 = 1.0
    term1 = x
    for j in range(1, 500):
        term0 *= x * x / (j * j)
        i0 += term0
        if j == 1:
            i1 += term1
        else:
            term1 *= x * x / ((j - 1) * j)
            i1 += term1
        if max(abs(term0), abs(term1)) < 1e-14 * max(i0, i1):
            break
    return 2 * x * (i0 + i1)


def Bessel_exact_S(n, u):
    m = n // 2
    total = 0.0
    for k in range(1, n):
        counts = 0
        for a,b in types_for(k):
            if a <= m and b <= m:
                counts += math.comb(m - 1, a - 1) * math.comb(m - 1, b - 1)
        total += counts * (u ** k)
    return total


def run():
    tests = 0
    for n in (2, 4, 6, 8, 10, 12, 14):
        bc = brute(n)
        for k in range(1, n):
            for th in range(1, n // 2 + 1):
                lhs = sum(v for (kk, maximum), v in bc.items()
                          if kk == k and maximum <= th)
                rhs = formula(n, k, th)
                assert lhs == rhs, (n, k, th, lhs, rhs)
                tests += 1
        for u in (Fraction(1, 9), Fraction(1, 3), Fraction(2, 3)):
            weighted_brute = sum(Fraction(num) * u ** k
                                 for (k, mx), num in bc.items())
            weighted_formula = sum(Fraction(formula(n, k, n // 2)) * u ** k
                                   for k in range(1, n))
            assert weighted_brute == weighted_formula
            tests += 1
    for n in (40, 100, 400):
        m = n // 2
        for x in (0.5, 1.0, 2.0, 3.0):
            u = x / m
            exact = Bessel_exact_S(n, u)
            ratio = m * exact / bessel_F(x)
            assert -1e-10 <= 1 - ratio <= x * (x + 1) / m + 1e-10
            tests += 1
    print(f'PASS: {tests} finite exact/analytic comparison assertions')


if __name__ == '__main__':
    run()
