#!/usr/bin/env python3
"""Finite checks of a general homotopy and symmetry formula for 2-independence complexes.
Run with Python 3.10 or newer. No nonstandard dependencies.
"""
from itertools import product
from collections import Counter
from math import prod


def make_tree(branch_sizes):
    assert len(branch_sizes) >= 2 and min(branch_sizes) >= 1
    a = len(branch_sizes)
    edges = [(0, i) for i in range(1, a + 1)]
    branches = []
    next_vertex = a + 1
    for i, b in enumerate(branch_sizes):
        leaves = tuple(range(next_vertex, next_vertex + b))
        next_vertex += b
        branches.append(leaves)
        edges.extend((i + 1, z) for z in leaves)
    return next_vertex, edges, tuple(branches)


def enumerate_faces(n, edges):
    nbr = [0] * n
    for u, v in edges:
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
    faces = []
    for s in range(1 << n):
        # In a tree, a connected component of size >= 3 includes a
        # vertex with two selected neighbors.
        if all(not(s & (1 << u)) or (nbr[u] & s).bit_count() <= 1
               for u in range(n)):
            faces.append(s)
    return faces


def matching_remaining(faces, pivots):
    remaining = set(faces)
    pairs = 0
    for v in pivots:
        bit = 1 << v
        matched = [(s, s | bit) for s in remaining
                   if not(s & bit) and (s | bit) in remaining]
        for lo, hi in matched:
            remaining.remove(lo)
            remaining.remove(hi)
        pairs += len(matched)
    return remaining, pairs


def acyclic_hasse_check(faces, pivots, n):
    """Verify acyclicity for all augmented Hasse incidence orientations."""
    from collections import deque
    fs = set(faces)
    remainder = set(faces)
    paired = set()
    for v in pivots:
        bit = 1 << v
        new_pairs = [(s, s | bit) for s in remainder
                     if not (s & bit) and (s | bit) in remainder]
        for lo, hi in new_pairs:
            remainder.remove(lo)
            remainder.remove(hi)
            paired.add((lo, hi))
    adjacency = {s: [] for s in fs}
    indeg = {s: 0 for s in fs}
    incidences = 0
    for lo in fs:
        for v in range(n):
            hi = lo | (1 << v)
            if hi == lo or hi not in fs:
                continue
            # Matched covers point upward; all other covers point downward.
            src, dst = (lo, hi) if (lo, hi) in paired else (hi, lo)
            adjacency[src].append(dst)
            indeg[dst] += 1
            incidences += 1
    q = deque(s for s in fs if indeg[s] == 0)
    seen = 0
    while q:
        src = q.popleft()
        seen += 1
        for dst in adjacency[src]:
            indeg[dst] -= 1
            if indeg[dst] == 0:
                q.append(dst)
    assert seen == len(fs), (seen, len(fs), incidences)
    return incidences


def gf2_betti(faces, n):
    by_card = [[] for _ in range(n + 1)]
    for s in faces:
        by_card[s.bit_count()].append(s)
    boundary_rank = {}
    for k in range(1, n + 1):
        rows = {s: i for i, s in enumerate(by_card[k-1])}
        piv = {}
        for s in by_card[k]:
            bits = 0
            for v in range(n):
                if s & (1 << v):
                    bits ^= 1 << rows[s ^ (1 << v)]
            while bits:
                high = bits.bit_length()-1
                if high not in piv:
                    piv[high] = bits
                    break
                bits ^= piv[high]
        boundary_rank[k] = len(piv)
    result = {}
    for k, fs in enumerate(by_card):
        rank = len(fs) - boundary_rank.get(k, 0) - boundary_rank.get(k+1, 0)
        if rank:
            result[k-1] = rank
    return result


def permutation_trace(faces, perm):
    value = 0
    for s in faces:
        elements = [v for v in range(len(perm)) if s & (1 << v)]
        image = [perm[v] for v in elements]
        if sorted(image) != elements:
            continue
        inversions = sum(image[i] > image[j]
                         for i in range(len(image))
                         for j in range(i+1, len(image)))
        value += (-1) ** (len(elements) + inversions)
    return value


def test_case(branch_sizes):
    n, edges, branches = make_tree(branch_sizes)
    faces = enumerate_faces(n, edges)
    pivots = [leaves[0] for leaves in branches]
    crit, pairs = matching_remaining(faces, pivots)
    incidences = acyclic_hasse_check(faces, pivots, n)
    a = len(branch_sizes)
    expected_critical = {
        sum((1 << (i+1)) | (1 << leaf)
            for i, leaf in enumerate(selection))
        for selection in product(*(leaf[1:] for leaf in branches))
    }
    assert crit == expected_critical
    assert 2*pairs + len(crit) == len(faces)
    rank = prod(b-1 for b in branch_sizes)
    assert len(crit) == rank
    betti = gf2_betti(faces, n)
    assert betti == ({2*a-1: rank} if rank else {})
    ident = list(range(n))
    assert permutation_trace(faces, ident) == rank
    # A transposition among leaves has standard-representation trace b-3.
    for i, leaves in enumerate(branches):
        if len(leaves) < 2:
            continue
        p = ident.copy()
        p[leaves[0]], p[leaves[1]] = p[leaves[1]], p[leaves[0]]
        expected = (len(leaves)-3) * prod(branch_sizes[j]-1
                                        for j in range(a) if j != i)
        assert permutation_trace(faces, p) == expected
    # Exchange two branches of the same size, without a Koszul minus sign.
    for i in range(a):
        for j in range(i+1, a):
            if branch_sizes[i] != branch_sizes[j]:
                continue
            p = ident.copy()
            p[i+1], p[j+1] = p[j+1], p[i+1]
            for u, v in zip(branches[i], branches[j]):
                p[u], p[v] = p[v], p[u]
            expected = (branch_sizes[i]-1)*prod(
                branch_sizes[k]-1 for k in range(a) if k not in (i,j))
            assert permutation_trace(faces, p) == expected
    # A 3-cycle of equal arms has trace b-1, with no sign.
    if a >= 3 and branch_sizes[0] == branch_sizes[1] == branch_sizes[2]:
        p = ident.copy()
        for i in range(3):
            p[i+1] = ((i+1) % 3) + 1
            for t, leaf in enumerate(branches[i]):
                p[leaf] = branches[(i+1) % 3][t]
        expected = (branch_sizes[0]-1) * prod(
            branch_sizes[j]-1 for j in range(3, a))
        assert permutation_trace(faces, p) == expected
    # Compose a branch exchange with a transposition inside one branch.
    if a >= 2 and branch_sizes[0] == branch_sizes[1] and branch_sizes[0] >= 2:
        p = ident.copy()
        p[1], p[2] = p[2], p[1]
        for u, v in zip(branches[0], branches[1]):
            p[u], p[v] = p[v], p[u]
        u, v = branches[0][:2]
        p[u], p[v] = p[v], p[u]
        expected = (branch_sizes[0]-3) * prod(
            branch_sizes[j]-1 for j in range(2, a))
        assert permutation_trace(faces, p) == expected
    print(f'OK branches={branch_sizes} vertices={n} faces={len(faces)} incidences={incidences} '
          f'pairs={pairs} critical={len(crit)} reduced_F2_betti={betti}')


if __name__ == '__main__':
    for bs in [(1,1), (1,3), (2,2), (2,3), (2,2,3),
               (2,3,2), (3,3), (2,2,2), (3,3,3)]:
        test_case(bs)
    print('VERIFY_OK all cases and symmetry tests')
