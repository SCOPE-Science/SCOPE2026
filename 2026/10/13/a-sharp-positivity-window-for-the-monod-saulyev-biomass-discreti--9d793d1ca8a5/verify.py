#!/usr/bin/env python3
"""Exact and bounded numerical checks for the published biomass Saulyev recurrence."""
from fractions import Fraction as F
from math import exp

def coefficients(D, u, dt, dx, M, m, mu, n):
    from math import exp as _exp
    lam = D * dt / (dx * dx)
    gam = u * dt / dx
    if mu == 0:
        b = (1 - lam + (M - m) * dt) / (1 + lam)
    else:
        b = (1 - float(lam) + (float(M) * _exp(float(mu) * n * float(dt)) - float(m)) * float(dt)) / (1 + float(lam))
    return (lam + gam / 2) / (1 + lam), b, (lam - gam / 2) / (1 + lam), 2 * lam / (1 + lam)

D, dt, dx, M, m = F(9, 100), F(1, 100), F(1, 100), F(99, 100), F(2, 5)
lam = D * dt / dx**2
assert lam == 9
for u in [F(1, 20), F(7, 20), F(13, 20)]:
    a, b, c, right = coefficients(D, u, dt, dx, M, m, F(0), 0)
    assert b == F(-79941, 100000)
    assert a >= 0 and c >= 0 and right > 0
    assert a * 27 + b * 100 < F(-54, 1)
    c1 = float(a) * (25 + exp(.01)) + float(b) * 100
    assert c1 < -54

# Rational examples on either side of the two independent sharp barriers.
examples = [
    (F(1), F(1), F(1, 10), F(1), F(0), F(0), True),
    (F(1), F(3), F(1, 10), F(1), F(0), F(0), False),
    (F(1), F(1), F(2), F(1), F(0), F(0), False),
    (F(1), F(1), F(2), F(1), F(3), F(0), True),
    (F(1), F(1), F(2), F(1), F(0), F(3), False),
]
for D0, u0, dt0, dx0, M0, m0, expected in examples:
    a, b, c, right = coefficients(D0, u0, dt0, dx0, M0, m0, F(0), 0)
    criterion = (u0*dx0 <= 2*D0 and dt0*(D0/dx0**2-M0+m0) <= 1)
    assert criterion == (a >= 0 and b >= 0 and c >= 0 and right >= 0)
    assert criterion == expected

# A direct finite-grid propagation test of the sufficiency half, not a substitute for its proof.
D0,u0,dt0,dx0,M0,m0=F(1),F(1),F(1,10),F(1),F(1,5),F(1,10)
a,b,c,right=coefficients(D0,u0,dt0,dx0,M0,m0,F(0),0)
old=[F(1), F(4), F(0), F(5), F(8), F(7)]
for k in range(30):
    new=[F(2)]+[F(0)]*5
    for i in range(1,5):
        new[i]=a*new[i-1]+b*old[i]+c*old[i+1]
    new[5]=right*new[4]+b*old[5]
    assert all(x>=0 for x in new)
    old=new
print('VERIFY_OK')
