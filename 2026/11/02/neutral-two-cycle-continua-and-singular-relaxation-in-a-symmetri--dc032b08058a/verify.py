"""Standalone numerical and symbolic checks for the neutral two-cycle theorem.

The proof is analytical; these checks test its formulas and finite examples only.
Run: python verify.py
"""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

z,p=sp.symbols('z p', real=True)
J=2**(-p)*((1+z)**p-(1-z)**p)
assert sp.simplify(J.subs(p,1)-z)==0
assert sp.simplify(J.subs(p,2)-z)==0
H1=sp.diff(J,p).subs(p,1)
H2=sp.diff(J,p).subs(p,2)
assert sp.simplify(H1-( ((1+z)*sp.log((1+z)/2)-(1-z)*sp.log((1-z)/2))/2))==0
assert sp.simplify(H2-( ((1+z)**2*sp.log((1+z)/2)-(1-z)**2*sp.log((1-z)/2))/4))==0
assert sp.simplify(sp.diff(H1,z,2)+z/(1-z*z))==0
assert sp.simplify(sp.diff(H2,z,2)-(sp.log(1+z)-sp.log(1-z))/2)==0

checks=6

def j(power,x):
    return ((1+x)**power-(1-x)**power)/2**power

def invj(power,x):
    if x<=0: return 0.0
    if x>=1: return 1.0
    return brentq(lambda y:j(power,y)-x,0,1,xtol=1e-14)

def h(power0,x):
    if power0==1:
        return ((1+x)*math.log((1+x)/2)-(1-x)*math.log((1-x)/2))/2
    return ((1+x)**2*math.log((1+x)/2)-(1-x)**2*math.log((1-x)/2))/4

for power in [0.3,0.8,1.25,1.8,2.2,3.0,5.0]:
    for x in [.1,.25,.5,.8,.95]:
        value=j(power,x)-x
        expected=1 if 1<power<2 else -1
        assert value*expected>1e-12
        y=invj(power,x)
        assert (y-x)*expected<0
        assert abs(j(power,y)-x)<1e-11
        checks+=3
for p0 in [1,2]:
    for x in [.15,.4,.7,.85]:
        hh=h(p0,x)
        assert hh>0 if p0==1 else hh<0
        for delta in [1e-3,-1e-3,3e-4,-3e-4]:
            exact=invj(p0+delta,x)
            estimate=x-delta*hh
            assert abs(exact-estimate)<2*delta**2
            checks+=2
for p0 in [1,2]:
    c=quad(lambda y:1/abs(h(p0,y)),.25,.75,epsabs=1e-11)[0]
    print('p0',p0,'slow-time passage .25 to .75 coefficient',format(c,'.12f'))
    for delta in [0.0002,-0.0002]:
        ascending=(delta<0) if p0==1 else (delta>0)
        y=.25 if ascending else .75
        threshold=.75 if ascending else .25
        n=0
        while (y<threshold if ascending else y>threshold) and n<1000000:
            y=invj(p0+delta,y);n+=1
        assert n<1000000
        print(' p',p0+delta,'n',n,'n*abs(delta)',n*abs(delta),'relative err',abs(n*abs(delta)-c)/c)
        assert abs(n*abs(delta)-c)/c<0.003
        checks+=1
print('PASS',checks,'finite assertions and identities')
