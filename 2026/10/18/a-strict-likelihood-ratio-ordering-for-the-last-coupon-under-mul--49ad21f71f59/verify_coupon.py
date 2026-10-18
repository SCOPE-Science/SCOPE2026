"""Independent exact-rational checks for last-type/finishing-time likelihood ratios.
Run with Python 3, standard library only. No external inputs.
"""
from fractions import Fraction as Q
from functools import reduce
from itertools import product
from math import factorial


def conv(a, b, degree):
    out = [Q(0)] * (degree + 1)
    for i, ai in enumerate(a[: degree + 1]):
        for j, bj in enumerate(b[: degree + 1 - i]):
            out[i + j] += ai * bj
    return out


def joint_formula(ps, h, n):
    """ps[0] may be zero/null probability; positive coupons are ps[1:]."""
    m = len(ps) - 1
    if n < m * h:
        return [Q(0)] * m
    degree = n - h
    null = [ps[0] ** r / factorial(r) for r in range(degree + 1)]
    f = [[Q(0) if r < h else p ** r / factorial(r)
          for r in range(degree + 1)] for p in ps[1:]]
    ret = []
    for i in range(m):
        coeffs = null[:]
        for j in range(m):
            if j != i:
                coeffs = conv(coeffs, f[j], degree)
        ret.append(ps[i + 1] ** h * factorial(n - 1)
                   * coeffs[degree] / factorial(h - 1))
    return ret


def joint_enumerate(ps, h, n):
    """Enumerate full strings; null is type zero, last must finish a quota."""
    m = len(ps) - 1
    ans = [Q(0)] * m
    for w in product(range(m + 1), repeat=n):
        i = w[-1]
        if i == 0:
            continue
        counts = [w[:-1].count(j) for j in range(1, m + 1)]
        if counts[i-1] != h-1 or any(counts[j] < h for j in range(m) if j != i-1):
            continue
        p = Q(1)
        for j in w:
            p *= ps[j]
        ans[i - 1] += p
    return ans


def check():
    cases = [
        (1, [Q(0), Q(1,6), Q(1,3), Q(1,2)], 10),
        (1, [Q(1,5), Q(1,10), Q(3,10), Q(2,5)], 10),
        (2, [Q(0), Q(1,4), Q(3,4)], 13),
        (2, [Q(1,5), Q(1,5), Q(3,5)], 13),
        (2, [Q(0), Q(1,6), Q(1,3), Q(1,2)], 12),
        (3, [Q(1,10), Q(3,10), Q(6,10)], 15),
    ]
    exhaustive = 0
    comparisons = 0
    for h, ps, limit in cases:
        assert sum(ps) == 1
        m = len(ps) - 1
        prev = None
        first = joint_formula(ps, h, m * h)
        assert len(set(first)) == 1 and first[0] > 0
        for n in range(m * h, limit + 1):
            cur = joint_formula(ps, h, n)
            if (m + 1) ** n <= 200000:
                assert cur == joint_enumerate(ps, h, n), (h, ps, n)
                exhaustive += 1
            if prev is not None:
                for i in range(m):
                    for j in range(m):
                        if ps[i + 1] < ps[j + 1]:
                            assert cur[i] * prev[j] > prev[i] * cur[j], (h, ps, n, i, j)
                            comparisons += 1
                        elif ps[i + 1] == ps[j + 1]:
                            assert cur[i] == cur[j]
            prev = cur
    print('PASS:', exhaustive, 'exhaustive word enumerations;', comparisons,
          'strict exact-rational consecutive-time odds comparisons')

if __name__ == '__main__':
    check()
