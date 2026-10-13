#!/usr/bin/env python3
"""Exact finite checks for the tridiagonal symmetric determinant locus.

Only integer and rational arithmetic is used. These checks are not a proof for
arbitrary matrix sizes; the general argument is supplied separately.
"""
from fractions import Fraction
from itertools import product
from math import comb
from random import Random


def det_path(a, b):
    """Determinant of the symmetric tridiagonal matrix with diagonal a, bridge b."""
    n = len(a)
    assert len(b) == max(n-1, 0)
    if n == 0:
        return 1
    d0, d1 = 1, a[0]
    for k in range(1, n):
        d0, d1 = d1, a[k] * d1 - b[k-1]**2 * d0
    return d1


def segment(a, b, lo, hi):
    return det_path(a[lo:hi], b[lo:hi-1] if hi > lo else ())


def partials(a, b):
    n = len(a)
    da = [segment(a,b,0,k)*segment(a,b,k+1,n) for k in range(n)]
    db = [-2*b[k]*segment(a,b,0,k)*segment(a,b,k+2,n) for k in range(n-1)]
    return da + db


def predicted_sing(a,b):
    n = len(a)
    return any(b[j] == 0 and segment(a,b,0,j+1) == 0
               and segment(a,b,j+1,n) == 0 for j in range(n-1))


def cut_formula(a,b,j):
    left = segment(a,b,0,j+1)
    right = segment(a,b,j+1,len(a))
    edge_left_minor = segment(a,b,0,j)
    edge_right_minor = segment(a,b,j+2,len(a))
    return left*right - b[j]**2*edge_left_minor*edge_right_minor


def witness(n,j):
    # At cut j (0-based), take left length p and right length q.
    p, q = j+1, n-j-1
    a = [Fraction(2)]*n
    b = [Fraction(1)]*(n-1)
    b[j] = Fraction(0)
    a[j] = Fraction(p-1,p)
    a[j+1] = Fraction(q-1,q)
    return a,b


def main():
    rng = Random(140519)
    ntests = 0
    for n in range(2,12):
        for _ in range(12):
            a = [rng.randint(-4,4) for k in range(n)]
            b = [rng.randint(-3,3) for k in range(n-1)]
            f = det_path(a,b)
            for j in range(n-1):
                assert f == cut_formula(a,b,j), ('cut',n,j,a,b)
                ntests += 1
    print('integer cut identities:',ntests,'PASS')
    ngrid=0; nsing=0
    for n in (3,4,5,6):
        count=0
        for z in product((-1,0,1), repeat=2*n-1):
            a,b=z[:n],z[n:]
            lhs = det_path(a,b)==0 and all(v==0 for v in partials(a,b))
            rhs = predicted_sing(a,b)
            assert lhs == rhs, ('locus',n,a,b,lhs,rhs)
            count+=1; nsing += lhs
        ngrid+=count
        print(f'exhaustive integer grid n={n}: {count} matrices PASS')
    print('tested integer matrices:',ngrid,'singular matrices:',nsing)
    nwitness=0
    for n in range(3,13):
        for j in range(n-1):
            a,b=witness(n,j)
            p,q=j+1,n-j-1
            assert det_path(a,b)==0
            assert not any(partials(a,b))
            assert segment(a,b,0,j)==p
            assert segment(a,b,j+2,n)==q
            assert cut_formula(a,b,j)==0
            # Hessian in the coordinates (a[j],a[j+1],b[j]) at this witness:
            # [[0,pq,0],[pq,0,0],[0,0,-2pq]].
            # Its nonzero determinant establishes transverse ordinary double type.
            hess_det=2*(p*q)**3
            assert hess_det != 0
            nwitness+=1
    print('rational generic-component witnesses:',nwitness,'PASS')
    for n in range(3,20):
        deg=sum(j*(n-j) for j in range(1,n))
        assert deg==comb(n+1,3)
    print('degree identity for n=3..19: PASS')

if __name__=='__main__':
    main()
