"""Reproducible checks for tetrahedral spherical Voronoi margin formulas.

Run with Python 3 and its standard library:
    python tetrahedral_margin_checker.py

The exact theorem follows from the geometric proof, not these finite tests.
"""
import itertools
import math
import random

SQ = math.sqrt
PI = math.pi
KAPPA = SQ(8.0 / 3.0)
S_MAX = SQ(2.0 / 3.0)
T_MAX = 4.0 / 3.0
ALPHA = math.atan(1.0 / SQ(2.0))
V = tuple(tuple(x / SQ(3.0) for x in v) for v in
          ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)))


def h(s):
    if not 0 <= s <= S_MAX:
        return 0.0
    return max(0.0, math.acos(max(-1.0, min(1.0, s / SQ(3 * (1 - s*s))))) - ALPHA)


def density(t):
    if t < 0 or t >= T_MAX:
        return 0.0
    return 6.0 / (PI * KAPPA) * h(t / KAPPA)


def cdf(t):
    if t <= 0:
        return 0.0
    if t >= T_MAX:
        return 1.0
    s = t / KAPPA
    return 6 / PI * (s * h(s) + math.atan(SQ(3)) - math.atan(SQ(3 - 4*s*s)))


def quadrature(f, a, b, intervals=10000):
    assert intervals % 2 == 0
    step = (b-a)/intervals
    total = f(a)+f(b)
    for j in range(1, intervals):
        total += (4 if j%2 else 2) * f(a+j*step)
    return total * step / 3


def gap(u):
    top = sorted(sum(u[i]*v[i] for i in range(3)) for v in V)
    return top[-1]-top[-2]


def vector(u):
    norm = SQ(sum(x*x for x in u))
    return tuple(x/norm for x in u)


def verify():
    assert abs(cdf(0)) < 1e-14
    assert cdf(T_MAX) == 1.0
    assert abs(quadrature(density, 0, T_MAX)-1) < 1e-9
    m1 = quadrature(lambda t:t*density(t), 0, T_MAX)
    m2 = quadrature(lambda t:t*t*density(t), 0, T_MAX)
    target1 = 2*SQ(6)/PI*math.asin(1/3)
    target2 = 8/9-8/(3*PI*SQ(3))
    assert abs(m1-target1) < 2e-10
    assert abs(m2-target2) < 2e-10
    for j in range(1, 90):
        t = T_MAX*j/90
        direct = quadrature(density, 0, t, 1000)
        assert abs(direct-cdf(t)) < 1e-9
        assert density(t) > density(t+T_MAX/1000)
    deterministic = 0
    for p in itertools.permutations((11, 7, 3)):
        for signs in itertools.product((-1, 1), repeat=3):
            u = vector(tuple(a*b for a, b in zip(p, signs)))
            a, b, c = sorted(map(abs, u), reverse=True)
            want = 2/SQ(3) * (b+c if u[0]*u[1]*u[2]>0 else b-c)
            assert abs(gap(u)-want) < 1e-13
            deterministic += 1
    assert deterministic == 48
    rng = random.Random(315901)
    n = 180000
    grid = (0.1, 0.3, 0.5, 0.8, 1.0, 1.2)
    count = [0]*len(grid)
    s1 = s2 = 0.0
    max_angle_error = 0.0
    for _ in range(n):
        u = vector((rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)))
        g = gap(u)
        s1 += g
        s2 += g*g
        for i,t in enumerate(grid):
            count[i] += (g<=t)
        dots = [sum(u[j]*v[j] for j in range(3)) for v in V]
        best = max(range(4),key=dots.__getitem__)
        # Direct distance to the nearest great-circle decision boundary.
        boundary = min(math.asin(max(-1.0,min(1.0,(dots[best]-dots[j])/KAPPA)))
                       for j in range(4) if j!=best)
        max_angle_error = max(max_angle_error, abs(boundary-math.asin(g/KAPPA)))
    assert abs(s1/n-target1) < .006
    assert abs(s2/n-target2) < .007
    assert max_angle_error < 1e-12
    for t,numer in zip(grid,count):
        assert abs(numer/n-cdf(t)) < .006, (t,numer/n,cdf(t))
    print('TETRAHEDRAL_VORONOI_MARGIN_OK deterministic=48 cdf_checks=89 sample=180000')
    print('integral=1 mean=%.12f second_moment=%.12f max_angle_error=%.3g' %
          (m1,m2,max_angle_error))
    print('empirical_mean=%.12f empirical_second=%.12f max_CDF_discrepancy=%.6f' %
          (s1/n,s2/n,max(abs(numer/n-cdf(t)) for t,numer in zip(grid,count))))


if __name__ == '__main__':
    verify()
