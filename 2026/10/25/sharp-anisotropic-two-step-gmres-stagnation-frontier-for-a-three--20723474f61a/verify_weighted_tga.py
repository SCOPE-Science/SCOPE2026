"""Reproducibility checks for weighted three-site GMRES(2) stagnation.

Dependencies: Python 3.10+, numpy, scipy, sympy. Universal statements
are proven in RESULT.md; finite tests only check independent instances.
"""
from math import sqrt, log, exp
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize_scalar
import sympy as sp

z, rho = sp.symbols('z rho', positive=True)
gexpr = (z*z+1)*(z+rho)**2/(z*(z*z+rho*z+rho*rho))
assert sp.simplify(gexpr-sp.factor(gexpr.subs({z:1/z,rho:1/rho}, simultaneous=True))) == 0
assert sp.factor(gexpr.subs(rho,1)-sp.Rational(8,3)) == (z-1)**2*(3*z*z+4*z+3)/(3*z*(z*z+z+1))
assert sp.factor(gexpr.subs(z,1)-2) == 2*rho/(rho*rho+rho+1)

u=(sp.Integer(5)+sp.sqrt(5))/(2*sp.sqrt(2))
v=(sp.Integer(5)-sp.sqrt(5))/(2*sp.sqrt(2))
r=sp.Matrix([1,-1/sp.sqrt(2),1])
A=sp.eye(3)+sp.Matrix([[0,u,0],[0,0,v],[0,0,0]])
assert sp.simplify(u*v)==sp.Rational(5,2)
assert sp.simplify((r.T*A*r)[0])==0
assert sp.simplify((r.T*A*A*r)[0])==0
assert sp.simplify(sp.Matrix.hstack(r,A*r,A*A*r).det()) != 0

# The derivative of the scalar frontier equals zero at its optimizer;
# minimizing over logarithmic t avoids the positive-axis boundary.
def G(t,ratio):
    return (t*t+1)*(t+ratio)**2/(t*(t*t+ratio*t+ratio*ratio))
def gstar(ratio):
    opt=minimize_scalar(lambda q:G(exp(q),ratio),bounds=(-20.,20.), method='bounded',options={'xatol':1.e-13})
    assert opt.success
    return opt.fun
assert abs(gstar(1)-8/3)<1.e-10
for ratio in [0.01,0.03,0.1,0.3,0.5,1,2,3,10,33,100]:
    th=gstar(ratio)
    assert 2-1.e-10<th<=8/3+1.e-10
    assert abs(th-gstar(1/ratio))<1.e-8
assert gstar(0.01)<2.03

rng=np.random.default_rng(20261018)
for case in range(4000):
    ratio=exp(rng.uniform(-2,2))
    t=exp(rng.uniform(-2,2))
    product=G(t,ratio)
    u0=sqrt(product/ratio)
    v0=sqrt(product*ratio)
    y=-product/(u0*sqrt(t)+v0/sqrt(t))
    r0=np.array([sqrt(t),y,1/sqrt(t)])
    M=np.array([[1,u0,0],[0,1,v0],[0,0,1]],dtype=float)
    assert abs(r0@M@r0)<1.e-9*(1+np.linalg.norm(r0)**2)
    assert abs(r0@M@M@r0)<1.e-9*(1+np.linalg.norm(r0)**2)
    dirs=np.column_stack((M@r0, M@M@r0))
    coeff=np.linalg.lstsq(dirs,r0,rcond=None)[0]
    assert np.linalg.norm(coeff)<1.e-8
    assert np.linalg.norm(M@M@M@r0)>0

# Complementary exact split: same positive edge product with and without
# a two-step stagnation starting vector, depending on edge imbalance.
balanced=sqrt(2.5)
M=np.array([[1.,balanced,0.],[0.,1.,balanced],[0.,0.,1.]])
assert 2.5 < gstar(1)
assert 2.5 >= gstar(float(v/u))
print('VERIFICATION_OK: exact algebraic witness and identities; 4000 numerical constructions; 11 frontier ratios')
