"""High-precision spot checks for the classical conditional-subentropy bound.

This finite computation illustrates, but does not establish, the theorem for all
probability distributions. The accompanying argument is analytic.
Python standard library only.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from random import Random


def q_spectrum(v):
    """Divided-difference subentropy, positive and pairwise-distinct eigenvalues.

    Zero entries are omitted by subentropy's standard zero-padding identity.
    Repeated positive values are handled analytically in the proof, not here.
    """
    v = [x for x in v if x > 0]
    if len(v) == 1:
        return Decimal(0)
    if len(set(v)) != len(v):
        raise ValueError("Use a distinct-spectrum verification instance")
    vals = [Decimal(x.numerator) / Decimal(x.denominator) for x in v]
    d = len(vals)
    return -sum(
        (a**d * a.ln()) / _denominator(vals, i)
        for i, a in enumerate(vals)
    )


def _denominator(v, i):
    out = Decimal(1)
    for j, b in enumerate(v):
        if j != i:
            out *= v[i] - b
    return out


def check(table):
    assert table and all(row and len(row) == len(table[0]) for row in table)
    entries = [Fraction(w) for row in table for w in row]
    assert sum(entries, Fraction(0)) == 1
    marginal = [sum(map(Fraction, row), Fraction(0)) for row in table]
    p_guess = sum((max(map(Fraction, row)) for row in table), Fraction(0))
    conditional_q = q_spectrum(entries) - q_spectrum(marginal)
    error = Decimal((1 - p_guess).numerator) / Decimal((1 - p_guess).denominator)
    tol = Decimal('1e-36')
    assert conditional_q >= -tol, (table, conditional_q)
    assert conditional_q <= error + tol, (table, conditional_q, error)
    return conditional_q


def main():
    with localcontext() as ctx:
        ctx.prec = 85
        explicit = [
            [[Fraction(17, 100), Fraction(1, 100), Fraction(2, 100)],
             [Fraction(31, 100), Fraction(13, 100), Fraction(36, 100)]],
            [[Fraction(41, 100), Fraction(3, 100), Fraction(1, 100)],
             [Fraction(10, 100), Fraction(14, 100), Fraction(31, 100)]],
            [[Fraction(17, 100), Fraction(0), Fraction(3, 100)],
             [Fraction(0), Fraction(13, 100), Fraction(67, 100)]],
        ]
        for t in explicit:
            check(t)
        rng = Random(41821)
        checked = 0
        while checked < 45:
            # Exactly rational probability vectors; all positive entries and
            # both positive marginal values must be pairwise distinct.
            vals = rng.sample(range(1, 300), 6)
            q1, q2 = sum(vals[:3]), sum(vals[3:])
            if q1 == q2:
                continue
            total = sum(vals)
            t = [[Fraction(i, total) for i in vals[:3]],
                 [Fraction(i, total) for i in vals[3:]]]
            check(t)
            checked += 1
        for n in (100, 1000, 10000):
            e = Fraction(1, n)
            val = q_spectrum([1-e, e])
            assert Decimal(0) < val < Decimal(1) / Decimal(n)
        print('VERIFY_OK tables=48 binary_edges=3 precision=85 analytic_proof_required=yes')


if __name__ == '__main__':
    main()
