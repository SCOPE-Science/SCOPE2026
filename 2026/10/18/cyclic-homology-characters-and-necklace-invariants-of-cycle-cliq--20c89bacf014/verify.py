#!/usr/bin/env python3
"""Independent finite checks for cyclic symmetry on cycle-product independence complexes.

Uses only the Python standard library. Run: python3 verify.py
"""
from itertools import combinations
from math import gcd, cos, sin, pi


def allowed(left, right):
    return not left or not right or (left == right and left.bit_count() == 1)


def independent_faces(m, n):
    """Generate exact faces from row color-subsets (including the empty face)."""
    blocks = range(1 << n)
    def recur(rows):
        if len(rows) == m:
            if allowed(rows[-1], rows[0]):
                mask = 0
                for i, block in enumerate(rows):
                    mask |= block << (i*n)
                yield mask
            return
        for block in blocks:
            if rows and not allowed(rows[-1], block):
                continue
            yield from recur(rows + (block,))
    yield from recur(())


def signed_reduced_lefschetz(m, n, t):
    """Trace on oriented augmented face chains, without orbit or transfer reductions."""
    total = 0
    for mask in independent_faces(m, n):
        selected = [i for i in range(m*n) if mask >> i & 1]
        permuted = [((i // n + t) % m)*n + (i % n) for i in selected]
        if sorted(permuted) != selected:
            continue
        # Sign of permutation of ordered selected vertices, insertion-sort parity.
        inversions = sum(x > y for i, x in enumerate(permuted) for y in permuted[i+1:])
        total += (-1 if (len(selected)-1 + inversions) % 2 else 1)
    return total


def predicted_character(m, n, t):
    d = gcd(m, t)
    q = n-1
    return q * (-1 if d % 2 else 1) + (3*q**(d//3) if d % 3 == 0 else 0)


def brute_row_signed_sum(d, n):
    """Direct local face enumeration for cyclic quotient length d=1,2,3,..."""
    patterns = range(1 << n)
    total = 0
    def go(rows, weight):
        nonlocal total
        if len(rows) == d:
            if allowed(rows[-1], rows[0]):
                total += weight
            return
        for a in patterns:
            if rows and not allowed(rows[-1], a):
                continue
            go(rows+(a,), weight * (-1 if a.bit_count() % 2 else 1))
    go((),1)
    return total


def tr_matrix_power(d, n):
    """Independent integer transfer-matrix computation, n+2 states."""
    size = n+2
    w = [1]+[-1]*n+[n-1]
    def adjacent(i,j):
        if i == 0 or j == 0: return True
        if i == size-1 or j == size-1: return False
        return i == j
    a = [[(w[j] if adjacent(i,j) else 0) for j in range(size)] for i in range(size)]
    power = [[int(i==j) for j in range(size)] for i in range(size)]
    for _ in range(d):
        power = [[sum(power[i][k]*a[k][j] for k in range(size))
                  for j in range(size)] for i in range(size)]
    return sum(power[i][i] for i in range(size))


def rational_character_checks():
    for r in range(1,8):
        m=3*r
        for n in range(2,8):
            chi=[predicted_character(m,n,t) for t in range(m)]
            # Cyclotomic Fourier multiplicities must be integers, nonnegative.
            for j in range(m):
                real=sum(chi[t]*cos(2*pi*j*t/m) for t in range(m))/m
                imag=sum(chi[t]*sin(2*pi*j*t/m) for t in range(m))/m
                assert abs(real-round(real))<1e-6 and abs(imag)<1e-6, (m,n,j,real,imag)
                assert round(real)>=0,(m,n,j,real)
            q=n-1
            necklace=sum(q**gcd(r,s) for s in range(r))//r
            assert sum(q**gcd(r,s) for s in range(r)) % r==0
            expected_invariant=necklace-(q if r%2 else 0)
            assert sum(chi)%m == 0
            assert sum(chi)//m == expected_invariant


def main():
    direct_cases = [(3,2),(3,3),(3,4),(6,2),(6,3),(9,2)]
    for m,n in direct_cases:
        for t in range(m):
            actual=signed_reduced_lefschetz(m,n,t)
            expect=-predicted_character(m,n,t)
            assert actual == expect, (m,n,t,actual,expect)
        print('CHAIN_LEFSCHETZ_OK',m,n)
    for d in range(1,10):
        for n in range(2,6):
            formula=predicted_character(3*d,n,d)  # gcd(3d,d)=d
            a=tr_matrix_power(d,n)
            assert a==formula,(d,n,a,formula)
            if d<=6 and n<=4:
                b=brute_row_signed_sum(d,n)
                assert b==formula,(d,n,b,formula)
    print('TRANSFER_AND_QUOTIENT_ENUMERATION_OK',9,5)
    rational_character_checks()
    print('CHARACTER_MULTIPLICITIES_AND_NECKLACES_OK',7,7)
    print('ALL_TESTS_PASSED')

if __name__=='__main__':
    main()
