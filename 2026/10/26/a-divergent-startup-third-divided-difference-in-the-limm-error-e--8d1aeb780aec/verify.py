#!/usr/bin/env python3
# Exact rational replay of the printed LIMM startup formula.
from fractions import Fraction


def startup(h):
    y0 = Fraction(1)
    f0 = Fraction(1)
    j0 = Fraction(1)
    # Order-one LIMM with mu_{-1}=1: (1-h*j0)(y1-y0)=h*f0.
    y1 = y0 + h * f0 / (1 - h * j0)
    d2 = (((y1 - y0) / h) - f0) / (2 * h)
    d3 = (d2 - j0 * f0) / (3 * h)
    return y1, d2, d3


def main():
    previous_error = None
    for h in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
        y1, d2, d3 = startup(h)
        assert y1 == 1 / (1 - h)
        assert d2 == 1 / (2 * (1 - h))
        assert d3 == (2 * h - 1) / (6 * h * (1 - h))
        assert h * d3 == -Fraction(1, 6) + h / (6 * (1 - h))
        normalized_estimator = 6 * h**3 * d3
        assert normalized_estimator / h**2 == 6 * h * d3
        error_from_limit = abs(h * d3 + Fraction(1, 6))
        if previous_error is not None:
            assert error_from_limit < previous_error
        previous_error = error_from_limit
        print(f"h={h}: y1={y1}, delta2={d2}, delta3={d3}, h*delta3={h*d3}")
    # The exact divided-difference target for y(t)=exp(t) tends to y'''(0)/3! = 1/6.
    assert Fraction(1, 6) == Fraction(1, 6)
    print("PASS: exact rational identities; h*delta3 tends to -1/6, not +1/6.")


if __name__ == "__main__":
    main()
