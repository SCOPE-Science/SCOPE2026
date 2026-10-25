#!/usr/bin/env python3
"""Exact integral-chain certificate for minimal spheres of the folded-five-cube neighborhood complex.
Run: python3 verify.py certificate.json. Uses Python standard library only.
"""
import itertools
import json
import sys

D = (1, 2, 4, 8, 15)
V = tuple(range(16))
NEIGHBORHOODS = tuple(tuple(sorted(v ^ d for d in D)) for v in V)
FACES = {k: tuple(sorted({t for n in NEIGHBORHOODS
                          for t in itertools.combinations(n, k + 1)}))
         for k in range(5)}
INDEX = {k: {face: i for i, face in enumerate(FACES[k])}
         for k in range(5)}


def boundary(k, t):
    """The integral simplicial boundary of sorted (k+1)-vertex face t.
    Output uses sorted k-vertex faces indexed in FACES[k-1].
    """
    return {INDEX[k - 1][t[:i] + t[i + 1:]]: 1 if i % 2 == 0 else -1
            for i in range(k + 1)}


def compose(columns_inner, columns_outer):
    for outer in columns_outer:
        result = {}
        for j, a in outer.items():
            for i, b in columns_inner[j].items():
                result[i] = result.get(i, 0) + a * b
        assert all(v == 0 for v in result.values())


def rank_mod(columns, p):
    basis = {}
    for c in columns:
        row = {i: x % p for i, x in c.items() if x % p}
        while row:
            i = min(row)
            if i not in basis:
                u = pow(row[i], -1, p)
                basis[i] = {j: (v * u) % p for j, v in row.items()}
                break
            q = row[i]
            for j, v in basis[i].items():
                w = (row.get(j, 0) - q * v) % p
                if w:
                    row[j] = w
                else:
                    row.pop(j, None)
    return len(basis)


def select_mod2(columns):
    """Greedy lexicographic column selection over F_2, output zero-based indices."""
    basis = {}
    chosen = []
    for ix, c in enumerate(columns):
        row = {j for j, value in c.items() if value % 2}
        while row:
            i = min(row)
            if i not in basis:
                basis[i] = row.copy()
                chosen.append(ix)
                break
            row.symmetric_difference_update(basis[i])
    return chosen


