#!/usr/bin/env python3
"""Exact finite checks for the two-weight isotonic stability formula.

Only Python standard-library modules are used. These tests corroborate an
analytical all-posets result; finite enumeration is not a universal proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def closure(n, edges):
    r = [[i == j for j in range(n)] for i in range(n)]
    for u, v in edges:
        r[u][v] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j] |= r[i][k] and r[k][j]
    return r


def connected(B, edges):
    if not B:
        return False
    seen = {next(iter(B))}
    while True:
        nxt = seen | {v for u, v in edges if u in seen and v in B} | {u for u, v in edges if v in seen and u in B}
        if nxt == seen:
            return seen == B
        seen = nxt


def admissible_blocks(n, edges):
    r = closure(n, edges)
    out = []
    for mask in range(1, 1 << n):
        B = {i for i in range(n) if (mask >> i) & 1}
        if not connected(B, edges):
            continue
        if all(c in B for a in B for b in B if r[a][b] for c in range(n) if r[a][c] and r[c][b]):
            out.append(frozenset(B))
    return out


def fractions_of_block(B, m, h):
    s = sum(m[j] for j in B)
    t = sum(h[j] for j in B)
    ell1 = t * max(m[j] / h[j] for j in B) / s
    ell2_squared = t * sum(m[j]**2 / h[j] for j in B) / (s*s)
    return ell1, ell2_squared, F(1)


def possible_partitions(n, edges):
    # Every active-edge pattern produces connected equality components;
    # the quotient is feasible with strict inequalities iff it is acyclic.
    result = set()
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def root(u):
            while u != parent[u]:
                u = parent[u]
            return u
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                a, b = root(u), root(v)
                parent[a] = b
        blocks = tuple(sorted(tuple(sorted(j for j in range(n) if root(j) == root(i))) for i in range(n) if root(i) == i))
        label = {v: k for k, B in enumerate(blocks) for v in B}
        quotient = {(label[u], label[v]) for u, v in edges if label[u] != label[v]}
        if any(closure(len(blocks), quotient)[i][j] and closure(len(blocks), quotient)[j][i] for i in range(len(blocks)) for j in range(i+1, len(blocks))):
            continue
        result.add(blocks)
    return result


def check_one(n, edges, m, h):
    m = tuple(F(v) for v in m)
    h = tuple(F(v) for v in h)
    B = admissible_blocks(n, edges)
    values = [fractions_of_block(b, m, h) for b in B]
    sharp = tuple(max(x[k] for x in values) for k in range(3))
    parts = possible_partitions(n, edges)
    actual = tuple(max(max(fractions_of_block(block, m, h)[k] for block in part) for part in parts) for k in range(3))
    assert sharp == actual, (n, edges, m, h, sharp, actual)
    # All admissible blocks can occur as one block, other vertices singleton.
    for b in B:
        part = tuple(sorted((tuple(sorted(b)),) + tuple((j,) for j in range(n) if j not in b)))
        assert part in parts, (b, n, edges)
        # Check a projected point and KKT multipliers exactly.
        labels = {i: k for k, bb in enumerate(part) for i in bb}
        quotient = {(labels[u], labels[v]) for u, v in edges if labels[u] != labels[v]}
        rank = [0] * len(part)
        for _ in range(len(part)):
            for u, v in quotient:
                rank[v] = max(rank[v], rank[u]+1)
        y = [F(10*rank[labels[j]]) for j in range(n)]
        lam = [F(1) if u in b and v in b else F(0) for u, v in edges]
        gradient = [F(0) for _ in range(n)]
        for (u,v), l in zip(edges, lam):
            gradient[u] += l
            gradient[v] -= l
        x = [y[j] + gradient[j]/m[j] for j in range(n)]
        assert all(y[u] <= y[v] for u,v in edges)
        assert all(y[u] < y[v] for u,v in edges if not (u in b and v in b))
        assert all(m[j]*(x[j]-y[j]) == gradient[j] for j in range(n))
        assert all(sum(m[j]*(x[j]-y[j]) for j in bb)==0 for bb in part)
    return len(B), len(parts)


def main():
    graphs = [
        (2, ((0,1),)),
        (3, ((0,1),(1,2))),
        (4, ((0,1),(1,2),(2,3))),
        (4, ((0,1),(0,2),(1,3),(2,3))),
        (5, ((0,1),(0,2),(0,3),(0,4))),
        (5, ((0,2),(1,2),(2,3),(2,4))),
        (6, ((0,2),(0,3),(1,3),(2,4),(3,4),(4,5))),
    ]
    checks = blocks = partitions = 0
    for n, edges in graphs:
        for m in [(1,)*n, tuple(i+1 for i in range(n)), tuple(2**i for i in range(n)), tuple(3 if i%2 else 1 for i in range(n))]:
            for h in [(1,)*n, m, tuple((i+1)**2 for i in range(n))]:
                b, p = check_one(n, edges, m, h)
                checks += 1
                blocks += b
                partitions += p
    assert checks == 84
    print('PASS: %d weighted graph cases; %d admissible-block checks; %d feasible-partition comparisons.' % (checks, blocks, partitions))
    # Nonexpansive iff monitoring masses agree with fit masses along covers.
    for n, edges in graphs:
        for m in [(1,)*n, tuple(i+1 for i in range(n)), tuple(2**i for i in range(n))]:
            for h in [(1,)*n, m, tuple((i+1)**2 for i in range(n))]:
                mm = tuple(map(F, m)); hh = tuple(map(F,h))
                blocks = admissible_blocks(n, edges)
                L1 = max(fractions_of_block(b, mm, hh)[0] for b in blocks)
                L2sq = max(fractions_of_block(b, mm, hh)[1] for b in blocks)
                expected = all(mm[u]*hh[v] == mm[v]*hh[u] for u,v in edges)
                assert (L1==1) == expected and (L2sq==1)==expected
    print('PASS: %d exact rigidity comparisons.' % (len(graphs)*3*3))
    assert fractions_of_block({0,1}, (F(9),F(1)), (F(1),F(1)))[:2] == (F(9,5), F(41,25))
    print('PASS: two-node witness L1=9/5; L2 squared=41/25; L-infinity=1.')

if __name__ == '__main__':
    main()
