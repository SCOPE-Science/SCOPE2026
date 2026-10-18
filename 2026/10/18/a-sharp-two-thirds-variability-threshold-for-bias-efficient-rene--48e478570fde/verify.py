#!/usr/bin/env python3
"""Standalone numerical checks for the renewal-bias efficiency transition.

This script verifies algebraic/numerical identities and finite-cycle examples;
the all-parameter uniqueness theorem is proved analytically in RESULT.md.
"""
import math
import random


def cost(m):
    return 2*m*math.atanh(m)


def efficiency(m,b,mean2_over_A=1):
    return mean2_over_A*m/((1-(1-b)*m*m)*math.atanh(m))


def tval(m):
    return (1-m*m)*math.atanh(m)/m


def g(m):
    t=tval(m)
    return (1-t)/(m*m*(1+t))


def stationary_root(b):
    assert 0 < b < 2/3
    left,right=0.001,1-1e-13
    for _ in range(100):
        middle=(left+right)/2
        if g(middle) < 1-b: left=middle
        else: right=middle
    return (left+right)/2


def golden_max(fn,left,right):
    ratio=(math.sqrt(5)-1)/2
    c=right-ratio*(right-left)
    d=left+ratio*(right-left)
    for _ in range(110):
        if fn(c)<fn(d):
            left=c;c=d;d=left+ratio*(right-left)
        else:
            right=d;d=c;c=right-ratio*(right-left)
    return (left+right)/2


def cycle_coeff(nr_law):
    # Triples (probability,duration,reward): a bounded independent cycle law.
    en=sum(w*n for w,n,r in nr_law)
    er=sum(w*r for w,n,r in nr_law)
    A=sum(w*r*r for w,n,r in nr_law)
    rho=er/en
    B=sum(w*(r-rho*n)**2 for w,n,r in nr_law)
    return en,er,A,B


def test():
    count=0
    laws=[[(.5,1,1),(.5,1,3)],[(.9,1,0),(.1,1,10)],[(1.0,1,1)],[(.5,1,1),(.5,2,3)],[(.2,1,3),(.3,2,5),(.5,3,2)]]
    for law in laws:
        en,er,A,B=cycle_coeff(law)
        b=B/A
        for m in (.02,.21,.57,.83,.97):
            mean_j=m*er/en
            asymptotic_var=((1-m*m)*A+m*m*B)/en
            direct=sum(w*sum(p*(x*r-mean_j*n)**2 for p,x in (((1+m)/2,1),((1-m)/2,-1))) for w,n,r in law)/en
            assert abs(direct-asymptotic_var)<2e-12
            assert abs(2*mean_j**2/(asymptotic_var*(cost(m)/en))-efficiency(m,b,er*er/A))<3e-12
            count+=2
    for b in (.01,.05,.2,.5,.65):
        root=stationary_root(b)
        numeric=golden_max(lambda m:efficiency(m,b),1e-4,1-1e-12)
        assert abs(root-numeric)<5e-7,(b,root,numeric)
        assert efficiency(root,b)>1
        count+=3
    for b in (2/3,.7,.9,1,4):
        vals=[efficiency(i/100,b) for i in range(1,100)]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
        count+=1
    for b in (0,.1,.4,.8):
        for i in range(2,90):
            m=i/100
            h=1e-6
            deriv=(efficiency(m+h,b)-efficiency(m-h,b))/(2*h)
            expected=math.copysign(1.0,(1-b)-g(m))
            assert (deriv>0)==(expected>0),(b,m,deriv,expected)
            count+=1
    assert efficiency(.99999,0)>efficiency(.99,0)*4
    count+=1
    # Independent finite-cycle Monte Carlo moment check for an irregular bounded law.
    law=[(.2,1,3),(.3,2,5),(.5,3,2)]
    rng=random.Random(281828)
    m=.4
    en,er,A,B=cycle_coeff(law)
    times=[]
    drifts=[]
    cumsum=0
    for _ in range(120000):
        u=rng.random()
        n,r=(1,3) if u<.2 else ((2,5) if u<.5 else (3,2))
        x=1 if rng.random()<(1+m)/2 else -1
        times.append(n)
        drifts.append(x*r-(m*er/en)*n)
    emp=sum(y*y for y in drifts)/sum(times)
    theory=((1-m*m)*A +m*m*B)/en
    assert abs(emp/theory-1)<.025,(emp,theory)
    count+=1
    print(f'PASS: {count} deterministic assertions; simulated ratio={emp/theory:.7f}')
    print('Representative b=0.2: m*=',stationary_root(.2),'gain=',efficiency(stationary_root(.2),.2))
    print('Representative b=0.5: m*=',stationary_root(.5),'gain=',efficiency(stationary_root(.5),.5))


if __name__=='__main__':
    test()
