#!/usr/bin/env python3
"""Checks for the migration-response formula of the seasonal three-patch model.
The theorem is analytic; tests are finite checks, not proof of universal assertions.
"""
import math
from fractions import Fraction


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def polynomial(lam, s, p):
    return lam**3+(p-1)*lam**2+(p-1)*s*lam+(1-2*p)*s


def root(s, p):
    lo, hi = s**(1/3), s**0.5
    if abs(p-1)<1e-15:
        return lo
    for _ in range(130):
        mid=(lo+hi)/2
        if polynomial(mid,s,p)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def exponent(a,b,T,m):
    h=T/3
    s=math.exp((a-b)*h)
    p=(1+math.exp(-2*m*h))/2
    return b+math.log(root(s,p))/h


def formula_derivative(a,b,T,m):
    h=T/3
    s=math.exp((a-b)*h)
    p=(1+math.exp(-2*m*h))/2
    lam=root(s,p)
    f_lam=3*lam**2+2*(p-1)*lam+(p-1)*s
    f_p=lam**2+s*lam-2*s
    return math.exp(-2*m*h)*f_p/(lam*f_lam)


def run():
    checks=0
    for s in [Fraction(8,1),Fraction(27,1),Fraction(125,1),Fraction(64,27)]:
        for p in [Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(1,1)]:
            for lam in [Fraction(1,2),Fraction(2,1),Fraction(5,1)]:
                a=[[lam,-p,-(1-p)],[0,lam-(1-p),-p],[-s,0,lam]]
                assert det3(a)==polynomial(lam,s,p)
                checks+=1
    for delta in [0.2,0.7,1.5,3.0,5.0]:
        for T in [0.15,0.8,2.0,6.0]:
            a,b=delta/2,-delta/2
            previous=exponent(a,b,T,0)
            assert abs(previous-(a+2*b)/3)<1e-10
            checks+=1
            for m in [0.01,0.04,0.1,0.3,0.7,1.5,3]:
                val=exponent(a,b,T,m)
                assert val>previous+1e-13, (delta,T,m,val,previous)
                assert val<(a+b)/2+1e-10
                diff=formula_derivative(a,b,T,m)
                assert diff>0
                step=min(1e-4, m/5)
                numeric=(exponent(a,b,T,m+step)-exponent(a,b,T,m-step))/(2*step)
                assert abs(diff-numeric)<max(2e-5,abs(diff)*0.005),(delta,T,m,diff,numeric)
                checks+=4
                previous=val
            slope=(math.exp(delta*T/9)-1)**2/(3*math.exp(delta*T/9))
            assert abs(formula_derivative(a,b,T,0)-slope)<1e-10
            checks+=1
    print(f'PASS: {checks} finite exact-rational and numerical assertions')

if __name__=='__main__':
    run()
