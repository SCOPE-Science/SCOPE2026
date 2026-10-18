#!/usr/bin/env python3
"""Self-contained verification of a one-point-extension count comparison for finite posets."""
from itertools import combinations, permutations, product
from collections import defaultdict


def transitive_closure(edges, n):
    reach = [[False] * n for _ in range(n)]
    for i, j in edges:
        if i == j:
            return None
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    if any(reach[i][i] for i in range(n)):
        return None
    return frozenset((i, j) for i in range(n) for j in range(n) if reach[i][j])


def all_posets(n):
    items = {frozenset()}
    for i, j in combinations(range(n), 2):
        new = set()
        for edges in items:
            for case in ((), ((i, j),), ((j, i),)):
                C = transitive_closure(edges.union(case), n)
                if C is not None:
                    new.add(C)
        items = new
    return items


def count_extensions(edges, n):
    # 0 := old point below the new point; 1 := incomparable; 2 := old point above.
    total = 0
    for states in product(range(3), repeat=n):
        E = set(edges)
        for i, s in enumerate(states):
            if s == 0:
                E.add((i, n))
            elif s == 2:
                E.add((n, i))
        if transitive_closure(E, n + 1) == frozenset(E):
            total += 1
    return total


def canonical_pair(p, q, n):
    return min((tuple(sorted((v[i], v[j]) for i, j in p)),
                tuple(sorted((v[i], v[j]) for i, j in q)))
               for v in permutations(range(n)))


def first_failure():
    expected = {1: 1, 2: 3, 3: 19, 4: 219}
    for n in range(1, 5):
        posets = all_posets(n)
        assert len(posets) == expected[n], (n, len(posets))
        counts = {p: count_extensions(p, n) for p in posets}
        failures = defaultdict(list)
        changes = 0
        for p in posets:
            for x in range(n):
                for y in range(n):
                    if x == y or (x, y) in p or (y, x) in p:
                        continue
                    q = transitive_closure(p.union(((x, y),)), n)
                    if q is None:
                        continue
                    changes += 1
                    if counts[q] > counts[p]:
                        failures[canonical_pair(p, q, n)].append((counts[p], counts[q]))
        if n < 4:
            assert not failures, (n, failures)
            print(f"n={n}: {len(posets)} labeled posets, {changes} comparisons, no increase")
        else:
            assert len(failures) == 6 and sum(map(len, failures.values())) == 120
            summary = sorted((len(v), v[0][0], v[0][1]) for v in failures.values())
            assert summary == [(12, 22, 24), (12, 22, 24),
                               (24, 18, 19), (24, 18, 19),
                               (24, 19, 20), (24, 20, 22)], summary
            print(f"n=4: {len(posets)} labeled posets, {changes} comparisons, 120 increases in 6 orbits")
            for (p, q), cases in sorted(failures.items(), key=lambda e:(e[1][0],e[0])):
                print(f"  multiplicity={len(cases)}: {cases[0][0]} -> {cases[0][1]}; P={p}, Q={q}")


def biclique_gap():
    for a in range(1, 5):
        for b in range(1, 5):
            n = a + b
            full = frozenset((i, a+j) for i in range(a) for j in range(b))
            almost = full - {(0, a)}
            cfull = count_extensions(full, n)
            cmiss = count_extensions(almost, n)
            assert cfull == 2**n + 2**a + 2**b - 2, (a,b,cfull)
            assert cmiss == 3 * 2**(n-2) + 2**a + 2**b, (a,b,cmiss)
            assert cfull - cmiss == 2**(n-2)-2, (a,b)
            print(f"a={a}, b={b}: missing={cmiss}, complete={cfull}, gain={cfull-cmiss}")


if __name__ == '__main__':
    first_failure()
    biclique_gap()
    print('PASS: all independently generated finite checks')
