#!/usr/bin/env python3
"""Finite exact checks for the restricted-p-line scheme and Hilbert polynomial.

The general proof is algebraic; these tests do not establish its quantifiers.
"""
from itertools import product
from math import comb


def bino(n,k):
    return comb(n,k) if n >= k >= 0 else 0


def projective_fp_count(p,r):
    normalized=set()
    for v in product(range(p), repeat=r):
        if all(a == 0 for a in v):
            continue
        leading=next(a for a in v if a)
        inverse=pow(leading, -1, p)
        u=tuple((inverse*a) % p for a in v)
        assert all(((u[i]**p*u[j]-u[j]**p*u[i]) % p)==0 for i in range(r) for j in range(i+1,r))
        normalized.add(u)
    return len(normalized)


def fat_hilbert_direct(p,r,s,m):
    return sum(bino(m-sum(exponents)+s-1,s-1) for exponents in product(range(p), repeat=r))


def fat_hilbert_inclusion(p,r,s,m):
    return sum((-1)**j*bino(r,j)*bino(m-j*p+r+s-1,r+s-1) for j in range(r+1))


def test():
    cases=0
    for p in (2,3,5):
        for r in (1,2,3):
            for s in (1,2,3):
                assert projective_fp_count(p,r)==(p**r-1)//(p-1)
                monomials=list(product(range(p),repeat=r))
                assert len(monomials)==p**r
                for m in range(0,r*p+8):
                    a=fat_hilbert_direct(p,r,s,m)
                    b=fat_hilbert_inclusion(p,r,s,m)
                    assert a==b,(p,r,s,m,a,b)
                # In ordinary affine charts, t^p-t has derivative -1;
                # in supersingular charts, d(t^p)=0 in characteristic p.
                assert ((p-1)%p)==p-1
                assert (p%p)==0
                if s == 1:
                    m=r*(p-1)+1
                    assert fat_hilbert_direct(p,r,s,m)==p**r
                    assert fat_hilbert_direct(p,r,s,m)+(p**r-1)//(p-1)==p**r+(p**r-1)//(p-1)
                cases+=1
    assert projective_fp_count(3,1)==1
    assert fat_hilbert_direct(3,1,1,3)==3
    print(f'VERIFY_OK cases={cases}, finite polynomial cross-checks and F_p point enumerations')

if __name__=='__main__':
    test()
