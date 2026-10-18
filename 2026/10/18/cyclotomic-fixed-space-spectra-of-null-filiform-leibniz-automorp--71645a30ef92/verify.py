#!/usr/bin/env python3
"""Independent finite-field checks of null-filiform Leibniz automorphism fixed-space frequencies."""
from itertools import product
from collections import Counter
from math import gcd

class Field:
    # Polynomials store base-p digits; irreducible reduction polynomial lists are low-to-high.
    specifications = {2:(2,[0,1]),3:(3,[0,1]),4:(2,[1,1,1]),5:(5,[0,1]),7:(7,[0,1]),8:(2,[1,1,0,1]),9:(3,[1,0,1]),11:(11,[0,1])}
    def __init__(self,q):
        self.q=q;self.p,self.mod=self.specifications[q]; p=self.p
        f=0;u=q
        while u>1:
            assert u%p==0
            u//=p;f+=1
        self.f=f
        def digits(k):
            v=[]
            for _ in range(f):v.append(k%p); k//=p
            return v
        self.digits=[digits(a) for a in range(q)]
        self.add=[[sum(((self.digits[a][j]+self.digits[b][j])%p)*p**j for j in range(f)) for b in range(q)] for a in range(q)]
        self.neg=[sum((-self.digits[a][j]%p)*p**j for j in range(f)) for a in range(q)]
        self.mul=[]
        for a in range(q):
            row=[]
            for b in range(q):
                prod=[0]*(2*f-1)
                for i,x in enumerate(self.digits[a]):
                    for j,y in enumerate(self.digits[b]):prod[i+j]=(prod[i+j]+x*y)%p
                if f>1:
                    for d in range(2*f-2,f-1,-1):
                        z=prod[d]
                        if z:
                            for j in range(f):prod[d-f+j]=(prod[d-f+j]-z*self.mod[j])%p
                row.append(sum(prod[j]*p**j for j in range(f)))
            self.mul.append(row)
        self.inv=[0]*q
        for a in range(1,q):
            hits=[b for b in range(1,q) if self.mul[a][b]==1]
            assert len(hits)==1,(q,a,hits)
            self.inv[a]=hits[0]
    def order(self,a):
        v=1
        for l in range(1,self.q):
            v=self.mul[v][a]
            if v==1:return l
        raise AssertionError


def rank(matrix,F):
    p=[row[:] for row in matrix]; n=len(p); r=0
    for c in range(n):
        i=next((i for i in range(r,n) if p[i][c]),None)
        if i is None:continue
        p[r],p[i]=p[i],p[r];factor=F.inv[p[r][c]]
        for j in range(c,n):p[r][j]=F.mul[p[r][j]][factor]
        for i in range(r+1,n):
            if p[i][c]:
                factor=p[i][c]
                for j in range(c,n):p[i][j]=F.add[p[i][j]][F.neg[F.mul[factor][p[r][j]]]]
        r+=1
    return r


def count_direct(q,n):
    F=Field(q);counts=Counter()
    for a in range(1,q):
        for bs in product(range(q),repeat=n-1):
            b=(a,)+bs
            M=[[0]*n for _ in range(n)]
            for j in range(n):
                aj=1
                for _ in range(j):aj=F.mul[aj][a]
                for i in range(j,n):
                    M[i][j]=F.mul[aj][b[i-j]]
            for i in range(n):M[i][i]=F.add[M[i][i]][F.neg[1]]
            k=n-rank(M,F)
            counts[k]+=1
    return counts


def count_formula(q,n):
    F=Field(q);counts=Counter()
    for a in range(1,q):
        m=n//F.order(a)
        if m==0:counts[0]+=q**(n-1)
        else:
            for k in range(1,m):counts[k]+=(q-1)*q**(n-1-k)
            counts[m]+=q**(n-m)
    return counts


def check_normal_forms(q,n):
    F=Field(q)
    for a in range(1,q):
        ell=F.order(a)
        A=[1]
        for j in range(1,n):A.append(F.mul[A[-1]][a])
        observed=Counter()
        for coeff in product(range(q),repeat=n-1):
            U=[1]+list(coeff)
            W=[1]+[0]*(n-1)
            H=[1]+[0]*(n-1)
            for j in range(1,n):
                left=0;right=0
                for r in range(j+1):
                    left=F.add[left][F.mul[U[r]][F.mul[A[j-r]][W[j-r]]]]
                    right=F.add[right][F.mul[H[r]][W[j-r]]]
                d=F.add[left][F.neg[right]]
                if j%ell==0:H[j]=d
                else:
                    denom=F.add[A[j]][F.neg[1]]
                    W[j]=F.neg[F.mul[d][F.inv[denom]]]
            for j in range(n):
                left=0;right=0
                for r in range(j+1):
                    left=F.add[left][F.mul[U[r]][F.mul[A[j-r]][W[j-r]]]]
                    right=F.add[right][F.mul[H[r]][W[j-r]]]
                assert left==right,(q,n,a,U,W,H,j)
            observed[tuple(H[j] for j in range(ell,n,ell))]+=1
        M=(n-1)//ell
        assert len(observed)==q**M,(q,n,a,len(observed),M)
        assert set(observed.values())=={q**(n-1-M)},(q,n,a,observed)
    print(f'normal_forms q={q} n={n} verified')


def test():
    cases=[(2,2),(2,4),(2,7),(3,3),(3,6),(3,8),(4,3),(4,6),(5,3),(5,6),(7,4),(8,4),(9,4)]
    for q,n in cases:
        measured=count_direct(q,n)
        expected=count_formula(q,n)
        assert measured==expected,(q,n,measured,expected)
        assert sum(measured.values())==(q-1)*q**(n-1)
        orbits=sum(count*q**k for k,count in measured.items())//((q-1)*q**(n-1))
        assert orbits==2+sum(gcd(i,q-1) for i in range(2,n+1)),(q,n,orbits)
        print(f'q={q:2} n={n:2} checked={(q-1)*q**(n-1):6} ranks={sorted(measured.items())} one_tuple_orbits={orbits}')
    for q,n in [(2,6),(3,5),(4,5),(5,4)]:check_normal_forms(q,n)
    print('VERIFY_OK')

if __name__=='__main__':test()
