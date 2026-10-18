#!/usr/bin/env python3
"""Exact finite arithmetic witness checks for three-row determinantal divisors.

The infinite extension and nonfreeness use mathematical lemmas and the
published nonfreeness theorem, not finite search. Standard-library only.
"""
from itertools import combinations
from math import comb


def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def audit_columns(cols):
    n = len(cols)
    inside = [det3(*(cols[j] for j in I)) for I in combinations(range(5),3)]
    outside = [det3(*(cols[j] for j in I)) for I in combinations(range(n),3) if any(j >= 5 for j in I)]
    assert len(inside) == 10
    assert all(v == 0 for v in inside)
    assert len(outside) == comb(n,3)-10
    assert all(v != 0 for v in outside)
    assert any(det3(*(cols[j] for j in I)) != 0 for I in combinations(range(n),3))
    return len(inside),len(outside)


def main():
    base = [(1,j,0) for j in range(5)]
    for n in range(6,11):
        cols = base + [(1,t,t*t) for t in range(6,n+1)]
        a,b = audit_columns(cols)
        assert 16+3*(n-5) == 3*n+1
        print(f'n={n}: vanish-only-first-five={a}, mixed-nonzero={b}, ambient={3*n}, local-generator-count-from-cited-theorem={3*n+1}')
    cols=base+[(0,0,1)]
    print('simple rank-three six-column witness:',audit_columns(cols))
    print('PASS: finite arithmetic witnesses. The all-n theorem follows from the written generic-open argument.')

if __name__ == '__main__':
    main()
