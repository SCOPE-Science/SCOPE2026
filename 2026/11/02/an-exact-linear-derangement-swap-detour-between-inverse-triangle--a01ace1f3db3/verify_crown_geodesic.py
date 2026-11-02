"""Constructive verification of exact derangement-swap geodesics.

Run: python verify_crown_geodesic.py
Only standard-library Python is required.
"""
from collections import Counter

PAIR = ((0, 3), (0, 1), (1, 2), (2, 5), (2, 4), (2, 3))
TRIPLE = ((0, 3), (0, 1), (0, 6), (0, 8), (0, 7),
          (0, 6), (1, 2), (2, 5), (2, 4), (2, 3))


def sigma(k):
    n = 3 * k
    return tuple(3 * (i // 3) + (i + 1) % 3 for i in range(n))


def inverse(p):
    inv = [None] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def cycles(p):
    seen, count = set(), 0
    for i in range(len(p)):
        if i not in seen:
            count += 1
            x = i
            while x not in seen:
                seen.add(x)
                x = p[x]
    return count


def moves(k):
    if k < 2:
        raise ValueError('formula applies only for k>=2')
    groups = [(0, 3)] if k % 2 else []
    first = 3 if k % 2 else 0
    groups += [(start, 2) for start in range(first, k, 2)]
    result = []
    for block_start, amount in groups:
        offset = block_start * 3
        pattern = TRIPLE if amount == 3 else PAIR
        result.extend((offset + i, offset + j) for i, j in pattern)
    return result


def run(k):
    n = 3 * k
    p = list(sigma(k))
    tgt = inverse(p)
    merge, split = 0, 0
    visited = [tuple(p)]
    for i, j in moves(k):
        assert i != j and p[i] != j and p[j] != i
        old = tuple(p)
        rel_old = tuple(inverse(old)[tgt[a]] for a in range(n))
        c0 = cycles(rel_old)
        p[i], p[j] = p[j], p[i]
        assert len(set(p)) == n and all(p[a] != a for a in range(n))
        rel_new = tuple(inverse(p)[tgt[a]] for a in range(n))
        dc = cycles(rel_new) - c0
        assert abs(dc) == 1
        if dc == 1:
            split += 1
        else:
            merge += 1
        visited.append(tuple(p))
    assert tuple(p) == tgt
    assert len(moves(k)) == 2 * k + 2 * ((k + 1) // 2)
    assert merge == (k + 1) // 2 and split == 2 * k + merge
    return len(moves(k)), merge, split, len(visited)


if __name__ == '__main__':
    assert sigma(1) == (1, 2, 0)
    assert inverse(sigma(1)) == (2, 0, 1)
    for k in range(2, 31):
        length, mergers, splits, states = run(k)
        print(f'k={k:2d} n={3*k:2d} length={length:2d} merges={mergers:2d} splits={splits:2d}')
    print('CONSTRUCTIVE_ALL_K_2_TO_30_PASS')