def unit_pivot_determinant(a):
    """Exact Z-row/column elementary operations, using only unit pivots.
    If successful, no divisions by nonunits or floating-point computations occur.
    The resulting diagonal is plus or minus one at every step.
    """
    a = [list(map(int, row)) for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1
    for k in range(n):
        found = next(((i, j) for i in range(k, n)
                      for j in range(k, n) if abs(a[i][j]) == 1), None)
        assert found is not None, ('no unit pivot', k)
        i, j = found
        if i != k:
            a[i], a[k] = a[k], a[i]
            sign *= -1
        if j != k:
            for row in a:
                row[k], row[j] = row[j], row[k]
            sign *= -1
        pivot = a[k][k]
        assert pivot in (-1, 1)
        sign *= pivot
        for i in range(k + 1, n):
            factor = a[i][k] * pivot
            if factor:
                for j in range(k + 1, n):
                    a[i][j] -= factor * a[k][j]
            a[i][k] = 0
    assert all(a[i][j] == 0 for i in range(n) for j in range(i))
    assert all(abs(a[i][i]) == 1 for i in range(n))
    return sign


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'certificate.json'
    with open(filename, encoding='utf-8') as f:
        cert = json.load(f)
    assert cert['graph_directions'] == list(D)
    assert [len(FACES[k]) for k in range(5)] == [16, 80, 160, 80, 16]
    assert all(len(x) == 5 for x in NEIGHBORHOODS)
    assert all(len(set(x).intersection(y)) in (0, 2)
               for i, x in enumerate(NEIGHBORHOODS)
               for j, y in enumerate(NEIGHBORHOODS) if i != j)
    assert len(set(NEIGHBORHOODS)) == 16
    d1 = [{INDEX[0][(t[1],)]: 1, INDEX[0][(t[0],)]: -1}
          for t in FACES[1]]
    d2 = [boundary(2, t) for t in FACES[2]]
    d3 = [boundary(3, t) for t in FACES[3]]
    d4 = [boundary(4, t) for t in FACES[4]]
    compose(d1, d2)
    compose(d2, d3)
    compose(d3, d4)
    for p in (2, 3, 101):
        assert tuple(rank_mod(x, p) for x in (d1, d2, d3, d4)) == (15, 65, 64, 16)

    f2 = set(FACES[2]); f3 = set(FACES[3])
    missing = tuple(t for t in itertools.combinations(V, 4)
                    if t not in f3 and
                    all(s in f2 for s in itertools.combinations(t, 3)))
    assert len(missing) == 40
    affine = set()
    for triple in itertools.combinations(D, 3):
        base = (triple[0], triple[1], triple[2], triple[0] ^ triple[1] ^ triple[2])
        assert len(set(base)) == 4
        for t in V:
            affine.add(tuple(sorted(t ^ x for x in base)))
    assert len(affine) == 40
    assert affine == set(missing)

    z = [boundary(3, q) for q in missing]
    compose(d2, z)
    chosen_d3 = select_mod2(d3)
    selected = [d3[i] for i in chosen_d3]
    mod2_combined = select_mod2(selected + z)
    chosen_z = [i - len(selected) for i in mod2_combined if i >= len(selected)]
    assert chosen_d3 == cert['boundary_tetrahedra_indices']
    assert chosen_z == cert['sphere_indices']
    assert len(selected) == 64 and len(chosen_z) == 31
    C = selected + [z[i] for i in chosen_z]
    assert len(C) == 95
    rows = [{j: col[i] for j, col in enumerate(C) if i in col}
            for i in range(len(FACES[2]))]
    chosen_rows = select_mod2(rows)
    assert chosen_rows == cert['minor_triangle_row_indices']
    assert len(chosen_rows) == 95
    integer_minor = [[col.get(i, 0) for col in C] for i in chosen_rows]
    determinant = unit_pivot_determinant(integer_minor)
    assert determinant == cert['minor_determinant'] == -1

    # The affine T semidirect S_5 subgroup is transitive on all 40 carriers.
    # Each direction permutation extends uniquely linearly from the first 4 basis vectors.
    orbit = set()
    for images in itertools.permutations(D):
        def linear(x):
            y = 0
            for k in range(4):
                if (x >> k) & 1:
                    y ^= images[k]
            return y
        assert {linear(d) for d in D} == set(D)
        for translation in V:
            orbit.add(tuple(sorted(linear(x) ^ translation for x in missing[0])))
    assert orbit == set(missing)

    # By the exact unit minor and boundary ranks: 31 sphere classes are a Z-basis
    # of H_2; the other 9 give the rank-nine integral relation lattice.
    print('VERIFY_OK_FOLDED_CUBE_FORTY_MINIMAL_SPHERES')
    print('NEIGHBORHOOD_F_VECTOR', tuple(len(FACES[k]) for k in range(5)))
    print('BOUNDARY_RANKS_OVER_2_3_101', (15, 65, 64, 16))
    print('AFFINE_FOUR_VERTEX_SPHERES', len(missing), 'TRANSITIVE_ORBIT', len(orbit))
    print('BOUNDARY3_BASIS', len(chosen_d3), 'SPHERE_BASIS', len(chosen_z))
    print('INTEGRAL_MINOR_SHAPE', len(chosen_rows), len(C))
    print('INTEGER_DETERMINANT', determinant, 'UNIT_PIVOTS', len(chosen_rows))
    print('INTEGRAL_H2_RANK', len(chosen_z), 'RELATION_LATTICE_RANK', len(missing)-len(chosen_z))


if __name__ == '__main__':
    main()
