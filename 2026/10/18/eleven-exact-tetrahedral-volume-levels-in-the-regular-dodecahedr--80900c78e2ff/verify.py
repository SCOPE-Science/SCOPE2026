"""Exact tetrahedral-volume spectrum of the regular dodecahedron.

Uses integer pairs (a,b) for a+b*phi, phi^2=phi+1.
No floating-point arithmetic or external dependencies enter the certificate.
"""
from collections import Counter
import csv
from pathlib import Path
from itertools import combinations, product
from math import comb

Z = (0, 0)
O = (1, 0)
PHI = (0, 1)
INVPHI = (-1, 1)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, b):
    # (a0+a1 phi)(b0+b1 phi), using phi^2=phi+1.
    return (a[0] * b[0] + a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def neg(a):
    return -a[0], -a[1]


def scal(s, a):
    return s * a[0], s * a[1]


def dot(u, v):
    z = Z
    for i in range(3):
        z = add(z, mul(u[i], v[i]))
    return z


def det3(a, b, c):
    return add(sub(mul(a[0], sub(mul(b[1], c[2]), mul(b[2], c[1]))),
                   mul(a[1], sub(mul(b[0], c[2]), mul(b[2], c[0])))),
               mul(a[2], sub(mul(b[0], c[1]), mul(b[1], c[0]))))


def determinant(t):
    a, b, c, d = t
    edges = [tuple(sub(x[i], a[i]) for i in range(3)) for x in (b, c, d)]
    return det3(*edges)


def squared_determinant_by_gram(t):
    # Independent calculation via the Gram determinant of the three edges.
    a, b, c, d = t
    e = [tuple(sub(x[i], a[i]) for i in range(3)) for x in (b, c, d)]
    g = [[dot(e[i], e[j]) for j in range(3)] for i in range(3)]
    return det3(*g)


def sign(a):
    # Exact sign: conjugate quadratic field embedding, sqrt(5) between 2 and 3.
    # For a+b phi, compare N=(a+b phi)(a+b(1-phi))=a^2+ab-b^2.
    x, y = a
    if x == 0 and y == 0:
        return 0
    if y == 0:
        return 1 if x > 0 else -1
    # a+b phi = (2a+b+b sqrt5)/2; sqrt5 > 2.
    # For opposing signs of p=2a+b and b, use squared comparison.
    p = 2*x + y
    if p >= 0 and y >= 0:
        return 1
    if p <= 0 and y <= 0:
        return -1
    d = p*p - 5*y*y
    if p > 0:  # y < 0
        return 1 if d > 0 else -1
    # p < 0 and y > 0
    return 1 if d < 0 else -1


def absolute(a):
    return a if sign(a) >= 0 else neg(a)


def vertices():
    v = [((i, 0), (j, 0), (k, 0)) for i, j, k in product((-1, 1), repeat=3)]
    for i, j in product((-1, 1), repeat=2):
        p, q = scal(i, INVPHI), scal(j, PHI)
        v.extend(((Z, p, q), (q, Z, p), (p, q, Z)))
    assert len(v) == len(set(v)) == 20
    assert all(dot(x, x) == (3, 0) for x in v)
    return sorted(v)

# Each key is an absolute determinant coefficient pair (a,b); frequency among
# all unordered four-element vertex subsets. Ordinary tetrahedral volume is
# determinant/6.
EXPECTED = {
    (0, 0): 495,
    (8, -4): 320,
    (-4, 4): 900,
    (4, 0): 1110,
    (-8, 8): 120,
    (0, 4): 900,
    (8, 0): 400,
    (-4, 8): 150,
    (4, 4): 320,
    (0, 8): 120,
    (16, 0): 10,
}


def run():
    # Compare the externally listed certificate with the computed distribution.
    with Path(__file__).with_name('spectrum.csv').open(newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 11
    from_file = {}
    incidence_from_file = {}
    for row in rows:
        key = (int(row['det_a']), int(row['det_b']))
        assert key not in from_file
        from_file[key] = int(row['all_unordered_quadruples'])
        incidence_from_file[key] = int(row['through_fixed_vertex'])
    assert from_file == EXPECTED
    v = vertices()
    full = Counter()
    incidence = Counter()
    sum_squares = Z
    gram_sum = Z
    for idx in combinations(range(20), 4):
        t = tuple(v[i] for i in idx)
        raw = determinant(t)
        squared_gram = squared_determinant_by_gram(t)
        square = mul(raw, raw)
        assert square == squared_gram, (idx, square, squared_gram)
        k = absolute(raw)
        full[k] += 1
        if v.index((O, O, O)) in idx:
            incidence[k] += 1
        sum_squares = add(sum_squares, square)
        gram_sum = add(gram_sum, squared_gram)
    assert len(full) == 11
    assert full == Counter(EXPECTED), (full, EXPECTED)
    assert sum(full.values()) == comb(20, 4) == 4845
    assert sum(incidence.values()) == comb(19, 3) == 969
    # Vertex-transitivity of the dodecahedron yields 4N=20n_v.
    assert all(5*incidence[k] == full[k] for k in EXPECTED)
    assert incidence == Counter(incidence_from_file)
    assert sum_squares == gram_sum == (160000, 0)
    # The Cauchy--Binet prediction follows from X^T X = 20 I_4:
    assert all(tuple(sum(x[i][k] for x in v) for k in (0, 1)) == Z for i in range(3))
    assert all(sum((dot(x, x)[0] for x in v)) == 60 for _ in [0])
    assert all(
        sum((mul(x[i], x[j])[k] for x in v)) == (20 if i == j else 0) * (k == 0)
        for i in range(3) for j in range(3) for k in (0, 1)
    )
    assert full[(16, 0)] == 10
    assert full[(0, 8)] == 120
    assert sum(full[k] for k in full if k != (0, 0)) == 4350
    return full, incidence


if __name__ == '__main__':
    full, incidence = run()
    for k in EXPECTED:
        print(f'{k[0]:4d} {k[1]:4d} : {full[k]:4d} ({incidence[k]:3d} through a fixed vertex)')
    print('PASS: 4845 exact determinants, 4845 independent Gram identities,')
    print('      969 fixed-vertex incidences, Cauchy--Binet second moment.')
