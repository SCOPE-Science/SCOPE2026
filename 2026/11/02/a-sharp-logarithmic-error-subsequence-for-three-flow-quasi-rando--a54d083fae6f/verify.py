"""Exact rational checks for three-flow quasi-random splitting sharpness.

Run with Python 3, standard library only. Finite checks supplement, but do not
replace, the symbolic proof of the stated infinite family.
"""
from fractions import Fraction
from itertools import permutations

ORDERS = tuple(permutations((1, 2, 3)))


def radical_inverse(n):
    assert isinstance(n, int) and n >= 0
    numerator, denominator = 0, 1
    while n:
        denominator *= 2
        numerator = 2 * numerator + (n & 1)
        n >>= 1
    return Fraction(numerator, denominator)


def order(n):
    return ORDERS[int(6 * radical_inverse(n))]


def f(x):
    p = ORDERS[int(6 * x)]
    return 1 if p.index(2) < p.index(1) else -1


def g(x):
    return -1 if x < Fraction(1, 3) or x >= Fraction(5, 6) else 1


def D(n):
    return sum(f(radical_inverse(j)) for j in range(1, n + 1))


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4))
             for j in range(4)] for i in range(4)]


def identity():
    return [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]


def flow(j, h):
    out = identity()
    out[j - 1][j] = h
    return out


def compose(n, t):
    h = t / n
    out = identity()
    for index in range(1, n + 1):
        for j in order(index):
            out = matmul(flow(j, h), out)
    return out


def check():
    assert [order(j) for j in range(1, 7)] == [
        (2, 3, 1), (1, 3, 2), (3, 1, 2),
        (1, 2, 3), (2, 3, 1), (2, 1, 3)
    ]
    checks = 0
    for j in range(10000):
        x = radical_inverse(j)
        block = sum(f(radical_inverse(4*j + i)) for i in range(4))
        assert block == f(x) + g(x)
        checks += 1
        assert g(radical_inverse(2*j)) + g(radical_inverse(2*j+1)) == 0
        checks += 1
    for j in range(1, 1500, 2):
        assert D(4*j + 1) == D(j) - 2
        checks += 1
    n = 3
    for k in range(1, 10):
        assert D(n) == 1 - 2*k
        checks += 1
        n = 4*n + 1
    for k, n in enumerate((3, 13, 53, 213, 853), start=1):
        t = Fraction(1)
        h = t/n
        actual = compose(n, t)
        assert actual[0][2] - t*t/2 == Fraction(1-2*k, 2)*h*h
        checks += 1
    n = 53
    t = Fraction(7, 5)
    actual = compose(n, t)
    assert actual[0][2] - t*t/2 == Fraction(-5, 2)*(t/n)**2
    checks += 1
    print(f"PASS: {checks} exact-rational checks including full 4x4 products")
    print("family:", [(k, (5*4**k-2)//6, 1-2*k) for k in range(1, 6)])


if __name__ == '__main__':
    check()
