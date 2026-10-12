"""Reproducible checks for covariances of block-size counts in conditioned set partitions.
Only the Python standard library is required. Finite tests do not prove asymptotics.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, exp, factorial, isclose


def stirling(nmax):
    s = [[0] * (nmax + 1) for _ in range(nmax + 1)]
    s[0][0] = 1
    for n in range(1, nmax + 1):
        for k in range(1, n + 1):
            s[n][k] = k * s[n - 1][k] + s[n - 1][k - 1]
    return s


def sval(s, n, k):
    return s[n][k] if 0 <= k <= n else 0


def moments(n, k, j, s):
    """Exact rational first and cross moments, j >= 2."""
    den = sval(s, n, k)
    e1 = Fraction(n * sval(s, n - 1, k - 1), den)
    ej = Fraction(comb(n, j) * sval(s, n - j, k - 1), den)
    cross = Fraction(n * comb(n - 1, j) * sval(s, n - 1 - j, k - 2), den)
    return e1, ej, cross, cross - e1 * ej


def enumerate_partitions(n):
    """All restricted growth strings, with exactly one representative per partition."""
    if n == 0:
        yield ()
        return
    def go(word, maxlabel):
        if len(word) == n:
            yield tuple(word)
        else:
            for b in range(maxlabel + 2):
                word.append(b)
                yield from go(word, max(maxlabel, b))
                word.pop()
    yield from go([0], 0)


def alpha_of_x(x):
    return -__import__('math').expm1(-x) / x


def x_for_alpha(alpha):
    lo, hi = 0., max(2., 2. / alpha)
    for _ in range(110):
        mid = (lo + hi) / 2
        if alpha_of_x(mid) > alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def h(x, j):
    return x*x - j*x - j*__import__('math').expm1(-x)


def root_of_h(j):
    lo, hi = 1e-5, float(j)
    assert h(lo, j) < 0 and h(hi, j) > 0
    for _ in range(110):
        mid = (lo + hi) / 2
        if h(mid, j) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def c_limit(alpha, j):
    x = x_for_alpha(alpha)
    exm1 = __import__('math').expm1(x)
    mu = x * exp(x) / exm1
    var = mu * (1 + x - mu)
    p1 = x / exm1
    pj = x**j / (factorial(j) * exm1)
    return -p1 * pj * (j + mu * (x - j)) / var


def check():
    checks = 0
    s = stirling(360)
    for n in range(3, 9):
        aggregated = defaultdict(list)
        for part in enumerate_partitions(n):
            block_sizes = [0] * (max(part) + 1)
            for v in part:
                block_sizes[v] += 1
            profile = {r: block_sizes.count(r) for r in range(1, n + 1)}
            aggregated[len(block_sizes)].append(profile)
        for k, profiles in aggregated.items():
            assert len(profiles) == s[n][k]
            for j in range(2, n):
                e1, ej, ecross, cov = moments(n, k, j, s)
                m1 = Fraction(sum(p[1] for p in profiles), len(profiles))
                mj = Fraction(sum(p[j] for p in profiles), len(profiles))
                mcross = Fraction(sum(p[1]*p[j] for p in profiles), len(profiles))
                assert (e1, ej, ecross, cov) == (m1, mj, mcross, mcross-m1*mj)
                checks += 1
    for n in (80, 160, 320):
        for alpha in (0.4, 0.6):
            k = int(n * alpha)
            for j in (2, 3, 4, 5):
                actual = float(moments(n, k, j, s)[-1] / k)
                target = c_limit(alpha, j)
                # Saddle-point errors decay at rate 1/k for these fixed parameters.
                assert abs(actual-target) < 0.014, (n, alpha, j, actual, target)
                checks += 1
    assert c_limit(0.4, 3) < 0 < c_limit(0.6, 3)
    assert c_limit(0.4, 2) < 0 and c_limit(0.6, 2) < 0
    checks += 4
    previous = 1.
    for j in range(3, 30):
        x = root_of_h(j)
        alpha = alpha_of_x(x)
        assert isclose(h(x, j), 0, abs_tol=1e-9)
        assert alpha < previous
        assert h(x / 2, j) < 0 and h(1.05 * j, j) > 0
        previous = alpha
        checks += 4
    x3 = root_of_h(3)
    assert abs(alpha_of_x(x3) - 0.5464068225505325) < 1e-11
    checks += 1
    print('PASS:', checks, 'exact, finite asymptotic, and threshold checks')


if __name__ == '__main__':
    check()
