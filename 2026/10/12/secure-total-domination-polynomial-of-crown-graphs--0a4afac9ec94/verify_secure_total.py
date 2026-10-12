from itertools import combinations
from math import comb
from collections import Counter


def vertices(n):
    return [('A', i) for i in range(n)] + [('B', i) for i in range(n)]


def adjacent(u, v):
    return u[0] != v[0] and u[1] != v[1]


def total_dominating(n, S):
    S = set(S)
    return all(any(adjacent(u, v) for v in S) for u in vertices(n))


def secure_total(n, S):
    S = set(S)
    if not total_dominating(n, S):
        return False
    for u in vertices(n):
        if u in S:
            continue
        good = False
        for v in tuple(S):
            if adjacent(u, v):
                T = (S - {v}) | {u}
                if total_dominating(n, T):
                    good = True
                    break
        if not good:
            return False
    return True


def criterion(n, S):
    S = set(S)
    I = {i for side, i in S if side == 'A'}
    J = {i for side, i in S if side == 'B'}
    return (len(I) >= 2 and len(J) >= 2
            and (len(I) == n or len(J) >= 3)
            and (len(J) == n or len(I) >= 3))


def formula_distribution(n):
    out = Counter()
    for i in range(3, n + 1):
        for j in range(3, n + 1):
            out[i + j] += comb(n, i) * comb(n, j)
    out[n + 2] += 2 * comb(n, 2)
    return out


def expected_minimum(n):
    if n == 3:
        return 5, 6
    if n == 4:
        return 6, 28
    return 6, comb(n, 3) ** 2


def main():
    subset_checks = 0
    secure_sets = 0
    swap_checks = 0
    coefficient_checks = 0
    for n in range(3, 9):
        V = vertices(n)
        empirical = Counter()
        for mask in range(1 << (2 * n)):
            S = {V[k] for k in range(2 * n) if (mask >> k) & 1}
            a = secure_total(n, S)
            b = criterion(n, S)
            subset_checks += 1
            if a != b:
                raise AssertionError((n, S, a, b))
            if a:
                secure_sets += 1
                empirical[len(S)] += 1
                # count candidate outside-vertex/defender incidences for reporting only
                for u in V:
                    if u not in S:
                        swap_checks += sum(1 for v in S if adjacent(u, v))
        expected = formula_distribution(n)
        keys = set(empirical) | set(expected)
        for k in keys:
            coefficient_checks += 1
            if empirical[k] != expected[k]:
                raise AssertionError((n, k, empirical[k], expected[k]))
        m = min(empirical)
        if (m, empirical[m]) != expected_minimum(n):
            raise AssertionError(('minimum', n, m, empirical[m], expected_minimum(n)))
    print('VERIFY_OK n_range=3..8 subset_checks=%d secure_sets=%d swap_incidence_checks=%d coefficient_checks=%d max_order=16' %
          (subset_checks, secure_sets, swap_checks, coefficient_checks))


if __name__ == '__main__':
    main()
