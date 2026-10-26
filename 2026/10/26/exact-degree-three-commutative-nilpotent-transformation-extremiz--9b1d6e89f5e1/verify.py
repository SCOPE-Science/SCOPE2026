"""Exhaustive finite-transformation verification for degree-three commuting nilpotent extremizers.

Requires Python 3.10+ and networkx 3.x. Run: python verify.py
All maps are represented by their complete image tuples, with point 0 the fixed zero.
"""
from itertools import combinations, product
import networkx as nx

EXPECTED = {4: (16, 3, 6), 5: (101, 6, 24),
            6: (756, 12, 180), 7: (6607, 36, 360)}


def compose(f, g):
    return tuple(f[g[x]] for x in range(len(f)))


def cube_zero_maps(n):
    for tail in product(range(n), repeat=n-1):
        f = (0,) + tail
        if all(f[f[f[x]]] == 0 for x in range(n)):
            yield f


def construction(n, t, a, z, y, u):
    """The explicit two-layer family; a contains 0 and has length t."""
    assert len(a) == t and 0 in a and u in a and u != 0
    b = tuple(x for x in range(n) if x not in a)
    assert z in b and y in b and y != z
    flexible = tuple(x for x in b if x != z)
    base = set()
    for values in product(a, repeat=len(flexible)):
        f = [0] * n
        for x, v in zip(flexible, values):
            f[x] = v
        base.add(tuple(f))
    flexible2 = tuple(x for x in b if x not in (z, y))
    for values in product(a, repeat=len(flexible2)):
        f = [0] * n
        f[z] = u
        f[y] = z
        for x, v in zip(flexible2, values):
            f[x] = v
        base.add(tuple(f))
    return frozenset(base)


def constructed_extremizers(n, target):
    result = set()
    zero = (0,) * n
    for t in range(2, n-1):
        expected_size = (t+1)*t**(n-t-2)
        if expected_size != target:
            continue
        for other_a in combinations(range(1, n), t-1):
            a = (0,) + other_a
            b = tuple(x for x in range(n) if x not in a)
            for z in b:
                for y in b:
                    if y == z:
                        continue
                    for u in a[1:]:
                        s = construction(n, t, a, z, y, u)
                        assert len(s) == target
                        squares = set()
                        for f in s:
                            for g in s:
                                h = compose(f, g)
                                assert h == compose(g, f)
                                assert h in s
                                squares.add(h)
                        assert squares != {zero}
                        assert all(compose(h, f) == zero for h in squares for f in s)
                        result.add(s)
    return result


def verify(n):
    count, target, expected_extremizers = EXPECTED[n]
    maps = list(cube_zero_maps(n))
    assert len(maps) == count
    graph = nx.Graph()
    graph.add_nodes_from(range(len(maps)))
    for i, f in enumerate(maps):
        for j in range(i+1, len(maps)):
            g = maps[j]
            if all(f[g[x]] == g[f[x]] for x in range(n)):
                graph.add_edge(i, j)
    zero = (0,) * n
    extremizers = set()
    maximal_count = 0
    for cl in nx.find_cliques(graph):
        maximal_count += 1
        if len(cl) < target:
            continue
        nonnull = any(compose(maps[i], maps[i]) != zero for i in cl)
        if not nonnull:
            nonnull = any(compose(maps[i], maps[j]) != zero
                          for k, i in enumerate(cl) for j in cl[k+1:])
        if nonnull:
            assert len(cl) <= target, ('upper bound fails', n, len(cl))
            if len(cl) == target:
                extremizers.add(frozenset(maps[i] for i in cl))
    constructed = constructed_extremizers(n, target)
    assert len(extremizers) == expected_extremizers
    assert len(constructed) == expected_extremizers
    assert extremizers == constructed
    print('n=%d rooted_maps=%d commuting_edges=%d maximal_cliques=%d'
          ' class3_extremal_order=%d labelled_extremizers_per_root=%d'
          ' constructions_complete=YES'
          % (n, len(maps), graph.number_of_edges(), maximal_count,
             target, len(extremizers)), flush=True)


if __name__ == '__main__':
    for n in EXPECTED:
        verify(n)
    print('ALL_DEGREE_THREE_EXTREMAL_CHECKS_PASSED', flush=True)
