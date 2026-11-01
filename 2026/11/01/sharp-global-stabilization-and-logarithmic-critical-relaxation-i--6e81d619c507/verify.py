#!/usr/bin/env python3
"""Reproducibility checks for a quadratic Lorenz-like flow.

This checks finite symbolic identities and finite numerical illustrations.
It is not a computer-assisted proof of global convergence.
"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

X,Y,Z,a,b,c,q,u = sp.symbols('X Y Z a b c q u', real=True)
dX=-a*X+Y*Z
dY=X*(b-Z)
dZ=-Z+X*Y+c
V=(X*X+(1+q)*Y*Y+q*(Z-c)**2)/2
dV=sp.expand(sp.diff(V,X)*dX+sp.diff(V,Y)*dY+sp.diff(V,Z)*dZ)
assert sp.simplify(dV.subs(q,b/(c-b)) + a*X**2 + b/(c-b)*(Z-c)**2)==0
w=Z-b
Vcritical=(Y*Y+(Z-b)**2)/2
assert sp.simplify(sp.diff(Vcritical,X)*dX+sp.diff(Vcritical,Y)*dY+sp.diff(Vcritical,Z)*dZ+w*w).subs(c,b)==0

A=b/a
B=b*(a*a+b*b)/a**4
D=b*(a*a+2*a*b*b+b*b)/a**4
H=A*u+B*u**3
W=A*u**2+D*u**4
U=-H*W
Xeq=-a*H+b*u+u*W
Weq=-W+H*u
hres=sp.Poly(sp.expand(Xeq-sp.diff(H,u)*U),u)
wres=sp.Poly(sp.expand(Weq-sp.diff(W,u)*U),u)
for j in range(5): assert sp.simplify(hres.coeff_monomial(u**j))==0
for j in range(6): assert sp.simplify(wres.coeff_monomial(u**j))==0
k=b*b/a**2
ell=2*b*b/a**3+2*b**4/a**4+2*b**4/a**5
assert sp.simplify(sp.expand(U).coeff(u,3)+k)==0
assert sp.simplify(sp.expand(U).coeff(u,5)+ell)==0
assert sp.simplify(ell/k-2*(a*a+a*b*b+b*b)/a**3)==0

# Check the two noncentral equilibria algebraically at a sample parameter.
for xx in [np.sqrt(3*2/2),-np.sqrt(3*2/2)]:
    yy=2*xx/3
    zz=3
    assert abs(-2*xx+yy*zz)<1e-12
    assert abs(xx*(3-zz))<1e-12
    assert abs(-zz+xx*yy+1)<1e-12

# Numerical checks are finite examples, not global certificates.
def rhs(t,v,av,bv,cv):
    x,y,z=v
    return [-av*x+y*z,x*(bv-z),-z+x*y+cv]
for av,bv,cv,initial in [(2.,3.,3.,[.1,.2,3.05]),
                          (1.,1.,1.,[.1,.2,1.05]),
                          (3.,1.,1.,[.1,.2,1.05])]:
    sol=solve_ivp(rhs,(0,4000),initial,args=(av,bv,cv),rtol=5e-12,atol=2e-13,
                  t_eval=[1500,3000,4000],method='DOP853')
    assert sol.success
    leading=2*bv*bv/av**2
    logarithm=2*(av*av+av*bv*bv+bv*bv)/av**3
    vals=[1/float(y*y)-leading*float(t)-logarithm*np.log(float(t))
           for y,t in zip(sol.y[1],sol.t)]
    assert abs(vals[-1]-vals[-2])<1.0, (av,bv,vals)
    assert max(abs(v) for v in vals)<100, (av,bv,vals)
    print('critical', av,bv,'inverse-square residuals',np.array(vals))
sol=solve_ivp(rhs,(0,200),[2.,-1.,10.],args=(2.,3.,4.),rtol=1e-11,atol=1e-12)
assert sol.success and np.linalg.norm(sol.y[:,-1]-np.array([0.,0.,4.]))<1e-6
print('symbolic identities and finite trajectory checks passed')
