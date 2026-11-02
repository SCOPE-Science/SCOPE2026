#!/usr/bin/env python3
"""Exact checks for the ranked-spacing/Greenwood covariance theorem.

This checker uses independent polynomial integration of degree-three Dirichlet
monomials, rather than relying on the harmonic covariance identity being tested.
The finite computations support, but do not replace, the proof for all sizes.
"""
from fractions import Fraction as F
from math import factorial, exp, log

checks=0

def chk(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def dirichlet_moment(m, indices):
    """E product(Y_i), Y uniform on the (m-1)-simplex."""
    counts={}
    for i in indices:
        counts[i]=counts.get(i,0)+1
    numerator=1
    for count in counts.values():
        numerator*=factorial(count)
    denominator=1
    for h in range(len(indices)):
        denominator*=m+h
    return F(numerator,denominator)


def direct(m):
    a=[[F(1,max(i,j)) for j in range(1,m+1)] for i in range(1,m+1)]
    equad=sum((a[i][j]*dirichlet_moment(m,[i,j]) for i in range(m) for j in range(m)),F(0))
    chk(equad==F(2,m+1),f'quadratic mean m={m}')
    cov=[]
    for k in range(1,m+1):
        ex=sum((F(1,j)*dirichlet_moment(m,[j-1]) for j in range(k,m+1)),F(0))
        exq=sum((F(1,j)*a[i][h]*dirichlet_moment(m,[j-1,i,h])
                   for j in range(k,m+1) for i in range(m) for h in range(m)),F(0))
        cov.append(exq-ex*equad)
    return cov


def formula(m):
    h=[F(0)]
    h2=[F(0)]
    for i in range(1,m+1):
        h.append(h[-1]+F(1,i))
        h2.append(h2[-1]+F(1,i*i))
    den=m*(m+1)*(m+2)
    vals=[]
    for k in range(1,m+1):
        t=h[m]-h[k-1]
        u=h2[m]-h2[k-1]
        vals.append((t*t+u-2*t)/den)
        chk(t>0,f'positive tail m={m}, k={k}')
    return vals

for m in range(2,10):
    actual=direct(m)
    predicted=formula(m)
    for k,(a,b) in enumerate(zip(actual,predicted),1):
        chk(a==b,f'exact covariance m={m}, k={k}: {a} != {b}')

for m in range(2,351):
    vals=formula(m)
    chk(vals[0]>0,f'largest covariance sign m={m}')
    chk(vals[-1]<0,f'smallest covariance sign m={m}')
    state=0
    zeros=0
    for k,v in enumerate(vals,1):
        if v>0:
            chk(state==0,f'positive covariance after sign transition m={m} k={k}')
        elif v==0:
            zeros+=1
            chk(state==0,f'second zero crossing m={m} k={k}')
            state=1
        else:
            state=1
    chk(zeros<=1,f'multiple zero indices m={m}')

for m in [50,100,500,1000,5000,20000]:
    h=[0.0]
    for j in range(1,m+1):h.append(h[-1]+1.0/j)
    positive=[]
    for k in range(1,m+1):
        t=h[m]-h[k-1]
        u=sum(1.0/(j*j) for j in range(k,m+1)) if m<=1000 else 0.0
        if t*t+u-2*t>0:positive.append(k)
    threshold=positive[-1]/m
    print(f'rank fraction m={m}: {threshold:.6f}; limiting value exp(-2)={exp(-2):.6f}')
    chk(abs(threshold-exp(-2))<max(0.11,5.0/m),f'asymptotic threshold m={m}')

print(f'PASS: {checks} deterministic exact/arithmetic checks')
