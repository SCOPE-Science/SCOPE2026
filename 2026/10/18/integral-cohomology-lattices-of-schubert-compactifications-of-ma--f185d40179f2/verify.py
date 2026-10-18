"""Exact sample checks for integral cup lattices of matrix-pencil Schubert surfaces.

No external dependencies. This checks finite instances of the general lattice
calculation; it does not prove the theorem for unbounded block sizes.
"""
from itertools import combinations
from math import gcd, prod


def determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    d = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if a[i][k]), None)
            if piv is None:
                return 0
            a[k], a[piv] = a[piv], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (p * a[i][j] - a[i][k] * a[k][j]) // d
            a[i][k] = 0
        d = p
    return sign * a[-1][-1]


def dot(x, y):
    return x[0] * y[0] - sum(a * b for a, b in zip(x[1:], y[1:]))


def case(chains, regular):
    # chains: one list of strictly increasing distinct Jordan block sizes per eigenvalue.
    n = sum(sizes[-1] for sizes in chains)
    blocks, contracted = [], []
    offset = 0
    for sizes in chains:
        endpoints = set(sizes)
        prev = 0
        for k in sizes:
            blocks.append(tuple(range(offset + prev + 1, offset + k + 1)))
            prev = k
        for j in range(1, sizes[-1]):
            if j not in endpoints:
                v = [0] * (n + 1)
                v[offset + j] = 1
                v[offset + j + 1] = -1
                contracted.append(tuple(v))
        offset += sizes[-1]
    if regular:
        contracted.append(tuple([1] + [-1] * n))
    lengths = [len(b) for b in blocks]
    basis = []
    if not regular:
        basis.append(tuple([1] + [0] * n))
    for b in blocks:
        v = [0] * (n + 1)
        if regular:
            v[0] = -len(b)
        for i in b:
            v[i] = 1
        basis.append(tuple(v))
    assert len(basis) + len(contracted) == n + 1
    assert all(dot(x, e) == 0 for x in basis for e in contracted)
    gram = [[dot(x, y) for y in basis] for x in basis]
    r = len(lengths)
    if regular:
        expected = [[lengths[i] * lengths[j] - (lengths[i] if i == j else 0)
                     for j in range(r)] for i in range(r)]
        expected_det = (-1) ** r * (1 - sum(lengths)) * prod(lengths)
    else:
        expected = [[(1 if i == j == 0 else -lengths[i-1] if i == j else 0)
                     for j in range(r + 1)] for i in range(r + 1)]
        expected_det = (-1) ** r * prod(lengths)
    assert gram == expected
    assert determinant(gram) == expected_det
    # The combined basis of the contracted lattice and orthogonal kernel
    # need not be unimodular. Primitivity is tested directly via maximal minors.
    if contracted and n <= 8:
        m = len(contracted)
        g = 0
        for inds in combinations(range(n + 1), m):
            d = determinant([[v[i] for i in inds] for v in contracted])
            g = gcd(g, abs(d))
            if g == 1:
                break
        assert g == 1, (chains, regular, g)
    return len(basis), expected_det


def main():
    samples = [([], False), ([[1]], False), ([[2]], True), ([[1], [1]], True),
               ([[1, 3]], True), ([[1, 3]], False), ([[1, 2, 4]], True),
               ([[2, 5], [1, 3]], False), ([[2, 5], [1, 3]], True),
               ([[1, 2], [1, 2]], True), ([[3, 4]], True)]
    for chains, regular in samples:
        rank, disc = case(chains, regular)
        print(f'chains={chains}, regular={regular}, rank={rank}, signed_disc={disc}')
    print('EXACT_SAMPLE_CHECKS_OK')


if __name__ == '__main__':
    main()
