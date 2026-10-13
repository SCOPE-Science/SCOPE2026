#!/usr/bin/env python3
"""Standalone exact algebra and reproducible finite-sample checks for the Watson/AD cross moment."""
from fractions import Fraction as F
from math import pi, log, sqrt
from random import Random


def add(*polys):
    n=max(map(len,polys)); return tuple(sum((p[k] if k<len(p) else 0 for p in polys),F(0)) for k in range(n))

def neg(p): return tuple(-z for z in p)

def scale(p,a): return tuple(a*z for z in p)

def mul(a,b):
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return tuple(r)

def power(a,k):
    r=(F(1),)
    for _ in range(k):r=mul(r,a)
    return r

def integrate_0_1(p):return sum((c/F(i+1) for i,c in enumerate(p)),F(0))

def integrate_affine_square(a,b,lower,upper):
    """Exactly integrate (a(s)*t+b(s))**2 dt from t=lower(s) to upper(s)."""
    diff=lambda k:add(power(upper,k),neg(power(lower,k)))
    return add(scale(mul(mul(a,a),diff(3)),F(1,3)),
               mul(mul(a,b),diff(2)),mul(mul(b,b),diff(1)))


def algebra_checks():
    one=(F(1),); s=(F(0),F(1)); zero=(F(0),)
    one_minus_s=add(one,neg(s)); two=F(2)
    kappa=scale(mul(s,one_minus_s),F(1,2))
    lower=integrate_affine_square(one_minus_s,neg(kappa),zero,s)
    upper=integrate_affine_square(neg(s),add(s,neg(kappa)),s,one)
    residual=add(lower,upper)
    goal=scale(mul(mul(s,s),mul(one_minus_s,one_minus_s)),F(1,12))
    assert add(residual,neg(goal))==(F(0),)*len(residual), (residual,goal)
    # With 1/[s(1-s)] Anderson-Darling weight, the exact cross kernel is 1/72.
    assert integrate_0_1(scale(mul(s,one_minus_s),F(1,12)))==F(1,72)
    # For independent uniform pair, |U-V| has density 2(1-z).
    z=s
    h=add((F(1,12),),scale(z,-F(1,2)),scale(mul(z,z),F(1,2)))
    eh2=integrate_0_1(mul(mul(h,h),scale(one_minus_s,F(2))))
    assert eh2==F(1,720), eh2
    for n in range(1,201):
        cov=F(n-1,36*n)
        varu=F(n-1,360*n)
        assert (cov==0)==(n==1)
        assert varu>=0 and cov>=0
        if n>=2:
            vara=(2*(n-1)*(pi*pi/3-3)+(4-pi*pi/3))/n
            corr=float(cov)/sqrt(float(varu)*vara)
            if n>2:
                pm=n-1
                previous=(pm-1)/(36*pm)/sqrt((pm-1)/(360*pm)*((2*(pm-1)*(pi*pi/3-3)+(4-pi*pi/3))/pm))
                assert corr>previous
            assert 0<corr<1
    return residual,eh2


def gof_from_uniform(xs):
    n=len(xs);u=sorted(xs)
    w=1/(12*n)
    w+=sum((x-(2*i-1)/(2*n))**2 for i,x in enumerate(u,1))
    watson=w-n*(sum(u)/n-0.5)**2
    ad=-n-sum((2*i-1)*(log(u[i-1])+log(1-u[n-i])) for i in range(1,n+1))/n
    return watson,ad


def simulation_checks():
    rng=Random(450920)
    output=[]
    for n in (1,2,4,9,20):
        reps=60000 if n<=9 else 40000
        u=[];a=[]
        for _ in range(reps):
            vals=[rng.random() for _ in range(n)]
            w,ad=gof_from_uniform(vals)
            u.append(w);a.append(ad)
        mu=sum(u)/reps;ma=sum(a)/reps
        cov=sum((x-mu)*(y-ma) for x,y in zip(u,a))/reps
        target=(n-1)/(36*n)
        tol=0.004 if n==20 else 0.003
        assert abs(cov-target)<tol,(n,cov,target)
        if n==1:assert max(u)-min(u)<1e-12
        output.append((n,reps,round(cov,7),round(target,7)))
    return output


if __name__=='__main__':
    polynomial, eh2=algebra_checks()
    print('EXACT_ALGEBRA_OK centered_bridge_polynomial=',tuple(map(str,polynomial)),
          'independent_watson_kernel_second_moment=',eh2)
    print('SIMULATION_OK',simulation_checks())
    print('VERIFY_OK')
