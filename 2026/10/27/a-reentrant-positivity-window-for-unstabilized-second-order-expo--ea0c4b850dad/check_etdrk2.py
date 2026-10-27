"""Numerical cross-checks of the exact scalar ETDRK2 positivity-window theorem.
Run: python3 check_etdrk2.py. Computational tests supplement, not replace, the proof.
"""
import math
from scipy.optimize import brentq, minimize_scalar

def phi1(z):
    return -math.expm1(-z)/z if z else 1.

def phi2(z):
    return (z + math.expm1(-z))/(z*z) if z else .5

def exact(rho, x):
    q=math.exp(-x)
    s=-math.expm1(-x)
    return q+rho*rho*s-rho*(1+rho)*s*s/x

def stage(rho,x):
    q=math.exp(-x)
    v=q-rho*x*phi1(x)
    return q-rho*x*((phi1(x)-phi2(x))+phi2(x)*v)

count=0
for rho in (.001,.002,.005,.01,.02,.05,.1,.15,.2,.24):
    for x in (.001,.02,.1,.5,1,2,5,10,20,100):
        a,b=exact(rho,x),stage(rho,x)
        assert abs(a-b)<1.e-11,(rho,x,a,b)
        assert abs(a)<1,(rho,x,a)
        count+=2
for rho in (.001,.002,.005,.01,.02,.05,.1):
    L=math.log(1/rho)
    f=lambda x:exact(rho,x)
    assert f(2*L)<0 and f(.5*L)>0 and f(3/rho)>0
    left=brentq(f,.5*L,2*L,xtol=2e-13)
    right=brentq(f,2*L,3/rho,xtol=2e-13)
    m=minimize_scalar(f,bounds=(left,right),method='bounded',options={'xatol':1.e-11})
    assert left<m.x<right and m.fun<0
    assert f(left-1e-5)>0 and f(left+1e-5)<0
    assert f(right-1e-5)<0 and f(right+1e-5)>0
    count+=7
for rho in (1e-4,1e-5,1e-6):
    L=math.log(1/rho)
    f=lambda x:exact(rho,x)
    a=brentq(f,.5*L,2*L,xtol=1e-14)
    b=brentq(f,2*L,3/rho,xtol=1e-12)
    m=minimize_scalar(f,bounds=(a,b),method='bounded',options={'xatol':1.e-8})
    # The asymptotics are slowly convergent; these tests use deliberately loose bands.
    assert abs(a-(L+math.log(L)))<2.0
    assert abs(b-(1/rho+1))<1e-5
    assert abs(m.x-(L+2*math.log(L)))<2.0
    assert 0.4<-m.fun*L/rho<1.5
    count+=4
print('PASS',count,'deterministic checks')
