#!/usr/bin/env python3
"""Exact finite tests of the strong-Morse bipartite simplex classification.

No third-party modules. Run: python3 verify_complete_bipartite_strong_morse.py
Proof for all sizes is mathematical, not inferred from these finite tests.
"""
from itertools import permutations, combinations


def powerset_nonempty(vertices):
    seq = tuple(vertices)
    for j in range(1, len(seq) + 1):
        for subset in combinations(seq, j):
            yield frozenset(subset)


def facets(m, n):
    A, B = range(m), range(m, m + n)
    out = []
    for b in B:
        out.append(frozenset((a, b) for a in A))
        for a in A:
            out.append(frozenset([(b, a)] + [(i, b) for i in A if i != a]))
    for a in A:
        out.append(frozenset((b, a) for b in B))
        for b in B:
            out.append(frozenset([(a, b)] + [(i, a) for i in B if i != b]))
    return out


def faces(m, n):
    return set().union(*(set(powerset_nonempty(f)) for f in facets(m, n)))


def full_order_faces(m, n):
    V = range(m + n)
    out = set()
    for order in permutations(V):
        position = {v: i for i, v in enumerate(order)}
        match = []
        for v in V:
            neighbors = range(m, m + n) if v < m else range(m)
            earlier = [w for w in neighbors if position[w] < position[v]]
            if len(earlier) == 1:
                match.append((v, earlier[0]))
        out.add(frozenset(match))
    return set().union(*(set(powerset_nonempty(f)) for f in out))


def collapse(m, n):
    remaining = faces(m, n)
    pairs = 0

    def remove_pair(lower, upper):
        nonlocal pairs
        low, high = frozenset(lower), frozenset(upper)
        assert low in remaining and high in remaining and len(high) == len(low) + 1
        immediate = [f for f in remaining if len(f) == len(low) + 1 and low <= f]
        assert immediate == [high], (m, n, low, immediate, high)
        remaining.remove(low)
        remaining.remove(high)
        pairs += 1

    # Collapse mixed simplices in the first family, keeping their two endpoints.
    for b in range(m, m + n):
        for a in range(m):
            j = 0 if a != 0 else 1
            rest = [(i, b) for i in range(m) if i not in (a, j)]
            y, x = (b, a), (j, b)
            for k in range(len(rest), 0, -1):
                for S in combinations(rest, k):
                    remove_pair(set(S) | {y}, set(S) | {y, x})
        hub = (0, b)
        rest = [(i, b) for i in range(1, m)]
        for k in range(len(rest), 1, -1):
            for S in combinations(rest, k):
                remove_pair(S, set(S) | {hub})

    # Collapse mixed simplices in the second family, retaining their endpoints.
    for a in range(m):
        for b in range(m, m + n):
            j = m if b != m else m + 1
            rest = [(i, a) for i in range(m, m + n) if i not in (b, j)]
            y, x = (a, b), (j, a)
            for k in range(len(rest), 0, -1):
                for S in combinations(rest, k):
                    remove_pair(set(S) | {y}, set(S) | {y, x})
        hub = (m, a)
        rest = [(i, a) for i in range(m + 1, m + n)]
        for k in range(len(rest), 1, -1):
            for S in combinations(rest, k):
                remove_pair(S, set(S) | {hub})

    assert all(len(f) <= 2 for f in remaining)
    vertices = [next(iter(f)) for f in remaining if len(f) == 1]
    edges = [tuple(f) for f in remaining if len(f) == 2]
    assert len(vertices) == 2 * m * n
    assert len(edges) == 4 * m * n - m - n
    root = vertices[0]
    seen = {root}
    changed = True
    while changed:
        changed = False
        for u, v in edges:
            if u in seen and v not in seen: seen.add(v); changed = True
            if v in seen and u not in seen: seen.add(u); changed = True
    assert len(seen) == len(vertices)
    return pairs, len(vertices), len(edges)


def parity(permutation):
    return -1 if sum(permutation[i] > permutation[j]
                     for i in range(len(permutation))
                     for j in range(i + 1, len(permutation))) % 2 else 1


def homology_trace(m, n, source_faces, s, t, swap=False):
    def action_vertex(v):
        if swap:
            return m + s[v] if v < m else t[v - m]
        return s[v] if v < m else m + t[v - m]
    def action_arc(x): return action_vertex(x[0]), action_vertex(x[1])
    lefschetz = 0
    for f in source_faces:
        dst = frozenset(action_arc(x) for x in f)
        if dst != f: continue
        ordered = sorted(f)
        index = {x: i for i, x in enumerate(ordered)}
        signed = parity([index[action_arc(x)] for x in ordered])
        lefschetz += (-1) ** (len(f) - 1) * signed
    return 1 - lefschetz  # H_0 has trace one, all higher H_k vanish except H_1.


def test(m, n):
    F = faces(m, n)
    assert full_order_faces(m, n) == F, 'Facets do not capture strong gradients'
    pair_count, v_count, e_count = collapse(m, n)
    action_count = 0
    for s in permutations(range(m)):
        for t in permutations(range(n)):
            fixed_a = sum(i == s[i] for i in range(m))
            fixed_b = sum(i == t[i] for i in range(n))
            expected = 2 * fixed_a * fixed_b - fixed_a - fixed_b + 1
            assert homology_trace(m, n, F, s, t) == expected
            action_count += 1
            if m == n:
                assert homology_trace(m, n, F, s, t, swap=True) == 1
                action_count += 1
    print(f'K_{{{m},{n}}}: {len(F)} faces, {pair_count} certified collapses, '
          f'{v_count} final vertices, {e_count} final edges, '
          f'{action_count} symmetry comparisons, beta_1={e_count-v_count+1}')


if __name__ == '__main__':
    for shape in [(2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]:
        test(*shape)
    print('PASS: complete-order, collapse and signed Lefschetz tests')
