#!/usr/bin/env python3
"""Exact rational checks for cubic spherical-harmonic sampling on third hypersimplices.
Only the standard library is required. Analytic arguments for all dimensions are in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def eig(n):
    assert n >= 6
    return (
        F(n*(n-6)**2*(n+1), 18*(n-3)*(n-2)),
        F(n*n*(n*n-17*n+54)**2, 54*(n-3)**3*(n-2)),
        F(2*n*n*(n-6)**2*(n+1), 9*(n-3)**3*(n-2)),
        F(2*n**3*(n+1), 9*(n-3)**3*(n-2)),
    )


def kernel(n, c):
    z = F(n*c-9, 3*(n-3))
    return ((n+1)*z**3-3*z)/(n-2)


def v_r(n, X, r):
    if r == 0:
        return [1]*len(X)
    pairs = [(0,1), (2,3), (4,5)][:r]
    pattern = []
    for bits in product((0,1), repeat=r):
        T=frozenset(pairs[j][bits[j]] for j in range(r))
        pattern.append(((-1)**sum(bits),T))
    return [sum(sign for sign,T in pattern if T.issubset(S)) for S in X]


def test_n(n):
    X=[frozenset(t) for t in combinations(range(n),3)]
    lam=eig(n)
    vals=[kernel(n,j) for j in range(4)]
    for r in range(4):
        v=v_r(n,X,r)
        assert any(v), (n,r,'empty sector vector')
        for i,S in enumerate(X):
            lhs=sum(vals[len(S&T)]*vv for T,vv in zip(X,v) if vv)
            assert lhs==lam[r]*v[i], (n,r,i,lhs,lam[r]*v[i])
    assert sum((comb(n,r)-(comb(n,r-1) if r else 0))*lam[r] for r in range(4)) == len(X)
    rank=sum((comb(n,r)-(comb(n,r-1) if r else 0)) for r in range(4) if lam[r])
    assert rank==(10 if n==6 else comb(n,3))
    return len(X)


def main():
    tested=0
    for n in (6,7,8,9,10,11,12,13,15):
        tested+=test_n(n)
    beta=F(169,148500)
    assert eig(13)[1]==beta
    assert eig(12)[1]==F(16,1215)
    assert eig(13)[0]==F(4459,990)
    assert min(eig(13))==beta
    for n in range(7,101):
        assert min(eig(n))>=beta
        if n!=13:
            assert min(eig(n))>beta
    print('HYPERSIMPLEX_CUBIC_SAMPLING_OK',tested,'exact Gram rows; 94 extra dimension spot checks')

if __name__ == '__main__':
    main()
