"""Numerical consistency check of a three-rotation convex lens example.

Requires Python 3 and NumPy. This is not a proof of the general theorem.
"""
import math
import numpy as np


def check_lens(samples=98304, c=1.0):
    assert samples % 6 == 0
    theta = 2 * math.pi * (np.arange(samples) + 0.5) / samples
    active = ((theta < math.pi / 3) |
              ((theta >= math.pi) & (theta < 4 * math.pi / 3)))
    rho = np.where(active, c, 0.0)
    shifts = [np.roll(rho, j * samples // 3) for j in range(3)]
    orbit_error = float(np.max(np.abs(sum(shifts) - c)))
    coeff = np.fft.rfft(rho) / samples
    first_moment_error = float(abs(coeff[1]))
    n = np.arange(2, len(coeff), dtype=float)
    area_est = (math.pi * abs(coeff[0]) ** 2
                - 2 * math.pi * np.sum(abs(coeff[2:]) ** 2 / (n * n - 1)))
    area_exact = c * c * (math.pi / 3 - math.sqrt(3) / 2)
    print(f"rotated curvature-sum max error = {orbit_error:.3g}")
    print(f"first Fourier moment error = {first_moment_error:.3g}")
    print(f"computed area = {area_est:.13f}")
    print(f"exact segment area = {area_exact:.13f}")
    print(f"absolute area error = {abs(area_est-area_exact):.3g}")
    assert orbit_error < 1e-12
    assert first_moment_error < 1e-12
    assert abs(area_est - area_exact) < 5e-10


if __name__ == "__main__":
    check_lens()
