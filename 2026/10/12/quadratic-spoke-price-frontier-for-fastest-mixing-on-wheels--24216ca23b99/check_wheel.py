"""Supplementary finite checks for the price-optimal continuous-time wheel spectral gap.
This is supplementary computation, not an infinite-dimensional or all-n proof.
Requires Python 3, numpy and sympy.
"""
from fractions import Fraction
from math import cos, pi, sin
import random
import numpy as np
import sympy as sp

def wheel_laplacian(n, a, b, exact=False):
    if exact:
        M=sp.zeros(n+1)
    else:
        M=np.zeros((n+1,n+1), dtype=float)
    for i in range(n):
        for u,v,w in [(0,i+1,a[i]),(i+1,((i+1)%n)+1,b[i])]:
            M[u,u]+=w
            M[v,v]+=w
            M[u,v]-=w
            M[v,u]-=w
    return M

def proposed(n,t):
    mu=4*sin(pi/n)**2
    if t < 1/mu:
        a=1/(n*t); b=0.
    elif t>1/mu:
        a=mu/(n*(mu*t+n)); b=1/(mu*t+n)
    else:
        a=mu/(n*(n+1)); b=(1/n-a/mu)
    return a,b,min((n+1)*a,a+mu*b)

checks=0
for n in (4,5,6,7,8,10,13,19):
    tc=1/(4*sin(pi/n)**2)
    for t in (tc/4,tc*0.8,tc,tc*1.2,tc*5):
        a,b,val=proposed(n,t)
        assert a>0 and b>=0 and abs(n*(t*a+b)-1)<2e-14
        lam=np.linalg.eigvalsh(wheel_laplacian(n,[a]*n,[b]*n))[1]
        assert abs(lam-val)<4e-13,(n,t,lam,val)
        checks+=1

rng=random.Random(360047)
for n in (4,6,9,12):
    tc=1/(4*sin(pi/n)**2)
    for t in (tc/5,tc,tc*7):
        a,b,opt=proposed(n,t)
        for _ in range(100):
            raw=[rng.expovariate(1.) for i in range(2*n)]
            cost=sum(t*x for x in raw[:n])+sum(raw[n:])
            aw=[x/cost for x in raw[:n]]
            bw=[x/cost for x in raw[n:]]
            lam=np.linalg.eigvalsh(wheel_laplacian(n,aw,bw))[1]
            assert lam <=opt+4e-13,(n,t,lam,opt)
            checks+=1

# Exact six-spoke cases, with mu=1 and threshold t=1.
for t,spoke,rim,opt in [(sp.Rational(1,2),sp.Rational(1,3),sp.Rational(0),sp.Rational(1,3)),
                          (sp.Rational(1),sp.Rational(1,42),sp.Rational(1,7),sp.Rational(1,6)),
                          (sp.Rational(1),sp.Rational(1,6),sp.Rational(0),sp.Rational(1,6)),
                          (sp.Rational(2),sp.Rational(1,48),sp.Rational(1,8),sp.Rational(7,48))]:
    assert 6*(t*spoke+rim)==1
    eig=wheel_laplacian(6,[spoke]*6,[rim]*6,True).eigenvals()
    eiglist=sorted([v for v,m in eig.items() for _ in range(m)])
    assert eiglist[0]==0 and eiglist[1]==opt,(t,eiglist,opt)
    checks+=1

# Exact four-spoke asymmetric Laplacian Fourier trial identity for rational weights.
n=4
aw=[sp.Rational(1,5),sp.Rational(1,7),sp.Rational(1,9),sp.Rational(1,13)]
bw=[sp.Rational(1,3),sp.Rational(1,11),sp.Rational(1,4),sp.Rational(1,15)]
L=wheel_laplacian(n,aw,bw,True)
c=sp.Matrix([0,1,0,-1,0]); s=sp.Matrix([0,0,1,0,-1]); h=sp.Matrix([-4,1,1,1,1]);
assert h.dot(L*h)/h.dot(h)==5*sum(aw)/4
mu=sp.Integer(2)
assert sp.simplify((c.dot(L*c)/c.dot(c)+s.dot(L*s)/s.dot(s))/2 - (sum(aw)+mu*sum(bw))/4)==0
checks+=2
print('VERIFY_OK',checks,'supplementary finite wheel spectral and Rayleigh checks; analytical argument proves arbitrary size')
