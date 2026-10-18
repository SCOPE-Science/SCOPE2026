"""Independent algebraic and numerical checks for robust two-hub spectral design.
Run with Python >=3.9, sympy, numpy, scipy.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

M, R, Z = sp.symbols('M R Z', integer=True, positive=True)
P = Z**3-(2*M+2+2*R)*Z**2+(M**2+3*M+(2*M+5)*R)*Z-(M**2+M+(2*M+4)*R)+2
Q = sp.Matrix([[M-1+R,-R,0,-(M-1)],[-R,M+R,-1,-(M-1)],[0,-1,1,0],[-1,-1,0,2]])
assert sp.factor((Z*sp.eye(4)-Q).det()-Z*P)==0
assert sp.factor(P.subs(Z,1)-(1-R))==0
assert sp.factor(P.subs(Z,2)-(M-1)*(M+2*R-2))==0
assert sp.factor(P.subs(Z,0)+(M+2)*(M+2*R-1))==0
assert sp.factor(sp.diff(P,R)-(-2*Z**2+(2*M+5)*Z-(2*M+4)))==0
assert sp.factor(sp.diff(P,Z)-(3*Z**2-(4*M+4+4*R)*Z+(M**2+3*M+(2*M+5)*R)))==0
print('Symbolic quotient and coefficient identities: PASS')


def lap(m,a,b,failed=None,asymmetric=None):
    n=m+2
    edges=[(0,1,b)]
    for j in range(m):
        v=j+2
        edges += [(0,v,a),(1,v,a)]
    if asymmetric is not None:
        assert len(asymmetric)==2*m+1
        edges=[(u,v,float(w)) for (u,v,_),w in zip(edges,asymmetric)]
    L=np.zeros((n,n))
    for idx,(u,v,w) in enumerate(edges):
        if idx==failed:continue
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    return L

def gap(L):
    return float(np.linalg.eigvalsh(L)[1])

def robust(w,m):
    return min(gap(lap(m,0,0,failed=i,asymmetric=w)) for i in range(2*m+1))

def froot(m,r):
    def polynomial(z):
        return z**3-(2*m+2+2*r)*z**2+(m*m+3*m+(2*m+5)*r)*z-(m*m+m+(2*m+4)*r)+2
    return brentq(polynomial,0,1+2/(m+1),xtol=1e-13)

def deriv(m,r,z):
    p_r=-2*z*z+(2*m+5)*z-(2*m+4)
    p_z=3*z*z-(4*m+4+4*r)*z+(m*m+3*m+(2*m+5)*r)
    return -p_r/p_z

def price_critical(m):
    z=froot(m,0.0)
    return 2*m*deriv(m,0,z)/z

rng=np.random.default_rng(8675309)
checks=0
for m in range(2,17):
    for r in (0,.0125,.25,1,3,10,50):
        z=froot(m,r)
        e=gap(lap(m,1,r,failed=1))
        assert abs(e-z)<5e-9,(m,r,e,z)
        assert z<2 and z>0
        assert gap(lap(m,1,r,failed=0))>=z-1e-9
        assert abs(robust(np.array([r]+[1.]*(2*m)),m)-z)<5e-9
        checks+=3
print('Direct spectral and every-outage checks:',checks)

for m in range(2,12):
    tc=price_critical(m)
    for t in [tc*.08,tc*.4,tc*.95,tc,tc*1.05,tc*2,tc*5]:
        B=1+0.24*m
        def obj(r):return froot(m,r)*B/(2*m+t*r)
        rstar = 0 if t>=tc else brentq(lambda rr: (2*m+t*rr)*deriv(m,rr,froot(m,rr))-t*froot(m,rr),0,30000,xtol=1e-10)
        a=B/(2*m+t*rstar);b=a*rstar
        assert abs(robust([b]+[a]*(2*m),m)-obj(rstar))<2e-8
        rnum=minimize_scalar(lambda r: -obj(r),bounds=(0,max(5,3*rstar+3)),method='bounded',options={'xatol':1e-12}).x
        assert obj(rnum) <= obj(rstar)+1e-9
        # also random asymmetric alternatives with the same budget
        for k in range(12):
            v=rng.uniform(.0001,1,2*m+1)
            v*=B/(t*v[0]+sum(v[1:]))
            assert robust(v,m) <= obj(rstar)+2e-8,(m,t,k,robust(v,m),obj(rstar))
            checks+=1
        checks+=2
print('Optimality scalar and nonsymmetric samples checked:',checks)

# Exact m=2 threshold: 3+2 sqrt(2)
z2=2-sp.sqrt(2)
t2=sp.factor(4*((2*z2**2-9*z2+8)/(3*z2**2-12*z2+10))/z2)
assert sp.simplify(t2-(3+2*sp.sqrt(2)))==0
print('Exact price at m=2:', t2)

for m in [3,4,5,10,20,50,100,1000]:
    z=froot(m,0)
    tc=price_critical(m)
    assert tc>0
    print('m',m,'z',round(z,11),'critical price',round(tc,11),'m*critical',round(m*tc,8))
assert abs(1000*price_critical(1000)-2)<.01
print('ALL CHECKS PASS',checks)
