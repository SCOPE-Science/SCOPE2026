"""Reproduce finite tests of three-tap convolution on generalized dihedral groups.

Python 3 standard library only. Ranks are computed modulo 1000003; these are
finite consistency tests, not a substitute for the all-characteristic proof.
"""
import itertools
import math
from collections import Counter


def group(p, d):
    A = list(itertools.product(range(p), repeat=d))
    G = [(v, e) for e in range(2) for v in A]

    def mul(a, b):
        t = 1 if a[1] == 0 else -1
        return (tuple((x + t * y) % p for x, y in zip(a[0], b[0])),
                (a[1] + b[1]) % 2)
    return A, G, mul


def rank_mod(matrix, prime=1000003):
    a = [[x % prime for x in row] for row in matrix]
    m, n = len(a), len(a[0]); rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, prime)
        a[rank] = [(v * inv) % prime for v in a[rank]]
        for i in range(rank+1, m):
            f = a[i][j]
            if f:
                a[i] = [(x - f * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def predicted_nullity(p, d, three):
    n = p ** d
    if p != 3:
        return 0
    if len({s[1] for s in three}) == 2:
        return 2*n // 3
    v0, v1, v2 = (s[0] for s in three)
    a = tuple((x-y) % 3 for x, y in zip(v1, v0))
    b = tuple((x-y) % 3 for x, y in zip(v2, v0))
    return 4*n // (3 if b in {tuple((t*x) % 3 for x in a) for t in range(3)} else 9)


def run(p, d, exhaustive=True):
    A, G, mul = group(p, d)
    n = len(G); N = len(A)
    lookup = {g:i for i, g in enumerate(G)}
    permutations = [[lookup[mul(s,g)] for g in G] for s in G]
    triples = list(itertools.combinations(range(n), 3))
    if not exhaustive:
        triples = triples[::max(1, len(triples)//80)]
    counts = Counter()
    for triple in triples:
        mat = [[0]*n for _ in range(n)]
        for t in triple:
            for j, i in enumerate(permutations[t]):
                mat[i][j] += 1
        nullity = n-rank_mod(mat)
        expected = predicted_nullity(p, d, [G[i] for i in triple])
        assert nullity == expected, (p,d,triple,nullity,expected)
        counts[nullity] += 1
    if p == 3 and exhaustive:
        lines = N*(N-1)//6
        expected_counts = {2*N//3:N*N*(N-1), 4*N//3:2*lines}
        if d >= 2:
            expected_counts[4*N//9] = 2*(math.comb(N,3)-lines)
        assert counts == expected_counts, (counts, expected_counts)
    print('CHECK', (p,d), 'tested', len(triples), 'nullities', dict(sorted(counts.items())))


if __name__ == '__main__':
    for p,d in [(2,2), (2,3), (3,1), (3,2), (5,1)]:
        run(p,d)
    run(3,3,False)
    print('VERIFY_OK')
