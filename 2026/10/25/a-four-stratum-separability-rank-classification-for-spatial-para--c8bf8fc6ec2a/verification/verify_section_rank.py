#!/usr/bin/env python3
"""Direct numerical and exact-arithmetic checks for separable ranks of three-dimensional ellipsoid sections.

Standard library only.  Run: python3 verify_section_rank.py
The finite checks supplement, but do not prove, the universal rank theorem.
"""
from fractions import Fraction as F
from math import pi, sqrt


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def exact_rank(rows):
    a = [[F(v) for v in row] for row in rows]
    i = 0
    for j in range(len(a[0])):
        k = next((k for k in range(i, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        z = a[i][j]
        a[i] = [v/z for v in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                z = a[k][j]
                a[k] = [w-z*v for w, v in zip(a[k], a[i])]
        i += 1
        if i == len(a):
            break
    return i


def orthonormal_frame(u):
    u = tuple(map(float, u))
    if abs(u[2]) > .95:
        e1 = (1.0, 0.0, 0.0)
    else:
        z = sqrt(u[0]**2+u[1]**2)
        e1 = (-u[1]/z, u[0]/z, 0.0)
    e2 = cross(u, e1)
    return e1, e2


def plane_area_direct(diag, c, u, t):
    """Calculate planar ellipse area using a 2x2 Gram matrix, not the section formula."""
    u = tuple(map(float, u))
    c = tuple(map(float, c))
    e, f = orthonormal_frame(u)
    d = [t*u[i]-c[i] for i in range(3)]
    g11 = sum(e[i]*e[i]/diag[i] for i in range(3))
    g22 = sum(f[i]*f[i]/diag[i] for i in range(3))
    g12 = sum(e[i]*f[i]/diag[i] for i in range(3))
    h1 = sum(e[i]*d[i]/diag[i] for i in range(3))
    h2 = sum(f[i]*d[i]/diag[i] for i in range(3))
    s = sum(d[i]*d[i]/diag[i] for i in range(3))
    det = g11*g22-g12*g12
    rho2 = 1-s+(g22*h1*h1-2*g12*h1*h2+g11*h2*h2)/det
    if not rho2 > 0:
        raise AssertionError('test hyperplane misses ellipsoid')
    return pi*rho2/sqrt(det)


def plane_area_closed(diag, c, u, t):
    u = tuple(map(float, u))
    c = tuple(map(float, c))
    q = sum(diag[i]*u[i]*u[i] for i in range(3))
    v = dot(c, u)
    return pi*sqrt(diag[0]*diag[1]*diag[2])*(q-(t-v)**2)/(q**1.5)


U = [tuple(map(F, v)) for v in [
    (1,0,0),(0,1,0),(0,0,1),(-1,0,0),
    (F(3,5),F(4,5),0),(F(-3,5),F(4,5),0),
    (F(3,5),0,F(4,5)),(F(-3,5),0,F(4,5)),
    (0,F(3,5),F(4,5)),(0,F(-3,5),F(4,5)),
    (F(1,3),F(2,3),F(2,3)),(F(-1,3),F(2,3),F(2,3)),
]]

CASES = [
    ('centered ball', (4,4,4), (0,0,0), 1),
    ('centered nonspherical ellipsoid', (9,4,1), (0,0,0), 2),
    ('focal prolate spheroid', (5,1,1), (2,0,0), 2),
    ('translated ball', (4,4,4), (F(1,2),0,0), 3),
    ('off-center triaxial ellipsoid', (5,3,2), (F(1,5),F(1,3),F(1,7)), 3),
]

def run():
    comparisons = 0
    for name, diag0, c0, expected in CASES:
        diag, c = tuple(map(F,diag0)), tuple(map(F,c0))
        rows = []
        for u in U:
            v = dot(u,c)
            q = sum(diag[i]*u[i]*u[i] for i in range(3))
            rows.append((q-v*v, 2*v, -1))
            for t in (-.04,0,.04):
                direct = plane_area_direct(tuple(map(float,diag)),c,u,t)
                closed = plane_area_closed(tuple(map(float,diag)),c,u,t)
                assert abs(direct-closed) < 2e-12*max(1,abs(direct)), (name,u,t,direct,closed)
                comparisons += 1
        rank = exact_rank(rows)
        assert rank == expected, (name,rank,expected)
        print(f'PASS {name}: exact coefficient rank {rank}')
    # The focal identity is exact at rational directions: q-(u.c)^2=1.
    diag,c = tuple(map(F,(5,1,1))),tuple(map(F,(2,0,0)))
    for u in U:
        assert sum(diag[i]*u[i]*u[i] for i in range(3)) - dot(u,c)**2 == 1
    print(f'PASS {comparisons} direct plane-section area comparisons')
    print('PASS exact focal factorization for all rational witness directions')

if __name__ == '__main__':
    run()
