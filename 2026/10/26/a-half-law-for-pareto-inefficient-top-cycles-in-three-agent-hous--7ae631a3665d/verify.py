#!/usr/bin/env python3
"""Finite certificate for the three-agent top-cycle and efficiency law.

Uses only Python's standard library; execute: python3 verify.py
"""
from collections import Counter
from itertools import permutations, product

ORDERS = tuple(permutations(range(3)))
ASSIGNMENTS = ORDERS


def relation(profile):
    """A[i][j]: assignment i weakly defeats assignment j.

    B[i][j]: assignment i strictly defeats assignment j.
    """
    ranks = tuple(tuple(order.index(h) for h in range(3)) for order in profile)
    a = [[False] * 6 for _ in range(6)]
    b = [[False] * 6 for _ in range(6)]
    for i, x in enumerate(ASSIGNMENTS):
        for j, y in enumerate(ASSIGNMENTS):
            margin = sum(
                (ranks[t][x[t]] < ranks[t][y[t]])
                - (ranks[t][x[t]] > ranks[t][y[t]])
                for t in range(3)
            )
            a[i][j] = margin >= 0
            b[i][j] = margin > 0
    for i in range(6):
        for j in range(6):
            if i != j:
                assert a[i][j] or a[j][i]
                assert b[i][j] == (a[i][j] and not a[j][i])
    return ranks, a, b


def measure_direct(profile):
    ranks, weak, strict = relation(profile)
    reach = [row[:] for row in weak]
    for h in range(6):
        for i in range(6):
            for j in range(6):
                reach[i][j] = reach[i][j] or (reach[i][h] and reach[h][j])
    tc = frozenset(i for i in range(6) if all(reach[i]))

    po = frozenset(
        i for i, x in enumerate(ASSIGNMENTS)
        if not any(
            all(ranks[t][y[t]] <= ranks[t][x[t]] for t in range(3))
            and any(ranks[t][y[t]] < ranks[t][x[t]] for t in range(3))
            for y in ASSIGNMENTS
        )
    )

    covers = [[False] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            if not strict[i][j]:
                continue
            bordes = all(not strict[j][k] or strict[i][k] for k in range(6))
            gillies = all(not strict[k][i] or strict[k][j] for k in range(6))
            covers[i][j] = bordes and gillies
    uc = frozenset(i for i in range(6) if not any(covers[j][i] for j in range(6)))
    return tc, po, uc


def measure_independent(profile):
    ranks, weak, strict = relation(profile)
    # Independent cycle detection: each vertex in the source SCC of the
    # semicomplete majority digraph is in the top cycle.
    reachable = []
    for start in range(6):
        seen = {start}
        todo = [start]
        while todo:
            i = todo.pop()
            for j in range(6):
                if weak[i][j] and j not in seen:
                    seen.add(j)
                    todo.append(j)
        reachable.append(seen)
    tc = frozenset(i for i in range(6) if len(reachable[i]) == 6)

    # Pareto efficiency equals the set of serial-dictatorship allocations.
    sd = set()
    for priority in permutations(range(3)):
        remaining = set(range(3))
        assignment = [None] * 3
        for t in priority:
            chosen = min(remaining, key=lambda h: ranks[t][h])
            assignment[t] = chosen
            remaining.remove(chosen)
        sd.add(ASSIGNMENTS.index(tuple(assignment)))
    po = frozenset(sd)

    # Independent form of the McKelvey uncovered set: weak reachability
    # within two edges, at least one of the edges being strict.
    uc = frozenset(i for i in range(6) if all(
        i == j or weak[i][j] or (
            any((strict[i][k] and weak[k][j]) or
                (weak[i][k] and strict[k][j]) for k in range(6))
        ) for j in range(6)))
    return tc, po, uc


def label(order):
    return ''.join(str(c + 1) for c in order)


def check_two_agent_boundary():
    houses = (0, 1)
    assignments = ((0, 1), (1, 0))
    for preferences in product(permutations(houses), repeat=2):
        ranks = tuple(tuple(order.index(h) for h in houses) for order in preferences)
        margins = []
        for x, y in ((assignments[0], assignments[1]),):
            margins.append(sum(
                (ranks[t][x[t]] < ranks[t][y[t]]) -
                (ranks[t][x[t]] > ranks[t][y[t]]) for t in range(2)))
        margin = margins[0]
        top = {0, 1} if margin == 0 else ({0} if margin > 0 else {1})
        pareto = {0, 1}
        if all(ranks[t][assignments[0][t]] < ranks[t][assignments[1][t]] for t in range(2)):
            pareto = {0}
        elif all(ranks[t][assignments[1][t]] < ranks[t][assignments[0][t]] for t in range(2)):
            pareto = {1}
        assert top == pareto


def main():
    check_two_agent_boundary()
    joint = Counter()
    canonical = []
    total = 0
    for pref in product(ORDERS, repeat=3):
        tc, po, uc = measure_direct(pref)
        other = measure_independent(pref)
        assert (tc, po, uc) == other, (pref, (tc, po, uc), other)
        assert uc <= po <= tc
        joint[(len(tc), len(po), len(uc))] += 1
        total += 1
        if pref[0] == ORDERS[0]:
            canonical.append((pref[1], pref[2], len(tc), len(po), len(uc)))
    assert total == 216 and len(canonical) == 36
    expected = Counter({
        (1, 1, 1): 48,
        (2, 2, 2): 36,
        (4, 3, 2): 36,
        (4, 4, 2): 18,
        (6, 3, 2): 36,
        (6, 4, 2): 36,
        (6, 6, 6): 6,
    })
    assert joint == expected, (joint, expected)
    # The non-Pareto-efficient part of the top cycle.
    excess = Counter({0: 108, 1: 36, 2: 36, 3: 36})
    assert Counter({d: sum(n for (t, p, u), n in joint.items() if t - p == d)
                    for d in range(4)}) == excess
    assert sum((t-p)*n for (t,p,u), n in joint.items()) == 216
    canonical_matrix = []
    for p2 in ORDERS:
        row = []
        for p3 in ORDERS:
            entry = next(x for x in canonical if x[0] == p2 and x[1] == p3)
            row.append((entry[2], entry[3], entry[4]))
        canonical_matrix.append(row)
    assert Counter((t,p,u) for row in canonical_matrix for t,p,u in row) == Counter({k:v//6 for k,v in expected.items()})
    print('ORDER:', *map(label, ORDERS))
    print('TOP CYCLE / PARETO / McKELVEY UNCOVERED canonical cells:')
    for order,row in zip(ORDERS,canonical_matrix):
        print(label(order), ' '.join(''.join(map(str,cell)) for cell in row))
    print('JOINT PROFILE COUNTS:', dict(sorted(joint.items())))
    print('EXCESS DISTRIBUTION:',dict(sorted(excess.items())))
    print('P(TC contains dominated)=1/2, E[# dominated in TC]=1')
    print('All 216 direct and independently reconstructed cases agree.')

if __name__ == '__main__':
    main()
