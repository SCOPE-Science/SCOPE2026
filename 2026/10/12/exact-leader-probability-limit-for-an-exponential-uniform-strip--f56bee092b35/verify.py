"""Deterministic diagnostics for the exponential--uniform strip."""

from math import atan, exp, expm1, fsum, isclose, log


def midpoint(fun, lo, hi, n):
    h = (hi - lo) / n
    return h * fsum(fun(lo + (j + 0.5) * h) for j in range(n))


def trapezoid(fun, lo, hi, n):
    h = (hi - lo) / n
    return h * ((fun(lo) + fun(hi)) / 2 + fsum(fun(lo + j * h)
                                               for j in range(1, n)))


def main():
    for x, w in [(0.2, 0.8), (0.4, 0.4), (1.25, 0.5), (1.0, 0.999)]:
        # For z below x, one's only chance to exceed is in coordinate 2.
        competing = exp(-x) + midpoint(
            lambda z: exp(-z) * (w - x + z), max(0.0, x - w), x, 20000
        )
        t = exp(-x)
        formula = ((exp(w) - w) * t if x >= w else
                   1 + w + log(t) - w * t)
        assert isclose(competing, formula, rel_tol=1e-9, abs_tol=1e-10)

    integrand = lambda w: 1 / (exp(w) - w)
    limit = midpoint(integrand, 0, 1, 100000)
    assert abs(limit - trapezoid(integrand, 0, 1, 100000)) < 1e-10
    printed_cdf_limit = midpoint(lambda w: 1 / (1 + w * expm1(w)),
                                 0, 1, 100000)
    assert printed_cdf_limit < atan(1.0) < 0.8 < limit
    print(f"VERIFY_OK limit={limit:.10f} printed_cdf_limit={printed_cdf_limit:.10f}")


if __name__ == "__main__":
    main()
