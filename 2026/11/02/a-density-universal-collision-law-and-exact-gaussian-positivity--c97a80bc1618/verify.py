#!/usr/bin/env python3
"""Standalone numerical consistency checks for affine least-norm quadrature."""
import math
import random

COUNT = 0

def near(a, b, tol=1e-10):
    global COUNT
    COUNT += 1
    if not math.isfinite(a) or abs(a-b) > tol:
        raise AssertionError((a, b, tol))

def simpson(fun, lo, hi, n=60000):
    if n % 2: n += 1
    h = (hi-lo)/n
    s = fun(lo) + fun(hi)
    for j in range(1, n):
        s += (4 if j & 1 else 2) * fun(lo+j*h)
    return s*h/3

def calc_weights(xs):
    n = len(xs)
    m = sum(xs)/n
    s = sum((x-m)**2 for x in xs)
    if s <= 0: raise ValueError('duplicate nodes')
    w = [1/n - m*(x-m)/s for x in xs]
    return m, math.sqrt(s), [(x-m)/math.sqrt(s) for x in xs], w

def run():
    global COUNT
    rng = random.Random(20261025)
    for n in (2,3,4,5,8):
        for k in range(250):
            xs=[rng.gauss(0,1) for _ in range(n)]
            m,r,a,w=calc_weights(xs)
            if r < 0.05: continue # Avoid machine-cancellation cases when checking exact algebra.
            near(sum(w), 1, 2e-11)
            near(sum(x*y for x,y in zip(xs,w)), 0, 2e-11)
            near(sum(a), 0, 2e-11)
            near(sum(x*x for x in a), 1, 2e-11)
            near(sum(x*y for x,y in zip(w,a)), -m/r, 2e-11)
            kappa=sum(map(abs,w))
            major=abs(m)*sum(map(abs,a))/r
            if not (major-1-1e-12 <= kappa <= major+1+1e-12):
                raise AssertionError('polar sandwich')
            COUNT += 1
    # Two-point angular counting measure, three-point angular integral.
    sphere2=2*math.sqrt(2)
    c2=(math.sqrt(2)*math.gamma(1)/(2*math.pi))*sphere2
    near(c2, 2/math.pi)
    def a3(th):
        return [math.sqrt(2/3)*math.cos(th-2*math.pi*j/3) for j in range(3)]
    # Absolute cosine products have finitely many kinks; sufficiently fine
    # Simpson nodes give an independent geometric numerical check.
    sphere3=simpson(lambda th: sum(abs(x) for x in a3(th))**2,0,2*math.pi)
    exact_sphere3=4*math.sqrt(3)+8*math.pi/3
    near(sphere3, exact_sphere3, 2e-8)
    c3=exact_sphere3/(12*math.pi)
    near(c3, 2/9+math.sqrt(3)/(3*math.pi))
    # Gaussian integral: direct integration versus analytic gamma expression.
    for n in (2,3,4):
        f=lambda x: math.exp(-n*x*x/2)/(2*math.pi)**(n/2)*abs(x)**(n-1)
        integ=simpson(f,-11,11,30000)
        expected=math.gamma(n/2)/(n*math.pi)**(n/2)
        near(integ, expected, 1e-8)
    p=3/math.pi*simpson(lambda t: 1/math.sqrt(1+2*math.cos(t)**2),0,math.pi/3)
    near(p, 0.6542087649561548, 2e-12)
    # Direct independent MC with standard Gaussian nodes (no angle model).
    ntrials=280000
    positive=0
    feasible=0
    for _ in range(ntrials):
        xs=[rng.gauss(0,1) for _ in range(3)]
        _,_,_,w=calc_weights(xs)
        positive += all(z>0 for z in w)
        feasible += min(xs)<0<max(xs)
    observed_pos=positive/ntrials
    observed_feasible=feasible/ntrials
    near(observed_pos,p,0.006)
    near(observed_feasible,0.75,0.006)
    print('PASS:',COUNT,'deterministic or seeded numerical checks')
    print('Gaussian p3 analytic',format(p,'.15f'),'sample',format(observed_pos,'.6f'))
    print('Gaussian c2/c3',format(c2,'.12f'),format(c3,'.12f'))
    print('convex feasible analytic 0.75 sample',format(observed_feasible,'.6f'))

if __name__=='__main__':
    run()
