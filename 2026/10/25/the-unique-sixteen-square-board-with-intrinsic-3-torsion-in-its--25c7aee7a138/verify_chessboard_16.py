"""Reproduce the exact intrinsic 3-torsion threshold for 5-by-5 rook subboards.

Only the Python standard library is required. All operations are exact integers
or arithmetic modulo 3; no full-size matrix data is loaded from elsewhere.
"""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
from math import gcd

N = 5
PAIRS = tuple(permutations(range(N)))
MASK_TRANSFORMS = tuple(tuple(sum(1 << p[j] for j in range(N)
                                   if mask & (1 << j)) for mask in range(32))
                        for p in PAIRS)


def all_matching_faces(size):
    out = []
    for rows in combinations(range(N), size):
        for cols in combinations(range(N), size):
            for perm in permutations(cols):
                out.append(tuple(sorted(5 * i + j for i, j in zip(rows, perm))))
    return tuple(sorted(set(out)))

F1, F2, F3 = (all_matching_faces(k) for k in (2, 3, 4))


def canonical_rows(rows):
    return min(tuple(sorted(transform[x] for x in rows))
               for transform in MASK_TRANSFORMS)


def classes_through_16():
    classes = [set() for _ in range(17)]
    for rows in combinations_with_replacement(range(32), N):
        k = sum(x.bit_count() for x in rows)
        if k <= 16:
            classes[k].add(canonical_rows(rows))
    return classes


def retained(rows, faces):
    active = sum(1 << (N*i+j) for i, mask in enumerate(rows)
                 for j in range(N) if mask & (1 << j))
    return tuple(f for f in faces if all(active & (1 << x) for x in f))


def boundary_columns(rows, d):
    if d == 2:
        lower, upper = retained(rows, F1), retained(rows, F2)
    elif d == 3:
        lower, upper = retained(rows, F2), retained(rows, F3)
    else:
        raise ValueError(d)
    indexing = {face: i for i, face in enumerate(lower)}
    columns = []
    for face in upper:
        columns.append({indexing[face[:i]+face[i+1:]]: (-1)**i
                        for i in range(d+1)})
    return len(lower), lower, upper, columns


def integral_unit_reduce(nrows, columns):
    """Integral unimodular row/column cancellation at unit pivots.

    Returns (number of unit pivots, exact remaining nonzero columns).
    """
    cols = {j: dict(c) for j, c in enumerate(columns)}
    rows = {i: {} for i in range(nrows)}
    for j, col in cols.items():
        for i, value in col.items():
            rows[i][j] = value
    count = 0
    while True:
        best = None
        for j, col in cols.items():
            for i, value in col.items():
                if abs(value) == 1:
                    candidate = (len(rows[i])*len(col), i, j, value)
                    if best is None or candidate < best:
                        best = candidate
        if best is None:
            break
        _, pivot_row, pivot_col, pivot_value = best
        pivot_entries = dict(cols[pivot_col])
        for j, value in list(rows[pivot_row].items()):
            if j == pivot_col:
                continue
            factor = value*pivot_value
            for i, c in pivot_entries.items():
                result = cols[j].get(i, 0) - factor*c
                if result:
                    cols[j][i] = result
                    rows[i][j] = result
                else:
                    cols[j].pop(i, None)
                    rows[i].pop(j, None)
        for i in pivot_entries:
            rows[i].pop(pivot_col, None)
        del cols[pivot_col]
        del rows[pivot_row]
        count += 1
    return count, {j: c for j, c in cols.items() if c}


def add_mod3(column, basis, insert=True):
    """Exact sparse field-elimination; return whether column raises rank."""
    a = {int(k): int(v)%3 for k, v in column.items() if v%3}
    while a:
        pivot = min(a)
        if pivot not in basis:
            if insert:
                scale = pow(a[pivot], -1, 3)
                basis[pivot] = {i: (v*scale)%3 for i, v in a.items()}
            return True
        factor = a[pivot]
        for i, v in basis[pivot].items():
            t = (a.get(i, 0)-factor*v)%3
            if t:
                a[i] = t
            else:
                a.pop(i, None)
    return False


def rank_mod3(columns):
    basis = {}
    for column in columns:
        add_mod3(column, basis)
    return len(basis), basis


