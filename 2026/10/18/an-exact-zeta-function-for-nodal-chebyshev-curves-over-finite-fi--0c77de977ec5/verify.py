#!/usr/bin/env python3
"""Finite-field spot checks of an affine Chebyshev-curve point-count identity.

Self-contained; checks are finite tests and do not constitute the all-field proof.
"""
from math import gcd


def residue_sign(q, k):
    r = q % (2*k)
    if r == 1:
        return 1
    if r == (2*k)-1:
        return -1
    return None


def cheb_int(k, x, mod):
    t0, t1 = 1, x % mod
    if k == 0:
        return 1
    if k == 1:
        return t1
    for _ in range(2, k+1):
        t0, t1 = t1, (2*x*t1-t0) % mod
    return t1


def count_prime(p, n, m):
    return sum(cheb_int(n, x, p) == cheb_int(m, y, p)
               for x in range(p) for y in range(p))


def fp2_mul(a, b, p, d):
    return ((a[0]*b[0]+d*a[1]*b[1])%p,
            (a[0]*b[1]+a[1]*b[0])%p)


def fp2_cheb(k, x, p, d):
    zero=(0,0); one=(1,0)
    if k == 0: return one
    if k == 1: return x
    a,b=one,x
    for _ in range(2,k+1):
        c=fp2_mul((2,0),fp2_mul(x,b,p,d),p,d)
        a,b=b,((c[0]-a[0])%p,(c[1]-a[1])%p)
    return b


def count_quadratic(p,n,m):
    d=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    els=[(i,j) for i in range(p) for j in range(p)]
    f=[fp2_cheb(n,x,p,d) for x in els]
    g=[fp2_cheb(m,y,p,d) for y in els]
    counts={}
    for a in g: counts[a]=counts.get(a,0)+1
    return sum(counts.get(a,0) for a in f)


def test():
    primes=[5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127]
    pairs=[(3,2),(4,3),(5,3),(5,4),(7,4),(7,6),(9,2),(9,4)]
    cnt=0
    for n,m in pairs:
        assert gcd(m,n)==1
        delta=(m-1)*(n-1)//2
        for p in primes:
            e_n,e_m=residue_sign(p,n),residue_sign(p,m)
            if e_n is None or e_m is None: continue
            got=count_prime(p,n,m)
            expected=p-delta*e_n*e_m
            assert got==expected,(p,n,m,got,expected)
            cnt+=1
    ext=0
    for p in [5,7,11,13]:
        for n,m in [(3,2),(4,3),(5,3),(5,4)]:
            en,em=residue_sign(p,n),residue_sign(p,m)
            if en is None or em is None: continue
            got=count_quadratic(p,n,m)
            expected=p*p-(m-1)*(n-1)//2
            assert got==expected,(p,n,m,got,expected)
            ext+=1
    for n,m in [(5,2),(5,4)]:
        q=9
        en,em=residue_sign(q,n),residue_sign(q,m)
        assert en is not None and em is not None
        got=count_quadratic(3,n,m)
        expected=q-(n-1)*(m-1)//2*en*em
        assert got==expected,(q,n,m,got,expected)
        ext+=1
    print('PASS:',cnt,'prime-field tests and',ext,'quadratic-field tests')
    print('Example p=5, n=3, m=2:',count_prime(5,3,2),'and F25:',count_quadratic(5,3,2))

if __name__=='__main__':test()
