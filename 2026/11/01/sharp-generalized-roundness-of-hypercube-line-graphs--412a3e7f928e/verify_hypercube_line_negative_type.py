#!/usr/bin/env python3
"""Reproduce finite spectral cross-checks for the powered-distance theorem.

This checks finite instances; the all-dimension result is proved in RESULT.md.
Requires NumPy. Run: python3 verify_hypercube_line_negative_type.py
"""
from itertools import combinations
from math import comb
from collections import deque
import numpy as np


def edges(n):
    # (i, x) denotes the edge from x to x^(1<<i), x_i=0.
    return [(i, x) for i in range(n) for x in range(1 << n) if not (x >> i) & 1]


def distances_by_graph(n):
    e = edges(n)
    N = len(e)
    endpoints = [(x, x ^ (1 << i)) for i, x in e]
    adj = [[] for _ in e]
    for a in range(N):
        A = set(endpoints[a])
        for b in range(a + 1, N):
            if A.intersection(endpoints[b]):
                adj[a].append(b)
                adj[b].append(a)
    matrix = np.empty((N, N), dtype=np.int64)
    for a in range(N):
        distance = [-1] * N
        distance[a] = 0
        queue = deque([a])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        assert -1 not in distance
        matrix[a] = distance
    for a, (i, x) in enumerate(e):
        for b, (j, y) in enumerate(e):
            if a == b:
                expect = 0
            elif i == j:
                expect = 1 + ((x ^ y).bit_count())
            else:
                mask = ((1 << n) - 1) ^ (1 << i) ^ (1 << j)
                expect = 1 + (((x ^ y) & mask).bit_count())
            assert matrix[a, b] == expect, (n, a, b, matrix[a, b], expect)
    return matrix


def F(m, s, p):
    assert 0 <= s <= m
    return sum((-1)**a * comb(s,a) * comb(m-s,b) * (1+a+b)**p
               for a in range(s+1) for b in range(m-s+1))


def walsh_spectrum(n,p):
    output = []
    for s in range(n):
        a = F(n-1,s,p) - 1
        b = 2*F(n-2,s,p) if s <= n-2 else 0.0
        output += [a+(n-s-1)*b]*comb(n,s)
        if n-s >= 2:
            output += [a-b]*((n-s-1)*comb(n,s))
    assert len(output) == n*2**(n-1)
    return np.sort(np.array(output, dtype=float))


def S(n,p):
    return sum(comb(n-2,h)*((h+2)**p-(h+1)**p) for h in range(n-1))


def critical(n):
    a,b=0.,1.
    for _ in range(65):
        mid=(a+b)/2
        if S(n,mid)>1: b=mid
        else: a=mid
    return (a+b)/2


def main():
    direct=0
    for n in range(2,6):
        D=distances_by_graph(n)
        N=len(D)
        for p in [0.125,0.375,0.75,1.0,critical(n)]:
            M = D.astype(float)**p
            got = np.linalg.eigvalsh(M)
            expected = walsh_spectrum(n,p)
            err = np.max(np.abs(got-expected))
            assert err < 2e-8, (n,p,err)
            direct += 1
        r=critical(n)
        vals=walsh_spectrum(n,r)
        assert abs(S(n,r)-1)<1e-10
        assert np.count_nonzero(np.abs(vals)<2e-8)==n-1, (n,r,vals)
        assert vals[-1] > 0
        assert vals[-n-1] < -1e-7
    for n in range(2,13):
        r=critical(n)
        assert 0 < r <= 1+1e-12
        assert abs(S(n,r)-1)<2e-10
        if n>2: assert r<critical(n-1)
    assert abs(critical(2)-1)<1e-12
    assert abs(critical(3)-np.log(2)/np.log(3))<1e-12
    print('CUBE_LINE_POWERED_DISTANCE_OK',direct,'independent BFS/Gram spectral comparisons; n=2..12 roots')
    for n in range(2,13):
        print('n=%d p_crit=%.12f asymptotic_ratio=%.9f'%(n,critical(n),critical(n)*2**(n-1)/n))

if __name__ == '__main__':
    main()
