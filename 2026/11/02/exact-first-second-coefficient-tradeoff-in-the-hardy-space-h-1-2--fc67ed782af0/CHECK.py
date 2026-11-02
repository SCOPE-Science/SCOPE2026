#!/usr/bin/env python3
"""Reproduce symbolic identities and supplementary numerical checks for the exact
first--second Taylor coefficient tradeoff in Hardy H^{1/2}.

Universal statements are established analytically in RESULT.md; finite checks
here are diagnostic, not substitutes for the inequalities proved there.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize

checks = 0

def test(condition, message):
    global checks
    if not bool(condition):
        raise AssertionError(message)
    checks += 1

u, v, lam = sp.symbols('u v lam', positive=True, real=True)
Q = 9*lam**2*u**4 + 12*lam*u**3 + (3-6*lam**2)*u**2 - 6*lam*u - 1
v_expr = lam*u/(1+3*lam*u)
D = 1 + u**2 + v**2
F = (4*u+4*lam*v+6*lam*u**2)/D**2
Dtilde = 9*lam**2*u**4 + 10*lam**2*u**2 + 6*lam*u**3 + 6*lam*u + u**2 + 1
# Both free-variable derivatives vanish exactly when the same quartic vanishes
# after the positive multiplier-stationarity relation is imposed.
test(sp.cancel(sp.diff(F,u).subs(v,v_expr) +
               4*(3*lam*u+1)**5*Q/Dtilde**3) == 0,
     'u stationarity algebra')
test(sp.cancel(sp.diff(F,v).subs(v,v_expr) +
               4*lam*(3*lam*u+1)**4*Q/Dtilde**3) == 0,
     'v stationarity algebra')
test(sp.simplify(Q.subs(u,1/sp.sqrt(3))+
                 lam**2+2*lam/sp.sqrt(3)) == 0,
     'lower root endpoint')
test(sp.simplify(Q.subs(u,sp.sqrt(sp.Rational(2,3))) -
                 1-2*sp.sqrt(6)*lam/3) == 0,
     'upper root endpoint')

u0 = 1/sp.sqrt(3)
vinf = sp.Rational(1,3)
uinf = sp.sqrt(sp.Rational(2,3))
test(sp.simplify(4*u0/(1+u0**2)**2-3*sp.sqrt(3)/4) == 0,
     'first coefficient norm endpoint')
test(sp.simplify(6*u0**2/(1+u0**2)**2-sp.Rational(9,8)) == 0,
     'right derivative endpoint')
test(sp.simplify((4*vinf+6*uinf**2)/(1+uinf**2+vinf**2)**2-
                 sp.Rational(27,16)) == 0,
     'second coefficient norm endpoint')
test(sp.simplify(4*uinf/(1+uinf**2+vinf**2)**2-
                 27*sp.sqrt(6)/64) == 0,
     'first coefficient at second-coefficient extremal')

lo,hi=1/math.sqrt(3), math.sqrt(2/3)

def solve_at(t):
    def q(r): return 9*t*t*r**4+12*t*r**3+(3-6*t*t)*r*r-6*t*r-1
    r=brentq(q,lo,hi,xtol=1e-14)
    s=t*r/(1+3*t*r)
    den=1+r*r+s*s
    return r,s,den,(4*r+4*t*s+6*t*r*r)/(den*den)

# Independent numerical constrained optimization on the positive octant sphere,
# not a re-evaluation of the derived quartic after the root is found.
starts=[[.95,.25,.2],[.75,.6,.2],[.6,.5,.6],[.5,.1,.85],[.9,.05,.4]]
for t in [0.01,0.1,0.5,1.0,3.0,20.0,100.0]:
    r,s,den,correct=solve_at(t)
    test(lo<r<hi and 0<s<1/3, 'root bounds')
    test(abs(9*t*t*r**4+12*t*r**3+(3-6*t*t)*r*r-6*t*r-1)<1e-8*(1+t*t),
         'stationarity residual')
    x,y,z = 1/math.sqrt(den),r/math.sqrt(den),s/math.sqrt(den)
    test(abs(x*x+y*y+z*z-1)<1e-12, 'H2 norm')
    # The polynomial 1+r*z+s*z^2 has no root in the unit disk.
    test(np.min(np.abs(np.roots([s,r,1.0])))>1.0+1e-8,
         'no zeros in closed disk')
    a1=4*x**3*y
    a2=4*x**3*z+6*x*x*y*y
    test(abs(a1+t*a2-correct)<3e-12*max(1,correct),
         'coefficient recombination')
    # Numerical integration of |f|^(1/2)=|g|^2 at normalized frequencies.
    angles=2*np.pi*np.arange(4096)/4096
    g=(1+r*np.exp(1j*angles)+s*np.exp(2j*angles))/math.sqrt(den)
    test(abs(np.mean(np.abs(g)**2)-1)<2e-12, 'boundary Hardy normalization')
    def minus_F(a):
        aa=np.maximum(np.asarray(a),0)
        xx,yy,zz=aa/np.linalg.norm(aa)
        return -(4*xx**3*yy + t*(4*xx**3*zz+6*xx**2*yy**2))
    vals=[]
    for initial in starts:
        sol=minimize(minus_F,initial,method='SLSQP',
                     bounds=[(0.000001,1)]*3,
                     options={'ftol':1e-12,'maxiter':300})
        vals.append(-minus_F(sol.x))
        test(vals[-1]<=correct+2e-7*max(1,correct),
             'independent constrained optimization cannot exceed')
    test(abs(max(vals)-correct)<2e-7*max(1,correct),
         'independent optimization attains predicted bound')

print('CHECK_OK',checks)
