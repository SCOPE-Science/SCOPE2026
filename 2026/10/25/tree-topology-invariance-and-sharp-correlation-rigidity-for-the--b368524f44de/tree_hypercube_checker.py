"""Exact coefficient certificate for tree-Ising four-cube simplex weights.

Uses only the Python standard library. No numerical fitting or random sampling.
"""
from itertools import combinations, permutations, product
from collections import Counter

VERTICES = tuple(product((0, 1), repeat=4))
EDGES = tuple(combinations(range(4), 2))
PERMS = tuple(permutations(range(4)))
SIGNS = tuple((-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1,4)) for p in PERMS)


def determinant4(rows):
    return sum(sign * rows[0][p[0]] * rows[1][p[1]] * rows[2][p[2]] * rows[3][p[3]]
               for p, sign in zip(PERMS, SIGNS))


def simplices():
    out = []
    hist = Counter()
    for U in combinations(range(16), 5):
        anchor = VERTICES[U[0]]
        rows = [[VERTICES[k][j] - anchor[j] for j in range(4)] for k in U[1:]]
        d = abs(determinant4(rows))
        hist[d] += 1
        if d:
            out.append((U, d))
    assert dict(hist) == {0: 1360, 1: 2672, 2: 320, 3: 16}, hist
    assert sum(d for U, d in out) == 3360
    return out


def is_tree(edges):
    seen = {0}
    while True:
        nxt = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if nxt == seen:
            return len(seen) == 4
        seen = nxt


def polynomial_on_tree(edges, rho, terms):
    a, b, c = rho
    weights = []
    for v in VERTICES:
        spin = tuple(1 if j == 0 else -1 for j in v)
        weights.append((1 + a * spin[edges[0][0]] * spin[edges[0][1]]) *
                       (1 + b * spin[edges[1][0]] * spin[edges[1][1]]) *
                       (1 + c * spin[edges[2][0]] * spin[edges[2][1]]))
    return sum(d * weights[U[0]] * weights[U[1]] * weights[U[2]] * weights[U[3]] * weights[U[4]]
               for U, d in terms)


def target_polynomial(a, b, c):
    A, B, C = a*a, b*b, c*c
    return 32*(1-A)*(1-B)*(1-C)*(105+15*(A+B+C)-7*(A*B+A*C+B*C)-A*B*C)


def check():
    terms = simplices()
    trees = tuple(e for e in combinations(EDGES, 3) if is_tree(e))
    assert len(trees) == 16
    grid = tuple(product((0, 1, 2), repeat=3))
    for edges in trees:
        for rho in grid:
            got = polynomial_on_tree(edges, rho, terms)
            want = target_polynomial(*rho)
            assert got == want, (edges, rho, got, want)
    # Independent explicit normalization check at uniform weights.
    assert sum(d for _, d in terms)*16**3 == 105*8**8//128
    print('TREE_HYPERCUBE_OK trees=16 grid_per_tree=27 subsets=4368 nonzero=3008')


if __name__ == '__main__':
    check()
