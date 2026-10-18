"""Exact finite checks for two-letter Bernoulli pattern-count laws.

Standard-library only. Finite checks support, but do not replace, the
analytic all-length and all-parameter proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, cos, pi


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) +
            (b[i] if i < len(b) else 0) for i in range(n)]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def exact_distribution(n, p, pat):
    q = 1-p
    out = [Fraction(0) for _ in range(n)]
    for word in product((0, 1), repeat=n):
        count = sum(word[i:i+2] == pat for i in range(n-1))
        out[count] += p**sum(word) * q**(n-sum(word))
    return out


def pgf_from_formula(n, p):
    t = p*(1-p)
    ans = [Fraction(0)] * (n//2 + 1)
    for k in range(n//2 + 1):
        scalar = (-t)**k * comb(n-k, k)
        for j in range(k+1):
            ans[j] += scalar * comb(k, j) * (-1)**j
    return ans


checks = 0
for n in range(1, 11):
    for p in (Fraction(1, 7), Fraction(2, 5), Fraction(1, 2),
              Fraction(5, 7)):
        q = 1-p
        laws = {w: exact_distribution(n, p, w) for w in
                ((0, 0), (0, 1), (1, 0), (1, 1))}
        assert laws[(0, 1)] == laws[(1, 0)]
        assert sum(laws[(0, 1)]) == 1
        expected = pgf_from_formula(n, p)
        assert laws[(0, 1)][:len(expected)] == expected
        assert all(x == 0 for x in laws[(0, 1)][len(expected):])
        checks += 3
        if n >= 3:
            dist = laws[(1, 1)]
            d = n-1
            assert dist[d] == p**n
            assert dist[d-1] == 2*p**(n-1)*q
            checks += 2
            if n == 3:
                discriminant = dist[1]**2-4*dist[0]*dist[2]
                assert discriminant == -4*p**3*q and discriminant < 0
                checks += 1
            else:
                assert dist[d-2] == ((n-2)*p**(n-1)*q +
                                     3*p**(n-2)*q**2)
                assert (d-1)*dist[d-1]**2 < 2*d*dist[d]*dist[d-2]
                checks += 2
        if n >= 2:
            # Direct independent factorization check (numerical cosines).
            pis = [4*float(p*q)*cos(j*pi/(n+1))**2
                   for j in range(1, n//2+1)]
            assert all(0 < t < 1 for t in pis)
            out = [1.0]
            for t in pis:
                out = mul(out, [1-t, t])
            assert all(abs(float(a)-b) < 3e-12
                       for a, b in zip(expected, out))
            checks += 2
print('PASS:', checks, 'exact and numerical distribution/property checks')
