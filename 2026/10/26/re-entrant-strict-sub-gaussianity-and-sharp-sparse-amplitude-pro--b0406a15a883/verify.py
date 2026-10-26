"""Finite consistency checks for the four-point Gaussian proxy theorem.

Run with Python 3. No numerical output constitutes an infinite-domain proof.
"""
from fractions import Fraction
import math


def logcosh(x):
    y = abs(x)
    return y + math.log1p(math.exp(-2*y)) - math.log(2)


def logmgf(a, p, t):
    s = math.log1p(-p) + logcosh(t)
    u = math.log(p) + logcosh(a*t)
    m = max(s, u)
    return m + math.log(math.exp(s-m) + math.exp(u-m))


for a in (4, 5, 10, 100, 1000):
    a_int = int(a)
    p_exact = Fraction(1, 2 * a_int**4)
    variance = 1 + p_exact * (a_int**2-1)
    fourth = 1 + p_exact * (a_int**4-1)
    cumulant = fourth - 3 * variance**2
    assert cumulant < Fraction(-3, 2)
    p = float(p_exact)
    t = float(a)
    witness = logmgf(a, p, t) - float(variance) * t*t/2
    assert witness > 0
    L = math.log(1/p)
    tstar = 2*L/a
    q = 2*logmgf(a, p, tstar)/tstar**2
    analytic_lower = (a*a/(2*L)) * (1-math.log(2)/L)
    assert q + 1e-9 >= analytic_lower
    print('a=',a,'p=',p_exact,'cumulant=',cumulant,
          'witness=',round(witness,5),'proxy evaluation=',round(q,6),
          'leading approximation=',round(a*a/(2*L),6))
print('Finite consistency checks passed; the global proof is analytic.')
