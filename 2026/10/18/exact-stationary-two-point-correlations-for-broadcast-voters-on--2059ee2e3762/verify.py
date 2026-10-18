"""Exact finite-state checks of a two-ancestral-lineage tree model.

All arithmetic is rational; finite checks do not prove the infinite-tree limit.
"""
from fractions import Fraction as F


def closed(d, q, k):
    assert d >= 3 and 0 <= q <= 1 and k >= 0
    if k == 0:
        return F(1)
    den = 2 * (d - 1) ** 2 + (d - 2) * q
    if k == 1:
        return (2 * (d - 1) + (d - 2) * q) / den
    return (2 + (d - 2) * q) / den / (d - 1) ** (k - 2)


def generator(d, q, k):
    """Unnormalized CTMC rates: (coalescence, inward, outward)."""
    if k == 1:
        return F(2), F(0), F(2 * (d - 1))
    if k == 2:
        return q, 2 * (1 - q), F(2 * (d - 1))
    return F(0), F(2), F(2 * (d - 1))


def truncated(d, q, boundary):
    """Independent exact tridiagonal Dirichlet solver: success at 0, loss at boundary."""
    n = boundary - 1
    lower, diag, upper, right = [], [], [], []
    for k in range(1, boundary):
        c, inward, outward = generator(d, q, k)
        lower.append(-inward)
        diag.append(c + inward + outward)
        upper.append(-outward)
        right.append(c)
    # Forward elimination, first line lacks a variable at zero (handled as a coalescence rate).
    for k in range(1, n):
        factor = lower[k] / diag[k - 1]
        diag[k] -= factor * upper[k - 1]
        right[k] -= factor * right[k - 1]
    vals = [F(0)] * (boundary + 1)
    vals[0] = F(1)
    for k in range(n - 1, -1, -1):
        vals[k + 1] = (right[k] - (upper[k] * vals[k + 2] if k < n - 1 else 0)) / diag[k]
    return vals


def main():
    assertions = 0
    qs = (F(0), F(1, 5), F(1, 2), F(4, 5), F(1))
    for d in range(3, 13):
        for q in qs:
            for k in range(1, 18):
                c, inward, outward = generator(d, q, k)
                # Verify the boundary-to-interior CTMC harmonic equation exactly.
                lhs = (c + inward + outward) * closed(d, q, k)
                rhs = c + inward * closed(d, q, k - 1) + outward * closed(d, q, k + 1)
                assert lhs == rhs, (d, q, k, lhs, rhs)
                assertions += 1
            for boundary in (6, 9, 13):
                h = truncated(d, q, boundary)
                for k in range(1, boundary):
                    delta = closed(d, q, k) - h[k]
                    # The boundary correction is at most the probability of return from boundary.
                    assert F(0) <= delta <= closed(d, q, boundary), (d, q, boundary, k, delta)
                    assertions += 1
            # Classical uncoordinated dual: simple regular-tree hitting probabilities.
            if q == 0:
                for k in range(1, 18):
                    assert closed(d, q, k) == F(1, (d - 1) ** k)
                    assertions += 1
            # Strict increase in q for each nonzero distance.
            if q < 1:
                for k in (1, 2, 3, 5):
                    assert closed(d, q, k) < closed(d, F(1), k)
                    assertions += 1
    print(f"PASS: {assertions} exact rational recurrence, finite-boundary and monotonicity checks")


if __name__ == '__main__':
    main()
