"""Independent finite checks of the two-mode Gaussian harmonic-projection theorem.

Requires Python 3, numpy and scipy. Finite checks supplement, not replace,
the analytic proof of the Beta law and asymptotics.
"""
from fractions import Fraction as F
from itertools import product
from math import asin, erf, gamma, pi, sqrt
import numpy as np
from scipy.special import betainc, ndtr


def c2(k):
    return 4 * k / (k + 1)**2


def probability(s, k):
    return float(betainc(0.5, (s - 1)/2, c2(k)))


# Exhaust finite integer 2x2 sketches: determinant and the sign of the
# exact harmonic denominator must agree with the squared-cosine condition.
rational_checks = 0
negative_witnesses = 0
for x, y, u, v in product(range(-2, 3), repeat=4):
    det_s = x*v - y*u
    if det_s == 0:
        continue
    xx = x*x + y*y
    yy = u*u + v*v
    xy = x*u + y*v
    for k in (F(2), F(3), F(5), F(11), F(1)):
        h11 = F(xx)
        h22 = k * yy
        h12 = F(1 + k, 2) * xy
        det_h = h11*h22 - h12*h12
        condition = F(xy*xy, xx*yy) < F(4*k, (k+1)**2)
        assert (det_h > 0) == condition
        if det_h < 0:
            # b=(-h12/h11,1) makes b^T H b<0, so theta<0.
            b1 = -h12 / h11
            b2 = F(1)
            denom = h11*b1*b1 + 2*h12*b1*b2 + h22*b2*b2
            ab1 = b1
            ab2 = k*b2
            numerator = (x*ab1 + u*ab2)**2 + (y*ab1 + v*ab2)**2
            assert denom < 0 < numerator
            negative_witnesses += 1
        rational_checks += 1

# Independently test the matrix-sign equivalence in larger sketch dimensions.
# This checks the actual symmetric Jordan product, not just the angle formula.
matrix_eigen_checks = 0
rng_matrix = np.random.default_rng(781931)
for s in (3, 6, 12):
    for k in (2., 6., 100.):
        for _ in range(200):
            u = rng_matrix.standard_normal(s)
            v = rng_matrix.standard_normal(s)
            xx, yy, xy = np.dot(u,u), np.dot(v,v), np.dot(u,v)
            h = np.array([[xx, .5*(1+k)*xy], [.5*(1+k)*xy, k*yy]])
            angle_test = xy*xy/(xx*yy) < c2(k)
            eigen_test = np.linalg.eigvalsh(h)[0] > 0
            assert bool(eigen_test) == bool(angle_test)
            matrix_eigen_checks += 1

# Closed probability checks for sketch dimensions two and three.
special_checks = 0
for k in (1.001, 1.3, 2., 4., 9., 33., 300., 10000.):
    c = sqrt(c2(k))
    assert abs(probability(2,k) - 2*asin(c)/pi) < 2e-12
    assert abs(probability(3,k) - c) < 2e-12
    special_checks += 2

# Direct Gaussian simulations test the entire event over all trial vectors
# without discretizing directions: a negative H determinant gives a witness.
rng = np.random.default_rng(406281)
trials = 50000
simulation_checks = 0
for s, k in ((2,4), (3,9), (5,25), (10,100), (24,30), (50,100)):
    u = rng.normal(size=(trials,s))
    v = rng.normal(size=(trials,s))
    r2 = np.sum(u*v,axis=1)**2 / (np.sum(u*u,axis=1)*np.sum(v*v,axis=1))
    empirical = np.mean(r2 < c2(k))
    exact = probability(s,k)
    assert abs(empirical-exact) < 0.014, (s,k,empirical,exact)
    simulation_checks += 1

# Verify monotonicity and fixed ratio asymptotics numerically.
asymptotic_checks = 0
for k in (10000., 100000.):
    for t in (0.2, 0.5, 1., 2., 4.):
        s = max(2,round(t*k))
        exact = probability(s,k)
        limit = 2*ndtr(2*sqrt(t))-1
        assert abs(exact-limit)<0.008, (s,k,exact,limit)
        asymptotic_checks += 1
for s in range(2,13):
    p = probability(s,1e7)
    coeff = 4*gamma(s/2)/(sqrt(pi)*gamma((s-1)/2))
    assert abs(sqrt(1e7)*p/coeff-1) < 1e-5
    asymptotic_checks += 1

for k in (1.01,2,7,20,100):
    vals=[probability(s,k) for s in range(2,30)]
    assert all(x < y or (x > 1-1e-10 and y == 1.) for x,y in zip(vals, vals[1:]))

print('VERIFY_OK', f'{rational_checks} exact determinant cases,',
      f'{negative_witnesses} negative witnesses,',
      f'{matrix_eigen_checks} direct Jordan eigentests,',
      f'{special_checks} closed-Beta cases,',
      f'{simulation_checks} Gaussian simulations,',
      f'{asymptotic_checks} asymptotic checks')
