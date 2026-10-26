#!/usr/bin/env python3
"""Numerical corroboration of the orbit-diffusion spectral theorem.

Two independent variational discretizations are used. Computations at
finite grid sizes do not certify monotonicity or limiting asymptotics;
those follow from the analytic Rayleigh/Hardy argument in RESULT.md.
Dependencies: NumPy and SciPy.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.special import eval_legendre, roots_legendre
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


def galerkin_gap(q, modes=28, quadrature=450):
    """Weighted Legendre odd-mode Galerkin eigenvalue on (-1,1)."""
    nodes, weights = roots_legendre(quadrature)
    degrees = np.arange(1, 2 * modes, 2)
    phi = np.array([eval_legendre(int(k), nodes) for k in degrees])
    mass = (phi * (weights / (1.0 + q * q * nodes * nodes))) @ phi.T
    energy = np.diag(2.0 * degrees * (degrees + 1.0) / (2.0 * degrees + 1.0))
    return float(eigh(energy, mass, subset_by_index=(0, 0), eigvals_only=True)[0] / 4.0)


def finite_element_gap(q, count=880, cutoff=13.0):
    """Independent half-line y=atanh(x) piecewise-linear Ritz approximation."""
    half = count // 2
    grid = np.r_[0.0, np.geomspace(1e-7, 1.0, half),
                 np.linspace(1.00001, cutoff, count - half)]
    ds = np.diff(grid)
    nd, wd = roots_legendre(5)
    locations = grid[:-1, None] + ds[:, None] * (nd + 1) / 2
    wt = (ds[:, None] * wd[None, :] / 2) / (
        1.0 + (1.0 + q * q) * np.sinh(locations) ** 2)
    left = (1 - nd) / 2
    right = (1 + nd) / 2
    mass_left = (wt * left[None, :] ** 2).sum(axis=1)
    mass_right = (wt * right[None, :] ** 2).sum(axis=1)
    mass_cross = (wt * (left * right)[None, :]).sum(axis=1)
    count_nodes = len(grid)
    diagonal_mass = np.zeros(count_nodes)
    diagonal_energy = np.zeros(count_nodes)
    diagonal_mass[:-1] += mass_left
    diagonal_mass[1:] += mass_right
    diagonal_energy[:-1] += 1 / ds
    diagonal_energy[1:] += 1 / ds
    stiffness = diags([-1 / ds, diagonal_energy, -1 / ds],
                      offsets=(-1, 0, 1), format='csc')[1:, 1:]
    mass = diags([mass_cross, diagonal_mass, mass_cross],
                 offsets=(-1, 0, 1), format='csc')[1:, 1:]
    return float(eigsh(stiffness, k=1, M=mass, sigma=0,
                       which='LM', tol=1e-9,
                       return_eigenvectors=False)[0] / 4)


def main():
    cases = [0.0, 0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
    estimates = [galerkin_gap(q) for q in cases]
    comparisons = 0
    def check(cond, label):
        nonlocal comparisons
        comparisons += 1
        if not cond:
            raise AssertionError(label)
    check(abs(estimates[0] - 0.5) < 1e-11, 'exact Legendre gap at q=0')
    for i in range(1, len(cases)):
        check(estimates[i] > estimates[i-1], 'increasing unnormalized gap')
        check(estimates[i]/(1+cases[i]**2) <
              estimates[i-1]/(1+cases[i-1]**2),
              'decreasing normalized gap')
    for q, value in zip(cases, estimates):
        check(value >= (1.0 + q*q)/16 - 1e-9, 'sharp Hardy lower bound')
        check(value >= 0.5 - 1e-10, 'Legendre baseline lower bound')
        if q > 0:
            trial = q**3/(6*(q-math.atan(q)))
            check(value < trial + 1e-8, 'one-mode variational bound')
    check(abs((estimates[1]-.5)/cases[1]**2-.3)<1e-3,
          'small-q perturbation coefficient 3/10')
    for q in [0., .2, .5, 1., 2., 5., 10.]:
        v1 = galerkin_gap(q, modes=26, quadrature=500)
        v2 = finite_element_gap(q)
        check(abs(v1-v2) < .002*max(1.,v1),
              'independent Galerkin and transformed mesh agreement')
    for q in [20., 70., 200.]:
        v = finite_element_gap(q, count=1200)
        check(v/(1+q*q) > 1/16,
              'large-q Hardy lower bound')
        check(v/(1+q*q) < .17,
              'large-q trend towards 1/16')
    print('PASS:',comparisons,'numerical comparisons')
    print(' q             mu1              mu1/(1+q^2)')
    for q, value in zip(cases, estimates):
        print(f'{q:6g} {value:18.10f} {value/(1+q*q):19.10f}')

if __name__ == '__main__':
    main()
