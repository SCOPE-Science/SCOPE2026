#!/usr/bin/env python3
"""Exact finite checks for the Johnson-subset Gaussian first-loss theorem.
Python standard library only. Finite checks complement the analytic proof.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction as F

def C(n,r):return comb(n,r) if 0<=r<=n else 0

def B(k,x):return sum((-1)**r*C(k,r)*x**(r*r) for r in range(k+1))

def coeff(k,j,x):
    s=k-j
    return sum((-1)**r*C(j,r)*x**((s+r)**2) for r in range(j+1))

def decomposition(k,x):
    count=0
    points=list(combinations(range(2*k),k))
    for S in points:
        SS=set(S)
        for T in points:
            h=len(SS.intersection(T))
            lhs=x**((k-h)**2)
            rhs=sum(coeff(k,j,x)*C(h,j) for j in range(k+1))
            assert lhs==rhs, (k,S,T)
            count+=1
    return count

def top_vector(k,n):
    pairs=[(2*i,2*i+1) for i in range(k)]
    vec={tuple(sorted(t)):(-1)**sum(t[i]==pairs[i][1] for i in range(k)) for t in product(*pairs)}
    vals=list(combinations(range(n),k))
    for S in vals:
        val=[0]*(k+1)
        for T,w in vec.items():val[k-len(set(S).intersection(T))]+=w
        for i in range(k+1):
            assert val[i] == ((-1)**i*C(k,i))*vec.get(S,0),(k,n,S,i)
    return len(vals)*(k+1)

def main():
    signatures=0
    dense=0
    direct=0
    for k in range(3,13):
        q=F(1,k-1)
        assert B(k,F(0))==1 and B(k,q)<0,k
        # Rational sign checks for intermediate finite differences at the proved upper bracket.
        for j in range(k):
            assert coeff(k,j,q)>0,(k,j)
            signatures+=1
        # First zero is bracketed by rational endpoints; the proof establishes uniqueness.
        low,high=0.0,1.0/(k-1)
        for _ in range(55):
            mid=(low+high)/2
            if B(k,mid)>0: low=mid
            else: high=mid
        for factor in (2,3,5):
            x=F(1,factor*k)
            assert B(k,x)>0,(k,x)
            assert min(coeff(k,j,x) for j in range(k))>0,(k,x)
    for k in (3,4): dense+=decomposition(k,F(1,k))
    for k in (3,4,5,6):direct+=top_vector(k,2*k)
    print('PASS:',signatures,'exact rational coefficient tests;',dense,
          'exact matrix-entry decompositions;',direct,'exact top-sector matrix components')

if __name__=='__main__':main()
