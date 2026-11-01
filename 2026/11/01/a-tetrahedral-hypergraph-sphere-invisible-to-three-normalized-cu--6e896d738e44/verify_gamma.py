#!/usr/bin/env python3
"""Exact integral degree-two Gamma-homology certificate for a tetrahedral boundary.

Input: gamma_minor.json in the same directory. Requires Python 3 standard library only.
The input specifies 219 admissible 3-cubes and 219 rows of the 2-cube boundary basis.
A unit 219-by-219 integer minor proves that all integral 2-cycles are boundaries.
"""
import json
from itertools import combinations, product
from pathlib import Path

COLORS = range(4)


def degenerate(cube, dimension):
    return any(all(cube[v] == cube[v | (1 << i)]
                   for v in range(1 << dimension) if not (v >> i) & 1)
               for i in range(dimension))


def gamma_admissible(cube, dimension):
    # The four maximal hyperedges of the target are all three-element subsets.
    if dimension == 0:
        return True
    if dimension == 1:
        return True
    for v in range(1 << dimension):
        star = (v,) + tuple(v ^ (1 << i) for i in range(dimension))
        if len({cube[w] for w in star}) > 3:
            return False
    return True


def face(cube, dimension, i, bit):
    out = []
    for v in range(1 << (dimension - 1)):
        source = sum(((v >> j) & 1) << (j if j < i else j + 1)
                     for j in range(dimension - 1)) + (bit << i)
        out.append(cube[source])
    return tuple(out)


def boundary(cube, dimension, index):
    out = {}
    for i in range(dimension):
        for bit in (0, 1):
            sub = face(cube, dimension, i, bit)
            if sub in index:
                row = index[sub]
                out[row] = out.get(row, 0) + (-1) ** (i + bit + 1)
                if not out[row]:
                    del out[row]
    return out


def rank_mod_two(columns):
    basis = {}
    for v in columns:
        mask = 0
        for row, coeff in v.items():
            if coeff & 1:
                mask ^= 1 << row
        while mask:
            lead = mask.bit_length() - 1
            if lead in basis:
                mask ^= basis[lead]
            else:
                basis[lead] = mask
                break
    return len(basis)


def bareiss_determinant(a):
    # Fraction-free integer elimination, preserving the exact determinant.
    size = len(a)
    previous, sign = 1, 1
    for k in range(size - 1):
        if not a[k][k]:
            substitute = next((i for i in range(k + 1, size) if a[i][k]), None)
            if substitute is None:
                return 0
            a[k], a[substitute] = a[substitute], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            entry = a[i][k]
            if entry == 0 and pivot == previous:
                continue
            for j in range(k + 1, size):
                numerator = a[i][j] * pivot - entry * a[k][j]
                assert numerator % previous == 0, "Bareiss division not exact"
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def main():
    data = json.loads((Path(__file__).parent / 'gamma_minor.json').read_text())
    selected = [tuple(c) for c in data['selected_cubes']]
    rows = data['selected_rows']
    assert len(selected) == len(set(selected)) == 219
    assert len(rows) == len(set(rows)) == 219
    assert all(0 <= r < 228 for r in rows)
    assert all(len(c) == 8 and set(c) <= set(COLORS) and not degenerate(c, 3)
               and gamma_admissible(c, 3) for c in selected)

    c1 = [c for c in product(COLORS, repeat=2) if not degenerate(c, 1)]
    c2 = [c for c in product(COLORS, repeat=4) if not degenerate(c, 2)
          and gamma_admissible(c, 2)]
    assert (len(c1), len(c2)) == (12, 228)
    i1 = {c: j for j, c in enumerate(c1)}
    i2 = {c: j for j, c in enumerate(c2)}
    d2 = [boundary(c, 2, i1) for c in c2]
    assert rank_mod_two(d2) == 9
    # Each d2 boundary lies in ker d1, which has rational rank 12-(4-1)=9.
    # Thus d2 has exact rank 9 over Q and ker(d2: Z^228 -> Z^12) has rank 219.
    admissible_c3 = sum(not degenerate(c, 3) and gamma_admissible(c, 3)
                        for c in product(COLORS, repeat=8))
    assert admissible_c3 == 32868

    row_positions = {r: i for i, r in enumerate(rows)}
    minor = [[0] * 219 for _ in range(219)]
    for j, cube in enumerate(selected):
        col = boundary(cube, 3, i2)
        for r, coeff in col.items():
            if r in row_positions:
                minor[row_positions[r]][j] = coeff
        # Verify the selected 3-cube is a genuine chain in the Gamma complex.
        composed = {}
        for r, coeff in col.items():
            for edge, ec in d2[r].items():
                composed[edge] = composed.get(edge, 0) + coeff * ec
        assert all(x == 0 for x in composed.values())
    determinant = bareiss_determinant(minor)
    assert abs(determinant) == 1, determinant
    print('VERIFY_OK: C1=12; C2=228; admissible C3=32868; rank(d2)=9;')
    print('219 admissible 3-cubes have a 219x219 unit integral minor: det=', determinant)
    print('Consequently H_2^Gamma(boundary tetrahedron; Z)=0.')
    print('The tetrahedral four-facet simplicial boundary has embedded H_2=Z.')


if __name__ == '__main__':
    main()
