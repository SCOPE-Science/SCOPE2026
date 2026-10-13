"""Standalone exact finite checks of connected KD45 bounded-map and rank-spectrum formulas.
No network access, independent enumeration of all function tables over small frames.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def forest(n, r):
    assert r >= 1 and n >= 0
    return 1 if n == 0 else r * (r + n) ** (n - 1)


def expected(c, s):
    E, I, A = [], [], []
    for j in range(s + 1):
        onto = sum((-1) ** (j - i) * comb(j, i) * (c + i) ** s for i in range(j + 1))
        E.append(factorial(c) * comb(s, j) * onto)
        I.append(comb(s, j) * (c + j) ** (s - j))
        A.append(factorial(c) * comb(s, j) * factorial(j) * forest(s - j, c + j))
    return E, I, A


def successors(c, s, x):
    return set(range(c))


def is_bounded(f, c, s, d, t):
    return all({f[y] for y in successors(c, s, x)} == successors(d, t, f[x]) for x in range(c + s))


def is_idempotent(f):
    return all(f[f[x]] == f[x] for x in range(len(f)))


def eventual(f):
    pts = set(range(len(f)))
    for _ in range(len(f) + 2):
        next_pts = {f[x] for x in pts}
        if next_pts == pts:
            return next_pts
        pts = next_pts
    raise AssertionError('stabilization bound')


def stirling2(n, k):
    if k > n or k < 0:
        return 0
    vals = [0] * (k + 1)
    vals[0] = 1
    for v in range(1, n + 1):
        new = [0] * (k + 1)
        for j in range(1, min(v, k) + 1):
            new[j] = j * vals[j] + vals[j - 1]
        vals = new
    return vals[k]


def direct_algebra_condition(f, c, s, d, t):
    # Modal algebra homomorphism is inverse image.  Exhaustively check Diamond on each subset.
    codomain = range(d + t)
    domain = range(c + s)
    for mask in range(1 << (d + t)):
        W = {x for x in codomain if mask & (1 << x)}
        dia_W = {x for x in codomain if successors(d, t, x) & W}
        lhs = {x for x in domain if f[x] in dia_W}
        pre = {x for x in domain if f[x] in W}
        rhs = {x for x in domain if successors(c, s, x) & pre}
        if lhs != rhs:
            return False
    return True


def run():
    function_tables = bounded_maps = direct_checks = comparisons = 0
    for c in range(1, 7):
        for s in range(7 - c):
            n = c + s
            if n > 6:
                continue
            e_count, i_count, a_count = Counter(), Counter(), Counter()
            for f in product(range(n), repeat=n):
                function_tables += 1
                if not is_bounded(f, c, s, c, s):
                    continue
                bounded_maps += 1
                j = len(set(f)) - c
                e_count[j] += 1
                a_count[len(eventual(f)) - c] += 1
                if is_idempotent(f):
                    i_count[j] += 1
                if n <= 4:
                    assert direct_algebra_condition(f, c, s, c, s)
                    direct_checks += 1
            E, I, A = expected(c, s)
            assert [e_count[j] for j in range(s + 1)] == E, (c, s, e_count, E)
            assert [i_count[j] for j in range(s + 1)] == I, (c, s, i_count, I)
            assert [a_count[j] for j in range(s + 1)] == A, (c, s, a_count, A)
            assert sum(E) == factorial(c) * (c + s) ** s
            assert sum(A) == sum(E)
            comparisons += 5

    # Independent source-target exhaustive hom-set checking, including zero satellites.
    hom_pairs = 0
    for c in range(1, 5):
        for s in range(5 - c):
            for d in range(1, 5):
                for t in range(5 - d):
                    n, m = c + s, d + t
                    n_maps = 0
                    for f in product(range(m), repeat=n):
                        okay = is_bounded(f, c, s, d, t)
                        if n <= 3 and m <= 3:
                            assert okay == direct_algebra_condition(f, c, s, d, t)
                            direct_checks += 1
                        n_maps += okay
                    expectation = factorial(d) * stirling2(c, d) * (d + t) ** s
                    assert n_maps == expectation, ((c,s),(d,t),n_maps,expectation)
                    comparisons += 1
                    hom_pairs += 1
    print('VERIFY_OK',
          'function_tables',function_tables,
          'bounded_maps',bounded_maps,
          'hom_pairs',hom_pairs,
          'modal_algebra_checks',direct_checks,
          'exact_comparisons',comparisons)
    print('example_c2_s3',expected(2, 3))


if __name__ == '__main__':
    run()
