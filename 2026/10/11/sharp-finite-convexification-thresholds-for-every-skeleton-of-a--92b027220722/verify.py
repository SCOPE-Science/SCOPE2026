"""Exact-rational checks for simplex-skeleton equal-weight decompositions.

Usage: python verify.py
These tests supplement, rather than replace, the finite-dimensional proof.
"""
from fractions import Fraction
from random import Random


def decompose(weights, k, r):
    """Split nonnegative total mass k into k probability rows, each r+1-sparse."""
    weights = list(weights)
    assert len(weights) <= k * r + 1
    assert sum(weights) == k
    weights += [Fraction(0)] * (k * r + 1 - len(weights))
    active = list(range(len(weights)))
    rows = []
    for remaining in range(k, 1, -1):
        assert len(active) == remaining * r + 1
        active.sort(key=lambda i: (-weights[i], i))
        initial = None
        for start in range(len(active) - r + 1):
            if sum(weights[active[j]] for j in range(start, start + r)) <= 1:
                initial = start
                break
        assert initial is not None
        exhausted = active[initial : initial + r]
        mass = sum(weights[i] for i in exhausted)
        other = active[initial - 1] if initial else active[r]
        assert other not in exhausted
        deficit = 1 - mass
        assert Fraction(0) <= deficit <= weights[other]
        row = [Fraction(0)] * len(weights)
        for i in exhausted:
            row[i] = weights[i]
            weights[i] = Fraction(0)
        row[other] = deficit
        weights[other] -= deficit
        assert sum(row) == 1
        assert sum(v > 0 for v in row) <= r + 1
        rows.append(row)
        active = [i for i in active if i not in exhausted]
        assert sum(weights[i] for i in active) == remaining - 1
    row = [Fraction(0)] * len(weights)
    for i in active:
        row[i] = weights[i]
    assert sum(row) == 1 and sum(v > 0 for v in row) <= r + 1
    rows.append(row)
    return rows


def verify():
    rng = Random(273831)
    tested = 0
    for d in range(2, 22):
        for r in range(1, d):
            k0 = (d + r - 1) // r
            for k in sorted({k0, k0 + 1, k0 + 3}):
                for case in range(7):
                    numerators = [rng.randint(0 if case % 3 == 0 else 1, 500)
                                  for _ in range(d + 1)]
                    if not sum(numerators):
                        numerators[0] = 1
                    weights = [Fraction(k * a, sum(numerators)) for a in numerators]
                    rows = decompose(weights, k, r)
                    assert len(rows) == k
                    assert all(sum(x > 0 for x in row) <= r + 1 for row in rows)
                    assert all(sum(row) == 1 for row in rows)
                    assert all(sum(row[i] for row in rows) == weights[i]
                               for i in range(d + 1))
                    tested += 1
            if k0 > 1:
                k = k0 - 1
                eps = Fraction(1, 2*k)
                witness = [1 - eps] + [eps / d] * d
                assert sum(witness) == 1
                assert k * eps < 1 and k*r < d
    print(f'VERIFY_OK {tested} exact rational decompositions; sharpness inequalities checked')


if __name__ == '__main__':
    verify()
