#!/usr/bin/env python3
"""Reproducible numerical checks for right-truncated exponential-rate mixtures.

The general shape theorem is proved analytically; these finite tests check the
formulas and representative boundary/interior configurations.
"""
import math
import random


def moments(weights, rates, x):
    v = [p * math.exp(-r*x) for p, r in zip(weights, rates)]
    return tuple(sum(z * r**j for z, r in zip(v, rates)) for j in range(4))


def Q(weights, rates, x):
    a,b,c,_ = moments(weights, rates, x)
    return a-b*b/c


def hazard(weights, rates, x, U):
    a,b,_,_ = moments(weights, rates, x)
    return b/(a-moments(weights, rates, U)[0])


def hazard_derivative(weights, rates, x, U):
    a,b,c,_=moments(weights, rates, x)
    return (c*(moments(weights, rates, U)[0]-Q(weights,rates,x)))/(a-moments(weights,rates,U)[0])**2


def bisect_zero(f, a, b, ascending, count=100):
    for _ in range(count):
        m=(a+b)/2
        if (f(m)>0)==ascending:
            b=m
        else:
            a=m
    return (a+b)/2


def critical_cutoff(weights, rates):
    first = sum(p*r for p,r in zip(weights,rates))
    second=sum(p*r*r for p,r in zip(weights,rates))
    H=1-first*first/second
    assert 0 < H < 1
    lo,hi=0.0,1.0
    while moments(weights,rates,hi)[0]>H:
        hi *= 2
    return bisect_zero(lambda U:moments(weights,rates,U)[0]-H,lo,hi,False)


def minimum_location(weights, rates, U):
    aU=moments(weights,rates,U)[0]
    return bisect_zero(lambda x:Q(weights,rates,x)-aU,0.0,U,False)


def near(a,b,rel=1e-8,abs_tol=1e-9):
    return abs(a-b)<=abs_tol+rel*max(abs(a),abs(b))


def main():
    weights=[0.5,0.5]; rates=[1.,2.]
    x=(math.sqrt(1.8)-1)/2
    Uc=-math.log(x)
    assert near(critical_cutoff(weights,rates), Uc,abs_tol=1e-12)
    assert near(Uc,1.767142606336257,abs_tol=1e-12)
    U=3.
    xm=minimum_location(weights,rates,U)
    assert near(xm,1.033068418354241,abs_tol=1e-12)
    assert near(hazard(weights,rates,xm,U),1.415828609472885,abs_tol=1e-11)
    assert hazard(weights,rates,xm,U)<hazard(weights,rates,0,U)
    assert hazard(weights,rates,xm,U)<hazard(weights,rates,2.5,U)
    assert minimum_location(weights,rates,20)/20>0.49999

    rng=random.Random(92148615)
    for test in range(3000):
        k=rng.randrange(2,7)
        rates=sorted([rng.uniform(0.4,2.2) for _ in range(k)])
        ws=[rng.uniform(0.1,1) for _ in range(k)]
        s=sum(ws);weights=[p/s for p in ws]
        Uc=critical_cutoff(weights,rates)
        for U in [0.65*Uc,1.4*Uc]:
            assert U>0
            L=[hazard_derivative(weights,rates,U*z/25,U) for z in range(1,25)]
            if U<Uc:
                assert min(L)>-1e-8, (test,'monotone',U,Uc,min(L))
            else:
                xm=minimum_location(weights,rates,U)
                assert 0<xm<U
                assert max(hazard_derivative(weights,rates,xm*z/10,U) for z in range(1,10))<1e-8
                assert min(hazard_derivative(weights,rates,xm+(U-xm)*z/10,U) for z in range(1,10))>-1e-8
                assert abs(hazard_derivative(weights,rates,xm,U))<1e-7
            x=U*0.35
            h=1e-5*max(x,0.1)
            assert h<x and x+h<U
            fd=(hazard(weights,rates,x+h,U)-hazard(weights,rates,x-h,U))/(2*h)
            hd=hazard_derivative(weights,rates,x,U)
            assert near(fd,hd,rel=8e-7,abs_tol=1e-7), (test,fd,hd)
            a,b,c,d=moments(weights,rates,x)
            qprime=b*(1-b*d/(c*c))
            assert qprime < 0, (test,qprime)
            z=1e-5
            numerical=(Q(weights,rates,x+z)-Q(weights,rates,x-z))/(2*z)
            assert near(qprime,numerical,rel=5e-6,abs_tol=1e-8)
    # The finite-support large-cutoff selection law, with three rate classes.
    w=[0.2,0.5,0.3];r=[1.0,2.0,3.0]
    xstar=minimum_location(w,r,30.0)
    asympt=0.5*30+0.5*math.log(w[1]*(r[1]-r[0])**2/(w[0]*r[0]**2))
    assert abs(xstar-asympt)<1e-2, (xstar,asympt)
    print('PASS: 3000 nondegenerate mixtures, 6000 cutoff shapes,')
    print('      6000 finite-difference checks and two explicit asymptotic checks')
    print('U_critical = %.12f, minimum at U=3 = %.12f'%(critical_cutoff([.5,.5],[1,2]),xm if False else minimum_location([.5,.5],[1,2],3)))


if __name__=='__main__':
    main()
