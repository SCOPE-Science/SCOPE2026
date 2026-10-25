#!/usr/bin/env python3
"""Finite exact checks for generalized-dihedral quotient-type theorem.

Standard library only; multiplication tables and normal-subgroup tests are
constructed independently of the structural classification in the proof.
"""
from collections import Counter, deque
from itertools import product
from math import prod


def gaussian_two(d, r):
    if r < 0 or r > d:
        return 0
    # Use an exact rational product.
    from fractions import Fraction
    z = Fraction(1)
    for j in range(r):
        z *= Fraction(2 ** (d-j) - 1, 2 ** (r-j) - 1)
    assert z.denominator == 1
    return int(z)


def group(moduli):
    vs = list(product(*[range(m) for m in moduli])) if moduli else [()]
    nv = len(vs)
    index = {v: i for i, v in enumerate(vs)}
    order = 2 * nv
    def mul(x, y):
        a, t = divmod(x, 2)
        b, u = divmod(y, 2)
        sgn = -1 if t else 1
        return 2*index[tuple((v + sgn*w) % m for v, w, m in zip(vs[a], vs[b], moduli))] + (t ^ u)
    M = [[mul(x,y) for y in range(order)] for x in range(order)]
    inv = [next(y for y in range(order) if M[x][y] == 0 and M[y][x] == 0) for x in range(order)]
    return nv, M, inv


def generated(H, x, M, inv):
    gens = tuple(H) + (x, inv[x])
    q = deque([0])
    found = {0}
    while q:
        a = q.popleft()
        for g in gens:
            b = M[a][g]
            if b not in found:
                found.add(b)
                q.append(b)
    return frozenset(found)


def all_subgroups(M, inv):
    n = len(M)
    first = frozenset([0])
    seen = {first}
    q = deque([first])
    while q:
        H = q.popleft()
        for x in range(n):
            if x in H:
                continue
            K = generated(H, x, M, inv)
            if K not in seen:
                seen.add(K)
                q.append(K)
    return seen


def test(moduli):
    nv, M, inv = group(moduli)
    n = len(M)
    subs = all_subgroups(M, inv)
    normal = [H for H in subs if all(M[M[g][h]][inv[g]] in H for g in range(n) for h in H)]
    d = sum(m % 2 == 0 for m in moduli)
    counts = Counter()
    for H in normal:
        if all(M[x][x] in H for x in range(n)):
            v = n // len(H)
            assert v & (v-1) == 0
            counts[v.bit_length()-1] += 1
    expected = {r: gaussian_two(d, r-1) + (1 << r) * gaussian_two(d, r) for r in range(1,d+2)}
    expected[0] = 1
    assert all(counts[r] == expected[r] for r in expected), (moduli, counts, expected)
    assert all(r in expected for r in counts), (moduli, counts, expected)
    # All normal subgroups not lying in the rotation group must have elementary quotient.
    rotations = frozenset(range(0,n,2))
    assert all(H <= rotations or all(M[x][x] in H for x in range(n)) for H in normal)
    # Check each subgroup of A is normal in its generalized dihedral group.
    assert all(any(H == K for K in normal) for H in subs if H <= rotations)
    print('CASE', moduli, 'order', n, 'subgroups',len(subs), 'normal',len(normal), 'elementary quotient counts', sorted(counts.items()))


if __name__ == '__main__':
    for dims in [(), (2,), (3,), (4,), (5,), (6,), (2,2), (3,3), (4,2), (2,3), (2,2,2), (4,3), (2,4,2)]:
        test(dims)
    print('VERIFY_OK')
