"""Finite sanity checks for the Schreier right-shift power-growth theorem.

The analytic inequalities and asymptotic are proved in RESULT.md; these
finite calculations only test the combinatorial partitions and witnesses.
"""
from fractions import Fraction
from math import ceil, log, log2


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


checks = 0
# Direct exact rational check of the harmonic witness bound against log 2.
# For every Schreier set of cardinality at most m and minimum m, the
# decreasing witness attains its largest mass on [m,2m-1].
for m in range(1, 401):
    mass = harmonic(2 * m) - harmonic(m)
    assert float(mass) < log(2), (m, mass)
    checks += 1

# The geometric block decomposition consumes m*(2**q-1) entries in q blocks.
# Its r-th full block begins at coordinate at least 2**r*m.
for k in range(0, 129):
    cap = ceil(log2(k + 2))
    for m in range(1, 65):
        remaining = m + k
        consumed = 0
        for r in range(cap):
            capacity = (2**r) * m
            assert m + consumed >= capacity
            consumed += min(capacity, remaining - consumed)
            if consumed == remaining:
                break
        assert consumed == remaining, (k, m, cap, consumed, remaining)
        checks += 1

for k in range(0, 2001):
    lower = float(harmonic(k + 2) - 1) / log(2)
    upper = ceil(log2(k + 2))
    assert lower <= upper + 1e-12, (k, lower, upper)
    checks += 1

print(f"PASS: {checks} finite sanity checks; no claim of exhaustive or infinite verification")
