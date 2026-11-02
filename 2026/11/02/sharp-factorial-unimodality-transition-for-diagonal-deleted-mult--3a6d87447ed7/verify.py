#!/usr/bin/env python3
"""Standalone exact-integer consistency checks for the stated graph family.

Run: python3 verify.py
"""
from math import comb, factorial
from itertools import combinations


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def coeff(r, a, k):
    if k == 0:
        return 1
    if k == 1:
        return r * a
    if k == 2:
        return choose(r*a, 2)
    return (a*choose(r, k) + r*choose(a, k)
            + factorial(k)*choose(a,k)*choose(r,k)
            + choose(a,2)*choose(r,2)*choose(4,k))


def unimodal(vals):
    reached_fall = False
    for before, after in zip(vals, vals[1:]):
        if after < before:
            reached_fall = True
        elif after > before and reached_fall:
            return False
    return True


def brute_graph_counts(r, a):
    vertices = [(i,j) for i in range(a) for j in range(r)]
    n = len(vertices)
    adj = [[i != k and j != l for k,l in vertices] for i,j in vertices]
    # These graphs have diameter two whenever a,r >= 3.
    bad = [0] * (1 << n)
    for x,y,z in combinations(range(n),3):
        if ((not adj[x][y] and adj[x][z] and adj[y][z])
            or (not adj[x][z] and adj[x][y] and adj[z][y])
            or (not adj[y][z] and adj[y][x] and adj[z][x])):
            bad[(1<<x)|(1<<y)|(1<<z)] = 1
    # A subset is invalid iff it contains a forbidden triple.
    invalid = bytearray(1<<n)
    for mask in range(1,1<<n):
        low=mask & -mask
        prev=mask ^ low
        invalid[mask] = invalid[prev] or bool(bad[mask] if mask.bit_count()==3 else 0)
        if not invalid[mask] and mask.bit_count()>3:
            # All triple submasks were already classified, so build from n-bit
            # recursion by checking all immediate deletions.
            for v in range(n):
                if mask & (1<<v) and invalid[mask ^ (1<<v)]:
                    invalid[mask] = 1
                    break
    # Correction: for size >3, every invalid triple is detected via deletion
    # recurrence; for size 3 the bad mask directly encodes the obstruction.
    counts = [0]*(n+1)
    for mask,flag in enumerate(invalid):
        if not flag:
            counts[mask.bit_count()] += 1
    return counts


def main():
    for a,r in [(3,3),(3,4),(4,3),(4,4),(3,5)]:
        actual=brute_graph_counts(r,a)
        expected=[coeff(r,a,k) for k in range(r*a+1)]
        assert actual==expected,(a,r,actual,expected)
    for a in range(5,12):
        R=(a+1)*factorial(a-1)+2*a+2
        assert R >= 2*a+4
        for r in {2*a+4, 2*a+5, R-2, R-1, R, R+1, R+2}:
            vals=[coeff(r,a,k) for k in range(a+3)]
            assert all(vals[i]<vals[i+1] for i in range(a)),(a,r,'prefix')
            assert vals[a+2]>vals[a+1],(a,r,'tail')
            assert (vals[a+1]>=vals[a]) == (r>=R),(a,r,'threshold')
            expected_gap=(a*choose(r,a)*(r-R+1))//(a+1)-r
            # First numerator is always divisible by a+1 by the binomial identity.
            assert vals[a+1]-vals[a]==expected_gap,(a,r,'gap')
    for a in [5,6]:
        R=(a+1)*factorial(a-1)+2*a+2
        for r in [2*a+4,2*a+5,R-1,R,R+1]:
            seq=[coeff(r,a,k) for k in range(r+1)]
            assert unimodal(seq)==(r>=R),(a,r,'full')
    print('VERIFY_OK: exhaustive small graphs; exact coefficients; factorial threshold boundaries')

if __name__ == '__main__':
    main()
