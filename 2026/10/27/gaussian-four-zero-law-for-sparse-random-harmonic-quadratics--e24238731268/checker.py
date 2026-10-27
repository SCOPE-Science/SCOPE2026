"""Reproducibility checks for the Gaussian quadratic harmonic-zero law.

Requires: mpmath, numpy. Run: python checker.py
Finite checks supplement, and do not replace, the analytical proof.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 45

def probability(s):
    s = mp.mpf(s)
    def g(t):
        c = mp.cos(3*t)
        q = 5 - 4*c
        u = 2*s/mp.sqrt(q)
        return (1+c)/(mp.pi*q)*(1-mp.sqrt(mp.pi)*u*mp.exp(u*u)*mp.erfc(u))
    # Segmenting at the three cusps accelerates high-precision integration.
    return mp.quad(g, [j*mp.pi/3 for j in range(7)])

modulus = 2*mp.sqrt(2)/3
C1 = 2*(9*mp.ellipe(modulus**2)-mp.ellipk(modulus**2))/(3*mp.sqrt(mp.pi))
assert abs(C1-mp.mpf('2.81908397948545026798298522597384738')) < mp.mpf('1e-33')
assert abs(probability(1)-mp.mpf('0.1463548751372028')) < mp.mpf('1e-16')
for s in ['0.01','0.1','0.3','1','3','10']:
    assert 0 < probability(s) < 1
for left,right in zip(['0.01','0.1','0.3','1','3'], ['0.1','0.3','1','3','10']):
    assert probability(left)>probability(right)

# Analytic coefficients are checked numerically by limit sequences.
for s in ['0.0002','0.0005','0.001']:
    s = mp.mpf(s)
    residual = (probability(s)-1+C1*s)/s**2
    assert abs(residual-mp.mpf(16)/3) < mp.mpf('0.03')
for s in ['25','40','60']:
    s = mp.mpf(s)
    residual = (probability(s)-1/(4*s**2))*s**4
    assert abs(residual+mp.mpf(9)/32) < mp.mpf('0.004')

# Independent algebraic root-count check against point-in-deltoid winding.
rng = np.random.default_rng(20261023)
theta = np.linspace(0.0,2*np.pi,1025)
curve = np.exp(2j*theta)-2*np.exp(-1j*theta)

def is_inside(z):
    winding = np.angle((curve[1:]-z)/(curve[:-1]-z)).sum()/(2*np.pi)
    return round(winding) != 0

count = 0
for i in range(350):
    a = math.sqrt(rng.exponential())
    sigma = 10**rng.uniform(-1,1)
    c = sigma*(rng.normal()+1j*rng.normal())/math.sqrt(2)
    quartic = [1,0,-2*c,-a**3,c*c-a*a*c.conjugate()]
    roots = np.roots(quartic)
    physical = [z for z in roots if abs(z*z-a*z.conjugate()-c) < 1e-5*(1+a*a+abs(c))]
    expected = 4 if is_inside(4*c/(a*a)) else 2
    assert len(physical) == expected, (a, c, len(physical), expected)
    count += 1
print('PASS: probability, endpoint coefficients, strict monotonicity samples,',count,'random algebraic-root/caustic checks')
print('P(N=4) for sigma=1:',mp.nstr(probability(1),30))
print('small-noise linear coefficient:',mp.nstr(C1,30))
