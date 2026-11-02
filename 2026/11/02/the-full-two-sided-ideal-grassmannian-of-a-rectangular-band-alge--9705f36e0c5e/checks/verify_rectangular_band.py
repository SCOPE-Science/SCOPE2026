#!/usr/bin/env python3
"""Direct exhaustive tests of two-sided ideals in finite rectangular-band algebras.
Run with Python 3, no external dependencies. The test enumerates every RREF subspace
and checks closure under the defining multiplication, without using the proposed
classification or the row/column conditions in the membership test.
"""
from itertools import combinations, product
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 or self.q == 2 else (a+b) % self.q
    def neg(self, a):
        return a if self.q in (2, 4) else (-a) % self.q
    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        z = 0
        for i in range(2):
            if (b >> i) & 1:
                z ^= a << i
        if z & 4:
            z ^= 0b111
        return z

def gaussian(n, k, q):
    if k < 0 or k > n: return 0
    a = 1
    b = 1
    for i in range(k):
        a *= q**(n-i)-1
        b *= q**(k-i)-1
    return a//b

def expected(m, n, q):
    out = Counter({m*n:1})
    for u in range(n):
        for v in range(m):
            factor = gaussian(n-1,u,q)*gaussian(m-1,v,q)
            free = (m-1-v)*(n-1-u)
            base = m*u+n*v-u*v
            for w in range(free+1):
                out[base+w] += factor*gaussian(free,w,q)
    return out

def rref_subspaces(N,q):
    for d in range(N+1):
        for piv in combinations(range(N),d):
            pivset = set(piv)
            free = [(i,j) for i,p in enumerate(piv) for j in range(p+1,N) if j not in pivset]
            for digits in product(range(q), repeat=len(free)):
                basis = [[0]*N for i in range(d)]
                for i,p in enumerate(piv): basis[i][p]=1
                for (i,j),v in zip(free,digits): basis[i][j]=v
                yield d, piv, basis

def contains(span_piv, basis, z, f):
    z = z[:]
    for i,p in enumerate(span_piv):
        a = z[p]
        if a:
            for j, b in enumerate(basis[i]):
                z[j] = f.add(z[j], f.neg(f.mul(a,b)))
    return not any(z)

def is_ideal(m,n,piv,basis,f):
    N=m*n
    for x in basis:
        # Original multiplication (i,j)(k,l)=(i,l): every basis element
        # left-multiplication checks every row target; right every column target.
        for a in range(m):
            for b in range(n):
                left=[0]*N
                right=[0]*N
                for k in range(m):
                    for l in range(n):
                        c=x[k*n+l]
                        left[a*n+l] = f.add(left[a*n+l],c)
                        right[k*n+b] = f.add(right[k*n+b],c)
                if not contains(piv,basis,left,f) or not contains(piv,basis,right,f):
                    return False
    return True

def check(m,n,q):
    f=Field(q)
    counted=Counter()
    scanned=0
    for d,piv,basis in rref_subspaces(m*n,q):
        scanned+=1
        if is_ideal(m,n,piv,basis,f): counted[d]+=1
    target=expected(m,n,q)
    if counted!=target:
        raise AssertionError(f'(m,n,q)={(m,n,q)} actual={dict(counted)} predicted={dict(target)}')
    return scanned,dict(sorted(counted.items()))

if __name__=='__main__':
    tests=[(2,2,2),(2,2,3),(2,2,4),(2,3,2),(2,3,3),(3,2,2),(1,4,2)]
    for m,n,q in tests:
        scanned,distr=check(m,n,q)
        print(f'PASS m={m} n={n} q={q} tested_subspaces={scanned} ideals_by_dimension={distr}')
    print(f'RECTANGULAR_BAND_IDEALS_OK {len(tests)} EXHAUSTIVE_CASES')
