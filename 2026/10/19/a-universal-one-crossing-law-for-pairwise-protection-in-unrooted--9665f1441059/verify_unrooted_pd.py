#!/usr/bin/env python3
"""Exact finite checks of a phylogenetic-diversity protection identity.

All general assertions are proved separately; finite enumeration checks the
edge-event algebra and the displayed examples rather than infinity.
"""
from fractions import Fraction as F
from itertools import combinations


def partitions(n, edges):
    adjacency = {}
    for i, (a, b, _) in enumerate(edges):
        adjacency.setdefault(a, []).append((b, i))
        adjacency.setdefault(b, []).append((a, i))
    output = []
    for omit, (a, _, length) in enumerate(edges):
        visited = {a}
        todo = [a]
        while todo:
            u = todo.pop()
            for v, edge_id in adjacency[u]:
                if edge_id != omit and v not in visited:
                    visited.add(v)
                    todo.append(v)
        side = frozenset(j for j in range(n) if j in visited)
        other = frozenset(range(n)) - side
        assert side and other
        output.append((side, other, F(length)))
    return output


def exact_pd(survivors, splits):
    return sum((length for a, b, length in splits
                if a.intersection(survivors) and b.intersection(survivors)), F(0))


def independent_enumeration(n, splits, guaranteed, q):
    remaining = [i for i in range(n) if i not in guaranteed]
    total = F(0)
    for mask in range(1 << len(remaining)):
        survivors = set(guaranteed)
        weight = F(1)
        for k, leaf in enumerate(remaining):
            if mask >> k & 1:
                survivors.add(leaf)
                weight *= 1 - q[leaf]
            else:
                weight *= q[leaf]
        total += weight * exact_pd(survivors, splits)
    return total


def edge_expectation(splits, guaranteed, q):
    total = F(0)
    for a, b, length in splits:
        qa = F(0) if guaranteed.intersection(a) else product(q[i] for i in a)
        qb = F(0) if guaranteed.intersection(b) else product(q[i] for i in b)
        total += length * (1 - qa) * (1 - qb)
    return total


def product(iterable):
    ans = F(1)
    for item in iterable:
        ans *= item
    return ans


def pair_hessian(n, splits, x, y, q):
    def V(s):
        return independent_enumeration(n, splits, s, q)
    return V({x, y}) - V({x}) - V({y}) + V(set())


def pair_formula(n, splits, x, y, q):
    Q = product(q)
    full_length = sum((length for _, _, length in splits), F(0))
    penalty = F(0)
    for a, b, length in splits:
        if x in a and y in a:
            away = b
        elif x in b and y in b:
            away = a
        else:
            continue
        penalty += length / product(q[i] for i in away)
    return Q * (full_length - penalty)


def verify():
    networks = [
        (3, [(3, 0, 1), (3, 1, 1), (3, 2, 1)]),
        (5, [(5, 0, 2), (5, 1, 3), (5, 6, 5),
             (6, 2, 7), (6, 7, 11), (7, 3, 13), (7, 4, 17)]),
    ]
    checked_edge = checked_hess = checked_anchor = 0
    for n, edges in networks:
        splits = partitions(n, edges)
        risk_profiles = [[F(1, 3)] * n,
                         [F(i + 1, i + 3) for i in range(n)],
                         [F(3, 4)] * n]
        for risks in risk_profiles:
            for bits in range(1 << n):
                S = {i for i in range(n) if (bits >> i) & 1}
                assert independent_enumeration(n, splits, S, risks) == edge_expectation(splits, S, risks)
                checked_edge += 1
            for x, y in combinations(range(n), 2):
                assert pair_hessian(n, splits, x, y, risks) == pair_formula(n, splits, x, y, risks)
                checked_hess += 1
            for anchor in range(n):
                candidates = [i for i in range(n) if i != anchor]
                for x, y in combinations(candidates, 2):
                    remaining = [i for i in candidates if i not in (x, y)]
                    for bits in range(1 << len(remaining)):
                        S = {anchor} | {i for j, i in enumerate(remaining) if bits >> j & 1}
                        V = lambda T: independent_enumeration(n, splits, T, risks)
                        d = V(S | {x, y}) - V(S | {x}) - V(S | {y}) + V(S)
                        assert d <= 0
                        checked_anchor += 1
    n, edges = networks[0]
    splits = partitions(n, edges)
    for q, expected in [(F(1, 4), -F(1, 64)),
                        (F(1, 3), F(0)),
                        (F(1, 2), F(1, 8))]:
        assert pair_hessian(n, splits, 0, 1, [q] * n) == expected
    n, edges = networks[1]
    splits = partitions(n, edges)
    previous = None
    weights = [1, 2, 1, 3, 2]
    for t in (F(1, 5), F(2, 5), F(3, 5), F(4, 5)):
        q = [t ** w for w in weights]
        h = pair_hessian(n, splits, 0, 3, q)
        normalized = h / product(q)
        if previous is not None:
            assert normalized > previous
        previous = normalized
    print('VERIFY_OK edge_probabilities=%s pair_hessians=%s anchored_margins=%s homogeneous_three_leaf_threshold=1/3 heterogeneous_normalized_increase=PASS' %
          (checked_edge, checked_hess, checked_anchor))


if __name__ == '__main__':
    verify()
