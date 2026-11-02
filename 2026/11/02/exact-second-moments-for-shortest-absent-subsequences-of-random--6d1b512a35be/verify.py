"""Reproduce exact first and second moments for shortest absent subsequences.

Requires Python 3 standard library only.  Run: python verify.py
"""
from fractions import Fraction
from itertools import permutations, product


def matmul(a, b):
    return [
        [sum(a[i][t] * b[t][j] for t in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transfer(permutation):
    q = len(permutation)
    ranks = {symbol: rank for rank, symbol in enumerate(permutation)}
    return [[int(ranks[a] >= ranks[b]) for b in range(q)] for a in range(q)]


def matrix_sas(blocks, q):
    row = [[1] * q]
    for block in blocks:
        row = matmul(row, transfer(block))
    return sum(row[0])


def is_subsequence(pattern, word):
    it = iter(word)
    return all(any(x == symbol for x in it) for symbol in pattern)


def literal_sas(blocks, q):
    word = tuple(x for block in blocks for x in block)
    k = len(blocks)
    return sum(not is_subsequence(pattern, word)
               for pattern in product(range(q), repeat=k + 1))


def theory(q, k):
    h = Fraction(q + 1, 2)
    mean = q * h ** k
    t = Fraction((q + 1) * (3 * q + 4), 12)
    d = Fraction((q + 1) ** 2 * (q + 2), 72)
    m0 = Fraction(q * q)
    m1 = Fraction(q * q * (q + 1) ** 2, 4)
    if k == 0:
        second = m0
    elif k == 1:
        second = m1
    else:
        for _ in range(2, k + 1):
            m0, m1 = m1, t * m1 - d * m0
        second = m1
    return mean, second


def reduced_transfer(q):
    return [
        [Fraction(q + 1, 2), Fraction(q * q - 1, 3)],
        [Fraction(q + 1, 3), Fraction((q + 1) * (3 * q - 2), 12)],
    ]


def power_action(q, k):
    v = [[Fraction(1)], [Fraction(1)]]
    t = reduced_transfer(q)
    for _ in range(k):
        v = matmul(t, v)
    return q * v[0][0] + q * (q - 1) * v[1][0]


def exact_covariance(q):
    ps = list(permutations(range(q)))
    z = len(ps)
    matrix = [[Fraction(0) for _ in range(q * q)] for _ in range(q * q)]
    for p in ps:
        H = transfer(p)
        for a in range(q):
            for c in range(q):
                for b in range(q):
                    for d in range(q):
                        matrix[a * q + c][b * q + d] += Fraction(H[a][b] * H[c][d], z)
    T = reduced_transfer(q)
    for a in range(q):
        for c in range(q):
            row = matrix[a * q + c]
            diag = sum(row[b * q + b] for b in range(q))
            off = sum(row) - diag
            idx = 0 if a == c else 1
            assert (diag, off) == tuple(T[idx]), (q, a, c)


def check():
    for q in range(2, 6):
        exact_covariance(q)
        for k in range(0, 9):
            assert power_action(q, k) == theory(q, k)[1]
        print(f'q={q}: pair transfer and moment recurrence agree')

    for q, maxk in ((2, 6), (3, 3), (4, 2)):
        ps = list(permutations(range(q)))
        for k in range(1, maxk + 1):
            total = total_sq = count = 0
            for blocks in product(ps, repeat=k):
                computed = matrix_sas(blocks, q)
                direct = literal_sas(blocks, q)
                assert direct == computed, (q, k, blocks, direct, computed)
                total += direct
                total_sq += direct * direct
                count += 1
            mean, second = theory(q, k)
            assert Fraction(total, count) == mean
            assert Fraction(total_sq, count) == second
            print(f'q={q}, k={k}: {count} words, mean={mean}, second={second}')
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
