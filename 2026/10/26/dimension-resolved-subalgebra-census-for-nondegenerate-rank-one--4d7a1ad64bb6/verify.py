#!/usr/bin/env python3
"""Exact subalgebra census for rank-one quadratic multiplication.

No external dependencies.  Tests several nondegenerate symmetric forms over
prime fields and F_9, comparing direct subspace enumeration with polar formulas.
"""
from itertools import combinations, product
from math import prod, comb

class Field:
    def __init__(self, q):
        assert q in (3, 5, 7, 9)
        self.q = q
        self.p = 3 if q == 9 else q
        self.elements = range(q)
        self.zero, self.one = 0, 1
    def add(self, a, b):
        if self.q != 9:
            return (a+b)%self.q
        return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(self, a):
        return self.sub(0,a)
    def sub(self, a,b):
        if self.q != 9:
            return (a-b)%self.q
        return ((a%3-b%3)%3)+3*((a//3-b//3)%3)
    def mul(self,a,b):
        if self.q!=9:
            return (a*b)%self.q
        x,y=divmod(a,3)[1],a//3
        s,t=b%3,b//3
        return (x*s-y*t)%3+3*((x*t+y*s)%3)
    def pow(self,a,k):
        z=1
        for _ in range(k): z=self.mul(z,a)
        return z
    def character(self,a):
        if a==0: return 0
        return 1 if self.pow(a,(self.q-1)//2)==1 else -1

def gaussian(n,r,q):
    if r<0 or r>n: return 0
    # Compute as two integer products to avoid premature division.
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))

def isotropic_lines(d,q,eps):
    if d<=0: return 0
    if d%2:
        return (q**(d-1)-1)//(q-1)
    m=d//2
    return (q**(m-1)+eps)*(q**m-eps)//(q-1)

def totally_singular(n,r,q,eps):
    if r==0: return 1
    if r>n//2 or r<0: return 0
    numerator=prod(isotropic_lines(n-2*j,q,eps) for j in range(r))
    denominator=prod((q**j-1)//(q-1) for j in range(1,r+1))
    return numerator//denominator

def predicted(n,q,eps,is_u_iso):
    nums=[1]
    for r in range(1,n+1):
        a=gaussian(n-1,r-1,q)
        b=totally_singular(n,r,q,eps)
        c=totally_singular(n-2,r-1,q,eps) if is_u_iso else 0
        nums.append(a+b-c)
    return nums

def subspaces_rref(n,r,field):
    if r==0:
        yield tuple()
        return
    for pivots in combinations(range(n),r):
        free_positions=[(i,j) for i in range(r) for j in range(pivots[i]+1,n) if j not in pivots]
        for entries in product(field.elements,repeat=len(free_positions)):
            rows=[[0]*n for _ in range(r)]
            for i,p in enumerate(pivots): rows[i][p]=1
            for (i,j),v in zip(free_positions,entries): rows[i][j]=v
            yield tuple(tuple(x) for x in rows)

def in_span(vec,rows,F):
    remain=list(vec)
    for row in rows:
        pivot=next(i for i,x in enumerate(row) if x)
        factor=remain[pivot]
        for j in range(len(vec)):
            remain[j]=F.sub(remain[j],F.mul(factor,row[j]))
    return not any(remain)

def bilinear(x,y,diag,F):
    z=0
    for xi,yi,di in zip(x,y,diag):
        z=F.add(z,F.mul(di,F.mul(xi,yi)))
    return z

def actual(n,F,diag,u):
    a=[0]*(n+1)
    total=0
    for r in range(n+1):
        for rows in subspaces_rref(n,r,F):
            total+=1
            # Independent multiplication test: B(x,y)u must lie in W
            # for every pair of RREF basis vectors.  Do not call the
            # structure classification here.
            if all(in_span(tuple(F.mul(bilinear(x,y,diag,F),v) for v in u),rows,F)
                   for x in rows for y in rows):
                a[r]+=1
    return a,total

def run():
    verified=[]
    for q,n_values in [(3,range(1,6)),(5,range(1,5)),(7,range(1,4)),(9,range(1,5))]:
        F=Field(q)
        nonsquare=next(a for a in range(1,q) if F.character(a)==-1)
        for n in n_values:
            for last in [1,nonsquare]:
                diag=[1]*(n-1)+[last]
                if n%2==0:
                    eps=F.character(F.mul(F.pow(F.neg(1),n//2),last))
                else: eps=1
                choices=[tuple([1]+[0]*(n-1))]
                if n>=2:
                    choices.append(tuple([1,1]+[0]*(n-2)))
                    iso_u=next((v for v in product(F.elements,repeat=n) if any(v) and bilinear(v,v,diag,F)==0),None)
                    if iso_u is not None and iso_u not in choices: choices.append(iso_u)
                for u in choices:
                    is_iso=bilinear(u,u,diag,F)==0
                    expected=predicted(n,q,eps,is_iso)
                    got,checked=actual(n,F,diag,u)
                    assert got==expected,(q,n,diag,u,got,expected)
                    verified.append((q,n,last,u,is_iso,tuple(got),checked))
    print('VERIFY_OK cases=',len(verified),'subspaces_examined=',sum(row[-1] for row in verified))
    for row in verified:
        if row[1] in (2,3,4) and row[0] in (3,9) and row[2]==1 and row[3][0]==1:
            print('EXAMPLE q={} n={} diag_last={} isotropic_u={} counts={}'.format(row[0],row[1],row[2],row[4],row[5]))

if __name__=='__main__': run()
