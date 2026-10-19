"""Finite exact and numerical falsification checks for cusp-switching return laws.

Run with Python 3. The analytical proof is in RESULT.md; the finite
checks here are not a substitute for its infinite-time arguments.
"""
from fractions import Fraction
from math import ceil, exp, log, log1p


def rational_events(lam, x0, y0, horizon):
    x, y = x0, y0
    events = []
    for n in range(horizon):
        assert y != x * x, "An orbit reached the excluded switching boundary"
        if y > x * x:
            events.append(n)
            x, y = 1 - lam * x, lam * y
        else:
            x, y = lam * x, lam * y
    return events


def ceiling_height_log(q, y):
    """Exact ceil(log_q(1/y)) for integral q and rational y in (0,1]."""
    power, n = Fraction(1), 0
    while power * y < 1:
        power *= q
        n += 1
    return n


def numerical_events(lam, p, x0, y0, horizon):
    """Track logarithmic coordinates to avoid underflow in late excursions."""
    xl, yl, ll = log(x0), log(y0), log(lam)
    events = []
    for n in range(horizon):
        if yl > p * xl:
            events.append(n)
            xl = log1p(-lam * exp(xl))
        else:
            xl += ll
        yl += ll
    return events


def main():
    lam = Fraction(1, 5)
    cases = [(Fraction(1, 10), Fraction(9, 10)),
             (Fraction(1, 10), Fraction(1, 5)),
             (Fraction(1, 10), Fraction(1, 25)),
             (Fraction(1, 4), Fraction(1)),
             (Fraction(1, 5), Fraction(1, 3))]
    for x, y in cases:
        ev = rational_events(lam, x, y, 170)
        offset = 2 + ceiling_height_log(5, y)
        assert len(ev) >= 5
        assert all(ev[j + 1] == 2 * ev[j] + offset
                   for j in range(1, len(ev) - 1)), (x, y, ev)
    for p, f in [(1.3, 0.15), (1.5, 0.2), (2.0, 0.2),
                 (2.5, 0.2), (3.0, 0.2), (5.0, 0.1)]:
        assert f < (1 - f) ** p
        ev = numerical_events(f, p, 0.2, 0.8, 80000)
        assert len(ev) >= 6
        factor = p / (p - 1)
        assert abs(ev[-1] / ev[-2] - factor) < 0.01, (p, ev[-3:])
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
