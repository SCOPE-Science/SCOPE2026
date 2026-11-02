#!/usr/bin/env python3
"""Exact finite checks of characteristic-selective graph-state entanglement.

All arithmetic and enumerations are deterministic and use only Python stdlib.
Execute: python3 verify.py
"""
from collections import Counter
from itertools import combinations, product, permutations
from math import comb

N = 16
V = [(a, b) for a in range(4) for b in range(4)]
P = (0, 1, 4, 15, 3, 2, 13, 6, 12, 7, 8, 9, 5, 14, 11, 10)
DIAG = (0, 5, 10, 15)


def make_graph(kind):
    rows = []
    for a, b in V:
        row = 0
        for j, (c, d) in enumerate(V):
            if kind == 'rook':
                edge = (a == c and b != d) or (b == d and a != c)
            elif kind == 'shrikhande':
                edge = ((c-a) % 4, (d-b) % 4) in {
                    (1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)
                }
            else:
                raise ValueError(kind)
            if edge:
                row |= 1 << j
        rows.append(row)
    return tuple(rows)


def edge(g, i, j):
    return (g[i] >> j) & 1


def check_srg(g):
    assert len(g) == N
    for i in range(N):
        assert not edge(g, i, i) and g[i].bit_count() == 6
        for j in range(N):
            assert edge(g, i, j) == edge(g, j, i)
            if i < j:
                assert (g[i] & g[j]).bit_count() == 2
    assert sum(row.bit_count() for row in g) // 2 == 48


def local_complement(g, v):
    # Toggle all pairs of distinct neighbours of v, simultaneously.
    h = list(g)
    for u in range(N):
        if edge(g, u, v):
            h[u] ^= g[v] ^ (1 << u)
    return tuple(h)


def rank_mod(g, subset, p):
    # Direct exact modular Gaussian elimination of the cut matrix.
    cols = [j for j in range(N) if j not in subset]
    a = [[edge(g, i, j) for j in cols] for i in subset]
    rank = 0
    for j in range(len(cols)):
        pivot = next((r for r in range(rank, len(a)) if a[r][j] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, p)
        for k in range(j, len(cols)):
            a[rank][k] = (a[rank][k] * inv) % p
        for r in range(rank+1, len(a)):
            factor = a[r][j]
            if factor:
                for k in range(j, len(cols)):
                    a[r][k] = (a[r][k] - factor*a[rank][k]) % p
        rank += 1
        if rank == len(a):
            break
    return rank


def binary_rank(g, mask):
    # A second, bit-packed elimination method for F_2.
    basis = {}
    complement = ((1 << N) - 1) ^ mask
    ans = 0
    for i in range(N):
        if (mask >> i) & 1:
            row = g[i] & complement
            while row:
                j = row.bit_length()-1
                if j in basis:
                    row ^= basis[j]
                else:
                    basis[j] = row
                    ans += 1
                    break
    return ans


def kernel_count3(g, subset):
    # Independent exhaustive GF(3) null-vector calculation, not elimination.
    complement = [j for j in range(N) if j not in subset]
    rows = [[edge(g, i, j) for j in complement] for i in subset]
    count = 0
    for coefficients in product(range(3), repeat=len(subset)):
        if all(x == 0 for x in coefficients):
            continue
        if all(sum(coefficients[i]*rows[i][j]
                   for i in range(len(subset))) % 3 == 0
               for j in range(len(complement))):
            count += 1
    return count


def induced_c4(g, subset):
    return all(sum(edge(g, i, j) for j in subset if j != i) == 2
               for i in subset)


def check_alternating_relation(g, subset):
    opposite = next((i, j) for i, j in combinations(subset, 2)
                    if not edge(g, i, j))
    other = [i for i in subset if i not in opposite]
    for v in range(N):
        if v not in subset:
            assert sum(edge(g, i, v) for i in opposite) == sum(
                edge(g, i, v) for i in other)


def determinant_integer(a):
    n = len(a)
    ans = 0
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j]
                  for i in range(n) for j in range(i+1, n))
        term = (-1) ** inv
        for i, j in enumerate(perm):
            term *= a[i][j]
        ans += term
    return ans


