#!/usr/bin/env python3
"""Exact, standalone integer-chain certificate for Folkman vertex-ball nerves.

Requires only Python 3 standard library. Bit positions label the twenty vertices.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from heapq import heapify, heappop, heappush


def bits(x):
    while x:
        b = x & -x
        yield b
        x ^= b


def graph_and_distances():
    # Point twins are 2*i+s (i=0..4, s=0,1), edge vertices are 10..19.
    vertices = list(range(20))
    edges = list(combinations(range(5), 2))
    adj = {u: set() for u in vertices}
    for t, (i, j) in enumerate(edges):
        w = 10+t
        for z in (2*i, 2*i+1, 2*j, 2*j+1):
            adj[w].add(z)
            adj[z].add(w)
    assert len(vertices) == 20 and sum(map(len, adj.values())) == 80
    assert all(len(adj[u]) == 4 for u in vertices)
    d = {}
    for s in vertices:
        ds = {s: 0}
        q = deque([s])
        while q:
            a = q.popleft()
            for b in sorted(adj[a]):
                if b not in ds:
                    ds[b] = ds[a]+1
                    q.append(b)
        assert len(ds) == 20
        d[s] = ds
    assert max(max(x.values()) for x in d.values()) == 4
    assert all(max(d[2*i].values()) == 3 for i in range(5))
    return vertices, adj, d


def ball_faces(vertices, d, radius):
    balls = [sum(1 << v for v in vertices if d[w][v] <= radius)
             for w in vertices]
    maximal = sorted({b for b in balls if not any(
        b != other and (b & other) == b for other in balls)})
    faces = set()
    for facet in maximal:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub-1) & facet
    return balls, maximal, faces


def elementary_collapses(original):
    """Return residual faces, number of certified elementary free-face pairs.

    A face with a unique *immediate* coface has no higher coface in a
    simplicial complex: a higher coface would yield two immediate ones.
    Every actual pair is rechecked against the active coface incidence.
    """
    faces = set(original)
    co = defaultdict(set)
    for f in faces:
        for one in bits(f):
            a = f ^ one
            if a:
                co[a].add(f)
    heap = [(-f.bit_count(), f) for f in faces
            if f.bit_count() > 1 and any(len(co[f ^ bit]) == 1 for bit in bits(f))]
    heapify(heap)
    pairs = 0
    while heap:
        _, f = heappop(heap)
        if f not in faces:
            continue
        a = next((f ^ b for b in bits(f)
                  if len(co[f ^ b]) == 1 and f in co[f ^ b]), None)
        if a is None:
            continue
        assert a in faces and co[a] == {f}
        # Uniqueness of the immediate coface suffices for freeness.
        faces.remove(f)
        faces.remove(a)
        pairs += 1
        for deleted in (f, a):
            for b in bits(deleted):
                lower = deleted ^ b
                if lower and deleted in co[lower]:
                    co[lower].remove(deleted)
                    if len(co[lower]) == 1 and lower in faces:
                        parent = next(iter(co[lower]))
                        heappush(heap, (-parent.bit_count(), parent))
    assert 2 * pairs + len(faces) == len(original)
    assert all((f ^ b) in faces for f in faces for b in bits(f) if f ^ b)
    return faces, pairs


def boundary(faces, degree):
    high = sorted(f for f in faces if f.bit_count() == degree + 1)
    low = sorted(f for f in faces if f.bit_count() == degree)
    idx = {f: i for i, f in enumerate(low)}
    cols, rows = {}, defaultdict(dict)
    for j, f in enumerate(high):
        entries = {}
        for pos, one in enumerate(bits(f)):
            i = idx[f ^ one]
            v = (-1) ** pos
            entries[i] = v
            rows[i][j] = v
        cols[j] = entries
    for i in range(len(low)):
        rows[i]  # zero rows included
    return cols, dict(rows), len(low), len(high)


def integral_unit_diagonalization(col0, row0):
    """Integer unit-pivot row/column operations; no division other than by ±1.

    Each unit pivot splits an integral direct summand. When the remaining
    matrix is zero, all Smith invariants are 1, so no torsion is hidden.
    """
    cols = {j: dict(c) for j, c in col0.items()}
    rows = {i: dict(c) for i, c in row0.items()}
    rank, max_abs = 0, 1
    while True:
        best = None
        for j, col in cols.items():
            for i, v in col.items():
                if abs(v) != 1:
                    continue
                score = (len(col)-1)*(len(rows[i])-1)
                if best is None or score < best[0]:
                    best = (score, i, j, v)
                if score == 0:
                    break
            if best and best[0] == 0:
                break
        if best is None:
            break
        _, i, j, pivot = best
        source_col = dict(cols[j])
        source_row = dict(rows[i])
        assert source_col[i] == source_row[j] == pivot
        for other_j, b in source_row.items():
            if other_j == j:
                continue
            target = cols[other_j]
            for other_i, a in source_col.items():
                if other_i == i:
                    continue
                value = target.get(other_i, 0) - a*b*pivot
                if value:
                    target[other_i] = value
                    rows[other_i][other_j] = value
                    max_abs = max(max_abs, abs(value))
                else:
                    target.pop(other_i, None)
                    rows[other_i].pop(other_j, None)
            target.pop(i, None)
        for other_i in source_col:
            if other_i != i:
                rows[other_i].pop(j, None)
        del rows[i]
        del cols[j]
        rank += 1
    assert all(not c for c in cols.values()), 'Unresolved nonunit Smith block'
    assert all(not c for c in rows.values()), 'Remaining integer boundary not zero'
    return rank, max_abs


def gf2_rank(faces, degree):
    high = (f for f in faces if f.bit_count() == degree+1)
    low = sorted(f for f in faces if f.bit_count() == degree)
    index = {f: i for i, f in enumerate(low)}
    basis = {}
    for f in high:
        c = 0
        for one in bits(f):
            c ^= (1 << index[f ^ one])
        while c:
            p = c.bit_length()
            if p not in basis:
                basis[p] = c
                break
            c ^= basis[p]
    return len(basis)


def verify_one(radius, expected_faces, expected_pairs, expected_vector,
               expected_ranks, expected_betti):
    vertices, adj, d = graph_and_distances()
    balls, maxima, faces = ball_faces(vertices, d, radius)
    assert len(faces) == expected_faces
    assert all(any((f & b) == f for b in balls) for f in faces)
    if radius == 1:
        assert len(maxima) == 20 and all(m.bit_count() == 5 for m in maxima)
    elif radius == 2:
        assert len(maxima) == 15 and Counter(m.bit_count() for m in maxima) == {11:10, 14:5}
    smaller, pairs = elementary_collapses(faces)
    assert pairs == expected_pairs
    fvec = [sum(f.bit_count() == k+1 for f in smaller)
            for k in range(max(f.bit_count() for f in smaller))]
    assert fvec == expected_vector
    ranks, maxima_abs = {}, {}
    for dimension in range(1, len(fvec)):
        cols, rows, nrows, ncols = boundary(smaller, dimension)
        assert (nrows, ncols) == (fvec[dimension-1], fvec[dimension])
        rank, max_abs = integral_unit_diagonalization(cols, rows)
        assert rank == gf2_rank(smaller, dimension)
        ranks[dimension] = rank
        maxima_abs[dimension] = max_abs
    assert [ranks.get(k, 0) for k in range(1, len(fvec))] == expected_ranks
    betti = [fvec[k] - ranks.get(k,0) - ranks.get(k+1,0)
             for k in range(len(fvec))]
    assert betti == expected_betti
    reduced = [betti[0]-1] + betti[1:]
    print('radius', radius, 'full_faces', len(faces), 'maximal_facets', len(maxima),
          'collapse_pairs', pairs, 'residual_fvec', fvec,
          'integral_boundary_ranks', expected_ranks, 'ordinary_betti', betti,
          'maximum_intermediate_coefficients', maxima_abs,
          'all_Smith_invariants_one', True)
    return reduced


def main():
    vertices, adj, d = graph_and_distances()
    assert len(ball_faces(vertices,d,0)[2]) == 20
    # A twin point has eccentricity 3, so radius 3 contains all vertices.
    assert max(d[0].values()) == 3
    b1 = verify_one(1,430,130,[20,80,70],[19,55],[1,6,15])
    b2 = verify_one(2,81233,39641,[19,159,558,811,404],
                    [18,141,417,389],[1,0,0,5,15])
    assert b1 == [0,6,15] and b2 == [0,0,0,5,15]
    print('radius 0: 20 discrete points; radius >=3: a full 19-simplex')
    print('VERIFY_OK: exact integer homology and full vertex-witness barcode')


if __name__ == '__main__':
    main()
