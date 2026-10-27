#!/usr/bin/env python3
"""Exhaustive multiplication and rank checks for three-generator quantum exterior algebras.

The program independently multiplies PBW basis monomials, tests square-zero
conditions, and computes left-multiplication ranks by field Gaussian elimination.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, order):
        self.order = order
        self.ext4 = order == 4
        assert self.ext4 or order in (2, 3, 5)
    def add(self, a, b):
        return a ^ b if self.ext4 else (a+b) % self.order
    def sub(self, a, b):
        return a ^ b if self.ext4 else (a-b) % self.order
    def mul(self, a, b):
        if not self.ext4:
            return a*b % self.order
        v = 0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):
                    v ^= 1<<(i+j)
        if v&8: v ^= 0b1110  # t^3 = t*(t+1) = 1 for t^2+t+1=0.
        if v&4: v ^= 0b111  # t^2=t+1.
        return v
    def pow(self, a, n):
        v = 1
        for _ in range(n): v=self.mul(v,a)
        return v
    def inv(self, a):
        assert a
        return next(b for b in range(1,self.order) if self.mul(a,b)==1)

def basis_products(F,t):
    factors=[]
    for i in range(8):
        row=[]
        for j in range(8):
            if i&j: row.append((0,0)); continue
            inversions=sum((i>>r)&1 and (j>>s)&1 for r in range(3) for s in range(r))
            row.append((i|j,F.pow(t,inversions)))
        factors.append(row)
    return factors

def multiply(F, prod, u, v):
    out=[0]*8
    for i,ai in enumerate(u):
        if not ai: continue
        for j,bj in enumerate(v):
            if not bj: continue
            mask,k=prod[i][j]
            if k:
                out[mask] = F.add(out[mask], F.mul(F.mul(ai,bj),k))
    return out

def rank(F,M):
    a=[row[:] for row in M]
    pivot=0
    for j in range(len(a[0])):
        row=next((i for i in range(pivot,len(a)) if a[i][j]),None)
        if row is None: continue
        a[pivot],a[row]=a[row],a[pivot]
        v=F.inv(a[pivot][j])
        a[pivot]=[F.mul(x,v) for x in a[pivot]]
        for i in range(pivot+1,len(a)):
            m=a[i][j]
            if m: a[i]=[F.sub(x,F.mul(m,y)) for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot

def formula(F,t):
    Q=F.order
    if F.add(1,t)==0:
        if F.add(1,1)==0: return Q**7,1,7
        return Q**6+Q**4-Q**3,1,6
    if F.add(1,1)==0:
        return Q**5+2*Q**4-2*Q**3,3,5
    if F.add(1,F.mul(t,t))==0:
        return 2*Q**5-Q**3,3,5
    return 4*Q**4-3*Q**3,4,4

def check(Q,t):
    F=Field(Q)
    prod=basis_products(F,t)
    hist=Counter()
    for a,b,c,d,e,f,g in product(range(Q),repeat=7):
        u=[0,a,b,d,c,e,f,g]
        if any(multiply(F,prod,u,u)):
            continue
        cols=[]
        for j in range(8):
            basis=[0]*8; basis[j]=1
            cols.append(multiply(F,prod,u,basis))
        lr=rank(F,[[col[i] for col in cols] for i in range(8)])
        expected=(4 if a or b or c else 2 if d or e or f else 1 if g else 0)
        assert lr==expected,(Q,t,u,lr,expected)
        hist[lr]+=1
    expected_total,components,dimension=formula(F,t)
    expected_hist={0:1,1:Q-1,2:Q**4-Q,4:expected_total-Q**4}
    assert dict(hist)=={r:v for r,v in expected_hist.items() if v},(Q,t,hist,expected_hist)
    print('PASS Q=%s t=%s components=%s dimension=%s total=%s rank_counts=%s' % (Q,t,components,dimension,expected_total,dict(sorted(hist.items()))))

if __name__=='__main__':
    total=0
    for Q in (2,3,4,5):
        for t in range(1,Q):
            check(Q,t);total+=1
    print('QUANTUM_EXTERIOR_SQUARE_ZERO_OK',total,'exhaustive field-parameter cases')
