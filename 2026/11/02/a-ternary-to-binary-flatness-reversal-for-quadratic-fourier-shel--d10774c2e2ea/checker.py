#!/usr/bin/env python3
"""Exact-arithmetic verification of phase-alphabet fourth moments of quadratic torus shells.

Run with Python 3.9 or later: python3 checker.py
No third-party modules or input files are required.
"""
from itertools import combinations, product
from collections import Counter

# Eisenstein integers a+b*omega; omega^2+omega+1=0.
ZERO = (0, 0)
ONE = (1, 0)
OMEGA = (0, 1)
OMEGA2 = (-1, -1)
ROOTS3 = (ONE, OMEGA, OMEGA2)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1],
            a[0]*b[1] + a[1]*b[0] - a[1]*b[1])


def conj(a):
    return (a[0]-a[1], -a[1])


def norm(a):
    return a[0]*a[0] - a[0]*a[1] + a[1]*a[1]


def edge_names(n):
    return tuple(combinations(range(n), 2))


def edge_map(n, values):
    es = edge_names(n)
    assert len(values) == len(es)
    return dict(zip(es, values))


def quad_terms(a, i, j, k, l):
    return (mul(a[i, j], a[k, l]),
            mul(a[i, k], a[j, l]),
            mul(a[i, l], a[j, k]))


def fourth_moment_by_products(n, a):
    baseline = n*(n-1)*(4*n-7)//2
    defect = 0
    for i, j, k, l in combinations(range(n), 4):
        x, y, z = quad_terms(a, i, j, k, l)
        defect += norm(add(add(x, y), z))
    return baseline + 4*defect, defect


def fourth_moment_by_matrix(n, a):
    # This independent identity uses row correlations of the symmetric matrix.
    correlations = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            inner = ZERO
            for k in range(n):
                if k != i and k != j:
                    u = a[min(i,k), max(i,k)]
                    v = a[min(j,k), max(j,k)]
                    inner = add(inner, mul(u, conj(v)))
            correlations += norm(inner)
    lower = n*(n-1)*(n*n-3*n+3)//2
    return lower + correlations, correlations


def make_ternary_n5():
    a = {e: ONE for e in edge_names(5)}
    # Opposite edges of the K4 on vertices 1,2,3,4 have equal phases.
    for e in [(1,2), (3,4)]:
        a[e] = ONE
    for e in [(1,3), (2,4)]:
        a[e] = OMEGA
    for e in [(1,4), (2,3)]:
        a[e] = OMEGA2
    return a


def make_real_n6():
    c = (
        (0, 1, 1, 1, 1, 1),
        (1, 0, -1, -1, 1, 1),
        (1, -1, 0, 1, 1, -1),
        (1, -1, 1, 0, -1, 1),
        (1, 1, 1, -1, 0, -1),
        (1, 1, -1, 1, -1, 0),
    )
    for i in range(6):
        for j in range(6):
            assert c[i][j] == c[j][i]
            assert sum(c[i][k]*c[j][k] for k in range(6)) == (5 if i == j else 0)
    return c


def signed_submatrix(c, inds):
    n = len(inds)
    return edge_map(n, [ (c[inds[i]][inds[j]], 0)
                         for i, j in edge_names(n) ])


def normalized_phase_assignments(n, q):
    # Vertex-gauge symmetry fixes every coefficient incident to vertex 0.
    # The remaining (n-1 choose 2) edge phases are independent.
    fixed = {e: 0 for e in edge_names(n) if 0 in e}
    unknown = [e for e in edge_names(n) if 0 not in e]
    for digits in product(range(q), repeat=len(unknown)):
        exp = fixed.copy()
        exp.update(zip(unknown, digits))
        yield digits, exp


def minimal_binary_by_exact_enumeration(n):
    low = 10**8
    how_many = 0
    for digits, e in normalized_phase_assignments(n, 2):
        signed = {pair: (1 if d == 0 else -1, 0)
                  for pair, d in e.items()}
        m, _ = fourth_moment_by_products(n, signed)
        if m < low:
            low, how_many = m, 1
        elif m == low:
            how_many += 1
    return low, how_many


