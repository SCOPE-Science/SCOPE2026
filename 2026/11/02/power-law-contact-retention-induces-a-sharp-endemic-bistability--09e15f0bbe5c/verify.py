#!/usr/bin/env python3
"""Standalone exact-algebra and numerical checks for the power-law adaptive SIS theorem."""
from fractions import Fraction
from math import isclose, sqrt
import sympy as S
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

y,s,w,xi,tau=S.symbols('y s w xi tau', positive=True)
q=S.symbols('q', real=True, positive=True)
T=1/s+w*s**(q-1)
assert S.simplify(S.diff(T,s)-(w*(q-1)*s**q-1)/s**2)==0
# At the fold, omega*(q-1)*s**q=1, so T''=q/s**3.
fold_second=S.diff(T,s,2)
assert S.simplify(fold_second-(2+w*(q-1)*(q-2)*s**q)/s**3)==0
# The Jacobian and determinant at endemic equilibrium follow from the original equations.
F=y*(tau*(1-y)*S.Symbol('z')-1)
z=S.Symbol('z')
G=xi*(1-(1+w*(1-y)**q)*z)
J=S.Matrix([F,G]).jacobian([y,z]); zstar=1/(1+w*(1-y)**q)
Je=J.subs({tau:1/((1-y)*zstar),z:zstar})
assert S.simplify(Je.det()-xi*y*(1-w*(q-1)*(1-y)**q)/(1-y))==0
assert S.simplify(Je.trace()+y/(1-y)+xi*(1+w*(1-y)**q))==0
# At omega=1, q=2, tau=2, the invariant center manifold has
# h(y)=1/2+y/2+y**2/4+O(y**3), which gives cubic drift -y**3/2.
h=S.Rational(1,2)+y/2+y**2/4
critdrift=S.series(y*(2*(1-y)*h-1),y,0,4).removeO()
assert S.expand(critdrift)==-y**3/2
critical_defect=S.series(xi*(1-(1+(1-y)**2)*h)-S.diff(h,y)*y*(2*(1-y)*h-1),y,0,3).removeO()
assert S.expand(critical_defect)==0
# q=3, omega=1, tau=2 has exact endemic s=(sqrt(5)-1)/2.
sstar=(S.sqrt(5)-1)/2; ystar=1-sstar; zstar3=1/(1+sstar**3)
assert S.simplify(sstar*(2)-1-sstar**3)==0
assert S.simplify(J.subs({w:1,q:3,xi:1,tau:2,y:ystar,z:zstar3}).det())>0
# q=3, omega=1 has fold strictly below invasion 2.
fold=1.5*2**(1/3)
assert 1.88<fold<1.90
roots=[]
for a,b in [(.5,.75),(.75,1.)]:
 roots.append(brentq(lambda u:1/u+u*u-1.95,a,b,xtol=1e-14))
assert 0<roots[0]<2**(-1/3)<roots[1]<1
assert all(abs(1/r+r*r-1.95)<1e-12 for r in roots)
for s0,positive in [(roots[0],True),(roots[1],False)]:
 y0=1-s0; z0=1/(1+s0**3)
 ev=S.Matrix(J.subs({w:1,q:3,xi:1,tau:S.Rational(39,20),y:y0,z:z0})).evalf()
 determinant=float(ev.det())
 assert (determinant>0)==positive
# Full system trajectories approach predicted global critical rates.
def integrate(qval, initial, end):
 def field(t,v):
  a,b=v
  return [a*(2*(1-a)*b-1),1-(1+(1-a)**qval)*b]
 result=solve_ivp(field,(0,end),initial,method='BDF',rtol=1e-10,atol=1e-12)
 assert result.success, result.message
 return result.y[0,-1]
yt1=integrate(1,(.8,.8),150000)
yt2=integrate(2,(.8,.8),150000)
assert abs(150000*yt1-2)<.02
assert abs(150000*yt2*yt2-1)<.02
print('PASS: root-curve derivative, Jacobian, fold, critical center expansion, exact endemic state, bistability, and critical integration')
print('q=1: t*y =',150000*yt1,'q=2: t*y^2 =',150000*yt2*yt2)
