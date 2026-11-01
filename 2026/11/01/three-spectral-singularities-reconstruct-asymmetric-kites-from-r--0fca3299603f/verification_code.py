"""Reproducible checks of directional-width laws for Euclidean kites.

No finite check is intended to replace the analytic proof for all parameters.
"""
from math import pi, atan, acos, sqrt, cos, sin, isclose
import numpy as np
from scipy.integrate import quad


def data(p,q,r=1.0):
    assert 0<p<=q and r>0
    a=atan(1/q); b=atan(1/p); t=atan(q)
    R=sqrt(1+q*q); S=p+q
    m1=2*q/R; m2=S/sqrt(1+p*p)
    return a,b,t,R,S,m1,m2

def direct(theta,p,q,r=1.0):
    return r*(max(cos(theta),p*sin(theta))+max(cos(theta),q*sin(theta)))

def piecewise(theta,p,q,r=1.0):
    a,b,t,R,S,m1,m2=data(p,q,r)
    if theta<=a: return 2*r*cos(theta)
    if theta<=b: return r*(cos(theta)+q*sin(theta))
    return r*S*sin(theta)

def density(w,p,q,r=1.0):
    a,b,t,R,S,m1,m2=data(p,q,r)
    if w<=0: return 0.0
    v=w/r
    n1=int(m1 < v < 2)
    n3=int(m2 < v < S)
    n2=0
    if 0<v<R:
        h=acos(v/R)
        n2=int(a<t-h<b)+int(a<t+h<b)
    return 2/pi*(n1/sqrt((2*r)**2-w*w) if n1 else 0.0)+(2/pi)*(n2/sqrt((r*R)**2-w*w) if n2 else 0.0)+(2/pi)*(n3/sqrt((r*S)**2-w*w) if n3 else 0.0)

def check(p,q):
    a,b,t,R,S,m1,m2=data(p,q)
    for theta in np.linspace(0,pi/2,1001):
        assert abs(direct(theta,p,q)-piecewise(theta,p,q))<1e-12
    pts=sorted(set([0,m1,m2,S,R,2,max(2,R,S)]))
    # Integrate on each regular interval, using square-root integrable endpoints.
    total=0
    for lo,hi in zip(pts,pts[1:]):
        if hi>lo+1e-10:
            val,err=quad(lambda x:density(x,p,q),lo+1e-12,hi-1e-12,epsabs=5e-8,limit=500)
            total+=val
    assert abs(total-1)<1e-5,(p,q,total)
    return total

for p,q in ((.25,1.5),(.24,1.675),(.5,.9),(.8,1.5),(1.2,1.8)):
    mass=check(p,q)
    print('NORMALIZATION',p,q,f'{mass:.12f}')

p,q,r=.25,1.5,1.7
_,_,_,R,S,_,_=data(p,q)
z1,z2,z3=r*S,r*R,2*r
assert z1<z2<z3
for z,expect in ((z1,2/pi),(z2,4/pi),(z3,2/pi)):
    for eps in (1e-7,1e-9):
        w=z-eps
        measured=density(w,p,q,r)*sqrt(z*z-w*w)
        assert abs(measured-expect)<.01,(z,measured,expect)
    print('SINGULAR',z, 'coefficient',measured,'limit',expect)
recovered_r=z3/2
recovered_q=sqrt((z2/recovered_r)**2-1)
recovered_p=z1/recovered_r-recovered_q
assert isclose(recovered_r,r,abs_tol=1e-12)
assert isclose(recovered_p,p,abs_tol=1e-12)
assert isclose(recovered_q,q,abs_tol=1e-12)
print('INVERSION',recovered_r,recovered_p,recovered_q)
print('ALL_CHECKS_PASSED')
