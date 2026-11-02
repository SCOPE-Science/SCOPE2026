#!/usr/bin/env python3
"""Independent numerical and rational checks of the stated Hill-toggle fold formulas.

The infinite-parameter theorem relies on the proof, not numerical sampling.
"""
import math
from fractions import Fraction as Q

checks = 0

def near(a,b,rel=1.e-9,abs_=1.e-11):
    global checks
    assert math.isclose(a,b,rel_tol=rel,abs_tol=abs_), (a,b)
    checks += 1

def critical(p,q):
    r=p*q
    if r<=1:
        return None
    x=((q+1)/(r-1))**(1/q)
    y=((p+1)/(r-1))**(1/p)
    a=p*x**(q+1)
    b=q*y**(p+1)
    curvature=p*(r-1)*x**(2*q-1)
    k=q/(p*x*x*y**(p-1))
    c=(4/3)*k*math.sqrt(2/curvature)
    return x,y,a,b,curvature,k,c

def f(x,p,q):
    r=p*q
    return r*x**(q+1)/((r-1)*x**q-1)

def B(x,a,p,q):
    y=(a/x-1)**(1/p)
    return y*(1+x**q)

def derivative_sign_quantity(x,a,p,q):
    return a*((p*q-1)*x**q-1)-p*q*x**(q+1)

def folds(p,q,epsilon):
    x,y,a,b,d,k,c=critical(p,q)
    target=a+epsilon
    x0=(1/(p*q-1))**(1/q)
    lo=x0*(1+1.e-10)
    hi=x
    assert f(lo,p,q)>target and f(hi,p,q)<target
    for i in range(115):
        mid=(lo+hi)/2
        if f(mid,p,q)>target: lo=mid
        else: hi=mid
    left=(lo+hi)/2
    lo=x
    hi=max(2*x,2*target)
    for _ in range(50):
        if f(hi,p,q)>target:break
        hi*=2
    assert f(lo,p,q)<target and f(hi,p,q)>target
    for i in range(115):
        mid=(lo+hi)/2
        if f(mid,p,q)<target:lo=mid
        else:hi=mid
    right=(lo+hi)/2
    return left,right,B(left,target,p,q),B(right,target,p,q)

# Exact Jacobian/directional slope equality at rational equilibrium points.
for p,q in [(2,2),(2,3),(3,2),(3,3),(4,1),(1,4)]:
    for ni in range(1,7):
        x=Q(ni,3); y=Q(ni+1,4)
        a=x*(1+y**p)
        b=y*(1+x**q)
        det=1-Q(p*q)*x**q*y**p/((1+x**q)*(1+y**p))
        # dB/dx computed through implicit first nullcline.
        yd=-(1+y**p)/(Q(p)*x*y**(p-1))
        Bd=yd*(1+x**q)+q*x**(q-1)*y
        determinant_from_slope=-Q(p)*x*y**(p-1)*Bd/((1+y**p)*(1+x**q))
        assert det == determinant_from_slope
        checks+=1

# Exact symbolic cusp at p=q=2: x_c=y_c=1, alpha_c=beta_c=2, coefficient=4/(3sqrt(3)).
x,y,a,b,d,k,c=critical(2,2)
for lhs,rhs in [(x,1),(y,1),(a,2),(b,2),(d,6),(k,1),(c,4/(3*math.sqrt(3)))]:
    near(lhs,rhs,rel=1.e-13)

# General fold turning points and on-curve tangency, including noninteger Hill powers.
for p,q in [(2.,2.),(2.,3.),(3.,2.),(4.,1.),(1.,4.),(1.7,1.2),(.8,1.6),(.4,3.4),(.7,2.0),(1.1,1.1)]:
    x,y,a,b,d,k,c=critical(p,q)
    near(a,x*(1+y**p),rel=1.e-11)
    near(b,y*(1+x**q),rel=1.e-11)
    near(derivative_sign_quantity(x,a,p,q),0,abs_=1.e-9)
    for eps in [1.e-2,1.e-3,1.e-4,1.e-5]:
        left,right,bmin,bmax=folds(p,q,eps)
        assert 0<left<x<right<a+eps and bmin<bmax
        checks += 1
        near(f(left,p,q),a+eps,rel=1.e-10)
        near(f(right,p,q),a+eps,rel=1.e-10)
        near(derivative_sign_quantity(left,a+eps,p,q),0,abs_=1.e-7)
        near(derivative_sign_quantity(right,a+eps,p,q),0,abs_=1.e-7)
        w=bmax-bmin
        scale=w/(eps**1.5)
        # leading asymptotic must converge to positive analytic prefactor
        assert 0<scale/c<2
        checks+=1
        if eps<=1.e-4:
            near(scale,c,rel=.06)
# Finite differences for derivative of fold curve, distinct from stationarity calculations.
for p,q in [(2.,2.),(2.,3.),(1.7,1.2),(.4,3.4)]:
    x,y,a,b,d,k,c=critical(p,q)
    hh=1.e-4*x
    numerical=(f(x+hh,p,q)-2*f(x,p,q)+f(x-hh,p,q))/(hh*hh)
    near(numerical,d,rel=3.e-7)

print('VERIFY_OK',checks,'exact/rational-and-numerical-assertions')
