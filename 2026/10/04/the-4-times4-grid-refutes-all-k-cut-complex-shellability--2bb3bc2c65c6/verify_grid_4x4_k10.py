#!/usr/bin/env python3
from itertools import combinations

ROWS = 4
COLS = 4
K = 10
N = ROWS * COLS
FULL = (1 << N) - 1
EXPECTED_F_VECTOR = [16, 120, 560, 1820, 4344, 5722]
EXPECTED_RANKS = {1: 15, 2: 105, 3: 455, 4: 1365, 5: 2975}
EXPECTED_BETTI = [1, 0, 0, 0, 4, 2747]


def vertex(i, j):
    return i * COLS + j


def adjacency():
    adj = [0] * N
    for i in range(ROWS):
        for j in range(COLS):
            u = vertex(i, j)
            if i + 1 < ROWS:
                v = vertex(i + 1, j)
                adj[u] |= 1 << v
                adj[v] |= 1 << u
            if j + 1 < COLS:
                v = vertex(i, j + 1)
                adj[u] |= 1 << v
                adj[v] |= 1 << u
    return adj


def connected(mask, adj):
    if mask == 0:
        return False
    first = (mask & -mask).bit_length() - 1
    seen = 1 << first
    stack = [first]
    while stack:
        u = stack.pop()
        new = adj[u] & mask & ~seen
        while new:
            bit = new & -new
            new -= bit
            seen |= bit
            stack.append(bit.bit_length() - 1)
    return seen == mask


def masks_of_size(size):
    for comb in combinations(range(N), size):
        mask = 0
        for x in comb:
            mask |= 1 << x
        yield mask


def enumerate_faces_from_facets(facets):
    faces = {0}
    for facet in facets:
        sub = facet
        while True:
            faces.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & facet
    return faces


def enumerate_faces_direct(disconnected_k):
    disconnected = set(disconnected_k)
    faces = {0}
    for size in range(1, N - K + 1):
        for face in masks_of_size(size):
            comp_vertices = [v for v in range(N) if not ((face >> v) & 1)]
            found = False
            for comb in combinations(comp_vertices, K):
                s = 0
                for v in comb:
                    s |= 1 << v
                if s in disconnected:
                    found = True
                    break
            if found:
                faces.add(face)
    return faces


def boundary_columns(high_faces, low_index):
    cols = []
    for face in high_faces:
        col = 0
        z = face
        while z:
            bit = z & -z
            z -= bit
            col ^= 1 << low_index[face ^ bit]
        cols.append(col)
    return cols


def rank_bit_columns(columns):
    basis = {}
    for col in columns:
        x = col
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def rank_bit_rows(columns, nrows):
    # Independent transpose construction and row-space elimination.
    rows = [0] * nrows
    for j, col in enumerate(columns):
        z = col
        while z:
            bit = z & -z
            z -= bit
            i = bit.bit_length() - 1
            rows[i] |= 1 << j
    basis = {}
    for row in rows:
        x = row
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def main():
    adj = adjacency()
    assert sum(a.bit_count() for a in adj) // 2 == 24

    disconnected_k = []
    connected_count = 0
    for mask in masks_of_size(K):
        if connected(mask, adj):
            connected_count += 1
        else:
            disconnected_k.append(mask)

    assert connected_count + len(disconnected_k) == 8008
    assert connected_count == 2286
    assert len(disconnected_k) == 5722

    facets = [FULL ^ mask for mask in disconnected_k]
    assert len(set(facets)) == 5722
    assert all(f.bit_count() == 6 for f in facets)

    faces_a = enumerate_faces_from_facets(facets)
    faces_b = enumerate_faces_direct(disconnected_k)
    assert faces_a == faces_b

    by_dim = {}
    for face in faces_a:
        if face:
            by_dim.setdefault(face.bit_count() - 1, []).append(face)
    for d in by_dim:
        by_dim[d].sort()

    f_vector = [len(by_dim[d]) for d in range(6)]
    assert f_vector == EXPECTED_F_VECTOR

    ranks = {}
    boundaries = {}
    for d in range(1, 6):
        low = by_dim[d - 1]
        high = by_dim[d]
        low_index = {f: i for i, f in enumerate(low)}
        cols = boundary_columns(high, low_index)
        boundaries[d] = cols
        rank_a = rank_bit_columns(cols)
        rank_b = rank_bit_rows(cols, len(low))
        assert rank_a == rank_b
        ranks[d] = rank_a
    assert ranks == EXPECTED_RANKS

    # Check d_{d-1} d_d = 0 over F_2 using the actual boundary data.
    for d in range(2, 6):
        low_faces = by_dim[d - 1]
        low_index = {f: i for i, f in enumerate(low_faces)}
        prev_cols = boundaries[d - 1]
        for face in by_dim[d]:
            accum = 0
            z = face
            while z:
                bit = z & -z
                z -= bit
                accum ^= prev_cols[low_index[face ^ bit]]
            assert accum == 0

    betti = []
    for d in range(6):
        betti.append(len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0))
    assert betti == EXPECTED_BETTI

    euler_faces = sum(((-1) ** d) * f_vector[d] for d in range(6))
    euler_homology = sum(((-1) ** d) * betti[d] for d in range(6))
    assert euler_faces == euler_homology == -2742

    # A pure shellable 5-complex has reduced homology only in degree 5.
    assert betti[4] == 4 > 0

    print('grid_edges=24')
    print('ten_subsets=8008 connected=2286 disconnected=5722')
    print('f_vector=' + repr(f_vector))
    print('boundary_ranks_F2=' + repr([ranks[d] for d in range(1, 6)]))
    print('betti_F2=' + repr(betti))
    print('reduced_betti_F2=[0,0,0,0,4,2747]')
    print('euler_characteristic=-2742')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
