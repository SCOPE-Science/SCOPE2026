#!/usr/bin/env python3
"""Independent exhaustive checks for square-zero image-shape counts over short chain rings."""
from collections import Counter
from itertools import product
from math import prod

class Ring:
    def __init__(self, q, kind):
        assert q in (2, 3, 4)
        assert kind == 'dual' or (kind == 'z' and q in (2, 3))
        self.q, self.kind, self.order = q, kind, q*q

    def fa(self, x, y):
        return (x ^ y) if self.q in (2,4) else (x+y)%self.q

    def fm(self, x, y):
        if self.q != 4:
            return x*y%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (x>>i)&1 and (y>>j)&1:
                    z ^= 1<<(i+j)
        if z & 4:
            z ^= 7  # x^2 = x+1 in F4
        return z

    def red(self, x):
        return x%self.q

    def add(self, x, y):
        if self.kind == 'z': return (x+y)%self.order
        return self.fa(x%self.q, y%self.q) + self.q*self.fa(x//self.q, y//self.q)

    def mul(self, x, y):
        if self.kind == 'z': return (x*y)%self.order
        a,b=x%self.q,x//self.q
        c,d=y%self.q,y//self.q
        return self.fm(a,c)+self.q*self.fa(self.fm(a,d),self.fm(b,c))


def field_rank(values, n, ring):
    mat=[[ring.red(values[i*n+j]) for j in range(n)] for i in range(n)]
    rank=0
    for j in range(n):
        k=next((i for i in range(rank,n) if mat[i][j]),None)
        if k is None: continue
        mat[rank],mat[k]=mat[k],mat[rank]
        a=mat[rank][j]
        inv=next(x for x in range(1,ring.q) if ring.fm(a,x)==1)
        mat[rank]=[ring.fm(inv,v) for v in mat[rank]]
        for i in range(n):
            if i==rank or not mat[i][j]: continue
            c=mat[i][j]
            # subtraction equals addition over characteristics two
            if ring.q == 3: neg=lambda x:(-x)%3
            else: neg=lambda x:x
            mat[i]=[ring.fa(mat[i][z],neg(ring.fm(c,mat[rank][z]))) for z in range(n)]
        rank+=1
    return rank


def square_zero(a,n,R):
    for i in range(n):
        for j in range(n):
            val=0
            for k in range(n): val=R.add(val,R.mul(a[i*n+k],a[k*n+j]))
            if val: return False
    return True


def image_cardinality(a,n,R):
    out=set()
    for v in product(range(R.order),repeat=n):
        out.add(tuple(_dot(a,i,n,v,R) for i in range(n)))
    return len(out)


def _dot(a,i,n,v,R):
    z=0
    for j in range(n): z=R.add(z,R.mul(a[i*n+j],v[j]))
    return z


def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**n-q**i for i in range(k))
    den=prod(q**k-q**i for i in range(k))
    return num//den


def rankcount(s,t,q):
    return gaussian(s,t,q)*prod(q**s-q**i for i in range(t))


def gl(r,q):
    return prod(q**r-q**i for i in range(r))


def predicted(n,q):
    C=Counter()
    for r in range(n//2+1):
        s=n-2*r
        base=gaussian(n,r,q)*gaussian(n-r,r,q)*gl(r,q)*q**(2*r*(n-r))
        for t in range(s+1):C[(r,t)]=base*rankcount(s,t,q)
    return +C


def verify_case(n,R):
    actual=Counter()
    for a in product(range(R.order), repeat=n*n):
        if not square_zero(a,n,R):continue
        r=field_rank(a,n,R)
        card=image_cardinality(a,n,R)
        t=0
        while R.q**(2*r+t)<card:t+=1
        assert R.q**(2*r+t)==card,(n,R.q,R.kind,a,r,card)
        assert t<=n-2*r
        actual[(r,t)]+=1
    expected=predicted(n,R.q)
    assert actual == expected, (n,R.q,R.kind,actual,expected)
    print(f'CHECK_OK n={n} q={R.q} ring={R.kind} total={sum(actual.values())} shapes={sorted(actual.items())}')
    return sum(actual.values())


def main():
    cases=[(1,2,'z'),(1,2,'dual'),(2,2,'z'),(2,2,'dual'),(3,2,'z'),(3,2,'dual'),(2,3,'z'),(2,3,'dual'),(2,4,'dual')]
    for n,q,kind in cases:verify_case(n,Ring(q,kind))
    print('VERIFY_OK_SQUARE_ZERO_CHAIN2_SHAPE')

if __name__=='__main__':main()
