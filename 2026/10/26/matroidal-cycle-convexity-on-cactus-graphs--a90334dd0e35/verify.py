#!/usr/bin/env python3
"""Exact finite checks for cycle-convex closure on cactus graphs.
Uses only the Python standard library. Run: python verify.py
"""
from itertools import combinations
from random import Random


def cycles(adj):
    n = len(adj)
    out = []
    for a in range(n):
        def dfs(path, used):
            u = path[-1]
            for v in range(n):
                if not ((adj[u] >> v) & 1):
                    continue
                if v == a and len(path) >= 3:
                    if path[1] < path[-1]:
                        out.append(tuple(path))
                elif v > a and not ((used >> v) & 1):
                    dfs(path + [v], used | (1 << v))
        dfs([a], 1 << a)
    return out


def is_connected(adj):
    if not adj:
        return True
    seen = 1
    while True:
        nxt = seen
        for i in range(len(adj)):
            if seen >> i & 1:
                nxt |= adj[i]
        if nxt == seen:
            return seen == (1 << len(adj)) - 1
        seen = nxt


def cactus_cycles(adj):
    if not is_connected(adj):
        return None
    used = set()
    cc = cycles(adj)
    for cyc in cc:
        for u, v in zip(cyc, cyc[1:] + cyc[:1]):
            e = (min(u, v), max(u, v))
            if e in used:
                return None
            used.add(e)
    return [sum(1 << i for i in cyc) for cyc in cc]


def hull(mask, cc):
    while True:
        nxt = mask
        for c in cc:
            if (c & mask).bit_count() == c.bit_count() - 1:
                nxt |= c
        if nxt == mask:
            return mask
        mask = nxt


def quotient_closure(mask, relations, n):
    out = mask
    outside = ((1 << n) - 1) ^ mask
    for r in relations:
        rem = r & outside
        if rem and not (rem & (rem - 1)):
            out |= rem
    return out


def verify_one(adj, cc, check_triples=False, masks=None):
    n = len(adj)
    rel = [0]
    for c in cc:
        rel += [r ^ c for r in rel]
    if len(set(rel)) != 1 << len(cc):
        raise AssertionError('dependent cycle relations')
    if any(r.bit_count() == 1 for r in rel):
        raise AssertionError('loop in quotient')
    if masks is None:
        masks = range(1 << n)
    for s in masks:
        if hull(s, cc) != quotient_closure(s, rel, n):
            raise AssertionError(('closure mismatch', n, cc, s))
    if check_triples:
        cl = [hull(s, cc) for s in range(1 << n)]
        rank = helly = radon = 0
        for s in range(1 << n):
            elems = [1 << i for i in range(n) if s >> i & 1]
            size = len(elems)
            if all(not (cl[s ^ v] & v) for v in elems):
                rank = max(rank, size)
            inter = (1 << n) - 1
            for v in elems:
                inter &= cl[s ^ v]
            if not inter:
                helly = max(helly, size)
            if all(not (cl[a] & cl[s ^ a]) for a in range(1, s) if (a & s) == a):
                radon = max(radon, size)
        if (rank, helly, radon) != (n - len(cc),) * 3:
            raise AssertionError(('triple mismatch', rank, helly, radon, n, cc))


def exhaustive():
    counts = []
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        checked = 0
        for mask in range(1 << len(pairs)):
            if mask.bit_count() < n - 1:
                continue
            adj = [0] * n
            for t, (u, v) in enumerate(pairs):
                if mask >> t & 1:
                    adj[u] |= 1 << v
                    adj[v] |= 1 << u
            cc = cactus_cycles(adj)
            if cc is not None:
                verify_one(adj, cc, check_triples=True)
                checked += 1
        counts.append((n, checked))
    return counts


def randomized():
    rng = Random(20261019)
    checked = 0
    for _ in range(200):
        adj = [0]
        while len(adj) < 15:
            root = rng.randrange(len(adj))
            remaining = 15 - len(adj)
            if remaining >= 2 and rng.randrange(3):
                d = rng.randrange(2, min(6, remaining) + 1)
                vertices = [root] + list(range(len(adj), len(adj) + d))
                adj.extend([0] * d)
                for a, b in zip(vertices, vertices[1:] + vertices[:1]):
                    adj[a] |= 1 << b
                    adj[b] |= 1 << a
            else:
                v = len(adj)
                adj.append(1 << root)
                adj[root] |= 1 << v
        cc = cactus_cycles(adj)
        assert cc is not None
        masks = [rng.randrange(1 << len(adj)) for _ in range(64)]
        verify_one(adj, cc, masks=masks)
        checked += 1
    return checked


def boundary():
    # Diamond: triangles (0,1,2) and (0,1,3) share an edge.
    adj = [0] * 4
    for u, v in [(0,1),(1,2),(2,0),(0,3),(1,3)]:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    cc = [sum(1 << v for v in c) for c in cycles(adj)]
    S, x, y = 1 << 2, 0, 3
    return bool(hull(S | (1 << x), cc) & (1 << y)) and not bool(hull(S | (1 << y), cc) & (1 << x))

if __name__ == '__main__':
    print('EXHAUSTIVE_CONNECTED_LABELED_CACTI', exhaustive())
    print('RANDOM_CACTI_15_VERTICES', randomized(), 'SAMPLED_SUBSETS_EACH', 64)
    assert boundary()
    print('DIAMOND_EXCHANGE_FAILURE_CONFIRMED')
    print('VERIFY_OK')
