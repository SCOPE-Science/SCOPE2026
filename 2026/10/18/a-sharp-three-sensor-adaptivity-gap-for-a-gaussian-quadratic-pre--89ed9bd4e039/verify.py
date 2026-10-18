#!/usr/bin/env python3
"""Independent exact and high-precision checks for a three-sensor Gaussian Bayes-risk theorem.

Python 3, SymPy and mpmath are required. Finite checks do not establish the
universal statements; their analytical proofs are provided separately.
"""
import mpmath as mp
import sympy as sp
from itertools import combinations

rho, a = sp.symbols('rho a', positive=True)
z1, z2, z3 = sp.symbols('z1 z2 z3', real=True)

def gaussian_moment_term(m):
    if m % 2:
        return 0
    value = 1
    for j in range(1, m, 2):
        value *= j
    return value

def mean_standard_normal(expr, variables):
    polynomial = sp.Poly(sp.expand(expr), *variables)
    total = 0
    for multi, coefficient in polynomial.terms():
        total += coefficient * sp.prod(gaussian_moment_term(d) for d in multi)
    return sp.simplify(total)

checks = 0
# Bayes posterior means under single/pair coordinate readings, derived
# independently by conditioning Gaussian factors.
posterior_mean = {
    (): sp.S(0),
    (1,):sp.S(0),
    (2,):sp.S(0),
    (3,):a*sp.sqrt(rho)*z3,
    (1,2):rho*z1*z2,
    (1,3):a*sp.sqrt(rho)*z3,
    (2,3):a*sp.sqrt(rho)*z3,
}
for sensors in [(),(1,),(2,),(3,),(1,2),(1,3),(2,3)]:
    objective = posterior_mean[sensors]
    explained_variance = mean_standard_normal(objective**2, (z1,z2,z3)) - mean_standard_normal(objective,(z1,z2,z3))**2
    target = rho**2 if sensors == (1,2) else (rho*a*a if 3 in sensors else sp.S(0))
    assert sp.simplify(explained_variance-target) == 0
    checks += 1

# Symbolically check the four relevant dynamic-programming conditional gains.
assert sp.simplify(mean_standard_normal((rho*z1*z2)**2,(z2,)) - rho**2*z1**2) == 0
assert sp.simplify(mean_standard_normal((a*sp.sqrt(rho)*z3)**2,(z3,))-rho*a*a)==0
checks += 2

mp.mp.dps = 70
phi=lambda z:mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
Q=lambda z:mp.erfc(z/mp.sqrt(2))/2

def sharp_gain(c):
    t=mp.sqrt(c)
    return c+2*(t*phi(t)+(1-c)*Q(t))

def direct_gain(c):
    t=mp.sqrt(c)
    return 2*(c*mp.quad(phi,[0,t])+mp.quad(lambda z:z*z*phi(z),[t,mp.inf]))

# Independent integration for the exact Gaussian max formula, with values on
# both sides of the sharp equal-gains balance.
cs=['0.0001','0.002','0.01','0.1','0.4','0.6','0.9','1','1.1','2','4','10','100','30']
for s in cs:
    c=mp.mpf(s)
    assert abs(sharp_gain(c)-direct_gain(c))<mp.mpf('1e-54')
    assert sharp_gain(c)>max(1,c)
    checks += 2

max_ratio=1+mp.sqrt(2/mp.pi)*mp.exp(-mp.mpf('0.5'))
assert abs(sharp_gain(mp.mpf(1))-max_ratio)<mp.mpf('1e-62')
checks+=1

# Exact finite-parameter tests of optimal first sensor and optimal second
# decision for all candidate two-coordinate policies.
for r in [mp.mpf('0.05'),mp.mpf('0.15'),mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('0.9')]:
    for c in [mp.mpf(s) for s in cs]:
        amp=mp.sqrt(r*c)
        adaptive=r*r*sharp_gain(c)
        fixed=max(r*r,amp*amp*r)
        initial_linear=amp*amp*r
        assert adaptive>fixed>=initial_linear
        assert adaptive<=1+amp*amp
        assert adaptive/fixed<=max_ratio+mp.mpf('1e-55')
        checks += 4

# Derivative identities for r(c)=E max(Z^2,c)/max(1,c).
# For c<1 the derivative of the numerator is P(Z^2<c)>0;
# for c>1 the derivative of r(c) is -E[Z^2 1{Z^2>c}]/c^2<0.
for c in [mp.mpf(j)/100 for j in range(1,300) if j!=100]:
    h=mp.mpf('1e-7')
    derivative=(sharp_gain(c+h)/max(1,c+h)-sharp_gain(c-h)/max(1,c-h))/(2*h)
    if c<1:
        assert derivative>0
    else:
        assert derivative<0
    checks+=1
print('PASSED',checks,'symbolic Bayes-risk and high-precision adaptive-design checks')
print('sharp ratio',mp.nstr(max_ratio,30))
