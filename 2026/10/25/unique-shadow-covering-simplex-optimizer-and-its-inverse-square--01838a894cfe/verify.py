#!/usr/bin/env python3
"""Self-contained algebraic reproduction and independent optional geometry checks."""
from fractions import Fraction as F
from math import comb, isclose, sqrt

def polynom(n):
    """Exact coefficients of R_n(t), constant through leading."""
    ans=[F(0) for _ in range(n+1)]
    for j in range(n+1):
        pref=F(comb(n,j)**2,(n-1)**j)
        for r in range(j+1):
            ans[n-j+r]+=pref*(-1 if r%2 else 1)*comb(j,r)
    return ans

def value(n,t):
    """Directly evaluate the independent binomial expression."""
    return sum(comb(n,j)**2*t**(n-j)*((1-t)/(n-1))**j for j in range(n+1))

def efficient_value(n,t):
    """Stable O(n) binomial recurrence near t=1."""
    if t==0: return 1/(n-1)**n
    a=t**n
    out=a
    q=(1-t)/((n-1)*t)
    for j in range(1,n+1):
        a*=((n-j+1)/j)**2*q
        out+=a
    return out

def slope(n,t):
    a=polynom(n)
    return sum(float(j*a[j])*t**(j-1) for j in range(1,n+1))

def bisection(n):
    low,high=0.,1.
    for _ in range(90):
        mid=(low+high)/2
        if slope(n,mid)>0:low=mid
        else: high=mid
    return (low+high)/2

def legendre_poly(n):
    """Coefficients of P_n(x) in increasing order, exact recurrence."""
    p0=[F(1)];p1=[F(0),F(1)]
    if n==0:return p0
    if n==1:return p1
    for k in range(1,n):
        a=[F(0)]*(k+2)
        for j,v in enumerate(p1):a[j+1]+=(2*k+1)*v
        for j,v in enumerate(p0):a[j]-=k*v
        a=[v/F(k+1) for v in a]
        p0,p1=p1,a
    return p1

def legendre_identity_by_samples(n):
    p=legendre_poly(n)
    for z in (F(-3,8),F(-1,10),F(0),F(1,7),F(2,3)):
        x=(1+z)/(1-z)
        pn=sum(v*x**j for j,v in enumerate(p))
        lhs=sum(F(comb(n,j)**2)*z**j for j in range(n+1))
        assert lhs==(1-z)**n*pn

for n in range(2,14):
    a=polynom(n)
    assert sum(a)==1
    assert a[0]==F(1,(n-1)**n)
    assert sum(F(j)*a[j] for j in range(1,n+1))==F(-n,n-1)
    assert a[1]==F(n*n*(n-1)-n,(n-1)**n)
    legendre_identity_by_samples(n)
print('EXACT_ORTHANT_POLYNOMIAL_COEFFICIENTS_AND_LEGENDRE_IDENTITY_OK')

assert polynom(4)==[F(1,81),F(44,81),F(186,81),F(-76,81),F(-74,81)]
for bound,expect in [(F(870215,10**6),1),(F(870216,10**6),-1)]:
    g=74*bound**3+57*bound**2-93*bound-11
    assert (g<0 if expect==1 else g>0)
r4=bisection(4)
assert abs(r4-.8702150625262818)<2e-14
assert abs(value(4,r4)-1.0817625306405636)<1e-13
assert abs(bisection(3)-(1+2*sqrt(14))/11)<1e-14
print('EXACT_FOUR_DIMENSIONAL_CUBIC_ISOLATION_AND_2011_BENCHMARK_OK',r4,value(4,r4))

for n in (25,50,100,200,500,1000):
    # For large n numerical differentiation of polynomials is unstable.
    z=2.0;t=1-z/n**2
    gain=n**2*(efficient_value(n,t)-1)
    assert abs(gain-1)<0.24
    print('ASYMPTOTIC_RESCALED_CHECK',n,round(gain,9))
print('SYMBOLIC_AND_LIMIT_CHECKS_OK')

try:
    import numpy as np
    from scipy.spatial import ConvexHull
except ImportError:
    print('INDEPENDENT_HULL_OPTIONAL_DEPENDENCIES_NOT_INSTALLED')
else:
    for n in (2,3,4,5):
        vertices=np.zeros((n+1,n))
        vertices[1:]=np.eye(n)
        original=ConvexHull(vertices).volume
        for t in (.13,.37,.71,.87):
            mix=np.array([t*a-(1-t)*b/(n-1) for a in vertices for b in vertices])
            measured=ConvexHull(mix).volume/original
            assert abs(measured-value(n,t))<1e-10,(n,t,measured,value(n,t))
    print('INDEPENDENT_MINKOWSKI_SUM_CONVEX_HULLS_OK',16)
print('ALL_SHADOW_COVERING_FAMILY_REPRODUCTION_CHECKS_OK')
