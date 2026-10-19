"""Independent dense-matrix checks of the coupled-prime-prism trapping theorem.

These are finite corroborations, not a proof for arbitrary prime size.
"""
import math
import numpy as np
from scipy.linalg import eigh, expm


def hamiltonian(p, g, t):
    h = np.zeros((2 * p, 2 * p), dtype=float)
    for layer in range(2):
        for j in range(p):
            a = layer * p + j
            b = layer * p + ((j + 1) % p)
            h[a, b] = g
            h[b, a] = g
    for j in range(p):
        h[j, j + p] = t
        h[j + p, j] = t
    return h


def dense_dark_survival(p, g, t):
    lam, vec = eigh(hamiltonian(p, g, t))
    sink = np.zeros(2 * p)
    start = np.zeros(2 * p)
    sink[0] = 1
    start[p] = 1
    capture = 0.0
    i = 0
    while i < 2 * p:
        j = i + 1
        while j < 2 * p and abs(lam[j] - lam[i]) < 1.e-8:
            j += 1
        sub = vec[:, i:j]
        a = sub.T @ sink
        b = sub.T @ start
        if float(a @ a) > 1.e-12:
            capture += float((a @ b) ** 2 / (a @ a))
        i = j
    return 1.0 - capture


def exceptional_values(p, g):
    c = [math.cos(2 * math.pi * a / p) for a in range((p + 1) // 2)]
    return [(abs(g) * (c[a] - c[b]), a, b)
            for a in range(len(c)) for b in range(a + 1, len(c))]


def main():
    cases = 0
    max_err = 0.0
    for p in [3, 5, 7, 11, 13, 17]:
        for g in [1.3, -0.71]:
            es = exceptional_values(p, g)
            assert len(es) == (p * p - 1) // 8
            for i, (t, a, b) in enumerate(es):
                assert all(abs(t - other[0]) > 1.e-7
                           for j, other in enumerate(es) if i != j)
                want = (4.0 / (3 * p)) if a == 0 else (2.0 / p)
                got = dense_dark_survival(p, g, t)
                max_err = max(max_err, abs(got - want))
                assert abs(got - want) < 2.e-10, (p, g, a, b, got, want)
                cases += 1
            for t in [0.109123 * abs(g), 0.741257 * abs(g), abs(g),
                      2.5 * abs(g)]:
                assert all(abs(t - val[0]) > 1.e-6 for val in es)
                got = dense_dark_survival(p, g, t)
                max_err = max(max_err, abs(got))
                assert abs(got) < 2.e-10, (p, g, t, got)
                cases += 1

    # Direct non-Hermitian propagation checks.  The asymptotic projection
    # is verified independently of the dense eigenspace algorithm.
    dynamics = 0
    for p in [3, 5]:
        for t, a, b in exceptional_values(p, 1.1)[:2]:
            h = hamiltonian(p, 1.1, t).astype(complex)
            h[0, 0] -= 0.5j * 0.8
            v = np.zeros(2 * p, dtype=complex)
            v[p] = 1
            for time in [400.0, 1600.0]:
                q = expm(-1j * h * time) @ v
                got = float(np.real(np.vdot(q, q)))
                want = dense_dark_survival(p, 1.1, t)
                assert abs(got - want) < 5.e-5, (p, t, time, got, want)
                dynamics += 1

    print(f"VERIFY_OK dense_spectral_cases={cases} nonhermitian_checks={dynamics} "
          f"max_dense_error={max_err:.3e}")


if __name__ == '__main__':
    main()
