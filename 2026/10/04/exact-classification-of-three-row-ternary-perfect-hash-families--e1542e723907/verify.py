#!/usr/bin/env python3
import json
import sys
from itertools import combinations, permutations, product


def is_phf(columns):
    for triple in combinations(columns, 3):
        if not any(len({x[row] for x in triple}) == 3 for row in range(3)):
            return False
    return True


def transform(columns, row_perm, symbol_perms):
    return tuple(sorted(tuple(symbol_perms[r][x[row_perm[r]]] for r in range(3)) for x in columns))


def canonical(columns, perms):
    best = None
    for row_perm in perms:
        for p0 in perms:
            for p1 in perms:
                for p2 in perms:
                    candidate = transform(columns, row_perm, (p0, p1, p2))
                    if best is None or candidate < best:
                        best = candidate
    return best


def main(path):
    with open(path, 'r', encoding='utf-8') as fh:
        cert = json.load(fh)
    universe = list(product(range(3), repeat=3))
    maxima = []
    for idxs in combinations(range(len(universe)), 6):
        columns = tuple(universe[i] for i in idxs)
        if is_phf(columns):
            maxima.append(columns)
    for idxs in combinations(range(len(universe)), 7):
        columns = tuple(universe[i] for i in idxs)
        if is_phf(columns):
            raise AssertionError('found a seven-column family')
    perms = list(permutations(range(3)))
    canonical_forms = {canonical(columns, perms) for columns in maxima}
    if len(canonical_forms) != 1:
        raise AssertionError('maximum families split into multiple equivalence classes')
    representative = next(iter(canonical_forms))
    orbit = set()
    for row_perm in perms:
        for p0 in perms:
            for p1 in perms:
                for p2 in perms:
                    orbit.add(transform(representative, row_perm, (p0, p1, p2)))
    group_size = len(perms) ** 4
    if group_size % len(orbit):
        raise AssertionError('orbit size does not divide group size')
    stabilizer = group_size // len(orbit)
    expected_rep = tuple(tuple(x) for x in cert['canonical_representative_columns'])
    assert len(universe) == cert['universe_size'] == 27
    assert len(maxima) == cert['maximum_labeled_families'] == 36
    assert representative == expected_rep
    assert len(orbit) == cert['orbit_size'] == 36
    assert stabilizer == cert['stabilizer_size'] == 36
    assert cert['maximum_columns'] == 6
    assert cert['equivalence_group_order'] == group_size == 1296
    print('VERIFY_OK p3(3,3)=6 maxima=36 orbits=1 stabilizer=36')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: verify.py certificate.json')
    main(sys.argv[1])
