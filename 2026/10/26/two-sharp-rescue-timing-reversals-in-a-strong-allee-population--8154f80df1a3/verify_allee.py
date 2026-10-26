"""Reproducible checks for a fixed-amplitude strong-Allee pulse timing theorem.
These finite numerical checks supplement the analytical proof; they do not establish its universal quantifiers.
"""
import math
import random
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def flow(x, a, rate, horizon):
    return float(solve_ivp(
        lambda _t, y: [rate*y[0]*(y[0]-a)*(1-y[0])],
        (0.0, horizon), [x], rtol=2e-12, atol=2e-14,
    ).y[0, -1])


def delta(x,a,q,rate,t):
    return flow(x+q,a,rate,t)-flow(x,a,rate,t)-q


def analytic_example():
    q=0.2
    t=2*math.log(2)
    def F(x):
        y=2*x-1
        return 0.5*(1+y/math.sqrt(0.5+0.5*y*y))
    def d(x):return F(x+q)-F(x)-q
    lo=brentq(d,0.0,0.4,xtol=1e-15)
    hi=brentq(d,0.4,0.8,xtol=1e-15)
    assert abs(lo+hi-0.8)<1e-13
    assert abs(lo-0.1450297056066189501)<1e-13
    assert d(0)<0<d(0.4) and d(0.8)<0
    return lo,hi


def parameter_sweep():
    rng=random.Random(46022)
    checks=0
    for k in range(96):
        a=rng.uniform(0.1,0.9)
        q=rng.uniform(0.01,0.80*min(a,1-a))
        rate=rng.uniform(0.6,2)
        t=rng.uniform(0.13,3.5)
        f=lambda x:delta(x,a,q,rate,t)
        mid=a-q/2
        assert f(0)<0<f(mid) and f(1-q)<0
        lo=brentq(f,0,mid,xtol=4e-13)
        hi=brentq(f,mid,1-q,xtol=4e-13)
        assert 0<lo<a-q<a<hi<1-q
        # Derivative-sampling-independent sign cross test on both intervals.
        grid=[(1-q)*j/100 for j in range(101)]
        signs=[f(x)>0 for x in grid]
        changes=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
        assert changes==2, (k, a,q,rate,t,lo,hi,changes)
        assert f((lo+hi)/2)>0
        checks+=1
    return checks

if __name__=='__main__':
    print('SYMMETRIC_EXAMPLE',analytic_example())
    print('RANDOM_PARAMETER_TRIPLES',parameter_sweep())
    print('VERIFICATION_OK')
