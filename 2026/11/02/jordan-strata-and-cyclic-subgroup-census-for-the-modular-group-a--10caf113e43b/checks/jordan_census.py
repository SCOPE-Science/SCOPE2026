#!/usr/bin/env python3
"""Finite-field tests for regular multiplication in k[X,Y]/(X^3,Y^3), characteristic three."""
from collections import Counter
from itertools import product
import random

MONS = tuple((i,j) for i in range(3) for j in range(3))
IDX = {p:i for i,p in enumerate(MONS)}

class Field:
    def __init__(self,q):
        assert q in (3,9)
        self.q=q
        self.p=3
        if q==3:
            self.add = lambda a,b:(a+b)%3
            self.neg = lambda a:(-a)%3
            self.mul = lambda a,b:(a*b)%3
        else:
            # t^2+1 irreducible over F3; coordinates a+3b
            self.add=lambda a,b: ((a%3+b%3)%3)+3*((a//3+b//3)%3)
            self.neg=lambda a:((-(a%3))%3)+3*((-(a//3))%3)
            self.mul=lambda a,b:((a%3)*(b%3)+2*(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        self.inv={a:next(b for b in range(1,q) if self.mul(a,b)==1) for a in range(1,q)}
    def sub(self,a,b):return self.add(a,self.neg(b))

def mult(A,B,F):
    C=[0]*9
    for ia,(i,j) in enumerate(MONS):
        for ib,(u,v) in enumerate(MONS):
            if i+u<3 and j+v<3:
                pos=IDX[i+u,j+v]
                C[pos]=F.add(C[pos],F.mul(A[ia],B[ib]))
    return C

def rank(M,F):
    A=[list(row) for row in M];n=len(A);m=len(A[0]);r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        factor=F.inv[A[r][c]]
        for j in range(c,m):A[r][j]=F.mul(A[r][j],factor)
        for i in range(r+1,n):
            if A[i][c]:
                val=A[i][c]
                for j in range(c,m):A[i][j]=F.sub(A[i][j],F.mul(val,A[r][j]))
        r+=1
        if r==n:break
    return r

def operator(f,F):
    basis=[tuple(int(i==j) for i in range(9)) for j in range(9)]
    cols=[mult(f,e,F) for e in basis]
    return [[cols[j][i] for j in range(9)] for i in range(9)]

def type_from_ranks(f,F):
    a=operator(f,F)
    r1=rank(a,F)
    ff=mult(f,f,F)
    r2=rank(operator(ff,F),F)
    assert mult(ff,f,F)==[0]*9
    t3=r2;t2=r1-2*r2;t1=9-2*t2-3*t3
    assert min(t1,t2,t3)>=0
    return (t3,t2,t1)

def expected(f,F):
    # Polynomial coefficient indices for x, y, x², xy, y², x²y, xy², x²y².
    ix=IDX[1,0];iy=IDX[0,1]
    ia=IDX[2,0];ib=IDX[1,1];ic=IDX[0,2]
    id_=IDX[2,1];ie=IDX[1,2];ig=IDX[2,2]
    if f[ix]!=0 or f[iy]!=0: return (3,0,0)
    a,b,c=f[ia],f[ib],f[ic]
    if (a,b,c)!=(0,0,0):
        disc=F.sub(F.mul(b,b),F.mul(a,c))
        if disc:return (1,2,2)
        return (0,3,3)
    if f[id_]!=0 or f[ie]!=0:return (0,2,5)
    if f[ig]!=0:return (0,1,7)
    return (0,0,9)

def expected_counts(q):
    return {(3,0,0):(q*q-1)*q**6,
            (1,2,2):(q**3-q*q)*q**3,
            (0,3,3):(q*q-1)*q**3,
            (0,2,5):(q*q-1)*q,
            (0,1,7):q-1,
            (0,0,9):1}

def run(q,full,nrandom=2000):
    F=Field(q); rng=random.Random(723700+q)
    D=Counter();n=0
    choices=product(range(q),repeat=8) if full else [tuple(rng.randrange(q) for _ in range(8)) for j in range(nrandom)]
    for coeff in choices:
        f=[0]*9
        for i,c in enumerate(coeff):f[i+1]=c
        got=type_from_ranks(f,F);pred=expected(f,F)
        assert got==pred,(q,coeff,got,pred)
        D[got]+=1;n+=1
    if full:
        assert D==expected_counts(q),(D,expected_counts(q))
        # The two nonidentity elements of each order-three subgroup of 1+J
        # have the same Jordan type. Check the involution f -> 2f+f^2.
        subgroup_reps=set()
        for coeff in product(range(q),repeat=8):
            if coeff==(0,)*8:continue
            f=[0]+list(coeff)
            ff=mult(f,f,F)
            other=tuple(F.add(F.mul(2, f[i]),ff[i]) for i in range(1,9))
            assert other!=coeff
            assert expected([0]+list(other),F)==expected(f,F)
            subgroup_reps.add(min(coeff,other))
        assert len(subgroup_reps)==(q**8-1)//2
        print('  order-three subgroups of normalized units:',len(subgroup_reps))
    if q==9:
        # Exhaust every quadratic leading form over the extension field and
        # vary the higher terms; also test all cubic leading vectors.
        tested=0
        for a,b,c in product(range(q),repeat=3):
            for j in range(3):
                f=[0]*9
                f[IDX[2,0]],f[IDX[1,1]],f[IDX[0,2]]=a,b,c
                f[IDX[2,1]]=rng.randrange(q)
                f[IDX[1,2]]=rng.randrange(q)
                f[IDX[2,2]]=rng.randrange(q)
                assert type_from_ranks(f,F)==expected(f,F)
                tested+=1
        for d,e,g in product(range(q),repeat=3):
            f=[0]*9
            f[IDX[2,1]],f[IDX[1,2]],f[IDX[2,2]]=d,e,g
            assert type_from_ranks(f,F)==expected(f,F)
            tested+=1
        assert tested==3*q**3+q**3
        print('  targeted extension-field checks:',tested,'(all quadratic and cubic leading data)')
    # count discriminant zero directly, independent of Jordan spectrum
    quad=0
    for a,b,c in product(range(q),repeat=3):
        if F.sub(F.mul(b,b),F.mul(a,c))==0:quad+=1
    assert quad==q*q,(q,quad)
    print(f'FIELD F_{q}: checked {n} augmentation elements; expected Jordan partitions matched; quadratic discriminant zeros {quad}/{q**3}; '+('complete census matched' if full else 'sample only'))
    for part,cnt in sorted(D.items(),reverse=True):print('  partition multiplicity (3-blocks,2-blocks,1-blocks):',part,'count',cnt)

if __name__=='__main__':
    run(3,True)
    run(9,False,1800)
    print('MODULAR_C3xC3_MULTIPLICATION_JORDAN_OK')
