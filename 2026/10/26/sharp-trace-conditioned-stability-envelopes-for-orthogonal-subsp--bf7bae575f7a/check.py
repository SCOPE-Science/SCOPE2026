#!/usr/bin/env python3
"""Exact-moment and numerical checks for orthogonal-subspace quadratic stability."""
from fractions import Fraction
from itertools import product
from math import isclose
import random


def coeff(d,k):
    assert 2 <= d and 1 <= k <= d
    a=Fraction(d*((k+1)*d-2), k*(d-1)*(d+2))
    b=Fraction(d*(d-k), k*(d-1)*(d+2))
    return a,b


def root(vals,k):
    d=len(vals); a,b=map(float,coeff(d,k))
    if k==d:return 2./max(vals)
    lo,hi=0.,2/(a*max(vals))
    for _ in range(110):
        z=(lo+hi)/2
        f=z*b*sum(l/(2-a*z*l) for l in vals)
        if f>1:hi=z
        else:lo=z
    return (lo+hi)/2


def matrix_B(vals,k,eta):
    d=len(vals);a,b=map(float,coeff(d,k))
    return [[(1-2*eta*li+eta**2*a*li*li if i==j else 0.)+eta*eta*b*vals[j]*vals[j] for j in range(d)] for i,li in enumerate(vals)]


def perron(B,n=1800):
    d=len(B);u=[1/d]*d;old=0
    for it in range(n):
        v=[sum(B[i][j]*u[j] for j in range(d)) for i in range(d)]
        z=sum(v)
        if z==0:return 0.
        u=[t/z for t in v]
        if abs(z-old)<1.e-14:break
        old=z
    return z


def run():
    checks=0
    for d in range(2,10):
        for k in range(1,d+1):
            a,b=coeff(d,k)
            assert a>=1 and b>=0 and a+ d*b==Fraction(d,k)
            assert a+b==Fraction(d*(k+2),k*(d+2))
            checks+=3
    for d in range(2,10):
        for k in range(1,d):
            # Equal-eigenvalue data have sharp classical spherical sufficient step.
            assert isclose(root([2]*d,k),float(Fraction(k,d)),rel_tol=3.e-12)
            checks+=1
    vbest=[1,2.5,2.5,4]
    vworst=[1,1,4,4]
    best=root(vbest,2);worst=root(vworst,2)
    assert abs(best-0.337597786803083)<1e-12
    assert abs(worst-0.3131948736438942)<1e-12
    assert worst<best and worst>0.25
    checks+=3
    rr=random.Random(652026)
    for d in (3,4,5,7):
        for k in range(1,d):
            for trial in range(48):
                x=[rr.uniform(.35,4.7) for _ in range(d)]
                edge=root(x,k)
                for mult,good in ((.75,True),(1.25,False)):
                    B=matrix_B(x,k,mult*edge)
                    rad=perron(B)
                    assert rad < 1-1e-7 if good else rad>1+1e-7,(x,k,mult,rad)
                    checks+=1
    # Check convex majorization with fixed endpoints, fixed trace.
    for k in range(1,5):
        for j in range(101):
            t=1.0+1.5*j/100
            balanced=[1.,2.5,2.5,4.]
            spread=[1.,t,5.-t,4.]
            assert root(balanced,k)>=root(spread,k)-1e-10
            checks+=1
    # Exact subspace moment formula from Beta diagonal + idempotence.
    for d in range(2,14):
        for k in range(1,d):
            diag2=Fraction(k*(k+2),d*(d+2))
            off2=(Fraction(k,d)-diag2)/(d-1)
            a,b=coeff(d,k)
            scale=Fraction(d*d,k*k)
            assert off2*scale==b and (diag2-off2)*scale==a
            checks+=2
    print('CHECK_OK',checks,'best',repr(best),'worst',repr(worst))

if __name__=='__main__':run()
