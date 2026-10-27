"""Reproduce the algebraic and numerical checks for an ideal two-branch hydrograph.
Run with: python3 verify.py. Requires only the Python standard library.
"""
from fractions import Fraction
from math import exp, isclose, log
from random import Random


def threshold_polynomial(k):
    return 5*k**4 - 24*k**3 + 36*k*k - 20*k + 2


def stationary_polynomial(k, x):
    return k*(1-k)*x**3 + (2*k*k-2*k-1)*x*x + (4-2*k)*x - 2


def derivative(k, w, x):
    return w*k*k*exp(-k*x)*(1-k*x) + (1-w)*x*exp(-x)*(2-x)/2


def density(k, w, x):
    return w*k*k*x*exp(-k*x) + (1-w)*x*x*exp(-x)/2


def derivative_ratio(k, x):
    return exp((k-1)*x)*x*abs(2-x)/(2*k*k*abs(k*x-1))


def bisect(f, left, right, iterations=90):
    fl=f(left)
    assert fl*f(right)<0
    for _ in range(iterations):
        middle=(left+right)/2
        fm=f(middle)
        if fm==0: return middle
        if fl*fm>0: left,fl=middle,fm
        else: right=middle
    return (left+right)/2


def root_count_by_grid(k, w, grid=3500):
    lo=min(1/k,2)
    hi=max(1/k,2)
    if lo==hi: return 1
    # Deliberately count zeros of the original hydrograph derivative,
    # rather than zeros of the stationary-point polynomial.
    previous=derivative(k,w,lo)
    roots=0
    for j in range(1,grid+1):
        x=lo+(hi-lo)*j/grid
        value=derivative(k,w,x)
        if abs(value)<1e-13: continue
        if previous*value<0: roots+=1
        previous=value
    return roots


def cubic_discriminant(k):
    a=k*(1-k)
    b=2*k*k-2*k-1
    c=4-2*k
    d=Fraction(-2,1)
    return b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d


def critical_points(k):
    lo=min(1/k,2)
    hi=max(1/k,2)
    previous=stationary_polynomial(k,lo)
    out=[]
    for j in range(1,10001):
        x=lo+(hi-lo)*j/10000
        y=stationary_polynomial(k,x)
        if previous*y<0:
            l=lo+(hi-lo)*(j-1)/10000
            out.append(bisect(lambda s:stationary_polynomial(k,s),l,x))
        previous=y
    return out


def checks():
    # Degree-six polynomial identity: equality at seven distinct rational
    # arguments proves equality of two polynomials of degree at most six.
    for j in range(1,13):
        k=Fraction(j,7)
        assert cubic_discriminant(k)==4*(2*k-1)**2*threshold_polynomial(k)

    kminus=bisect(threshold_polynomial,0.12,0.13)
    kplus=bisect(threshold_polynomial,2.5,2.7)
    assert abs(kminus-0.126398265529446)<1e-12
    assert abs(kplus-2.59924909113955)<1e-12
    for k in [0.0001,0.01,0.1]: assert threshold_polynomial(k)>0
    for k in [0.15,0.5,1,2.5]: assert threshold_polynomial(k)<0
    for k in [3,10,100]: assert threshold_polynomial(k)>0

    rng=Random(20261024)
    # Exact algebraic numerator N(x) of the logarithmic derivative of Q.
    for _ in range(1000):
        k=exp(rng.uniform(log(0.015),log(90)))
        if abs(k-0.5)<0.025: continue
        low,high=sorted((1/k,2))
        x=low+(high-low)*rng.uniform(0.02,0.98)
        L=(k-1)-1/(x*(k*x-1))-1/(2-x)
        D=x*(k*x-1)*(2-x)
        value=stationary_polynomial(k,x)
        assert isclose(D*L,value,rel_tol=3e-11,abs_tol=5e-11)

    # Both sides of the universal-unimodality interval, and in its interior.
    for k in [0.05,0.10,3.0,4.0,10.0]:
        cps=critical_points(k)
        assert len(cps)==2,(k,cps)
        q1,q2=(derivative_ratio(k,x) for x in cps)
        lower,upper=sorted((q1,q2))
        odds=(lower*upper)**0.5
        w=odds/(1+odds)
        assert root_count_by_grid(k,w)==3,(k,w,cps)
        # Mix proportions on either side of both fold points are unimodal.
        for oo in [lower/3,upper*3]:
            ww=oo/(1+oo)
            assert root_count_by_grid(k,ww)==1,(k,ww)
    for k in [0.14,0.2,0.45,0.5,0.7,1.0,1.7,2.3,2.55]:
        for w in [0.01,0.1,0.3,0.5,0.8,0.97]:
            assert root_count_by_grid(k,w)==1,(k,w)

    # An exact transcendental mixing weight forces the central trough at x=1.
    k=3
    w=exp(2)/(36+exp(2))
    assert abs(derivative(k,w,1))<1e-14
    assert derivative_ratio(k,Fraction(2,3))<w/(1-w)
    assert derivative_ratio(k,Fraction(3,2))>w/(1-w)
    assert root_count_by_grid(k,w)==3
    assert density(k,w,1)<density(k,w,0.55)
    assert density(k,w,1)<density(k,w,1.7)
    print('PASS: exact degree-six discriminant identity, critical roots,')
    print('1000 logarithmic-derivative checks, both bimodal regimes,')
    print('unimodal regimes, and the explicit two-peak witness.')
    print('rate ratios:',format(kminus,'.15f'),format(kplus,'.15f'))


if __name__=='__main__':
    checks()