def check_binary_minor_bound():
    # All zero-one matrices of both sizes are enumerated, not sampled.
    bounds = {}
    for n, expected in ((3, 2), (4, 3)):
        largest = 0
        for bits in range(1 << (n*n)):
            a = [[(bits >> (n*i+j)) & 1 for j in range(n)]
                 for i in range(n)]
            largest = max(largest, abs(determinant_integer(a)))
        assert largest == expected
        bounds[n] = largest
    return bounds


def main():
    rook = make_graph('rook')
    shr = make_graph('shrikhande')
    for graph in (rook, shr):
        check_srg(graph)
    # Nonisomorphic: the open neighbourhood of a vertex has
    # two connected K3 components in rook and one C6 in Shrikhande.
    def neighborhood_components(graph):
        neighbors = {j for j in range(N) if edge(graph, 0, j)}
        sizes = []
        while neighbors:
            seed = next(iter(neighbors))
            seen = {seed}
            todo = [seed]
            while todo:
                u = todo.pop()
                for v in tuple(neighbors - seen):
                    if edge(graph, u, v):
                        seen.add(v)
                        todo.append(v)
            neighbors -= seen
            sizes.append(len(seen))
        return sorted(sizes)
    assert neighborhood_components(rook) == [3, 3]
    assert neighborhood_components(shr) == [6]
    # Graph equality after four diagonal local complementations and P.
    h = rook
    for v in DIAG:
        h = local_complement(h, v)
    assert sorted(P) == list(range(N))
    for i in range(N):
        for j in range(N):
            assert edge(h, i, j) == edge(shr, P[i], P[j])
    print('LC_ISOMORPHISM_OK: vertices (0,5,10,15), permutation', P)

    # Cut-rank conservation on *every* labelled binary bipartition.
    for mask in range(1 << N):
        permuted = sum(1 << P[i] for i in range(N) if mask & (1 << i))
        assert binary_rank(rook, mask) == binary_rank(shr, permuted)
    print('ALL_QUBIT_CUTS_OK:', 1 << N)

    max_d = check_binary_minor_bound()
    print('ZERO_ONE_DETERMINANT_BOUNDS_OK:', max_d)

    for g, label, expected in ((rook, 'rook', 36),
                               (shr, 'shrikhande', 12)):
        counts3 = Counter()
        counts5 = Counter()
        squares = 0
        square_sets = set()
        for subset in combinations(range(N), 4):
            r3 = rank_mod(g, subset, 3)
            r5 = rank_mod(g, subset, 5)
            # Independent exhaustive null-vector check over GF(3).
            assert kernel_count3(g, subset) == 3 ** (4-r3)-1
            assert r3 in (3, 4)
            assert r5 == r3
            is_square = induced_c4(g, subset)
            assert (r3 == 3) == is_square
            if is_square:
                squares += 1
                square_sets.add(frozenset(subset))
                check_alternating_relation(g, subset)
            counts3[r3] += 1
            counts5[r5] += 1
        assert sum(counts3.values()) == comb(16, 4) == 1820
        assert squares == expected
        assert counts3 == counts5 == Counter({3:expected, 4:1820-expected})
        if label == 'rook':
            expected_squares = {frozenset(4*a+b for a in aa for b in bb)
                for aa in combinations(range(4),2)
                for bb in combinations(range(4),2)}
        else:
            expected_squares = {frozenset(4*((a+t*da)%4)+((b+t*db)%4)
                                         for t in range(4))
                for a,b in V for da,db in ((1,0),(0,1),(1,1))}
        assert square_sets == expected_squares
        print('ODD_PRIME_FOUR_SITE_PROFILE_OK:',label,
              'rank 3 =', counts3[3], 'rank 4 =', counts3[4],
              'induced C4 =', squares)
    # Since every 4x4 zero-one determinant has absolute value <=3,
    # F_3 full rank implies full rank in every odd characteristic;
    # rank deficiency mod 5 implies integer rank <=3. Rank-3 minors
    # are <=2 in absolute value, so F_3 rank 3 survives every odd prime.
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
