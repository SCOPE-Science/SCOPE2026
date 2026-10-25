#!/usr/bin/env python3
"""Reproduce the integral discrete-Morse certificates for two 12-vertex graphs.

Requires Python 3.9+ standard library only. Run: python3 verify_polyhedra.py
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 12
ORDER = [10, 3, 0, 2, 7, 11, 1, 9, 5, 4, 6, 8]


def truncated_tetrahedron():
    vertices = [(i, j) for i in range(4) for j in range(4) if i != j]
    number = {v: i for i, v in enumerate(vertices)}
    edges = set()
    for i in range(4):
        triangle = [number[(i, j)] for j in range(4) if j != i]
        for a, b in combinations(triangle, 2):
            edges.add(tuple(sorted((a, b))))
    for i in range(4):
        for j in range(i + 1, 4):
            edges.add(tuple(sorted((number[(i, j)], number[(j, i)]))))
    return sorted(edges)


def cuboctahedron():
    cube_edges = [(x, x ^ (1 << k)) for x in range(8)
                  for k in range(3) if not ((x >> k) & 1)]
    assert len(cube_edges) == N
    return [(i, j) for i, j in combinations(range(N), 2)
            if set(cube_edges[i]).intersection(cube_edges[j])]


def faces_by_triples(edges):
    adj = [0] * N
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    forbidden = []
    for a, b, c in combinations(range(N), 3):
        e = int(bool((adj[a] >> b) & 1)) + int(bool((adj[a] >> c) & 1)) + int(bool((adj[b] >> c) & 1))
        if e >= 2:
            forbidden.append((1 << a) | (1 << b) | (1 << c))
    faces = [m for m in range(1, 1 << N)
             if all((m & t) != t for t in forbidden)]
    return adj, forbidden, faces


def face_by_components(mask, adj):
    remaining = mask
    while remaining:
        seen = 0
        active = remaining & -remaining
        while active:
            one = active & -active
            active ^= one
            seen |= one
            active |= adj[one.bit_length() - 1] & remaining & ~seen & ~active
        if seen.bit_count() > 2:
            return False
        remaining &= ~seen
    return True


def sign_of_face(upper, lower):
    if (lower & upper) != lower or upper.bit_count() != lower.bit_count() + 1:
        raise ValueError('not a codimension-one incidence')
    omitted = upper ^ lower
    return -1 if ((upper & (omitted - 1)).bit_count() & 1) else 1


def verify_one(title, edges, expected_f, expected_critical, expected_forbidden,
               expected_facets, expected_arrows):
    assert len(edges) == len(set(edges))
    assert len(set(v for e in edges for v in e)) == N
    adj, forbidden, faces = faces_by_triples(edges)
    assert len(forbidden) == expected_forbidden
    face_set = set(faces)
    for m in range(1, 1 << N):
        assert (m in face_set) == face_by_components(m, adj)
    counts = Counter(m.bit_count() - 1 for m in faces)
    assert tuple(counts[d] for d in range(max(counts) + 1)) == expected_f
    facets = [m for m in faces
              if all((m | (1 << v)) not in face_set
                     for v in range(N) if not ((m >> v) & 1))]
    facet_counts = Counter(m.bit_count() - 1 for m in facets)
    assert facet_counts == expected_facets

    unmatched = set(faces)
    pairs = []
    # Sequential vertex matching: always pair a face not containing v
    # with its union with v, if both remain unmatched.
    for v in ORDER:
        bit = 1 << v
        for low in faces:
            if (low & bit) == 0 and low in unmatched and (low | bit) in unmatched:
                up = low | bit
                unmatched.remove(low)
                unmatched.remove(up)
                pairs.append((low, up))
    critical = sorted(unmatched)
    low_to_up = dict(pairs)
    up_to_low = {u: l for l, u in pairs}
    assert len(low_to_up) == len(up_to_low) == len(pairs)
    assert (len(pairs) * 2 + len(critical)) == len(faces)
    critical_counts = Counter(m.bit_count() - 1 for m in critical)
    assert critical_counts == expected_critical

    # Verify acyclicity of the FULL oriented Hasse graph, not a sample.
    incoming = {m: 0 for m in faces}
    outgoing = {m: [] for m in faces}
    incidences = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if not lower:
                continue
            assert lower in face_set
            src, dst = ((lower, upper) if low_to_up.get(lower) == upper
                        else (upper, lower))
            outgoing[src].append(dst)
            incoming[dst] += 1
            incidences += 1
    assert incidences == expected_arrows
    queue = deque(m for m in faces if incoming[m] == 0)
    visited = 0
    while queue:
        m = queue.popleft()
        visited += 1
        for next_m in outgoing[m]:
            incoming[next_m] -= 1
            if incoming[next_m] == 0:
                queue.append(next_m)
    assert visited == len(faces), 'gradient cycle detected'

    # Integral algebraic-Morse projection: a paired upper cell projects to
    # zero; a paired lower cell is replaced via its matched upper boundary.
    # Acyclicity proves the recursion terminates.
    @lru_cache(None)
    def projection(m):
        if m in up_to_low:
            return {}
        if m not in low_to_up:
            return {m: 1}
        upper = low_to_up[m]
        pivot = sign_of_face(upper, m)
        coeff = {}
        b = upper
        while b:
            bit = b & -b
            b ^= bit
            lower = upper ^ bit
            if lower == m:
                continue
            sign = sign_of_face(upper, lower)
            for c, value in projection(lower).items():
                coeff[c] = coeff.get(c, 0) - sign * value * pivot
        return {k: v for k, v in coeff.items() if v}

    integral_morse_boundary = {}
    for upper in critical:
        if upper.bit_count() == 1:
            continue
        coeff = {}
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            for c, value in projection(lower).items():
                coeff[c] = coeff.get(c, 0) + sign_of_face(upper, lower) * value
        integral_morse_boundary[upper] = {k: v for k, v in coeff.items() if v}
    assert all(not x for x in integral_morse_boundary.values()), integral_morse_boundary

    # Independent mod-two boundary-rank computation on ORIGINAL cells.
    by_dim = {d: sorted(m for m in faces if m.bit_count() == d + 1)
              for d in counts}
    ranks = {}
    for d in range(1, max(counts) + 1):
        index = {m: k for k, m in enumerate(by_dim[d - 1])}
        pivots = {}
        for cell in by_dim[d]:
            value = 0
            bits = cell
            while bits:
                bit = bits & -bits
                bits ^= bit
                value ^= 1 << index[cell ^ bit]
            while value:
                pivot = value.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = value
                    break
                value ^= pivots[pivot]
        ranks[d] = len(pivots)
    mod2 = {d: counts[d] - ranks.get(d, 0) - ranks.get(d + 1, 0) - int(d == 0)
            for d in counts}
    assert mod2 == {d: expected_critical.get(d, 0) - int(d == 0) for d in counts}
    print('%s: faces=%d, forbidden_triples=%d, pairs=%d, critical=%s, directed_incidences=%d, Morse_boundary=ZERO, mod2=%s'
          % (title, len(faces), len(forbidden), len(pairs), dict(sorted(critical_counts.items())),
             incidences, mod2))


def main():
    verify_one('Truncated tetrahedron', truncated_tetrahedron(),
               (12, 66, 192, 303, 228, 62), {0: 1, 3: 3, 4: 3}, 28,
               {3: 3, 5: 62}, 3432)
    verify_one('Cuboctahedron', cuboctahedron(),
               (12, 66, 164, 177, 36), {0: 1, 3: 32}, 56,
               {3: 45, 4: 36}, 1512)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
