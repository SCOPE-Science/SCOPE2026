"""Finite symbolic and numerical checks for a period-two theorem on a memristive Lozi map.

Requires Python 3, sympy, numpy. The proof of completeness and hyperbolicity
is in RESULT.md; finite numerical tests here do not establish either theorem.
"""
from fractions import Fraction
from math import asin, pi, sin, cos, sqrt
import sympy as sp
import numpy as np

checks=0

def ck(condition, message):
    global checks
    assert condition, message
    checks+=1

K,T,ETA,S,C,L=sp.symbols('K T ETA S C L', real=True)
Jp=sp.Matrix([[1,1,0],[1,0,ETA*K*T],[0,1,1]])
Jq=sp.Matrix([[-1,1,0],[1,ETA*K*S,-ETA*K*T*C],[0,1,1]])
P=sp.expand((L*sp.eye(3)-Jq*Jp).det())
P0=sp.expand(P.subs(K,0))
P1=sp.expand(sp.diff(P,K).subs({K:0,T:1}))
ck(sp.simplify(P0-(L-1)*(L**2-L+1))==0,'monodromy at zero coupling')
ck(sp.simplify(P1-ETA*((C-1)*L**2+S*L-C-S-1))==0,'first characteristic variation')
ck(sp.simplify(-P1.subs(L,1)/sp.diff(P0,L).subs(L,1)-2*ETA)==0,'real eigenvalue slope')
complex_root=(sp.Integer(1)+sp.I*sp.sqrt(3))/2
first_slope=sp.simplify(-P1.subs(L,complex_root)/sp.diff(P0,L).subs(L,complex_root))
radial=sp.simplify(sp.re(sp.conjugate(complex_root)*first_slope))
ck(sp.simplify(radial-ETA*(C+S-1)/2)==0,'complex pair radial slope')
ck(Fraction(1,1)-3*Fraction(3,10)>0,'parameter monotonicity margin')

def f(point,b,k):
    x,y,z=point
    return (1-abs(x)+y, b*x+k*y*sin(z),z+y)

def branch(z,b,k):
    lo=0.0;hi=b/(1-k)
    for _ in range(85):
        mid=(lo+hi)*.5
        if mid*(1+k*sin(z+mid))<b:lo=mid
        else:hi=mid
    return (lo+hi)/2

def mtx(x,y,z,b,k):
    return np.array([[-1. if x>0 else 1.,1.,0.],
                     [b,k*sin(z),k*y*cos(z)],
                     [0.,1.,1.]])

for kr in [Fraction(1,200),Fraction(1,20),Fraction(1,10),Fraction(1,5),Fraction(3,10)]:
    k=float(kr)
    for c in [-1,-.9,-.4,0,.4,.9,1]:
        b=1+c*k
        zmain=asin(c)
        phases=[zmain] if abs(c)==1 else [zmain,pi-zmain]
        for z in phases:
            t=branch(z,b,k)
            p=(-t,t,z)
            q=(1.,-t,z+t)
            p1=f(p,b,k);p2=f(q,b,k)
            for u,v in zip(p1,q):ck(abs(u-v)<3e-13, 'first recurrence')
            for u,v in zip(p2,p):ck(abs(u-v)<3e-13, 'second recurrence')
            ck(t>0,'positive branch')
            ck(b/(1+k)-1e-13<=t<=b/(1-k)+1e-13,'a priori amplitude bounds')
            ck((1-k)**2>k*b,'strict derivative lower bound')
            if abs(c)<1:
                ck(abs(sin(z)-c)<2e-14,'phase condition')
        ck(len(phases)==(1 if abs(c)==1 else 2),'phase count')

for k in [.002,.005,.01,.02,.03]:
    b=1.0
    spectral=[]
    for z in [0.0,pi]:
        t=branch(z,b,k)
        p=(-t,t,z);q=(1.,-t,z+t)
        M=mtx(*q,b,k)@mtx(*p,b,k)
        spectrum=np.linalg.eigvals(M)
        mags=np.abs(spectrum)
        spectral.append(mags)
    ck(min(spectral[0])>1,'phase zero is repelling for sampled small couplings')
    ck(max(spectral[1])<1,'phase pi is attracting for sampled small couplings')

print('PASS:',checks,'finite symbolic/numerical checks; analytical completeness and local stability are proved in RESULT.md')
