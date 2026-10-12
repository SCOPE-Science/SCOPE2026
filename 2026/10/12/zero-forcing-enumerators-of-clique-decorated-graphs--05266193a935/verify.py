"""Exhaustive independent checks for clique-attached graph zero-forcing identity.

All computations use ordinary finite bit sets and integer arithmetic.
"""
from itertools import combinations, product
from collections import Counter
from math import comb

def zero_forces(adj, blue):
    total = (1 << len(adj)) - 1
    while True:
        added = 0
        for v, neighbors in enumerate(adj):
            if blue >> v & 1:
                w = neighbors & ~blue
                if w and w & (w - 1) == 0:
                    added |= w
        if not added:
            return blue == total
        blue |= added

def base_graph(n, mask):
    g = [0] * n
    for j, (u, v) in enumerate(combinations(range(n), 2)):
        if mask >> j & 1:
            g[u] |= 1 << v
            g[v] |= 1 << u
    return g

def decorate(g, sizes):
    n = len(g)
    adj = g[:]
    blocks = []
    for u, s in enumerate(sizes):
        block = list(range(len(adj), len(adj) + s))
        adj += [0] * s
        blocks.append(block)
        for v in block:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            for w in block:
                if w != v:
                    adj[v] |= 1 << w
    return adj, blocks

def predicted(g, sizes):
    """Polynomial from exact formal weighted expansion (no corona propagation)."""
    result = Counter()
    n = len(g)
    zf = [B for B in range(1 << n) if zero_forces(g, B)]
    for B in zf:
        p = Counter({0: 1})
        for v, s in enumerate(sizes):
            # active root has s+1 options with s selected and one with s+1;
            # inactive root has s choices with s-1 selected.
            loc = {s: s + 1, s + 1: 1} if (B >> v & 1) else {s - 1: s}
            nxt = Counter()
            for a, va in p.items():
                for b, vb in loc.items(): nxt[a + b] += va * vb
            p = nxt
        result.update(p)
    return result

def check(g, sizes):
    adj, blocks = decorate(g, sizes)
    predicted_poly = predicted(g, sizes)
    observed = Counter()
    wrong_shape = 0
    wrong_status = 0
    for S in range(1 << len(adj)):
        expected = True
        B = 0
        for v, block in enumerate(blocks):
            nblue = sum((S >> u) & 1 for u in block)
            if nblue < len(block) - 1:
                expected = False
                break
            if ((S >> v) & 1) or nblue == len(block):
                B |= 1 << v
        if expected:
            expected = zero_forces(g, B)
        actual = zero_forces(adj, S)
        if expected != actual: wrong_status += 1
        if actual: observed[S.bit_count()] += 1
    assert wrong_status == 0, ('structure', g, sizes, wrong_status)
    assert observed == predicted_poly, ('polynomial', g, sizes, observed, predicted_poly)
    return (1 << len(adj)), len(predicted_poly)

def main():
    assignments = trials = graph_cases = coeffs = 0
    for n in range(1, 5):
        for mask in range(1 << comb(n, 2)):
            g = base_graph(n, mask)
            for sizes in product((2, 3, 4), repeat=n):
                if n + sum(sizes) > 12:
                    continue
                a, c = check(g, sizes)
                assignments += a
                coeffs += c
                trials += 1
            graph_cases += 1
        print(f'base_order={n} passed_graphs={1 << comb(n, 2)} cumulative_decorated_instances={trials}')
    print(f'EXHAUSTIVE_PASS graph_cases={graph_cases} decorated_instances={trials} tested_initial_subsets={assignments} nonzero_coefficient_comparisons={coeffs}')
    print('Boundary s=1 excluded: K_2 with one pendant leaf on each endpoint produces P_4 with polynomial 2x+6x²+4x³+x⁴.')
    print('All checks use finite labeled examples only; general proof is independent.')

if __name__ == '__main__': main()
