#!/usr/bin/env python3
"""Exact four-round first-order type census for binary hypercube adjacency graphs.

Runs a coordinate-orbit dynamic programme for dimensions 1 through 16 and an
independent direct graph calculation for dimensions 1 through 5.
The infinite stabilization uses the separate mathematical cutoff proof.
"""

from itertools import product

TYPES = {}


def intern(stage, value):
    key = (stage, frozenset(value))
    if key not in TYPES:
        TYPES[key] = len(TYPES) + 1
    return TYPES[key]


def atomic(distances):
    """Encode equality (0), adjacency (1), and other nonadjacency (2)."""
    return tuple(min(v, 2) for v in distances)


def triple_type(c):
    """All extensions of the tuple (zero word, second word, third word).

    c=(c00,c01,c10,c11), where indices are the bit pairs of second/third.
    """
    d12 = c[2] + c[3]
    d13 = c[1] + c[3]
    d23 = c[1] + c[2]
    types = set()
    for x0 in range(c[0] + 1):
        for x1 in range(c[1] + 1):
            for x2 in range(c[2] + 1):
                for x3 in range(c[3] + 1):
                    s = x0 + x1 + x2 + x3
                    d14 = s
                    d24 = d12 + s - 2 * (x2 + x3)
                    d34 = d13 + s - 2 * (x1 + x3)
                    types.add(atomic((d12, d13, d23, d14, d24, d34)))
    return intern('triple-to-fourth', types)


def orbit_root(d):
    pair_types = []
    triple_orbit_types = {}
    for h in range(d + 1):
        extensions = set()
        for a in range(d - h + 1):
            for b in range(h + 1):
                counts = (d - h - a, a, h - b, b)
                triple_id = triple_type(counts)
                triple_orbit_types[(h, a, b)] = triple_id
                extensions.add(triple_id)
        pair_types.append(intern('pair-to-triple', extensions))
    root = intern('root-to-pair', pair_types)
    return root, len(set(pair_types)), len(set(triple_orbit_types.values()))


def direct_root(d):
    """Calculate the full four-move game without coordinate symmetries."""
    vertex_count = 1 << d
    vs = range(vertex_count)

    def pair_rel(u, v):
        return min((u ^ v).bit_count(), 2)

    triples = {}
    for a, b, c in product(vs, repeat=3):
        prefix = (pair_rel(a, b), pair_rel(a, c), pair_rel(b, c))
        suffixes = set()
        for z in vs:
            suffixes.add(prefix + (pair_rel(a, z), pair_rel(b, z), pair_rel(c, z)))
        triples[a, b, c] = intern('triple-to-fourth', suffixes)

    pairs = {}
    for a, b in product(vs, repeat=2):
        pairs[a, b] = intern('pair-to-triple', (triples[a, b, c] for c in vs))

    singles = {}
    for a in vs:
        singles[a] = intern('root-to-pair', (pairs[a, b] for b in vs))
    if len(set(singles.values())) != 1:
        raise AssertionError('vertex transitivity check failed')
    return singles[0]


def main():
    roots = {}
    for d in range(1, 17):
        root, pairs, triples = orbit_root(d)
        roots[d] = root
        print(f'ORBIT_CENSUS dimension={d:2d} root_type={root:3d} '
              f'pair_types={pairs:2d} triple_types={triples:2d}')

    classes = {}
    for d, root in roots.items():
        classes.setdefault(root, []).append(d)
    observed = sorted(classes.values(), key=lambda group: group[0])
    expected = [[1], [2], [3], [4], [5], list(range(6, 17))]
    if observed != expected:
        raise AssertionError((observed, expected))
    print('EXHAUSTIVE_BOUNDARY_CLASSIFICATION_OK ' + repr(observed))

    for d in range(1, 6):
        direct = direct_root(d)
        if direct != roots[d]:
            raise AssertionError(('independent direct mismatch', d, direct, roots[d]))
        print(f'INDEPENDENT_DIRECT_AGREEMENT_OK dimension={d} vertices={1<<d}')

    # The two mathematical truncation lemmas imply that every root type in
    # dimension >=16 occurs already in dimension 16. Numerical agreement of
    # dimensions 6..16 then proves the infinite tail.
    print('INFINITE_TAIL_REQUIRES_PROVED_CELL_TRUNCATION_LEMMAS cutoff=16')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
