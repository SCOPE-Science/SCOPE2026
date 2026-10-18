#!/usr/bin/env python3
"""Exact finite certificates supporting the k=3 bipartite nonmatching homology theorem.

Standard library only. The universal-rank input is the published theorem of
Linusson--Shareshian--Welker and is proved mathematically, not by extrapolating
these finite checks.
"""
from collections import defaultdict
from itertools import combinations, permutations, product

EDGES = [(i, j) for i in range(3) for j in range(3)]
MATCHINGS = [sum(1 << (3*i+p[i]) for i in range(3))
             for p in permutations(range(3))]
FACES = [m for m in range(1, 1 << 9)
         if not any((m & p) == p for p in MATCHINGS)]
FACESET = set(FACES)
PAIRS = [(1, 5), (2, 7), (3, 8), (4, 6)]
COCHAIN = {29: 1, 30: 1, 43: -1, 46: 1, 51: -1, 53: -1}


def inversion_sign(a):
    return (-1)**sum(a[i] > a[j] for i in range(len(a))
                      for j in range(i+1, len(a)))


def cycle():
    chain = {}
    for bits in product((0, 1), repeat=4):
        vertices = [PAIRS[i][bits[i]] for i in range(4)]
        face = sum(1 << v for v in vertices)
        sign = (-1)**sum(bits)*inversion_sign(vertices)
        assert face not in chain and face in FACESET
        chain[face] = sign
    return chain


def boundary(chain, n=9):
    out = defaultdict(int)
    for face, coeff in chain.items():
        vertices = [i for i in range(n) if (face >> i) & 1]
        for t, i in enumerate(vertices):
            out[face ^ (1 << i)] += coeff*((-1)**t)
    return {x: y for x, y in out.items() if y != 0}


def transform_cycle(chain, prow, pcol):
    out = defaultdict(int)
    for face, coeff in chain.items():
        indices = [i for i in range(9) if (face >> i) & 1]
        images = [3*prow[i//3]+pcol[i % 3] for i in indices]
        if len(set(images)) != 4:
            continue
        out[sum(1 << k for k in images)] += coeff*inversion_sign(images)
    return {x: y for x, y in out.items() if y}


def evaluate(chain):
    return sum(COCHAIN.get(face, 0)*coeff
               for face, coeff in chain.items())


def verify_local():
    assert len(FACES) == 264
    assert [sum(m.bit_count() == d+1 for m in FACES)
            for d in range(6)] == [9, 36, 78, 90, 45, 6]
    z = cycle()
    assert len(z) == 16 and boundary(z) == {}
    assert evaluate(z) == 1
    four_faces = [f for f in FACES if f.bit_count() == 5]
    assert len(four_faces) == 45
    for f in four_faces:
        vertices = [i for i in range(9) if (f >> i) & 1]
        assert sum((-1)**j * COCHAIN.get(f ^ (1 << v), 0)
                   for j, v in enumerate(vertices)) == 0
    # The ordinary simplicial Lefschetz number of either transposition is 2.
    for typ in ('row', 'column'):
        perm = [EDGES.index(((1, 0, 2)[i], j) if typ == 'row'
                            else (i, (1, 0, 2)[j])) for i, j in EDGES]
        chain_traces = [0]*6
        for f in FACES:
            vs = [i for i in range(9) if (f >> i) & 1]
            images = [perm[i] for i in vs]
            if sorted(images) == vs:
                chain_traces[len(vs)-1] += inversion_sign(images)
        assert chain_traces == [3, 0, -8, -6, 3, 2]
        assert sum((-1)**d * chain_traces[d] for d in range(6)) == 2
    # All 36 natural row/column permutations have the predicted integral degree.
    for prow in permutations(range(3)):
        for pcol in permutations(range(3)):
            image = transform_cycle(z, prow, pcol)
            assert boundary(image) == {}
            assert evaluate(image) == inversion_sign(prow)*inversion_sign(pcol)
    print('BASE_3x3_OK F_VECTOR 9_36_78_90_45_6 OCTAHEDRAL_FACETS 16')
    print('INTEGRAL_COCYCLE_SUPPORT 6 PAIRING 1 DELTA_ZERO_45_CELLS')
    print('LEFSCHETZ_TRANSPOSE_ROW_COLUMN 2 H3_SIGN_CHARACTER')
    print('ALL_S3xS3_DEGREES_OK 36')


def projected_value(rows, cols, a, b, c, d):
    prow = {x: (1 if x == a else 2 if x == b else 0)
            for x in rows}
    pcol = {x: (1 if x == c else 2 if x == d else 0)
            for x in cols}
    projected = defaultdict(int)
    for face, coeff in cycle().items():
        # Inclusion into K_{r,s}, then vertex-class amalgamation to K_{3,3}.
        vs = [i for i in range(9) if (face >> i) & 1]
        images = [3*prow[rows[i//3]] + pcol[cols[i % 3]]
                  for i in vs]
        if len(set(images)) != 4:
            continue
        projected[sum(1 << v for v in images)] += (
            coeff*inversion_sign(images))
    return evaluate(projected)


def expected_coefficient(triple, a, b):
    images = [1 if x == a else 2 if x == b else 0 for x in triple]
    return inversion_sign(images) if len(set(images)) == 3 else 0


def verify_projections():
    cases = 0
    for r in (3, 4, 5):
        for s in (3, 4, 5):
            for rows in combinations(range(r), 3):
                for cols in combinations(range(s), 3):
                    for a, b in combinations(range(1, r), 2):
                        for c, d in combinations(range(1, s), 2):
                            got = projected_value(rows, cols, a, b, c, d)
                            want = (expected_coefficient(rows, a, b)*
                                    expected_coefficient(cols, c, d))
                            assert got == want, (r, s, rows, cols,
                                                 a, b, c, d, got, want)
                            cases += 1
    print('ROOT_PROJECTION_DETERMINANTS_OK CASES', cases)


def verify_s4_rational_character():
    n = 4
    match3 = []
    for left in combinations(range(n), 3):
        for right in combinations(range(n), 3):
            for p in permutations(right):
                match3.append(sum(1 << (n*left[i]+p[i]) for i in range(3)))
    faces = [m for m in range(1, 1 << 16)
             if not any(m & f == f for f in match3)]
    assert len(faces) == 3016
    def ctype(p):
        lengths, seen = [], set()
        for i in range(n):
            if i not in seen:
                j, k = i, 0
                while j not in seen:
                    seen.add(j); j = p[j]; k += 1
                lengths.append(k)
        return tuple(sorted(lengths))
    perms = {ctype(p): p for p in permutations(range(n))}
    def hook(p):
        u = sum(p[i] == i for i in range(n))-1
        v = sum(p[p[i]] == i for i in range(n))-1
        return (u*u-v)//2
    for p in perms.values():
        for q in perms.values():
            perm = [4*p[i]+q[j] for i in range(n) for j in range(n)]
            L = 0
            for f in faces:
                vs = [i for i in range(16) if f >> i & 1]
                images = [perm[i] for i in vs]
                if sorted(images) == vs:
                    L += (-1)**(len(vs)-1)*inversion_sign(images)
            assert L == 1-hook(p)*hook(q)
    print('S4xS4_LEFSCHETZ_CHARACTER_OK 25_CONJUGACY_PAIRS')


if __name__ == '__main__':
    verify_local()
    verify_projections()
    verify_s4_rational_character()
    print('VERIFY_OK_INTEGRAL_BIPARTITE_NONMATCHING_K3_HOOK_TENSOR')
