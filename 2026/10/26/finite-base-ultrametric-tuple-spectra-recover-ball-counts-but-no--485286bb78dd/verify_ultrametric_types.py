"""Exhaustive finite checks of ultrametric extension and tuple-type spectra.

Run: python3 verify_ultrametric_types.py
Only Python standard library is required. The exhaustive checks do not prove
claims for unbounded arity or distance alphabet; those use the accompanying proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    for blocks in partitions(n - 1):
        for i in range(len(blocks)):
            updated = list(blocks)
            updated[i] += (n - 1,)
            yield tuple(updated)
        yield blocks + ((n - 1,),)


def codes(n):
    out = []
    for blocks in partitions(n):
        p = [None] * n
        for i, block in enumerate(blocks):
            for x in block:
                p[x] = i
        out.append(tuple(p))
    return out


def coarsens(p, q):
    n = len(p)
    return all(p[i] != p[j] or q[i] == q[j]
               for i in range(n) for j in range(i + 1, n))


@lru_cache(None)
def ultrametrics(n, D):
    assert n >= 1 and D >= 1
    if D == 1:
        return (tuple(tuple(0 if i == j else 1 for j in range(n))
                      for i in range(n)),)
    pp = codes(n)
    result = []

    def rec(h, prev, levels):
        if h == D:
            M = tuple(tuple(0 if i == j else next(
                (level for level, p in enumerate(levels, 1)
                 if p[i] == p[j]), D)
                            for j in range(n)) for i in range(n))
            result.append(M)
            return
        for p in pp:
            if prev is None or coarsens(prev, p):
                rec(h + 1, p, levels + (p,))

    rec(1, None, ())
    assert len(result) == len(set(result))
    return tuple(result)


def ball_vector(A, D):
    n = len(A)
    return (n,) + tuple(
        len(set(tuple(i for i in range(n) if A[i][j] <= h)
                for j in range(n))) for h in range(1, D + 1))


def exp_egf(log, K):
    vals = [1] + [0] * K
    for k in range(1, K + 1):
        vals[k] = sum(comb(k - 1, j - 1) * log[j] * vals[k - j]
                      for j in range(1, k + 1))
    return vals


def predicted(A, D, K):
    b = ball_vector(A, D)
    U = [[0] * (K + 1) for _ in range(D + 1)]
    if K:
        U[0][1] = 1
    for h in range(1, D + 1):
        U[h] = exp_egf(U[h - 1], K)
        U[h][0] = 0
    inj = [0] + [sum(b[h] * U[h - 1][j]
                     for h in range(1, D + 1))
                 for j in range(1, K + 1)]
    full = [0] + [sum(b[h] * U[h][j]
                      for h in range(D + 1))
                  for j in range(1, K + 1)]
    return exp_egf(inj, K), exp_egf(full, K)


@lru_cache(None)
def extension_counts(A, D, K):
    n = len(A)
    values = []
    for k in range(K + 1):
        values.append(sum(all(M[i][j] == A[i][j]
                              for i in range(n) for j in range(n))
                          for M in ultrametrics(n + k, D)))
    return tuple(values)


def equality_patterns(n_base, K):
    # Values < n_base are named old parameters; >= n_base are
    # new blocks canonically labelled by their first occurrence.
    def rec(seq, new_count):
        if len(seq) == K:
            yield tuple(seq), new_count
            return
        for x in range(n_base + new_count + 1):
            yield from rec(seq + [x], new_count + (x == n_base + new_count))
    yield from rec([], 0)


def brute_all_types(A, D, K):
    m = len(A)
    return [sum(extension_counts(A, D, r)[r]
                for _, r in equality_patterns(m, k))
            for k in range(K + 1)]


def canonical(A):
    n = len(A)
    return min(tuple(A[p[i]][p[j]] for i in range(n) for j in range(n))
               for p in permutations(range(n)))


def run():
    checks = 0
    for m, D, K in [(1, 2, 4), (1, 3, 4), (2, 2, 4), (2, 3, 3),
                     (3, 2, 3), (3, 3, 3), (4, 2, 3), (4, 3, 2)]:
        for A in ultrametrics(m, D):
            pred_inj, pred_all = predicted(A, D, K)
            assert pred_inj == list(extension_counts(A, D, K))
            assert pred_all == brute_all_types(A, D, K)
            checks += 1
    for D in (2, 3, 4):
        for m in (1, 2, 3):
            signatures = {}
            for A in ultrametrics(m, D):
                b = ball_vector(A, D)
                iso = canonical(A)
                assert b not in signatures or signatures[b] == iso
                signatures[b] = iso
    A31 = ((0, 1, 1, 2), (1, 0, 1, 2),
           (1, 1, 0, 2), (2, 2, 2, 0))
    A22 = ((0, 1, 2, 2), (1, 0, 2, 2),
           (2, 2, 0, 1), (2, 2, 1, 0))
    for D in (2, 3, 4):
        assert ball_vector(A31, D) == ball_vector(A22, D)
        assert canonical(A31) != canonical(A22)
        assert predicted(A31, D, 6) == predicted(A22, D, 6)
    print('EXHAUSTIVE_BASE_CONFIGURATIONS_PASS', checks)
    print('ALL_EQUALITY_AND_DISTINCT_TYPE_COEFFICIENTS_PASS')
    print('NO_PROFILE_COLLISION_UP_TO_THREE_PARAMETERS_PASS')
    print('FOUR_PARAMETER_NONISOMETRIC_COLLISION_PASS')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    run()
