"""Exact, standard-library verifier for the minimum second-homology supports
in the order-thirteen Paley open-neighborhood complex.

Usage: python3 verify.py
No external data or dependencies are required.
"""
from itertools import combinations

N = 13
RESIDUES = {pow(x, 2, N) for x in range(1, N)}
assert RESIDUES == {1, 3, 4, 9, 10, 12}


def bits(x):
    return [i for i in range(N) if x & (1 << i)]


def gf2_add(basis, v):
    while v:
        k = v.bit_length() - 1
        if k in basis:
            v ^= basis[k]
        else:
            basis[k] = v
            return True
    return False


def rank_mod2_columns(columns):
    b = {}
    for v in columns:
        gf2_add(b, v)
    return len(b)


def signed_boundary(s, index):
    out = {}
    for k, v in enumerate(bits(s)):
        t = s ^ (1 << v)
        if t in index:
            j = index[t]
            out[j] = (-1) ** k
        else:
            raise AssertionError('missing boundary face')
    return out


def bareiss_det(rows):
    """Exact signed determinant by fraction-free elimination."""
    a = [list(row) for row in rows]
    n = len(a)
    assert all(len(row) == n for row in a)
    if n == 1:
        return a[0][0]
    denominator, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            replacement = next((i for i in range(k + 1, n)
                                if a[i][k] != 0), None)
            if replacement is None:
                return 0
            a[k], a[replacement] = a[replacement], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            x = a[i][k]
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - x * a[k][j]
                q, rem = divmod(numerator, denominator)
                assert rem == 0
                a[i][j] = q
            a[i][k] = 0
        denominator = pivot
    return sign * a[n - 1][n - 1]


def select_independent_mod2(vectors, size):
    basis, chosen = {}, []
    for x in vectors:
        v = sum(1 << k for k, entry in enumerate(x) if entry % 2)
        if gf2_add(basis, v):
            chosen.append(x)
        if len(chosen) == size:
            break
    return chosen


def integer_minor(columns):
    size = len(columns)
    return bareiss_det([[columns[j][i] for j in range(size)]
                        for i in range(size)])


