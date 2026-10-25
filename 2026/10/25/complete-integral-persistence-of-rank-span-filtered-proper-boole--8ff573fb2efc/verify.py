"""Exact, standard-library verification of Boolean rank-span topology data.

Enumerates simplices and computes simplicial homology over GF(2) in small
cases, independently comparing full face counts with closed formulas.
The finite calculation is not a proof of the uniform result.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, factorial


def stirling_second(s, j):
    dp = [[0] * (j + 2) for _ in range(s + 1)]
    dp[0][0] = 1
    for a in range(1, s + 1):
        for b in range(1, min(a, j) + 1):
            dp[a][b] = b * dp[a - 1][b] + dp[a - 1][b - 1]
    return dp[s][j]


def theoretical(n, k):
    ranks = [comb(n, s) * (2 ** (n - s) - 2) for s in range(n - 1)]
    beta = 2 ** n - 3
    for s in range(1, k + 1):
        beta = ranks[s] - beta
    f = [2 ** n - 2]
    for j in range(1, k + 1):
        f.append(sum(comb(n, s) * (2 ** (n - s) - 2)
                     * factorial(j) * stirling_second(s, j)
                     for s in range(j, k + 1)))
    return f, beta


def simplices(n, k):
    masks = list(range(1, 2 ** n - 1))
    by_dim = defaultdict(list)
    def grow(chain):
        by_dim[len(chain) - 1].append(chain)
        smallest = chain[0]
        last = chain[-1]
        for nxt in masks:
            if (last & nxt) == last and nxt != last and (nxt.bit_count() - smallest.bit_count() <= k):
                grow(chain + (nxt,))
    for mask in masks:
        grow((mask,))
    return by_dim


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            pivot = col.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = col
                break
            col ^= pivots[pivot]
    return len(pivots)


def homology(n, k):
    faces = simplices(n, k)
    actual = [len(faces[j]) for j in range(k + 1)]
    expected, beta = theoretical(n, k)
    assert actual == expected, (n, k, actual, expected)
    dranks = [0] * (k + 2)
    for j in range(1, k + 1):
        index = {face: pos for pos, face in enumerate(faces[j - 1])}
        cols = []
        for face in faces[j]:
            boundary = 0
            for h in range(len(face)):
                boundary ^= 1 << index[face[:h] + face[h+1:]]
            cols.append(boundary)
        dranks[j] = rank_mod2(cols)
    hom = [len(faces[j]) - dranks[j] - dranks[j + 1] for j in range(k + 1)]
    hom[0] -= 1
    assert hom == [0] * k + [beta], (n, k, hom, beta)
    return actual, hom


def main():
    tested = 0
    for n in range(3, 7):
        row = []
        for k in range(n - 1):
            f, h = homology(n, k)
            row.append(h[k])
            tested += 1
        print(f"n={n}: reduced mod-2 top Betti sequence {row}")
    for n in range(3, 41):
        for k in range(n - 1):
            f, beta = theoretical(n, k)
            chi = sum((-1) ** j * v for j, v in enumerate(f)) - 1
            assert chi == (-1) ** k * beta
            if k:
                _, previous = theoretical(n, k-1)
                assert beta + previous == comb(n, k)*(2**(n-k)-2)
        assert theoretical(n, n-2)[1] == 1
    print(f"VERIFY_OK: {tested} exact boundary-rank instances and all face/Euler formulas for 3 <= n <= 40")


if __name__ == '__main__':
    main()
