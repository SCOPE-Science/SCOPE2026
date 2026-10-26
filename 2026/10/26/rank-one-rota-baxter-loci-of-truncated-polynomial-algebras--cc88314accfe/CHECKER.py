#!/usr/bin/env python3
"""Independent finite-field basis-identity tests for rank-one Rota--Baxter maps.
Run with python3 CHECKER.py. No external packages.
"""
from itertools import product

class Field:
    def __init__(self,q):
        self.q=q
        if q not in (2,3,4): raise ValueError('test field')
    def add(self,a,b): return (a^b) if self.q==4 else ((a+b)%self.q)
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        p=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: p ^= 1 << (i+j)
        if p & 8: raise AssertionError('degree exceeded')
        if p & 4: p ^= 7   # x^2=x+1 over GF(4)
        return p
    def inv(self,a):
        if a==0: raise ZeroDivisionError
        return next(z for z in range(1,self.q) if self.mul(a,z)==1)
    def sum(self,terms):
        res=0
        for t in terms: res=self.add(res,t)
        return res

def mul_poly(a,b,F):
    n=len(a); out=[0]*n
    for i,ai in enumerate(a):
        for j,bj in enumerate(b[:n-i]):
            out[i+j]=F.add(out[i+j],F.mul(ai,bj))
    return out

def identity_holds_for_rank_one(a,phi,F):
    n=len(a)
    aa=mul_poly(a,a,F)
    at=[([0]*i+list(a[:n-i])) for i in range(n)]
    phi_at=[F.sum(F.mul(phi[j],at[i][j]) for j in range(n)) for i in range(n)]
    for i in range(n):
        for j in range(n):
            lhs=F.mul(phi[i],phi[j]); rhs=F.add(F.mul(phi[i],phi_at[j]),F.mul(phi[j],phi_at[i]))
            if any(F.mul(lhs,aa[k]) != F.mul(rhs,a[k]) for k in range(n)):
                return False
    return True

def test_case(q,n):
    F=Field(q)
    zero=(0,)*n
    ones=0; expected=0; fail=0; tested=0; valuation_counts={}
    for a0 in product(range(q),repeat=n):
        if a0==zero: continue
        v=next(i for i,x in enumerate(a0) if x)
        c=F.inv(a0[v]); a=tuple(F.mul(c,z) for z in a0)
        if a != a0: continue  # canonical generator of each image line
        for phi in product(range(q),repeat=n):
            if phi==zero: continue
            tested+=1
            actual=identity_holds_for_rank_one(a,phi,F)
            predicted=(v >= (n+1)//2 and all(phi[j]==0 for j in range(v,n)))
            if actual!=predicted: fail+=1
            if actual:
                ones+=1
                valuation_counts[v]=valuation_counts.get(v,0)+1
            if predicted: expected+=1
    h=n//2
    target=h*q**(n-1)-sum(q**j for j in range(h))
    assert fail==0 and ones==expected==target,(q,n,ones,expected,target,fail)
    for v in range((n+1)//2,n):
        assert valuation_counts.get(v,0)==q**(n-v-1)*(q**v-1)
    return q,n,tested,ones,valuation_counts

if __name__=='__main__':
    cases=[(2,n) for n in range(2,8)] + [(3,n) for n in range(2,6)] + [(4,n) for n in range(2,5)]
    for q,n in cases:
        print('q=%s n=%s tested=%s rank1=%s by_valuation=%s'%test_case(q,n),flush=True)
    print('RANK_ONE_ROTA_BAXTER_IDENTITY_OK',len(cases),'cases')
