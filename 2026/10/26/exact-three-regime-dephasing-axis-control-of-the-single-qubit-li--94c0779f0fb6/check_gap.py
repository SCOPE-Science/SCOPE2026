"""Standalone reproducibility checks for a single-qubit Hermitian-dephasing gap theorem.
Requires Python 3, numpy, sympy; no external data or prior outputs.
"""
from math import sqrt
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0

def assert_close(a, b, atol=3e-6):
    global checks
    assert abs(a-b) <= atol, (a,b)
    checks += 1

def optimal(u):
    if u <= .25:
        return 1., (1.-sqrt(1.-4.*u))/2.
    if u <= 1./3.:
        s = sqrt((1./3.-u)/3.)
        return 2./3.+(2./27.+2*s**3)/u, 2./3.-s
    return 2./3.+2./(27.*u), 2./3.

def bloch(u, z):
    s, c = sqrt(max(0,z)), sqrt(max(0,1-z))
    return np.array([[-c*c, -sqrt(u), s*c],
                     [sqrt(u), -1., 0.],
                     [s*c, 0., -s*s]], dtype=float)

def gap(u,z):
    return -max(np.linalg.eigvals(bloch(u,z)).real)

# Characteristic polynomial derivation is symbolic, independently of numerical tests.
l = sp.Symbol('l'); w, Gamma, c, sn = sp.symbols('w Gamma c sn', real=True)
M = sp.Matrix([[-Gamma*c*c,-w,Gamma*c*sn],[w,-Gamma,0],[Gamma*c*sn,0,-Gamma*sn*sn]])
char = sp.expand(M.charpoly(l).as_expr().subs(sn**2,1-c*c))
expected = l**3+2*Gamma*l*l+(Gamma**2+w*w)*l+Gamma*w*w*(1-c*c)
assert sp.simplify(char-expected)==0
checks+=1

# Three exact phase witnesses and Jordan certificate.
r = sp.symbols('r')
for u,z,factor in [(sp.Rational(1,4),1,(r+1)*(r+sp.Rational(1,2))**2),
                   (sp.Rational(5,16),sp.Rational(49,54),(r+sp.Rational(5,6))*(r+sp.Rational(7,12))**2),
                   (sp.Rational(1,3),sp.Rational(8,9),(r+sp.Rational(2,3))**3),
                   (sp.Rational(2,5),sp.Rational(23,27),(r+sp.Rational(2,3))*( (r+sp.Rational(2,3))**2+sp.Rational(1,15)))]:
    poly = r**3+2*r*r+(1+u)*r+u*z
    assert sp.factor(poly-factor)==0
    checks += 1

N = sp.Matrix([[-sp.Rational(1,9),-1/sp.sqrt(3),2*sp.sqrt(2)/9],
 [1/sp.sqrt(3),-1,0],[2*sp.sqrt(2)/9,0,-sp.Rational(8,9)]])+sp.Rational(2,3)*sp.eye(3)
assert N**2 != sp.zeros(3) and N**3 == sp.zeros(3)
checks += 1

# At each sampled coupling, the analytic optimizer maximizes among a dense set of axes.
for u in [0.005,.04,.125,.21,.2499,.25,.2501,.26,.29,5/16,.328,1/3,.34,.4,1.,5.,30.]:
    z, target = optimal(u)
    assert 0. <= z <= 1.
    checks += 1
    assert_close(gap(u,z),target,atol=1e-5)
    for zz in np.linspace(0,1,1001):
        assert gap(u,float(zz)) <= target+1.5e-6, (u,z,zz,target,gap(u,float(zz)))
        checks += 1

# Explicit nonoptimal small-angle tests plus trace consistency.
for u in [0.1,0.27,0.32,0.7]:
    for z in [0.,.1,.5,.85,1.]:
        vals=np.linalg.eigvals(bloch(u,z))
        assert_close(float(vals.real.sum()),-2,atol=1e-10)
        assert_close(float(np.prod(vals).real),-u*z,atol=1e-10)
print('PASS',checks,'checks')
