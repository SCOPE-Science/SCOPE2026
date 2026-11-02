#!/usr/bin/env python3
"""Exact finite-state checks for regular-hypergraph group reproduction."""
from fractions import Fraction as Q
from itertools import combinations
from math import prod

def fixation(n, edges, r):
    E = [sum(1 << v for v in e) for e in edges]
    incidence = [[k for k, e in enumerate(E) if e & (1 << v)] for v in range(n)]
    degrees = {len(a) for a in incidence}
    assert len(degrees) == 1 and next(iter(degrees)) > 0
    d = next(iter(degrees))
    states = list(range(1, (1 << n) - 1))
    idx = {s: j for j, s in enumerate(states)}
    m = len(states)
    A = [[Q(int(j == k)) for k in range(m)] + [Q(0)] for j in range(m)]
    for s in states:
        j = idx[s]
        i = s.bit_count()
        total = r * i + n - i
        for v in range(n):
            f = r if s & (1 << v) else Q(1)
            for ek in incidence[v]:
                e = E[ek]
                nxt = s | e if s & (1 << v) else s & ~e
                prob = f / (total * d)
                if nxt == (1 << n) - 1:
                    A[j][-1] += prob
                elif nxt != 0:
                    A[j][idx[nxt]] -= prob
    # Exact rational Gauss-Jordan elimination, state systems here have at most 30 states.
    for j in range(m):
        piv = next((k for k in range(j, m) if A[k][j]), None)
        assert piv is not None
        A[j], A[piv] = A[piv], A[j]
        z = A[j][j]
        A[j] = [w / z for w in A[j]]
        for k in range(m):
            if k == j: continue
            z = A[k][j]
            if z:
                A[k] = [v - z*w for v, w in zip(A[k], A[j])]
    return {s: A[idx[s]][-1] for s in states}

def moran(i, n, r):
    return Q(i, n) if r == 1 else (1-r**(-i))/(1-r**(-n))

def local_gap(a,b,r):
    return r*a*(r**(-b)-1)+b*(r**a-1)

def run():
    for a in range(1, 10):
        for b in range(1, 10):
            for r in [Q(1, 8), Q(1, 2), Q(2, 3), Q(3, 2), Q(2), Q(7)]:
                gap = local_gap(a,b,r)
                assert gap >= 0 and (gap == 0) == (a == 1 and b == 1)
    print('local mixed-edge gap: exact for 9x9 compositions, six rates')
    fams = [
        ('single triple',3,[(0,1,2)]),
        ('complete four-vertex triple',4,list(combinations(range(4),3))),
        ('five-vertex triple cycle',5,[tuple((j+k)%5 for k in range(3)) for j in range(5)]),
        ('degree-four mixed size 3/5',5,[tuple((j+k)%5 for k in range(3)) for j in range(5)]+[tuple(range(5))]),
    ]
    for name,n,edges in fams:
        for r in [Q(1,2),Q(1),Q(2)]:
            p = fixation(n,edges,r)
            diff = [p[s]-moran(s.bit_count(),n,r) for s in p]
            assert all(x > 0 for x in diff) if r < 1 else (all(x < 0 for x in diff) if r > 1 else all(x == 0 for x in diff))
            print(f'{name}: r={r}, checked {len(p)} transient states; phi_single={p[1]}, gap_min={min(map(abs,diff))}')
    # Cross-check the originating paper's Eq. (20), for N=4, all 4 triple edges.
    n=4; edges=list(combinations(range(n),3))
    for r in [Q(1,2),Q(2)]:
        p=fixation(n,edges,r)
        assert p[1] == r**2/(r+1)**2
    print('SOURCE_N4_FORMULA_OK; ALL_EXACT_CHECKS_OK')

if __name__ == '__main__':run()
