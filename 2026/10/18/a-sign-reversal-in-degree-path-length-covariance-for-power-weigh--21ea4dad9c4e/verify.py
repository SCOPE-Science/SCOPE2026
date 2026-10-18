"""Independent finite-size checks for label-weighted recursive-tree covariance."""
from fractions import Fraction
from itertools import product
from math import pi, fsum


def weights(alpha, n):
    return [None] + [Fraction(j ** alpha) if alpha >= 0 else Fraction(1, j ** (-alpha)) for j in range(1, n + 1)]


def formula(alpha, n, i):
    w = weights(alpha, n)
    W = [Fraction(0)] * (n + 1)
    for j in range(1, n + 1):
        W[j] = W[j - 1] + w[j]
    p = [Fraction(0)] + [w[j] / W[j] for j in range(1, n + 1)]
    return w[i] * sum((p[j] + (1 - j * p[j]) / n) * (1 - sum(p[k] for k in range(i, j))) / W[j - 1] for j in range(i + 1, n + 1))


def exhaustive(alpha, n, i):
    w = weights(alpha, n)
    W = [Fraction(0)] * (n + 1)
    for j in range(1, n + 1):
        W[j] = W[j - 1] + w[j]
    et = er = etr = Fraction(0)
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        depths = [0] * (n + 1)
        mass = Fraction(1)
        degree = 0
        for j, k in enumerate(parents, 2):
            depths[j] = depths[k] + 1
            degree += (k == i)
            mass *= w[k] / W[j - 1]
        length = sum(depths)
        et += mass * length
        er += mass * degree
        etr += mass * length * degree
    return (etr - et * er) / n


def check():
    count = 0
    for alpha in [-2, -1, 0, 1, 2]:
        for n in range(3, 8):
            for i in range(1, n):
                assert exhaustive(alpha, n, i) == formula(alpha, n, i), (alpha, n, i)
                count += 1
    def c1(i):
        return 4 * i * (pi * pi / 6 - fsum(1 / (k * k) for k in range(1, i + 1))) + 2 / (i + 1) - 4
    for i in range(1, 100):
        assert c1(i) < 0
        count += 1
    for i in [30, 100, 300, 1000]:
        assert abs(i * i * c1(i) + 4 / 3) < 2.2 / i
        count += 1
    assert abs(c1(1) - (2 * pi * pi / 3 - 7)) < 1e-12
    count += 1
    assert count == 204
    print(f"all {count} deterministic checks passed")

if __name__ == "__main__":
    check()
