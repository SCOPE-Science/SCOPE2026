#!/usr/bin/env python3
"""Independent symbolic and matrix checks for a three-mode resetting walk.

Requires sympy, numpy, and scipy. Execute: python CHECK.py
"""
import sympy as sp
import numpy as np

alpha, beta, rho, diff, vel2, z, prob, t = sp.symbols(
    'alpha beta rho diff vel2 z prob t', positive=True, real=True)
B = beta + rho
L = alpha + beta + rho
H = sp.expand((alpha + rho + diff*z)*(B*B + vel2*z)-alpha*beta*B)
ND = B*L + vel2*z
NV = B*(L + diff*z)
N = sp.expand(prob*ND + (1-prob)*NV)
phi = rho*N/H
ref = rho/(rho+diff*z)
Delta = diff*B-vel2
assert sp.factor(H.subs(z,0)) == rho*B*L
assert sp.simplify(phi.subs(z,0)-1) == 0
assert sp.factor((rho+diff*z)*N-H-Delta*z*(alpha+(1-prob)*(rho+diff*z))) == 0
assert sp.factor((ND-NV)-(vel2-diff*B)*z)==0
assert sp.factor(H.subs(vel2,diff*B)-B*(rho+diff*z)*(L+diff*z))==0
assert sp.factor(N.subs(vel2,diff*B)-B*(L+diff*z))==0
assert sp.simplify(phi.subs(vel2,diff*B)-ref)==0

p0=(beta+prob*rho)/L
pball=(alpha+(1-prob)*rho)/L
variance=sp.factor(-2*sp.diff(phi,z).subs(z,0))
variance_from_generator=2*(diff*p0+vel2*pball/B)/rho
assert sp.simplify(variance-variance_from_generator)==0
assert sp.simplify(variance.subs(vel2,diff*B)-2*diff/rho)==0
assert sp.simplify(p0+pball-1)==0

Cx=sp.exp(-rho*t)*(2*diff/rho+diff*pball*(1-sp.exp(-beta*t))/beta)
Cx0=sp.simplify(Cx.subs(t,0))
Cxp=sp.simplify(sp.diff(Cx,t).subs(t,0))
assert Cx0==2*diff/rho
assert sp.simplify(Cxp+diff*(1+p0))==0
CD=Cx.subs(prob,1)
CV=Cx.subs(prob,0)
assert sp.simplify(CV-CD-rho*diff/(beta*L)*sp.exp(-rho*t)*(1-sp.exp(-beta*t)))==0
recovered=1+alpha/rho-(beta*L/(rho*diff))*(sp.exp(rho*t)*Cx-2*diff/rho)/(1-sp.exp(-beta*t))
assert sp.simplify(recovered-prob)==0
assert sp.simplify(CD-sp.exp(-rho*t)*2*diff/rho-sp.exp(-rho*t)*diff*alpha/(beta*L)*(1-sp.exp(-beta*t)))==0

# Cross-check the rational characteristic function against the uneliminated
# three-state Fourier stationary forward equations at independent parameters.
checks=0
for a,b,r,d in ((2.,3.,1.,5.),(0.8,1.4,2.1,0.25),(7.,0.2,0.03,10.)):
 for v2 in (d*(b+r),d*(b+r)*0.37,d*(b+r)*2.8):
  for q in (0.,0.1,0.8,3.2):
   for pp in (0.,0.25,0.5,0.75,1.):
    A=np.array([[-(r+a+d*q*q),b,b],
                [a/2,-(r+b)+1j*np.sqrt(v2)*q,0],
                [a/2,0,-(r+b)-1j*np.sqrt(v2)*q]],dtype=complex)
    src=r*np.array([pp,(1-pp)/2,(1-pp)/2])
    fnum=sum(np.linalg.solve(A,-src))
    zz=q*q
    HH=(a+r+d*zz)*((b+r)**2+v2*zz)-a*b*(b+r)
    NN=(b+r)*(a+b+r)+(pp*v2+(1-pp)*d*(b+r))*zz
    fclosed=r*NN/HH
    assert abs(fnum-fclosed)<2.e-11, (a,b,r,d,v2,q,pp,fnum,fclosed)
    if abs(v2-d*(b+r))<1.e-12:
     assert abs(fnum-r/(r+d*q*q))<2.e-11
    checks+=1

# Cross-check the autocovariance against a direct 2-by-2 matrix exponential.
from scipy.linalg import expm
for a,b,r,d in ((2.,3.,1.,5.),(0.8,1.4,2.1,0.25),(7.,0.2,0.03,10.)):
 v2=d*(b+r)
 for pp in (0.,0.33,1.):
  bp=(a+(1-pp)*r)/(a+b+r)
  cov0=2*d/r
  cross0=np.sqrt(v2)*bp/(b+r)
  mat=np.array([[-r,np.sqrt(v2)],[0.,-(b+r)]])
  for lag in (0.,0.1,1.,2.,8.):
   numerical=(expm(mat*lag)@np.array([cov0,cross0]))[0]
   analytical=np.exp(-r*lag)*(cov0+d*bp*(1-np.exp(-b*lag))/b)
   assert abs(numerical-analytical)<2.e-10*max(1.,abs(analytical))
   checks+=1
print(f"PASS: rational identities, moment and strict-order formulas; {checks} independent matrix comparisons")
