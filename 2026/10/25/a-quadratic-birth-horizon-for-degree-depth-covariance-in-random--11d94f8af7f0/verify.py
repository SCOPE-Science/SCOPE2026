"""Exact finite checks for the degree--depth covariance law of a uniform recursive tree.

Run with Python 3: python verify.py
The unrestricted formula is proved separately; these are independent finite checks.
"""
from fractions import Fraction
from itertools import product


def formula(i, j):
    if i >= j:
        return Fraction(0)
    return Fraction(i - 1, i * i) - sum(
        (Fraction(1, s * s) for s in range(i + 1, j)), Fraction(0)
    )


def check():
    assertions = 0
    trees = 0
    for n in range(2, 10):
        count = 0
        sd = [0] * (n + 1)
        sh = [0] * (n + 1)
        sdh = [[0] * (n + 1) for _ in range(n + 1)]
        for parents in product(*(range(1, t) for t in range(2, n + 1))):
            depth = [0] * (n + 1)
            outdegree = [0] * (n + 1)
            for t, parent in enumerate(parents, start=2):
                depth[t] = depth[parent] + 1
                outdegree[parent] += 1
            count += 1
            for i in range(1, n + 1):
                sd[i] += outdegree[i]
                sh[i] += depth[i]
                for j in range(1, n + 1):
                    sdh[i][j] += outdegree[i] * depth[j]
        trees += count
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                observed = Fraction(sdh[i][j], count) - Fraction(
                    sd[i] * sh[j], count * count
                )
                assert observed == formula(i, j), (n, i, j, observed, formula(i, j))
                assertions += 1
        for i in range(1, n + 1):
            for j in range(i + 1, n):
                assert formula(i, j + 1) - formula(i, j) == -Fraction(1, j * j)
                assertions += 1
    for i in range(2, 31):
        j = i + 1
        value = formula(i, j)
        assert value > 0
        assertions += 1
        while value > 0:
            assert formula(i, j + 1) == value - Fraction(1, j * j)
            assertions += 1
            j += 1
            value = formula(i, j)
        assert formula(i, j - 1) > 0 and value <= 0
        assertions += 1
    print(f'VERIFY_OK {assertions} exact assertions; {trees} enumerated recursive trees')


if __name__ == '__main__':
    check()
