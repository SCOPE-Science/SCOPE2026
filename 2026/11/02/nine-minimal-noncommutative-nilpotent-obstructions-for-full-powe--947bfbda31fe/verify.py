#!/usr/bin/env python3
"""Finite certificates for the five-element nilpotent power-semiring census.

No external packages are required. The finite-duality criterion is the
core-square dismantling theorem for finite relational structures.
"""
from itertools import product, permutations, combinations
from functools import lru_cache

V = (0, 1, 2)
ARCS = tuple((i, j) for i in V for j in V if i != j)


def canonical(arcs):
    return min(tuple(int((p[i], p[j]) in arcs) for i, j in ARCS)
               for p in permutations(V))


def graph(bits):
    return frozenset(edge for edge, flag in zip(ARCS, bits) if flag)


def core(arcs):
    # Exhaustively find the smallest induced retract of the directed graph.
    for size in range(1, 4):
        for U in combinations(V, size):
            complement = tuple(x for x in V if x not in U)
            for values in product(U, repeat=len(complement)):
                fold = dict(zip(complement, values))
                fold.update({u: u for u in U})
                if all((fold[a], fold[b]) in arcs for a, b in arcs):
                    return frozenset(U), frozenset((a, b) for a, b in arcs
                                                 if a in U and b in U)
    raise AssertionError('Every finite digraph has a core')


def finite_duality(arcs):
    U, c = core(arcs)
    pairs = frozenset(product(U, repeat=2))
    diagonal = frozenset((u, u) for u in U)
    @lru_cache(None)
    def dismantles(state):
        if state == diagonal:
            return True
        edges = frozenset(((a, b), (u, v))
                          for a, b in state for u, v in state
                          if (a, u) in c and (b, v) in c)
        inbound = {x: frozenset(u for u, v in edges if v == x) for x in state}
        outbound = {x: frozenset(v for u, v in edges if u == x) for x in state}
        for x in state - diagonal:
            for y in state - {x}:
                if inbound[x] <= inbound[y] and outbound[x] <= outbound[y]:
                    if dismantles(state - {x}):
                        return True
        return False
    return dismantles(pairs)


def semigroup_table(arcs):
    # On {a,b,c,t,0}: xy=t exactly on the selected directed arcs.
    tab = [[4] * 5 for _ in range(5)]
    for i, j in arcs:
        tab[i][j] = 3
    return tab


def associative(tab):
    n = len(tab)
    return all(tab[tab[i][j]][k] == tab[i][tab[j][k]]
               for i, j, k in product(range(n), repeat=3))


def classify_digraphs():
    representatives = {}
    totals = {'FB_noncomm': 0, 'NFB_noncomm': 0,
              'FB_comm': 0, 'NFB_comm': 0}
    for mask in product((0, 1), repeat=6):
        A = graph(mask)
        if not A:
            continue
        key = canonical(A)
        representatives.setdefault(key, graph(key))
        symmetric = all(((j, i) in A) == ((i, j) in A) for i, j in ARCS)
        fd = finite_duality(A)
        totals[('FB' if fd else 'NFB') + ('_comm' if symmetric else '_noncomm')] += 1
        assert associative(semigroup_table(A))
    assert len(representatives) == 15
    assert totals == {'FB_noncomm': 18, 'NFB_noncomm': 38,
                      'FB_comm': 0, 'NFB_comm': 7}, totals
    nfb_types = []
    fb_types = []
    for key, A in sorted(representatives.items()):
        symmetric = all(((j, i) in A) == ((i, j) in A) for i, j in ARCS)
        fd = finite_duality(A)
        if not symmetric:
            (fb_types if fd else nfb_types).append(''.join(map(str, key)))
    assert len(fb_types) == 4 and len(nfb_types) == 8
    print('three-generator case: 15 nonempty digraph types')
    print('noncommutative, finitely based:', ','.join(fb_types))
    print('noncommutative, nonfinitely based:', ','.join(nfb_types))
    print('labeled support digraph totals:', totals)
    return nfb_types


def classify_index_four():
    # Every order-five index-four semigroup with two generators admits
    # a stratification {a,b}|{c}|{d}|{0}. Products in the layers must
    # respect the filtration S^i S^j subset S^(i+j).
    count = 0
    for top in product((2, 3, 4), repeat=4):
        for mixed in product((3, 4), repeat=4):
            tab = [[4] * 5 for _ in range(5)]
            for (i, j), x in zip(product((0, 1), repeat=2), top):
                tab[i][j] = x
            for (i, j), x in zip(((0, 2), (1, 2), (2, 0), (2, 1)), mixed):
                tab[i][j] = x
            if not associative(tab):
                continue
            square = {tab[i][j] for i, j in product(range(5), repeat=2)}
            cube = {tab[tab[i][j]][k] for i, j, k in product(range(5), repeat=3)}
            if square != {2, 3, 4} or cube != {3, 4}:
                continue
            if all(tab[i][j] == tab[j][i] for i, j in product(range(5), repeat=2)):
                continue
            count += 1
            assert tab[tab[0][0]][0] == 3 or tab[tab[1][1]][1] == 3
    print('index-four, noncommutative, labeled-layer tables:', count)
    assert count == 8


def check_second_shape():
    # Unique two-generator case with two nonzero output values.
    tab = [[4] * 5 for _ in range(5)]
    tab[0][1], tab[1][0] = 2, 3
    assert associative(tab)
    # The nonzero product support is the bidirected 2-edge core.
    # Its square cannot dismantle to the diagonal.
    assert not finite_duality(frozenset({(0, 1), (1, 0)}))
    print('two-generator two-output type: one NFB isomorphism class')


if __name__ == '__main__':
    t = classify_digraphs()
    classify_index_four()
    check_second_shape()
    print('TOTAL_MINIMAL_NONCOMMUTATIVE_NFB_CLASSES:', len(t) + 1)
    print('VERIFY_OK')
