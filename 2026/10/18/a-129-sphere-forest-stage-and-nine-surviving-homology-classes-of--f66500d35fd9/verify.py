#!/usr/bin/env python3
"""Exact integral boundary and inclusion verifier for cube vertex-forest complexes.
Uses only Python's standard library; all matrices and masks are reconstructed.
"""
from collections import defaultdict
import heapq

VERTICES = tuple(range(16))
NEIGHBORS = tuple(sum(1 << (v ^ (1 << a)) for a in range(4)) for v in VERTICES)
EXPECTED_A = (16, 120, 560, 1732, 3552, 4616, 3392, 922)
EXPECTED_B = (16, 120, 560, 1796, 4080, 6488, 6848, 4090, 1008, 8)
EXPECTED_A_RANK = (15, 105, 455, 1277, 2275, 2341, 922)
EXPECTED_B_MOD2_RANK = (15, 105, 455, 1341, 2739, 3749, 3090, 1000, 8)


def is_face(mask, degree_limit):
    """Validate acyclicity with disjoint sets and bounded induced degree."""
    parents = list(VERTICES)

    def root(x):
        while parents[x] != x:
            x = parents[x]
        return x

    for v in VERTICES:
        if mask >> v & 1:
            if degree_limit is not None and (NEIGHBORS[v] & mask).bit_count() > degree_limit:
                return False
            for w in range(v + 1, 16):
                if (mask >> w & 1) and (NEIGHBORS[v] >> w & 1):
                    a, b = root(v), root(w)
                    if a == b:
                        return False
                    parents[a] = b
    return True


def enumerate_faces(degree_limit):
    faces = defaultdict(list)
    for mask in range(1 << 16):
        if is_face(mask, degree_limit):
            faces[mask.bit_count() - 1].append(mask)
    return dict(faces)


def boundary_columns(faces, k):
    assert k > 0
    lower = {mask: row for row, mask in enumerate(faces[k - 1])}
    cols = []
    for mask in faces[k]:
        col = {}
        position = 0
        for v in VERTICES:
            if mask >> v & 1:
                col[lower[mask ^ (1 << v)]] = -1 if position % 2 else 1
                position += 1
        assert len(col) == k + 1
        cols.append(col)
    return cols, len(lower)


def integer_unit_rank(columns, nrows):
    """Unimodular row/column elimination; fail if residual nonzero entries remain."""
    cols = [dict(c) for c in columns]
    rows = [{} for _ in range(nrows)]
    for j, col in enumerate(cols):
        for i, z in col.items():
            rows[i][j] = z
    heap = []

    def offer(i, j):
        if abs(cols[j].get(i, 0)) == 1:
            cost = (len(cols[j]) - 1) * (len(rows[i]) - 1)
            heapq.heappush(heap, (cost, max(len(cols[j]), len(rows[i])), i, j))

    for i, row in enumerate(rows):
        for j, z in row.items():
            if abs(z) == 1:
                offer(i, j)
    rank = 0
    while heap:
        cost, _, i, j = heapq.heappop(heap)
        if not rows[i] or not cols[j] or abs(cols[j].get(i, 0)) != 1:
            continue
        updated_cost = (len(cols[j]) - 1) * (len(rows[i]) - 1)
        if updated_cost > cost:
            heapq.heappush(heap, (updated_cost, max(len(cols[j]), len(rows[i])), i, j))
            continue
        coefficient = cols[j][i]
        pivot_col = cols[j]
        pivot_row = list(rows[i].items())
        for k, z in pivot_row:
            if k == j:
                continue
            multiplier = z // coefficient
            other = cols[k]
            for ii, zz in pivot_col.items():
                if ii == i:
                    continue
                new = other.get(ii, 0) - multiplier * zz
                if new:
                    other[ii] = new
                    rows[ii][k] = new
                    if abs(new) == 1:
                        offer(ii, k)
                else:
                    other.pop(ii, None)
                    rows[ii].pop(k, None)
            other.pop(i, None)
        for ii in pivot_col:
            rows[ii].pop(j, None)
        cols[j] = {}
        rows[i] = {}
        rank += 1
        for ii in pivot_col:
            if ii != i:
                for k in rows[ii]:
                    if abs(cols[k].get(ii, 0)) == 1:
                        offer(ii, k)
        for k, _ in pivot_row:
            if k != j:
                for ii in cols[k]:
                    if abs(cols[k].get(ii, 0)) == 1:
                        offer(ii, k)
    assert all(not col for col in cols), 'Nonzero residual matrix: not fully resolved by unit pivots'
    assert all(not row for row in rows)
    return rank


