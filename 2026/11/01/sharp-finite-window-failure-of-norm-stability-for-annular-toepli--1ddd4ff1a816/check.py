#!/usr/bin/env python3
"""Exact finite checks and asymptotic diagnostics for annular Toeplitz displacement."""
from fractions import Fraction as Q
from math import sqrt

checks = 0

def eq(a, b):
    global checks
    assert a == b, (a,b)
    checks += 1

def F(t, delta):
    """C1 compactly supported bump, exactly normalized at its peak."""
    if t <= 0 or t >= 1:
        return Q(0)
    c = 2 / (1 - 2*delta)
    if t <= delta:
        return c*t*t/(2*delta)
    if t <= Q(1,2) - delta:
        return c*(t - delta/2)
    if t <= Q(1,2) + delta:
        z = t - (Q(1,2)-delta)
        return c*(Q(1,2) - Q(3,2)*delta + z-z*z/(2*delta))
    if t <= 1-delta:
        return c*(1-t-delta/2)
    return c*(1-t)*(1-t)/(2*delta)

def finite_values(q, m):
    N=m*m
    delta=Q(1,m)
    assert m>=4
    raw=[F(Q(j,N+1),delta) for j in range(N+2)]
    scale=max(raw)
    k={N+j:raw[j]/scale for j in range(1,N+1)}
    def get(n):return k.get(n,Q(0))
    errors=[]
    for n in range(N-3,2*N+4):
        ell=get(n+2)-(1+q)*get(n+1)+q*get(n)
        direct=((1+q**(n+2))*get(n+2)-(1+q)*(1+q**(n+1))*get(n+1)+q*(1+q**n)*get(n))/(1+q**n)
        correction=(1-q*q)*q**n/(1+q**n)*(get(n+1)-get(n+2))
        eq(direct,ell+correction)
        assert 0<=get(n)<=1
        errors.append(abs(direct))
    assert max(k.values())==1
    eta=max(errors)
    bound=Q(2)*(1-q)/Q(N+1)-(1-q*q)*q**(N-1)
    assert eta>=bound
    global checks
    checks+=2
    return N,float(N*eta)

for q in (Q(1,4),Q(1,2),Q(3,4)):
    vals=[]
    for m in (4,5,7,10,15,20):
        N, v=finite_values(q,m)
        vals.append((N,round(v,8)))
    print('q=',q,'N*residual:',vals,'asymptotic target:',float(2*(1-q)))
print('EXACT_ASSERTIONS_PASSED',checks)
