#!/usr/bin/env python3
"""Self-contained numerical diagnostics for a resetting trapped-boson temporal cross-covariance."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

def formula(r,w,a,h):
    q=r/w
    den=(q*q+1)**2*(q*q+4)
    return 4*a*a*math.exp(-r*h)*((5*q*q+2)*math.cos(w*h)+q*(2*q*q-1)*math.sin(w*h))/den

def integral(r,w,a,h):
    def m(x):return a*(2*math.cos(w*x)-1)
    def avg(f):return quad(lambda x:math.exp(-x)*f(x/r),0,100,epsabs=1e-12,epsrel=1e-12,limit=1500)[0]
    u=avg(m)
    mu_future=avg(lambda x:m(x+h))
    mixed=avg(lambda x:m(x)*m(x+h))
    return math.exp(-r*h)*(mixed-u*mu_future)

checks=0
for r,w,a in [(0.2,1.4,0.7),(0.6,1,1.2),(1,1,1),(3,0.8,0.9),(15,1.2,0.5)]:
    for h in [0,0.12/w,0.7/w,1.6/w,3.0/w,5.3/w]:
        v=formula(r,w,a,h); q=integral(r,w,a,h)
        assert abs(v-q)<2e-10*(1+abs(v)),(r,w,h,v,q)
        checks+=1

r,w,a=0.6,1.3,1.7
q=r/w
C0=formula(r,w,a,0)
assert C0>0
eta=q*(2*q*q-1)/(5*q*q+2)
h0=(math.pi/2+math.atan(eta))/w
assert abs(formula(r,w,a,h0))<1e-12
assert formula(r,w,a,h0+0.1/w)<0 and formula(r,w,a,h0-0.1/w)>0
checks+=3

qstar=math.sqrt((3*math.sqrt(41)-17)/20)
qstatic=math.sqrt((3*math.sqrt(21)-13)/10)
assert 0<qstatic<qstar<1/math.sqrt(2)
firstzero=lambda q: math.pi/2+math.atan(q*(2*q*q-1)/(5*q*q+2))
for q in [qstar/2,qstar*0.9,qstar*1.1,qstar*2,1,4,20]:
    assert firstzero(q)>firstzero(qstar)
    checks+=1
opt=minimize_scalar(firstzero,bounds=(0.0001,12),method='bounded',options={'xatol':1e-12})
assert abs(opt.x-qstar)<5e-7
checks+=1

# Direct trajectory Monte Carlo of stationary age and future reset gap;
# this does not sample from the analytic covariance integrals.
r,w,a,h=1.1,1.8,0.8,0.9
rng=np.random.default_rng(16254)
n=1_000_000
age0=rng.exponential(1/r,n)
reset_after=rng.random(n) > math.exp(-r*h)
age1=age0+h
u=rng.random(reset_after.sum())
age1[reset_after]=-np.log1p(-u*(1-math.exp(-r*h)))/r
x0=a*(2*np.cos(w*age0)-1)
x1=a*(2*np.cos(w*age1)-1)
mc=float((x0*x1).mean()-x0.mean()*x1.mean())
truth=formula(r,w,a,h)
assert abs(mc-truth)<0.007,(mc,truth)
checks+=1
print('PASS',checks,'checks', 'q_earliest',format(qstar,'.14f'), 'q_static',format(qstatic,'.14f'), 'omega_h_min',format(firstzero(qstar),'.14f'), 'mc',format(mc,'.9f'), 'exact',format(truth,'.9f'))
