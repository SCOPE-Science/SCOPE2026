#!/usr/bin/env python3
"""Finite consistency checks for the analytic convolution threshold theorem.

Requires Python 3 standard library only. These finite tests supplement, but do
not replace, the analytical Herglotz argument and global minimum proof.
"""
import cmath
import math
from fractions import Fraction

for beta in (Fraction(0), Fraction(1, 3), Fraction(1)):
    for n in range(1, 35):
        a = Fraction(2, n + 1)
        h = a * a
        direct = h * (beta + (1-beta)*(n+1))
        integral_moment = 4*((1-beta)/Fraction(n+1) + beta/Fraction((n+1)**2))
        assert direct == integral_moment, (n, beta)

critical = (0.75-math.log(2))/(math.pi**2/12-math.log(2))
assert 0 < critical < 1
boundary = lambda beta: 4*math.log(2)-3+beta*(math.pi**2/3-4*math.log(2))
assert abs(boundary(critical)) < 2e-14
assert boundary(0) < 0 < boundary(1)

f=lambda r: 1-4*(1-math.log1p(r)/r)
lo,hi=0.6,0.9
for _ in range(85):
    mid=(lo+hi)/2
    if f(mid)>0:lo=mid
    else:hi=mid
r=(lo+hi)/2
assert abs(f(r))<3e-15 and abs(r-0.7336009888787581)<2e-14

for t in (0.07,0.27,0.73,0.98):
    s=0.93*t
    left=(-s)/(1+s)
    for theta in (0.0, 0.2, 0.9, 2.1, math.pi):
        z=s*cmath.exp(1j*theta)
        val=(z/(1-z)).real
        assert val+1e-13>=left

# The sharp bounded-turning factor is not covered by either known sufficient
# hypothesis (convexity or Re(g(z)/z)>1/2).
z=-0.95
fstar=-z-2*math.log1p(-z)
f_over_z=fstar/z
convex_test=(1+2*z-z*z)/(1-z*z)
assert f_over_z<0.5 and convex_test<0
print('CHECK_OK: exact convolution coefficients, transition, scalar root, angular ordering, prior-criterion controls')
