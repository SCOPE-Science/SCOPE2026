#!/usr/bin/env python3
"""Exact integral cellular homology of Hom(C3->, Paley(11)).

Only the Python standard library is used. All reduction operations are over Z.
The script reconstructs the complete polyhedral cell complex, its integral
boundary maps, and an explicit sequence of unimodular Smith reductions.
"""

from collections import Counter, defaultdict
from math import gcd

N = 11
ALL = (1 << N) - 1
QR = {pow(a, 2, N) for a in range(1, N)}
assert QR == {1, 3, 4, 5, 9}


def bits(mask):
    return [i for i in range(N) if mask & (1 << i)]


OUT = [sum(1 << j for j in range(N) if (j - i) % N in QR)
       for i in range(N)]
IN = [sum(1 << j for j in range(N) if (i - j) % N in QR)
      for i in range(N)]


def all_cells():
    """Enumerate all nonempty triples A,B,C with A->B->C->A."""
    cells = []
    for a in range(1, 1 << N):
        allowed_b = ALL
        for i in bits(a):
            allowed_b &= OUT[i]
        b = allowed_b
        while b:
            allowed_c = ALL
            for j in bits(b):
                allowed_c &= OUT[j]
            for i in bits(a):
                allowed_c &= IN[i]
            c = allowed_c
            while c:
                cells.append((a, b, c))
                c = (c - 1) & allowed_c
            b = (b - 1) & allowed_b
    # Independent direct verification of every enumerated cell.
    assert len(cells) == len(set(cells))
    for a, b, c in cells:
        for u in bits(a):
            for v in bits(b):
                assert (v - u) % N in QR
        for u in bits(b):
            for v in bits(c):
                assert (v - u) % N in QR
        for u in bits(c):
            for v in bits(a):
                assert (v - u) % N in QR
    return cells


def independently_enumerated_cells():
    """Alternative enumeration by growing triples of singleton images."""
    initial = set()
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if ((b-a) % N in QR and (c-b) % N in QR
                        and (a-c) % N in QR):
                    initial.add((1 << a, 1 << b, 1 << c))
    seen = set(initial)
    queue = list(initial)
    while queue:
        t = queue.pop()
        for block in range(3):
            for v in range(N):
                if any(mask & (1 << v) for mask in t):
                    continue
                u = list(t)
                u[block] |= 1 << v
                a, b, c = u
                if (all((y-x) % N in QR for x in bits(a) for y in bits(b))
                        and all((y-x) % N in QR for x in bits(b) for y in bits(c))
                        and all((y-x) % N in QR for x in bits(c) for y in bits(a))):
                    key = tuple(u)
                    if key not in seen:
                        seen.add(key)
                        queue.append(key)
    return seen


def build_boundary(k, grouped, where):
    """Integral product-of-oriented-simplices differential, in columns."""
    result = []
    for triple in grouped[k]:
        column = {}
        offset = 0
        for component, mask in enumerate(triple):
            vertices = bits(mask)
            if len(vertices) > 1:
                for pos, v in enumerate(vertices):
                    face = list(triple)
                    face[component] ^= 1 << v
                    row = where[k - 1][tuple(face)]
                    coeff = -1 if (offset + pos) & 1 else 1
                    assert row not in column
                    column[row] = coeff
            offset += len(vertices) - 1
        result.append(column)
    return result


def matrix_product_zero(d1, d2):
    for col in d2:
        val = defaultdict(int)
        for edge, coefficient in col.items():
            for vertex, number in d1[edge].items():
                val[vertex] += coefficient * number
        assert not any(val.values()), "cellular differential does not square to zero"


def connected_vertices(d1, n_vertices):
    parent = list(range(n_vertices))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for c in d1:
        assert len(c) == 2 and sorted(c.values()) == [-1, 1]
        u, v = c
        parent[find(u)] = find(v)
    return len({find(i) for i in range(n_vertices)})


