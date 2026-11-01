"""Standalone numerical corroboration of two-disk Fock localization asymptotics.

Requires Python 3 with numpy and scipy. It does not certify infinite-dimensional
claims: the analytical proof supplies those statements. This script checks
normalization, quadrature convergence, and the predicted separation scaling.
"""
from math import exp, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gammaln


def two_disk_eigenvalues(distance, squared_radius=1.0,
                         modes=70, radial_nodes=30, angular_nodes=192):
    """Rayleigh-Ritz matrix via tensor Gaussian disk quadrature."""
    s = float(squared_radius)
    x, gauss_weights = leggauss(radial_nodes)
    r = np.sqrt(s * (x + 1.0) / 2.0)
    dr2_weights = (s / 2.0) * gauss_weights
    angles = 2.0 * np.pi * np.arange(angular_nodes) / angular_nodes
    angular_points = np.exp(1j * angles)
    z_list, weights_list = [], []
    for center in (-distance / 2.0, distance / 2.0):
        z_list.append((center + r[:, None] * angular_points[None, :]).ravel())
        weights_list.append(np.repeat(dr2_weights / angular_nodes,
                                      angular_nodes))
    z = np.concatenate(z_list)
    weights = np.concatenate(weights_list)
    n = np.arange(modes)
    powers = np.exp(n[None, :] * np.log(np.where(z[:, None] == 0,
                                                   1.0, z[:, None]))
                    - 0.5 * gammaln(n[None, :] + 1))
    samples = np.exp(-0.5 * np.abs(z) ** 2)[:, None] * powers
    matrix = (samples.conj().T * weights[None, :]) @ samples
    eigenvalues = np.linalg.eigvalsh(matrix)
    return eigenvalues[-2:]


def main():
    s = 1.0
    lambda0 = 1.0 - exp(-s)
    lambda1 = 1.0 - (1.0 + s) * exp(-s)
    delta = s * exp(-s)
    assert abs(lambda0 - lambda1 - delta) < 1e-14
    checks = 1
    for d, tolerance in [(4.0, 0.035), (5.0, 0.002), (6.0, 0.0002)]:
        eigen = two_disk_eigenvalues(d)
        refined = two_disk_eigenvalues(d, modes=85,
                                       radial_nodes=38, angular_nodes=256)
        assert np.max(np.abs(eigen - refined)) < 3e-11
        checks += 1
        eps = exp(-d * d / 2.0)
        ratios = (eigen - lambda0) / (lambda0 * eps)
        assert abs(ratios[0] + 1.0) < tolerance, (d, ratios)
        assert abs(ratios[1] - 1.0) < tolerance, (d, ratios)
        checks += 2
        assert eigen[0] > lambda1
        assert eigen[1] > eigen[0]
        checks += 2
        print(f"d={d:g}: eig=({eigen[0]:.12f}, {eigen[1]:.12f}); "
              f"scaled=({ratios[0]:.8f}, {ratios[1]:.8f})")
    assert checks == 16
    print(f"PASS: {checks} deterministic assertions; no infinite-dimensional certification")


if __name__ == '__main__':
    main()
