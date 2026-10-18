"""Reproduce analytic and event-driven checks for slow-return telegraph first passage.

Requires: mpmath, scipy, numpy.  All rates are dimensionless when b=c=1.
"""
import math
import random
import mpmath as mp
from scipy.optimize import minimize_scalar, brentq
from scipy.integrate import quad
import numpy as np

mp.mp.dps=55

def terms(z,e):
    z=mp.mpf(z);e=mp.mpf(e)
    w=mp.sqrt(z*(z+2*e))
    A=((1+z/w)*mp.exp(w)-1)/z
    B=2*mp.sinh(w)/w-1+(2*mp.cosh(w)-1)/(z+2*e)
    return A,B

def published(z,e):
    z=mp.mpf(z);e=mp.mpf(e)
    w=mp.sqrt(z*(z+2*e))
    R=1+mp.sqrt(z/(z+2*e))
    A=(R*mp.exp(w)-1)/z
    B=2*R*mp.sinh(w)/w-1+(R-1)*(2*mp.exp(-w)-1)/w
    return A,B

ecrit=mp.findroot(lambda e:8*e**3+12*e**2-3,.44)
g1=lambda e:1+mp.mpf(2)*e/3-1/(4*e**2)
g2=lambda e:e**2/15+e/6+mp.mpf(1)/3+1/(8*e**3)
a=lambda e:(2*e+1)/mp.sqrt(2*e)

assert abs(ecrit-mp.mpf('0.439692620785908'))<mp.mpf('1e-15')
checks=1
for e in [.05,.20,float(ecrit),.9,2.4]:
    for z in [.007,.07,.5,1.4]:
        for x,y in zip(terms(z,e),published(z,e)):
            assert abs(x-y)<mp.mpf('1e-45')
            checks+=1
    assert mp.diff(lambda z:terms(z,e)[1],mp.mpf('.6'),2)>0
    checks+=1

# Symbolic coefficients are checked from independent high-precision limits.
for e in [.20,float(ecrit),1.2]:
    es=mp.mpf(e)
    g0=1+1/(2*es)
    for z0 in [mp.mpf('1e-8'),mp.mpf('1e-10')]:
        B=terms(z0,es)[1]
        assert abs((B-g0)/z0-g1(es))<mp.mpf('1e-6')
        assert abs((B-g0-g1(es)*z0)/z0**2-g2(es))<mp.mpf('1e-6')
        checks+=2

def optimal(e,h):
    e=mp.mpf(e);h=mp.mpf(h)
    f=lambda z:terms(z,e)[0]+h*terms(z,e)[1]
    df=lambda z:mp.diff(f,z)
    lo=mp.mpf('1e-16'); hi=mp.mpf('1')
    while df(hi)<0:hi*=2
    # Derivative starts negative. Bisection requires only the single stationary
    # minimizer established at large h, and is used there.
    for _ in range(140):
        mid=(lo+hi)/2
        if df(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

for e in [mp.mpf('.2'),ecrit,mp.mpf('1')]:
    for h in [mp.mpf('1e5'),mp.mpf('1e7')]:
        zz=optimal(e,h)
        if e>ecrit:
            target=(a(e)/(2*g1(e)))**(mp.mpf(2)/3)
            ratio=zz*h**(mp.mpf(2)/3)/target
        elif e==ecrit:
            target=(a(e)/(4*g2(e)))**(mp.mpf(2)/5)
            ratio=zz*h**(mp.mpf(2)/5)/target
        else:
            eta=mp.findroot(lambda z:mp.diff(lambda t:terms(t,e)[1],z),(.1,.5))
            target=eta
            ratio=zz/target
        assert abs(ratio-1)<(mp.mpf('.18') if h==mp.mpf('1e5') else mp.mpf('.06')),(str(e),str(h),str(ratio))
        checks+=1
        print('asymptotic eps=',mp.nstr(e,9),'h=',mp.nstr(h,6),'z=',mp.nstr(zz,13),'ratio=',mp.nstr(ratio,10))

# Independent killed telegraph-resolvent integration for the failed-cycle
# mean return distance.  qhat(x,z) solves the two-velocity absorbing PDE.
for e,z in [(.20,.60),(.45,.30),(1.1,.85)]:
    w=math.sqrt(z*(z+2*e))
    k=(z+e-w)/e
    q=lambda x: w/(2*z)*(math.exp(-w*abs(x))-k*math.exp(-w*(2-x)))
    massdist=quad(lambda x: z*abs(x)*q(x),-math.inf,0,epsabs=1e-11)[0]
    massdist+=quad(lambda x: z*abs(x)*q(x),0,1,epsabs=1e-11)[0]
    p_hit=math.exp(-w)/(1+z/w)
    assert abs(massdist/p_hit-float(terms(z,e)[1]))<1e-10
    checks+=1

# Independent event-driven trajectories: flips occur at rate e, Poisson
# alarms at rate z, and an alarm entails a ballistic return at speed 1/h.
def simulate(e,z,h,n=42000,seed=47118):
    rng=random.Random(seed)
    total=0.0
    for _ in range(n):
        x=0.0;direction=1 if rng.random()<.5 else -1
        t=0.0
        while True:
            nxt=rng.expovariate(e+z)
            if direction>0 and (1-x)<nxt:
                t+=(1-x)
                break
            x+=direction*nxt;t+=nxt
            if rng.random() < z/(e+z):
                t+=h*abs(x)
                x=0.0
                direction=1 if rng.random()<.5 else -1
            else:
                direction=-direction
        total+=t
    return total/n

for i,(e,z,h) in enumerate([(0.4,.8,0.4),(1.0,0.7,1.5),(0.2,0.6,2.0)]):
    observed=simulate(e,z,h,seed=47118+i)
    A,B=terms(z,e)
    expected=float(A+h*B)
    rel=abs(observed/expected-1)
    print('Monte Carlo eps,z,h=',e,z,h,'observed=',round(observed,7),'expected=',round(expected,7),'relative=',round(rel,6))
    assert rel < .035
    checks+=1

print('PASS',checks,'comparisons; critical epsilon',mp.nstr(ecrit,18))
