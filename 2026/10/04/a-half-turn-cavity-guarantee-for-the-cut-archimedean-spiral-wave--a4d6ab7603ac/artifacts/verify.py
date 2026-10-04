#!/usr/bin/env python3
from fractions import Fraction
import math
import mpmath as mp

# Exact Bessel sign certificate at R=481/200.
# J_0(R)=sum_{n>=0} (-1)^n (R^2/4)^n/(n!)^2.
# From n=1 onward magnitudes decrease because y/(n+1)^2 <= y/4 < 1.
R = Fraction(481,200)
y = R*R/Fraction(4,1)
assert y/Fraction(4,1) < 1
S6 = sum((Fraction(-1 if n%2 else 1,1) * y**n / Fraction(math.factorial(n)**2,1) for n in range(7)), Fraction(0,1))
assert S6 < 0  # the remaining alternating tail starts negative, so J_0(R)<S6<0

# Rigorous interval enclosure for the distance from c=(73/100,73/100)
# to gamma(t)=(t cos t/2,t sin t/2), on the slightly larger interval
# [3.1415,7] containing [pi,7]. mpmath.iv performs outward interval arithmetic.
mp.iv.dps = 60
c = mp.iv.mpf(['0.73','0.73'])
Riv = mp.iv.mpf(['2.405','2.405'])
lo = mp.mpf('3.1415')
hi = mp.mpf('7')
N = 1000
step = (hi-lo)/N
min_lower = None
for i in range(N):
    aa = lo + i*step
    bb = lo + (i+1)*step
    t = mp.iv.mpf([aa,bb])
    f = t*t/4 - c*t*(mp.iv.cos(t)+mp.iv.sin(t)) + 2*c*c
    fl = mp.mpf(f.a)
    if min_lower is None or fl < min_lower:
        min_lower = fl
    assert fl > mp.mpf('2.405')**2

# For t>=7, reverse triangle inequality and ||c||<1.033 give
# dist >= t/2-||c|| > 3.5-1.033 = 2.467 > 2.405.
assert Fraction(73*73*2,10000) < Fraction(1033*1033,1000*1000)
assert Fraction(7,2) - Fraction(1033,1000) > R

print('VERIFY_OK R=481/200 S6_negative=1 interval_boxes=1000 min_distance_sq_lower=%s radial_tail=1' % mp.nstr(min_lower,18))
