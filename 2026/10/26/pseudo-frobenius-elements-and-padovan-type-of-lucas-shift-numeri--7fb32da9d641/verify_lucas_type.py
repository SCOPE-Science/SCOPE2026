#!/usr/bin/env python3
"""Exact finite checks for the Lucas numerical-semigroup pseudo-Frobenius theorem.
Finite tests support, but do not replace, the written all-index proof.
"""
from heapq import heappush, heappop

L = [2, 1]
for _ in range(25):
    L.append(L[-1] + L[-2])
T = [1, 2] + L[2:]

def masks(a):
    m = L[a]
    out = {}
    for z in range(1 << a):
        if z & (z << 1) or z & 5 == 5:
            continue
        x = sum(T[i] for i in range(a) if (z >> i) & 1)
        assert x < m and x not in out
        out[x] = z
    assert len(out) == m
    return out

def expected(a):
    out = set()
    for x, b in masks(a).items():
        bits = {i for i in range(a) if b >> i & 1}
        # independent dominating set on induced path indices 3,...,a-1
        up = all(j in bits or j-1 in bits or j+1 in bits for j in range(3, a))
        case_a = 0 in bits and up
        case_b = 1 in bits and 3 in bits and up
        case_c = a % 2 == 1 and x in (L[a]-1, L[a]-2)
        if case_a or case_b or case_c:
            out.add(x)
    return out

def actual(a):
    m = L[a]
    bs = [10**8] * m
    bs[0] = 0
    for x in range(1, m):
        bs[x] = 1 + min(bs[x-v] for v in T[:a] if v <= x)
    out = {x for x in range(1, m) if all(bs[(x+v)%m] <= bs[x] + (x+v)//m for v in T[:a])}
    return out, bs

def path_maximal(n):
    return sum(1 for b in range(1 << n) if not (b & (b << 1)) and all((b >> j) & 1 or (j > 0 and (b >> (j-1)) & 1) or (j + 1 < n and (b >> (j+1)) & 1) for j in range(n)))

for a in range(5, 22):
    got, bs = actual(a)
    exp = expected(a)
    assert got == exp, (a, got ^ exp)
    p = path_maximal(a-3)
    q = sum(1 for b in range(1 << (a-3)) if b & 1 and not b & (b << 1) and all((b >> j) & 1 or (j and (b >> (j-1)) & 1) or (j+1 < a-3 and (b >> (j+1)) & 1) for j in range(a-3)))
    assert len(got) == p + q + 2*(a%2)
    # Independently verify each pseudo-Frobenius gap by Dijkstra over Apéry graph for small a
    if a <= 13:
        m = L[a]
        d = [10**30] * m
        d[0] = 0
        h = [(0,0)]
        while h:
            cost, x = heappop(h)
            if cost != d[x]: continue
            for t in T[:a]:
                y = (x+t) % m
                nc = cost + m+t
                if nc < d[y]: d[y] = nc; heappush(h,(nc,y))
        assert d == [bs[x]*m+x for x in range(m)]
    print(f'PASS a={a:2d} L_a={L[a]:5d} type={len(got):3d}')
print('ALL FINITE CHECKS PASS')
