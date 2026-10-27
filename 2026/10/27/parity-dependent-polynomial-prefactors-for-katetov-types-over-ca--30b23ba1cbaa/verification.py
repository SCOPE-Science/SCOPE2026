#!/usr/bin/env python3
"""Independent finite checks for a capped-geodesic Katetov-count asymptotic theorem.

Only Python's standard library is required. Finite checks are corroboration,
not a replacement for the general proof.
"""
from collections import defaultdict
from itertools import product
from math import cos, pi, sin


def direct_count(D, n):
    count = 0
    for f in product(range(1, D + 1), repeat=n):
        if any(abs(f[i] - f[i + 1]) > 1 for i in range(n - 1)):
            continue
        if all(f[i] + f[j] >= min(j - i, D)
               for i in range(n) for j in range(i + 1, n)):
            count += 1
    return count


def transfer_count(D, N, lower=1):
    """Exact state DP retaining D most recent labels and the older minimum."""
    states = {((), D): 1}
    totals = []
    for _ in range(N):
        following = defaultdict(int)
        for (recent, old_min), weight in states.items():
            far_min = min(old_min, recent[0]) if len(recent) == D else old_min
            for x in range(lower, D + 1):
                if recent and abs(recent[-1] - x) > 1:
                    continue
                if x + far_min < D:
                    continue
                if any(x + y < gap for gap, y in enumerate(reversed(recent), 1)
                       if gap < D):
                    continue
                following[((recent + (x,))[-D:], far_min)] += weight
        states = following
        totals.append(sum(states.values()))
    return totals


def matvec(v, M):
    return [sum(v[i] * M[i][j] for i in range(len(v))) for j in range(len(M))]


def odd_critical_count(D, N):
    """Closed convolution for sequences using only labels >= (D-1)/2."""
    assert D % 2 == 1
    r = D // 2
    high = list(range(r + 1, D + 1))
    all_labels = list(range(r, D + 1))
    A = [[int(abs(i - j) <= 1) for j in high] for i in high]
    B = [[int(abs(i - j) <= 1) for j in all_labels] for i in all_labels]
    high_sum = []
    end = [1] * len(high)
    a = [1]
    for _ in range(N):
        high_sum.append(sum(end))
        a.append(end[0])
        end = matvec(end, A)
    q = []
    walk = [1] + [0] * (len(all_labels) - 1)
    for _ in range(D):
        q.append(walk[0])
        walk = matvec(walk, B)
    result = []
    for n in range(1, N + 1):
        value = high_sum[n - 1]
        for L in range(1, min(D, n) + 1):
            value += q[L - 1] * sum(a[k] * a[n - L - k] for k in range(n - L + 1))
        result.append(value)
    return result, q


def asymptotic_constants(D):
    m = D // 2 + 1
    lam = 1 + 2 * cos(pi / (m + 1))
    v = [sin(j * pi / (m + 1)) for j in range(1, m + 1)]
    den = sum(x * x for x in v)
    if D % 2 == 0:
        return lam, sum(v) ** 2 / (lam * den)
    _, q = odd_critical_count(D, D)
    scalar = sum(v) ** 2 * v[0] ** 2 / den ** 2
    return lam, scalar * sum(q[L - 1] / lam ** (L + 2) for L in range(1, D + 1))


def run_checks():
    direct_cases = 0
    for D in range(2, 8):
        transfer = transfer_count(D, 6)
        for n in range(1, 7):
            assert direct_count(D, n) == transfer[n - 1], (D, n)
            direct_cases += 1
    for D in (3, 5, 7):
        left = transfer_count(D, 14, lower=D // 2)
        right, _ = odd_critical_count(D, 14)
        assert left == right, (D, left, right)
    for n, v in enumerate(transfer_count(3, 24), 1):
        assert (v == (4 * n + 21) * 2 ** (n - 4)) if n >= 4 else v == (3, 7, 17)[n - 1]
    assert transfer_count(2, 30) == [2 ** n for n in range(1, 31)]
    lam3, c3 = asymptotic_constants(3)
    assert abs(lam3 - 2.0) < 1e-12 and abs(c3 - 0.25) < 1e-12
    lam4, c4 = asymptotic_constants(4)
    assert abs(lam4 - (1 + 2 ** .5)) < 1e-12
    assert abs(c4 - ((1 + 2 ** .5) / 2)) < 1e-12
    print('DIRECT_DP_MATCH:', direct_cases, 'cases (D=2..7, n=1..6)')
    print('ODD_CRITICAL_CONVOLUTION_MATCH: D=3,5,7; n=1..14')
    print('D3_EXACT_FORMULA_MATCH: n=1..24')
    for D in range(2, 8):
        lam, c = asymptotic_constants(D)
        print('D=%d lambda=%.12f leading=%.12f' % (D, lam, c))
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    run_checks()
