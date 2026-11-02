#!/usr/bin/env python3
"""Finite checker for cyclic binary complement-free four-factors.

Standard-library only. Every classification step ranges over a fixed finite set
of de Bruijn graphs, not over source lengths; this supports an all-length proof.
"""
from itertools import product
from collections import deque

# A four-bit factor e is the edge from its first three bits (e >> 1)
# to its last three bits (e & 7) in the binary order-three de Bruijn graph.
# Each edge set below lists integers whose 4-bit expansions are its factors.
FAMILIES = (
    frozenset((0, 1, 2, 5, 6, 8, 11, 12)),
    frozenset((0, 1, 3, 4, 6, 8, 10, 13)),
    frozenset((2, 5, 7, 9, 11, 12, 14, 15)),
    frozenset((3, 4, 7, 9, 10, 13, 14, 15)),
    frozenset((0, 1, 2, 4, 8, 9)),
    frozenset((6, 7, 11, 13, 14, 15)),
)


def recurrent_components(edges):
    """Return edge sets of the nontrivial recurrent SCCs, plus loop SCCs."""
    edges = frozenset(edges)
    adj = [[] for _ in range(8)]
    for e in edges:
        adj[e >> 1].append(e & 7)
    reach = []
    for v in range(8):
        seen = {v}
        todo = [v]
        while todo:
            for t in adj[todo.pop()]:
                if t not in seen:
                    seen.add(t)
                    todo.append(t)
        reach.append(seen)
    unseen = set(range(8))
    out = []
    while unseen:
        v = min(unseen)
        group = {w for w in unseen if w in reach[v] and v in reach[w]}
        assert v in group
        unseen.difference_update(group)
        inside = frozenset(e for e in edges if (e >> 1) in group
                           and (e & 7) in group)
        if len(group) > 1 or any((e >> 1) == (e & 7)
                                  for e in inside):
            out.append(inside)
    return out


def trace_power(edges, n):
    """Exact trace of the nth power of the eight-vertex adjacency matrix."""
    A = [[0] * 8 for _ in range(8)]
    for e in edges:
        A[e >> 1][e & 7] += 1
    P = [row[:] for row in A]
    for _ in range(1, n):
        P = [[sum(P[i][k] * A[k][j] for k in range(8))
              for j in range(8)] for i in range(8)]
    return sum(P[i][i] for i in range(8))


def det_coefficients(edges):
    """Newton identities: det(I-z A) from the first eight traces."""
    traces = [0] + [trace_power(edges, j) for j in range(1, 9)]
    coeff = [1]
    for j in range(1, 9):
        number = -sum(coeff[j - i] * traces[i] for i in range(1, j + 1))
        assert number % j == 0
        coeff.append(number // j)
    return tuple(coeff)


def lucas_gap(gap, n):
    # trace coefficients of det(I-z A)=1-z-z^gap; n>=1.
    p = [0] * (max(n, gap) + 1)
    for j in range(1, len(p)):
        if j < gap:
            p[j] = 1
        elif j == gap:
            p[j] = gap + 1
        else:
            p[j] = p[j - 1] + p[j - gap]
    return p[n]


def expected(n):
    return 4 * lucas_gap(7, n) + 2 * lucas_gap(3, n) - 4


def valid(word):
    n = len(word)
    seen = {tuple(word[(i + j) % n] for j in range(4))
            for i in range(n)}
    return all(tuple(1 - b for b in factor) not in seen
               for factor in seen)


def has_both_double_runs(word):
    n = len(word)
    doubles = {(word[i], word[(i + 1) % n]) for i in range(n)}
    return (0, 0) in doubles and (1, 1) in doubles


def check():
    # All six named graphs obey complementary exclusion, individually.
    pairs = tuple((e, 15 ^ e) for e in range(16) if e < (15 ^ e))
    assert len(pairs) == 8
    for f in FAMILIES:
        for a, b in pairs:
            assert not (a in f and b in f)

    # Every admissible cyclic word lies in at least one of six graphs:
    # choose an allowed orientation of each of the eight complement pairs.
    # A closed walk lies in one SCC; check the SCC's edges are included
    # in a named graph. These are precisely 256 exhaustive cases.
    checked_components = 0
    for bits in product((0, 1), repeat=8):
        allowed = {pairs[i][c] for i, c in enumerate(bits)}
        for component in recurrent_components(allowed):
            checked_components += 1
            assert any(component <= family for family in FAMILIES), (bits, component)
    assert checked_components > 256

    # Any common cyclic walk in two different graphs must be all zero
    # or all one. For each edge-set intersection, test ALL recurrent SCCs.
    for i in range(6):
        for j in range(i + 1, 6):
            for component in recurrent_components(FAMILIES[i] & FAMILIES[j]):
                assert component in (frozenset((0,)), frozenset((15,)))

    # Reconstruct characteristic polynomials from exact integer matrix
    # traces, checking every coefficient, not just leading eigenvalues.
    for i, f in enumerate(FAMILIES):
        gap = 7 if i < 4 else 3
        target = tuple(1 if j == 0 else -1 if j in (1, gap) else 0
                       for j in range(9))
        assert det_coefficients(f) == target, (i, det_coefficients(f))

    # Independent brute force: enumerate all marked binary circular words,
    # without using graph classification.
    instances = 0
    counts = {}
    for n in range(4, 17):
        good = with_both = 0
        for val in range(1 << n):
            word = [(val >> i) & 1 for i in range(n)]
            if valid(word):
                good += 1
                with_both += has_both_double_runs(word)
            instances += 1
        assert good == expected(n), (n, good, expected(n))
        assert with_both == 4 * (lucas_gap(7, n) - 1), (n, with_both)
        counts[n] = good
    assert counts[7] == 58 and counts[12] == 244 and counts[16] == 1066

    # Independent transfer-matrix check beyond brute-force lengths.
    for n in range(1, 31):
        transfer = sum(trace_power(f, n) for f in FAMILIES) - 4
        assert transfer == expected(n), n
    print('VERIFY_OK; orientations=256; recurrent_SCCs=%d; families=6; '
          'pair_intersections=15; bruteforce_instances=%d; lengths=4..16; '
          'transfer_lengths=1..30' % (checked_components, instances))
    print('A_n (n=4..16):', [counts[n] for n in range(4,17)])


if __name__ == '__main__':
    check()
