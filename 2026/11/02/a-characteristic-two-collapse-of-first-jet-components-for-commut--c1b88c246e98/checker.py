#!/usr/bin/env python3
"""Direct coefficient-equation verification of commuting square-zero matrices over dual numbers."""
from itertools import product
from math import comb

class Field:
    def __init__(self, q):
        assert q in (2,3,4,5,7)
        self.q=q
    def plus(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def minus(self,a,b):
        return self.plus(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        x=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    x^=(1<<(i+j))
        if x&8:x^=0b1110  # polynomial x^3=x^2+x, never needed for 2-bit inputs
        if x&4:x^=0b111  # x^2=x+1
        return x
    def inv(self,a):
        for x in range(1,self.q):
            if self.mul(x,a)==1:return x
        raise ValueError('zero divisor')
    def matmul(self,a,b):
        p=self.plus; t=self.mul
        return (p(t(a[0],b[0]),t(a[1],b[2])),p(t(a[0],b[1]),t(a[1],b[3])),p(t(a[2],b[0]),t(a[3],b[2])),p(t(a[2],b[1]),t(a[3],b[3])))
    def madd(self,a,b):
        return tuple(self.plus(x,y) for x,y in zip(a,b))
    def msub(self,a,b):
        return tuple(self.minus(x,y) for x,y in zip(a,b))
    def rank(self,rows,n):
        M=[list(row) for row in rows if any(row)]
        r=0
        for j in range(n):
            pivot=next((i for i in range(r,len(M)) if M[i][j]),None)
            if pivot is None:continue
            M[r],M[pivot]=M[pivot],M[r]
            iv=self.inv(M[r][j]); M[r]=[self.mul(x,iv) for x in M[r]]
            for i in range(len(M)):
                if i==r or not M[i][j]:continue
                a=M[i][j]
                M[i]=[self.minus(x,self.mul(a,y)) for x,y in zip(M[i],M[r])]
            r+=1
            if r==len(M):break
        return r

def zeros(F):return tuple(0 for _ in range(4))

def squarezero(F,A):return F.matmul(A,A)==zeros(F)

def commute(F,A,B):return F.matmul(A,B)==F.matmul(B,A)

def fibers_rank(F,As):
    m=len(As); n=4*m
    eq=[[0]*n for _ in range(4*m+4*(m*(m-1)//2))]
    Z=zeros(F)
    E=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    def evaluator(Bs):
        out=[]
        for A,B in zip(As,Bs):out.extend(F.madd(F.matmul(A,B),F.matmul(B,A)))
        for i in range(m):
            for j in range(i+1,m):
                out.extend(F.madd(F.msub(F.matmul(As[i],Bs[j]),F.matmul(Bs[j],As[i])),F.msub(F.matmul(Bs[i],As[j]),F.matmul(As[j],Bs[i]))))
        return out
    for ix in range(n):
        Bs=[Z for _ in range(m)]; Bs[ix//4]=E[ix%4]
        col=evaluator(Bs)
        for row,val in zip(eq,col):row[ix]=val
    return F.q**(n-F.rank(eq,n))

def analytic(q,m):
    if q%2==0:
        return q**(4*m)+(q+1)*(q**m-1)*q**(2*m)
    return q**(4*m)+(q+1)*q**(m+1)*((2*q-1)**m-q**m)

def verify_ranks(q,m):
    F=Field(q)
    M=list(product(range(q),repeat=4))
    sq=[A for A in M if squarezero(F,A)]
    assert len(sq)==q*q,(q,len(sq))
    nonzero=[A for A in sq if A!=zeros(F)]
    reps=[]
    for A in nonzero:
        if all(A!=tuple(F.mul(t,x) for x in N) for N in reps for t in range(1,q)):
            reps.append(A)
    assert len(reps)==q+1
    total=q**(4*m)
    detail=[]
    for N in reps:
        for ts in product(range(q),repeat=m):
            if not any(ts):continue
            As=[tuple(F.mul(t,x) for x in N) for t in ts]
            # independent check all original constant-matrix equations
            assert all(squarezero(F,A) for A in As)
            assert all(commute(F,As[i],As[j]) for i in range(m) for j in range(i+1,m))
            f=fibers_rank(F,As)
            r=sum(t!=0 for t in ts)
            expect=q**(2*m if q%2==0 else 2*m-r+1)
            assert f==expect,(q,m,ts,f,expect)
            total+=f;detail.append((ts,f))
    assert total==analytic(q,m),(q,m,total,analytic(q,m))
    print('RANK_FIBERS_OK',q,m,'base',1+(q+1)*(q**m-1),'total',total)

def verify_brute(q,m):
    F=Field(q); Z=zeros(F)
    # all matrices over ring F[eps]/eps^2, coordinate pair (A,B)
    M=list(product(range(q),repeat=4))
    valid=[]
    for A in M:
        if not squarezero(F,A):continue
        for B in M:
            if F.madd(F.matmul(A,B),F.matmul(B,A))==Z:
                valid.append((A,B))
    assert len(valid)==analytic(q,1),(q,len(valid),analytic(q,1))
    if m==1:
        print('EXHAUSTIVE_RING_OK',q,m,len(valid));return
    # direct two-sided commutation in the actual ring, not using ranks
    total=0
    for A,B in valid:
        for C,D in valid:
            if F.matmul(A,C)!=F.matmul(C,A):continue
            if F.madd(F.matmul(A,D),F.matmul(B,C))!=F.madd(F.matmul(C,B),F.matmul(D,A)):continue
            total+=1
    assert total==analytic(q,2),(q,total,analytic(q,2))
    print('EXHAUSTIVE_RING_OK',q,2,total)

if __name__=='__main__':
    for q,m in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(7,2)]:
        verify_ranks(q,m)
    verify_brute(2,2)
    verify_brute(3,1)
    print('DUAL_JETS_COMMUTING_SQUARE_ZERO_OK 15 RANK_CASES 2 BRUTE_CASES')
