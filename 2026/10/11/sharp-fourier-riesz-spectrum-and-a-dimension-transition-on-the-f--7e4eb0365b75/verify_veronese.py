#!/usr/bin/env python3
"""Independent small-field and symbolic checks of the rank-one symmetric Fourier-frame theorem.

Requires numpy and sympy. Uses direct finite-field Fourier summation, not spectral entry formulas,
for q=3,5,7,9 and m=4, plus q=3 and m=5.
"""
import itertools
import math
import numpy as np
import sympy as sp


def field(q):
    if q == 9:
        def mul(x, y):
            a, b = x % 3, x // 3
            c, d = y % 3, y // 3
            return ((a * c - b * d) % 3) + 3 * ((a * d + b * c) % 3)
        def phase(x):
            return np.exp(2j * np.pi * ((2 * (x % 3)) % 3) / 3)
    else:
        def mul(x, y):
            return (x * y) % q
        def phase(x):
            return np.exp(2j * np.pi * x / q)
    return mul, phase


def parameters(q, m):
    Q = q ** m
    N = Q + 1
    E = m * (m - 1) // 2
    u = (1 + q ** (m - 1)) / N
    v = (1 + q ** (m - 2)) / N
    a, b, c = 1 + (q - 2) * u, (q - 1) * u, (q - 1) * v
    R = a + 2 * (m - 2) * b + ((m - 2) * (m - 3) // 2) * c
    h = math.sqrt(E * (q - 1)) * u
    low, high = np.linalg.eigvalsh(np.array([[1, h], [h, R]], float))
    return (1 - u, (a - c) + (m - 4) * (b - c), a - 2 * b + c, low, high)


def independent_test(q, m):
    mul, phase = field(q)
    edges = list(itertools.combinations(range(m), 2))
    freqs = [(e, a) for e in edges for a in range(1, q)]
    vectors = itertools.product(range(q), repeat=m)
    mat = np.empty((q ** m, len(freqs) + 1), dtype=complex)
    for index, x in enumerate(vectors):
        mat[index, 0] = 1
        mat[index, 1:] = [phase(mul(a, mul(x[e[0]], x[e[1]]))) for e, a in freqs]
    G = (mat.conj().T @ mat + 1) / (q ** m + 1)
    lam_variation, lam_star, lam_cycle, lam_low, lam_high = parameters(q, m)
    E = len(edges)
    expected = ([lam_variation] * (E * (q - 2))
                + [lam_star] * (m - 1)
                + [lam_cycle] * (E - m)
                + [lam_low, lam_high])
    actual = np.linalg.eigvalsh(G)
    deviation = max(abs(x - y) for x, y in zip(sorted(expected), actual))
    assert deviation < 2e-10, (q, m, deviation)
    assert actual[0] > 0, (q, m, actual[0])
    # Verify three eigenspaces directly, not only the characteristic polynomial.
    edge_count = len(edges)
    edge_to_index = {e: idx for idx, e in enumerate(edges)}
    vec = np.zeros(len(freqs) + 1, complex)
    vec[1] = 1
    vec[2] = -1
    assert np.linalg.norm(G @ vec - lam_variation * vec) < 2e-10
    vec = np.zeros(len(freqs) + 1, complex)
    w = [1, -1] + [0] * (m - 2)
    for idx, (i, j) in enumerate(edges):
        vec[1 + idx * (q - 1):1 + (idx + 1) * (q - 1)] = w[i] + w[j]
    assert np.linalg.norm(G @ vec - lam_star * vec) < 2e-10
    if m >= 4:
        vec = np.zeros(len(freqs) + 1, complex)
        weights = {(0, 1): 1, (2, 3): 1, (0, 2): -1, (1, 3): -1}
        for e, wt in weights.items():
            idx = edge_to_index[e]
            vec[1 + idx * (q - 1):1 + (idx + 1) * (q - 1)] = wt
        assert np.linalg.norm(G @ vec - lam_cycle * vec) < 2e-10
    return len(freqs) + 1, deviation


def symbolic_test():
    q, m, z = sp.symbols('q m z')
    D = q ** 2 * z + 1
    u, v = (1 + q * z) / D, (1 + z) / D
    E = m * (m - 1) / 2
    a, b, c = 1 + (q - 2) * u, (q - 1) * u, (q - 1) * v
    R = a + 2 * (m - 2) * b + (m - 2) * (m - 3) * c / 2
    h_squared = E * (q - 1) * u ** 2
    cyc = (q - 1) * z / D
    test = sp.factor(((1 - cyc) * (R - cyc) - h_squared) * D ** 2)
    answer = z * (m - 1) * (q - 1) ** 2 * (m * (q - 2) + 4 + z * (4 * (q ** 2 - q + 1) - m)) / 2
    assert sp.simplify(test - answer) == 0
    assert sp.simplify((a - 2 * b + c) - cyc) == 0
    assert sp.simplify(((a - c) + (m - 4) * (b - c)) -
                       z * (q - 1) * (m * (q - 1) - 2 * q + 3) / D) == 0
    for qq in [3, 5, 7, 9, 11]:
        m0 = 4 * (qq * qq - qq + 1)
        def sign_value(mm):
            return mm * (qq - 2) + 4 + qq ** (mm - 2) * (m0 - mm)
        assert sign_value(m0) > 0 and sign_value(m0 + 1) < 0
        assert sign_value(m0 + 2) < 0
    return 'symbolic_factor_and_integer_threshold=PASS'


if __name__ == '__main__':
    print(symbolic_test())
    cases = [(3, 4), (3, 5), (5, 4), (7, 4), (9, 4)]
    tests = [independent_test(q, m) for q, m in cases]
    print('VERIFY_OK cases=', cases, 'total_columns=', sum(x for x, _ in tests),
          'max_direct_spectral_error=', max(e for _, e in tests),
          'Johnson_eigenspaces=PASS direct_finite_field_character_sums=PASS')
