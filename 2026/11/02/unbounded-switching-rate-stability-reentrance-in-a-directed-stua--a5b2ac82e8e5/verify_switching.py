#!/usr/bin/env python3
"""Finite consistency checks for a switched directed three-oscillator Floquet theorem.

Requires only Python 3 standard library; does not prove the asymptotic count.
"""
import cmath
import math

SQ3=math.sqrt(3.0)
LAM=complex(-1.5,SQ3/2)

def mul(x,y):
    return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def det(x):
    return x[0][0]*x[1][1]-x[0][1]*x[1][0]

def tr(x):
    return x[0][0]+x[1][1]

def matrices(u,v):
    jh=[[3*u,-v],[3*v,u]]
    return [[[(-2 if i==j==0 else 0) + (l*jh[i][j]) for j in range(2)] for i in range(2)] for l in [LAM,LAM.conjugate()]]

def exp2(A,t):
    ct=tr(A)/2
    C=[[A[i][j]-(ct if i==j else 0) for j in range(2)] for i in range(2)]
    d=cmath.sqrt(C[0][0]**2+C[0][1]*C[1][0])
    f=cmath.sinh(d*t)/d if abs(d)>1.e-14 else t
    scale=cmath.exp(ct*t)
    return [[scale*((cmath.cosh(d*t) if i==j else 0)+f*C[i][j]) for j in range(2)] for i in range(2)]

def closed(u,v,t):
    B=2+6*u
    h=1+3*u+3*u*u-9*v*v
    R=math.sqrt(h*h+9*v*v)
    r=h/R
    delta=cmath.sqrt((-1+u*LAM)**2-3*v*v*LAM**2)
    return math.exp(-B*t)*((1+r)*math.cosh(2*delta.real*t)+(1-r)*math.cos(2*delta.imag*t)),math.exp(-2*B*t)

def stable(u,v,t):
    z,d=closed(u,v,t)
    return abs(z)<1+d

for u in (.02,.05,.2,.7,2):
    for v in (.1,1,10,100):
        h=1+3*u+3*u*u-9*v*v
        d2=(-1+u*LAM)**2-3*v*v*LAM**2
        assert abs(abs(d2)**2-h*h-9*v*v)<1.e-8*max(1,9*v*v)
        ap,am=matrices(u,v)
        avg=[[(ap[i][j]+am[i][j])/2 for j in range(2)] for i in range(2)]
        davg=3*u+27*(u*u+v*v)/4
        assert abs(det(avg)-davg)<1.e-10*max(1,davg)
        for t in (.0001,.003,.01):
            M=mul(exp2(am,t),exp2(ap,t))
            Z,D=closed(u,v,t)
            assert abs(tr(M).imag)<1.e-8*max(1,abs(Z))
            assert abs(tr(M)-Z)<2.e-8*max(1,abs(Z))
            assert abs(det(M)-D)<2.e-8*max(1,abs(D))

u=.05
v=1000.
d=cmath.sqrt((-1+u*LAM)**2-3*v*v*LAM**2)
eta=abs(d.imag)
assert stable(u,v,1.e-6)
for n in (2,3,4):
    peak=math.pi*n/eta
    trough=math.pi*(n+.5)/eta
    assert not stable(u,v,peak), ('peak',n,peak)
    assert stable(u,v,trough), ('trough',n,trough)
    peak_trace,_=closed(u,v,peak)
    trough_trace,_=closed(u,v,trough)
    B=2+6*u
    print(f'n={n}: unstable peak tau={peak:.12f}, normalized trace={peak_trace/(1+math.exp(-2*B*peak)):.9f}; stable trough tau={trough:.12f}, normalized trace={trough_trace/(1+math.exp(-2*B*trough)):.9f}')
print('PASS: 60 direct monodromy comparisons, 20 discriminant/average identities, and 6 alternating sample inequalities.')
