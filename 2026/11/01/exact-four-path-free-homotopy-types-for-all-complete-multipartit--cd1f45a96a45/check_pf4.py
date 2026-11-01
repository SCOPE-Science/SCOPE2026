#!/usr/bin/env python3
"""Independent finite checks of the PF_4 multipartite homotopy formula.

Usage: python check_pf4.py
Only finite instances are tested. The all-parameter result is proved separately.
"""
from itertools import combinations, permutations
from math import comb
from collections import deque


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted_rank(sizes):
    N = sum(sizes)
    return C(N - 1, 3) - sum(C(s - 1, 3) + (N - s) * C(s - 1, 2) for s in sizes)


def examine(sizes):
    N = sum(sizes)
    part = []
    for i, s in enumerate(sizes):
        part.extend([i] * s)
    chosen = []
    at = 0
    for s in sizes:
        chosen.append(at)
        at += s

    forbidden = []
    for quad in combinations(range(N), 4):
        if any(all(part[p[i]] != part[p[i + 1]] for i in range(3))
               for p in permutations(quad)):
            forbidden.append(sum(1 << i for i in quad))

    faces = {s for s in range(1 << N)
             if all((s & quad) != quad for quad in forbidden)}

    for s in faces:
        c = [sum(bool(s & (1 << i)) for i in range(N) if part[i] == j)
             for j in range(len(sizes))]
        structural = (s.bit_count() <= 3 or
                      any(s.bit_count() - t <= 1 for t in c))
        assert structural, (sizes, s, 'invalid structural classification')

    lower_to_upper, upper_to_lower = {}, {}
    for s in sorted(faces):
        if s.bit_count() < 3:
            continue
        counts = [sum(bool(s & (1 << i)) for i in range(N) if part[i] == j)
                  for j in range(len(sizes))]
        owners = [j for j, count in enumerate(counts)
                  if count >= 2 and s.bit_count() - count <= 1]
        if len(owners) != 1:
            assert s.bit_count() == 3 or s == 0, (sizes, s, owners)
            continue
        j = owners[0]
        x = 1 << chosen[j]
        if not (s & x):
            u = s | x
            assert u in faces and u not in upper_to_lower
            lower_to_upper[s] = u
            upper_to_lower[u] = s

    assert all(s in lower_to_upper or s in upper_to_lower
               for s in faces if s.bit_count() >= 4)
    assert set(lower_to_upper).isdisjoint(upper_to_lower)
    assert all(u.bit_count() == s.bit_count() + 1
               for s, u in lower_to_upper.items())

    # Complete directed Hasse graph: matched incidences up, all others down.
    outgoing = {s: [] for s in faces}
    indeg = {s: 0 for s in faces}
    for upper in faces:
        bits = upper
        while bits:
            b = bits & -bits
            bits -= b
            lower = upper ^ b
            if lower not in faces:
                raise AssertionError('not downward closed')
            if lower_to_upper.get(lower) == upper:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            outgoing[src].append(dst)
            indeg[dst] += 1
    queue = deque(s for s in faces if indeg[s] == 0)
    reached = 0
    while queue:
        u = queue.popleft()
        reached += 1
        for v in outgoing[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    assert reached == len(faces), (sizes, 'matching cyclic')

    critical = [s for s in faces if s not in lower_to_upper and s not in upper_to_lower]
    assert all(s.bit_count() <= 3 for s in critical)
    critical_triangles = sum(s.bit_count() == 3 for s in critical)
    assert critical_triangles == C(N, 3) - sum(
        C(t - 1, 3) + (N - t) * C(t - 1, 2) for t in sizes)
    chi = sum((-1) ** (s.bit_count() - 1) for s in faces if s)
    assert chi - 1 == predicted_rank(sizes)

    # Independent simplicial-chain mod-two ranks, not derived from matching.
    bydim = {}
    for s in faces:
        if s:
            bydim.setdefault(s.bit_count() - 1, []).append(s)
    for dim in bydim:
        bydim[dim].sort()
    boundaries = {}
    for dim in range(1, max(bydim, default=0) + 1):
        row_index = {s: i for i, s in enumerate(bydim[dim - 1])}
        piv = {}
        for s in bydim[dim]:
            col, bits = 0, s
            while bits:
                b = bits & -bits
                bits ^= b
                col ^= 1 << row_index[s ^ b]
            while col:
                hi = col.bit_length() - 1
                if hi in piv:
                    col ^= piv[hi]
                else:
                    piv[hi] = col
                    break
        boundaries[dim] = len(piv)
    bettis = {d: len(simplices) - boundaries.get(d, 0) - boundaries.get(d + 1, 0)
              for d, simplices in bydim.items()}
    assert bettis.get(0, 0) == 1
    assert bettis.get(2, 0) == predicted_rank(sizes)
    assert all(v == 0 for d, v in bettis.items() if d not in (0, 2))
    return len(faces), len(lower_to_upper), predicted_rank(sizes)


if __name__ == '__main__':
    cases = [(1, 1), (1, 4), (2, 2), (2, 3), (3, 3),
             (1, 1, 1), (2, 2, 2), (2, 3, 3), (3, 3, 3),
             (1, 1, 1, 1), (1, 2, 2, 2), (2, 2, 2, 2),
             (1, 1, 1, 1, 1), (1, 1, 2, 2, 2)]
    for sizes in cases:
        count, pairs, rank = examine(sizes)
        print(f'{sizes}: faces={count}, matching_pairs={pairs}, beta2={rank}: OK')
    print(f'PASS: {len(cases)} independent exhaustive checks of faces, '
          'acyclic matchings and mod-two homology')
