"""Exact finite sanity checks for one-attacker stable-extension diversity."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial


def actual_polynomial(parent):
    n = len(parent)
    stable = []
    for mask in range(1 << n):
        if all(bool(mask & (1 << v)) ==
               (not bool(mask & (1 << parent[v])) if parent[v] >= 0 else True)
               for v in range(n)):
            stable.append(mask)
    return Counter((a ^ b).bit_count() for a in stable for b in stable)


def predicted_polynomial(parent):
    n = len(parent)
    root = list(range(n))
    def find(x):
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
    for v, p in enumerate(parent):
        if p >= 0:
            a, b = find(v), find(p)
            root[a] = b
    groups = {}
    for v in range(n):
        groups.setdefault(find(v), []).append(v)
    result = Counter({0: 1})
    for group in groups.values():
        v = group[0]
        seen = {}
        cyc = []
        while v >= 0 and v not in seen:
            seen[v] = len(seen)
            v = parent[v]
        if v >= 0:
            cyc = list(seen)[seen[v]:]
            if len(cyc) % 2:
                return Counter()
            s = len(group)
            updated = Counter()
            for k, ways in result.items():
                updated[k] += 2 * ways
                updated[k + s] += 2 * ways
            result = updated
    return result


def q_coefficients(max_n):
    T = [Fraction(0)] + [Fraction(n ** (n - 1), factorial(n))
                              for n in range(1, max_n + 1)]
    u = [sum((T[j] * T[n-j] for j in range(n+1)), Fraction(0))
         for n in range(max_n + 1)]
    q = [Fraction(1)]
    for n in range(1, max_n + 1):
        q.append(sum((u[j] * q[n-j] for j in range(1,n+1)), Fraction(0)))
    return q


def main():
    checks = 0
    for n in range(1, 6):
        histogram = Counter()
        for parent in product(range(-1, n), repeat=n):
            actual = actual_polynomial(parent)
            predicted = predicted_polynomial(parent)
            assert actual == predicted, (n, parent, actual, predicted)
            checks += 1
            if all(p >= 0 for p in parent):
                histogram.update(actual)
        q = q_coefficients(n)
        for k in range(n+1):
            expected = factorial(n) * q[k] * q[n-k]
            assert expected.denominator == 1
            assert histogram[k] == expected.numerator, (n,k,histogram[k],expected)
            checks += 1
        if n == 5:
            print('n=5 ordered-pair disagreement totals:',dict(sorted(histogram.items())))
    print('CHECKS',checks,'ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
