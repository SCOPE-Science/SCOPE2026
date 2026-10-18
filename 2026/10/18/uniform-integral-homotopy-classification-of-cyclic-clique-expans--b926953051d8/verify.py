#!/usr/bin/env python3
"""Exact face and mod-two boundary checks for lexicographic cycle--clique independence complexes."""
from math import comb


def predicted(n, m):
    assert n >= 7 and m >= 2
    out = {}
    if n % 3 == 0:
        out[n // 3 - 1] = 2
    elif n % 3 == 1:
        out[n // 3 - 1] = 1
    else:
        out[n // 3] = 1
    if n % 3 == 0:
        d = n // 3 - 1
        out[d] += 3 * (m ** (n // 3) - 1)
    for t in range(1, n // 2 + 1):
        if (n + t) % 3:
            continue
        h = (n + t) // 3
        if t > h:
            continue
        b = n * comb(h - 1, t - 1) * (m - 1) ** t * m ** (h - t)
        assert b % t == 0
        out[h - 1] = out.get(h - 1, 0) + b // t
    return {k: v for k, v in out.items() if v}


def actual_complex(n, m):
    size = n * m
    adjacency = [0] * size
    for a in range(size):
        i, c = divmod(a, m)
        for b in range(size):
            j, d = divmod(b, m)
            if (i == j and c != d) or (i - j) % n in (1, n - 1):
                adjacency[a] |= 1 << b
    good = bytearray(1 << size)
    good[0] = 1
    groups = {}
    for mask in range(1, 1 << size):
        v = mask.bit_length() - 1
        rest = mask ^ (1 << v)
        if good[rest] and not (rest & adjacency[v]):
            good[mask] = 1
            groups.setdefault(mask.bit_count() - 1, []).append(mask)
    count_by_size = [len(groups.get(k - 1, [])) for k in range(1, n // 2 + 1)]
    for j, observed in enumerate(count_by_size, 1):
        expected = n * comb(n - j, j) * m ** j // (n - j)
        assert observed == expected, (n, m, j, observed, expected)
    return groups


def mod2_homology(groups, n, m):
    dimensions = sorted(groups)
    assert dimensions == list(range(dimensions[-1] + 1))
    previous_rank = 0
    result = {}
    for d in dimensions:
        higher = groups.get(d + 1, [])
        rows = {face: i for i, face in enumerate(groups[d])}
        pivots = {}
        for simplex in higher:
            bd = 0
            for vertex in range(n * m):
                if simplex & (1 << vertex):
                    bd ^= 1 << rows[simplex ^ (1 << vertex)]
            while bd:
                high = bd.bit_length() - 1
                if high not in pivots:
                    pivots[high] = bd
                    break
                bd ^= pivots[high]
        rank = len(pivots)
        betti = len(groups[d]) - previous_rank - rank - (1 if d == 0 else 0)
        assert betti >= 0, (d, betti)
        if betti:
            result[d] = betti
        previous_rank = rank
    return result


def main():
    for n, m in [(7, 2), (8, 2), (9, 2), (7, 3)]:
        face_groups = actual_complex(n, m)
        got = mod2_homology(face_groups, n, m)
        want = predicted(n, m)
        assert got == want, (n, m, want, got)
        print('PASS', n, m, 'faces', sum(map(len, face_groups.values())),
              'reduced_mod2_betti', got)
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
