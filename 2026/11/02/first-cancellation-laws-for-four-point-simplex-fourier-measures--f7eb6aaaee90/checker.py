#!/usr/bin/env python3
"""Exact integer/cyclotomic checks for four-digit simplex Fourier cancellations.

Uses only the Python standard library. Exhaustively checks all frequency classes
at the listed resolutions; it is a finite check, not a proof for arbitrary bases.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def monic_division_exact(f, g):
    f = f[:]
    if not g or g[-1] != 1:
        raise ValueError('monic divisor required')
    out = [0] * max(0, len(f) - len(g) + 1)
    while len(f) >= len(g):
        d = len(f) - len(g)
        c = f[-1]
        out[d] = c
        for i, a in enumerate(g):
            f[i + d] -= c * a
        while f and f[-1] == 0:
            f.pop()
    if f:
        raise ArithmeticError('nonzero remainder')
    return out


def polynomial_remainder(f, g):
    f = f[:]
    while len(f) >= len(g):
        d = len(f) - len(g)
        c = f[-1]
        for i, a in enumerate(g):
            f[i+d] -= c*a
        while f and f[-1] == 0:
            f.pop()
    return f


@lru_cache(None)
def cyclotomic(n):
    if n == 1:
        return (-1, 1)
    q = [-1] + [0] * (n-1) + [1]
    for d in range(1,n):
        if n%d == 0:
            q = monic_division_exact(q,list(cyclotomic(d)))
    return tuple(q)


def residues(n):
    f = cyclotomic(n)
    d = len(f)-1
    a=[]
    for r in range(n):
        p=polynomial_remainder([0]*r+[1], list(f))
        a.append(tuple((p+[0]*d)[:d]))
    return a


def geometric_mask_zero(m,b,j):
    if b%2:
        return False
    n=b**j
    h=n//2
    for i in range(3):
        u,v=[x for x in range(3) if x!=i]
        if m[i]%n==h and (m[u]-m[v])%n==h:
            return True
    return False


def exact_mask_zero(m,n,R):
    return all(1+R[m[0]%n][q]+R[m[1]%n][q]+R[m[2]%n][q] == 0
               if q==0 else
               R[m[0]%n][q]+R[m[1]%n][q]+R[m[2]%n][q] == 0
               for q in range(len(R[0])))


def expected_first(b,j):
    if b%2:
        return Fraction(0)
    return Fraction(3,b-1)*(Fraction(1,b**(3*j))+(b-2)*Fraction(1,b**(2*j)))


def expected_double(b,L):
    if b%2:
        return Fraction(0)
    return sum((Fraction(3,b**(3*j+2))*sum((Fraction(1,b**(2*r))
                    for r in range(L-j)),Fraction(0))
                for j in range(1,L)),Fraction(0))


def run(b,L):
    N=b**L
    R=[None]+[residues(b**j) for j in range(1,L+1)]
    histogram=[0,0,0,0]
    first=[0]*(L+1)
    for m in product(range(N),repeat=3):
        flags=[]
        for j in range(1,L+1):
            n=b**j
            flag=exact_mask_zero(m,n,R[j])
            assert flag == geometric_mask_zero(m,b,j), (b,L,m,j)
            if flag:flags.append(j)
        assert len(flags)<=2,(b,m,flags)
        histogram[len(flags)]+=1
        if flags:first[flags[0]]+=1
    for j in range(1,L+1):
        assert Fraction(first[j],N**3)==expected_first(b,j), (b,L,j,first[j])
    assert Fraction(histogram[2],N**3)==expected_double(b,L)
    assert sum(histogram)==N**3
    return b,L,histogram,first[1:]


if __name__=='__main__':
    for b,L in [(2,4),(3,2),(4,3),(6,2)]:
        print('base,levels,histogram,first counts:',run(b,L))
    print('FOUR_ATOM_SIMPLEX_EXACT_CYCLOTOMIC_OK')
