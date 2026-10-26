"""Reproducible numerical and symbolic spot checks for asymmetric triangular Fourier bounds.
This script verifies finite instances only; the theorem is proved analytically.
"""
import math
import cmath
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

x,t,c=sp.symbols('x t c', positive=True, real=True)
lhs=2/c*sp.integrate(x*sp.exp(-sp.I*t*x),(x,0,c))+2/(1-c)*sp.integrate((1-x)*sp.exp(-sp.I*t*x),(x,c,1))
rhs=2*(sp.exp(-sp.I*c*t)-(1-c)-c*sp.exp(-sp.I*t))/(c*(1-c)*t*t)
assert sp.simplify(lhs-rhs)==0
print('Symbolic integration identity: PASS')

def numerator(c,t):
    return cmath.exp(-1j*c*t)-(1-c)-c*cmath.exp(-1j*t)

def fourier(c,t):
    return 2*numerator(c,t)/(c*(1-c)*t*t) if t else 1.0

for c0 in [0.225,0.4, (math.sqrt(5)-1)/2]:
  for t0 in [.29,1.8,4.7,11.4,19.7]:
    re=quad(lambda u: (2*u/c0 if u<=c0 else 2*(1-u)/(1-c0))*math.cos(t0*u),0,1,points=[c0],epsabs=1e-12)[0]
    im=-quad(lambda u: (2*u/c0 if u<=c0 else 2*(1-u)/(1-c0))*math.sin(t0*u),0,1,points=[c0],epsabs=1e-12)[0]
    assert abs(complex(re,im)-fourier(c0,t0))<1e-10
print('Direct Fourier quadrature comparisons: 15 PASS')

constant=1+math.pi**2/4
worst=100.
for c0 in [0.25,1/3, (math.sqrt(5)-1)/2,math.sqrt(2)-1, math.pi-3]:
  for k in [1,2,3,5,8,13,34,55,89]:
    d=abs(1-cmath.exp(-2j*math.pi*k*c0))
    obj=lambda u:abs(numerator(c0,2*math.pi*k+u))
    grid=[-math.pi+j*2*math.pi/128 for j in range(129)]
    candidates=[obj(u) for u in grid]
    for u in grid[::8]:
      opt=minimize_scalar(obj,bounds=(max(-math.pi,u-2*math.pi/16),min(math.pi,u+2*math.pi/16)),method='bounded',options={'xatol':1e-11})
      candidates.append(opt.fun)
    obs=min(candidates)
    assert obs>=d/constant-1e-9, (c0,k,obs,d/constant)
    assert obs<=d+1e-9
    if d>1e-9:worst=min(worst,obs/d)
print('Universal cell estimate: 45 sampled (parameter, cell) pairs PASS; minimum observed relative ratio: %.8f' % worst)

for p,q in [(1,3),(2,5),(3,7)]:
    c0=p/q
    for ell in [1,2,4]:
        t0=2*math.pi*q*ell
        assert abs(numerator(c0,t0))<1e-12
        der=-1j*c0*cmath.exp(-1j*c0*t0)+1j*c0*cmath.exp(-1j*t0)
        secon=-c0*c0*cmath.exp(-1j*c0*t0)+c0*cmath.exp(-1j*t0)
        assert abs(der)<1e-12 and abs(secon-c0*(1-c0))<1e-12
print('Rational zero order (exact formulas evaluated): 9 instances PASS')
