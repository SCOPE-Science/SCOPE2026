#!/usr/bin/env python3
"""Independent finite-field checks of a modular Zinbiel multiplication census.

Usage: python zinbiel_joint_census_check.py
Only the Python standard library is required.
"""
from collections import Counter
from itertools import product
from math import comb
import random


class FiniteField:
    def __init__(self, p, degree=1, modulus=None):
        self.p, self.e, self.q = p, degree, p**degree
        self.modulus = modulus or [0, 1]
        if degree > 1:
            assert len(self.modulus) == degree + 1 and self.modulus[-1] == 1
        self.add = [[0]*self.q for _ in range(self.q)]
        self.neg = [0]*self.q
        self.mul = [[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            ac = self.digits(a)
            self.neg[a] = self.encode([(-v)%p for v in ac])
            for b in range(self.q):
                bc = self.digits(b)
                self.add[a][b] = self.encode([(x+y)%p for x,y in zip(ac,bc)])
                prod = [0]*(2*degree-1)
                for i,x in enumerate(ac):
                    for j,y in enumerate(bc): prod[i+j] = (prod[i+j]+x*y)%p
                for k in range(2*degree-2, degree-1, -1):
                    lead = prod[k]
                    if lead:
                        for i in range(degree): prod[k-degree+i]=(prod[k-degree+i]-lead*self.modulus[i])%p
                self.mul[a][b] = self.encode(prod[:degree])
        self.inverse=[0]*self.q
        for a in range(1,self.q):
            hits=[b for b in range(1,self.q) if self.mul[a][b]==1]
            assert len(hits)==1, ('not a field',self.p,self.e,self.modulus,a)
            self.inverse[a]=hits[0]
        self.one = 1

    def digits(self,a):
        out=[]
        for i in range(self.e):out.append(a%self.p);a//=self.p
        return out

    def encode(self,cs):return sum((int(v)%self.p)*self.p**i for i,v in enumerate(cs))
    def addv(self,a,b):return self.add[a][b]
    def mulv(self,a,b):return self.mul[a][b]


def matrix_rank(M,F):
    A=[row[:] for row in M]
    n=len(A); r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        factor=F.inverse[A[r][j]]
        A[r]=[F.mulv(factor,v) for v in A[r]]
        for i in range(r+1,n):
            h=A[i][j]
            if h:
                minus=F.neg[h]
                A[i]=[F.addv(x,F.mulv(minus,y)) for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r


def matrix_product(A,B,F):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    if B[k][j]:C[i][j]=F.addv(C[i][j],F.mulv(A[i][k],B[k][j]))
    return C


def power_ranks(A,F):
    n=len(A); powers=[]; prod=[row[:] for row in A]
    for k in range(1,n+1):
        powers.append(matrix_rank(prod,F))
        prod=matrix_product(prod,A,F)
    assert powers[-1]==0
    return tuple(powers)


def multiplication_matrix(coeff,F,hand):
    n=len(coeff)
    M=[[0]*n for _ in range(n)]
    for i,a in enumerate(coeff,1):
        if not a:continue
        for j in range(1,n+1-i):
            scalar=comb(i+j-1,j if hand=='left' else i)%F.p
            if scalar:
                M[i+j-1][j-1]=F.addv(M[i+j-1][j-1], F.mulv(a,scalar))
    return M


def predicted_rank_sequence(p,d,hand,n):
    if d==n:return tuple([0]*n)
    if n<=p:return tuple(max(n-k*d,0) for k in range(1,n+1))
    if hand=='left':
        if d==1:return tuple(max(n-k,0) for k in range(1,n+1))
        return tuple(max(p-k*d,0) for k in range(1,n+1))
    if d==p:return (1,)+tuple([0]*(n-1))
    return tuple(max(p-k*d,0) for k in range(1,n+1))


def verify(p,degree,modulus=None,n=None,max_vectors=None,seed=20261028):
    F=FiniteField(p,degree,modulus);n=n or p+1
    assert 2<=n<=p+1
    for i,j,k in product(range(1,n+1),repeat=3):
        if i+j+k>n:continue
        lhs=comb(i+j-1,j)*comb(i+j+k-1,k)
        rhs=(comb(j+k-1,k)+comb(j+k-1,j))*comb(i+j+k-1,j+k)
        assert lhs==rhs,('Zinbiel identity coefficient',i,j,k)
    if max_vectors is None or F.q**n <= max_vectors:
        vectors=product(range(F.q),repeat=n)
        expected_total=F.q**n
        mode='exhaustive'
    else:
        rng=random.Random(seed+p*100+F.q)
        vectors=(tuple(rng.randrange(F.q) for _ in range(n)) for j in range(max_vectors))
        expected_total=max_vectors
        mode='sample'
    counts=Counter(); seen=0
    for coeff in vectors:
        d=next((i for i,a in enumerate(coeff,1) if a!=0),n)
        lr=power_ranks(multiplication_matrix(coeff,F,'left'),F)
        rr=power_ranks(multiplication_matrix(coeff,F,'right'),F)
        assert lr==predicted_rank_sequence(p,d,'left',n),(p,F.q,coeff,'left',lr,predicted_rank_sequence(p,d,'left',n))
        assert rr==predicted_rank_sequence(p,d,'right',n),(p,F.q,coeff,'right',rr,predicted_rank_sequence(p,d,'right',n))
        counts[(lr[0],rr[0])]+=1;seen+=1
    assert seen==expected_total
    if mode=='exhaustive':
        if n<=p:
            want={(0,0):F.q}
            for r in range(1,n):want[(r,r)]=(F.q-1)*F.q**r
        else:
            want={(p,p-1):(F.q-1)*F.q**p,(0,1):(F.q-1)*F.q,(0,0):F.q}
            for r in range(1,p-1):want[(r,r)]=(F.q-1)*F.q**(r+1)
        assert counts==Counter(want),(p,F.q,counts,want)
    return f'p={p}, q={F.q}, n={n}, {mode}={seen}, joint_ranks={sorted(counts.items())}'


def main():
    tests=[
        (2,1,None,2,None),
        (2,1,None,3,None),
        (2,2,[1,1,1],2,None),
        (2,2,[1,1,1],3,None),
        (2,3,[1,1,0,1],3,None),
        (3,1,None,3,None),
        (3,1,None,4,None),
        (3,2,[1,0,1],3,None),
        (3,2,[1,0,1],4,None),
        (5,1,None,5,None),
        (5,1,None,6,None),
        (7,1,None,7,2500),
        (7,1,None,8,2500),
        (11,1,None,12,2500),
    ]
    for t in tests:print(verify(*t))
    print('ZINBIEL_FIRST_MODULAR_JOINT_JORDAN_OK',len(tests))

if __name__=='__main__':main()