def ternary_quad_cost(x, y, z):
    # The squared absolute value of omega^x+omega^y+omega^z.
    if x == y == z:
        return 9
    if x != y and x != z and y != z:
        return 0
    return 3


def all_ternary_n6():
    n = 6
    es = edge_names(n)
    lookup = {e: ix for ix, e in enumerate(es)}
    unknown = [lookup[e] for e in es if 0 not in e]
    patterns = []
    for i, j, k, l in combinations(range(n), 4):
        patterns.append(((lookup[i,j], lookup[k,l]),
                         (lookup[i,k], lookup[j,l]),
                         (lookup[i,l], lookup[j,k])))
    best = 10**9
    count = 0
    sample = None
    checked = 0
    histogram = Counter()
    for digits in product(range(3), repeat=len(unknown)):
        exps = [0]*len(es)
        for ix, d in zip(unknown, digits):
            exps[ix] = d
        defect = 0
        for pattern in patterns:
            x, y, z = ((exps[r]+exps[s]) % 3 for r,s in pattern)
            defect += ternary_quad_cost(x,y,z)
        checked += 1
        histogram[defect] += 1
        if defect < best:
            best, count, sample = defect, 1, digits
        elif defect == best:
            count += 1
    expected_histogram = {
        27:360, 30:2646, 33:3240, 36:4680, 39:8640,
        42:9180, 45:10170, 48:4320, 51:5130, 54:2700,
        57:4050, 60:1080, 63:900, 69:810, 72:360,
        75:270, 81:420, 99:90, 135:3,
    }
    assert checked == 3**10 == 59049
    assert histogram == expected_histogram
    assert sum(histogram.values()) == 59049
    assert best == 27 and count == 360
    # Independently check an attaining witness with exact Eisenstein arithmetic.
    a = {e: ONE for e in es}
    exp = {e: 0 for e in es}
    for ix,d in zip(unknown, sample):
        exp[es[ix]] = d
    a.update({e: ROOTS3[d] for e,d in exp.items()})
    m1, defect = fourth_moment_by_products(6, a)
    m2, corr = fourth_moment_by_matrix(6, a)
    assert (m1, m2, defect, corr) == (363, 363, 27, 48)
    return best, count, sample


def independently_test_moment_identity():
    # Exhaust all normalized binary matrices through six vertices and compare
    # the two mathematically distinct exact integer identities.
    for n in (4,5,6):
        tested = 0
        for _, e in normalized_phase_assignments(n, 2):
            a = {pair: (1 if d == 0 else -1, 0)
                 for pair, d in e.items()}
            m1,_ = fourth_moment_by_products(n,a)
            m2,_ = fourth_moment_by_matrix(n,a)
            assert m1 == m2
            tested += 1
        assert tested == 2**((n-1)*(n-2)//2)


def main():
    assert add(add(ONE, OMEGA), OMEGA2) == ZERO
    assert [norm(z) for z in ROOTS3] == [1,1,1]
    independently_test_moment_identity()
    a5 = make_ternary_n5()
    assert fourth_moment_by_products(5, a5) == (130, 0)
    assert fourth_moment_by_matrix(5, a5) == (130, 0)
    c6 = make_real_n6()
    a6 = signed_submatrix(c6, tuple(range(6)))
    assert fourth_moment_by_products(6, a6) == (315, 15)
    assert fourth_moment_by_matrix(6, a6) == (315, 0)
    a5binary = signed_submatrix(c6, (1,2,3,4,5))
    assert fourth_moment_by_products(5, a5binary) == (150, 5)
    assert minimal_binary_by_exact_enumeration(4) == (58, 6)
    assert minimal_binary_by_exact_enumeration(5) == (150, 12)
    assert minimal_binary_by_exact_enumeration(6) == (315, 12)
    best, count, sample = all_ternary_n6()
    print('PASS: exact identities for all binary gauges at n=4,5,6;')
    print('      sharp n=5 ternary and binary fourth moments 130, 150;')
    print('      sharp n=6 binary fourth moment 315;')
    print('      exhaustive 59049 ternary gauges at n=6: minimum 363,')
    print('      360 normalized witnesses, example exponents:', sample)

if __name__ == '__main__':
    main()