def check_cycle_inclusion(witness):
    n2, f2, f3, d3cols = boundary_columns(witness, 3)
    n1, f1, _, d2cols = boundary_columns(witness, 2)
    r2, _ = rank_mod3(d2cols)
    r3, small_span = rank_mod3(d3cols)
    assert (n1, n2, len(f3), r2, r3) == (82, 161, 108, 67, 93)
    def check_d_squared(tetrahedra):
        for f in tetrahedra:
            signs = Counter()
            for i in range(4):
                triangle = f[:i] + f[i+1:]
                for j in range(3):
                    edge = triangle[:j] + triangle[j+1:]
                    signs[edge] += (-1)**(i+j)
            assert not any(signs.values())
    check_d_squared(f3)
    groups = ((0, 1), (7, 8), (14, 19))
    cycle = Counter()
    for bits in range(8):
        tri = tuple(groups[i][(bits >> i) & 1] for i in range(3))
        assert tri in set(f2)
        cycle[tri] += (-1)**bits.bit_count()
    cycle = {f: c for f, c in cycle.items() if c}
    d2boundary = Counter()
    for f, c in cycle.items():
        for i in range(3):
            d2boundary[f[:i]+f[i+1:]] += c*(-1)**i
    assert all(v == 0 for v in d2boundary.values())
    indexed_small = {i: cycle.get(f, 0) for i, f in enumerate(f2)
                     if cycle.get(f, 0)}
    assert add_mod3(indexed_small, small_span, False)
    full = (31,)*5
    nf, all_f2, all_f3, fullcols = boundary_columns(full, 3)
    nfull1, _, _, full2cols = boundary_columns(full, 2)
    full2rank, _ = rank_mod3(full2cols)
    assert (nfull1, full2rank) == (200, 176)
    fullrank, fullspan = rank_mod3(fullcols)
    indexed_full = {i: cycle.get(f, 0) for i, f in enumerate(all_f2)
                    if cycle.get(f, 0)}
    assert (nf, len(all_f3), fullrank) == (600, 600, 423)
    check_d_squared(all_f3)
    assert add_mod3(indexed_full, fullspan, False)
    print('INCLUSION_CERTIFICATE witness_d2_mod3=67 witness_d3_mod3=93 '
          'full_d2_mod3=176 full_d3_mod3=423 '
          'both_cycle_augmentation_ranks=94,424')
    print('EXPLICIT_TORSION_CYCLE', sorted((f, c) for f, c in cycle.items()))


def check_labeled_orbit(witness):
    orbit = set()
    for rowperm in PAIRS:
        for tr in MASK_TRANSFORMS:
            orbit.add(tuple(tr[witness[i]] for i in rowperm))
    assert len(orbit) == 3600
    print('EXCEPTIONAL_LABELED_BOARDS', len(orbit))


def main():
    classes = classes_through_16()
    signatures = []
    exceptions = []
    for k, rowtypes in enumerate(classes):
        with_residual = 0
        for rowtype in sorted(rowtypes):
            n2, _, _, d3cols = boundary_columns(rowtype, 3)
            units, residual = integral_unit_reduce(n2, d3cols)
            if residual:
                with_residual += 1
                exceptions.append((k, rowtype, units, residual, n2))
        signatures.append((k, len(rowtypes), with_residual))
    assert all(exception[0] == 16 for exception in exceptions)
    assert len(exceptions) == 1
    k, rows, units, residual, n2 = exceptions[0]
    assert rows == (3, 13, 28, 30, 30)
    assert (n2, units, len(residual)) == (161, 93, 1)
    values = list(next(iter(residual.values())).values())
    assert len(values) >= 1
    assert set(map(abs, values)) == {3}
    assert gcd(*values) == 3
    print('CANONICAL_CLASS_COUNTS_AND_RESIDUAL_COUNTS', signatures)
    print('EXCEPTIONAL_BOARD', rows, 'UNIT_PIVOTS', units,
          'RESIDUAL_ONE_COLUMN', sorted(values), 'GCD', gcd(*values))
    check_cycle_inclusion(rows)
    check_labeled_orbit(rows)
    print('VERIFY_OK_UNIQUE_16_SQUARE_INTRINSIC_THREE_TORSION')

if __name__ == '__main__':
    main()
