"""Verify proposed total-perfect-Roman weight enumerator on crown graphs.

Uses the literal adjacency definition for exhaustive checks, and an
independent inclusion/exclusion algebraic coefficient calculation.
Run with Python 3.9 or newer; no third-party dependencies.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def multiply(left, right):
    out = Counter()
    for p, c in left.items():
        for q, d in right.items():
            out[p + q] += c * d
    return out


def factor_power(allow_zero, exponent):
    result = Counter({0: 1})
    factor = {1: 1, 0: 1} if allow_zero else {1: 1}
    for _ in range(exponent):
        result = multiply(result, factor)
    return result


def predicted(n):
    if n < 3:
        raise ValueError('Domain requires n >= 3')
    formal = Counter()
    for a in range(n + 1):
        for b in range(n + 1):
            for k in range(max(0, a + b - n), min(a, b) + 1):
                u, v, w = a - k, b - k, n - a - b + k
                choices = factorial(n) // (factorial(k) * factorial(u) *
                                          factorial(v) * factorial(w))
                term = Counter({2 * (a + b): choices})
                for exponent, permit_zero in ((v, b == 2), (u, a == 2),
                                               (w, b == 1), (w, a == 1)):
                    term = multiply(term, factor_power(permit_zero, exponent))
                formal.update(term)
    formal[n + 2] -= 2 * n
    for j in range(n):
        formal[4 + j] -= 2 * n * comb(n - 1, j)
    formal[4] += n
    if n == 3:
        formal[6] -= 2 * n
        formal[7] -= 2 * n
    assert all(value >= 0 for value in formal.values())
    return +formal


def observed(n):
    # A_i is vertex i, B_j vertex n+j; their edge exists exactly if i != j.
    neighbors = [tuple(n + j for j in range(n) if i != j)
                 for i in range(n)]
    neighbors += [tuple(i for i in range(n) if i != j)
                  for j in range(n)]
    counts = Counter()
    for f in product((0, 1, 2), repeat=2 * n):
        okay = True
        for v in range(2 * n):
            if f[v] == 0:
                if sum(f[w] == 2 for w in neighbors[v]) != 1:
                    okay = False
                    break
            elif not any(f[w] > 0 for w in neighbors[v]):
                okay = False
                break
        if okay:
            counts[sum(f)] += 1
    return counts


def main():
    examined = 0
    for n in range(3, 7):
        expected = predicted(n)
        actual = observed(n)
        examined += 3 ** (2 * n)
        assert actual == expected, (n, actual, expected)
        assert min(actual) == 6
        assert actual[6] == (31 if n == 3 else n*n*(n - 1))
        print('n=%d assignments=%d min_weight=%d minimum_count=%d total=%d coefficients=%s' %
              (n, 3 ** (2*n), min(actual), actual[6], sum(actual.values()),
               sorted(actual.items())))
    for n in range(7, 13):
        expected = predicted(n)
        assert min(expected) == 6
        assert expected[6] == n*n*(n-1)
        print('n=%d symbolic_degree=%d symbolic_min_count=%d symbolic_total=%d' %
              (n, max(expected), expected[6], sum(expected.values())))
    print('PASS: original adjacency definition matches exact polynomial for n=3..6;'
          ' coefficient identities checked algebraically for n=3..12;'
          ' independent exhaustive assignments=%d.' % examined)


if __name__ == '__main__':
    main()
