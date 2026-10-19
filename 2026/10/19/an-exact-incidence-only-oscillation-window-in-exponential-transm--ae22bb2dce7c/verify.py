#!/usr/bin/env python3
"""Independent symbolic and numerical checks for the incidence-only SIR phase theorem.
No numerical computation is used as a substitute for its analytic proof.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

X,Y,r,a=sp.symbols('X Y r a',positive=True)
phi=X-a-a*sp.log(X/a)+Y-r-r*sp.log(Y/r)
dX=X*(r-Y); dY=Y*(X-a)
assert sp.simplify(sp.diff(phi,X)*dX+sp.diff(phi,Y)*dY)==0
assert sp.simplify((r-Y)+(X-a-r))==X-a-Y
x=sp.symbols('x',positive=True)
psi=phi.subs({X:x,Y:x-a})
assert sp.simplify(sp.diff(psi,x)-(2-a/x-r/(x-a)))==0
assert sp.simplify(sp.together(sp.diff(psi,x))*x*(x-a)-(2*x*x-(3*a+r)*x+a*a))==0
assert sp.simplify(sp.diff(psi,x,2)-(a/x**2+r/(x-a)**2))==0
assert sp.simplify(sp.diff(psi,x).subs(x,a+r)-r/(a+r))==0

rval=1.; aval=1.; gamma=2.; beta0=4.;
xstar=(3*aval+rval+math.sqrt(aval**2+6*aval*rval+rval**2))/4
y0star=xstar-aval
F=lambda u,v:u-aval-aval*math.log(u/aval)+v-rval-rval*math.log(v/rval)
hi=F(xstar,y0star); hp=F(gamma,rval)
x0=1.9; y0=1.0; h=F(x0,y0)
assert 0<hi<h<hp
assert x0+y0<=beta0

def rhs(t,z):
    xx,yy=z
    return [xx*(rval-yy),yy*(xx-aval)]

sol=solve_ivp(rhs,(0,65),(x0,y0),rtol=2e-11,atol=2e-13,dense_output=True,max_step=.04)
assert sol.success
T=np.linspace(0,65,20001)
xx,yy=sol.sol(T)
inc=(xx*yy/beta0)*np.exp(-rval*T)
prev=(yy/beta0)*np.exp(-rval*T)
ci=np.where(xx-aval-yy>0)[0]
assert len(ci)>50
# Precise derivative signs, not numerical differencing.
assert max(xx)<gamma-1e-5
assert min(xx-aval-yy)<-.01<max(xx-aval-yy)
pk,_=find_peaks(inc,prominence=1e-25)
assert len(pk)>=4
assert np.all(np.diff(prev)<1e-12)
assert abs(np.max([F(float(u),float(v)) for u,v in zip(xx[::20],yy[::20])])-h)<1e-8
# A second energy lies above the prevalence threshold and contains both peak species.
sol2=solve_ivp(rhs,(0,60),(4.,1.),rtol=2e-11,atol=2e-13,dense_output=True,max_step=.04)
assert sol2.success
x2,y2=sol2.sol(np.linspace(0,60,15000))
assert min(x2)<gamma<max(x2)
assert min(x2-aval-y2)<0<max(x2-aval-y2)
print('VERIFY_OK: symbolic LV conservation and convex-ray threshold; incidence-only strict regime, >=4 peaks, monotonically decreasing prevalence, high-energy two-observable crossing')
