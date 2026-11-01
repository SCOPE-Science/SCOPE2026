#!/usr/bin/env python3
"""Exact reproducibility checks for facial distances of hypersimplices.

Standard library only. This verifies finite rational identities and geometric
witness constructions; the all-parameter proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations

COUNT = 0

def face_gap(n,k,a,b):
    """Squared distance of a positive-dimensional coordinate face."""
    m=n-a-b
    assert 0<=a<=k-1 and 0<=b<=n-k-1 and a+b>0
    assert 0<k-a<m
    D=m*(a+b)+4*a*b
    return Q(n,D)

def direct_face_minimum(n,k,a,b):
    """Independently minimize the 1-simplex mixture quadratic in rationals."""
    m=n-a-b
    assert 0<k-a<m
    if a==0: return Q(1,b)+Q(1,m)
    if b==0: return Q(1,a)+Q(1,m)
    p,q,u=Q(1,a),Q(1,b),Q(1,m)
    t=(q+2*u)/(p+q+4*u)
    assert 0<t<1
    return p*t*t+q*(1-t)*(1-t)+u*(2*t-1)**2

def closed_D(n,k):
    q=min(k,n-k)
    if n==2:return q*(n-q)
    if n>=4*q-1:
        return n*n//4+2*n*(q-1)
    return 4*q*(n-q)-2*n

def check_witness(n,k,a,b):
    """Enumerate vertices; verify both one-swap outside orbits and their barycenters."""
    global COUNT
    m=n-a-b
    I=set(range(a));J=set(range(a,a+b));M=set(range(a+b,n))
    r=k-a
    assert 0<r<m
    verts=[set(c) for c in combinations(range(n),k)]
    F=[S for S in verts if I<=S and not (S & J)]
    assert F
    outside=[S for S in verts if S not in F]
    assert outside
    x=[Q(1) if i in I else Q(0) if i in J else Q(r,m) for i in range(n)]
    # Inward one-swap orbits from I to M and M to J.
    yA=[S for S in outside if len(I-S)==1 and not (S & J)]
    yB=[S for S in outside if not (I-S) and len(S & J)==1]
    if a:assert yA
    if b:assert yB
    def average(sets):return [sum((Q(i in S) for S in sets),Q(0))/len(sets) for i in range(n)]
    if a: ya=average(yA)
    if b: yb=average(yB)
    if a and b:
        D=m*(a+b)+4*a*b
        t=Q(a*(m+2*b),D)
        y=[t*ya[i]+(1-t)*yb[i] for i in range(n)]
    elif a: y=ya
    else: y=yb
    d2=sum(((u-v)**2 for u,v in zip(x,y)),Q(0))
    assert d2==face_gap(n,k,a,b),(n,k,a,b,d2,face_gap(n,k,a,b))
    COUNT+=1

if __name__=='__main__':
    for n in range(3,31):
        for k in range(1,n):
            q=min(k,n-k)
            candidates=[]
            for a in range(k):
                for b in range(n-k):
                    if a+b==0:continue
                    v=face_gap(n,k,a,b)
                    assert v==direct_face_minimum(n,k,a,b),(n,k,a,b)
                    candidates.append((n*(a+b)-(a-b)**2,a,b))
                    COUNT+=1
            D=max(t[0] for t in candidates)
            assert D==closed_D(n,k),(n,k,D,closed_D(n,k))
            assert D>=k*(n-k)
            COUNT+=1
    for n in range(3,9):
        for k in range(1,n):
            for a in range(k):
                for b in range(n-k):
                    if a+b:check_witness(n,k,a,b)
    # Special boundary and asymptotic tests are exact integer identities.
    for q in range(1,81):
        for n in range(max(3,2*q),max(3,6*q)):
            if q>n//2:continue
            D=closed_D(n,q)
            upper=n*n//4+2*n*(q-1)
            cap=4*q*(n-q)-2*n
            assert D == (upper if n>=4*q-1 else cap)
            COUNT+=1
    assert closed_D(2,1)==1
    assert closed_D(3,1)==2
    assert closed_D(4,2)==8
    assert closed_D(8,2)==32
    assert closed_D(10,2)==45
    print(f'PASS: {COUNT} exact rational/integer and vertex-orbit checks')
