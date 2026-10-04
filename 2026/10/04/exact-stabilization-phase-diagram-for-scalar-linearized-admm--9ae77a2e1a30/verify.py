#!/usr/bin/env python3
from fractions import Fraction as F
import math


def td_formula(r, h):
    T = (h*r + 2*h + r*r - r - 1) / ((h+r)*(r+1))
    D = (h-1) / ((h+r)*(r+1))
    return T, D


def matrix_fraction(r, h):
    p = (h-1)/(r+h)
    c = (r-1)/(r+h)
    d = r/(1+r)
    e = 1/(1+r)
    return ((p, c), (d*p, d*c+e))


def trace_det_fraction(M):
    (a,b),(c,d) = M
    return a+d, a*d-b*c

# Exact rational reconstruction checks.
for r,h in [(F(1,2),F(8,5)), (F(4,5),F(9,5)), (F(11,10),F(2,7)),
            (F(3,2),F(1,14)), (F(2,1),F(0,1)), (F(3,1),F(1,1))]:
    T1,D1 = td_formula(r,h)
    T2,D2 = trace_det_fraction(matrix_fraction(r,h))
    assert T1 == T2 and D1 == D2

# Exact one-step multiplier invariant for rational data.
def update(m, rho, eta, x, w, y):
    xn = (rho*w + (eta-m)*x - y)/(rho+eta)
    wn = (y + rho*xn)/(m+rho)
    yn = y - rho*(wn-xn)
    return xn,wn,yn
for vals in [
    (F(2),F(3),F(5),F(7,3),F(-2,5),F(11,7)),
    (F(5),F(2),F(0),F(-3,4),F(9,8),F(-1,6)),
]:
    m,rho,eta,x,w,y = vals
    xn,wn,yn = update(m,rho,eta,x,w,y)
    assert yn == m*wn


def radius(r,h):
    T,D = td_formula(float(r),float(h))
    disc = T*T - 4*D
    if disc >= 0:
        s = math.sqrt(max(0.0,disc))
        return max(abs((T+s)/2), abs((T-s)/2))
    return math.sqrt(D)

phi = (1+math.sqrt(5))/2

def hstar(r):
    if r < 1:
        return (-r*r+r+3-2*math.sqrt(2*(1-r*r)))/r
    if r == 1:
        return None
    if r < phi:
        return (1+r-r*r)/(r+2)
    return 0.0

# Balanced case factors exactly: eigenvalues 1/2 and (h-1)/(h+1).
for h in [F(0), F(1,3), F(1), F(3), F(4)]:
    T,D = td_formula(F(1),h)
    lam1 = F(1,2)
    lam2 = (h-1)/(h+1)
    assert T == lam1+lam2 and D == lam1*lam2
assert abs(radius(1,1/3)-0.5) < 1e-14
assert abs(radius(1,3)-0.5) < 1e-14
assert radius(1,0.3) > 0.5 and radius(1,3.1) > 0.5

# The source majorization value h=1 has the stated closed form.
for r in [0.1,0.5,0.8,1.0,1.1,1.5,2.0,10.0]:
    q = (r*r+1)/(r+1)**2
    assert abs(radius(r,1)-q) < 2e-13

# Closed-form branch checks plus dense deterministic regression around the global minimum.
for r in [0.08,0.2,0.5,0.8,0.99,1.01,1.1,1.4,1.6,phi,2.0,5.0,20.0]:
    hs = hstar(r)
    qs = radius(r,hs)
    # Log/linear grid spanning the relevant nonnegative domain.
    grid = [0.0]
    grid += [i/200 for i in range(1,401)]
    grid += [2.0 + i*0.05 for i in range(1,361)]
    grid += [20.0*(1.08**i) for i in range(1,70)]
    best_grid = min(radius(r,h) for h in grid)
    assert qs <= best_grid + 2e-4
    for eps in [1e-7,1e-5,1e-3,1e-2]:
        if hs-eps >= 0:
            assert qs <= radius(r,hs-eps) + 2e-10
        assert qs <= radius(r,hs+eps) + 2e-10

# Representative strict improvements away from r=1.
for r in [0.2,0.5,0.8,1.1,1.5,2.0,5.0]:
    assert radius(r,hstar(r)) < radius(r,1) - 1e-9

print("VERIFY_OK")
