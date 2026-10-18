"""Exact rational enclosures for a two-law resetting survival reversal.

Run: python3 verification.py
Uses Python's standard library only. This verifies the four explicit
transcendental inequalities, not the general spectral or convex-order proofs.
"""
from fractions import Fraction as F
from math import factorial

N = 12


def cos_interval_from_square(t):
    """Certified enclosure of cos(sqrt(t)), for 0 <= t <= 1."""
    assert F(0) <= t <= F(1)
    s = sum((-1)**k * t**k / factorial(2*k) for k in range(N+1))
    err = t**(N+1) / factorial(2*N+2)  # alternating remainder
    return (s - err, s + err)


def cosh_interval_from_square(t):
    """Certified enclosure of cosh(sqrt(t)), for 0 <= t <= 3."""
    assert F(0) <= t <= F(3)
    s = sum(t**k / factorial(2*k) for k in range(N+1))
    term = t**(N+1) / factorial(2*N+2)
    ratio = t / ((2*N+3)*(2*N+4))
    assert ratio < 1
    return (s, s + term / (1 - ratio))


def scale(c, k):
    return (k*c[0], k*c[1]) if k>=0 else (k*c[1], k*c[0])


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


def subtract(a,b):
    return (a[0]-b[1],a[1]-b[0])


def floor(q):
    return q.numerator//q.denominator


def dec_band(interval, precision=10):
    v=10**precision
    lo=floor(interval[0]*v)
    hi=-floor(-interval[1]*v)
    return f'[{lo/v:.{precision}f}, {hi/v:.{precision}f}]'


L2=F(79,50)**2
assert L2==F(6241,2500)
cosL=cos_interval_from_square(L2/F(5))
cosmu=cos_interval_from_square(F(1,10))
cosnu=scale(add((F(1),F(1)),cos_interval_from_square(F(1,5))),F(1,2))
# For r=4/5: K>1 iff (4/5)E[cos(Y/sqrt(5))] > cos(L/sqrt(5)).
low_mu=subtract(scale(cosmu,F(4,5)),cosL)
low_nu=subtract(scale(cosnu,F(4,5)),cosL)

chL=cosh_interval_from_square(L2)
chmu=cosh_interval_from_square(F(1,2))
chnu=scale(add((F(1),F(1)),cosh_interval_from_square(F(1))),F(1,2))
# For r=2: K>1 iff cosh(L)>2 E[cosh(Y)].
high_mu=subtract(chL,scale(chmu,2))
high_nu=subtract(chL,scale(chnu,2))

cases=[
 ('r=4/5, concentrated: extinction', low_mu, -1),
 ('r=4/5, dispersed: growth',low_nu,1),
 ('r=2, concentrated: growth',high_mu,1),
 ('r=2, dispersed: extinction',high_nu,-1),
]
for title,bound,sgn in cases:
    assert bound[0] <= bound[1]
    assert bound[1]<0 if sgn<0 else bound[0]>0, (title, bound)
    print(title, dec_band(bound, 12))

# The reset laws are +/-1/sqrt(2) equally, versus 0 with probability
# 1/2 and +/-1 with probability 1/4 each. Their second moments match,
# while the fourth moments differ by exactly 1/4.
assert F(1,2) == (F(1,2)*0 + F(1,4)*1 + F(1,4)*1)
assert F(1,2)**2 == F(1,4)
assert F(1,2)-F(1,4) == F(1,4)
print('CERTIFIED: four strict viability signs, common second moment, fourth-moment difference.')
