#!/usr/bin/env python3
"""Finite exact checks of a value-sensitive modal successor certificate theorem.

Pure standard Python, deterministic; checks are illustrations, not a proof of the
unbounded arity statement or NP-hardness reduction.
"""
import itertools


def downsets(n, lt):
    rel = set(lt) | {(i, i) for i in range(n)}
    return [frozenset(i for i in range(n) if bits & (1 << i))
            for bits in range(1 << n)
            if all(j not in frozenset(i for i in range(n) if bits & (1 << i))
                   or i in frozenset(i for i in range(n) if bits & (1 << i))
                   for i, j in rel)]


def boundary(n, lt, value):
    rel = set(lt) | {(i, i) for i in range(n)}
    return frozenset(p for p in range(n) if p not in value and
                     not any(q not in value and q != p and (q, p) in rel
                             for q in range(n)))


def meet(n, seq):
    result = frozenset(range(n))
    for s in seq:
        result = result & s
    return result


def minimum(n, data):
    # data is a list of successor tuples of down-sets
    q = len(data[0])
    target = [meet(n, [row[i] for row in data]) for i in range(q)]
    for r in range(len(data) + 1):
        for inds in itertools.combinations(range(len(data)), r):
            if all(meet(n, (data[v][i] for v in inds)) == target[i]
                   for i in range(q)):
                return r
    raise AssertionError('all successors should preserve all values')


def check_poset(label, n, order):
    rel = set(order) | {(i, i) for i in range(n)}
    assert all((a, c) in rel for a, b in rel for d, c in rel if b == d)
    values = downsets(n, order)
    assert values[0] == frozenset()
    exhaustive = 0
    for q in (1, 2):
        tuples = list(itertools.product(values, repeat=q))
        max_len = 3 if len(tuples) <= 16 else 2
        for length in range(1, max_len + 1):
            for data in itertools.product(tuples, repeat=length):
                targets = [meet(n, [row[i] for row in data]) for i in range(q)]
                bound = sum(len(boundary(n, order, m)) for m in targets)
                assert minimum(n, data) <= bound, (label, data, bound)
                # Boundary hypergraph is exact: each missing minimal generator
                # must be excluded by at least one retained successor.
                edges = [frozenset(v for v, row in enumerate(data) if b not in row[i])
                         for i, m in enumerate(targets)
                         for b in boundary(n, order, m)]
                assert all(edges)
                for mask in range(1 << length):
                    inds = [v for v in range(length) if (mask >> v) & 1]
                    good = all(meet(n, (data[v][i] for v in inds)) == targets[i]
                               for i in range(q))
                    hit = all(any(v in inds for v in edge) for edge in edges)
                    assert good == hit, (label, data, inds)
                exhaustive += 1
        # Sharp for every prescribed target tuple: build disjoint witnesses
        for targets in itertools.product(values, repeat=q):
            witnesses = []
            for i, m in enumerate(targets):
                for b in boundary(n, order, m):
                    omitted = frozenset(p for p in range(n) if (b, p) in rel)
                    row = [frozenset(range(n)) for _ in range(q)]
                    row[i] = frozenset(range(n)) - omitted
                    assert row[i] in values
                    witnesses.append(tuple(row))
            actual = [meet(n, (row[i] for row in witnesses)) for i in range(q)]
            assert tuple(actual) == targets, (label, targets, actual)
            if witnesses:
                assert minimum(n, witnesses) == len(witnesses), (label, targets)
            else:
                assert all(t == frozenset(range(n)) for t in targets)
    return label, len(values), exhaustive


def check_classical_reduction():
    # Hitting set {a,b}, {b,c}, {a,c}; singleton fails, pair works.
    edges = [{0, 1}, {1, 2}, {0, 2}]
    data = []
    for vertex in range(3):
        row = tuple(frozenset() if vertex in edge else frozenset({0})
                    for edge in edges)
        data.append(row)
    assert minimum(1, data) == 2


if __name__ == '__main__':
    posets = (
        ('chain3', 3, ((0, 1), (1, 2), (0, 2))),
        ('antichain3', 3, ()),
        ('v3', 3, ((0, 2), (1, 2))),
        ('diamond4', 4, ((0, 1), (0, 2), (1, 3), (2, 3), (0, 3))),
    )
    for p in posets:
        print('CHECK', *check_poset(*p))
    check_classical_reduction()
    print('VALUE_SENSITIVE_MODAL_CERTIFICATES_VERIFY_OK')
