#!/usr/bin/env python3
"""Independent finite-field checks for block-code absorption on binary cubes.

Uses only the Python standard library. Character restriction ranks are exact:
Walsh characters restricted to a binary subspace are orthogonal over F_3,
so their ranks in odd characteristic equal their ranks over the rationals.
The Krylov comparisons independently use adjacency multiplication over F_101;
all cube adjacency eigenvalues are distinct modulo 101 for the tested sizes.
Finite checks supplement, not replace, the all-dimensions proof.
"""
from itertools import combinations
from math import comb


def partitions_of(n):
    for mask in range(1 << (n - 1)):
        blocks, run = [], 1
        for j in range(n - 1):
            if (mask >> j) & 1:
                blocks.append(run)
                run = 1
            else:
                run += 1
        blocks.append(run)
        yield tuple(blocks)


def trap_sites(blocks):
    out = []
    for pattern in range(1 << len(blocks)):
        site, offset = 0, 0
        for i, length in enumerate(blocks):
            if (pattern >> i) & 1:
                site |= ((1 << length) - 1) << offset
            offset += length
        out.append(site)
    return out


def rank_mod(vectors, modulus):
    pivots = {}
    rank = 0
    for vec in vectors:
        v = [int(x) % modulus for x in vec]
        for i in range(len(v)):
            a = v[i]
            if not a:
                continue
            if i in pivots:
                row = pivots[i]
                for j in range(i, len(v)):
                    v[j] = (v[j] - a * row[j]) % modulus
            else:
                inv = pow(a, -1, modulus)
                pivots[i] = [0] * i + [(z * inv) % modulus for z in v[i:]]
                rank += 1
                break
    return rank


def expected_profile(n, m):
    s = n - m + 1
    return [sum(comb(m - 1, j) for j in range(max(0, w - s),
                                           min(m - 1, w) + 1))
            for w in range(n + 1)]


def walsh_profile(blocks):
    n = sum(blocks)
    traps = trap_sites(blocks)
    ranks = []
    for w in range(n + 1):
        vectors = []
        for chosen in combinations(range(n), w):
            mask = sum(1 << j for j in chosen)
            vectors.append([1 if ((mask & x).bit_count() & 1) == 0 else -1
                            for x in traps])
        ranks.append(rank_mod(vectors, 3))
    return ranks


def krylov_bright_rank(blocks):
    n = sum(blocks)
    dim = 1 << n
    current = []
    for x in trap_sites(blocks):
        row = [0] * dim
        row[x] = 1
        current.append(row)
    rows = [row[:] for row in current]
    for _ in range(n):
        current = [[sum(row[y ^ (1 << j)] for j in range(n)) % 101
                    for y in range(dim)] for row in current]
        rows.extend(current)
    return rank_mod(rows, 101)


def main():
    spectral = 0
    krylov = 0
    for n in range(2, 8):
        for blocks in partitions_of(n):
            predicted = expected_profile(n, len(blocks))
            actual = walsh_profile(blocks)
            assert actual == predicted, (blocks, actual, predicted)
            assert sum(actual) == (1 << (len(blocks) - 1)) * (
                n - len(blocks) + 2)
            spectral += 1
            if n <= 5:
                direct = krylov_bright_rank(blocks)
                assert direct == sum(predicted), (blocks, direct, sum(predicted))
                krylov += 1
    for blocks in ((2, 2, 2, 2), (1, 1, 3, 3), (1, 2, 2, 3),
                   (1, 1, 1, 5), (4, 4), (3, 5), (2, 6), (1, 7)):
        assert walsh_profile(blocks) == expected_profile(8, len(blocks))
        spectral += 1
    assert expected_profile(8, 4) == [1, 4, 7, 8, 8, 8, 7, 4, 1]
    assert sum(expected_profile(8, 4)) == 48
    print(f'VERIFY_OK spectral_partitions={spectral} krylov_partitions={krylov}')


if __name__ == '__main__':
    main()
