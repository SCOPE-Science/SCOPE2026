"""Reproducible finite checks for the folded-Skellam dispersion threshold.

The mathematical uniqueness proof uses strict modified-Bessel Turan inequalities,
not finite enumeration.  All endpoint enclosures below use rational arithmetic.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import factorial


def exp_enclosure(t, n=35):
    assert isinstance(t, Fraction) and t > 0 and n > t
    term = Fraction(1)
    total = term
    for j in range(1, n):
        term *= t / j
        total += term
    first_omitted = term * t / n
    q = t / (n + 1)
    assert q < 1
    return total, total + first_omitted / (1 - q)


def bessel_enclosure(t, nu, n=35):
    assert isinstance(t, Fraction) and t > 0 and nu in (0, 1)
    q = t / 2
    term = q**nu / factorial(nu)
    total = term
    for j in range(1, n):
        term *= q*q / (j*(j+nu))
        total += term
    first_omitted = term * q*q / (n*(n+nu))
    ratio = q*q / ((n+1)*(n+nu+1))
    assert ratio < 1
    return total, total + first_omitted / (1-ratio)


def h_enclosure(t):
    b0 = bessel_enclosure(t, 0)
    b1 = bessel_enclosure(t, 1)
    exp = exp_enclosure(t)
    r_lo = (b0[0] + b1[0]) / exp[1]
    r_hi = (b0[1] + b1[1]) / exp[0]
    return r_lo + t*r_lo*r_lo, r_hi + t*r_hi*r_hi


for t, expected in ((Fraction(17389, 5000), 1), (Fraction(1739, 500), -1)):
    lo, hi = h_enclosure(t)
    assert (lo > 1) if expected > 0 else (hi < 1)
    print('t=', float(t), 'H(t)-1 interval', float(lo-1), float(hi-1),
          'certified sign', expected)

# The defining Bessel formula for E|X-Y| is compared with an independent
# truncated Poisson double sum.  The omitted Poisson tails are tiny for
# the test inputs; these checks are illustrative and not the theorem proof.
with localcontext() as ctx:
    ctx.prec = 64
    for L in ('0.5', '1', '2', '3'):
        lam = Decimal(L)
        p = [(-lam).exp()]
        for i in range(1, 100):
            p.append(p[-1]*lam/Decimal(i))
        direct = sum(Decimal(abs(i-j))*p[i]*p[j]
                     for i in range(len(p)) for j in range(len(p)))
        t = lam*2
        q = t/2
        i0 = sum(q**(2*j)/(Decimal(factorial(j))**2) for j in range(80))
        i1 = sum(q**(2*j+1)/(Decimal(factorial(j))*Decimal(factorial(j+1)))
                 for j in range(80))
        closed = t*(-t).exp()*(i0+i1)
        assert abs(direct-closed) < Decimal('1e-48')
        print('lambda=', L, 'mean range=', str(+closed), 'independent PMF check passed')
print('All rational and independent finite checks passed.')
