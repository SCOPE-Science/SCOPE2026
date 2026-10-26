#!/usr/bin/env python3
"""Reproduce linear-envelope speed and sharp mixture thresholds for a two-pathway population model.
Standard-library implementation; finite tests are supplemental, not an exhaustive proof.
"""
import math
import random


def bisect(f, lo, hi, steps=90):
    a, b = f(lo), f(hi)
    assert a <= 0 < b or a >= 0 > b, (lo, hi, a, b)
    sign = 1 if a < 0 else -1
    for _ in range(steps):
        m = (lo + hi) / 2
        if sign * f(m) < 0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def log_growth(t, R, s, theta):
    A = R*(1-theta)*math.cosh(t)
    B = R*s*theta*math.cosh(2*t)
    L = (A + math.sqrt(A*A+4*B))/2
    At = R*(1-theta)*math.sinh(t)
    Bt = 2*R*s*theta*math.sinh(2*t)
    gt = (At*L+Bt)/((2*L-A)*L)
    return math.log(L), gt


def speed(R, s, theta):
    def psi(t):
        g, gt = log_growth(t, R, s, theta)
        return t*gt-g
    hi=1.
    while psi(hi) < 0:
        hi*=2
        assert hi <= 32
    t=bisect(psi, 1e-8, hi)
    return log_growth(t,R,s,theta)[0]/t, t


def base(R):
    def hh(t):
        return t*math.tanh(t)-math.log(math.cosh(t)) -math.log(R)
    hi=1.
    while hh(hi)<0:
        hi*=2
    t=bisect(hh,1e-10,hi)
    return math.tanh(t), t


def sc(R):
    v,_=base(R)
    return R/(1+v*v)


def opt(R,s):
    u=math.sqrt(R/s-1)
    t=math.atanh(u)
    z=math.tanh(2*t)
    v=math.log(R*math.cosh(t))/t
    theta=(v-u)/(2*z-u-v)
    return theta,v,t


def near(a,b,atol=3e-10):
    assert abs(a-b)<atol, (a,b,a-b)


def tests():
    rng=random.Random(451019)
    m=0
    for i in range(900):
        R=rng.uniform(1.02,1.95)
        s=rng.uniform(1/R+0.0001*(1-1/R),1)
        th=rng.random()
        t=rng.uniform(.001,5)
        g,gt=log_growth(t,R,s,th)
        step=1e-5
        deriv=(log_growth(t+step,R,s,th)[0]-log_growth(t-step,R,s,th)[0])/(2*step)
        near(gt,deriv,1e-7)
        base_speed,_=base(R)
        near(speed(R,s,0)[0],base_speed)
        near(speed(R,s,1)[0],base(R*s)[0])
        near(math.exp(g)**2, R*(1-th)*math.cosh(t)*math.exp(g)+R*s*th*math.cosh(2*t),1e-7*math.exp(2*g))
        m+=4
    for i in range(90):
        R=rng.uniform(1.06,1.90)
        scl=sc(R)
        for s in [1/R+0.08*(scl-1/R), (1/R+scl)/2,scl]:
            c0=base(R)[0]
            for th in [0.1,0.35,0.7,1]:
                c,_=speed(R,s,th)
                assert c < c0 + 2e-10, (R,s,th,c,c0)
                if th>0:
                    assert c<c0+1e-11
                m+=1
        for s in [scl + .17*(1-scl), scl+.45*(1-scl), 1]:
            th,v,t=opt(R,s)
            assert 0<th<1, (R,s,th)
            near(speed(R,s,th)[0],v)
            assert v>base(R)[0] + 1e-12
            for d in [.005,.04,.15,.5]:
                if th-d>=0:
                    assert speed(R,s,th-d)[0]<v
                if th+d<=1:
                    assert speed(R,s,th+d)[0]<v
                m+=1
    tcrit=bisect(lambda t: t-math.tanh(2*t), .1, 1.8)
    rcrit=math.exp(tcrit*math.tanh(tcrit))/math.cosh(tcrit)
    scrit=sc(rcrit)
    near(tcrit,.9575040240772689,2e-11)
    near(rcrit,1.363120373806496,2e-11)
    near(scrit,.8781357139504142,2e-11)
    for r in [1.0001,1.02,1.1,1.2,1.5,1.7,1.95,1.99]:
        assert sc(r)>scrit and sc(r)<1
    th,v,t=opt(1.5, .95)
    near(th, .2398051574096375)
    near(v,.8393775407107661)
    near(base(1.5)[0],.8326269598360458)
    near(base(1.5*.95)[0],.7871496866195206)
    print('PASS: 900 spectral/derivative/pure-channel checks, 90 models in each regime and threshold checks; comparisons:',m)
    print('universal minimizer (t,R,s_min):',tcrit,rcrit,scrit)
    print('R=1.5,s=.95: theta_opt,speed:',th,v)

if __name__=='__main__':
    tests()
