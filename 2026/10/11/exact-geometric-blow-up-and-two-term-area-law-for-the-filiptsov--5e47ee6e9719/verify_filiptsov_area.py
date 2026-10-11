#!/usr/bin/env python3
"""Rational coefficient and numerical quadrature diagnostics for an invariant oval."""
from fractions import Fraction as F
from math import sqrt


def conv(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x*y
    return r


def integ(p, u=F(3, 2)):
    return sum((v*u**(i+1)/F(i+1) for i, v in enumerate(p)), F(0))

# h_0=3z-2z^2, partial_a h at 0=3z-3
h0, h1 = [F(0),F(3),F(-2)], [F(-3),F(3)]
z2 = [F(0),F(0),F(1)]
i00 = integ(conv(z2,conv(h0,h0)))
i01 = integ(conv(z2,conv(h0,h1)))
c0 = F(2,9)*i00
c1 = F(2,9)*(2*i01-2*i00)
assert c0 == F(81,560), (c0, F(81,560))
assert c1 == -F(81,280), c1

# Max of X0 occurs at z=1; max of z X0 at z=9/8.
assert F(2,3)*F(1)**2*(3-2*F(1)) == F(2,3)
ymax = F(2,3)*F(9,8)**3*(3-2*F(9,8))
assert ymax == F(729,1024)


def scaled_area(a, n=30000):
    assert 0 < a < F(3,13) and n%2 == 0
    a=float(a)
    s=1+a
    root=sqrt(3*s*(3-13*a))
    zlo=(3*s-root)/4
    zhi=(3*s+root)/4
    dz=(zhi-zlo)/n
    def f(j):
        z=zlo+j*dz
        h=3*s*z-2*z*z-3*s*a
        # Stable discriminant factorization avoids endpoint cancellation.
        disc=max(0.,2*(z-zlo)*(zhi-z)*(h+3*s*a))
        return z*z*h*sqrt(disc)
    su=f(0)+f(n)
    for j in range(1,n):
        su+=(4 if j%2 else 2)*f(j)
    return (2/(9*s*s))*(dz/3)*su

for a in (0.02,0.01,0.005):
    measured=scaled_area(a)
    approx=float(c0+c1*F(str(a)))
    assert abs(measured-approx) < 3*a*a, (a,measured,approx)
print('CHECK_OK')
