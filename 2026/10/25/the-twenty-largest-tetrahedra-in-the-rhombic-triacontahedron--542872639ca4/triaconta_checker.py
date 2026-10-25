"""Exact determinant certificate for tetrahedra in the rhombic triacontahedron.

Run with Python 3 (standard library only): python3 triaconta_checker.py
All arithmetic is exact in Z[phi], phi^2=phi+1; no floating point is used.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
INV_PHI = (-1, 1)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c + b*d)

def sign(x):
    """Sign of a+b*phi via exact comparison of (2a+b)+b*sqrt(5)."""
    a, b = x
    c = 2*a + b
    if b == 0:
        return (c > 0) - (c < 0)
    if c == 0 or (c > 0) == (b > 0):
        return 1 if b > 0 else -1
    q = c*c - 5*b*b
    if q == 0:
        raise AssertionError('sqrt(5) would be rational')
    return (1 if c > 0 else -1) * (1 if q > 0 else -1)

def compare(x, y):
    return sign(sub(x, y))

def determinant3(x, y, z):
    terms = [
        mul(x[0], sub(mul(y[1], z[2]), mul(y[2], z[1]))),
        mul(x[1], sub(mul(y[0], z[2]), mul(y[2], z[0]))),
        mul(x[2], sub(mul(y[0], z[1]), mul(y[1], z[0])))
    ]
    return add(sub(terms[0], terms[1]), terms[2])

def determinant3_independent(x, y, z):
    from itertools import permutations
    result = ZERO
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1,3))
        term = mul(mul(x[p[0]], y[p[1]]), z[p[2]])
        result = add(result, neg(term) if inversions % 2 else term)
    return result

def cycles(t):
    return (t, (t[2], t[0], t[1]), (t[1], t[2], t[0]))

def generate_vertices():
    vertices = []
    kinds = []
    for A, B, kind in ((ONE, PHI, 'icosahedral'), (PHI, INV_PHI, 'dodecahedral')):
        for s, t in product((1, -1), repeat=2):
            for pt in cycles((ZERO, A if s > 0 else neg(A), B if t > 0 else neg(B))):
                vertices.append(pt)
                kinds.append(kind)
    for signs in product((1, -1), repeat=3):
        vertices.append(tuple(ONE if s > 0 else neg(ONE) for s in signs))
        kinds.append('dodecahedral')
    assert len(vertices) == len(set(vertices)) == 32
    assert kinds.count('icosahedral') == 12
    assert kinds.count('dodecahedral') == 20
    return vertices, kinds

def analyze():
    vertices, kinds = generate_vertices()
    max_determinant = ZERO
    maximizing = []
    levels = Counter()
    kinds_by_level = Counter()
    checked = 0
    for indices in combinations(range(32), 4):
        a, b, c, d = [vertices[i] for i in indices]
        x, y, z = [tuple(sub(pt[k], a[k]) for k in range(3)) for pt in (b, c, d)]
        det = determinant3(x, y, z)
        assert det == determinant3_independent(x, y, z)
        absdet = det if sign(det) >= 0 else neg(det)
        levels[absdet] += 1
        kinds_by_level[(absdet, sum(kinds[j] == 'icosahedral' for j in indices))] += 1
        cmp = compare(absdet, max_determinant)
        if cmp > 0:
            max_determinant = absdet
            maximizing = [indices]
        elif cmp == 0:
            maximizing.append(indices)
        checked += 1
    assert checked == comb(32, 4) == 35960
    assert max_determinant == (6, 8)
    assert len(maximizing) == 20
    assert all(sum(kinds[i] == 'icosahedral' for i in ids) == 3 for ids in maximizing)
    triple_counts = Counter(tr for ids in maximizing for tr in combinations(ids, 3))
    assert max(triple_counts.values()) == 1, 'Nonvertex maximizers may exist'
    def squared_length(p, q):
        return add(add(mul(sub(p[0],q[0]),sub(p[0],q[0])),mul(sub(p[1],q[1]),sub(p[1],q[1]))),mul(sub(p[2],q[2]),sub(p[2],q[2])))
    for ids in maximizing:
        ico = [vertices[j] for j in ids if kinds[j] == 'icosahedral']
        dod = [vertices[j] for j in ids if kinds[j] == 'dodecahedral'][0]
        assert all(squared_length(a,b) == (4,4) for a,b in combinations(ico,2))
        ico_sum = tuple(add(add(ico[0][j],ico[1][j]),ico[2][j]) for j in range(3))
        assert all(add(dod[j],mul(PHI,ico_sum[j])) == ZERO for j in range(3))
    ico_ids = [i for i,k in enumerate(kinds) if k=='icosahedral']
    large_equilateral = sum(all(squared_length(vertices[i], vertices[j]) == (4,4)
                         for i,j in combinations(ids,2))
                         for ids in combinations(ico_ids,3))
    assert large_equilateral == len(maximizing) == 20
    assert levels[(16, 0)] == 10, 'Classic regular tetrahedron compound not detected'
    print('CERTIFICATE_OK')
    print('vertex_count =', len(vertices))
    print('four_vertex_subsets =', checked)
    print('maximum_det = 6+8*phi')
    print('maximum_volume = (6+8*phi)/6 = (5+2*sqrt(5))/3')
    print('maximizer_count =', len(maximizing))
    print('all_maximizers_three_icosa_one_dodeca = True')
    print('no_two_maximizers_share_three_vertices = True')
    print('large_equilateral_icosahedral_triangles = 20')
    print('every_maximizer_apex_equals_minus_phi_times_triangle_sum = True')
    print('regular_tetrahedron_compound_determinant = 16, count =', levels[(16, 0)])
    print('determinant_levels_nonzero =', len(levels)-int(ZERO in levels))
    print('example_indices =', maximizing[0])
    for i in maximizing[0]:
        print('vertex', i, kinds[i], vertices[i])

if __name__ == '__main__':
    analyze()
