#!/usr/bin/env python3
"""Exact checks for perfect-leader allocation on unit-conductance K_{2,q}."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def inverse_trace(a):
    n = len(a)
    if n == 0:
        return Q(0)
    w = [[Q(a[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)]
         for i in range(n)]
    for i in range(n):
        t = next((r for r in range(i, n) if w[r][i] != 0), None)
        assert t is not None
        w[i], w[t] = w[t], w[i]
        pivot = w[i][i]
        w[i] = [v/pivot for v in w[i]]
        for r in range(n):
            if r != i:
                b = w[r][i]
                if b != 0:
                    w[r] = [w[r][j] - b*w[i][j] for j in range(2*n)]
    return sum((w[i][n+i] for i in range(n)), Q(0))


def direct(q, selected):
    vertices = range(q+2)
    followers = [v for v in vertices if v not in selected]
    f = len(followers)
    L = [[0]*f for _ in range(f)]
    for i,u in enumerate(followers):
        L[i][i] = q if u < 2 else 2
        for j,v in enumerate(followers):
            if u != v and ((u<2) != (v<2)):
                L[i][j] = -1
    return inverse_trace(L)


def closed(q,k,h):
    alpha, beta = 2-h, q-k+h
    assert alpha >= 0 and 0 <= beta <= q
    return Q(alpha-1,q) + Q(beta-1,2) + Q(q+2,2*q-alpha*beta)


def polynomial(q,k):
    return q**3+(1-2*k)*q**2+(-k*k+k-2)*q+2*k*(k-1)


def theorem_classes(q,k):
    if k == q+1:
        return {1}
    v = polynomial(q,k)
    return {0} if v < 0 else ({1} if v > 0 else {0,1})


def main():
    orbit_checks = 0
    exhaustive_sets = 0
    for q in range(4,16):
        for k in range(4,q+2):
            allowed = []
            for h in (0,1,2):
                if 0 <= k-h <= q:
                    s = frozenset([*range(h), *range(2,2+k-h)])
                    c = closed(q,k,h)
                    d = direct(q,s)
                    assert c == d, (q,k,h,c,d)
                    orbit_checks += 1
                    allowed.append((h,c))
            best = min(x[1] for x in allowed)
            winners = {h for h,v in allowed if v==best}
            expected = theorem_classes(q,k)
            assert winners == expected, (q,k,winners,expected)
    for q in range(4,9):
        for k in range(4,q+2):
            for selected in combinations(range(q+2), k):
                h = sum(v<2 for v in selected)
                assert direct(q,set(selected)) == closed(q,k,h)
                exhaustive_sets += 1
    for k in range(4,151):
        assert polynomial(k,k) < 0
        assert polynomial(2*k,k) < 0
        assert polynomial(3*k,k) > 0
        assert polynomial(2*k,k) < polynomial(3*k,k)
        for q in range(k,3*k+1):
            if polynomial(q,k) >= 0:
                assert all(polynomial(t,k)>0 for t in range(q+1,3*k+2))
                break
    assert closed(8,4,0)==Q(23,8)
    assert closed(8,4,1)==Q(32,11)
    assert closed(9,4,0)==Q(251,72)
    assert closed(9,4,1)==Q(41,12)
    assert closed(8,2,2)==Q(8,2)
    print(f'PASS exact independent grounded inversions: {orbit_checks} orbit representatives')
    print(f'PASS all {exhaustive_sets} leader sets for K_(2,q), 4<=q<=8, 4<=k<=q+1')
    print('PASS exact optimizer classes for all 4<=q<=15, 4<=k<=q+1')
    print('PASS integer polynomial signs and crossing for all 4<=k<=150')
    print('PASS K_(2,8), k=4: no hub has J=23/8 < 32/11 with one hub')
    print('PASS K_(2,9), k=4: one hub has J=41/12 < 251/72 with no hub')

if __name__ == '__main__':
    main()
