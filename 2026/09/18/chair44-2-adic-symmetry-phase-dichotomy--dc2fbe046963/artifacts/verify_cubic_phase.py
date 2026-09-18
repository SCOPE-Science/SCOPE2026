#!/usr/bin/env python3
"""Finite checks for the cubic-group lemmas used in the Chair44 phase theorem."""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd
from collections import Counter

I = ((1,0,0),(0,1,0),(0,0,1))


def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )


def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def sub(A, B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(3)) for i in range(3))


def rank_q(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        p = A[r][c]
        A[r] = [x/p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                q = A[i][c]
                A[i] = [A[i][j] - q*A[r][j] for j in range(n)]
        r += 1
    return r


def rank2_smith_invariants(A):
    entries = [abs(x) for row in A for x in row]
    d1 = 0
    for x in entries:
        d1 = gcd(d1, x)
    g2 = 0
    for rs in combinations(range(3), 2):
        for cs in combinations(range(3), 2):
            a, b = rs
            c, d = cs
            minor = abs(A[a][c]*A[b][d] - A[a][d]*A[b][c])
            g2 = gcd(g2, minor)
    return (d1, g2//d1)


def determinantal_divisor_3(rows):
    g = 0
    for rs in combinations(range(len(rows)), 3):
        M = tuple(rows[i] for i in rs)
        g = gcd(g, abs(det3(M)))
        if g == 1:
            return 1
    return g


def is_power_of_two(n):
    return n > 0 and n & (n-1) == 0


def proper_cubic_group():
    out = []
    for p in permutations(range(3)):
        for s in product((-1, 1), repeat=3):
            M = [[0]*3 for _ in range(3)]
            for i, j in enumerate(p):
                M[i][j] = s[i]
            M = tuple(tuple(row) for row in M)
            if det3(M) == 1:
                out.append(M)
    return tuple(out)


G = proper_cubic_group()
Gset = set(G)


def generated(gens):
    H = {I}
    changed = True
    while changed:
        changed = False
        for A in tuple(H):
            for B in gens:
                for C in (mul(A,B), mul(B,A)):
                    if C not in H:
                        H.add(C)
                        changed = True
    return frozenset(H)


def all_subgroups():
    subs = {frozenset((I,))}
    changed = True
    while changed:
        changed = False
        for H in tuple(subs):
            for M in G:
                if M not in H:
                    K = generated(tuple(H) + (M,))
                    if K not in subs:
                        subs.add(K)
                        changed = True
    return subs


def cyclic(H):
    return any(generated((h,)) == H for h in H)


print("proper_cubic_rotations", len(G))
assert len(G) == 24 and len(Gset) == 24

snf_counts = Counter()
for R in G:
    if R == I:
        continue
    A = sub(I, R)
    assert rank_q(A) == 2
    snf_counts[rank2_smith_invariants(A)] += 1

print("single_rotation_rank", 2)
for inv, count in sorted(snf_counts.items()):
    print("single_rotation_snf", inv, count)
assert snf_counts == Counter({(1,1): 8, (1,2): 12, (2,2): 3})

subs = all_subgroups()
print("subgroups", len(subs))
assert len(subs) == 30

summary = Counter()
for H in subs:
    if cyclic(H):
        continue
    rows = []
    for R in H:
        rows.extend(sub(I, R))
    r = rank_q(rows)
    delta = determinantal_divisor_3(rows)
    assert r == 3
    assert is_power_of_two(delta)
    summary[(len(H), delta)] += 1

for key, count in sorted(summary.items()):
    print("noncyclic_subgroup", "order", key[0], "delta3", key[1], "count", count)

expected = Counter({(4,4):3, (4,8):1, (6,2):4, (8,4):3, (12,2):1, (24,2):1})
assert summary == expected
print("all_noncyclic_full_rank", True)
print("all_noncyclic_delta3_power_of_two", True)
