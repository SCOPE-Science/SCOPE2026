"""Reproduce exact finite identities for isolated chords and crossings.

This is a finite consistency check; the proof of the formulas for every n
is given in RESULT.md. Only Python's standard library is needed.
"""
from fractions import Fraction
from math import comb


def double_factorial(n):
    out = 1
    for k in range(1, n + 1):
        out *= 2 * k - 1
    return out


def diagrams(points):
    if not points:
        yield ()
        return
    first, *rest = points
    for j, other in enumerate(rest):
        remaining = rest[:j] + rest[j + 1:]
        for tail in diagrams(remaining):
            yield ((first, other),) + tail


def crosses(a, b):
    x, y = a
    u, v = b
    return x < u < y < v or u < x < v < y


def exact_cov(n):
    m = double_factorial(n)
    return -Fraction(n * sum(
        double_factorial(k) * double_factorial(n - 1 - k)
        * (n - 1 + k * (n - 1 - k))
        for k in range(n)
    ), 3 * m)


def exact_mean_isolates(n):
    m = double_factorial(n)
    return Fraction(n * sum(
        double_factorial(k) * double_factorial(n - 1 - k)
        for k in range(n)
    ), m)


def exact_simple_cov(n):
    return -Fraction(2 * n * (n - 1), 3 * (2 * n - 1))


def test_enumeration(n):
    tally_i = tally_s = tally_x = tally_ix = tally_sx = count = 0
    root_moment = [0] * n
    root_count = [0] * n
    for matching in diagrams(list(range(2 * n))):
        count += 1
        deg = [0] * n
        x = 0
        for a in range(n):
            for b in range(a):
                if crosses(matching[a], matching[b]):
                    x += 1
                    deg[a] += 1
                    deg[b] += 1
        i = sum(d == 0 for d in deg)
        s = sum(b - a == 1 or b - a == 2 * n - 1
                for a, b in matching)
        tally_i += i
        tally_s += s
        tally_x += x
        tally_ix += i * x
        tally_sx += s * x
        a, b = matching[0]  # the matching generator always pairs endpoint 0 first
        assert a == 0
        if deg[0] == 0:
            assert b % 2 == 1
            k = (b - 1) // 2
            root_count[k] += 1
            root_moment[k] += x
    assert count == double_factorial(n)
    assert Fraction(tally_i, count) == exact_mean_isolates(n)
    assert Fraction(tally_x, count) == Fraction(n * (n - 1), 6)
    assert Fraction(tally_s, count) == Fraction(2 * n, 2 * n - 1)
    cov_ix = Fraction(tally_ix, count) - Fraction(tally_i * tally_x, count ** 2)
    cov_sx = Fraction(tally_sx, count) - Fraction(tally_s * tally_x, count ** 2)
    assert cov_ix == exact_cov(n)
    assert cov_sx == exact_simple_cov(n)
    assert cov_ix - cov_sx == exact_cov(n) - exact_simple_cov(n)
    for k in range(n):
        r = n - 1 - k
        assert root_count[k] == double_factorial(k) * double_factorial(r)
        assert Fraction(root_moment[k], root_count[k]) == Fraction(
            comb(k, 2) + comb(r, 2), 3
        )
    return count, len(root_count)


def test_all_n():
    comparisons = 0
    for n in range(2, 501):
        assert exact_cov(n) < 0
        assert exact_cov(n) <= exact_simple_cov(n)
        if n >= 3:
            assert exact_cov(n) < exact_simple_cov(n)
        if n >= 5:
            # The leading omitted k=1 and k=n-2 arcs supply this term.
            correction = -Fraction(2 * n, 3 * (2 * n - 1))
            assert exact_cov(n) - exact_simple_cov(n) <= correction
        comparisons += 1
    return comparisons


if __name__ == "__main__":
    diagrams_checked = 0
    conditional_checked = 0
    for size in range(2, 8):
        diagrams_n, cases_n = test_enumeration(size)
        diagrams_checked += diagrams_n
        conditional_checked += cases_n
        print(f"n={size} diagrams={diagrams_n} mean_isolated={exact_mean_isolates(size)} covariance={exact_cov(size)}")
    n_large = test_all_n()
    print(f"PASS diagrams={diagrams_checked} conditional_arc_cases={conditional_checked} all_n_checks={n_large}")
