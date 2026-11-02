"""Supplementary numerical and exact-arithmetic checks for the quadratic operator.
Requires only the Python standard library. This is supplementary, not a proof.
"""
from fractions import Fraction as Q
from math import log, exp, isclose
from random import Random


def H(x, theta):
    s = sum(x)
    return [theta[i]*x[i]*(s - x[i]/2) for i in range(len(x))]

def proj(p, theta):
    a=sum(theta[i]*p[i]*(1-p[i]/2) for i in range(len(p)))
    return ([theta[i]*p[i]*(1-p[i]/2)/a for i in range(len(p))],a)

def phi(p,theta):
    # integral_0^u log(1-t/2) dt = -2*(1-u/2)*log(1-u/2)-u
    return sum(p[i]*log(theta[i]) - 2*(1-p[i]/2)*log(1-p[i]/2)-p[i]
                for i in range(len(p)))

def waterfill(theta,support):
    lo=0.0; hi=max(theta)
    for k in range(90):
        mid=(lo+hi)/2
        t=sum(2*max(0,1-mid/theta[i]) for i in support)
        if t>1: lo=mid
        else: hi=mid
    lam=(lo+hi)/2
    return [2*max(0,1-lam/theta[i]) if i in support else 0 for i in range(len(theta))],lam

def logcrit(p,theta,N):
    acc=0.0
    for j in range(N):
        p,a=proj(p,theta)
        acc+=2**(-j-1)*log(a)
    return -acc

rng=Random(729194)
count_exact=0; count_float=0; count_mirror=0; count_direction=0
for n in range(2,9):
    for trial in range(18):
        theta=[Q(rng.randint(1,15),rng.randint(2,10)) for _ in range(n)]
        x=[Q(rng.randint(0,12),rng.randint(1,8)) for _ in range(n)]
        if not any(x): x[0]=Q(1)
        s=sum(x)
        p=[z/s for z in x]
        a=sum(theta[i]*p[i]*(1-p[i]/2) for i in range(n))
        y=H(x,theta)
        assert sum(y)==s*s*a
        pp=[theta[i]*p[i]*(1-p[i]/2)/a for i in range(n)]
        assert y==[sum(y)*v for v in pp]
        count_exact+=1
        th=[float(z) for z in theta]
        pf=[float(z) for z in p]
        for _ in range(50):
            new,af=proj(pf,th)
            assert abs(sum(new)-1)<1e-12
            assert phi(new,th)+1e-12>=phi(pf,th)
            count_mirror+=1
            pf=new
        target,lam=waterfill(th,{i for i in range(n) if x[i]>0})
        for _ in range(4500):
            pf,af=proj(pf,th)
        assert max(abs(pf[i]-target[i]) for i in range(n))<1.6e-3, (th, p, pf, target)
        count_direction+=1
        lc=logcrit([float(v) for v in p],th,60)
        ltail=logcrit([float(v) for v in p],th,24)
        B=max(abs(log(min(th)/2)),abs(log(max(th))))
        assert abs(lc-ltail) < (2**-24)*B+1e-11
        v=[float(z) for z in p]
        l0=lc
        for step in range(12):
            w,aa=proj(v,th)
            lnext=logcrit(w,th,60)
            assert abs(lnext-(2*l0+log(aa)))<1e-11
            v,l0=w,lnext
            count_float+=1
print('PASS exact decomposition',count_exact,'cases; monotone potential',count_mirror,
      'steps; direction convergence',count_direction,'cases; radial cocycle',count_float,'steps')
