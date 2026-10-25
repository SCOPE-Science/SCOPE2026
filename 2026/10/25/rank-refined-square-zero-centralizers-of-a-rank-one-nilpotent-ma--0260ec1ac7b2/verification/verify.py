#!/usr/bin/env python3
"""Direct enumeration for a rank-one square-zero centralizer."""
from itertools import product

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a+b) % self.q
    def mul(self, a, b):
        if self.q != 4:
            return (a*b) % self.q
        z = 0
        while b:
            if b&1: z ^= a
            a <<= 1
            if a&4: a ^= 7  # irreducible polynomial t^2+t+1
            b >>= 1
        return z
    def inv(self, a):
        assert a
        return next(v for v in range(1,self.q) if self.mul(a,v)==1)
    def dot(self,x,y):
        z = 0
        for a,b in zip(x,y): z = self.add(z,self.mul(a,b))
        return z

def rank(matrix, f):
    a = [row[:] for row in matrix]
    n, m = len(a),len(a[0]); k=0
    for j in range(m):
        pivot = next((i for i in range(k,n) if a[i][j]),None)
        if pivot is None: continue
        a[k],a[pivot] = a[pivot],a[k]
        inv = f.inv(a[k][j])
        a[k] = [f.mul(v,inv) for v in a[k]]
        for i in range(n):
            if i!=k and a[i][j]:
                scale=a[i][j]
                a[i] = [f.add(v,f.mul(scale,w)) if f.q==4 else (v-f.mul(scale,w))%f.q for v,w in zip(a[i],a[k])]
        k += 1
        if k==n:break
    return k

def gaussian(n,r,q):
    a=b=1
    for j in range(r):
        a *= q**(n-j)-1
        b *= q**(r-j)-1
    return a//b

def theoretical(q,b):
    result = {}
    for r in range(b//2+1):
        s=b-2*r
        gl=1
        for j in range(r): gl *= q**r-q**j
        mult=gaussian(b,r,q)*gaussian(b-r,r,q)*gl
        coeffs=[q**(2*r), q**(2*r)*(q-1+2*q*(q**s-1)),
                q**(2*r+1)*(q**s-1)*(q**(s-1)-1) if s>=1 else 0]
        for delta,count in enumerate(coeffs):
            if count:result[r,r+delta]=count*mult
    return result

def enumerate_census(q,b):
    f=Field(q); counts={}
    for entries in product(range(q),repeat=b*b):
        B=[list(entries[i*b:(i+1)*b]) for i in range(b)]
        if any(f.dot(B[i],[B[j][h] for j in range(b)]) for i in range(b) for h in range(b)):
            continue
        r=rank(B,f)
        for row in product(range(q),repeat=b):
            if any(f.dot(row,[B[i][j] for i in range(b)]) for j in range(b)):
                continue
            for col in product(range(q),repeat=b):
                if any(f.dot(B[i],col) for i in range(b)) or f.dot(row,col):
                    continue
                for scalar in range(q):
                    image=[list(row)+[scalar]]+[B[i]+[col[i]] for i in range(b)]
                    rho=rank(image,f)
                    counts[r,rho]=counts.get((r,rho),0)+1
    wanted=theoretical(q,b)
    assert counts==wanted,(q,b,counts,wanted)
    print('PASS',q,b,'total',sum(counts.values()),'rank_fibers',sorted(counts.items()))

if __name__=='__main__':
    for qb in [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1)]:
        enumerate_census(*qb)
    print('COMMUTING_SQUARE_ZERO_RANK_FIBERS_OK')