def exact_smith_unit_elimination(columns):
    """Run integer-unimodular pivots of coefficient +1 or -1.

    If a pivot at row i, column j is +/-1, subtract integer multiples
    of column j from every other column to clear row i. Subsequent
    integral row operations clear the other entries of column j.
    Hence deleting row i and column j preserves all remaining Smith
    invariants and contributes one invariant factor equal to 1.
    """
    cols = {j: c.copy() for j, c in enumerate(columns)}
    rows = defaultdict(dict)
    for j, c in cols.items():
        for i, value in c.items():
            assert value
            rows[i][j] = value
    steps = 0
    while cols:
        optimum = None
        for i, row in rows.items():
            for j, value in row.items():
                if abs(value) == 1:
                    score = (len(row) - 1) * (len(cols[j]) - 1)
                    candidate = (score, i, j, value)
                    if optimum is None or candidate < optimum:
                        optimum = candidate
                    if score == 0:
                        break
            if optimum and optimum[0] == 0:
                break
        if optimum is None:
            break
        _, i, j, pivot = optimum
        pivot_column = cols[j]
        for other_col, value in rows[i].copy().items():
            if other_col == j:
                continue
            factor = value * pivot  # reciprocal of +/-1 is itself
            d = cols[other_col]
            for h, a in pivot_column.items():
                new = d.get(h, 0) - factor * a
                if new:
                    d[h] = new
                    rows[h][other_col] = new
                else:
                    d.pop(h, None)
                    rows[h].pop(other_col, None)
        for h in pivot_column:
            rows[h].pop(j, None)
        del cols[j]
        assert not rows[i]
        del rows[i]
        steps += 1
    # Double-check sparse row/column consistency after exact eliminations.
    for j, col in cols.items():
        for i, a in col.items():
            assert rows[i][j] == a
    for i, row in rows.items():
        for j, a in row.items():
            assert cols[j][i] == a
    remaining = [{i: a for i, a in sorted(c.items())} for c in cols.values()]
    return steps, remaining


def rank_mod_p(columns, prime):
    pivots = {}
    for col in columns:
        v = {i: a % prime for i, a in col.items() if a % prime}
        while v:
            row = min(v)
            if row not in pivots:
                inv = pow(v[row], -1, prime)
                pivots[row] = {i: (x * inv) % prime for i, x in v.items()}
                break
            alpha = v[row]
            for i, x in pivots[row].items():
                new = (v.get(i, 0) - alpha * x) % prime
                if new:
                    v[i] = new
                else:
                    v.pop(i, None)
    return len(pivots)


def main():
    triples = all_cells()
    assert set(triples) == independently_enumerated_cells()
    cells = {k: sorted(t for t in triples
                       if sum(x.bit_count() for x in t) - 3 == k)
             for k in range(3)}
    assert set(triples) == set().union(*map(set, cells.values()))
    assert tuple(len(cells[k]) for k in range(3)) == (165, 495, 330)
    assert not any(sum(x.bit_count() for x in t) > 5 for t in triples)
    index = {k: {cell: i for i, cell in enumerate(cells[k])}
             for k in range(3)}
    d1 = build_boundary(1, cells, index)
    d2 = build_boundary(2, cells, index)
    assert Counter(tuple(sorted(x.bit_count() for x in t)) for t in cells[2]) == {
        (1, 1, 3): 165, (1, 2, 2): 165}
    matrix_product_zero(d1, d2)
    components = connected_vertices(d1, 165)
    assert components == 1
    units, remainder = exact_smith_unit_elimination(d2)
    assert units == 329
    assert len(remainder) == 1
    values = list(remainder[0].values())
    assert len(values) == 33
    assert Counter(values) == {-33: 22, 33: 11} or Counter(values) == {33: 22, -33: 11} or set(map(abs, values)) == {33}
    invariant = 0
    for value in values:
        invariant = gcd(invariant, value)
    assert invariant == 33
    for p, expected_rank in [(2, 330), (3, 329), (5, 330),
                             (11, 329), (13, 330)]:
        assert rank_mod_p(d2, p) == expected_rank
    # All 330 columns are linearly independent over Q, because 329
    # unimodular pivots remain with a nonzero final column.
    rank2 = units + 1
    rank1 = len(cells[0]) - components
    free_H1 = len(cells[1]) - rank1 - rank2
    assert (rank1, rank2, free_H1) == (164, 330, 1)
    print('Paley P11 arcs: 55; quadratic residues:', *sorted(QR))
    print('Hom directed triangle cells: C0=165, C1=495, C2=330, Ck>2=0')
    print('C2 cell shapes: 165 triangular, 165 square')
    print('Check d1*d2=0: PASS; connected components:', components)
    print('Exact unimodular Smith reduction: 329 unit pivots; residual',
          len(values), 'nonzero entries with gcd', invariant)
    print('Smith invariants for d2: (1 repeated 329 times, 33)')
    print('Integral H0 = Z; H1 = Z + Z/33; Hk = 0 for k>=2')
    print('All required exact checks: PASS')


if __name__ == '__main__':
    main()
