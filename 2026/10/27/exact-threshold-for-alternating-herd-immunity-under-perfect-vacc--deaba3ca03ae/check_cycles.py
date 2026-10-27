#!/usr/bin/env python3
"""Reproduce quantitative checks for the perfect-efficacy annual vaccination map.

Requires mpmath and sympy. Scientific definitions and assertions are independent
of any previously generated data files.
"""
import math
from scipy.optimize import brentq
import sympy as sp

Y=sp.symbols('Y', positive=True)
z_formula=Y/(1-sp.exp(-Y))-1
E=sp.exp(Y)
z1=E*(E-1-Y)/(E-1)**2
z2=E*((Y-2)*E+Y+2)/(E-1)**3
z3=-E*(Y*E**2+4*Y*E+Y-3*E**2+3)/(E-1)**4
for k, expected in [(1,z1),(2,z2),(3,z3)]:
    assert sp.simplify(sp.diff(z_formula,Y,k)-expected)==0
print('3 symbolic derivative identities: PASS')


def z_of_y(y):
    if y<1e-6:
        return y/2+y*y/12-y**4/720
    return y/(-math.expm1(-y))-1


def y_of_z(z):
    if z<=0:return 0.
    return brentq(lambda y:z_of_y(y)-z,z,z+1,xtol=1e-14)


def beta(z):
    if z==0:return 2/3
    return (2*z-y_of_z(z))/(z*z)


def epidemic_size(p,R):
    q=1-p
    if R*q<=1:return 0.
    return y_of_z(R*q-1)/R


def step(p,R,r):
    return (1-r)*p+epidemic_size(p,R)


def cost_boundary(R):
    if R<=2.5:return 0.
    return brentq(lambda z:beta(z)-1/(R-1),1e-5,R-1)/ (R-1)


def crossing(R,r):
    pc=1-1/R
    def h(p):
        return epidemic_size((1-r)*p,R)-r*(2-r)*p
    if h(pc)<-1e-11:return None
    hi=brentq(h,pc,1)
    return (1-r)*hi,hi

cases=0
for R in [1.1,1.4,2.,2.5,3.,5.,10.]:
    rc=cost_boundary(R)
    print('R',R,'critical r',round(rc,13))
    for r in [.01,.1,.25,.5,.75,.9]:
        z=r*(R-1)
        criterion=1/(R-1)-beta(z)
        ans=crossing(R,r)
        assert (ans is not None)==(criterion>0),(R,r,criterion)
        assert (r>rc)==(ans is not None),(R,r,rc)
        if ans:
            lo,hi=ans
            pc=1-1/R
            assert lo<pc<hi<1,(R,r,lo,hi)
            assert abs(step(lo,R,r)-hi)<3e-11,(R,r,lo,hi)
            assert abs(step(hi,R,r)-lo)<3e-11,(R,r,lo,hi)
            y=R*epidemic_size(lo,R)
            E=math.exp(-y)
            sensitivity=(-math.expm1(-y))**2/(1-(1+y)*E)
            assert 1<sensitivity<2
            multiplier=(1-r)*(1-r-sensitivity)
            assert -1<multiplier<0
        cases+=1
print(cases,'phase/cycle/spectral checks: PASS')

for j in range(1,200):
    z=j/20
    y=y_of_z(z)
    assert z<y<z+1
    assert 0<beta(z)<2/3
    assert beta(z)>beta(z+0.01)
print('199 inverse-branch and strict-monotonicity comparisons: PASS')

for R,r,present in [(3,.25,False),(3,.5,True),(5,.5,False),(5,.75,True),(2,.1,True)]:
    ans=crossing(R,r)
    assert (ans is not None)==present
    if ans:
        print('example R,r',R,r,'low,high',tuple(round(t,12) for t in ans))
print('ALL CHECKS PASSED')
