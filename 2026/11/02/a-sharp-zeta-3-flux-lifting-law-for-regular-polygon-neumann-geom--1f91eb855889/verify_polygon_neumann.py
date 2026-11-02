"""Standalone numerical checks for a regular-polygon Neumann flux benchmark.

Uses only Python's standard library. It checks exact Fourier identities through
independent quadrature and the limiting energy formula; it does not replace proof.
"""
from __future__ import annotations
import cmath
import math

TAU = 2.0 * math.pi


def sinc(x: float) -> float:
    return math.sin(x) / x if x else 1.0


def sine_coefficient(n: int, k: int) -> float:
    """Coefficient of sin(k*n*theta) in sin(tau_n(theta)); k >= 1."""
    assert n >= 3 and k >= 1
    return -2.0 * k * n * sinc(math.pi / n) * ((-1.0) ** k) / ((k * n) ** 2 - 1.0)


def independent_sine_coefficient(n: int, k: int, pieces: int = 80000) -> float:
    """Numerical integral on one facet, independent of the coefficient formula."""
    delta = math.pi / n
    dt = 2 * delta / pieces
    return sum(math.sin(-delta + (j + .5) * dt) *
               math.sin(k * n * (-delta + (j + .5) * dt))
               for j in range(pieces)) / pieces * 2


def harmonic_energy_cos_sine(n: int, kmax: int = 25000) -> float:
    """Exact Fourier-series expression for f=cos(theta), sine surrogate."""
    alpha = sinc(math.pi / n)
    return TAU * alpha * alpha * sum(
        (k * n) ** 3 / (((k * n) ** 2 - 1) ** 3)
        for k in range(1, kmax + 1))


def harmonic_energy_general(n: int, h_fourier: dict[int, complex], kmax: int = 25000) -> float:
    """Sum the exact separated Fourier sidebands, n>2*max(abs(m))."""
    assert n > 2 * max(map(abs, h_fourier))
    energy = 0.0
    for k in range(1, kmax + 1):
        a2 = sine_coefficient(n, k) ** 2 / 4
        for m, amp in h_fourier.items():
            energy += a2 * abs(amp) ** 2 * (
                1 / abs(k * n + m) + 1 / abs(-k * n + m))
    return TAU * energy


def polygon_flux_radially_flat(theta: float, n: int) -> float:
    """Pulled-back flux for u(r,theta)=cos(theta)."""
    period = TAU / n
    tau = (theta + period / 2) % period - period / 2
    return math.sin(theta) * math.tan(tau)


def polygon_flux_radially_flat_sin(theta: float, n: int) -> float:
    period = TAU / n
    tau = (theta + period / 2) % period - period / 2
    return math.sin(theta) * math.sin(tau)


def main() -> None:
    checks = 0
    for n in (3, 4, 5, 8, 13):
        for k in (1, 2, 3, 5):
            computed = independent_sine_coefficient(n, k)
            algebraic = sine_coefficient(n, k)
            assert abs(computed-algebraic) < 2e-8, (n, k, computed, algebraic)
            checks += 1

    # Compare the exact finite-N formula with a second spectral sideband sum.
    h = {-1: -0.5j, 1: 0.5j}  # h=-sin(theta)
    for n in (7, 11, 23, 53):
        a = harmonic_energy_cos_sine(n)
        b = harmonic_energy_general(n, h)
        assert abs(a-b) < 2e-11, (n, a, b)
        checks += 1

    # Full two-frequency tangent datum: f=cos(theta)+0.25cos(3theta).
    h2 = {-1: -0.5j, 1: 0.5j, -3: -0.375j, 3: 0.375j}
    h2_norm_squared = TAU * sum(abs(z)**2 for z in h2.values())
    zeta3 = sum(k ** -3 for k in range(1, 100001))  # <5e-11 tail
    target = 2 * zeta3 * h2_norm_squared
    ratios = []
    for n in (16, 32, 64, 128, 256):
        scaled = n**3 * harmonic_energy_general(n, h2)
        ratios.append(abs(scaled - target) / target)
        checks += 1
    assert all(a > b for a, b in zip(ratios, ratios[1:])), ratios
    assert ratios[-1] < 0.00018, ratios
    checks += 1

    # The true polygon tangent flux differs from its sine replacement by O(N^-3)
    # pointwise, and vanishes at the same angular cell centers.
    for n in (8, 16, 32, 64):
        delta = math.pi / n
        maxerr = max(abs(polygon_flux_radially_flat(t, n) -
                         polygon_flux_radially_flat_sin(t, n))
                     for t in [(j+0.5)*delta/50 for j in range(50)])
        assert maxerr < 2*delta**3
        checks += 1

    print('PASS', checks, 'independent numerical/Fourier consistency checks')
    print('single-mode N=256 scaled energy:', 256**3 * harmonic_energy_cos_sine(256))
    print('two-mode predicted limit:', target)
    print('two-mode N=256 relative difference:', ratios[-1])
    print('limits: finite Fourier sums and quadrature are not proof of the N-to-infinity claim')


if __name__ == '__main__':
    main()
