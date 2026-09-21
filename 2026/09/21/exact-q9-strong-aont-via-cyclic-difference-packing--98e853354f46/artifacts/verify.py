#!/usr/bin/env python3
"""Exact verification for M_R([1,2],9)=6 and CDPA(k,7;8) extremality.

The finite search is symmetry-complete.  A CDPA(k,7;8) can be normalized so
its first row and first column are zero.  Every other row then has the form
(0,r_1,...,r_6), where the last six entries are distinct nonzero residues of
Z_8.  After choosing one nonzero row, a permutation of the last six columns
puts it in one of seven canonical forms, indexed by its missing nonzero
residue.  A fifth row would force a triangle among the rows compatible with
one of these canonical forms.

The script also verifies the published 6 by 6 strong-AONT matrix over
F_9 = F_3[x]/(x^2+1): it is nonsingular, has no zero entries, and every
2 by 2 minor is nonzero.
"""

from itertools import combinations, permutations

MOD = 8


def cdpa_compatible(a, b):
    """Return whether the row difference uses seven distinct residues mod 8."""
    return len({(x - y) % MOD for x, y in zip(a, b)}) == 7


def verify_cdpa_extremum():
    candidates = []
    for missing in range(1, 8):
        values = [x for x in range(1, 8) if x != missing]
        candidates.extend((0,) + p for p in permutations(values))
    assert len(candidates) == 7 * 720 == 5040

    witness = [
        (0, 0, 0, 0, 0, 0, 0),
        (0, 2, 3, 4, 5, 6, 7),
        (0, 3, 5, 7, 2, 4, 6),
        (0, 5, 2, 6, 3, 7, 4),
    ]
    assert all(cdpa_compatible(a, b) for a, b in combinations(witness, 2))

    rows = []
    for missing in range(1, 8):
        canonical = (0,) + tuple(x for x in range(1, 8) if x != missing)
        neighbors = [r for r in candidates if cdpa_compatible(canonical, r)]

        index = {r: i for i, r in enumerate(neighbors)}
        adjacency = [set() for _ in neighbors]
        edge_count = 0
        for i, a in enumerate(neighbors):
            for j in range(i + 1, len(neighbors)):
                b = neighbors[j]
                if cdpa_compatible(a, b):
                    adjacency[i].add(j)
                    adjacency[j].add(i)
                    edge_count += 1

        triangle_count = 0
        for i in range(len(neighbors)):
            for j in adjacency[i]:
                if j <= i:
                    continue
                triangle_count += len({k for k in adjacency[i] & adjacency[j] if k > j})

        assert len(index) == len(neighbors)
        assert len(neighbors) == 64
        assert edge_count == 24
        assert triangle_count == 0
        rows.append((missing, len(neighbors), edge_count, triangle_count))

    return witness, rows


# Elements of F_9 are pairs (a,b) representing a+b*x, with x^2=-1=2 mod 3.
ZERO = (0, 0)
ONE = (1, 0)


def fadd(u, v):
    return ((u[0] + v[0]) % 3, (u[1] + v[1]) % 3)


def fneg(u):
    return ((-u[0]) % 3, (-u[1]) % 3)


def fsub(u, v):
    return fadd(u, fneg(v))


def fmul(u, v):
    a, b = u
    c, d = v
    return ((a * c + 2 * b * d) % 3, (a * d + b * c) % 3)


def finv(u):
    assert u != ZERO
    for a in range(3):
        for b in range(3):
            v = (a, b)
            if fmul(u, v) == ONE:
                return v
    raise AssertionError("nonzero field element had no inverse")


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    out = ONE
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            out = fneg(out)
        p = a[col][col]
        out = fmul(out, p)
        p_inv = finv(p)
        for j in range(col, n):
            a[col][j] = fmul(a[col][j], p_inv)
        for r in range(col + 1, n):
            factor = a[r][col]
            if factor != ZERO:
                for j in range(col, n):
                    a[r][j] = fsub(a[r][j], fmul(factor, a[col][j]))
    return out


def verify_aont_matrix():
    element = {
        "1": (1, 0), "2": (2, 0), "x": (0, 1),
        "x+1": (1, 1), "x+2": (2, 1), "2x": (0, 2),
        "2x+1": (1, 2), "2x+2": (2, 2),
    }
    source = [
        "1 1 1 1 1 1",
        "1 2 x x+1 x+2 2x",
        "1 x 2 2x 2x+1 x+1",
        "1 x+1 2x+2 x+2 2x 2x+1",
        "1 x+2 2x x 2x+2 2",
        "1 2x x+2 2 x+1 x",
    ]
    matrix = [[element[z] for z in row.split()] for row in source]
    nonzero_entries = all(v != ZERO for row in matrix for v in row)
    det = determinant(matrix)
    minors_ok = True
    for r1, r2 in combinations(range(6), 2):
        for c1, c2 in combinations(range(6), 2):
            minor = fsub(
                fmul(matrix[r1][c1], matrix[r2][c2]),
                fmul(matrix[r1][c2], matrix[r2][c1]),
            )
            if minor == ZERO:
                minors_ok = False
    assert nonzero_entries
    assert det != ZERO
    assert minors_ok
    return det, nonzero_entries, minors_ok


def main():
    witness, cases = verify_cdpa_extremum()
    det, entries_ok, minors_ok = verify_aont_matrix()

    print("normalized_cdpa_candidates=5040")
    print("cdpa_4_7_8_witness_valid=true")
    for missing, neighbors, edges, triangles in cases:
        print(
            f"canonical_missing={missing} neighbors={neighbors} "
            f"edges={edges} triangles={triangles}"
        )
    print("cdpa_5_7_8_exists=false")
    print("max_rows_cdpa_k_7_8=4")
    print(f"gf9_matrix_determinant={det[0]}+{det[1]}x")
    print(f"gf9_matrix_nonzero_entries={str(entries_ok).lower()}")
    print(f"gf9_matrix_all_2x2_minors_nonzero={str(minors_ok).lower()}")
    print("linear_strong_aont_q9_exact_size=6")


if __name__ == "__main__":
    main()
