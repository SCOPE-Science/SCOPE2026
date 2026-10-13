"""Exhaustive checks of the global defensive-alliance windmill formulas.

Runs with Python 3 and its standard library. Finite tests do not prove the
all-orders theorem, whose proof is combinatorial.
"""
import itertools
from math import comb


def product_polynomial(factors):
    ans = [1]
    for factor in factors:
        nxt = [0] * (len(ans) + len(factor) - 1)
        for i, a in enumerate(ans):
            for j, b in enumerate(factor):
                nxt[i + j] += a * b
        ans = nxt
    return ans


def formula(sizes):
    total = sum(sizes)
    lower = total // 2
    with_center = []
    without_center = []
    for m in sizes:
        p = [0] * (m + 1)
        q = [0] * (m + 1)
        p[0] = 1
        for j in range(m // 2, m + 1):
            p[j] = comb(m, j)
        for j in range(m // 2 + 1, m + 1):
            q[j] = comb(m, j)
        with_center.append(p)
        without_center.append(q)
    p = product_polynomial(with_center)
    q = product_polynomial(without_center)
    a = [0] * (total + 2)
    for j in range(lower, total + 1):
        a[j + 1] += p[j]
    for j, x in enumerate(q):
        a[j] += x
    odd_two = len(sizes) == 2 and all(m % 2 for m in sizes)
    min_count = p[lower] + (int(odd_two) *
                            (comb(sizes[0], (sizes[0] + 1) // 2) *
                             comb(sizes[1], (sizes[1] + 1) // 2)))
    return a, lower + 1, min_count


def check_one(sizes):
    order = 1 + sum(sizes)
    adj = [0] * order
    blade_ranges = []
    base = 1
    for m in sizes:
        vertices = range(base, base + m)
        blade_ranges.append(vertices)
        for i in vertices:
            adj[0] |= 1 << i
            adj[i] |= 1
            for j in vertices:
                if i != j:
                    adj[i] |= 1 << j
        base += m
    actual = [0] * (order + 1)
    membership_checks = 0
    for mask in range(1 << order):
        dominated = all(mask & ((1 << v) | adj[v]) for v in range(order))
        defended = all(
            (mask & ((1 << v) | adj[v])).bit_count() >=
            (adj[v] & ~mask).bit_count()
            for v in range(order) if mask & (1 << v)
        )
        is_alliance = bool(mask) and dominated and defended
        center = bool(mask & 1)
        selected = [sum(bool(mask & (1 << v)) for v in blade)
                    for blade in blade_ranges]
        if center:
            predicted = (sum(selected) >= sum(sizes) // 2 and
                         all(s == 0 or s >= m // 2
                             for s, m in zip(selected, sizes)))
        else:
            predicted = all(s >= m // 2 + 1
                            for s, m in zip(selected, sizes))
        if is_alliance != predicted:
            raise AssertionError((sizes, mask, is_alliance, predicted))
        membership_checks += 1
        if is_alliance:
            actual[mask.bit_count()] += 1
    coeffs, minimum, minimum_count = formula(sizes)
    assert actual == coeffs, (sizes, actual, coeffs)
    assert next(i for i, c in enumerate(actual) if c) == minimum
    assert actual[minimum] == minimum_count, (sizes, actual, minimum_count)
    return membership_checks, sum(actual), len(actual)


def main():
    tuples = subsets = valid = coeffs = 0
    for total in range(4, 13):
        for blades in range(2, total // 2 + 1):
            for sizes in itertools.combinations_with_replacement(range(2, total), blades):
                if sum(sizes) != total:
                    continue
                examined, accepted, ncoeffs = check_one(sizes)
                tuples += 1
                subsets += examined
                valid += accepted
                coeffs += ncoeffs
    print('VERIFY_OK', 'size_vectors=' + str(tuples),
          'membership_checks=' + str(subsets),
          'valid_sets=' + str(valid),
          'coefficient_checks=' + str(coeffs),
          'max_vertices=13')


if __name__ == '__main__':
    main()
