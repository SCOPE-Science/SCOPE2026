"""Independent numerical checks for an affine product-of-balls Fourier-zero theorem.

Requirements: Python 3, NumPy, SciPy. The analytic proof is in RESULT.md.
Run: python check_fourier_product.py
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import jv, gammaln


def first_bessel_zero(order):
    """Locate first J_order root by a short sign scan."""
    a = max(1e-5, order / 2)
    step = 0.04
    fa = jv(order, a)
    while a < 10 * (order + 1):
        b = a + step
        fb = jv(order, b)
        if fa > 0 and fb < 0:
            return brentq(lambda z: jv(order, z), a, b, xtol=1e-13)
        a, fa = b, fb
    raise RuntimeError('Bessel first zero not bracketed')


def intrinsic_data(dims):
    roots = [first_bessel_zero(n / 2) for n in dims]
    n = sum(dims)
    diag = np.concatenate([np.full(k, j) for k, j in zip(dims, roots)])
    return roots, diag, n


def diagnostics(A, dims, roots, diag):
    n = sum(dims)
    blocks = np.split(A, np.cumsum(dims)[:-1], axis=1)
    radius = min(j / np.linalg.norm(block, ord=2)
                 for j, block in zip(roots, blocks))
    C = radius * A / diag[np.newaxis, :]
    sign, logdet = np.linalg.slogdet(C)
    assert sign != 0
    gap = -logdet
    u, s, vh = np.linalg.svd(C)
    nearest = u @ vh
    sqdist = np.linalg.norm(C - nearest, ord='fro') ** 2
    assert gap >= -2e-11, (gap, dims)
    assert sqdist <= 2 * gap + 3e-9, (sqdist, gap)
    return radius, gap, sqdist


def f_value(n):
    root = first_bessel_zero(n / 2)
    log_unitball = (n / 2) * math.log(math.pi) - gammaln(n / 2 + 1)
    return math.exp(log_unitball / n) * root


def main():
    rng = np.random.default_rng(722602)
    runs = 0
    for dims in ((1, 1), (1, 2), (2, 2), (1, 1, 3), (2, 3, 2)):
        roots, diag, n = intrinsic_data(dims)
        u, _ = np.linalg.qr(rng.normal(size=(n, n)))
        r, gap, sqdist = diagnostics(u * diag, dims, roots, diag)
        assert abs(r - 1) < 5e-12
        assert abs(gap) < 5e-12
        assert sqdist < 1e-20
        runs += 1
        # Check the predicted first-zero frequency against each radial Bessel factor.
        for _ in range(5):
            a = rng.normal(size=(n, n)) + 1.5 * np.eye(n)
            blocks = np.split(a, np.cumsum(dims)[:-1], axis=1)
            spectral = [(j / np.linalg.norm(z, ord=2), i) for i, (j, z) in enumerate(zip(roots, blocks))]
            radius, winning = min(spectral)
            uu = np.linalg.svd(blocks[winning], full_matrices=False)[0][:, 0]
            z = np.linalg.norm(blocks[winning].T @ (radius * uu))
            assert abs(z - roots[winning]) < 1e-10
            assert abs(jv(dims[winning] / 2, z)) < 2e-9
            small_direction = rng.normal(size=n)
            small_direction /= np.linalg.norm(small_direction)
            for j, block, q in zip(roots, blocks, dims):
                arg = np.linalg.norm(block.T @ (0.9 * radius * small_direction))
                assert arg < j
                assert jv(q / 2, arg) > 0
        for _ in range(80):
            a = rng.normal(size=(n, n)) + np.eye(n)
            if abs(np.linalg.det(a)) < 1e-5:
                continue
            diagnostics(a, dims, roots, diag)
            runs += 1
    for epsilon in (0.2, 0.1, 0.05, 0.01):
        dims = (1, 1)
        roots, diag, n = intrinsic_data(dims)
        block = np.array([[1, epsilon], [0, math.sqrt(1 - epsilon**2)]])
        radius, gap, sqdist = diagnostics(block * diag, dims, roots, diag)
        assert abs(radius - 1) < 1e-10
        assert abs(gap + 0.5 * math.log(1 - epsilon**2)) < 1e-10
        assert abs(sqdist / gap - 1) < 0.1
        runs += 1
    print('PASS: exact scaled equality and Frobenius stability,', runs, 'matrix checks')
    print('balanced partition ratio and entropy limit:')
    for n in (10, 20, 40, 80):
        actual = f_value(n // 2) / f_value(n)
        print(f'd={n}: ratio={actual:.9f}, limit={1/math.sqrt(2):.9f}')
        assert actual < 1
        assert actual > 1 / math.sqrt(2)
    print('PASS: high-dimensional ratios approach the predicted entropy factor')

if __name__ == '__main__':
    main()
