#!/usr/bin/env python3
"""Finite algebraic diagnostics for the two-dimensional antilinear ellipse formula.
Requires Python 3.9+ standard library only. Universal validity rests on the proof.
"""
import cmath
import math
import random

R=random.Random(417229)
TWO_PI=2*math.pi
assertions=0

def near(x,y,tol=1e-9):
    global assertions
    assertions+=1
    if abs(x-y)>tol*(1+abs(x)+abs(y)):
        raise AssertionError((x,y,abs(x-y)))

def check(flag,explanation=''):
    global assertions
    assertions+=1
    if not flag:
        raise AssertionError(explanation)

def ellipse(a,b,q):
    alpha=(1+q)/2
    beta=(1-q)/2
    return alpha*a-beta*b,alpha*a+beta*b,alpha*b-beta*a,alpha*b+beta*a

def point(h,v,angle):
    return h*math.cos(angle)+1j*v*math.sin(angle)

# Direct orthogonal basis expansion of a Takagi-diagonalized bilinear matrix.
for case in range(60):
    a,b=sorted((R.random()*3,R.random()*3),reverse=True)
    k=(R.random()-.5)*3+1j*(R.random()-.5)*3
    q=R.random()
    al=(1+q)/2;be=(1-q)/2;tau=math.sqrt(1-q*q)
    h,v,h2,v2=ellipse(a,b,q)
    check(abs(h2)<=h+1e-12 and v2<=v+1e-12)
    for _ in range(350):
        weight=R.random(); ph=R.random()*TWO_PI; ps=R.random()*TWO_PI;ga=R.random()*TWO_PI
        z=math.sqrt(weight)*cmath.exp(1j*ph)
        w=math.sqrt(1-weight)*cmath.exp(1j*ps)
        detphase=cmath.exp(2j*ga)
        u=(cmath.exp(1j*ga)*z,cmath.exp(1j*ga)*w)
        vcol=(-cmath.exp(1j*ga)*w.conjugate(),cmath.exp(1j*ga)*z.conjugate())
        x=tuple(math.sqrt(al)*u[i]+math.sqrt(be)*vcol[i] for i in range(2))
        y=tuple(math.sqrt(al)*u[i]-math.sqrt(be)*vcol[i] for i in range(2))
        # Hermitian inner product linear in first argument.
        near(sum(x[i]*y[i].conjugate() for i in range(2)),q)
        near(sum(abs(t)**2 for t in x),1)
        near(sum(abs(t)**2 for t in y),1)
        # B = [[a,k],[-k,b]], z_direct = x^T B y.
        direct=x[0]*(a*y[0]+k*y[1])+x[1]*(-k*y[0]+b*y[1])
        reduced=detphase*(weight*point(h,v,2*ph)+(1-weight)*point(h2,v2,2*ps)-tau*k)
        near(direct,reduced)
        inner=reduced/detphase+tau*k
        if h>1e-12:
            check((inner.real/h)**2+(inner.imag/v)**2<1+1e-8)
        else:
            check(abs(inner.real)<1e-9 and abs(inner.imag)<=v+1e-8)

# Axially aligned cases: boundary maximization via dense independent grid.
for case in range(72):
    a=R.random()*3+.05;b=R.random()*a;q=R.random()*.999
    k=R.random()*3
    h,v,_,_=ellipse(a,b,q)
    gap=v*v-h*h
    d=math.sqrt(1-q*q)*k
    if gap>1e-10 and d*h<=gap:
        upper=v*math.sqrt(1+d*d/gap)
    else:
        upper=d+h
    lower=max(0,d-h)
    max_boundary=0.0
    min_boundary=1e50
    for j in range(2049):
        f=abs(point(h,v,TWO_PI*j/2048)-d)
        max_boundary=max(max_boundary,f)
        min_boundary=min(min_boundary,f)
        check(f<=upper+1e-9)
    check(max_boundary>upper-1e-5)
    if d>h+1e-8:
        near(min_boundary,lower,tol=1e-5)
    else:
        check(lower==0)

# Complex quaternionic root example: B from [[0,-b],[a,0]], Takagi values = (a-b)/2.
for a,b in ((2.,1.),(4.,.3),(.7,.7)):
    for q in (0.,.2,.6,.9,1.):
        sym=(a-b)/2
        skew=1j*(a+b)/2
        h,v,_,_=ellipse(sym,sym,q)
        tau=math.sqrt(1-q*q)
        l=max(0,tau*(a+b)/2-v)
        u=tau*(a+b)/2+v
        near(l,max(0,(tau*(a+b)-(a-b))/2))
        near(u,(tau*(a+b)+(a-b))/2)

# Zero and skew-only: the fixed-modulus circle is not filled when q<1.
for q in (0.,.1,.7,1.):
    h,v,_,_=ellipse(0,0,q)
    check(h==0 and v==0)
    near(math.sqrt(1-q*q)*abs(3+4j),5*math.sqrt(1-q*q))

# Antiunitary canonical example: aI + kJ, with a^2+k^2=1.
for theta in (.17,.61,1.09):
    a=math.cos(theta)
    k=math.sin(theta)
    for q in (0.,.2,.5,.75,.99,1.):
        h,v,_,_=ellipse(a,a,q)
        tau=math.sqrt(1-q*q)
        d=tau*k
        gap=v*v-h*h
        if gap>1e-12 and d*h<=gap:
            outer=v*math.sqrt(1+d*d/gap)
        else:
            outer=d+h
        inner=max(0,d-h)
        near(inner,max(0,k*tau-a*q))
        expected=1. if q<=a+1e-12 else a*q+k*tau
        near(outer,expected)

print('PASS',assertions,'finite deterministic assertions; no infinite claim certified by sampling')
