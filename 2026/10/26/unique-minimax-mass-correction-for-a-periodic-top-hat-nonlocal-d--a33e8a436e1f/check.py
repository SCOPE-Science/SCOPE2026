#!/usr/bin/env python3
"""Reproducible arithmetic and finite-sampling checks for a spectral-symbol theorem.
Universal statements require the proof in RESULT.md; sampling is not certification.
"""
from fractions import Fraction as F
from math import pi, sin, factorial
import numpy as np
from scipy.optimize import minimize_scalar


def p(t, beta):
    t = np.asarray(t, dtype=float)
    return 2.0 * (1.0 - np.sinc(t / np.pi)) * (beta + 1.0 / (t*t))


def h(t):
    return 1.0 / (6.0 * (1.0 - sin(t)/t)) - 1.0 / (t*t)

# Exact Taylor and polynomial claims from the proof.
p13 = sum(F((-1)**j * (4**(2*j+1)), factorial(2*j+1)) for j in range(7))
assert p13 == F(-131356,173745)
assert p13 < F(-20,27)
assert F(12264,6859) < F(9,5)
u = F(361,25)
polynomial_bound = F(1) + F(7,60)*u - u*u/F(140) + u**3/F(5040)
assert polynomial_bound < F(9,5)
assert F(2)*F(7,6)*(F(9,50)+F(1,36)) == F(1309,2700)
assert F(1309,2700) < F(8,15)
# Positive polynomial at t=6 and globally positive derivative form.
assert 6**3 - 10*6**2 + 60*6 - 60 == 156
assert 2*6**3 - 27*6**2 + 150*6 - 150 == 210

# Experimental stress test on logarithmic, finely spaced, and periodic frequencies.
t = np.unique(np.concatenate((np.geomspace(0.00005,1e6,60000),
                              np.linspace(0.003,55,250000))))
for beta in (1.0/6, .175, .5):
    vals = p(t,beta)
    assert np.isfinite(vals).all()
    assert vals.min() > 0
    if beta == 1.0/6:
        assert vals.min() >= 0.3 - 5e-7
        assert vals.max() <= 0.6 + 5e-7
    if beta == .5:
        assert vals.max() > 4.0/3.0

# Numerical localization of optimizer; not used to prove global optimality.
t_star = minimize_scalar(lambda z: -h(z),bounds=(7.6,8.2),method='bounded',
                         options={'xatol':1e-12}).x
beta_star = h(t_star)
u_star = minimize_scalar(lambda z: -float(p(z,beta_star)),bounds=(3,4.5),
                         method='bounded',options={'xatol':1e-12}).x
predicted_ratio = 3*float(p(u_star,beta_star))
assert .1747 < beta_star < .1749
assert 1.69 < predicted_ratio < 1.71
assert np.min(p(t,beta_star)) >= 1/3 - 5e-7
assert np.max(p(t,beta_star)) <= predicted_ratio/3 + 5e-7
assert np.isclose(float(p(t_star,beta_star)),1/3,atol=1e-10)

for beta in (beta_star-0.02, beta_star-0.005,beta_star+0.005,beta_star+0.02):
    condition = max(1/3,2*beta,float(np.max(p(t,beta)))) / min(1/3,2*beta,float(np.min(p(t,beta))))
    assert condition > predicted_ratio + 1e-5

# Finite periodic grids sampling p(2 pi n / L), merely corroborating uniform claim.
for length in (100.,250.,1000.):
    freqs = 2*pi*np.arange(1,50000)/length
    vals=p(freqs,beta_star)
    assert vals.max()/vals.min() <= predicted_ratio+1e-5

print('Exact rational checks: passed')
print('Scalar stress grid:',len(t),'frequencies; periodic grids: 3')
print('Numerical (not certified) optimizer: t*=',format(t_star,'.12f'),
      'beta*=',format(beta_star,'.12f'), 'u*=',format(u_star,'.12f'),
      'K*=',format(predicted_ratio,'.12f'))
print('All checks passed.')
