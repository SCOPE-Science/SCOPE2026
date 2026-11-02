"""Alternative finite checks of a cyclic Rule-110 predecessor theorem.

Uses direct truth-table evaluation, rather than the three-state proof graph,
and separately constructs the ordinary four-state de Bruijn transfer matrices.
Finite checks supplement, but do not establish, the all-length proof.
"""


def iterate_rule110(x, n):
    value = 0
    for i in range(n):
        a = (x >> ((i - 1) % n)) & 1
        b = (x >> i) & 1
        c = (x >> ((i + 1) % n)) & 1
        value |= ((110 >> (4 * a + 2 * b + c)) & 1) << i
    return value


def perrin(upper):
    p = [3, 0, 2]
    for i in range(3, upper + 1):
        p.append(p[i - 2] + p[i - 3])
    return p


def multiplication(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def pair_matrices():
    mats = [[[0] * 4 for _ in range(4)] for _ in range(2)]
    for left in range(2):
        for center in range(2):
            for right in range(2):
                old = 2 * left + center
                new = 2 * center + right
                label = (110 >> (4 * left + 2 * center + right)) & 1
                mats[label][old][new] += 1
    return mats


def trace_product(y, n, matrices):
    p = [[int(i == j) for j in range(4)] for i in range(4)]
    for i in range(n):
        p = multiplication(p, matrices[(y >> i) & 1])
    return sum(p[i][i] for i in range(4))


def check():
    p = perrin(19)
    assert p[:11] == [3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17]
    matrices = pair_matrices()
    for n in range(1, 14):
        counts = [0] * (1 << n)
        for x in range(1 << n):
            counts[iterate_rule110(x, n)] += 1
        assert sum(counts) == 1 << n
        assert counts[(1 << n) - 1] == p[n], (n, counts[-1], p[n])
        assert counts[0] == 2
        assert all(c <= p[y.bit_count()] for y, c in enumerate(counts))
        if n >= 5:
            maxima = [y for y, c in enumerate(counts) if c == max(counts)]
            assert maxima == [(1 << n) - 1], (n, maxima)
        if n <= 7:
            for y, observed in enumerate(counts):
                assert trace_product(y, n, matrices) == observed, (n, y)
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
