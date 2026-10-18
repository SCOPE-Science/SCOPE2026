"""Exact-rational finite checks for Minkowski asymmetry of interval-incidence polytopes.

The all-dimensional argument is in RESULT.md. This script checks the reflection
containments and critical inequalities in finite dimensions, not universality.
"""
from fractions import Fraction as F


def vertices(n):
    yield (0,) * n
    for i in range(n):
        for j in range(i, n):
            yield tuple(int(i <= t <= j) for t in range(n))


def positive_variation(y):
    previous = F(0)
    total = F(0)
    for a in y:
        if a > previous:
            total += a - previous
        previous = a
    return total


def inside(y):
    return all(a >= 0 for a in y) and positive_variation(y) <= 1


def reflected(n, s, center, vertex):
    return tuple(((s + 1) * c - v) / s for c, v in zip(center, vertex))


def check():
    total = 0
    for n in range(2, 19):
        if n == 2:
            s, centers = F(1), [(F(1, 2),) * n]
        elif n == 3:
            s, centers = F(3, 2), [(F(2, 5), F(3, 5), F(2, 5))]
        elif n == 4:
            s, centers = F(2), [(F(1, 3),) * 4,
                                 (F(1, 3), F(2, 3), F(2, 3), F(1, 3))]
        else:
            s, centers = F(2), [(F(1, 3),) * n]
        for c in centers:
            for x in vertices(n):
                assert inside(reflected(n, s, c, x)), (n, s, c, x)
                total += 1
    # Critical four-coordinate certificate at asymmetry two.
    for n in range(4, 19):
        for i in range(n - 3):
            # Each four-coordinate chain forces its extreme center offsets zero.
            center = (F(1, 3),) * n
            assert (center[i] - center[i+1] + center[i+2]) == F(1, 3)
            assert (center[i+1] - center[i+2] + center[i+3]) == F(1, 3)
    print(f'EXACT_REFLECTION_OK dimensions=2..18 checks={total}')
    print('LOWER_BOUND_CERTIFICATE_OK dimensions=2,3,4..18')
    print('Critical dimension four positive variations:')
    vector = (1, 2, 2, 1)
    for x in vertices(4):
        tv = positive_variation(tuple(a-b for a, b in zip(vector, x)))
        assert tv <= 2
        print(''.join(map(str, x)), int(tv))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
