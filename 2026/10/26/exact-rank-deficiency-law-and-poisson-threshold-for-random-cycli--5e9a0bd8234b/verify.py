"""Exact independent checks for the cyclic two-actuator reachability theorem.

Uses only Python's standard library. Run: python cyclic_schedule_verify.py
The analytic all-dimension theorem does not rely on these finite tests.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, exp


def poly_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_power(a, k):
    result = [Fraction(1)]
    while k:
        if k & 1:
            result = poly_mul(result, a)
        a = poly_mul(a, a)
        k //= 2
    return result


def rank_deficiency_pgf(n, r, q):
    assert n >= 2 and 1 <= r < n and q >= 1
    p = Fraction(1, 4 ** q)
    d = n // gcd(n, r)
    g = gcd(n, r)
    # R_0(t)=2, R_1(t)=1, R_d=R_{d-1}+t R_{d-2}
    # t=p(z-1); R_d is the independence polynomial of a cycle.
    u, v = [Fraction(2)], [Fraction(1)]
    for _ in range(2, d + 1):
        u, v = v, poly_add(v, poly_mul([-p, p], u))
    return poly_power(v, g)


def direct_histogram(n, r, q):
    h = n * q
    hist = Counter()
    for choices in product((0, 1), repeat=h):
        active_coordinates = {
            (h - 1 - k + r * choices[k]) % n for k in range(h)
        }
        hist[n - len(active_coordinates)] += 1
    return hist


cases = 0
for n in range(2, 10):
    for r in range(1, n):
        for q in (1, 2, 3):
            if q * n > 17:
                continue
            g = rank_deficiency_pgf(n, r, q)
            empirical = direct_histogram(n, r, q)
            denominator = 2 ** (q * n)
            assert sum(g) == 1, (n, r, q, g)
            for deficiency in range(n + 1):
                assert Fraction(empirical[deficiency], denominator) == (
                    g[deficiency] if deficiency < len(g) else Fraction(0)
                ), (n, r, q, deficiency)
            if q == 1:
                assert empirical[0] == 2 ** gcd(n, r)
            cases += 1

# The exact probability is computed two distinct ways: with the polynomial
# recurrence and the radical root formula.
for n, r, q in [(6, 2, 2), (12, 5, 3), (21, 7, 2), (40, 19, 4)]:
    g = rank_deficiency_pgf(n, r, q)
    p = 4.0 ** (-q)
    d = n // gcd(n, r)
    discriminant = (1 - 4*p) ** 0.5
    rp = (1 + discriminant) / 2
    rm = (1 - discriminant) / 2
    radical = (rp**d + rm**d) ** gcd(n, r)
    assert abs(float(g[0]) - radical) < 1e-12

# Lattice-subsequence Poisson critical window, n=4^k and q=k:
critical = []
for k in range(3, 8):
    n = 4 ** k
    q = k
    p = 4.0 ** (-q)
    a = (1 + (1-4*p)**0.5)/2
    b = (1 - (1-4*p)**0.5)/2
    prob_coprime = a**n + b**n
    prob_antipodal = (1 - 2*p)**(n//2)
    critical.append((n, prob_coprime, prob_antipodal))
assert abs(critical[-1][1] - exp(-1)) < 0.001
assert abs(critical[-1][2] - exp(-1)) < 0.001
print('VERIFY_OK exact rank-deficiency distributions for', cases,
      'independent enumeration cases; critical probabilities', critical[-1])
