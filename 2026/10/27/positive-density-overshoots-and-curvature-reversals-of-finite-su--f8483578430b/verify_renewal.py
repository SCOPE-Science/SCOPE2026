"""Exact finite-window sanity checks for renewal oscillation formulas.

Finite checks illustrate, but cannot establish, asymptotic positive density.
The infinite proof uses poles of the renewal generating function.
"""
from fractions import Fraction
from math import gcd
from functools import reduce

LAWS = [
    {1: Fraction(1, 2), 2: Fraction(1, 2)},
    {2: Fraction(2, 5), 3: Fraction(3, 5)},
    {1: Fraction(1, 4), 3: Fraction(1, 2), 4: Fraction(1, 4)},
    {3: Fraction(1, 4), 5: Fraction(1, 2), 6: Fraction(1, 4)},
]

def check_law(p, nmax=180):
    assert sum(p.values()) == 1 and len(p) >= 2
    assert reduce(gcd, p) == 1
    mean = sum(j * q for j, q in p.items())
    target = 1 / mean
    u = [Fraction(1)]
    for n in range(1, nmax + 1):
        u.append(sum((q * u[n - j] for j, q in p.items() if j <= n), Fraction(0)))
    lo = 60
    s_pos = sum(u[n] > target for n in range(lo, nmax + 1))
    s_neg = sum(u[n] < target for n in range(lo, nmax + 1))
    curv = [u[n - 1] * u[n + 1] - u[n] * u[n] for n in range(lo, nmax)]
    t_pos = sum(t > 0 for t in curv)
    t_neg = sum(t < 0 for t in curv)
    assert min(s_pos, s_neg, t_pos, t_neg) > 0
    print(f"support={sorted(p)} mean={mean} n=60..180 "
          f"mass_signs=(+{s_pos},-{s_neg}) "
          f"curvature_signs=(+{t_pos},-{t_neg})")

if __name__ == '__main__':
    for law in LAWS:
        check_law(law)
    print("PASS: all four finite exact-rational examples display both signs.")
