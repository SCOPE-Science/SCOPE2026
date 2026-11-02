"""Exact finite checks for strict comparable-pair semigroups of finite posets.

All computations use Python's standard library. The universal theorem is proved
symbolically in RESULT.md; these checks sample finite posets and obstruction graphs.
"""
from itertools import combinations


def posets_with_fixed_linear_extension(n):
    pairs = list(combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        strict = {pairs[i] for i in range(len(pairs)) if bits & (1 << i)}
        if any((a, c) not in strict for a, b in strict
               for x, c in strict if b == x):
            continue
        yield strict


def height(n, strict):
    longest = [1] * n
    for j in range(n):
        longest[j] = 1 + max([longest[i] for i in range(j) if (i, j) in strict] or [0])
    return max(longest, default=0)


def n_relations(strict):
    return {(x, y) for x, y in strict if any((y, z) in strict for z in {b for a, b in strict})}


def relation_edges(strict):
    return {((a, b), (c, d)) for a, b in strict for c, d in strict if b == c}


def oriented_odd_cycle(m):
    n = 2 * m + 1
    return {(i, (i + 1) % n) if i % 2 == 0 else
            ((i + 1) % n, i) for i in range(n)}


def hom_to_digraph(edges, domain, template_vertices, template_edges):
    """Backtracking CSP, exact for finite directed graphs."""
    domain = list(domain)
    if not template_vertices:
        return not domain
    # Use constraints on assigned neighbors, treating both directions.
    inc = {a: [] for a in domain}
    for u, v in edges:
        inc[u].append((v, True))
        inc[v].append((u, False))
    order = sorted(domain, key=lambda x: -len(inc[x]))
    col = {}
    def rec(i):
        if i == len(order):
            return True
        u = order[i]
        for value in template_vertices:
            if all((value, col[w]) in template_edges if forward else
                   (col[w], value) in template_edges
                   for w, forward in inc[u] if w in col):
                col[u] = value
                if rec(i+1):
                    return True
                del col[u]
        return False
    return rec(0)


def hom_odd_cycle_dp(m, V, E):
    """Exact cyclic constraint propagation, avoiding exponential backtracking."""
    n = 2*m+1
    for start in V:
        possible = {start}
        for i in range(n):
            if i % 2 == 0:
                possible = {b for a in possible for b in V if (a,b) in E}
            else:
                possible = {b for a in possible for b in V if (b,a) in E}
            if not possible:
                break
        if start in possible:
            return True
    return False


def proper_odd_cycles_map_to_three_path():
    Dv = (0, 1, 2)
    De = {(0, 1), (1, 2)}
    for m in range(1, 9):
        n = 2 * m + 1
        E = oriented_odd_cycle(m)
        for v in range(n):
            V = set(range(n)) - {v}
            F = {(a, b) for a, b in E if a in V and b in V}
            assert hom_to_digraph(F, V, Dv, De), (m, v)
    return 8


def main():
    counts = {}
    samples = 0
    for n in range(1, 7):
        hist = {}
        for R in posets_with_fixed_linear_extension(n):
            h = height(n, R)
            hist[h] = hist.get(h, 0) + 1
            edges = relation_edges(R)
            # At height <= 3, the graph of nonzero binary products
            # cannot contain a directed two-edge walk.
            if h <= 3:
                sources = {a for a, b in edges}
                targets = {b for a, b in edges}
                assert not sources & targets
            # Check the algebraic multiplication's associativity on all
            # strict intervals for a handful of dimensions.
            if n <= 5:
                S = [None] + sorted(R)
                def mul(x, y):
                    return (x[0], y[1]) if x is not None and y is not None and x[1] == y[0] else None
                for x in S:
                    for y in S:
                        for z in S:
                            assert mul(mul(x, y), z) == mul(x, mul(y, z))
            # Every height >= 4 poset contains a directed chain of three
            # composable strict intervals, enabling the local maps.
            if h >= 4:
                assert any((a,b) in R and (b,c) in R and (c,d) in R
                           for a in range(n) for b in range(n)
                           for c in range(n) for d in range(n))
            samples += 1
        counts[n] = hist
    proper = proper_odd_cycles_map_to_three_path()
    for n in (4, 5, 6):
        R = set(combinations(range(n), 2))
        V = R
        E = relation_edges(R)
        for m in range(1, 9):
            C = oriented_odd_cycle(m)
            assert not hom_odd_cycle_dp(m, V, E), (n, m)
    # The core graph of the four-chain interval template maps to
    # the directed three-vertex path, with a return homomorphism.
    chain4 = set(combinations(range(4), 2))
    edges = relation_edges(chain4)
    rho = {(0,1):0,(1,2):1,(2,3):2,(0,2):1,(1,3):1,(0,3):0}
    assert all((rho[a],rho[b]) in {(0,1),(1,2)} for a,b in edges)
    assert ((0,1),(1,2)) in edges and ((1,2),(2,3)) in edges
    print('POSETS_WITH_FIXED_LINEAR_EXTENSION', counts)
    print('FULLY_CHECKED_POSETS', samples)
    print('PROPER_ODD_CYCLE_TESTS',proper)
    print('CHAIN_TARGETS_AND_ODD_CYCLES', 'n=4..6, lengths=3..17')
    print('SEMIGROUP_ASSOCIATIVITY', 'all tested posets n<=5')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
