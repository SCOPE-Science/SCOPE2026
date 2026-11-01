#!/usr/bin/env python3
"""Exact small-instance checks for clique-bouquet metric power kernels.

This script is supplementary finite evidence; the accompanying proof handles
arbitrary clique sizes and real exponents.
"""
from fractions import Fraction as F
from itertools import combinations
from sympy import Matrix

def qmatrix(sizes, t):
    labels=[i for i,m in enumerate(sizes) for _ in range(m)]
    M=len(labels)
    return Matrix(M,M,lambda u,v: F(-2) if u==v else (F(-1) if labels[u]==labels[v] else F(t)-2))

def phi(sizes,t):
    if t<=2: return F(0)
    return (t-2)*sum((F(1,1)/(t-1+F(1,m)) for m in sizes),F(0))

def witness(sizes,t):
    outer=[]
    for m in sizes:
        a=t-1+F(1,m)
        outer.extend([1/a/m]*m)
    return Matrix(outer)

def compositions(M,r):
    for separators in combinations(range(1,M), r-1):
        ends=(0,)+separators+(M,)
        yield tuple(ends[i+1]-ends[i] for i in range(r))

def root(sizes):
    lo,hi=2.,5.
    for _ in range(75):
        mid=(lo+hi)/2
        val=(mid-2)*sum(1/(mid-1+1/m) for m in sizes)
        if val<1:lo=mid
        else:hi=mid
    return (lo+hi)/2

checks=0
for sizes in [(1,1),(1,1,1),(2,2),(2,2,2),(1,2),(2,3,1),(1,2,4),(3,3,1),(4,4,2)]:
    M=sum(sizes)
    for t in [F(1),F(2),F(5,2),F(11,4),F(3),F(7,2),F(4),F(5)]:
        A=qmatrix(sizes,t)
        x=witness(sizes,t) if t>2 else Matrix([F(1)]*M)
        s=[]; offset=0
        for m in sizes:
            s.append(sum((x[j] for j in range(offset,offset+m)),F(0)));offset+=m
        rhs=-sum((z*z for z in x),F(0))+(1-t)*sum((z*z for z in s),F(0))+(t-2)*sum(s)**2
        assert (x.T*A*x)[0]==rhs
        f=phi(sizes,t)
        if f>1:
            assert (x.T*A*x)[0]>0
        else:
            # A finite exact Sylvester certificate for nonpositive power quadratic forms.
            B=-A
            for k in range(1,M+1):
                minor=B[:k,:k].det()
                assert minor>=0
                if f<1: assert minor>0
            if f==1: assert B.rank()==M-1
        checks+=1

# Balanced partitions have the smallest exponent, extreme partitions the largest.
for M in range(4,13):
  for r in range(2,min(M,6)+1):
    a,b=divmod(M,r)
    balanced=tuple(sorted([a]*(r-b)+[a+1]*b))
    extreme=tuple(sorted([M-r+1]+[1]*(r-1)))
    low,high=root(balanced),root(extreme)
    for sizes in compositions(M,r):
      rr=root(sizes)
      assert low-1.e-10<=rr<=high+1.e-10
      if tuple(sorted(sizes))!=balanced: assert rr>low+1.e-11
      if tuple(sorted(sizes))!=extreme: assert rr<high-1.e-11
      checks+=1
print('PASS:', checks, 'exact metric-signature or partition-majorization checks')
