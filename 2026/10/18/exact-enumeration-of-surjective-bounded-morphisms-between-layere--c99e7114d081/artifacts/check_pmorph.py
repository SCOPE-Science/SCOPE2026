"""Finite exhaustive tests for counting surjective bounded morphisms.

All posets are ordinal sums of nonempty antichains. This script uses
only the Python standard library. It is not an infinite-proof checker.
"""

from functools import lru_cache
from itertools import product
from math import comb


def onto(n, q):
    """Surjections from an n-set onto q labeled elements."""
    return sum((-1) ** r * comb(q, r) * (q - r) ** n
               for r in range(q + 1))


def partial_onto(n, q):
    """Maps to q required values and one optional value, all required hit."""
    return sum((-1) ** r * comb(q, r) * (q + 1 - r) ** n
               for r in range(q + 1))


def recurrence(source, target):
    """Formula for the number of surjective upper-back morphisms."""
    h, k = len(source), len(target)
    f = [[0] * (k + 1) for _ in range(h + 1)]
    g = [[0] * (k + 1) for _ in range(h + 1)]
    f[0][0] = 1
    for j in range(1, k + 1):
        q = target[j - 1]
        prefix = 0
        for i in range(1, h + 1):
            n = source[i - 1]
            if q > 1:
                f[i][j] = onto(n, q) * f[i - 1][j - 1]
                g[i][j] = partial_onto(n, q) * f[i - 1][j - 1]
            else:
                if j == 1:
                    f[i][j] = 1
                else:
                    f[i][j] = prefix
                g[i][j] = (2 ** n - 1) * f[i][j]
            prefix += g[i][j - 1]
    return f[h][k]


def exhaustive(source, target):
    """Enumerate ALL set maps; check both order and p-morphism equations."""
    src = [lev for lev, size in enumerate(source) for _ in range(size)]
    dst = [lev for lev, size in enumerate(target) for _ in range(size)]
    sa, sb = len(src), len(dst)
    up_src = [{v for v in range(sa) if u == v or src[u] < src[v]}
              for u in range(sa)]
    up_dst = [{v for v in range(sb) if u == v or dst[u] < dst[v]}
              for u in range(sb)]
    total = 0
    for values in product(range(sb), repeat=sa):
        if len(set(values)) != sb:
            continue
        if all({values[v] for v in up_src[u]} == up_dst[values[u]]
               for u in range(sa)):
            # Equality of upward images already implies monotonicity.
            total += 1
    return total


def main():
    checks = 0
    for h in range(1, 4):
        for k in range(1, 4):
            for src in product((1, 2, 3), repeat=h):
                for dst in product((1, 2, 3), repeat=k):
                    if sum(src) > 7 or sum(dst) > 6 or sum(dst) > sum(src):
                        continue
                    found = exhaustive(src, dst)
                    expected = recurrence(src, dst)
                    assert found == expected, (src, dst, found, expected)
                    checks += 1
    # Non-brute-force anchors include larger heights and long singletons.
    anchors = [
        ((3, 3), (2, 1), 12),
        ((3, 3), (1, 2), 6),
        ((2, 4, 2), (2, 1, 2), 4),
        ((3, 1, 2, 2), (1, 2, 1, 2), 0),
        ((2, 2, 2, 2), (2, 1, 2), 4),
        ((3, 4, 2), (1, 1, 2), 14),
    ]
    for source, target, expected in anchors:
        actual = recurrence(source, target)
        assert actual == expected, (source, target, actual, expected)
    print(f"PASS: {checks} exhaustive pairs; {len(anchors)} anchors")


if __name__ == '__main__':
    main()
