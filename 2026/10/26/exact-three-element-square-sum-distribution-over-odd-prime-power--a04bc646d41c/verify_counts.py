"""Exact arithmetic cross-check of 3-distinct-square subset-sum formulas."""
from itertools import combinations
from functools import lru_cache
from math import comb

def legendre(t, p):
    v = t % p
    return 0 if v == 0 else (1 if pow(v, (p - 1)//2, p) == 1 else -1)

@lru_cache(None)
def ternary(p, a, b):
    if a == 0:
        return 1
    b %= p**a
    if a == 1:
        return p*p + (p*legendre(-b,p) if b else 0)
    if b % p:
        return p**(2*a-2) * (p*p + p*legendre(-b,p))
    return p**(2*a-2)*(p*p-1) + (p**3*ternary(p,a-2,b//(p*p)) if b % (p*p) == 0 else 0)

@lru_cache(None)
def binary(p, a, b):
    if a == 0:
        return 1
    b %= p**a
    eps = legendre(-2,p)
    if a == 1:
        return p-eps if b else p+(p-1)*eps
    if b % p:
        return p**(a-1)*(p-eps)
    return p**(a-1)*(p-1)*(1+eps) + (p*p*binary(p,a-2,b//(p*p)) if b % (p*p) == 0 else 0)

def square_roots(p, a, b):
    if a == 0:
        return 1
    b %= p**a
    if b == 0:
        return p**(a//2)
    v=0
    while b % p == 0:
        v += 1
        b //= p
    return 0 if v % 2 else p**(v//2)*(1+legendre(b,p))

def diagonal(p,a,b):
    q=p**a
    b%=q
    if p==3:
        if b%3:
            return 0
        return 3*square_roots(3,a-1,b//3)
    if b==0:
        return p**(a//2)
    v=0
    while b % p == 0:
        v+=1
        b//=p
    return 0 if v%2 else p**(v//2)*(1+legendre(3*b,p))

def count(p,a,b):
    z = ternary(p,a,b)-3*binary(p,a,b)+2*diagonal(p,a,b)
    assert z%6==0 and z>=0, (p,a,b,z)
    return z//6

if __name__=='__main__':
    for p,a in [(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(7,1),(7,2),(11,1),(11,2),(13,1),(13,2)]:
        q=p**a
        measured=[0]*q
        for xs in combinations(range(q),3):
            measured[sum(x*x for x in xs)%q]+=1
        expected=[count(p,a,b) for b in range(q)]
        assert measured==expected,(p,a,[(b,measured[b],expected[b]) for b in range(q) if measured[b]!=expected[b]][:10])
        assert sum(expected)==comb(q,3)
        assert all(c>0 for c in expected)==(p>=5 or a>=2)
        if p>=5:
            for b in range(1,q):
                if b%p:
                    expected6=(q*q-3*q+2+3*(q//p)*legendre(-2,p)+(q*q//p)*legendre(-b,p)+2*legendre(3*b,p))
                    assert 6*count(p,a,b)==expected6,(p,a,b)
        print('CHECK',p,a,'minimum',min(expected),'maximum',max(expected))
    print('VERIFY_OK')
