"""Independent finite transposition-quandle homomorphism census.

Run with Python 3.9+: python verify.py. No external dependencies.
The finite checks corroborate, but do not prove, the general theorem.
"""
from itertools import combinations
from collections import Counter
from math import comb, factorial


def transposition_quandle(n):
    edges = list(combinations(range(n), 2))
    locate = {e: i for i, e in enumerate(edges)}
    table = []
    for e in edges:
        row = []
        for a, b in edges:
            # Conjugate e by the transposition (a b).
            conjugate = tuple(sorted((b if x == a else a if x == b else x)
                                      for x in e))
            row.append(locate[conjugate])
        table.append(row)
    return edges, table


def census(n, m, keep_maps=False):
    """Exhaustive map enumeration using only the multiplication tables."""
    source, mult_s = transposition_quandle(n)
    target, mult_t = transposition_quandle(m)
    size_s, size_t = len(source), len(target)
    values = [-1] * size_s
    counts = Counter()
    maps = []

    def propagate(changes):
        again = True
        while again:
            again = False
            for i in range(size_s):
                if values[i] < 0:
                    continue
                for j in range(size_s):
                    if values[j] < 0:
                        continue
                    k = mult_s[i][j]
                    should = mult_t[values[i]][values[j]]
                    if values[k] == -1:
                        values[k] = should
                        changes.append(k)
                        again = True
                    elif values[k] != should:
                        return False
        return True

    def dfs():
        if -1 not in values:
            image_size = len(set(values))
            counts[image_size] += 1
            if keep_maps:
                maps.append(tuple(values))
            return
        index = values.index(-1)
        for output in range(size_t):
            values[index] = output
            changes = [index]
            if propagate(changes):
                dfs()
            for changed in changes:
                values[changed] = -1

    dfs()
    return counts, maps


def falling(m, n):
    return factorial(m) // factorial(m - n) if m >= n else 0


def prediction(n, m):
    result = Counter({1: comb(m, 2)})
    if n == 3:
        result[3] += 6 * comb(m, 3)
    elif n == 4:
        result[3] += 6 * comb(m, 3)
        result[6] += falling(m, 4)
    elif n >= 5:
        result[comb(n, 2)] += falling(m, n)
    return +result


def verify():
    tests = [(n, m) for n in range(3, 7) for m in range(2, 8)]
    tests += [(7, 7), (7, 8)]
    for n, m in tests:
        observed, _ = census(n, m)
        expected = prediction(n, m)
        assert +observed == expected, (n, m, observed, expected)

    _, rank_maps = census(4, 4, keep_maps=True)
    maps3 = [f for f in rank_maps if len(set(f)) == 3]
    assert len(maps3) == 24
    assert len({frozenset(f) for f in maps3}) == 4
    idempotents = [f for f in maps3 if tuple(f[f[i]] for i in range(6)) == f]
    assert len(idempotents) == 4
    # In the exceptional rank-3 ideal, the image of the left factor
    # is always the image of the composition.
    for f in maps3:
        for g in maps3:
            comp = tuple(f[g[i]] for i in range(6))
            assert len(set(comp)) == 3
            assert set(comp) == set(f)
    print("VERIFY_OK", len(tests), "independent source-target censuses;",
          "24 exceptional maps; 4 rank-3 idempotents; all 576 products")


if __name__ == "__main__":
    verify()
