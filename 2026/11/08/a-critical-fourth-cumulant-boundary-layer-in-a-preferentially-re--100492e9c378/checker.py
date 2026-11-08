#!/usr/bin/env python3
"""Independent algebraic and finite-time diagnostics for a preferential-resetting telegraph process.

Requires Python 3.10+, sympy, mpmath, scipy, and numpy. Run: python checker.py
The symbolic identity checks are exact; finite numerical tests are diagnostics,
not substitutes for the asymptotic uniformity proof in RESULT.md.
"""
import math

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

checks = 0

def verify(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

R, z = sp.symbols('R z', positive=True)
lam = 1 - sp.sqrt(1-z)
a = lam/(R+lam)
a1 = sp.simplify(sp.expand(sp.series(a,z,0,3).removeO()).coeff(z,1))
a2 = sp.simplify(sp.expand(sp.series(a,z,0,3).removeO()).coeff(z,2))
verify(sp.simplify(a1-1/(2*R)) == 0,'quadratic decay coefficient')
verify(sp.simplify(a2-(R-2)/(8*R**2)) == 0,'quartic decay coefficient')

# log-Gamma(1-a) = gamma_E a + zeta(2) a^2/2 + O(a^3).
logc = (sp.log((1+1/sp.sqrt(1-z))/2)
        -a*sp.log(1+lam/R)-sp.EulerGamma*a-sp.zeta(2)*a*a/2)
logc = sp.expand(sp.series(logc,z,0,3).removeO())
c1 = sp.simplify(logc.coeff(z,1))
c2 = sp.simplify(logc.coeff(z,2))
verify(sp.simplify(c1-(sp.Rational(1,4)-sp.EulerGamma/(2*R))) == 0,'quadratic prefactor')
verify(sp.simplify(c2-(sp.Rational(5,32)
   -(2+sp.pi**2/6)/(8*R**2)-sp.EulerGamma*(R-2)/(8*R**2))) == 0,
   'quartic prefactor')
verify(sp.simplify(24*c2-3*(sp.Rational(5,4)-(2+sp.pi**2/6)/R**2
        -sp.EulerGamma*(R-2)/R**2)) == 0,'fourth-cumulant constant')

Cstar = sp.simplify(24*c2.subs(R,2))
verify(sp.simplify(Cstar-(9-sp.pi**2/2)/4)==0,'critical fourth cumulant')
verify(bool(Cstar>0),'positive critical fourth cumulant')
root_shift = sp.simplify(-((24*c2.subs(R,2)))/(-3/sp.Integer(4)))
verify(sp.simplify(root_shift-(3-sp.pi**2/6))==0,'critical root shift')
verify(sp.simplify(sp.diff((2-R)/R**2,R)-(R-4)/R**3)==0,
       'strict negative derivative on the chosen rate interval')

mp.mp.dps=60

def kmoments(r,t,g=1,v=1):
    r=mp.mpf(str(r));t=mp.mpf(str(t));g=mp.mpf(str(g));v=mp.mpf(str(v))
    def Q(h):
        s=mp.sqrt(g*g-v*v*h)
        lp=g+s; lm=g-s
        aa=lp/(r+lp);bb=lm/(r+lm)
        return ((1-g/s)*mp.hyp1f1(aa,1,-(r+lp)*t)
              +(1+g/s)*mp.hyp1f1(bb,1,-(r+lm)*t))/2
    dh=mp.diff(Q,0,1);ddh=mp.diff(Q,0,2)
    m2=-2*dh;m4=12*ddh
    return float(m2),float(m4),float(m4-3*m2*m2)

def moment_ode(r,t,g=1.0,v=1.0):
    eps=1e-6
    def fun(s,y):
        b1,m2,b3,m4,B1,M2,B3,M4=y
        return [v-(r+2*g)*b1+r*B1/s,
                2*v*b1-r*m2+r*M2/s,
                3*v*m2-(r+2*g)*b3+r*B3/s,
                4*v*b3-r*m4+r*M4/s,
                b1,m2,b3,m4]
    init=[v*eps,v*v*eps**2,v**3*eps**3,v**4*eps**4,
          v*eps**2/2,v*v*eps**3/3,v**3*eps**4/4,v**4*eps**5/5]
    solution=solve_ivp(fun,(eps,t),init,rtol=3e-11,atol=3e-12)
    verify(solution.success,'ODE solved successfully')
    m2,m4=solution.y[1,-1],solution.y[3,-1]
    return m2,m4,m4-3*m2*m2

for r,t in [(1.5,20),(2.0,20),(2.5,20),(2.0,100),(1.5,150)]:
    A=kmoments(r,t)
    B=moment_ode(r,t)
    for idx in range(3):
        verify(abs(A[idx]-B[idx])<2e-7,'Fourier-vs-generator moment check')

for r,t,sgn in [(1.5,1000,1),(2.0,1000,1),(2.5,1000,-1),
                (1.8,10000,1),(2.5,10000,-1)]:
    verify(sgn*kmoments(r,t)[2]>0,'observed cumulant sign')

for t in [10000,1000000]:
    root = mp.findroot(lambda rr: kmoments(rr,t)[2],(2.05,2.45))
    verify(2<root<2.5,'critical root in the predicted interval')
    approx=2+(3-mp.pi**2/6)/mp.log(t)
    verify(abs(root-approx)<0.1,'asymptotic shift diagnostic')

limit=(9-float(mp.pi**2)/2)/4
verify(abs(kmoments(2,1000000)[2]-limit)<0.02,
       'critical constant approached by finite-time solution')
print(f'PASS: {checks} symbolic, transform, and independent moment-equation diagnostics')
print('critical fourth-cumulant limit:',f'{limit:.14f}')
