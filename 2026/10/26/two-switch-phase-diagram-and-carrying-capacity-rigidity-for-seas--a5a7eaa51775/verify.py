#!/usr/bin/env python3
"""Independent arithmetic checks for the two-season Ricker ordering theorem.

Standard Python library only. Finite tests do not replace the analytic proof.
"""
import math
import random


def F(R, a, x):
    return R*x*math.exp(-a*x)


def g(a,b,r1,r2,x):
    return (b-a)+a*r2*math.exp(-b*x)-b*r1*math.exp(-a*x)


def logratio(a,b,r1,r2,x):
    left=F(r2,b,F(r1,a,x))
    right=F(r1,a,F(r2,b,x))
    return math.log(left/right)/x


def bisect(f, lo, hi):
    f0=f(lo)
    assert f0*f(hi)<0
    for _ in range(110):
        mid=(lo+hi)/2
        if f0*f(mid)<=0:
            hi=mid
        else:
            lo=mid;f0=f(mid)
    return (lo+hi)/2


def run():
    rng=random.Random(9292025)
    # Direct composition versus closed-form analytic log-ratio, away from underflow.
    for _ in range(12000):
        a=math.exp(rng.uniform(-2,0.4))
        b=a+math.exp(rng.uniform(-2,0.4))
        r1=math.exp(rng.uniform(-1,1.7))
        r2=math.exp(rng.uniform(-1,1.7))
        x=math.exp(rng.uniform(-3,0.8))
        observed=logratio(a,b,r1,r2,x)
        theory=g(a,b,r1,r2,x)
        assert math.isclose(observed,theory,rel_tol=3e-10,abs_tol=3e-12),(a,b,r1,r2,x,observed,theory)
    # Exact witness via closed-form roots of 7y^2-8y+2=0.
    lo=math.log(7/(4+math.sqrt(2)))
    hi=math.log(7/(4-math.sqrt(2)))
    assert 0<lo<hi
    assert abs(g(1,2,2,3.5,lo))<1e-14
    assert abs(g(1,2,2,3.5,hi))<1e-14
    assert g(1,2,2,3.5,lo/2)>0
    assert g(1,2,2,3.5,(lo+hi)/2)<0
    assert g(1,2,2,3.5,2*hi)>0
    # Random interior phase points: exact criterion plus two numerically bracketed roots.
    for _ in range(2500):
        a=rng.uniform(.3,1.2)
        b=a+rng.uniform(.4,1.5)
        r1=rng.uniform(1.2,2.5)
        low=1+b/a*(r1-1)
        high=r1**(b/a)
        r2=low+.5*(high-low)
        star=math.log(r2/r1)/(b-a)
        assert g(a,b,r1,r2,0)>0 and g(a,b,r1,r2,star)<0
        assert g(a,b,r1,r2,star+max(10/a,10/b))>0
        left=bisect(lambda x:g(a,b,r1,r2,x),0,star)
        right=bisect(lambda x:g(a,b,r1,r2,x),star,star+max(10/a,10/b))
        assert 0<left<star<right
    # Common carrying capacity: sign globally nonnegative, unique zero at K.
    for _ in range(6000):
        a=rng.uniform(.1,1.6)
        b=a+rng.uniform(.05,2)
        k=rng.uniform(.2,2)
        r1=math.exp(a*k);r2=math.exp(b*k)
        x=rng.uniform(.00001,5)
        assert g(a,b,r1,r2,x)>-2e-13
        assert abs(g(a,b,r1,r2,k))<2e-13
    # Validate saddle-node square-root onset numerically.
    for delta in (.004,.002,.0004,.00008):
        a,b,r1=1.,2.,2.
        r2=r1**(b/a)*math.exp(-delta)
        star=math.log(r2/r1)/(b-a)
        l=bisect(lambda x:g(a,b,r1,r2,x),0,star)
        h=bisect(lambda x:g(a,b,r1,r2,x),star,star+1)
        pred=math.sqrt(2*delta/(b*(b-a)))
        assert abs((star-l)/pred-1)<.05
        assert abs((h-star)/pred-1)<.05
    # Algebraic structural comparator: Beverton-Holt commutator sign is constant.
    def h(r,a,x):return r*x/(1+a*x)
    for _ in range(2000):
        a=rng.uniform(.1,2);b=rng.uniform(.2,3)
        r1=rng.uniform(.2,3);r2=rng.uniform(.2,3)
        x=rng.uniform(.01,10)
        v=h(r2,b,h(r1,a,x))-h(r1,a,h(r2,b,x))
        exact=(r1*r2*x)*((b+a*r2)-(a+b*r1))*x / ((1+(a+b*r1)*x)*(1+(b+a*r2)*x))
        assert math.isclose(v,exact,rel_tol=5e-11,abs_tol=5e-13)
    print('PASS: 12000 identity, 2500 phase, 6000 rigidity, 4 onset, 2000 BH checks, exact witness')


if __name__=='__main__':run()
