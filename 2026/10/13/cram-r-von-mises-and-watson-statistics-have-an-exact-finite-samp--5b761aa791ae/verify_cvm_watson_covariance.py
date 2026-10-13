#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

def add(a,b):
    c=dict(a)
    for e,v in b.items():
        c[e]=c.get(e,Fraction(0))+v
        if c[e]==0:
            del c[e]
    return c

def scale(a,s):
    return {e:v*s for e,v in a.items() if v*s}

def mul(a,b):
    c={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            c[g]=c.get(g,Fraction(0))+v*w
    return {e:v for e,v in c.items() if v}

def const(n,c):
    return {(0,)*n:Fraction(c)}

def var(n,i,power=1,coef=Fraction(1)):
    e=[0]*n
    e[i]=power
    return {tuple(e):coef}

def monomial_expectation(e):
    # Joint density of uniform order statistics is n! on the ordered simplex.
    den=1
    prefix=0
    for k,a in enumerate(e,start=1):
        prefix += a
        den *= prefix+k
    return Fraction(factorial(len(e)),den)

def expectation(p):
    return sum((v*monomial_expectation(e) for e,v in p.items()),Fraction(0))

def build(n):
    W=const(n,Fraction(1,12*n))
    for i in range(n):
        a=Fraction(2*(i+1)-1,2*n)
        W=add(W,var(n,i,2))
        W=add(W,var(n,i,1,-2*a))
        W=add(W,const(n,a*a))
    centered_sum=const(n,-Fraction(n,2))
    for i in range(n):
        centered_sum=add(centered_sum,var(n,i))
    correction=scale(mul(centered_sum,centered_sum),Fraction(1,n))
    U=add(W,scale(correction,-1))
    return W,U

def moments(n):
    W,U=build(n)
    ew=expectation(W)
    eu=expectation(U)
    vw=expectation(mul(W,W))-ew*ew
    vu=expectation(mul(U,U))-eu*eu
    cov=expectation(mul(W,U))-ew*eu
    return ew,eu,vw,vu,cov

def run():
    exact_moment_checks=0
    correlation_checks=0
    for n in range(1,9):
        ew,eu,vw,vu,cov=moments(n)
        assert ew==Fraction(1,6)
        assert eu==Fraction(1,12)
        assert vw==Fraction(4*n-3,180*n)
        assert vu==Fraction(n-1,360*n)
        assert cov==Fraction(n-1,180*n)
        exact_moment_checks += 5
        if n>=2:
            rho2=cov*cov/(vw*vu)
            assert rho2==Fraction(2*(n-1),4*n-3)
            correlation_checks += 1
    print(
        "VERIFY_OK "
        f"sample_sizes=8 "
        f"exact_moment_checks={exact_moment_checks} "
        f"exact_correlation_squared_checks={correlation_checks}"
    )

if __name__=="__main__":
    run()
