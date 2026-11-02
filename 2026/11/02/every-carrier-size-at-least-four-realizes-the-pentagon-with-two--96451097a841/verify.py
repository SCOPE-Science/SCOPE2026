#!/usr/bin/env python3
"""Independent exhaustive finite checks for a two-valued unary pentagon construction.

No external packages. The symbolic proof is required for unbounded carrier size.
"""
from itertools import combinations


def partitions(n):
    """All equivalence relations on range(n), as restricted-growth strings."""
    def extend(prefix, largest):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for v in range(largest + 2):
            yield from extend(prefix + [v], max(largest, v))
    yield from extend([0], 0)


def canonical(labels):
    index = {}
    return tuple(index.setdefault(x, len(index)) for x in labels)


def operations(r):
    """All prescribed two-valued maps; points r,r+1 are the outsiders."""
    for a, b in combinations(range(r), 2):
        for mask in range(1, (1 << r) - 1):
            values = [b if (mask >> i) & 1 else a for i in range(r)]
            yield tuple(values + [values[0], values[1]])
    yield tuple([r] * r + [0, 0])
    yield tuple([r + 1] * r + [1, 1])


def preserves(f, p):
    n = len(p)
    for i in range(n):
        for j in range(i):
            if p[i] == p[j] and p[f[i]] != p[f[j]]:
                return False
    return True


def check(r):
    n = r + 2
    ops = list(operations(r))
    expected_count = r * (r - 1) // 2 * ((1 << r) - 2) + 2
    assert len(ops) == expected_count
    assert len(set(ops)) == len(ops)
    assert all(len(set(f)) == 2 for f in ops)
    rho = canonical([0] * r + [1, 2])
    sigma = canonical([0] * r + [1, 1])
    tau = canonical(list(range(r)) + [0, 1])
    wanted = {canonical(range(n)), rho, sigma, tau, canonical([0] * n)}
    assert len(wanted) == 5
    assert all(all(preserves(f, p) for f in ops) for p in wanted)
    actual = {p for p in partitions(n) if all(preserves(f, p) for f in ops)}
    assert actual == wanted, (n, actual, wanted)
    print(f"n={n}: operations={len(ops)}, congruences={len(actual)}, verification=PASS")


if __name__ == "__main__":
    for r in range(2, 7):
        check(r)
    print("VERIFY_OK")
