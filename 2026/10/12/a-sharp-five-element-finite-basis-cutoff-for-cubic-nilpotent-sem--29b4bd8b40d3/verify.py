#!/usr/bin/env python3
"""Exact small semigroup and digraph checks for the finite-basis cutoff.

All tests use only the Python standard library. Infinite duality assertions
follow from the mathematical proof, not from these finite computations.
"""
from itertools import permutations, product, combinations


def graph_arcs(n):
    return tuple((u, v) for u in range(n) for v in range(n) if u != v)


def edges_from_mask(n, mask):
    return frozenset(arc for bit, arc in enumerate(graph_arcs(n))
                     if mask & (1 << bit))


def transitive(n, edges):
    return all((u, w) in edges for u, v in edges for x, w in edges
               if v == x)


def canonical_graph(n, edges):
    arcs = graph_arcs(n)
    return min(sum(1 << bit for bit, (u, v) in enumerate(arcs)
                   if (p[u], p[v]) in edges)
               for p in permutations(range(n)))


def make_semigroup(n_atoms, output_count, table_edges):
    """Return products on {0, atoms, output elements}; outputs annihilate."""
    size = 1 + n_atoms + output_count
    T = [[0] * size for _ in range(size)]
    for (u, v), value in table_edges.items():
        assert 0 <= u < n_atoms and 0 <= v < n_atoms and u != v
        assert 1 <= value <= output_count
        T[1 + u][1 + v] = 1 + n_atoms + value - 1
    assert all(T[u][u] == 0 for u in range(size))
    assert all(T[T[u][v]][w] == T[u][T[v][w]] == 0
               for u, v, w in product(range(size), repeat=3))
    assert any(T[u][v] != 0 for u, v in product(range(size), repeat=2))
    assert {T[u][v] for u, v in product(range(size), repeat=2)} == \
           set(range(1 + n_atoms, size)) | {0}
    return T


def canonical_table(T):
    """Complete isomorphism invariant by testing all relabellings."""
    n = len(T)
    def candidate(perm):
        inv = [0] * n
        for old, new in enumerate(perm):
            inv[new] = old
        return tuple(perm[T[inv[u]][inv[v]]]
                     for u, v in product(range(n), repeat=2))
    return min(candidate(perm) for perm in permutations(range(n)))


def hom(n, source_edges, m, target_edges):
    """Brute-force graph homomorphism, including possible 2-cycles."""
    for f in product(range(m), repeat=n):
        if all((f[u], f[v]) in target_edges for u, v in source_edges):
            return True
    return False


def induced(edges, subset):
    vertices = tuple(sorted(subset))
    index = {old: new for new, old in enumerate(vertices)}
    return len(vertices), frozenset((index[u], index[v])
                                   for u, v in edges if u in index and v in index)


def signed_odd_cycle(k):
    """Odd cycle with cyclic edge signs +,-,+,-,...,+."""
    n = 2 * k + 1
    arcs = {(i, (i + 1) % n) if i % 2 == 0
            else ((i + 1) % n, i) for i in range(n)}
    return n, frozenset(arcs)


def directed_cycle(n):
    return n, frozenset((i, (i + 1) % n) for i in range(n))


def symmetric_odd_cycle(k):
    n = 2 * k + 1
    arcs = set()
    for i in range(n):
        j = (i + 1) % n
        arcs.update(((i, j), (j, i)))
    return n, frozenset(arcs)


def symmetric_odd_wheel(k):
    n = 2 * k + 1
    hub = n
    arcs = set(symmetric_odd_cycle(k)[1])
    for i in range(n):
        arcs.update(((i, hub), (hub, i)))
    return n + 1, frozenset(arcs)


def check_small_witness(template, witness):
    n, edges = witness
    assert not hom(n, edges, 3, template)
    # Every single-vertex deletion must map. Since the target is fixed,
    # any smaller induced subgraph also maps by restriction.
    for omitted in range(n):
        m, sub = induced(edges, set(range(n)) - {omitted})
        assert hom(m, sub, 3, template), (template, witness, omitted)


def main():
    patterns = {}
    classes = {}
    for mask in range(1, 64):
        arcs = edges_from_mask(3, mask)
        rep = canonical_graph(3, arcs)
        flag = transitive(3, arcs)
        if rep in patterns:
            assert patterns[rep] == flag
        patterns[rep] = flag
        T = make_semigroup(3, 1, {arc: 1 for arc in arcs})
        c = canonical_table(T)
        if c in classes:
            assert classes[c] == flag
        classes[c] = flag

    assert len(patterns) == 15
    assert sum(patterns.values()) == 4
    assert len(classes) == 15
    assert sum(classes.values()) == 4

    # The remaining order-five possibility has two indecomposables and
    # two distinct nonzero output elements, so both opposite products occur.
    T_double = make_semigroup(2, 2, {(0, 1): 1, (1, 0): 2})
    c_double = canonical_table(T_double)
    assert c_double not in classes
    classes[c_double] = False
    assert len(classes) == 16 and sum(classes.values()) == 4

    # Order four: directed one-edge and mutual-edge products.
    order_four = {}
    for a in (0, 1):
        for b in (0, 1):
            if not (a or b):
                continue
            arcs = set()
            if a: arcs.add((0, 1))
            if b: arcs.add((1, 0))
            T = make_semigroup(2, 1, {arc: 1 for arc in arcs})
            order_four[canonical_table(T)] = transitive(2, arcs)
    assert len(order_four) == 2 and sum(order_four.values()) == 1

    # Every nontransitive graph on at most 3 vertices falls into exactly
    # one of the three obstruction mechanisms in the proof.
    for mask in range(1, 64):
        arcs = edges_from_mask(3, mask)
        if transitive(3, arcs):
            continue
        mutual = {(u, v) for u, v in arcs if (v, u) in arcs}
        if mutual:
            if len(mutual) == 6:
                check_small_witness(arcs, symmetric_odd_wheel(2))
                check_small_witness(arcs, symmetric_odd_wheel(3))
            else:
                check_small_witness(arcs, symmetric_odd_cycle(2))
                check_small_witness(arcs, symmetric_odd_cycle(3))
        elif all((u, (u+1) % 3) in arcs for u in range(3)) or \
             all(((u+1) % 3, u) in arcs for u in range(3)):
            for n in (4, 5, 7):
                if n % 3:
                    check_small_witness(arcs, directed_cycle(n))
        else:
            assert len(arcs) == 2
            for k in (2, 3, 4):
                check_small_witness(arcs, signed_odd_cycle(k))

    # The order-six counterexample: transitivity fails, although its
    # product graph and the transitive 3-tournament are hom-equivalent.
    six = frozenset({(0, 1), (1, 2), (1, 3), (0, 3)})
    T6 = make_semigroup(4, 1, {arc: 1 for arc in six})
    assert len(T6) == 6 and not transitive(4, six)
    T3 = frozenset({(0, 1), (1, 2), (0, 2)})
    assert hom(4, six, 3, T3)
    assert hom(3, T3, 4, six)

    print('VERIFY_OK')
    print('order4_classes=2 order4_finitely_based=1')
    print('order5_classes=16 order5_finitely_based=4')
    print('order6_nontransitive_finitely_based_example=present')


if __name__ == '__main__':
    main()
