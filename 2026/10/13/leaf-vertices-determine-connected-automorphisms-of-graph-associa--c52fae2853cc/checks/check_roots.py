"""Exact finite regression tests for Demazure roots of graph-associahedral fans.

The infinite statement follows from the accompanying symbolic proof; the
bounded enumeration here only tests ray lists and their inequalities.
"""
from itertools import combinations, product


def connected(n, edges, selected):
    if not selected:
        return False
    visited = {min(selected)}
    while True:
        added = {b if a in visited else a for a, b in edges
                 if (a in visited) != (b in visited)
                 and a in selected and b in selected}
        nxt = visited | added
        if nxt == visited:
            break
        visited = nxt
    return len(visited) == len(selected)


def test_graph(n, edges):
    v = set(range(n))
    if not connected(n, edges, v):
        return False
    tubes = []
    for mask in range(1, (1 << n) - 1):
        selected = {i for i in range(n) if (mask >> i) & 1}
        if connected(n, edges, selected):
            tubes.append(selected)
    assert all({i} in tubes for i in range(n))
    degrees = [sum(i in e for e in edges) for i in range(n)]
    all_a = ((tuple(((-1 if i == neg else 1 if i == pos else 0))
                    for i in range(n)), neg, pos)
             for neg in range(n) for pos in range(n) if neg != pos)
    roots = []
    for a, neg, pos in all_a:
        pairings = [sum(a[i] for i in t) for t in tubes]
        if pairings.count(-1) == 1 and all(x >= 0 for x in pairings if x != -1):
            roots.append((neg, pos))
    predicted = {(i, next(j for j in range(n) if frozenset((i,j)) in edges))
                 for i in range(n) if degrees[i] == 1}
    if set(roots) != predicted:
        raise AssertionError((n, edges, roots, predicted))
    for i, j in roots:
        for k, l in roots:
            if i != k and (j == k or l == i):
                raise AssertionError('Unexpected root derivation interaction')
    return True


def main():
    totals = {}
    with_roots = {}
    for n in range(3, 6):
        complete = [frozenset(e) for e in combinations(range(n), 2)]
        total = rooted = 0
        for mask in range(1 << len(complete)):
            edges = {complete[i] for i in range(len(complete)) if (mask >> i) & 1}
            if test_graph(n, edges):
                total += 1
                rooted += int(any(sum(i in e for e in edges) == 1 for i in range(n)))
        totals[n], with_roots[n] = total, rooted
    assert totals == {3: 4, 4: 38, 5: 728}
    print('CONNECTED_GRAPHS', totals)
    print('WITH_LEAF_ROOTS', with_roots)
    print('ALL_GRAPH_ROOT_AND_COMMUTATOR_CHECKS_PASS', sum(totals.values()))

if __name__ == '__main__':
    main()
