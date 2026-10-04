from fractions import Fraction
from itertools import product


def e_bh(values, alpha):
    K = len(values)
    order = sorted(range(K), key=lambda i: values[i], reverse=True)
    kval = 0
    for r in range(1, K + 1):
        if values[order[r - 1]] >= Fraction(K, 1) / (alpha * r):
            kval = r
    if kval == 0:
        return set()
    cutoff = Fraction(K, 1) / (alpha * kval)
    return {i for i, v in enumerate(values) if v >= cutoff}


def threshold_grid_check():
    alpha = Fraction(1, 5)
    for K in range(2, 9):
        for m in range(1, K + 1):
            b = Fraction(K, 1) / (alpha * m)
            vals = [b] * m + [Fraction(1, 1)] * (K - m)
            got = e_bh(vals, alpha)
            assert got == set(range(m)), (K, m, b, got)
            lower = b - Fraction(1, 1000)
            vals2 = [lower] * m + [Fraction(1, 1)] * (K - m)
            assert e_bh(vals2, alpha) == set(), (K, m, lower)


def pathwise_check():
    K, m = 8, 3
    alpha = Fraction(1, 10)
    b = Fraction(K, 1) / (alpha * m)  # 80/3
    paths = [
        [Fraction(1), Fraction(5), Fraction(30), Fraction(20)],
        [Fraction(1), Fraction(27), Fraction(5)],
        [Fraction(1), Fraction(2), Fraction(3), Fraction(40)],
    ]
    taus = []
    for path in paths:
        tau = next(i for i, v in enumerate(path) if v >= b)
        taus.append(tau)
    assert taus == [2, 1, 3]
    parked = [paths[i][taus[i]] for i in range(m)] + [Fraction(1)] * (K - m)
    assert e_bh(parked, alpha) == set(range(m))

    best = None
    best_tuple = None
    for counts in product(*[range(len(p)) for p in paths]):
        vals = [paths[i][counts[i]] for i in range(m)] + [Fraction(1)] * (K - m)
        if set(range(m)).issubset(e_bh(vals, alpha)):
            total = sum(counts)
            if best is None or total < best:
                best, best_tuple = total, counts
    assert best == sum(taus) == 6, (best, best_tuple, taus)
    assert best_tuple == tuple(taus), (best_tuple, taus)


def rank_argument_check():
    alpha = Fraction(1, 7)
    for K in range(2, 10):
        for m in range(1, K + 1):
            for r in range(m + 1, K + 1):
                assert Fraction(K, 1) / (alpha * r) > 1


if __name__ == '__main__':
    threshold_grid_check()
    pathwise_check()
    rank_argument_check()
    print('VERIFY_OK')
