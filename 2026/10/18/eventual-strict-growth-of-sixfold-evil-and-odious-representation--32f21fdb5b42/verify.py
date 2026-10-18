"""Exact finite checks accompanying the sixth-moment theorem.

Run: python verify.py
The finite comparisons corroborate, but do not prove, the infinite result.
"""
from math import comb

P = {0: 20, 1: -15, -1: -15,
     2: 6, -2: 6, 3: -1, -3: -1}
M = ((20, 12, 0), (-15, -16, -1), (6, 20, 6))


def matstep(v):
    return tuple(sum(row[i] * v[i] for i in range(3)) for row in M)


def thue_signs(count):
    return [1 if i.bit_count() % 2 == 0 else -1 for i in range(count)]


def convolution(a, b, upper):
    c = [0] * (upper + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:upper + 1 - i]):
                if y:
                    c[i + j] += x * y
    return c


def exact_moment(m):
    t = thue_signs(1 << m)
    cube = [1]
    for _ in range(3):
        cube = convolution(cube, t, len(cube) + len(t) - 2)
    return sum(x * x for x in cube)


def representation_counts(limit, sign):
    base = [int(x == sign) for x in thue_signs(limit + 1)]
    sums = [1] + [0] * limit
    for _ in range(6):
        sums = convolution(sums, base, limit)
    return sums


def run():
    v = (1, 0, 0)
    for m in range(8):
        if m:
            v = matstep(v)
        observed = exact_moment(m)
        assert observed == v[0], (m, observed, v[0])
    poly = lambda x: x**3 - 10*x*x - 96*x + 512
    assert [poly(x) for x in (-9,-8,4,5,14,15)] == [-163,128,32,-93,-48,197]
    limit = 200
    evil = representation_counts(limit, 1)
    odious = representation_counts(limit, -1)
    assert [n for n in range(1,limit+1) if evil[n] <= evil[n-1]] == [1,2,4,7,10,13,16,19,22,25,28,31,34,37]
    assert [n for n in range(1,limit+1) if odious[n] <= odious[n-1]] == [1,2,3,4,5]
    assert evil[0] == 1 and odious[0] == 0
    print('PASS: 8 exact sixth-moment comparisons, six spectral sign checks, two sixfold representation profiles through n=200')


if __name__ == '__main__':
    run()
