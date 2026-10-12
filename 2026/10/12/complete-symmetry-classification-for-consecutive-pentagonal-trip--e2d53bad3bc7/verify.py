"""Exact checks for symmetry of three consecutive pentagonal generators.

The infinite exclusion is proved by inequalities and congruences in RESULT.md;
this checker independently tests the bounded remaining range via Apery sets.
Uses Python 3 and the standard library only.
"""
from math import gcd
from heapq import heappush, heappop

EXCEPTIONS = {2, 3, 5, 40}


def pentagonal(n):
    assert n >= 1
    return n * (3 * n - 1) // 2


def apery_frobenius_genus(a, b, c):
    assert gcd(gcd(a, b), c) == 1
    # Dijkstra computes minimal members in every residue class modulo a.
    distances = [None] * a
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        w, r = heappop(queue)
        if w != distances[r]:
            continue
        for step in (b, c):
            t = (r + step) % a
            nw = w + step
            if distances[t] is None or nw < distances[t]:
                distances[t] = nw
                heappush(queue, (nw, t))
    assert all(v is not None for v in distances)
    f = max(distances) - a
    double_g_numerator = 2 * sum(distances) - a * (a - 1)
    assert double_g_numerator % (2 * a) == 0
    g = double_g_numerator // (2 * a)
    return f, g


def two_coin_solution(target, x, y):
    for u in range(target // x + 1):
        rest = target - u * x
        if rest % y == 0:
            return (u, rest // y)
    return None


def gluing_criterion(n):
    vals = [pentagonal(n + j) for j in range(3)]
    for k in range(3):
        i, j = [z for z in range(3) if z != k]
        if two_coin_solution(vals[k], vals[i], vals[j]) is not None:
            return True  # Two minimal generators suffice.
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        d = gcd(vals[i], vals[j])
        if d > 1 and two_coin_solution(vals[k], vals[i] // d,
                                       vals[j] // d) is not None:
            return True
    return False


def verify():
    assert (3 * 11 * 11 - 7 * 11 - 2) > 0  # d=5 high-sum cutoff at 11
    assert (3 * 11 * 11 - 19 * 11 - 30) > 0  # d=5 low-sum cutoff
    assert (3 * 15 * 15 - 43 * 15 - 14) > 0  # d=7 high-sum cutoff
    assert (3 * 15 * 15 - 31 * 15 - 46) > 0  # d=7 low-sum cutoff
    assert (3 * 71 * 71 - 211 * 71 - 70) > 0  # d=35 high-sum cutoff
    assert (3 * 71 * 71 - 199 * 71 - 270) > 0  # d=35 low-sum cutoff
    # Each polynomial is increasing after the indicated cutoff.
    for n in range(2, 142):
        a, b, c = (pentagonal(n + j) for j in range(3))
        assert gcd(gcd(a, b), c) == 1
        assert gcd(a, b) == (2 if n % 4 == 3 else 1)
        assert gcd(b, c) == (2 if n % 4 == 2 else 1)
        expected = (5 if n % 5 == 0 else 1) * (7 if n % 7 == 5 else 1)
        assert gcd(a, c) == expected
        f, g = apery_frobenius_genus(a, b, c)
        symmetric = 2 * g == f + 1
        assert symmetric == gluing_criterion(n)
        assert symmetric == (n in EXCEPTIONS)
    for n, expected_f, expected_g in (
        (2, 43, 22), (3, 133, 67), (5, 1699, 850), (40, 258529, 129265)
    ):
        vals = [pentagonal(n + j) for j in range(3)]
        assert apery_frobenius_genus(*vals) == (expected_f, expected_g)
    assert two_coin_solution(2501, 68, 75) == (7, 27)
    assert two_coin_solution(35, 6, 11) == (4, 1)
    assert two_coin_solution(117, 35, 46) is None
    assert two_coin_solution(176, 29, 42) is None
    assert two_coin_solution(247, 30, 41) is None
    print('EXACT_CERTIFICATE_OK indices=2,3,5,40 apery_checked=2..141 '
          'high_cutoffs=11,15,71 max_F=258529')


if __name__ == '__main__':
    verify()
