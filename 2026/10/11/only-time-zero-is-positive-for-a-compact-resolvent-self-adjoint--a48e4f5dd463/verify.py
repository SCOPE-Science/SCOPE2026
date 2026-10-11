#!/usr/bin/env python3
"""Checks rational estimates and selected sign inequalities for an explicit semigroup.

The infinite-dimensional and all-real-time theorem requires the analytic proof
in RESULT.md; a finite calculation does not replace those arguments.
"""
from fractions import Fraction
from math import ceil, exp, factorial, log

r = Fraction(1, 20)
series_majorant = r * (1 + r) / (1 - r)**3
assert series_majorant == Fraction(420, 6859)
assert 1 + 2 * series_majorant < 2
# Taylor's series proves exp(3)>20, hence exp(-3)<1/20.
assert sum((Fraction(3)**k / factorial(k) for k in range(9)), Fraction(0)) > 20
# A polynomial Taylor bound proves exp(n)>4n for all n>=3:
# p(n)=1+n+n^2/2+n^3/6-4n has p(3)>0 and p'(n)>0.
def p(n):
    return 1 + n + Fraction(n*n,2) + Fraction(n*n*n,6) - 4*n
def dp(n):
    return -3 + n + Fraction(n*n,2)
assert p(3)>0 and dp(3)>0
# Check some exact rational t,n inequalities for the analytical cutoff.
for t in [Fraction(1,10), Fraction(1,2), Fraction(1), Fraction(7,4), Fraction(5), Fraction(101,3)]:
    n = ceil(t+3)
    assert n>=3 and n*(n-t)>=3*n
    assert n>t
    # Left side of the crucial exponent comparison exceeds 2t+log(4n).
    # Decimal check here only; the theorem uses exp(n)>4n analytically.
    assert float(n*(n-t)-2*t) > log(4*n)
    assert n*n-n*t>=3*n>2*t
print('NOWHERE_POSITIVE_SEMIGROUP_RATIONAL_BOUNDS_AND_CUTOFF_OK')
