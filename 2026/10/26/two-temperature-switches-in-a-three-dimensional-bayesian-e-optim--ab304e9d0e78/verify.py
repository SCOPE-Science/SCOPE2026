"""Standalone reproducibility checks for a three-mode entropic design selector.

Uses Python's standard library. Exact inequalities and a Descartes bound are
proved in RESULT.md; finite numerical samples here are consistency checks.
"""
from fractions import Fraction as F
from math import exp, log
from random import Random


def coeff_poly_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

# Ascending order coefficients. Eigenspectra are (1,1,8) and (0,4,5).
char_u = coeff_poly_product(coeff_poly_product([-1, 1], [-1, 1]), [-8, 1])
char_v = coeff_poly_product(coeff_poly_product([0, 1], [-4, 1]), [-5, 1])
assert char_u == [-8, 17, -10, 1], char_u
assert char_v == [0, 20, -9, 1], char_v
# M_u is block [[2,sqrt(6)],[sqrt(6),7]] plus the eigenvalue 1.
assert 2+7 == 1+8 and 2*7-6 == 1*8
# M_v is diag(0,5,4); both arise from C=diag(0,1,4)
# by rank-one updates (sqrt(2),0,sqrt(3)) and (0,2,0).

P = [-1, 2, 0, 0, -1, -1, 0, 0, 1]
Q = [1, -1, -1, -1, 0, 1, 1, 1]
assert coeff_poly_product([-1, 1], Q) == P


def eval_q(t):
    value = F(0)
    for coeff in reversed(Q):
        value = value*t+coeff
    return value

checks = [(F(1, 2), F(23, 128)),
          (F(3, 5), F(-1843, 78125)),
          (F(9, 10), F(1612279, 10000000))]
for t, val in checks:
    assert eval_q(t) == val, (t, eval_q(t), val)
assert [x for x in reversed(Q) if x] == [1,1,1,-1,-1,-1,1]
# Thus Descartes gives at most two positive roots; the three exact sign
# witnesses force exactly two, each simple, both between 0 and 1.


def q_float(t):
    v = 0.0
    for c in reversed(Q):
        v = v*t+c
    return v


def bracket_bisect(a, b):
    fa = q_float(a)
    fb = q_float(b)
    assert fa*fb < 0
    for _ in range(90):
        m = (a+b)/2
        fm = q_float(m)
        if fm == 0:
            return m
        if fm*fa > 0:
            a, fa = m, fm
        else:
            b, fb = m, fm
    return (a+b)/2

r1 = bracket_bisect(.5, .6)
r2 = bracket_bisect(.6, .9)
mu1, mu2 = -1/log(r1), -1/log(r2)
assert abs(r1-0.587411973105599) < 2e-13
assert abs(r2-0.863610809291643) < 2e-13


def s_u(mu):
    return 2*exp(-1/mu)+exp(-8/mu)


def s_v(mu):
    return 1+exp(-4/mu)+exp(-5/mu)

for mu, winner in [(0.1,'u'), (1.,'u'), (2.,'v'), (3.,'v'), (6.,'v'), (7.,'u'), (10.,'u'), (100.,'u')]:
    better = 'u' if s_u(mu) < s_v(mu) else 'v'
    assert better == winner, (mu,better)

# The 2-dimensional endpoint-order implication is proved analytically in the
# accompanying note; 9,000 seeded examples test the implication numerically.
rng = Random(20261023)
n2 = 0
for _ in range(9000):
    b1 = rng.uniform(0,5)
    b2 = b1+rng.uniform(0,8)
    a1 = b1+rng.uniform(.0005,.5)
    a2 = a1+rng.uniform(0,8)
    if a1+a2 <= b1+b2:
        continue
    for mu in (.04, .11, .4, 1., 5., 20., 400.):
        a = exp(-a1/mu)+exp(-a2/mu)
        b = exp(-b1/mu)+exp(-b2/mu)
        assert a <= b+2e-14, (a1,a2,b1,b2,mu,a,b)
    n2 += 1
print('CHECKS_OK')
print('exact_polynomial_sign_checks=3')
print('charpoly_checks=2')
print('sign_variations_Q=2')
print('two_dimensional_random_cases=', n2, sep='')
print('root_t_minus=%.15f' % r1)
print('root_t_plus=%.15f' % r2)
print('threshold_mu_minus=%.12f' % mu1)
print('threshold_mu_plus=%.12f' % mu2)
for mu in (1,3,10):
    print('mu=%g, trace_exp_u=%.14f, trace_exp_v=%.14f' % (mu, s_u(mu), s_v(mu)))
