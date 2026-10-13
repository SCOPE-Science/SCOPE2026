"""Exact certificate for first failure of domination-polynomial log concavity
on trivially perfect graphs. Standard library only. All polynomials use
coefficient tuples in increasing powers, and all computations use integers.
"""
from collections import Counter
from functools import lru_cache
from itertools import product, combinations
from math import comb


def multiply(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return tuple(r)


def plus(a, b):
    return tuple((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))


def defects(p):
    return [(i, p[i] * p[i] - p[i - 1] * p[i + 1])
            for i in range(1, len(p) - 1)
            if p[i] * p[i] < p[i - 1] * p[i + 1]]


@lru_cache(None)
def partitions(n, floor=1):
    if not n:
        return ((),)
    return tuple((a,) + q for a in range(floor, n + 1)
                 for q in partitions(n - a, a))


def polysets():
    """Inductively construct EVERY distinct domination polynomial in the class.
    Trivially perfect graphs are exactly the graphs built by isolated union
    and a new universal vertex. connected[n] is the universal-vertex case.
    """
    allp = {0: {(1,)}, 1: {(0, 1)}}
    connected = {1: {(0, 1)}}
    totals = []
    for n in range(2, 16):
        # Generate disconnected polynomials. Multiplicity of an isomorphism
        # type is irrelevant: the theorem concerns *distinct polynomials*.
        disconnected = set()
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            for ps in product(*(connected[k] for k in parts)):
                out = (1,)
                for p in ps:
                    out = multiply(out, p)
                disconnected.add(out)
        # If the universal vertex is selected, the remaining n-1 choices
        # are arbitrary. If it is excluded, its predecessor must dominate.
        universal = (0,) + tuple(comb(n - 1, j)
                                  for j in range(n))
        connected[n] = {plus(p, universal) for p in allp[n - 1]}
        allp[n] = disconnected | connected[n]
        assert all(len(p) == n + 1 for p in allp[n])
        fail = [(p, defects(p)) for p in allp[n] if defects(p)]
        assert not fail, (n, fail[:2])
        totals.append((n, len(connected[n]), len(allp[n])))
        print(f"order={n} connected_polynomials={len(connected[n])} "
              f"all_polynomials={len(allp[n])} LC_failures=0", flush=True)
    universal_16 = (0,) + tuple(comb(15, j) for j in range(16))
    connected16 = {plus(p, universal_16) for p in allp[15]}
    violations = [(p, defects(p)) for p in connected16 if defects(p)]
    assert len(connected16) == 230337
    assert len(violations) == 1, violations[:2]
    return totals, allp, connected16, violations


def independent_direct_windmill(t, m):
    """Independently enumerate graph-level dominating subsets for W(t,m)."""
    v = t * m + 1
    adj = [((1 << v) - 1) ^ 1]
    for i in range(t):
        blade = sum(1 << (1 + i * m + j) for j in range(m))
        for j in range(m):
            x = 1 + i * m + j
            adj.append((1 | (blade ^ (1 << x))))
    assert len(adj) == v
    closed = [m | (1 << i) for i, m in enumerate(adj)]
    target = (1 << v) - 1
    coeffs = [0] * (v + 1)
    for S in range(1 << v):
        dominated = 0
        for i in range(v):
            if (S >> i) & 1:
                dominated |= closed[i]
        if dominated == target:
            coeffs[S.bit_count()] += 1
    return tuple(coeffs)


def direct_labeled_graph_crosscheck(polynomial_sets):
    """Independent graph-level enumeration for every labelled graph n<=5.
    Recognize the class by forbidden induced P4/C4, not by recursion.
    """
    counts = []
    for n in range(1, 6):
        edges = tuple(combinations(range(n), 2))
        observed = set()
        tp_graphs = 0
        for g in range(1 << len(edges)):
            adj = [0] * n
            for k, (a, b) in enumerate(edges):
                if (g >> k) & 1:
                    adj[a] |= 1 << b
                    adj[b] |= 1 << a
            ok = True
            for Q in combinations(range(n), 4):
                deg = [sum((adj[v] >> w) & 1 for w in Q if w != v)
                       for v in Q]
                if sorted(deg) == [2, 2, 2, 2] or sorted(deg) == [1, 1, 2, 2]:
                    ok = False
                    break
            if not ok:
                continue
            tp_graphs += 1
            poly = [0] * (n + 1)
            for S in range(1 << n):
                covered = S
                for v in range(n):
                    if (S >> v) & 1:
                        covered |= adj[v]
                if covered == (1 << n) - 1:
                    poly[S.bit_count()] += 1
            p = tuple(poly)
            assert p in polynomial_sets[n], (n, g, p)
            observed.add(p)
        assert observed == polynomial_sets[n], (n, len(observed), len(polynomial_sets[n]))
        counts.append((n, tp_graphs, len(observed)))
        print(f"independent_all_labeled_graphs_order={n} "
              f"trivially_perfect_labeled={tp_graphs} distinct_polynomials={len(observed)}", flush=True)
    return counts


def main():
    totals, allp, connected16, violations = polysets()
    direct_labeled_graph_crosscheck(allp)
    expected_counts = [2, 4, 9, 20, 48, 115, 284, 713, 1821,
                       4701, 12283, 32374, 86063, 230337]
    assert [r[2] for r in totals] == expected_counts
    t, m = 3, 5
    # Formula for W(3,5) is known independently in earlier literature.
    blade = tuple(comb(m, j) for j in range(m + 1))
    blade = (0,) + blade[1:]
    term = (1,)
    for _ in range(t):
        term = multiply(term, blade)
    central = (0,) + tuple(comb(t * m, j) for j in range(t * m + 1))
    windmill = plus(term, central)
    direct = independent_direct_windmill(t, m)
    assert windmill == direct == violations[0][0]
    assert violations[0][1] == [(2, -5)], violations[0][1]
    assert len(connected16) == 230337
    # In the worst-order connected case, only ONE distinct coefficient
    # sequence fails LC. Any disconnected instance is a convolution of
    # smaller log-concave, gap-free coefficient sequences and remains LC.
    print(f"order=16 connected_polynomials={len(connected16)} LC_failures=1")
    print("unique_order16_violating_polynomial=", windmill)
    print("violating_inequalities=", violations[0][1])
    print("direct_graph_subsets_examined=", 2**16)
    print("orders_0_through_15_all_logconcave=True")
    print("disconnected_order16_logconcave_by_convolution=True")
    print("ALL CHECKS PASSED")


if __name__ == '__main__':
    main()
