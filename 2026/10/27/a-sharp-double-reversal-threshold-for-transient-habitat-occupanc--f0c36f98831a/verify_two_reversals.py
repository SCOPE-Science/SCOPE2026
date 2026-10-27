"""Independent arithmetic checks for a two-habitat occupancy-ranking theorem.

This is a finite reproducibility check, not a substitute for the analytical proof.
Requires only Python's standard library.
"""
from fractions import Fraction as Q
import math
import random


def threshold(d, u, v, fast, slow):
    if not (fast > slow > 0 and u > 0 and v > 0):
        return False, None, None
    ratio = fast * u / (slow * v)
    if ratio <= 1:
        return False, None, None
    tmin = math.log(ratio) / (fast - slow)
    m = v * (1 - slow / fast) * ratio ** (-slow / (fast - slow))
    return d + u - v > 0 and 0 < d < m, tmin, m


def delta(t, d, u, v, fast, slow):
    return d + u * math.exp(-fast*t) - v * math.exp(-slow*t)


def bisect(fun, a, b, iters=90):
    x, y = fun(a), fun(b)
    assert x*y < 0
    for _ in range(iters):
        c = (a+b)/2
        z=fun(c)
        if z == 0: return c
        if x*z > 0: a,x=c,z
        else: b,y=c,z
    return (a+b)/2


def exact_example():
    # Habitat 1: r=4, q=3/5, p(0)=4/5.
    # Habitat 2: r=1, q=1/2, p(0)=3/4.
    d,u,v = Q(1,10),Q(1,5),Q(1,4)
    def poly(x): return d+u*x**4-v*x
    assert poly(Q(1)) == Q(1,20)
    assert poly(Q(1,2)) == -Q(1,80)
    assert poly(Q(0)) == Q(1,10)
    assert poly(Q(2,5)) > 0 > poly(Q(1,2))
    assert poly(Q(4,5)) < 0 < poly(Q(9,10))
    ok,tm,m=threshold(float(d),float(u),float(v),4,1)
    assert ok and delta(tm,float(d),float(u),float(v),4,1)<0
    f=lambda t:delta(t,float(d),float(u),float(v),4,1)
    t1=bisect(f,0,tm)
    t2=bisect(f,tm,10)
    assert 0 < t1 < tm < t2
    print('exact rational witness: PASS; roots',format(t1,'.12f'),format(t2,'.12f'))
    # Fold separation at d=m-epsilon: coefficient tends to the predicted constant.
    for eps in (1e-4,1e-5,1e-6):
        g=lambda t:delta(t,m-eps,float(u),float(v),4,1)
        lo=bisect(g,0,tm)
        hi=bisect(g,tm,10)
        prediction=2*math.sqrt(2*eps/(4*1*m))
        assert abs((hi-lo)/prediction - 1) < 0.01
    print('square-root coalescence checks: PASS')


def randomized():
    rng=random.Random(20261023)
    classified=0
    for _ in range(5000):
        q1=rng.uniform(0.02,0.98)
        q2=rng.uniform(0.01,q1)
        p1=rng.random();p2=rng.random()
        r1=math.exp(rng.uniform(-2,2));r2=math.exp(rng.uniform(-2,2))
        d=q1-q2
        if r1>r2: rf,rs,u,v=r1,r2,p1-q1,p2-q2
        else: rf,rs,u,v=r2,r1,q2-p2,q1-p1
        if p1 <= p2: continue
        good,tm,m=threshold(d,u,v,rf,rs)
        if good:
            assert tm > 0 and delta(tm,d,u,v,rf,rs) < -1e-14
            assert delta(0,d,u,v,rf,rs)>0
            assert delta(tm+100/rs,d,u,v,rf,rs)>0
        else:
            grid=[k/(10*rf) for k in range(200)]+[k/(20*rs) for k in range(1,1500)]
            assert min(delta(t,d,u,v,rf,rs) for t in grid)>-1e-12
        classified += 1
    print('randomized strict phase classifications:',classified,'PASS')


if __name__=='__main__':
    exact_example()
    randomized()
