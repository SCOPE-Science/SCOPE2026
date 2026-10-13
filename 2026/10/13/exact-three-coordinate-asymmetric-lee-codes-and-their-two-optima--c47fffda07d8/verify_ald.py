#!/usr/bin/env python3
"""Exact maximum-clique census in the three-coordinate asymmetric Lee metric.

Independent exhaustive Bron--Kerbosch enumeration: Python standard library only.
Indices 0..63 encode (s0,s1,s2) as s0+4*s1+16*s2, with symbols
00, 01, 10, 11 mapped to 0, 1, 2, 3, respectively.
"""
from itertools import permutations

N = 64
words = [tuple((i // 4**k) % 4 for k in range(3)) for i in range(N)]


def elementary(a, c):
    """Equation (1) of Gabrys--Kiah--Milenkovic at lambda=1."""
    x, y = divmod(a, 2)
    z, w = divmod(c, 2)
    return (2 * (int(x == y) + int(z == w))
            + int(x == 1-y == 1-z == w)
            - 4 * int(x == y == z == w))


def distance(i, j):
    return sum(elementary(a, b) for a, b in zip(words[i], words[j]))


adj = [sum(1 << j for j in range(N) if j != i and distance(i, j) >= 3)
       for i in range(N)]
assert sum(a.bit_count() for a in adj) // 2 == 1752
max_size = 0
max_codes = set()
histogram = {}
node_count = 0


def bron_kerbosch(R, P, X):
    """Enumerate maximal cliques exactly once, with an exact pivot restriction."""
    global max_size, max_codes, node_count
    node_count += 1
    if not P and not X:
        size = R.bit_count()
        histogram[size] = histogram.get(size, 0) + 1
        if size > max_size:
            max_size, max_codes = size, {R}
        elif size == max_size:
            max_codes.add(R)
        return
    PX = P | X
    # Any maximal clique containing R not already rejected includes a vertex
    # outside N(u) for a pivot u in P union X.
    pivot = max((i for i in range(N) if PX >> i & 1),
                key=lambda i: (P & adj[i]).bit_count()) if PX else -1
    candidates = P & ~(adj[pivot] if pivot >= 0 else 0)
    while candidates:
        bit = candidates & -candidates
        v = bit.bit_length() - 1
        bron_kerbosch(R | bit, P & adj[v], X & adj[v])
        P &= ~bit
        X |= bit
        candidates &= ~bit


bron_kerbosch(0, (1 << N) - 1, 0)
expected_histogram = {10: 128, 11: 2344, 12: 32360, 13: 177712,
                      14: 300744, 15: 86648, 16: 16168,
                      17: 2464, 18: 24, 19: 32}
assert histogram == expected_histogram
assert max_size == 19 and len(max_codes) == 32
assert sum(histogram.values()) == 618624


def transform(code, permutation, local_mask):
    out = 0
    for i in range(N):
        if code >> i & 1:
            j = 0
            for k in range(3):
                symbol = words[i][permutation[k]]
                flags = (local_mask >> (2 * k)) & 3
                if ((symbol in (0, 3) and flags & 1)
                        or (symbol in (1, 2) and flags & 2)):
                    symbol = 3 - symbol
                j += symbol * 4**k
            out |= 1 << j
    return out


def distance_distribution(code):
    values = [i for i in range(N) if code >> i & 1]
    result = {}
    for position, i in enumerate(values):
        for j in values[position + 1:]:
            d = distance(i, j)
            result[d] = result.get(d, 0) + 1
    return result


expected = {
    0x2492490490292492: (8, {3: 24, 4: 69, 6: 24, 7: 24, 8: 30}),
    0x2492490490492492: (24, {3: 28, 4: 61, 5: 4, 6: 24, 7: 24, 8: 30}),
}
assert all(rep in max_codes for rep in expected)
orbits = []
for representative, (expected_size, spectrum) in expected.items():
    orbit = {transform(representative, p, m)
             for p in permutations(range(3)) for m in range(64)}
    assert len(orbit) == expected_size
    assert orbit <= max_codes
    assert distance_distribution(representative) == spectrum
    assert representative.bit_count() == 19
    assert all(distance(i, j) >= 3
               for i in range(64) if representative >> i & 1
               for j in range(i + 1, 64) if representative >> j & 1)
    orbits.append(orbit)
assert orbits[0].isdisjoint(orbits[1])
assert orbits[0] | orbits[1] == max_codes
print('VERIFY_OK_PY maximum=19 labeled_optima=32 maximal_cliques=618624 '
      'orbits=8,24 stabilizers=48,16')
