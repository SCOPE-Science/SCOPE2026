"""Reproducible finite checks for model-space compressed powers (NumPy >=1.24).

This checks finite sample calculations only; the universal statements use the proof.
Run: python CHECK.py
"""
import numpy as np


def taylor_from_zeros(zeros, order):
    numerator = np.array([1.0 + 0j])
    denominator = np.array([1.0 + 0j])
    for a in zeros:
        numerator = np.convolve(numerator, np.array([-a, 1.0 + 0j]))
        denominator = np.convolve(denominator, np.array([1.0 + 0j, -np.conj(a)]))
    out = []
    for j in range(order):
        value = (numerator[j] if j < len(numerator) else 0j)
        value -= sum(denominator[i] * out[j - i]
                     for i in range(1, min(j, len(denominator) - 1) + 1))
        out.append(value)
    return np.array(out, dtype=complex)


def compressed_adjoint(zeros):
    # Eigenfunctions of the backward shift: k_a(z)=(1-conj(a)z)^(-1).
    # The Gram matrix is G_ij = (k_aj,k_ai), in this array convention.
    z = np.array(zeros, dtype=complex)
    g = 1.0 / (1.0 - z[:, None] * z[None, :].conj())
    eigenvalues, u = np.linalg.eigh(g)
    assert min(eigenvalues) > 1e-8, "Use distinct well-spaced zeros."
    sqrt_g = (u * np.sqrt(eigenvalues)) @ u.conj().T
    inverse_sqrt_g = (u / np.sqrt(eigenvalues)) @ u.conj().T
    return sqrt_g @ np.diag(z.conj()) @ inverse_sqrt_g


def check_case(zeros, expected_flat=None):
    n = len(zeros)
    t = compressed_adjoint(zeros)
    coeff = taylor_from_zeros(zeros, n)
    r = abs(coeff[0])
    assert 0 < r < 1
    tests = 0
    for k in range(1, n + 1):
        singular = np.linalg.svd(np.linalg.matrix_power(t, k), compute_uv=False)
        predicted_sq = n - k + k * r**2 + sum(
            (k - j) * abs(coeff[j])**2 for j in range(1, k))
        np.testing.assert_allclose(sum(singular**2), predicted_sq,
                                   rtol=3e-10, atol=3e-10)
        tests += 1
        for p in (0.5, 1.0, 2.0, 3.5, 5.0):
            assert sum(singular**p) >= n - k + k * r**p - 3e-9
            tests += 1
        if expected_flat is not None and k == expected_flat:
            assert max(abs(coeff[1:k]), default=0.0) < 2e-9
            np.testing.assert_allclose(np.sort(singular),
                                       np.sort([r] * k + [1.0] * (n - k)),
                                       atol=3e-9, rtol=3e-9)
            tests += 1
        if k > 1 and max(abs(coeff[1:k])) > 1e-4:
            assert sum(singular) > n - k + k * r + 1e-8
            tests += 1
    return tests


def zeros_with_flat_jet(k, b, u, eta):
    # B(z)=(b + eta*z^k*(z-u)/(1-conj(u)z))
    #      /(1 + conj(b)*eta*z^k*(z-u)/(1-conj(u)z)).
    # Zeros come from b*(1-conj(u)z)+eta*z^k*(z-u).
    coeff = np.zeros(k + 2, dtype=complex)
    coeff[0] = b
    coeff[1] = -b * np.conj(u)
    coeff[k] += -eta * u
    coeff[k + 1] += eta
    z = np.roots(coeff[::-1])
    assert max(abs(z)) < 1 - 1e-6
    return z


def main():
    count = 0
    generic = (
        [0.19, -0.46],
        [0.15 + 0.13j, -0.45 + 0.12j, 0.50 - 0.24j],
        [0.20, -0.34, 0.46 + 0.17j, -0.53 + 0.06j],
        [0.16, 0.42j, -0.37, -0.45j, 0.53],
        [0.15, -0.28, 0.38j, -0.45j, 0.51, -0.56],
    )
    for zeros in generic:
        count += check_case(zeros)
    for k in (2, 3, 4):
        zeros = zeros_with_flat_jet(k, 0.17 + 0.08j, 0.31 - 0.11j,
                                    np.exp(0.29j))
        count += check_case(zeros, expected_flat=k)
    for n in (2, 3, 4, 5, 6):
        b = 0.14 + 0.12j
        eta = np.exp(0.37j)
        radius = abs(b)**(1.0 / n)
        phase = np.angle(-b / eta) / n
        roots = [radius * np.exp(1j * (phase + 2 * np.pi * j / n))
                 for j in range(n)]
        count += check_case(roots, expected_flat=n)
    print(f"PASS: {count} finite identities, bounds, or equality tests; "
          "no finite test substitutes for the analytical proof.")


if __name__ == "__main__":
    main()
