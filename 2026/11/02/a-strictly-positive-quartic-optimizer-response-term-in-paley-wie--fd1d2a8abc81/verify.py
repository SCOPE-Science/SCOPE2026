"""Supplementary finite Fourier-quadrature checks of a prolate perturbation identity.

Run with Python, NumPy. These finite matrices do not certify the continuum result.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss


def finite_check(n=90):
    pts, wgts = leggauss(n)
    freq, wgts = pts / 2.0, wgts / 2.0
    gap = freq[:, None] - freq[None, :]
    weight = np.sqrt(wgts[:, None] * wgts[None, :])

    def interval(left, right):
        length = right - left
        return length * np.sinc(length * gap) * np.cos(np.pi * (left + right) * gap)

    checks = 0
    for s in (0.75, 1.5, 3.0):
        a = s / 2.0
        baseline = weight * interval(-a, a)
        eigenvalues, modes = np.linalg.eigh(baseline)
        top = eigenvalues[-1]
        ground = modes[:, -1]
        q = weight * (-4.0 * np.pi * gap * np.sin(2.0 * np.pi * a * gap))
        transition = modes[:, :-1].T @ (q @ ground)
        w_value = float(np.sum(transition**2 / (top - eigenvalues[:-1])))
        assert w_value > 0.0
        checks += 1
        errors = []
        for m in (0.12, 0.08, 0.04):
            update = interval(a, a + m) + interval(-a - m, -a)
            update -= interval(a - m, a) + interval(-a, -a + m)
            e = baseline + weight * update
            optimal = np.linalg.eigvalsh(e)[-1]
            rayleigh = float(ground @ (e @ ground))
            observed = (optimal - rayleigh) / m**4
            assert observed > 0.0
            errors.append(abs(observed / w_value - 1.0))
            checks += 1
        assert errors[2] < errors[1] < errors[0]
        assert errors[2] < 0.02
        checks += 2
    print(f"SUPPLEMENTARY_QUADRATURE_OK: {checks} assertions")


if __name__ == "__main__":
    finite_check()
