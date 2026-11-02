#!/usr/bin/env python3
"""Symbolic and deterministic checks of three-state steady-state dissipation identities.

Requirements: SymPy >=1.12; these tests support, but do not substitute for,
the elementary analytic proof in RESULT.md.
"""
import math
import random
import sympy as sp

w = sp.symbols('w', positive=True)
terms = [
    w*(3-w)**2*sp.log(3-w)/3,
    -4*w*w*(3-2*w)*sp.log(2*w)/3,
    -3*w*(1-w)**2*sp.log(3*(1-w)),
    -2*w*w*(1-w),
]
expected_parts = [
    -sp.Rational(4,3)*sp.log(2)-sp.Rational(109,144)+sp.Rational(9,4)*sp.log(3),
    sp.Rational(5,18)-sp.Rational(2,3)*sp.log(2),
    sp.Rational(7,48)-sp.Rational(1,4)*sp.log(3),
    -sp.Rational(1,6),
]
checks = 0
for integrand, exact in zip(terms, expected_parts):
    assert sp.simplify(sp.integrate(integrand, (w, 0, 1)) - exact) == 0
    checks += 1
mean_sta = sp.simplify(sum(expected_parts))
assert sp.simplify(mean_sta-(2*sp.log(sp.Rational(3,2))-sp.Rational(1,2))) == 0
checks += 1
assert sp.simplify(sp.integrate(w*sp.log((1+w)/(1-w)), (w, 0, 1))-1) == 0
checks += 1
assert abs(float(mean_sta) - 0.310930216216328764) < 1e-14
checks += 1
# Independent flow-parametrization checks, including entropy-production formula.
rng = random.Random(20261024)
for k in range(1000):
    z = rng.random()
    j = (1 if rng.randrange(2) else -1)*z/3
    e = [-math.log(max(rng.random(),1e-15)) for _ in range(3)]
    u = [v/sum(e) for v in e]
    activities = [abs(j)+(1-z)*v for v in u]
    a,b,c = activities
    m = [[0, (a+j)/2, (c-j)/2],
         [(a-j)/2, 0, (b+j)/2],
         [(c+j)/2, (b-j)/2, 0]]
    assert abs(sum(sum(row) for row in m)-1) < 1e-12
    assert all(x>0 for row in m for x in row if x!=0)
    assert max(abs(sum(m[i])-sum(m[k][i] for k in range(3))) for i in range(3)) < 1e-12
    sigma = sum(m[i][k]*math.log(m[i][k]/m[k][i]) for i in range(3) for k in range(3) if i!=k)
    formula = abs(j)*sum(math.log((v+abs(j))/(v-abs(j))) for v in activities)
    assert abs(sigma-formula) < 2e-12
    assert sigma + 1e-13 >= z*math.log((1+z)/(1-z))
    checks += 5
print('PASS', checks, 'deterministic checks; mean=', sp.N(mean_sta, 25))
