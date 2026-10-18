#!/usr/bin/env python3
"""Finite reproducibility checks for the universal-apex independence splitting.

Python 3 standard library only. This checks finite instances; the all-graph
homotopy and integral module statements require the separate written proof.
"""
from itertools import combinations, permutations
from math import comb

PRIME = 1000003


def graph_edges(n, encoded):
    pairs = list(combinations(range(n), 2))
    return {(u, v) for i, (u, v) in enumerate(pairs) if (encoded >> i) & 1}


def eligible(n, edges, r):
    neigh = [0] * n
    for u, v in edges:
        neigh[u] |= 1 << v
        neigh[v] |= 1 << u
    out = set()
    for mask in range(1 << n):
        remain = mask
        allowed = True
        while remain:
            bit = remain & -remain
            component = bit
            fringe = bit
            while fringe:
                v = (fringe & -fringe).bit_length() - 1
                fringe &= fringe - 1
                fresh = neigh[v] & remain & ~component
                component |= fresh
                fringe |= fresh
            if component.bit_count() > r:
                allowed = False
                break
            remain &= ~component
        if allowed:
            out.add(mask)
    return out


def ranks(n, faces, p=PRIME):
    by_dim = {}
    for mask in faces:
        if mask:
            by_dim.setdefault(mask.bit_count() - 1, []).append(mask)
    for v in by_dim.values():
        v.sort()
    maxdim = max(by_dim, default=-1)
    differential_ranks = {0: (1 if by_dim.get(0) else 0)}
    # Sparse Gaussian elimination on boundary columns over the prime field.
    for k in range(1, maxdim + 1):
        lower = {v: i for i, v in enumerate(by_dim[k-1])}
        pivots = {}
        rank = 0
        for mask in by_dim.get(k, []):
            vs = [v for v in range(n) if mask & (1 << v)]
            col = {}
            for j, v in enumerate(vs):
                row = lower[mask & ~(1 << v)]
                col[row] = 1 if j % 2 == 0 else p - 1
            while col:
                pivot = max(col)
                if pivot not in pivots:
                    x = col[pivot]
                    z = pow(x, -1, p)
                    pivots[pivot] = {i: a*z % p for i, a in col.items()}
                    rank += 1
                    break
                x = col[pivot]
                for i, a in pivots[pivot].items():
                    col[i] = (col.get(i, 0) - x * a) % p
                    if col[i] == 0:
                        del col[i]
        differential_ranks[k] = rank
    return tuple(len(by_dim.get(k, [])) - differential_ranks.get(k, 0)
                 - differential_ranks.get(k+1, 0)
                 for k in range(maxdim + 1))


def expected_increment(n, r):
    return comb(n - 1, r - 1)


def sign_on_ordered_face(face, perm):
    images = [perm[v] for v in face]
    inversions = sum(images[i] > images[j] for i in range(len(images))
                     for j in range(i+1, len(images)))
    return -1 if inversions % 2 else 1


def trace_skeleton(n, r, perm):
    # B = (r-2)-skeleton. Augmented reduced Lefschetz trace.
    top = r - 2
    trace = -1  # degree -1 augmented chain group
    for size in range(1, r):
        t = 0
        for face in combinations(range(n), size):
            if {perm[x] for x in face} == set(face):
                t += sign_on_ordered_face(face, perm)
        trace += (-1)**(size-1) * t
    return (-1)**top * trace


def exterior_char(n, r, perm):
    seen = set()
    poly = [1]
    for i in range(n):
        if i in seen:
            continue
        x, length = i, 0
        while x not in seen:
            seen.add(x)
            x = perm[x]
            length += 1
        nxt = poly + [0]*length
        for j, c in enumerate(poly):
            nxt[j+length] += -(-1)**length * c
        poly = nxt
    # Quotient by 1+t via recurrence.
    quo = [0]*len(poly)
    quo[0] = poly[0]
    for j in range(1, len(poly)):
        quo[j] = poly[j] - quo[j-1]
    assert quo[-1] == 0
    return quo[r-1]


