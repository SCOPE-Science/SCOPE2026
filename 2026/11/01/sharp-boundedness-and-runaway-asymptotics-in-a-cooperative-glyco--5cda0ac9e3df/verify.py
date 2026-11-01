#!/usr/bin/env python3
"""Symbolic identities and illustrative numerical integration for a glycolysis ODE."""
from fractions import Fraction
import math
from scipy.integrate import solve_ivp
import sympy as sp

x,y,nu,sg,si,q,L,k,n,la = sp.symbols('x y nu sg si q L k n la', positive=True)
phi=x*(x+1)*(y+1)**2/(L+(x+1)**2*(y+1)**2)
R=y**n/(k**n+y**n)
fx=nu-sg*phi+si*R
fy=q*(sg*phi-si*R)-la*y
assert sp.simplify(fx+fy/q-nu+la*y/q)==0
assert sp.simplify(phi-x/(1+x)+L*x/((1+x)*(L+(x+1)**2*(y+1)**2)))==0
assert sp.simplify(sp.diff(x*(x+1)/(L+(x+1)**2),x)-((2*x+1)*L+(x+1)**2)/(L+(x+1)**2)**2)==0
xi=sp.factor((nu+si)/(sg-nu-si))
assert sp.simplify(nu+si-sg*xi/(1+xi))==0
print('Symbolic flux cancellation, saturation bound, monotonicity and limiting substrate identity: PASS')

nu0,sg0,si0,q0,L0,k0,n0=.255,10.,1.3,1.,20.,10.,2
xstar=(nu0+si0)/(sg0-nu0-si0)

def rhs(lamb):
 def f(t,u):
  x,y=u
  h=x*(x+1)*(y+1)**2/(L0+(x+1)**2*(y+1)**2)
  r=y**n0/(k0**n0+y**n0)
  return [nu0-sg0*h+si0*r,q0*(sg0*h-si0*r)-lamb*y]
 return f
for lam in [0.,-.2,.1]:
 sol=solve_ivp(rhs(lam),(0,300),(2.,15.),method='DOP853',rtol=2e-9,atol=2e-11,dense_output=True,max_step=.2)
 assert sol.success and min(sol.y[0])>0 and min(sol.y[1])>0
 if lam==0.:
  M=sol.y[0]+sol.y[1]/q0
  assert max(abs(M-(17.+nu0*sol.t))) < 1e-5
  assert abs(sol.y[0,-1]-xstar)<0.12  # finite-horizon proximity for this example
 elif lam<0:
  # Near the endpoint, the product exhibits exponential growth; ratio is bounded positive.
  assert sol.y[1,-1]>1e10
  assert sol.y[0,-1]>0
 else:
  assert max(sol.y[0])<100 and max(sol.y[1])<1000
 print(f'Illustrative IVP, lambda={lam}: x(T)={sol.y[0,-1]:.8g}, y(T)={sol.y[1,-1]:.8g}')
print('All standalone checks passed. Numerical samples are not substitutes for global asymptotic proof.')