def basis_add(basis, bitvector):
    while bitvector:
        h = bitvector.bit_length() - 1
        if h in basis:
            bitvector ^= basis[h]
        else:
            basis[h] = bitvector
            return True
    return False


def gf2_rank(columns):
    basis = {}
    for c in columns:
        basis_add(basis, sum(1 << i for i in c))
    return len(basis)


def gf2_kernel(columns):
    basis = {}
    cycles = []
    for j, col in enumerate(columns):
        image = sum(1 << i for i in col)
        chain = 1 << j
        while image:
            h = image.bit_length() - 1
            if h in basis:
                bb, cc = basis[h]
                image ^= bb
                chain ^= cc
            else:
                basis[h] = (image, chain)
                break
        else:
            cycles.append(chain)
    return cycles


def mod2_inclusion_rank(A, B, k):
    assert set(A[k]).issubset(B[k])
    src_c, _ = boundary_columns(A, k)
    target_boundary, _ = boundary_columns(B, k + 1)
    cycles = gf2_kernel(src_c)
    target_indexes = {mask: j for j, mask in enumerate(B[k])}
    embedding = [target_indexes[m] for m in A[k]]
    basis = {}
    for c in target_boundary:
        basis_add(basis, sum(1 << i for i in c))
    boundary_rank = len(basis)
    image_rank = 0
    for cycle in cycles:
        image = 0
        while cycle:
            bit = cycle & -cycle
            image ^= 1 << embedding[bit.bit_length() - 1]
            cycle ^= bit
        if basis_add(basis, image):
            image_rank += 1
    return image_rank, boundary_rank, len(cycles)


def check_chain(faces):
    for k in range(2, max(faces) + 1):
        c1, _ = boundary_columns(faces, k)
        c0, _ = boundary_columns(faces, k - 1)
        for col in c1:
            d = {}
            for j, x in col.items():
                for i, y in c0[j].items():
                    d[i] = d.get(i, 0) + x * y
            assert not any(d.values()), ('boundary square', k)


def main():
    A = enumerate_faces(2)
    B = enumerate_faces(None)
    assert [len(A[k]) for k in range(8)] == list(EXPECTED_A)
    assert [len(B[k]) for k in range(10)] == list(EXPECTED_B)
    assert len(A[-1]) == len(B[-1]) == 1
    assert all(is_face(s ^ (1 << v), 2) for k in range(1, 8) for s in A[k] for v in VERTICES if s >> v & 1)
    check_chain(A)
    check_chain(B)
    ranks = []
    for k in range(1, 8):
        c, n = boundary_columns(A, k)
        r = integer_unit_rank(c, n)
        assert r == EXPECTED_A_RANK[k - 1], (k, r)
        assert gf2_rank(c) == r, ('mod-two mismatch', k)
        ranks.append(r)
    betti_a = [len(A[k]) - (ranks[k-1] if k else 1) - (ranks[k] if k < 7 else 0) for k in range(8)]
    # For k=0 the reduced augmentation has rank one; for k>=1 use previous boundary.
    assert betti_a == [0, 0, 0, 0, 0, 0, 129, 0], betti_a
    assert -1 + sum((-1) ** k * len(A[k]) for k in range(8)) == 129
    ranks_b = [gf2_rank(boundary_columns(B, k)[0]) for k in range(1, 10)]
    assert ranks_b == list(EXPECTED_B_MOD2_RANK), ranks_b
    betti_b = [len(B[k]) - (ranks_b[k - 1] if k else 1) - (ranks_b[k] if k < 9 else 0) for k in range(10)]
    assert betti_b == [0, 0, 0, 0, 0, 0, 9, 0, 0, 0], betti_b
    assert -1 + sum((-1) ** k * len(B[k]) for k in range(10)) == 9
    rank, target_boundaries, source_cycles = mod2_inclusion_rank(A, B, 6)
    assert (rank, target_boundaries, source_cycles) == (9, 3090, 1051)
    print('A_faces=', EXPECTED_A)
    print('A_signed_integer_unit_ranks=', tuple(ranks))
    print('A_integral_reduced_homology=Z^129 in degree 6 only')
    print('B_faces=', EXPECTED_B)
    print('B_mod2_boundary_ranks=', tuple(ranks_b))
    print('B_mod2_reduced_homology=F2^9 in degree 6 only')
    print('B_reduced_Euler_characteristic=9')
    print('A_to_B_degree_6_mod2_image_rank=9')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
