"""Exact arithmetic checks for two truncated-triplex graph families.

Requires only Python 3 standard library. The universal assertions follow
from the block decomposition and polynomial identities given in RESULT.md;
finite graph enumerations provide independent calibration.
"""
from itertools import combinations


def bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            replacement = next((i for i in range(k + 1, n) if a[i][k]), None)
            if replacement is None:
                return 0
            a[k], a[replacement] = a[replacement], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def graph_trees(vertices, edges):
    verts = sorted(vertices)
    index = {v: i for i, v in enumerate(verts)}
    n = len(verts)
    laplacian = [[0] * n for _ in range(n)]
    for a, b in edges:
        i, j = index[a], index[b]
        assert i != j
        laplacian[i][i] += 1
        laplacian[j][j] += 1
        laplacian[i][j] -= 1
        laplacian[j][i] -= 1
    return bareiss([row[1:] for row in laplacian[1:]])


def edge_set():
    return set()


def addedge(edges, a, b):
    assert a != b
    edges.add(tuple(sorted((a, b))))


def a_graph(d):
    assert d >= 3
    r = d - 3
    base = ['u%d' % j for j in range(r)] + ['c%d' % j for j in range(4)]
    old = edge_set()
    for i, j in combinations(range(r), 2):
        addedge(old, 'u%d' % i, 'u%d' % j)
    for i in range(r):
        for j in range(4):
            addedge(old, 'u%d' % i, 'c%d' % j)
    for j in range(4):
        addedge(old, 'c%d' % j, 'c%d' % ((j + 1) % 4))
    vertices = [(b, layer) for b in base for layer in range(2)]
    edges = edge_set()
    for a, b in old:
        for layer in range(2):
            addedge(edges, (a, layer), (b, layer))
    for b in base:
        addedge(edges, (b, 0), (b, 1))
    return vertices, edges


def b_graph(d):
    assert d >= 3
    r = d - 3
    prism = ['a0', 'a1', 'a2', 'b0', 'b1', 'b2']
    apices = ['u%d' % j for j in range(r)]
    vertices = prism + apices
    edges = edge_set()
    for triangle in (prism[:3], prism[3:]):
        for a, b in combinations(triangle, 2):
            addedge(edges, a, b)
    for j in range(3):
        addedge(edges, 'a%d' % j, 'b%d' % j)
    for apex in apices:
        for neighbor in vertices:
            if apex != neighbor:
                addedge(edges, apex, neighbor)
    removed = 'a0'
    neighbors = sorted(v if u == removed else u
                       for u, v in edges if removed in (u, v))
    assert len(neighbors) == d
    edges = {e for e in edges if removed not in e}
    fresh = ['t_' + v for v in neighbors]
    for new, old in zip(fresh, neighbors):
        addedge(edges, new, old)
    for a, b in combinations(fresh, 2):
        addedge(edges, a, b)
    return [x for x in vertices if x != removed] + fresh, edges


def a_formula(d):
    return (d - 1) ** 2 * (d + 1) ** (d - 1) * (d + 3) ** (d - 2)


def b_formula(d):
    assert d >= 4
    return (d * (d + 1) * (d * d + 2 * d - 1)
            * (d ** 3 + 3 * d * d - d - 5)
            * (d * d + 4 * d + 2) ** (d - 4))


def quotient(r):
    d = r + 3
    return [
        [r + 2, -1, 0, -r, -1, 0, 0],
        [-1, r + 2, -1, -r, 0, 0, 0],
        [0, -2, d, -r, 0, -1, 0],
        [-2, -2, -1, 6, 0, 0, -1],
        [-1, 0, 0, 0, r + 2, -1, -r],
        [0, 0, -1, 0, -2, d, -r],
        [0, 0, 0, -1, -2, -1, 4],
    ]


def main():
    for r in range(7):
        Q = quotient(r)
        assert all(sum(row) == 0 for row in Q)
        cofactor = bareiss([[entry for j, entry in enumerate(row) if j != 2]
                            for i, row in enumerate(Q) if i != 2])
        assert cofactor == (r + 3) * (r ** 3 + 12*r*r + 44*r + 46)
    # Each entry of the 6x6 minor is affine in r, so its determinant
    # has degree at most six. Seven exact values prove the identity.
    for d in range(4, 16):
        std = bareiss([[d + 3, -1], [-1, d + 1]])
        odd = bareiss([[d + 1, -1, -1], [-1, d + 1, 0], [-1, 0, d + 1]])
        assert std == d*d + 4*d + 2
        assert odd == (d + 1) * (d*d + 2*d - 1)
        h = d - 3
        diff = ((d - 1)**2 * (d + 1)**2 * (d + 3)**2
                - d*(d*d + 2*d - 1)*(d**3 + 3*d*d - d - 5))
        assert diff == h**5 + 18*h**4 + 124*h**3 + 406*h*h + 628*h + 372
        assert diff > 0
    for d in range(3, 11):
        va, ea = a_graph(d)
        vb, eb = b_graph(d)
        assert len(va) == len(vb) == 2*d + 2
        assert len(ea) == len(eb) == (d + 3)*(d - 1)
        ta, tb = graph_trees(va, ea), graph_trees(vb, eb)
        assert ta == a_formula(d)
        assert tb == (336 if d == 3 else b_formula(d))
        assert ta > tb
    print('VERIFY_OK')
    print('Seven symbolic-identity interpolation points; twelve block checks;')
    print('eight complete graph-cofactor comparisons (d=3,...,10).')

if __name__ == '__main__':
    main()
