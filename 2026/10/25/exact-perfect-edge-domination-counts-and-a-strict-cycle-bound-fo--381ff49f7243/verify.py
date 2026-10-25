#!/usr/bin/env python3
"""Standalone exact checks for perfect-edge-domination counts in cycle-tailed graphs.

Requires only Python 3. No external data. Graph edges are labeled so that c cycle
edges precede t pendant-path edges. Every computational statement is finite.
"""
from itertools import product
from functools import lru_cache

STATES = ((0, 0), (0, 1), (1, 0), (1, 1))
M = tuple(tuple(int(v == w and (v == 1 or u + x == 1))
                for w, x in STATES) for u, v in STATES)
I = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
U = (0, 1, 1, 1)


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


@lru_cache(None)
def power(n):
    p, a = I, M
    while n:
        if n & 1:
            p = mul(p, a)
        a = mul(a, a)
        n >>= 1
    return p


@lru_cache(None)
def tail(s, p, t):
    if t == 1:
        return int(p == 1 or s == 1)
    v = tuple(sum(power(t - 2)[i][j] * U[j] for j in range(4)) for i in range(4))
    return sum(int(p == 1 or s + q == 1) * v[STATES.index((p, q))]
               for q in (0, 1))


@lru_cache(None)
def lollipop(c, t):
    assert c >= 3 and t >= 1
    a = power(c - 2)
    z = 0
    for aa, bb, x, y, p in product((0, 1), repeat=5):
        if aa == 0 and x + bb + p != 1:
            continue
        if bb == 0 and y + aa + p != 1:
            continue
        z += a[STATES.index((aa, x))][STATES.index((y, bb))] * tail(aa + bb, p, t)
    return z


@lru_cache(None)
def cycle(n):
    m = power(n)
    return sum(m[i][i] for i in range(4))


def edges(c, t):
    out = [(j, (j + 1) % c) for j in range(c)]
    out.extend((0 if i == 0 else c + i - 1, c + i) for i in range(t))
    return out


def brute(c, t):
    ee = edges(c, t)
    masks = []
    for i, (u, v) in enumerate(ee):
        masks.append(sum(1 << j for j, (a, b) in enumerate(ee)
                         if i != j and (u == a or u == b or v == a or v == b)))
    res = 0
    for k in range(1 << len(ee)):
        if all((k & (1 << i)) or (k & masks[i]).bit_count() == 1
               for i in range(len(ee))):
            res += 1
    return res


def validate():
    m4, m3, m2, m1 = power(4), power(3), power(2), power(1)
    assert all(m4[i][j] == m3[i][j] + m1[i][j]
               for i in range(4) for j in range(4))
    assert all(sum(m3[i][j] * U[j] for j in range(4)) ==
               sum((m2[i][j] + I[i][j]) * U[j] for j in range(4))
               for i in range(4))
    seeds = ((3, 3, 6), (4, 5, 8), (6, 9, 12))
    for c in range(3, 6):
        for t in range(1, 4):
            assert lollipop(c, t) == seeds[c - 3][t - 1]
    for c in range(3, 12):
        for t in range(1, 11):
            if c + t <= 15:
                assert brute(c, t) == lollipop(c, t), (c, t)
    for n in range(3, 16):
        assert cycle(n) == brute(n, 0), n
    for c in range(3, 31):
        for t in range(1, 31):
            f = lollipop(c, t)
            assert f < cycle(c + t), (c, t, f)
            if c >= 6:
                assert f == lollipop(c - 1, t) + lollipop(c - 3, t)
            if t >= 4:
                assert f == lollipop(c, t - 1) + lollipop(c, t - 3)
    print('VERIFY_OK: exact 4x4 matrix identities; 9 seeds; brute checks for all c>=3, t>=1, c+t<=15;')
    print('cycle brute checks n=3..15; recurrences and strict inequalities c=3..30, t=1..30.')
    for c in range(3, 6):
        print('c=', c, 'tail_counts=', [lollipop(c, t) for t in range(1, 4)],
              'differences=', [cycle(c+t)-lollipop(c,t) for t in range(1,4)])


if __name__ == '__main__':
    validate()
