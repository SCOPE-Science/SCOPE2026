#!/usr/bin/env python3
"""Exact arithmetic identity checks and finite torus-covering diagnostics.
No finite test is asserted to prove optimality or exhaust a continuum.
"""
from fractions import Fraction as F
from math import sqrt


def circle_dist(a, b, period):
    u = abs((a-b) % period)
    return min(u, period-u)


def torus_distance2(p, q, A, B):
    return circle_dist(p[0], q[0], A)**2 + circle_dist(p[1], q[1], B)**2


def covering_radius_grid2(p, A, B, n=120):
    other = ((p[0] + A/2) % A, (p[1] + B/2) % B)
    return max(min(torus_distance2(p, (A*i/n, B*j/n), A, B),
                   torus_distance2(other, (A*i/n, B*j/n), A, B))
               for i in range(n) for j in range(n))


cases = [(F(1), F(1)), (F(6,5),F(1)), (F(3,2),F(1)),
         (F(2),F(1)),(F(3),F(1)),(F(5),F(2)),(F(5),F(1))]
for A,B in cases:
    assert A >= B > 0
    R = (A*A+B*B)/(4*A)
    t = (A*A-B*B)/(4*A)
    # The circumcenter (t,B/2) equidistant from three triangulation vertices.
    vertices = ((F(0),F(0)),(F(0),B),(A/2,B/2))
    assert all((t-x)**2+(B/2-y)**2==R*R for x,y in vertices)
    # The point is a farthest torus target for the antipodal half-diagonal pair.
    sites = ((F(0),F(0)),(A/2,B/2))
    assert all(torus_distance2(site,(t,B/2),A,B)==R*R for site in sites)
    assert R>=B/2 and R<=A/2
    assert t == A/2-R
    # The critical horizontal-fiber tangency equality.
    assert R*R - B*B/4 == t*t
    # Independent finite grid: all sample points within proved radius.
    grid_radius2 = covering_radius_grid2((F(0),F(0)),A,B,n=80)
    assert grid_radius2<=R*R
    # A displaced second point yields at least one explicit farther target.
    # Computations not needed for theorem, just perturbation illustration.
    print(f'A={A}, B={B}, optimum_radius={R}, grid_radius={sqrt(float(grid_radius2)):.9f}')
print('VERIFY_OK')
