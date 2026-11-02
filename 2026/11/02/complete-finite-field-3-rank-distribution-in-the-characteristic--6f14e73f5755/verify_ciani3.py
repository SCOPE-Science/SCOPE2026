#!/usr/bin/env python3
"""Reproducible exact finite-field checks for characteristic-three Ciani quartics.
Proof of all-extension formulas rests on the discriminant character sum,
not on extrapolation from the displayed field enumerations.
"""
from itertools import product

class FiniteField:
    def __init__(self,n,poly):
        self.n=n;self.poly=poly;self.q=3**n
        self.digits=[tuple((x//3**i)%3 for i in range(n)) for x in range(self.q)]
        self.index={v:i for i,v in enumerate(self.digits)}
        self.add=[[self.index[tuple((u[i]+v[i])%3 for i in range(n))] for v in self.digits] for u in self.digits]
        self.mul=[[self._mult(u,v) for v in self.digits] for u in self.digits]
        self.neg=[self.index[tuple(-x%3 for x in u)] for u in self.digits]
        self.one=1
    def _mult(self,u,v):
        a=[0]*(2*self.n-1)
        for i in range(self.n):
            for j in range(self.n):a[i+j]=(a[i+j]+u[i]*v[j])%3
        for k in range(2*self.n-2,self.n-1,-1):
            c=a[k]
            for j in range(self.n):a[k-self.n+j]=(a[k-self.n+j]-c*self.poly[j])%3
            a[k]=0
        return self.index[tuple(a[:self.n])]
    def plus(self,*xs):
        a=0
        for x in xs:a=self.add[a][x]
        return a
    def minus(self,x,y):return self.add[x][self.neg[y]]
    def prod(self,*xs):
        a=1
        for x in xs:a=self.mul[a][x]
        return a
    def sq(self,x):return self.mul[x][x]

for n,poly in [(1,[0]),(2,[1,0]),(3,[2,2,0])]:
    # irreducible polynomials: t (n=1 dummy), t^2+1, t^3-t-1.
    f=FiniteField(n,poly);q=f.q
    rcounts=[0]*4;Nsmooth=0;singular=0
    for a,b,c in product(range(q),repeat=3):
        A=f.sq(a);B=f.sq(b);C=f.sq(c)
        p=f.minus(f.plus(A,B,C),f.plus(f.prod(a,b,c),1))
        factors=[f.minus(A,1),f.minus(B,1),f.minus(C,1),p]
        smooth=all(x!=0 for x in factors)
        if not smooth:singular+=1;continue
        Nsmooth+=1
        D=(f.plus(f.prod(a,b),c)==0,
           f.plus(f.prod(a,c),b)==0,
           f.plus(f.prod(b,c),a)==0)
        r=sum(D)
        rcounts[r]+=1
    expected=[(q-3)*(q*q-7*q+18),3*(q-3)*(q-5),3*(q-3),1]
    assert rcounts==expected,(q,rcounts,expected)
    assert Nsmooth==(q-2)**3-(q-3)**2
    assert sum(rcounts)==Nsmooth
    print('FIELD',q,'SMOOTH_PARAMETERS',Nsmooth,'BY_SUPERSINGULAR_ELLIPTIC_QUOTIENTS',rcounts)
    if q==3:assert rcounts==[0,0,0,1]
print('SMOOTH_DISCRIMINANT_FACTORS_AND_HASSE_DIVISORS: SYMBOLIC_PROOF_IN_RESULT')
print('VERIFY_OK')
