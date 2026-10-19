"""Exact and numerical checks for phase-uniform Ikeda fixed-point threshold.
Requires Python 3.10+, SymPy, NumPy, SciPy.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

u,t,v=sp.symbols('u t v',positive=True,real=True)
D=4*u**2-(1+u**2-t)**2
L=(1+t)**2/sp.sqrt(D)
critical=sp.factor(2*D-(1+t)*(1+u**2-t))
assert sp.simplify(critical.subs(t,1+u**2-v) - (-v**2-(2+u**2)*v+8*u**2)) == 0
assert sp.simplify(sp.diff(sp.log(L),t) - (2/(1+t)-(1+u**2-t)/D)) == 0
print('symbolic optimization derivative and quadratic: PASS')

def threshold(u):
    v0=(math.sqrt((2+u*u)**2+32*u*u)-(2+u*u))/2
    t0=1+u*u-v0
    eta=(1+t0)**2/math.sqrt(4*u*u-v0*v0)
    return eta,t0,v0

def f(r,u,eta,k):
    phase=k-eta/(1+r*r)
    return r*r*(1+u*u-2*u*math.cos(phase))-1

def roots(u,eta,k):
    r0,r1=1/(1+u),1/(1-u)
    grid=np.linspace(r0,r1,20002)
    vals=[f(r,u,eta,k) for r in grid]
    rs=[]
    for j in range(len(grid)-1):
        if vals[j]*vals[j+1]<0:
            r=brentq(lambda s:f(s,u,eta,k),grid[j],grid[j+1],xtol=1e-13)
            if not rs or abs(r-rs[-1])>1e-8:rs.append(r)
    return rs

for uval in (.2,.5,.9):
    ec,t0,v0=threshold(uval)
    assert (1-uval)**2<t0<(1+uval)**2
    rt=1/math.sqrt(t0)
    cos_theta=v0/(2*uval)
    assert abs(cos_theta)<1
    theta=-math.acos(cos_theta)
    eta=ec*1.15
    k=theta+eta/(1+rt*rt)
    rf=f(rt,uval,eta,k)
    ph=k-eta/(1+rt*rt)
    fp=2/rt+4*uval*eta*rt**3*math.sin(ph)/(1+rt*rt)**2
    assert abs(rf)<1e-10 and fp<0
    r3=roots(uval,eta,k)
    assert len(r3)>=3,(uval,ec,len(r3),r3)
    low=ec*.8
    for phase in np.linspace(-math.pi,math.pi,27):
        n=len(roots(uval,low,phase))
        assert n==1,(uval,phase,n)
    print('u',uval,'eta*',format(ec,'.12f'),'below unique (27 phases); above >=3 fixed:',r3)
print('ALL CHECKS PASSED')
