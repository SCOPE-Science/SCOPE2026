#!/usr/bin/env python3
from itertools import product
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def phi(n):
    x = n
    out = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            out -= out // p
        p += 1
    if x > 1:
        out -= out // x
    return out

def c(l, q):
    return (q - 1) ** l + ((-1) ** l) * (q - 1)

def necklace(l, r, s):
    return sum(phi(l // d) * c(d, r) * c(d, s) for d in divisors(l)) // l

def predicted(m, r, s):
    return 1 + sum(necklace(l, r, s) for l in range(2, m)) + c(m, r) * c(m, s)

def leq(x, y, r):
    return x == y or (x < r and y >= r)

def maps(m, r, s):
    vals = range(r + s)
    ans = []
    for lows in product(vals, repeat=m):
        opts = []
        for i in range(m):
            good = [y for y in vals
                    if leq(lows[i], y, r) and leq(lows[(i + 1) % m], y, r)]
            if not good:
                break
            opts.append(good)
        else:
            for highs in product(*opts):
                ans.append(tuple(lows) + tuple(highs))
    return ans

def comparable(f, g, r):
    return (all(leq(x, y, r) for x, y in zip(f, g))
            or all(leq(y, x, r) for x, y in zip(f, g)))

def component_count(m, r, s):
    ms = maps(m, r, s)
    n = len(ms)
    adj = [[] for _ in range(n)]
    for i in range(n):
        fi = ms[i]
        for j in range(i):
            if comparable(fi, ms[j], r):
                adj[i].append(j)
                adj[j].append(i)
    seen = [False] * n
    count = 0
    isolated = 0
    for i in range(n):
        if seen[i]:
            continue
        count += 1
        stack = [i]
        seen[i] = True
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        if size == 1:
            isolated += 1
    return n, count, isolated

def crown4_boundary(m):
    return 2 * ((m - 1) // 2) + 1 + (4 if m % 2 == 0 else 0)

cases = [
    (2, 2, 2, 5),
    (2, 2, 3, 13),
    (3, 2, 2, 3),
    (3, 2, 3, 7),
    (3, 3, 3, 55),
    (4, 2, 2, 7),
]

for m, r, s, expected in cases:
    total, got, isolated = component_count(m, r, s)
    form = predicted(m, r, s)
    assert got == expected == form, (m, r, s, total, got, expected, form)
    assert isolated == c(m, r) * c(m, s), (m, r, s, isolated)
    print((m, r, s), "maps", total, "components", got, "isolated", isolated)

for r in range(2, 7):
    for s in range(2, 7):
        assert predicted(2, r, s) == 1 + r * (r - 1) * s * (s - 1)

for m in range(2, 13):
    assert predicted(m, 2, 2) == crown4_boundary(m), (m, predicted(m,2,2), crown4_boundary(m))

print("VERIFY_OK")
