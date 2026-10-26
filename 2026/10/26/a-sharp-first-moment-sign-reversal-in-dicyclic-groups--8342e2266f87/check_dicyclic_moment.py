"""Exact arithmetic check of the first-moment threshold for dicyclic groups.
The proof of the formula and of the infinite tail bound is in RESULT.md.
Python 3 standard library only.
"""
from math import gcd
from fractions import Fraction

def cycle_independent(d):
    if d == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, d + 1):
        a, b = b, a + b
    return b

def first_moment(n):
    assert n >= 2
    m = 2 * n
    ans = -4 * n * 7 ** (n - 1)
    for t in range(m):
        c = gcd(m, t)
        q_missing = cycle_independent(m // c) ** (2 * c)
        h = gcd(m, n - t)
        p_missing = (3 ** (n - (t % 2 == 0))) * cycle_independent(m // h) ** h
        ans += q_missing - p_missing
    return ans

# Exact first moment: negative to n=29 and positive from n=30 to n=79.
for n in range(2, 80):
    val = first_moment(n)
    assert (val < 0) if n < 30 else (val > 0), (n, val)
print("n29",first_moment(29),"n30",first_moment(30))
assert first_moment(30) == 397569666293094423242677920
# At n=80, the normalized lower bound is positive, without rounding.
n = 80
lower = (Fraction(2, 3) - Fraction(1, 3 ** n) + Fraction(1, 9 ** n)
         - (2 * n - 2) * Fraction(25, 27) ** n
         - Fraction(4 * n, 7) * Fraction(7, 9) ** n)
assert lower > 0
# For n >= 80, each negative error term decreases: (2n-2)(25/27)^n,
# (4n/7)(7/9)^n and 3^(-n); the positive 9^(-n) can be dropped.
margin = (Fraction(2, 3) - Fraction(1, 3 ** n)
          - (2 * n - 2) * Fraction(25, 27) ** n
          - Fraction(4 * n, 7) * Fraction(7, 9) ** n)
assert margin > 0
print('EXACT_SIGN_THRESHOLD n=30 order=120')
print('M1_29', first_moment(29), 'M1_30', first_moment(30))
print('FINITE_RANGE_CHECKED 2..79')
print('INFINITE_TAIL_BOUND_POSITIVE_AT 80')
print('SMALL_MOMENTS', [first_moment(n) for n in range(2, 7)])
