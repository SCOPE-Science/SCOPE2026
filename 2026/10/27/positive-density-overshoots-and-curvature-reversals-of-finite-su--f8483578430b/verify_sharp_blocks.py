"""Finite exact arithmetic checks of the sharpness family, not a proof."""
from fractions import Fraction as F


def check(d, r):
    probabilities = [(1 - r) * r**j for j in range(d - 1)] + [r**(d - 1)]
    assert sum(probabilities) == 1
    limit = 1 / sum(j*p for j, p in enumerate(probabilities, 1))
    assert limit == (1 - r) / (1 - r**d)
    u = [F(1)]
    for n in range(1, 8*d + 2):
        u.append(sum(probabilities[j - 1]*u[n - j] for j in range(1, min(n, d) + 1)))
    for n, value in enumerate(u):
        m, s = divmod(n, d)
        expected = limit * (1 - r**(d*(m + 1))) + (r**(d*m + 1) if s == 0 else 0)
        assert value == expected
        assert (value > limit) == (s == 0)
        assert (value < limit) == (s != 0)
    for n in range(1, len(u) - 1):
        h = u[n - 1]*u[n + 1] - u[n]**2
        assert (h < 0) == (n % d == 0)
    for n in range(1, len(u) - d):
        curvature = [u[k - 1]*u[k + 1] - u[k]**2 for k in range(n, n + d)]
        assert min(curvature) < 0 < max(curvature)


if __name__ == '__main__':
    for maximum_step in range(2, 10):
        for ratio in (F(1, 4), F(1, 2), F(4, 5)):
            check(maximum_step, ratio)
    print('PASS: 24 truncated-geometric exact rational examples')
