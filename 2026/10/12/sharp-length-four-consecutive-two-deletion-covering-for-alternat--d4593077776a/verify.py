#!/usr/bin/env python3
"""Exact constructive certificates for length-four adjacent-pair deletion covers."""

BASE = {
    (2, 2): [(0, 1, 1, 0), (1, 1, 0, 0)],
    (2, 3): [(0, 0, 1, 2), (1, 0, 0, 1)],
    (2, 4): [(0, 3, 1, 0), (1, 0, 0, 1), (1, 3, 0, 2)],
    (3, 3): [(i, (i + 1) % 3, (i + 1) % 3, i) for i in range(3)],
    (4, 4): [(0, 0, 3, 1), (0, 2, 1, 3), (1, 1, 2, 0),
             (2, 1, 1, 2), (2, 3, 3, 0), (3, 2, 1, 3)],
}


def transpose(word):
    a, b, c, d = word
    return (d, c, b, a)


def burst_shadow(word):
    a, b, c, d = word
    return {(c, d), (a, d), (a, b)}


def tile_3_by_n(n, rows=(0, 1, 2), cols=None):
    """Partition a 3-by-n grid into disjoint three-edge L-paths, n >= 2."""
    assert n >= 2 and len(rows) == 3
    if cols is None:
        cols = list(range(n))
    assert len(cols) == n
    groups = ([3] if n % 2 else []) + [2] * ((n - 3 * (n % 2)) // 2)
    result = []
    k = 0
    for group in groups:
        if group == 2:
            patterns = [(1, 1, 0, 0), (2, 0, 0, 1)]
        else:
            patterns = BASE[(3, 3)]
        for a, b, c, d in patterns:
            result.append((rows[a], cols[k + b], rows[c], cols[k + d]))
        k += group
    assert k == n
    return result


def construct(m, n):
    """An exact-size cover for m,n >= 2, without optimization libraries."""
    if m < 2 or n < 2:
        raise ValueError('This theorem assumes both alphabets have >=2 symbols')
    if m >= 5:
        return construct(m - 3, n) + tile_3_by_n(n, list(range(m - 3, m)), list(range(n)))
    if n >= 5:
        block = tile_3_by_n(m, list(range(n - 3, n)), list(range(m)))
        return construct(m, n - 3) + [transpose(w) for w in block]
    if (m, n) in BASE:
        return list(BASE[(m, n)])
    if (n, m) in BASE:
        return [transpose(w) for w in BASE[(n, m)]]
    if m == 3 and n == 4:
        return tile_3_by_n(4)
    if m == 4 and n == 3:
        return [transpose(w) for w in tile_3_by_n(4)]
    raise AssertionError((m, n))


def verify(m, n):
    C = construct(m, n)
    assert len(C) == (m * n + 2) // 3, (m, n, len(C))
    assert len(set(C)) == len(C), (m, n, 'duplicate codewords')
    required = {(a, b) for a in range(m) for b in range(n)}
    received = set()
    for w in C:
        a, b, c, d = w
        assert 0 <= a < m and 0 <= c < m and 0 <= b < n and 0 <= d < n
        assert len(burst_shadow(w)) == 3, (m, n, w)
        received.update(burst_shadow(w))
    assert received == required, (m, n, len(received), m * n)
    return len(C)


if __name__ == '__main__':
    for m in range(2, 51):
        for n in range(2, 51):
            verify(m, n)
    for q in (2, 3, 4, 5, 6, 7, 8, 11, 23, 50):
        print(f'q={q}, minimum={verify(q, q)}')
    print('VERIFY_OK 2401 rectangular parameter pairs')
