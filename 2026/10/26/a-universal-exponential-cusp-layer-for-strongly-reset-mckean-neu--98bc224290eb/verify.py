"""Independent finite-volume and analytic checks for cusp-layer asymptotics.

Requires Python 3, numpy and scipy. Tests support, but do not prove, the limit.
"""
import math
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.integrate import quad

A, M0, ML, MR = 0.35, 1.14, -2.0, -2.0
D, I0, W = 0.5, 0.0, 0.35
b = math.sqrt(D)
checks = 0
for z in (-2.0,-1.0,0.0,0.4,1.0,2.0):
    rho = lambda t: math.exp(-abs(t)/b)/(2*b)
    lhs = quad(lambda t: max(z+t,0)*rho(t),-60,60,epsabs=1e-11)[0]-max(z,0)
    rhs = b*math.exp(-abs(z)/b)/2
    assert abs(lhs-rhs)<1e-9,(z,lhs,rhs)
    checks += 1
for t in (0.25,0.7,1.6,3.):
    lhs = quad(lambda u: math.cos(t*u)*math.exp(-abs(u)/b)/(2*b),-60,60)[0]
    assert abs(lhs-1/(1+D*t*t))<1e-9
    checks += 1
x=np.linspace(-1.15,1.85,6001)
h=x[1]-x[0]
n=len(x)
f=np.where(x<-A,ML*x-A*(M0-ML),np.where(x<=A,M0*x,MR*x+A*(M0-MR)))
g=f+I0-W
up=D/h**2+g[:-1]/(2*h)
lo=D/h**2-g[1:]/(2*h)
assert min(up)>0 and min(lo)>0
dg=np.zeros(n);dg[:-1]-=up;dg[1:]-=lo
QT=diags([up,dg,lo],[-1,0,1],format='csc')
for r in (64,256,625):
    R=r*diags([np.ones(n)],[0],format='csc')-QT
    for z in (-1.,0.,1.):
        reset=A+z/math.sqrt(r)
        idx=int((reset-x[0])/h)
        mix=(reset-x[idx])/h
        injection=np.zeros(n)
        injection[idx]=r*(1-mix)
        injection[idx+1]=r*mix
        pi=spsolve(R,injection)
        assert abs(pi.sum()-1)<1e-8
        checks += 1
        mu=x@pi
        f_reset=np.interp(reset,x,f)
        scaled=r**1.5*(mu-reset-(f_reset+I0-W)/r)
        prediction=(MR-M0)*math.sqrt(D)/2*math.exp(-abs(z)/math.sqrt(D))
        bound={64:0.060,256:0.018,625:0.009}[r]
        assert abs(scaled-prediction)<bound,(r,z,scaled,prediction)
        checks += 1
print(f'PASS: {checks} analytic and finite-volume check assertions')
