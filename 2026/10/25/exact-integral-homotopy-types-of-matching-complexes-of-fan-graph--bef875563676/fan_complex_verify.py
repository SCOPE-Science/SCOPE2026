#!/usr/bin/env python3
"""Exact finite checks for fan-graph matching complexes (Python standard library)."""

def fan_edges(n):
    """Vertex 0 is the hub; 1,...,n form the path."""
    return [(0, i) for i in range(1, n + 1)] + [(i, i + 1) for i in range(1, n)]


def faces(n):
    """Enumerate every matching; key d lists face bitmasks of dimension d."""
    edges = fan_edges(n)
    states = [(0, 0)]  # (selected edge bits, used graph vertex bits)
    for j, (u, v) in enumerate(edges):
        endpoints = (1 << u) | (1 << v)
        states += [(mask | (1 << j), used | endpoints)
                   for mask, used in states if not used & endpoints]
    result = {}
    for mask, _ in states:
        result.setdefault(mask.bit_count() - 1, []).append(mask)
    return result


def rank_mod2(columns):
    """Exact Gaussian elimination over F_2, columns encoded as binary rows."""
    pivots = {}
    for col in columns:
        while col:
            j = col.bit_length() - 1
            if j not in pivots:
                pivots[j] = col
                break
            col ^= pivots[j]
    return len(pivots)


def reduced_betti(n):
    cells = faces(n)
    ranks = {}
    for d in sorted(cells):
        if d < 0:
            continue
        previous = {mask: j for j, mask in enumerate(cells[d - 1])}
        columns = []
        for face in cells[d]:
            remaining, boundary = face, 0
            while remaining:
                bit = remaining & -remaining
                boundary ^= 1 << previous[face ^ bit]
                remaining ^= bit
            columns.append(boundary)
        ranks[d] = rank_mod2(columns)
    betti = {d: len(cells[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
             for d in cells if d >= 0}
    return {d: value for d, value in betti.items() if value}, sum(map(len, cells.values()))


def predicted(n):
    q, r = divmod(n, 3)
    if r == 0:
        return {q - 1: q + 1}
    if r == 1:
        return {q: q}
    return {q: 2 * q + 2}


if __name__ == '__main__':
    for n in range(3, 16):
        observed, total_faces = reduced_betti(n)
        expected = predicted(n)
        print('n=%d faces=%d reduced_F2_betti=%r expected=%r'
              % (n, total_faces, observed, expected))
        assert observed == expected, 'discrepancy at n=%d' % n
    print('PASS: complete mod-two simplicial boundary ranks for all 3<=n<=15')
