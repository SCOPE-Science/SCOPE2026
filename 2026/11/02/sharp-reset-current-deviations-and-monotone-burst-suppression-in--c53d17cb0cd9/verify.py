"""Finite checks of the analytic threshold-reset count theorem.

Requires Python 3, mpmath, scipy; no simulation is used as proof.
"""
from fractions import Fraction
import math
import mpmath as mp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import jv

mp.mp.dps = 55
checks = 0

def assert_close(a,b,tol=2e-8):
    global checks
    assert abs(float(a)-float(b)) <= tol * max(1.0,abs(float(a)),abs(float(b))), (a,b)
    checks+=1

def C(b, s):
    return mp.hyper([], [b], mp.mpf(b)*s)

def Cp(b, s):
    return mp.hyper([], [b+1], mp.mpf(b)*s)

def lam(b, theta):
    if theta==0: return mp.mpf('0')
    pole=mp.mpf(brentq(lambda x: jv(float(b)-1,x),1.5,2.5))**2 / (4*mp.mpf(b))
    lo=-pole + mp.mpf('1e-14')
    hi=mp.mpf('1')
    while mp.log(C(b,hi))<=theta:
        hi*=2
    for i in range(160):
        mid=(lo+hi)/2
        if mp.log(C(b,mid)) > theta:
            hi=mid
        else:
            lo=mid
    return (hi+lo)/2

def rate(b,j):
    assert j>1
    lo=mp.mpf('0');hi=mp.mpf('1')
    while C(b,hi)/Cp(b,hi)<=j:
        hi*=2
    for _ in range(160):
        x=(lo+hi)/2
        if C(b,x)/Cp(b,x)<j:
            lo=x
        else:hi=x
    x=(lo+hi)/2
    return j*mp.log(C(b,x))-x

alphas=[Fraction(0),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5),Fraction(20)]
bs=[(a+1)/(a+2) for a in alphas]
for n in range(2,31):
    coeff=[]
    for b in bs:
        q=Fraction(1)
        for k in range(1,n+1):
            q *= b/Fraction(k)/(b+k-1)
        coeff.append(q)
    for x,y in zip(coeff,coeff[1:]):
        assert x<y, (n,x,y)
        checks+=1

for a,b in zip(alphas,bs):
    bf=mp.mpf(b.numerator)/b.denominator
    assert_close(bf, (mp.mpf(a.numerator)/a.denominator+1)/(mp.mpf(a.numerator)/a.denominator+2))
    assert_close(mp.diff(lambda s: mp.log(C(bf,s)),0),1)
    assert_close(-mp.diff(lambda s: mp.log(C(bf,s)),0,2),1/(bf+1))
    for theta in [-3,-1,1,3]:
        x=lam(bf,mp.mpf(theta))
        assert_close(mp.log(C(bf,x)),theta)
    for s in [0.15,1,3]:
        assert_close(C(bf,s)*1/C(bf,s),1)

for a in [0,0.5,1.5,4.0]:
    b=(a+1)/(a+2)
    for q in [0.2,1.5,3.0]:
        def rhs(x,y): return [y[1],q*(x**a)*y[0]]
        z=solve_ivp(rhs,[0,1],[1,0],rtol=1e-11,atol=1e-12)
        v=z.y[0,-1]
        exact=mp.hyper([],[b],mp.mpf(q)/(a+2)**2)
        assert_close(v,exact)

for s in [0.1,1,3]:
    assert_close(1/C(mp.mpf('0.5'),mp.mpf(s)),1/mp.cosh(mp.sqrt(2*s)))
    assert_close(1/C(mp.mpf('1.0'),mp.mpf(s)),1/mp.besseli(0,2*mp.sqrt(s)))
    previous=None
    for b in [mp.mpf('0.5'),mp.mpf('0.6'),mp.mpf('0.75'),mp.mpf('0.9'),mp.mpf('0.99'),mp.mpf('1.0')]:
        v=1/C(b,mp.mpf(s))
        if previous is not None:
            assert v<previous
            checks+=1
        previous=v

for j in [1.1,1.5,2,5,20]:
    prior=None
    for b in [mp.mpf('0.5'),mp.mpf('0.6'),mp.mpf('0.75'),mp.mpf('0.9'),mp.mpf('0.99')]:
        val=rate(b,mp.mpf(j))
        assert val>0
        checks+=1
        if prior is not None:
            assert val>prior,(j,b,prior,val)
            checks+=1
        prior=val
for b in [mp.mpf('0.5'),mp.mpf('0.75'),mp.mpf('0.99')]:
    assert_close(rate(b,mp.mpf('500'))/(500**2),b,tol=0.04)

print('PASS',checks,'finite exact-arithmetic, ODE, transform, tilt and rate consistency assertions')
print('Selected rate values:')
for b in [mp.mpf('.5'),mp.mpf('.75'),mp.mpf('.99')]:
    print('b=',str(b),'I(1.5)=',mp.nstr(rate(b,mp.mpf('1.5')),12),
          'Fano=',mp.nstr(1/(b+1),12),
          'I(0)=',mp.nstr(mp.mpf(brentq(lambda x: jv(float(b)-1,x),1.5,2.5))**2/(4*b),12))
