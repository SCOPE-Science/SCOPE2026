#!/usr/bin/env python3
"""Exact rational root/sign certificate and independent graph checks for KG(11,5).
Requires Python 3 and numpy. No external files or network.
"""
from fractions import Fraction
from math import comb
from collections import deque
from itertools import combinations
import numpy as np

R=5
BASES=(1,2,3,4,5)
# Nonconstant spectral rows, ordered by Specht/Johnson level j=1,...,5.
ROWS={
 1:(-5,19,-35,40,-20),
 2:(4,10,10,-5,-20),
 3:(-3,3,3,-12,8),
 4:(2,-2,-7,-2,8),
 5:(-1,-5,5,10,-10),
}
MULT={j:comb(11,j)-comb(11,j-1) for j in range(1,6)}
ROW0=(6,30,75,150,200)

def rational_power_bounds(base, numer, denom, scale=10**10):
    if base==1:return (Fraction(1),Fraction(1))
    # Floating arithmetic supplies only a proposed integer; the assertions
    # below certify both rational inequalities using integers alone.
    q=int(base**(numer/denom)*scale)
    target=base**numer*scale**denom
    while q**denom>target:q-=1
    while (q+1)**denom<=target:q+=1
    assert q**denom<=target<(q+1)**denom
    return Fraction(q,scale),Fraction(q+1,scale)

def linear_bounds(coeff, boxes):
    lo=sum(Fraction(c)*boxes[b][0 if c>=0 else 1] for b,c in enumerate(coeff,1))
    hi=sum(Fraction(c)*boxes[b][1 if c>=0 else 0] for b,c in enumerate(coeff,1))
    return lo,hi

def certificate():
    assert 5**8>2**6*3**7   # makes level-4 derivative strictly positive for p >= 0
    lo_exp=(71,200) # 0.355
    hi_exp=(89,250) # 0.356
    lower={b:rational_power_bounds(b,*lo_exp) for b in BASES}
    upper={b:rational_power_bounds(b,*hi_exp) for b in BASES}
    # 1^p = 1, and 2^p,..,5^p increase with p.
    assert linear_bounds(ROWS[4],lower)[1]<0
    assert linear_bounds(ROWS[4],upper)[0]>0
    crossing={b:(lower[b][0],upper[b][1]) for b in BASES}
    for level in (1,2,3,5):
        left,right=linear_bounds(ROWS[level],crossing)
        assert right<0,(level,float(right))
    return {i:tuple(float(t) for t in linear_bounds(ROWS[i],crossing)) for i in (1,2,3,5)}

def graph_checks():
    masks=[sum(1<<i for i in s) for s in combinations(range(11),5)]
    N=len(masks)
    assert N==462
    A=np.zeros((N,N),dtype=np.int64)
    for i,a in enumerate(masks):
        for j in range(i+1,N):
            if a&masks[j]==0:A[i,j]=A[j,i]=1
    D=np.empty((N,N),dtype=np.int64)
    for i in range(N):
        distances=[-1]*N
        distances[i]=0
        q=deque([i])
        while q:
            u=q.popleft()
            for v in np.flatnonzero(A[u]):
                if distances[v]<0:
                    distances[v]=distances[u]+1
                    q.append(int(v))
        for j,b in enumerate(masks):
            s=(masks[i]&b).bit_count()
            assert distances[j]==min(2*(5-s),2*s+1)
        D[i]=distances
    assert np.all(A.sum(axis=1)==6)
    mats=[(D==d).astype(np.int64) for d in range(6)]
    b=(6,5,5,4,4,0); c=(0,1,1,2,2,3)
    for d in range(6):
        rhs=np.zeros_like(A)
        if d>0:rhs+=b[d-1]*mats[d-1]
        rhs+=(6-b[d]-c[d])*mats[d]
        if d<5:rhs+=c[d+1]*mats[d+1]
        assert np.array_equal(A@mats[d],rhs),d
    xx=[6,-5,4,-3,2,-1]
    mm=[1]+[MULT[j] for j in range(1,6)]
    assert sum(mm)==N
    for j,x in enumerate(xx):
        p=[1,x]
        for d in range(1,5):
            n=(x-(6-b[d]-c[d]))*p[-1]-b[d-1]*p[-2]
            assert n%c[d+1]==0
            p.append(n//c[d+1])
        assert tuple(p[1:])==(ROW0 if j==0 else ROWS[j]),(j,p)
    # Numerical eigen-solver is an independent finite cross-check, not the proof.
    for exponent in (0.,.3556362323741432,1.):
        weighted=np.zeros((N,N),float)
        for d in range(1,6):weighted+=d**exponent*mats[d]
        observed=np.linalg.eigvalsh(weighted)
        theoretical=[]
        for j in range(6):
            coefficients=ROW0 if j==0 else ROWS[j]
            value=sum(coefficients[d-1]*d**exponent for d in range(1,6))
            theoretical.extend([value]*mm[j])
        assert max(abs(a-b) for a,b in zip(observed,sorted(theoretical)))<1e-7
    return N

if __name__=='__main__':
    enclosures=certificate()
    n=graph_checks()
    print('EXACT_INTERVAL_CERTIFICATE_OK',enclosures)
    print('CHECK_OK',n,'vertices, exact graph distances, intersection recurrence, full three-exponent spectra')
