"""Independent numerical sanity checks for the stated two-coset Poisson Gabor formulas.

Uses only the Python standard library. The accompanying analytical argument, not this
finite test, proves the continuum and all-parameter assertions.
"""
import cmath
import math


def zak_closed(x, omega, width):
    alpha = math.pi * width
    r = math.exp(-2 * alpha)
    aa = math.exp(-2 * alpha * omega)
    bb = math.exp(-2 * alpha * (1 - omega))
    z = cmath.exp(2j * math.pi * x)
    return (math.pi / width) * cmath.exp(2j * math.pi * x * omega) * (
        aa / (1 - r * z) + bb / (z - r)
    )


def analytic_bounds(width, delta):
    alpha = math.pi * width
    distance = min(delta, 1 - delta)
    lower = (2 * math.pi**2 / width**2) * (
        math.sinh(alpha * distance) / math.cosh(alpha)
    ) ** 2
    upper = (math.pi**2 / width**2) * (
        math.cosh(alpha) ** 2 + math.cosh(alpha * (1 - 2 * delta)) ** 2
    ) / math.sinh(alpha) ** 2
    return lower, upper


def symbol(x, omega, width, delta):
    return abs(zak_closed(x, omega, width)) ** 2 + abs(
        zak_closed(x, (omega - delta) % 1, width)
    ) ** 2


def finite_zak(x, omega, width, cutoff=8000):
    return sum(
        1 / ((x + k) ** 2 + width**2) * cmath.exp(-2j * math.pi * k * omega)
        for k in range(-cutoff, cutoff + 1)
    )


for width in (0.6, 1.0, 1.7):
    for delta in (0.13, 0.37, 0.5, 0.81):
        lo, hi = analytic_bounds(width, delta)
        omega_min = (1 + delta) / 2 if delta <= 0.5 else delta / 2
        assert abs(symbol(0.5, omega_min, width, delta) - lo) < 1e-10
        assert abs(symbol(0, 0, width, delta) - hi) < 1e-10
        assert abs(symbol(0, delta, width, delta) - hi) < 1e-10
        for ix in range(13):
            for io in range(15):
                got = symbol(ix / 13, io / 15, width, delta)
                assert lo - 1e-10 <= got <= hi + 1e-10
        # Direct lattice sums provide a separate check of the Poisson Zak formula.
        for xx, oo in ((0, 0), (0.5, 0.25), (0.26, 0.44)):
            err = abs(finite_zak(xx, oo, width) - zak_closed(xx, oo, width))
            assert err < 0.0003, (width, delta, xx, oo, err)
    # The balanced two-coset case coincides with regular frequency 1/2 oversampling.
    lo, hi = analytic_bounds(width, 0.5)
    alpha = math.pi * width
    q2lower = math.pi**2 / width**2 * (
        1 / math.cosh(alpha) - 1 / math.cosh(alpha) ** 2
    )
    q2upper = math.pi**2 / width**2 * (
        (math.cosh(alpha) / math.sinh(alpha)) ** 2 + 1 / math.sinh(alpha) ** 2
    )
    assert abs(lo - q2lower) < 1e-11
    assert abs(hi - q2upper) < 1e-11

print('CHECK_OK: exact Zak extremal fibers, numeric grid, direct sums, and balanced-lattice limit')
