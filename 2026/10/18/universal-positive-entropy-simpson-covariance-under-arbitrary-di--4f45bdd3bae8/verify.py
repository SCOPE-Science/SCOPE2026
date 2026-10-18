"""Reproducibility checks for Dirichlet Shannon--collision covariance.

Run: python verify.py
Dependencies: Python 3.10+, scipy, numpy, mpmath.
Finite and numeric tests supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction
from itertools import product
import math

import numpy as np
from scipy.special import digamma
from scipy.integrate import quad

checks = 0

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction(0))

def direct_integer_moments(params):
    """Independent calculation from shifted Dirichlet gamma integrals."""
    a = list(map(int, params))
    A = sum(a)
    B = sum(z * (z+1) for z in a)
    d = A*(A+1)*(A+2)
    E_Q = Fraction(B, A*(A+1))
    E_H = harmonic(A) - sum((Fraction(z,A)*harmonic(z) for z in a), Fraction(0))
    # First differentiate the beta integral in one exponent, then sum all pairs.
    E_HQ = E_Q*harmonic(A+2) - Fraction(sum(z*(B+2*(z+1))*harmonic(z) + z*(2*z+3) for z in a), d)
    return E_HQ-E_H*E_Q

def simplified_integer(params):
    a = list(map(int, params))
    A = sum(a)
    C = sum(z*z for z in a)
    weighted_digamma_cov = sum((Fraction(z, A)*(z-Fraction(C,A))*harmonic(z) for z in a), Fraction(0))
    return -Fraction(A*A-C, A*(A+1)**2*(A+2)) - 2*weighted_digamma_cov/Fraction((A+1)*(A+2))

def formula(params):
    a = np.asarray(params, dtype=float)
    A = a.sum()
    C = (a*a).sum()
    w = a/A
    c = float(np.dot(w, (a-C/A)*digamma(a+1)))
    return -(A*A-C)/(A*(A+1)**2*(A+2)) - 2*c/((A+1)*(A+2))

for k in (2,3,4):
    for params in product((1,2,3), repeat=k):
        direct = direct_integer_moments(params)
        expression = simplified_integer(params)
        assert direct == expression, (params, direct, expression)
        assert direct < 0, (params, direct)
        checks += 2

for k in (2,3,4,5):
    for t in (0.125, 0.5, 1.0, 2.25, 5.0):
        alpha = [t]*k
        target = -(k-1)*t/((k*t+1)**2*(k*t+2))
        assert math.isclose(formula(alpha), target, rel_tol=3e-12, abs_tol=1e-14)
        checks += 1

# Independent numerical integration in dimension two, with asymmetric shapes.
for a,b in ((0.3,0.7),(0.5,1.5),(1.0,1.0),(1.1,3.0),(2.2,4.3),(5.0,0.7)):
    from scipy.special import betaln
    Z = math.exp(-betaln(a,b))
    def integrand(x, kind):
        if x <= 0 or x>=1:return 0.
        h = -x*math.log(x)-(1-x)*math.log1p(-x)
        q = x*x+(1-x)*(1-x)
        weight = Z*x**(a-1)*(1-x)**(b-1)
        return weight*({'h':h, 'q':q, 'hq':h*q}[kind])
    Eh=quad(lambda x:integrand(x,'h'),0,1,epsabs=3e-11,limit=300)[0]
    Eq=quad(lambda x:integrand(x,'q'),0,1,epsabs=3e-11,limit=300)[0]
    Ehq=quad(lambda x:integrand(x,'hq'),0,1,epsabs=3e-11,limit=300)[0]
    assert abs((Ehq-Eh*Eq)-formula([a,b])) < 5e-9, (a,b,Ehq-Eh*Eq,formula([a,b]))
    checks += 1

# Independently sample the simplex and compare joint empirical covariance with formula.
rng = np.random.default_rng(29031)
for alpha in ((0.5,1.0,2.0), (2,2,2), (0.2,2.4,0.9,1.7), (4,0.5,0.7,3.6,2.0)):
    xx = rng.dirichlet(alpha,size=250_000)
    h = -(xx*np.log(xx)).sum(axis=1)
    q=(xx*xx).sum(axis=1)
    emp=np.cov(h,q,bias=True)[0,1]
    assert abs(emp-formula(alpha)) < 0.0045,(alpha,emp,formula(alpha))
    checks += 1

# Deterministic comparison demonstrates entropy and concentration are not
# globally oppositely ordered on a three-coordinate simplex.
p=np.array([0.49,0.49,0.02]); r=np.array([0.7,0.15,0.15])
assert -(r*np.log(r)).sum() > -(p*np.log(p)).sum()
assert (r*r).sum() > (p*p).sum()
checks += 2
print(f"PASS {checks} independent exact and numerical assertions")
