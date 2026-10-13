#!/usr/bin/env python3
"""Finite definition-level corroboration for the complete-tripartite theorem."""
from itertools import product


def set_partitions_rgs(n):
    """Yield set partitions as tuples of blocks via restricted-growth strings."""
    if n == 0:
        yield ()
        return
    a = [0] * n
    def rec(pos, maxv):
        if pos == n:
            blocks = [[] for _ in range(maxv + 1)]
            for v, lab in enumerate(a):
                blocks[lab].append(v)
            yield tuple(tuple(b) for b in blocks)
            return
        for lab in range(maxv + 2):
            a[pos] = lab
            yield from rec(pos + 1, max(maxv, lab))
    a[0] = 0
    yield from rec(1, 0)


def support(block, parts):
    return frozenset(parts[v] for v in block)


def is_gc_partition(blocks, parts):
    supports = [support(block, parts) for block in blocks]
    universe = frozenset((0, 1, 2))
    # Every block must itself fail global domination.
    if any(s == universe for s in supports):
        return False
    # Every block must have a distinct coalition partner whose union is global.
    for i, s in enumerate(supports):
        if not any(i != j and (s | t) == universe for j, t in enumerate(supports)):
            return False
    return True


def exact_gc(a, b, c):
    parts = (0,) * a + (1,) * b + (2,) * c
    best = 0
    for blocks in set_partitions_rgs(len(parts)):
        if len(blocks) <= best:
            continue
        if is_gc_partition(blocks, parts):
            best = len(blocks)
    return best


def formula(a, b, c):
    n = a + b + c
    if c == 1:
        return a + 1
    if c == 2:
        return n - 2
    return n - 3


def main():
    profiles = 0
    for n in range(3, 11):
        for c in range(1, n + 1):
            for b in range(c, n + 1):
                a = n - b - c
                if a < b:
                    continue
                profiles += 1
                got = exact_gc(a, b, c)
                want = formula(a, b, c)
                if got != want:
                    raise AssertionError((a, b, c, got, want))
    assert profiles == 31, profiles
    print("ALL CHECKS PASSED; profiles=31; orders=3..10")


if __name__ == "__main__":
    main()
