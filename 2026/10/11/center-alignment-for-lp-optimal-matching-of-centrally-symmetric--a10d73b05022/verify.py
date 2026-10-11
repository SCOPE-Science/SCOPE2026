#!/usr/bin/env python3
import math

def defect(r, s, p):
    return abs(r+s)**p + abs(r-s)**p - 2*abs(r)**p

# Deterministic strict-convexity regression checks.
ps = (2.25, 2.5, 3.0, 4.0, 6.75)
rs = (-3.0, -1.25, -0.1, 0.0, 0.4, 2.0)
ss = (-1.5, -0.25, 0.0, 0.3, 1.2)
for p in ps:
    for r in rs:
        for s in ss:
            d = defect(r, s, p)
            assert d >= -1e-12, (p, r, s, d)
            if s != 0.0:
                assert d > 1e-14, (p, r, s, d)

# Exact p=4 identity on an integer grid.
for r in range(-7, 8):
    for s in range(-7, 8):
        lhs = (r+s)**4 + (r-s)**4 - 2*r**4
        rhs = 12*r*r*s*s + 2*s**4
        assert lhs == rhs
        if s:
            assert lhs > 0

# Circular quadrature for an even g(theta); translation mode is z dot u.
N = 200000
p = 3.5
def energy(z1, z2):
    total = 0.0
    for k in range(N):
        th = 2*math.pi*(k+0.5)/N
        c, s = math.cos(th), math.sin(th)
        g = 0.7 + 0.31*math.cos(2*th) - 0.11*math.cos(4*th)
        total += abs(g + z1*c + z2*s)**p
    return total/N

e0 = energy(0.0, 0.0)
for z in ((0.1,0.0), (0.0,-0.2), (0.3,0.4), (-0.8,0.15)):
    ez = energy(*z)
    assert ez > e0 + 1e-8, (z, e0, ez)

print("VERIFY_OK")
print("paired_strict_convexity = passed")
print("quartic_identity = exact")
print("antipodal_quadrature = passed")
