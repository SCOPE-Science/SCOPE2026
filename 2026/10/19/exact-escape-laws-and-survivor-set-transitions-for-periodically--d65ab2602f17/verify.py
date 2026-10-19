"""Exact rational checks for a periodically switched pair of endpoint holes.

Usage: python verify.py
Independent interval-backward construction; the proof is analytical.
"""
from fractions import Fraction as F


def intersection(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        left = max(a[i][0], b[j][0])
        right = min(a[i][1], b[j][1])
        if left < right:
            out.append((left, right))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return out


def surviving_measure(h, n):
    """Build the exact union of inverse cylinder intervals, without matrices."""
    sections = [(F(0), F(1))]
    for j in range(n - 1, -1, -1):
        sections = [(a / 2, b / 2) for a, b in sections] + [
            ((1 + a) / 2, (1 + b) / 2) for a, b in sections
        ]
        safe = [(h, F(1))] if j % 2 == 0 else [(F(0), 1 - h)]
        sections = intersection(sections, safe)
    return sum((b - a for a, b in sections), F(0))


def formula(h, n):
    if n == 0:
        return F(1)
    if n == 1:
        return 1 - h
    if h < F(1, 3):
        return (4 * h + (2 - 6 * h) * n) / (2 ** n)
    if h <= F(1, 2):
        return 2 * (1 - h) / (2 ** n)
    if h < F(2, 3):
        return (4 - 6 * h) / (2 ** n)
    return F(0)


def double(x):
    return (2 * x) % 1


def survives_prefix(x, h, n):
    for j in range(n):
        if (x <= h if j % 2 == 0 else x >= 1 - h):
            return False
        x = double(x)
    return True


def run():
    checks = 0
    hs = sorted(set([F(i, 120) for i in range(30, 121)] + [
        F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(1),
        F(10, 33), F(21, 41), F(17, 27),
    ]))
    for h in hs:
        for n in range(0, 32):
            actual = surviving_measure(h, n)
            predicted = formula(h, n)
            assert actual == predicted, (h, n, actual, predicted)
            checks += 1

    points = [F(2, 3) + F((-1) ** (m + 1), 3 * 2 ** m)
              for m in range(0, 25)]
    for h in (F(1, 4), F(7, 24), F(19, 60)):
        assert h < F(1, 3)
        for x in points + [F(2, 3)]:
            assert survives_prefix(x, h, 100), (h, x)
            checks += 1
    for h in (F(1, 3), F(3, 5), F(79, 120)):
        assert survives_prefix(F(2, 3), h, 100)
        assert all(not survives_prefix(x, h, 100) for x in points)
        checks += len(points) + 1
    assert not survives_prefix(F(2, 3), F(2, 3), 1)
    checks += 1
    print('VERIFY_OK', checks, 'exact rational comparisons and orbit checks')


if __name__ == '__main__':
    run()
