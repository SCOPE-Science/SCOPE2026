"""Numerical and exact-rational diagnostics for the two-time reset ABP sign theorem.

Run: python check.py (requires numpy). Independent science rests on the proof,
not finite numerical checks.
"""
from fractions import Fraction as F
import math
import numpy as np


def facts(k,a,r,v,D):
    p=r/(r+a)
    q=(r+2*a)/(r+4*a)
    z=2*a/(r+4*a)
    m=v*p/(k+r)
    H=v*q/(k+a+r)
    G=v*z/(k+a+r)
    J=H-m*p
    V=(2*D+2*v*H)/(2*k+r)-m*m
    VY=(2*D+2*v*G)/(2*k+r)
    return p,q,z,m,H,G,J,V,VY


def polynomial(k,a,r):
    return r**3-a*r*r-(2*a*a+5*a*k)*r-2*a*a*k


def sign_factor(k,a,r,v,D):
    p,q,z,m,H,G,J,V,VY=facts(k,a,r,v,D)
    if k>=a:
        return (J<0)
    return J<0 and V+v*J/(a-k)<0


def phi(k,a,r,h):
    if k==a:
        return h*math.exp(-(k+r)*h)
    return math.exp(-(k+r)*h)*math.expm1((k-a)*h)/(k-a)


def corr(k,a,r,v,D,h):
    p,q,z,m,H,G,J,V,VY=facts(k,a,r,v,D)
    return V*math.exp(-(k+r)*h)+v*J*phi(k,a,r,h), VY*math.exp(-(k+r)*h)+v*G*phi(k,a,r,h)


# Exact rational cross checks against the cubic and the direct moment formulas.
n=0
for k in (F(1,3),F(1,2),F(1),F(2),F(3)):
  for a in (F(1,2),F(1),F(3,2)):
    for r in (F(1,3),F(1),F(2),F(4),F(10),F(100)):
      p,q,z,m,H,G,J,V,VY=facts(k,a,r,F(2),F(1,13))
      Jpoly=-F(2)*a*polynomial(k,a,r)/((r+a)**2*(r+4*a)*(r+k)*(r+k+a))
      assert J==Jpoly
      assert V>0 and VY>0 and G>0 and p>0 and q>0 and z>0
      assert (J<0)==(polynomial(k,a,r)>0)
      n+=1
print('Exact rational moment/cubic identities:', n)

# Explicit reentrant longitudinal sign phase at nonzero translational noise.
k,a,v,D=F(1,2),F(1),F(1),F(1,200)
expected={1:False,10:True,100:False}
for r,negative in expected.items():
    p,q,z,m,H,G,J,V,VY=facts(k,a,F(r),v,D)
    late=V+v*J/(a-k)
    assert (late<0)==negative
    assert sign_factor(k,a,F(r),v,D)==negative
    print('Reentrant exact case r=',r,'slow mode numerator=',late)

# Degenerate angular/confinement modes, exact threshold and explicit root.
a=k=1.0
crit=(3+math.sqrt(13))/2
assert abs(polynomial(k,a,crit))<1e-12
assert not sign_factor(k,a,3.0,1.0,0.01)
assert sign_factor(k,a,5.0,1.0,0.01)
for r in (4.0,5.0,10.0,20.0):
    p,q,z,m,H,G,J,V,VY=facts(k,a,r,1.0,0.01)
    t0=V/(-J)
    assert abs(corr(k,a,r,1.0,0.01,t0)[0])<1e-14
    assert corr(k,a,r,1.0,0.01,0.5*t0)[0]>0
    assert corr(k,a,r,1.0,0.01,2*t0)[0]<0
    for t in (0.0,0.2,0.4,1.0,4.0):
        assert corr(k,a,r,1.0,0.01,t)[1]>0
print('Resonant exact-crossing diagnostics: 4 parameter sets')

# Nonresonant strict transition and unique zero for both k>a and k<a.
for k,a,r,v,D in ((2.,1.,8.,1.,.001),(.5,1.,10.,1.,.005)):
    p,q,z,m,H,G,J,V,VY=facts(k,a,r,v,D)
    if k>a:
        t0=math.log1p((k-a)*V/(-v*J))/(k-a)
    else:
        t0=-math.log1p(-(a-k)*V/(-v*J))/(a-k)
    for x in (0,.25,.5):
        assert corr(k,a,r,v,D,t0*x)[0]>0
    assert abs(corr(k,a,r,v,D,t0)[0])<1e-14
    for x in (1.2,1.5,2.0):
        assert corr(k,a,r,v,D,t0*x)[0]<0
    for x in (0.,.25,1.,t0,2*t0):
        assert corr(k,a,r,v,D,x)[1]>0
    print('Unique crossing k,a,r,D =',k,a,r,D,'t0=',t0)

# Independent stationary reset-age Monte Carlo (no moment formulas in sampler).
# Pathwise OU steps and angular Brownian increments; deliberately finite-step.
def stationary_mc(k,a,r,v,D,num=130000,steps=110,seed=41029):
    rng=np.random.default_rng(seed)
    age=rng.exponential(1/r, num)
    dt=age/steps
    decay=np.exp(-k*dt)
    theta=np.zeros(num)
    x=np.zeros(num)
    for i in range(steps):
        incr=np.sqrt(2*a*dt)*rng.standard_normal(num)
        midpoint=theta+incr/2
        x=decay*x+v*np.cos(midpoint)*(1-decay)/k
        if D>0:
            x+=np.sqrt(D/k*(1-decay**2))*rng.standard_normal(num)
        theta+=incr
    c=np.cos(theta)
    return float(x.mean()),float(c.mean()),float(x.var()),float(np.mean((x-x.mean())*(c-c.mean())))
for k,a,r,v,D in ((1.,1.,5.,1.,0.),(2.,1.,8.,1.,0.01)):
    m0,c0,v0,j0=stationary_mc(k,a,r,v,D)
    p,q,z,m,H,G,J,V,VY=facts(k,a,r,v,D)
    print('Stationary MC k,a,r,D:',(k,a,r,D),'mean/cos/var/J:',m0,c0,v0,j0,
          'theory:',m,p,V,J)
    assert abs(m0-m)<0.003
    assert abs(c0-p)<0.004
    assert abs(v0-V)<0.0035
    assert abs(j0-J)<0.0018
print('ALL CHECKS PASSED')
