#!/usr/bin/env python3
"""Exact integer checks for the all-degree Fermat-line Fourier spectrum.

For every test degree d this independently constructs the 3d^2 by 3d^2
incidence matrix from the three projective-line intersection congruences.
All calculations use standard-library arbitrary-precision integers.
The polynomial identity and the first r spectral moments together certify
the entire asserted spectrum at each tested degree (not for all degrees).
"""


def spectrum(d):
    if d % 2:
        return {
            4*d - 2: 1,
            d - 2: 9*d - 7,
            -2: 3*(d-1)*(d-3),
            -d - 2: 3*(d-1),
        }
    return {
        4*d - 2: 1,
        d - 2: 9*d - 8,
        -2: 3*(d-2)**2,
        -d - 2: 3*(d-2),
        -2*d - 2: 1,
    }


def graph(d):
    N = 3 * d * d
    nbr = [set() for _ in range(N)]
    def idx(f, a, b): return f*d*d + a*d + b
    def edge(i, j):
        assert i != j
        nbr[i].add(j)
        nbr[j].add(i)
    for f in range(3):
        for a in range(d):
            for b in range(d):
                for c in range(d):
                    for e in range(d):
                        if (a, b) < (c, e) and (a == c or b == e):
                            edge(idx(f, a, b), idx(f, c, e))
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    if (a + e - b - c) % d == 0:
                        edge(idx(0,a,b), idx(1,c,e))
                    if (c - a - b - e - 1) % d == 0:
                        edge(idx(0,a,b), idx(2,c,e))
                    if (c + e - a - b) % d == 0:
                        edge(idx(1,a,b), idx(2,c,e))
    assert all(len(x) == 4*d - 2 for x in nbr)
    assert all(i in nbr[j] and i != j for i, row in enumerate(nbr) for j in row)
    return [sorted(row) for row in nbr]


def right_multiply_by_adjacency(mat, nbr):
    size = len(nbr)
    nxt = [[0]*size for _ in range(size)]
    for i, row in enumerate(mat):
        res = nxt[i]
        for j, neighbors in enumerate(nbr):
            res[j] = sum(row[k] for k in neighbors)
    return nxt


def check(d):
    spec = {a:b for a,b in spectrum(d).items() if b}
    N = 3*d*d
    assert sum(spec.values()) == N
    nbr = graph(d)
    B = [[int(i == j) for j in range(N)] for i in range(N)]
    # The first r moments determine the multiplicities of r distinct roots
    # by Vandermonde nondegeneracy, after the annihilating identity is checked.
    for k in range(len(spec)):
        moment = sum(B[i][i] for i in range(N))
        expected = sum(mult * eig**k for eig, mult in spec.items())
        assert moment == expected, (d, k, moment, expected)
        B = right_multiply_by_adjacency(B, nbr)
    # Multiply the linear factors (A-lambda I), exactly, acting on I.
    B = [[int(i == j) for j in range(N)] for i in range(N)]
    for eig in spec:
        C = right_multiply_by_adjacency(B, nbr)
        B = [[C[i][j] - (eig * B[i][j]) for j in range(N)] for i in range(N)]
    assert all(entry == 0 for row in B for entry in row), (d,'annihilator')
    # Line intersection matrix has diagonal 2-d and off-diagonal adjacency.
    nonzero_gram = sum(m for eig,m in spec.items() if eig != d-2)
    rank = 3*(d-1)*(d-2) + 1 + (d % 2 == 0)
    assert nonzero_gram == rank
    assert spec[4*d-2] == 1  # connectedness: top eigenvalue simple
    print('degree=%d lines=%d degree_of_graph=%d distinct_eigenvalues=%d '
          'gram_rank=%d spectrum=%s VERIFIED' %
          (d,N,4*d-2,len(spec),rank,sorted(spec.items(),reverse=True)))


if __name__ == '__main__':
    for degree in (3,4,5,6,7,8,9):
        check(degree)
    print('VERIFY_OK')
