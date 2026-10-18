#!/usr/bin/env python3
"""Independent finite checks for one-point order-extension extremal bounds.
Run with Python 3.10 or later; no dependencies beyond the standard library.
"""
from itertools import product


def all_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for choices in product((-1, 0, 1), repeat=len(pairs)):
        relation = set()
        for (i, j), orientation in zip(pairs, choices):
            if orientation == 1:
                relation.add((i, j))
            elif orientation == -1:
                relation.add((j, i))
        if all((i, k) in relation for i, j in relation for h, k in relation if j == h and i != k):
            yield frozenset(relation)


def extension_count(n, relation):
    count = 0
    for coloring in product((0, 1, 2), repeat=n):
        below = [i for i, code in enumerate(coloring) if code == 1]
        above = [i for i, code in enumerate(coloring) if code == 2]
        # Below x must be a down-set; above x must be an up-set.
        if any((coloring[j] == 1 and coloring[i] != 1)
               or (coloring[i] == 2 and coloring[j] != 2)
               for i, j in relation):
            continue
        # In an extension, each old element below x precedes each above x.
        if any((i, j) not in relation for i in below for j in above):
            continue
        count += 1
    return count


def independent_closure_check(n, relation):
    # Separate method: explicitly insert x, then test whether the transitive
    # closure changes the preexisting induced order or makes a cycle.
    accepted = 0
    for coloring in product((0, 1, 2), repeat=n):
        reach = [[False] * (n + 1) for _ in range(n + 1)]
        for i, j in relation:
            reach[i][j] = True
        for i, code in enumerate(coloring):
            if code == 1:
                reach[i][n] = True
            if code == 2:
                reach[n][i] = True
        for k in range(n + 1):
            for i in range(n + 1):
                if reach[i][k]:
                    for j in range(n + 1):
                        if reach[k][j]:
                            reach[i][j] = True
        if any(reach[i][i] for i in range(n + 1)):
            continue
        if any(reach[i][j] != ((i, j) in relation)
               for i in range(n) for j in range(n) if i != j):
            continue
        if any(reach[i][n] != (coloring[i] == 1) or reach[n][i] != (coloring[i] == 2)
               for i in range(n)):
            continue
        accepted += 1
    return accepted


def main():
    known_labeled_posets = {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231}
    for n in range(1, 6):
        seen = 0
        equality = 0
        maximum = 0
        for relation in all_posets(n):
            seen += 1
            actual = extension_count(n, relation)
            if n <= 4:
                assert actual == independent_closure_check(n, relation)
            if not relation:
                assert actual == 2 ** (n + 1) - 1
            else:
                assert actual <= 3 * 2 ** (n - 1)
                if actual == 3 * 2 ** (n - 1):
                    equality += 1
            maximum = max(maximum, actual)
        assert seen == known_labeled_posets[n], (n, seen)
        assert maximum == 2 ** (n + 1) - 1
        print(f'n={n}: labeled_posets={seen}, global_maximum={maximum}, nonantichain_extremizers={equality}')
    # Verify the one-point doubling lemma and its unique triple fiber.
    # Enumerate every labeled 5-point poset with an order relation among
    # its first four vertices, treating the fifth vertex as newly adjoined.
    inspected = 0
    for relation in all_posets(5):
        base = frozenset((i, j) for i, j in relation if i < 4 and j < 4)
        if not base:
            continue
        fibers = {}
        for coloring in product((0, 1, 2), repeat=5):
            below = [i for i, code in enumerate(coloring) if code == 1]
            above = [i for i, code in enumerate(coloring) if code == 2]
            if any((coloring[j] == 1 and coloring[i] != 1) or
                   (coloring[i] == 2 and coloring[j] != 2) for i, j in relation):
                continue
            if any((i, j) not in relation for i in below for j in above):
                continue
            trace = coloring[:4]
            fibers[trace] = fibers.get(trace, 0) + 1
        assert max(fibers.values()) == 3
        assert list(fibers.values()).count(3) == 1
        assert list(fibers.values()).count(1) >= 1
        assert sum(fibers.values()) <= 2 * extension_count(4, base)
        inspected += 1
    print(f"verified doubling-fiber lemma on {inspected} labeled five-point posets")
    for n in range(2, 10):
        singleton_relation = {(0, 1)}
        star_relation = {(0, k) for k in range(1, n)}
        for relation in (singleton_relation, star_relation):
            actual = extension_count(n, relation)
            assert actual == 3 * 2 ** (n - 1), (n, actual)
    print('PASS: independent closure checks through four points; complete labeled census through five; extremizers through nine')

if __name__ == '__main__':
    main()