def main():
    neighborhoods = [sum(1 << j for j in range(N)
                         if (j - i) % N in RESIDUES)
                     for i in range(N)]
    all_faces = {0}
    for facet in neighborhoods:
        s = facet
        while s:
            all_faces.add(s)
            s = (s - 1) & facet
    by_d = {d: sorted(s for s in all_faces if s.bit_count() == d + 1)
            for d in range(6)}
    assert [len(by_d[d]) for d in range(6)] == [13, 78, 221, 195, 78, 13]
    assert len(all_faces) == 599

    def boundary_columns(d):
        target = {s: i for i, s in enumerate(by_d[d - 1])}
        for s in by_d[d]:
            v = 0
            for x in bits(s):
                v ^= 1 << target[s ^ (1 << x)]
            yield v

    rank_d2 = rank_mod2_columns(boundary_columns(2))
    rank_d3 = rank_mod2_columns(boundary_columns(3))
    rank_d4 = rank_mod2_columns(boundary_columns(4))
    assert (rank_d2, rank_d3, rank_d4) == (66, 130, 65)
    # The complete one-skeleton has 78 edges and 13 vertices.
    # Over Q, rank(d2) <= 78-12=66, rank(d3) <= 195-65=130.
    # The mod-2 ranks give the reverse characteristic-zero inequalities.
    assert 221 - rank_d2 - rank_d3 == 25

    missing = []
    for w in combinations(range(N), 4):
        mask = sum(1 << x for x in w)
        if (mask not in all_faces and
            all(mask ^ (1 << x) in all_faces for x in w)):
            missing.append(w)
    assert len(missing) == 104
    triangle_idx = {s: i for i, s in enumerate(by_d[2])}
    boundary_basis = {}
    for col in boundary_columns(3):
        gf2_add(boundary_basis, col)
    assert len(boundary_basis) == 130
    for w in missing:
        mask = sum(1 << x for x in w)
        signed = signed_boundary(mask, triangle_idx)
        z = sum(1 << j for j in signed)
        assert sum(abs(c) for c in signed.values()) == 4
        test_basis = boundary_basis.copy()
        assert gf2_add(test_basis, z), ('ambient class vanishes', w)

    group = [(a, b) for a in sorted(RESIDUES) for b in range(N)]
    assert len(group) == 78
    def transform(w, a, b):
        return tuple(sorted((a * x + b) % N for x in w))
    remaining, orbits = set(missing), []
    while remaining:
        representative = min(remaining)
        orbit = sorted({transform(representative, a, b)
                        for a, b in group})
        assert set(orbit).issubset(remaining)
        remaining.difference_update(orbit)
        orbits.append((representative, orbit))
    assert [(rep, len(orb)) for rep, orb in orbits] == [
        ((0, 1, 3, 9), 26),
        ((0, 1, 3, 11), 39),
        ((0, 1, 6, 8), 39)]

    # The complete one-skeleton has a star spanning tree rooted at 0.
    # Projection from its integral cycle lattice to the 66 chord
    # coordinates (edges not incident to 0) is a Z-isomorphism.
    chord_edges = [e for e in by_d[1] if not (e & 1)]
    assert len(chord_edges) == 66
    chord_idx = {e: i for i, e in enumerate(chord_edges)}
    b2columns = []
    for triangle in by_d[2]:
        c = [0] * 66
        for k, v in enumerate(bits(triangle)):
            edge = triangle ^ (1 << v)
            if edge in chord_idx:
                c[chord_idx[edge]] = (-1) ** k
        b2columns.append(c)
    pivot_columns = []
    mod2_basis = {}
    for j, col in enumerate(b2columns):
        v = sum(1 << i for i, c in enumerate(col) if c % 2)
        if gf2_add(mod2_basis, v):
            pivot_columns.append(j)
        if len(pivot_columns) == 66:
            break
    assert len(pivot_columns) == 66
    det_first = integer_minor([b2columns[j] for j in pivot_columns])
    assert abs(det_first) == 1, det_first

    # Since these 66 triangle columns project unimodularly to
    # the 1-cycle lattice, the 155 remaining triangle coordinates
    # give an integral coordinate system for ker(d2).
    pivot_set = set(pivot_columns)
    free_columns = [j for j in range(221) if j not in pivot_set]
    assert len(free_columns) == 155
    def complement_coordinates(mask):
        d = signed_boundary(mask, triangle_idx)
        return [d.get(j, 0) for j in free_columns]

    d3_in_kernel = [complement_coordinates(t) for t in by_d[3]]
    assert len(d3_in_kernel) == 195
    for representative, orbit in orbits:
        test = boundary_basis.copy()
        for w in orbit:
            mask = sum(1 << i for i in w)
            z = sum(1 << j for j in signed_boundary(mask, triangle_idx))
            gf2_add(test, z)
        predicted = 154 if len(orbit) == 26 else 155
        assert len(test) == predicted
        print('ORBIT_MOD2_H2_RANK', representative, len(test) - 130)

    # A determinant +/-1 for 130 boundary columns together with
    # 25 orbit classes gives a Z-basis of ker(d2).
    # The rational rank of d3 is exactly 130 (proved above),
    # and integrality then forces every other d3 column to be an
    # integer combination of the chosen 130 boundary columns.
    # Hence H_2 is Z^25 and each 39-orbit spans integrally.
    for representative, orbit in orbits:
        if len(orbit) != 39:
            continue
        sphere_columns = [complement_coordinates(sum(1 << i for i in w))
                          for w in orbit]
        chosen = select_independent_mod2(d3_in_kernel + sphere_columns, 155)
        assert len(chosen) == 155
        # Confirm the 130 first independent columns come from d3.
        assert len(select_independent_mod2(d3_in_kernel, 155)) == 130
        det = integer_minor(chosen)
        assert abs(det) == 1, (representative, det)
        print('ORBIT_INTEGRAL_BASIS', representative, len(orbit), det)
    print('VERIFY_OK',
          'F_VECTOR_13_78_221_195_78_13',
          '104_ESSENTIAL_SPHERES',
          'ORBIT_SIZES_26_39_39',
          'TWO_39_ORBITS_GENERATE_Z25',
          'FIRST_MINOR', det_first)

if __name__ == '__main__':
    main()
