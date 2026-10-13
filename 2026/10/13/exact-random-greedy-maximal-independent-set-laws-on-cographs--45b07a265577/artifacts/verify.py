#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial

EXPECTED = {1: 1, 2: 2, 3: 8, 4: 52, 5: 472, 6: 5504}


def components(vertices, adj, complement=False):
    verts = [v for v in range(len(adj)) if (vertices >> v) & 1]
    unseen = set(verts)
    out = []
    while unseen:
        root = next(iter(unseen))
        stack = [root]
        unseen.remove(root)
        comp = 0
        while stack:
            u = stack.pop()
            comp |= 1 << u
            nbrs = []
            for v in list(unseen):
                edge = ((adj[u] >> v) & 1) == 1
                linked = (not edge) if complement else edge
                if linked:
                    nbrs.append(v)
            for v in nbrs:
                unseen.remove(v)
                stack.append(v)
        out.append(comp)
    return out


def cotree(vertices, adj):
    if vertices & (vertices - 1) == 0:
        return ('leaf', vertices, ())
    comps = components(vertices, adj, complement=False)
    if len(comps) > 1:
        children = []
        for c in comps:
            t = cotree(c, adj)
            if t is None:
                return None
            children.append(t)
        return ('union', vertices, tuple(children))
    cocomps = components(vertices, adj, complement=True)
    if len(cocomps) > 1:
        children = []
        for c in cocomps:
            t = cotree(c, adj)
            if t is None:
                return None
            children.append(t)
        return ('join', vertices, tuple(children))
    return None


def structural_stats(t):
    kind, vertices, children = t
    n = vertices.bit_count()
    if kind == 'leaf':
        return n, 1, True
    stats = [structural_stats(c) for c in children]
    if kind == 'union':
        m = 1
        for _, mi, _ in stats:
            m *= mi
        return n, m, all(ui for _, _, ui in stats)
    m = sum(mi for _, mi, _ in stats)
    uniform = all(ui for _, _, ui in stats)
    if uniform:
        n0, m0, _ = stats[0]
        uniform = all(ni * m0 == n0 * mi for ni, mi, _ in stats[1:])
    return n, m, uniform


def cotree_law(t):
    kind, vertices, children = t
    n = vertices.bit_count()
    if kind == 'leaf':
        return {vertices: Fraction(1, 1)}
    laws = [cotree_law(c) for c in children]
    if kind == 'union':
        law = {0: Fraction(1, 1)}
        for child_law in laws:
            nxt = {}
            for a, pa in law.items():
                for b, pb in child_law.items():
                    nxt[a | b] = pa * pb
            law = nxt
        return law
    law = {}
    for c, child_law in zip(children, laws):
        ni = c[1].bit_count()
        w = Fraction(ni, n)
        for I, p in child_law.items():
            law[I] = w * p
    return law


def greedy_output(perm, adj):
    chosen = 0
    for v in perm:
        if adj[v] & chosen == 0:
            chosen |= 1 << v
    return chosen


def brute_law(adj):
    n = len(adj)
    counts = Counter(greedy_output(p, adj) for p in permutations(range(n)))
    den = factorial(n)
    return {I: Fraction(c, den) for I, c in counts.items()}


def graph_from_mask(n, mask):
    adj = [0] * n
    bit = 0
    for u in range(n):
        for v in range(u + 1, n):
            if (mask >> bit) & 1:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
            bit += 1
    return adj


def main():
    cographs = 0
    permutation_checks = 0
    by_order = {}
    for n in range(1, 7):
        edges = n * (n - 1) // 2
        count = 0
        full = (1 << n) - 1
        for mask in range(1 << edges):
            adj = graph_from_mask(n, mask)
            t = cotree(full, adj)
            if t is None:
                continue
            count += 1
            cographs += 1
            rec = cotree_law(t)
            brute = brute_law(adj)
            if rec != brute:
                raise AssertionError(('law', n, mask, rec, brute))
            nn, mm, uu = structural_stats(t)
            if nn != n or mm != len(rec):
                raise AssertionError(('stats', n, mask, nn, mm, len(rec)))
            law_uniform = len(set(rec.values())) == 1
            if uu != law_uniform:
                raise AssertionError(('uniformity', n, mask, uu, rec))
            permutation_checks += factorial(n)
        by_order[n] = count
        if count != EXPECTED[n]:
            raise AssertionError(('cograph_count', n, count, EXPECTED[n]))
    print('ALL CHECKS PASSED')
    print(f'labeled_cographs_checked={cographs}')
    print(f'vertex_permutations_checked={permutation_checks}')
    print('orders=1..6')
    print('counts=' + ','.join(f'{n}:{by_order[n]}' for n in sorted(by_order)))


if __name__ == '__main__':
    main()
