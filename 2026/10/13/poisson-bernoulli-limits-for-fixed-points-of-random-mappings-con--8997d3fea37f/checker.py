"""Independent finite verification of fixed-point factorial moments under prescribed kernel blocks.

Usage: python checker.py
All counts use integer arithmetic or exact Fraction objects; no external dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial


def partitions(n):
    """Enumerate all set partitions in restricted-growth order."""
    blocks = [[0]]

    def visit(i):
        if i == n:
            yield [tuple(b) for b in blocks]
            return
        for b in blocks:
            b.append(i)
            yield from visit(i + 1)
            b.pop()
        blocks.append([i])
        yield from visit(i + 1)
        blocks.pop()

    yield from visit(1)


def factorial_moments_from_sizes(sizes):
    """Compute n! injection enumeration formula using elementary symmetric coefficients."""
    n = sum(sizes)
    e = [1] + [0] * len(sizes)
    for s in sizes:
        for r in range(len(sizes), 0, -1):
            e[r] += s * e[r - 1]
    return [Fraction(factorial(r) * e[r], factorial(n) // factorial(n-r))
            for r in range(len(sizes) + 1)]


def exact_moments_from_enumeration(blocks, n):
    """Independently count all injective block-to-label assignments."""
    counts = Counter()
    for output_labels in permutations(range(n), len(blocks)):
        f = sum(int(label in blocks[j]) for j, label in enumerate(output_labels))
        counts[f] += 1
    total = sum(counts.values())
    moments = []
    for r in range(len(blocks) + 1):
        moment_numer = sum(freq * (factorial(j) // factorial(j-r))
                           for j, freq in counts.items() if j >= r)
        moments.append(Fraction(moment_numer, total))
    return moments


def limited_factorial_moments(sizes, order):
    """Exact low-order factorial moments, avoiding large full polynomials."""
    n = sum(sizes)
    e = [0] * (order + 1)
    e[0] = 1
    for s in sizes:
        for r in range(order, 0, -1):
            e[r] += s * e[r - 1]
    return [Fraction(factorial(r) * e[r], factorial(n) // factorial(n-r))
            for r in range(order + 1)]


def poisson_bernoulli_factorial_moments(a, delta, order):
    """Reference law's factorial moments from exp(delta*t)*prod(1+a_i*t)."""
    from math import comb
    e = [0.0]*(order+1)
    e[0] = 1.0
    for x in a:
        for r in range(order, 0, -1):
            e[r] += x * e[r-1]
    return [factorial(r) * sum(e[j] * delta**(r-j)/factorial(r-j)
                               for j in range(r+1)) for r in range(order+1)]


def verify():
    cases = 0
    moment_checks = 0
    for n in range(1, 7):
        for blocks in partitions(n):
            sizes = [len(b) for b in blocks]
            actual = exact_moments_from_enumeration(blocks, n)
            prediction = factorial_moments_from_sizes(sizes)
            assert actual == prediction, (n, blocks, actual, prediction)
            assert actual[1] == 1
            if n >= 2:
                variance = Fraction(n*n-sum(s*s for s in sizes), n*(n-1))
                assert actual[2] == variance if len(blocks) >= 2 else variance == 0
            cases += 1
            moment_checks += len(actual)

    # Reference laws: one macroscopic fibre; two macroscopic fibres; all singleton fibres.
    # These finite comparisons corroborate but do not prove the limit theorem.
    asymptotic_tests = 0
    for n in (200, 1000, 3000):
        for macro_fractions in ((0.5,), (0.25, 0.5), ()):
            macros = [round(n*a) for a in macro_fractions]
            sizes = macros + [1]*(n-sum(macros))
            actual = limited_factorial_moments(sizes, 5)
            target = poisson_bernoulli_factorial_moments(
                macro_fractions, 1.0-sum(macro_fractions), 5)
            for r, (x,y) in enumerate(zip(actual,target)):
                assert abs(float(x)-y) < (0.5 if n == 200 else 0.08), \
                       (n, macro_fractions, r, x, y)
                asymptotic_tests += 1

    print(f"PASS: {cases} exhaustive set-partition/injection cases; "
          f"{moment_checks} exact factorial-moment checks; "
          f"{asymptotic_tests} limit-profile moment comparisons")


if __name__ == "__main__":
    verify()
