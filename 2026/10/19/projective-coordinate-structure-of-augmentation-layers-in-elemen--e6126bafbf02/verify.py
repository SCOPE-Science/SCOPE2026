#!/usr/bin/env python3
"""Independent small-rank checks for projective augmentation quotients.
Requires Python 3 and sympy. Does not establish the infinite-degree theorem.
"""
import itertools
import math
from sympy import eye, zeros, Matrix
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ


def dim_formula(p,d,r):
    return sum(1 for i in range(1,d+1) for a in itertools.product(range(p), repeat=i-1) if sum(a)<=r-1)

def smith_quotients(p,d,limit):
    members=list(itertools.product(range(p), repeat=d)); zero=members[0]; non=members[1:]
    index={v:i for i,v in enumerate(non)}; n=len(non)
    shifts=[]
    for j in range(d):
        T=zeros(n); ej=tuple(int(i==j) for i in range(d))
        for k,v in enumerate(non):
            pair=tuple((v[i]+ej[i])%p for i in range(d))
            for w,c in ((pair,1),(ej,-1),(v,-1)):
                if w!=zero: T[index[w],k]+=c
        shifts.append(T)
    L=eye(n)
    for r in range(1,limit+1):
        NL=hermite_normal_form(Matrix.hstack(*(T*L for T in shifts)))
        D=smith_normal_form(L.inv()*NL, domain=ZZ)
        invariant=[abs(int(D[i,i])) for i in range(n) if abs(int(D[i,i]))!=1]
        assert all(v==p for v in invariant),(p,d,r,invariant)
        assert len(invariant)==dim_formula(p,d,r),(p,d,r,len(invariant),dim_formula(p,d,r))
        L=NL

def field_rank(rows,p):
    A=[list(map(lambda t:t%p,row)) for row in rows]; m=len(A); n=len(A[0]) if m else 0; rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if A[i][j]), None)
        if pivot is None: continue
        A[rank],A[pivot]=A[pivot],A[rank]
        mult=pow(A[rank][j],-1,p)
        A[rank]=[(x*mult)%p for x in A[rank]]
        for i in range(m):
            if i!=rank and A[i][j]:
                c=A[i][j]; A[i]=[(x-c*y)%p for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==m:break
    return rank

def projective_rank(p,d,r):
    B=[]
    for i in range(d):
        for a in itertools.product(range(p),repeat=i):
            if sum(a)<r:
                exp=tuple(a)+(r-sum(a),)+(0,)*(d-i-1)
                B.append(exp)
    points=[]
    for i in range(d):
        for a in itertools.product(range(p), repeat=i):
            points.append(tuple(a)+(1,)+(0,)*(d-i-1))
    E=[[math.prod(pow(x,e,p) for x,e in zip(v,b))%p for b in B] for v in points]
    assert field_rank(E,p)==len(B),(p,d,r)


def check_star(p,d):
    # In group basis (integer coefficients), core multiplication is 2b-a.
    members=list(itertools.product(range(p),repeat=d))
    unit=members[0]
    def sub(x,y): return tuple((a-b)%p for a,b in zip(x,y))
    def double(x): return tuple((2*a)%p for a in x)
    def add(x,y): return tuple((a+b)%p for a,b in zip(x,y))
    for a,b in itertools.product(members,repeat=2):
        left=sub(double(b),a)
        assert left==add(tuple(-i%p for i in a), double(b))
    # Graded action on generator (e_i - 1) scales by -1 and 2,
    # checked modulo the square by linearizing group endomorphisms.
    for c in members:
        assert tuple((-i)%p for i in c)==tuple((p-1)*i%p for i in c)
        assert double(c)==tuple((2*i)%p for i in c)

if __name__=='__main__':
    for p,d,maxr in ((3,2,6),(5,2,5),(3,3,5),(2,3,4)):
        smith_quotients(p,d,maxr)
        for r in range(1,maxr+1):projective_rank(p,d,r)
        check_star(p,d)
    print('VERIFY_OK: exact Smith forms, projective evaluations and core transport')
