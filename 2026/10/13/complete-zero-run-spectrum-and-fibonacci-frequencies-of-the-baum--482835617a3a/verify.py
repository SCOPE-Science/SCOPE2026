"""Standalone finite checks of a symbolic gap-spectrum theorem for the Baum-Sweet word."""
from collections import Counter


def fibs(n):
    f = [0, 1]
    while len(f) <= n:
        f.append(f[-1] + f[-2])
    return f


def baum_sweet(n):
    if n == 0:
        return 1
    s = format(n, 'b')
    return int(all(len(z) % 2 == 0 for z in s.split('1') if z))


def central(j):
    assert j >= 2
    return (1 << (j - 2)) + 1 + (j % 2 == 0)


def expected(K):
    F = fibs(K + 3)
    out = Counter({1: (K + 1) // 2, 2: K // 2})
    if K >= 2:
        out[3] = F[K + 1] - 2
    for j in range(4, K):
        out[central(j)] = F[K - j + 2] - 1
    return +out


def verify():
    Kmax = 18
    limit = 1 << Kmax
    direct = [baum_sweet(n) for n in range(limit)]
    recurrence = [1] * limit
    for n in range(1, limit):
        if n % 2:
            recurrence[n] = recurrence[n // 2]
        elif n % 4 == 2:
            recurrence[n] = 0
        else:
            recurrence[n] = recurrence[n // 4]
    assert direct == recurrence

    F = fibs(Kmax + 3)
    for K in range(1, Kmax + 1):
        positions = [n for n in range(1 << K) if direct[n]]
        gaps = Counter(b - a for a, b in zip(positions, positions[1:]))
        predicted = expected(K)
        assert gaps == predicted, (K, gaps, predicted)
        assert len(positions) == F[K + 2], K
        assert sum(predicted.values()) == len(positions) - 1

    for L in range(2, 14):
        from itertools import product
        words = [''.join(x) for x in product('01', repeat=L)]
        legal = [x for x in words if all(len(z) % 2 == 0 for z in x.split('1') if z)]
        left = [x for x in legal if x.startswith('00')]
        right = [x for x in legal if x.startswith('1')]
        assert left and right
        assert int(right[0], 2) - int(left[-1], 2) == central(L)

    print(f'VERIFY_OK direct_terms={limit} dyadic_cutoffs={Kmax} symbolic_central_boundaries=12 exact_counts=all')


if __name__ == '__main__':
    verify()
