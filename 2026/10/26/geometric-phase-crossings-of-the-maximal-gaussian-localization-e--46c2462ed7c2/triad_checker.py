"""Finite-section quadrature checks for triangular Gaussian-Fock localization."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln
from numpy.polynomial.legendre import leggauss


def sector_leaders(radius, disk_radius, modes=40, radial_nodes=18, angular_nodes=96):
    """Eigenvalues of the normalized disk-union Toeplitz matrix in C3 sectors."""
    nodes, weights = leggauss(radial_nodes)
    t = (nodes + 1.0) / 2.0
    weights = weights / 2.0
    angles = 2.0 * np.pi * np.arange(angular_nodes) / angular_nodes
    z = (radius + disk_radius * np.sqrt(t[:, None]) *
         np.exp(1j * angles[None, :])).ravel()
    integration_weights = np.repeat(weights, angular_nodes) / angular_nodes
    orders = np.arange(modes)
    values = np.array([z**int(j) * np.exp(-0.5 * gammaln(j + 1))
                       for j in orders]).T
    values *= np.exp(-0.5 * np.abs(z)**2)[:, None]
    leaders = []
    for sector in range(3):
        columns = np.flatnonzero(orders % 3 == sector)
        v = values[:, columns]
        matrix = 3.0 * (v.conj().T * integration_weights) @ v
        leaders.append(float(np.linalg.eigvalsh(matrix)[-1]))
    return np.array(leaders)


def point_limit_spectrum(radius):
    theta = math.sqrt(3.0) * radius**2 / 2.0
    rho = math.exp(-1.5 * radius**2)
    return np.array([1.0 + 2.0 * rho * math.cos(theta - 2.0 * math.pi * j / 3)
                     for j in range(3)])


def check():
    for m in (0, 1, 2):
        nominal_radius = math.sqrt(2 * (2*m + 1) * math.pi / (3 * math.sqrt(3)))
        epsilon = 0.08 if m < 2 else 0.025
        leading = np.argsort(point_limit_spectrum(nominal_radius))[-2:]
        i, j = int(leading[0]), int(leading[1])
        def difference(radius):
            levels = sector_leaders(radius, epsilon)
            return levels[i] - levels[j]
        halfwidth = 0.035
        assert difference(nominal_radius-halfwidth)*difference(nominal_radius+halfwidth) < 0
        root = brentq(difference, nominal_radius-halfwidth,
                      nominal_radius+halfwidth, xtol=1e-12)
        levels = sector_leaders(root, epsilon)
        assert abs(levels[i]-levels[j]) < 1e-10
        assert min(levels[i], levels[j]) > max(levels[k] for k in range(3) if k not in (i,j))
        assert abs(root-nominal_radius) < 0.015
        print(f'm={m}; nominal={nominal_radius:.12f}; numerical_crossing={root:.12f}; '
              f'top_pair=({i},{j}); gap_to_third={min(levels[i],levels[j])-min(levels):.10f}')
    for R in (0.3, 0.9, 1.7):
        numerical = sector_leaders(R, 0.004)
        predicted = np.sort(point_limit_spectrum(R))
        assert np.max(np.abs(np.sort(numerical)-predicted)) < 3e-5
        print(f'point_limit_radius={R:.2f}; max_error={np.max(np.abs(np.sort(numerical)-predicted)):.3e}')
    print('PASS: six finite-dimensional spectral checks. No inference of an infinite-dimensional proof from these checks.')

if __name__ == '__main__':
    check()