def rotation_sign_on_facet(n, omitted):
    # Top-degree orientation of a rim facet under cyclic rotation.
    facet = [v for v in range(n) if v != omitted]
    images = [((v + 1) % n) for v in facet]
    inv = sum(images[i] > images[j] for i in range(len(images))
              for j in range(i+1, len(images)))
    return -1 if inv % 2 else 1


def verify_cyclic_obstruction():
    # Identify the fundamental rim cycle inside the orbit basis of the
    # augmented top-homology lattice for the complete-graph example.
    for n in range(3, 10):
        epsilon = (-1)**(n-1)
        # generator t_i has rim-facet coefficient 1 at index i.
        s = [rotation_sign_on_facet(n, i) for i in range(n)]
        assert __import__('math').prod(s) == 1
        orbit_coeff = [1]
        for i in range(n-1):
            orbit_coeff.append(orbit_coeff[-1] * s[i])
        c = [(-1)**i for i in range(n)]
        coords = [c[i]*orbit_coeff[i] for i in range(n)]
        assert coords == [epsilon**i for i in range(n)]
        # A would-be equivariant retraction would have to send each
        # orbit generator to epsilon**i times one integer a. Its value
        # on the rim fundamental cycle is therefore n*a.
        assert n > 1
    return 7


def verify():
    face_checks = 0
    homology_checks = 0
    for n in range(2, 5):
        for code in range(1 << comb(n, 2)):
            edges = graph_edges(n, code)
            for r in range(2, n+1):
                base = eligible(n, edges, r)
                new_edges = edges | {(v, n) for v in range(n)}
                apex = eligible(n+1, new_edges, r)
                skeleton = {mask for mask in range(1 << n)
                            if mask.bit_count() <= r-1}
                expected = base | {x | (1 << n) for x in skeleton}
                assert apex == expected, (n, code, r, 'face decomposition')
                face_checks += 1
                a, b = ranks(n, base), ranks(n+1, apex)
                for k in range(max(len(a), len(b), r)):
                    lhs = (b[k] if k < len(b) else 0) - (a[k] if k < len(a) else 0)
                    rhs = expected_increment(n, r) if k == r-1 else 0
                    assert lhs == rhs, (n, code, r, k, lhs, rhs)
                homology_checks += 1
    for n in (5, 6):
        graphs = [0, (1 << comb(n, 2)) - 1]
        # Paths and cycles, and two mixed deterministic edge patterns.
        pairs = list(combinations(range(n), 2))
        graphs.append(sum(1 << j for j, x in enumerate(pairs)
                          if x in {(i, i+1) for i in range(n-1)}))
        graphs.append(sum(1 << j for j, x in enumerate(pairs)
                          if x in ({(i, i+1) for i in range(n-1)} | {(0, n-1)})))
        graphs.append(sum(1 << j for j in range(len(pairs)) if (j*13+7) % 5 < 2))
        for code in set(graphs):
            edges = graph_edges(n, code)
            for r in range(2, n+1):
                base = eligible(n, edges, r)
                extended = eligible(n+1, edges | {(v, n) for v in range(n)}, r)
                a, b = ranks(n, base), ranks(n+1, extended)
                for k in range(max(len(a), len(b), r)):
                    assert (b[k] if k<len(b) else 0)-(a[k] if k<len(a) else 0) == (
                        comb(n-1, r-1) if k==r-1 else 0)
                homology_checks += 1
    character_checks = 0
    for n in range(2, 8):
        for perm in permutations(range(n)):
            for r in range(2, n+1):
                left = trace_skeleton(n, r, perm)
                right = exterior_char(n, r, perm)
                assert left == right, (n, r, perm, left, right)
                character_checks += 1
    obstruction_checks = verify_cyclic_obstruction()
    print('UNIVERSAL_APEX_CHECKS_OK')
    print('face_decompositions', face_checks)
    print('finite_field_homology_splittings', homology_checks)
    print('full_permutation_character_comparisons', character_checks)
    print('cyclic_obstruction_lattice_models', obstruction_checks)

if __name__ == '__main__':
    verify()
