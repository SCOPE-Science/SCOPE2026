"""Independent finite-matrix checks for a lossy magnetic cycle.

Run with Python 3 and NumPy. Numerical checks supplement, not replace, the proof.
"""
from math import cos, pi, sin
import numpy as np
from numpy.polynomial.chebyshev import Chebyshev


def lossy_cycle(n, hopping, loss, flux):
    """Matrix in the vertex basis with one lossy site at vertex 0."""
    matrix = np.zeros((n, n), dtype=complex)
    phase = np.exp(1j * flux / n)
    for j in range(n):
        matrix[j, (j + 1) % n] = hopping * phase
        matrix[(j + 1) % n, j] = hopping * phase.conjugate()
    matrix[0, 0] -= 1j * loss
    return matrix


def secular_polynomial(n, hopping, loss, flux, z):
    cheb = Chebyshev.basis(n)
    scaled_energy = z / (2 * hopping)
    return 2 * hopping**n * (
        cheb(scaled_energy) - cos(flux)
        + 1j * loss / (2 * hopping * n) * cheb.deriv()(scaled_energy)
    )


def verified_energy(n, hopping, loss, flux, energy_at_symmetry):
    eig = np.linalg.eigvals(lossy_cycle(n, hopping, loss, flux))
    return eig[np.argmin(abs(eig - energy_at_symmetry))]


def run():
    checks = 0
    max_det_relative_error = 0.0
    # Construct the physical matrix independently of the analytic determinant.
    for n in range(3, 14):
        for hopping, loss, phi, z in [
            (1.3, 0.6, 0.37, 0.8 + 0.3j),
            (0.7, 2.0, 2.1, -1.1 + 0.5j),
            (1.8, 0.3, 3.7, 1.2 - 0.9j),
        ]:
            direct = np.linalg.det(z * np.eye(n) - lossy_cycle(n, hopping, loss, phi))
            formula = secular_polynomial(n, hopping, loss, phi, z)
            error = abs(direct - formula) / max(1.0, abs(direct), abs(formula))
            assert error < 5e-11, (n, hopping, loss, phi, error)
            max_det_relative_error = max(max_det_relative_error, error)
            checks += 1

    widths = 0
    max_coefficient_relative_error = 0.0
    max_real_quadratic_ratio = 0.0
    for n in range(3, 13):
        for hopping, loss in [(1.0, 0.8), (1.5, 2.1), (0.7, 3.4)]:
            for symmetric_flux in (0.0, pi):
                for index in range(n):
                    q = (2 * pi * index + symmetric_flux) / n
                    if not (1e-9 < q < pi - 1e-9):
                        continue
                    energy = 2 * hopping * cos(q)
                    expected_width_coefficient = (
                        2 * hopping**2 * sin(q)**2 / (loss * n)
                    )
                    d = 0.006
                    nearby = verified_energy(
                        n, hopping, loss, symmetric_flux + d, energy
                    )
                    inferred = -nearby.imag / d**2
                    rel = abs(inferred - expected_width_coefficient) / expected_width_coefficient
                    assert rel < 0.008, (n, index, symmetric_flux, rel)
                    max_coefficient_relative_error = max(max_coefficient_relative_error, rel)
                    # Leading change of the real energy vanishes; error is fourth order.
                    real_quadratic_ratio = (
                        abs(nearby.real - energy) / (d**2 * expected_width_coefficient)
                    )
                    assert real_quadratic_ratio < 0.003, (
                        n, index, symmetric_flux, real_quadratic_ratio
                    )
                    max_real_quadratic_ratio = max(
                        max_real_quadratic_ratio, real_quadratic_ratio
                    )
                    widths += 1

    print("PASS: determinant evaluations:", checks)
    print("PASS: mode linewidth evaluations:", widths)
    print("max determinant relative error:", max_det_relative_error)
    print("max linewidth-coefficient relative error:", max_coefficient_relative_error)
    print("max real quadratic ratio:", max_real_quadratic_ratio)


if __name__ == "__main__":
    run()
