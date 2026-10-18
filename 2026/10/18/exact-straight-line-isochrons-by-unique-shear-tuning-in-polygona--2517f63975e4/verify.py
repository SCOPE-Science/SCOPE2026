#!/usr/bin/env python3
"""Local exact radial-flight verification for polygonal affine oscillators."""
import cmath
import math
import random


def dot(u,v): return u[0]*v[0]+u[1]*v[1]
def det(u,v): return u[0]*v[1]-u[1]*v[0]

def parameters(vertices,lambdas,omegas):
    result=[]
    for i,p in enumerate(vertices):
        q=vertices[(i+1)%len(vertices)]
        e=(q[0]-p[0],q[1]-p[1]); ell2=dot(e,e)
        C=det(p,q); assert C>0
        a=dot(e,p)/ell2; b=a+1
        kappa=lambdas[i]*ell2; E=math.exp(-kappa/omegas[i]);
        mu=(kappa/C)*(a-b*E)/(-math.expm1(-kappa/omegas[i]))
        result.append((a,b,C,kappa,E,omegas[i],mu))
    return result

def crossing_time(delta,params,mu=None):
    a,b,C,k,E,w,m=params
    if mu is None:mu=m
    # Residual of exact section-crossing equation, not numerically integrated ODE.
    def F(t):
        u=math.exp(-k*t)
        return w*t-1-delta*(b*u-a+(mu*C/k)*(1-u))
    lo=0;hi=3/w
    assert F(lo)<0 and F(hi)>0,(delta,F(lo),F(hi))
    for _ in range(70):
        mid=(lo+hi)/2
        if F(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

count=0
rng=random.Random(314159265)
for N in [3,4,5,6,7,10,15]:
  for trial in range(10):
    # Positive radial samples and an angle gap below pi give star-shaped simple polygons.
    angles=[2*math.pi*i/N for i in range(N)]
    radii=[0.8+0.4*rng.random() for _ in range(N)]
    pts=[(r*math.cos(t),r*math.sin(t)) for r,t in zip(radii,angles)]
    ls=[0.4+1.5*rng.random() for _ in range(N)]
    ws=[0.6+1.4*rng.random() for _ in range(N)]
    pars=parameters(pts,ls,ws)
    P=sum(1/w for w in ws)
    R=math.prod(p[4] for p in pars)
    assert 0<R<1
    for initial_delta in [-1e-3,-1e-5,1e-5,1e-3]:
      v=initial_delta; T=0
      for par in pars:
        t=crossing_time(v,par)
        assert abs(t-1/par[5])<2e-13
        T+=t;v*=math.exp(-par[3]*t)
      assert abs(v-initial_delta*R)<2e-13
      assert abs(T-P)<2e-12
      count+=N
    # Check uniqueness in the constant-flight-time design criterion.
    for a,b,C,k,E,w,m in pars:
      δ=0.0001
      off_m=m+0.17*k/C
      t=crossing_time(δ,(a,b,C,k,E,w,m),off_m)
      assert abs(t-1/w)>1e-8
      count+=1

# Uniform polygon: closed-form hyperbolic-cotangent tuning.
for N in [3,4,6,10]:
  pts=[(math.cos(2*math.pi*j/N),math.sin(2*math.pi*j/N)) for j in range(N)]
  lam=1.25;w=0.9
  pp=parameters(pts,[lam]*N,[w]*N)
  _,_,C,k,E,_,mu=pp[0]
  expected=-k*(1+E)/(2*C*(1-E))
  assert abs(mu-expected)<2e-13
  for par in pp:assert abs(par[-1]-expected)<2e-13
  count+=N
print('PASS',count,'section-flight and tuning tests')
