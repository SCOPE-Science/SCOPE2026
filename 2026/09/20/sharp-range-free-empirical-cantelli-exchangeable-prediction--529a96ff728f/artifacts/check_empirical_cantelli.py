#!/usr/bin/env python3
"""Exact-rational checks for the exchangeable empirical Cantelli formulas."""

from fractions import Fraction

def fl(x):
    return x.numerator // x.denominator

def ce(x):
    return -((-x.numerator) // x.denominator)

def R(n, q):
    # q = t^2
    return Fraction(n*n - 1, 1) + n*q, Fraction(n - 1, 1) + n*q

def ratio_R(n, q):
    a,b=R(n,q)
    return a/b

def high_t2(n, r):
    # M=n+1; two-level centered vector has r equal positive coordinates
    # and M-r equal negative coordinates.  For a positive coordinate,
    # this is its leave-one-out externally studentized squared residual.
    M=n+1
    if r==1:
        return None  # +infinity: deleting the unique high leaves zero variance
    return Fraction((M-2)*(M-r), (M-1)*(r-1))

def a2(n,q):
    # squared full-sample normalized threshold equivalent to T >= sqrt(q)
    return Fraction(n*n,1)*q / (Fraction(n*n-1,1)+n*q)

qs = [
    Fraction(0,1), Fraction(1,100), Fraction(1,16), Fraction(1,4),
    Fraction(1,2), Fraction(1,1), Fraction(2,1), Fraction(4,1),
    Fraction(9,1), Fraction(25,1), Fraction(100,1)
]

checks=0
for n in range(2, 81):
    M=n+1
    for q in qs:
        rr=ratio_R(n,q)
        # Algebraic identity R = M/(1+a^2)
        assert rr == Fraction(M,1)/(1+a2(n,q))

        # Inclusive tail: r=floor(R) positive coordinates attain T >= sqrt(q).
        ri=fl(rr)
        assert 1 <= ri <= M
        if q == 0:
            # Inclusive T >= 0 is trivially allowed to have mass one.
            assert ri == M
        else:
            assert ri <= M-1
            ht=high_t2(n,ri)
            if ht is not None:
                assert ht >= q

        # Strict tail: r=ceil(R)-1 positive coordinates attain T > sqrt(q).
        rs=ce(rr)-1
        assert 1 <= rs <= M-1
        ht=high_t2(n,rs)
        if ht is not None:
            assert ht > q

        # The next integer cannot satisfy the corresponding count inequality.
        if q > 0 and ri+1 <= M-1:
            ht_next=high_t2(n,ri+1)
            if ht_next is not None:
                assert ht_next < q
        if rs+1 <= M-1:
            ht_next=high_t2(n,rs+1)
            if ht_next is not None:
                assert ht_next <= q

        checks += 1

# A concrete one-sided 95% prediction threshold at n=20:
# R=2 exactly when t=(n-1)/sqrt(n), so strict upper-tail mass <=1/21.
n=20
q=Fraction((n-1)**2,n)
assert ratio_R(n,q) == 2
assert ce(ratio_R(n,q))-1 == 1

print("all exact-rational checks passed")
print("parameter cases:", checks)
print("n range: 2..80")
print("n=20 threshold squared:", q)
print("n=20 strict-tail maximum mass: 1/21")
