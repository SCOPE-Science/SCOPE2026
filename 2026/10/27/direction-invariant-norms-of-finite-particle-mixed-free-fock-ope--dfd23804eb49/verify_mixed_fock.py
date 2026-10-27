"""Reproduce finite-dimensional tests for mixed free-Fock cutoff norms.

Analytic proofs, not these finite tests, establish the statement for arbitrary
one-particle Hilbert spaces and cutoff orders.

Requires NumPy. Run with: python verify_mixed_fock.py
"""
import math
import numpy as np


def path_matrix(N, a, b):
    B = np.zeros((N + 1, N + 1), dtype=float)
    for j in range(N):
        B[j + 1, j] = a
        B[j, j + 1] = b
    return B


def full_compression(N, u, v):
    d = len(u)
    sizes = [d ** k for k in range(N + 1)]
    offsets = np.cumsum([0] + sizes)
    T = np.zeros((offsets[-1], offsets[-1]), dtype=complex)
    for j in range(N):
        upward = np.kron(u[:, None], np.eye(sizes[j]))
        downward = np.kron(v.conj()[None, :], np.eye(sizes[j]))
        T[offsets[j + 1]:offsets[j + 2], offsets[j]:offsets[j + 1]] = upward
        T[offsets[j]:offsets[j + 1], offsets[j + 1]:offsets[j + 2]] = downward
    return T, offsets


def normalized_pure_chain(j, uhat, vhat, parity):
    if j == 0:
        return np.array([1.0 + 0j])
    sequence = [(uhat if k % 2 else vhat) if parity == 0
                else (vhat if k % 2 else uhat)
                for k in range(1, j + 1)]
    vector = np.array([1.0 + 0j])
    for letter in sequence:
        vector = np.kron(letter, vector)
    return vector


def check(N, u, v):
    a, b = np.linalg.norm(u), np.linalg.norm(v)
    B = path_matrix(N, a, b)
    T, offsets = full_compression(N, u, v)
    norm_T = np.linalg.norm(T, 2)
    norm_B = np.linalg.norm(B, 2)
    assert np.isclose(norm_T, norm_B, atol=3e-11, rtol=3e-11)
    # Exactly verify the scalar finite Jacobi pattern in the norm reduction.
    square = B.T @ B
    for j in range(N + 1):
        expected = (a*a if j < N else 0) + (b*b if j > 0 else 0)
        assert np.isclose(square[j, j], expected, atol=3e-12)
        for k in range(j + 1, N + 1):
            expected = a*b if k == j + 2 else 0
            assert np.isclose(square[j, k], expected, atol=3e-12)
    if a and b:
        uhat, vhat = u/a, v/b
        parity_values = []
        for parity in (0, 1):
            cols = list(range(parity, N+1, 2))
            if not cols:
                continue
            sub = B[:, cols]
            gram = sub.T @ sub
            vals, vecs = np.linalg.eigh(gram)
            coefficients = np.abs(vecs[:, -1])
            coefficients = coefficients / np.linalg.norm(coefficients)
            x = np.zeros(offsets[-1], dtype=complex)
            for col, coefficient in zip(cols, coefficients):
                chain = normalized_pure_chain(col, uhat, vhat, parity)
                x[offsets[col]:offsets[col+1]] = coefficient * chain
            assert np.isclose(np.linalg.norm(x), 1, atol=2e-12)
            actual = np.linalg.norm(T @ x)
            predicted = np.linalg.norm(sub @ coefficients)
            assert np.isclose(actual, predicted, atol=5e-11, rtol=5e-11)
            assert np.isclose(predicted, np.sqrt(max(vals[-1],0)), atol=5e-11)
            parity_values.append(actual)
        assert np.isclose(max(parity_values), norm_T, atol=5e-11, rtol=5e-11)
    return 1


def main():
    rng = np.random.default_rng(20261024)
    test_cases = 0
    for d, orders, reps in [(1, range(1, 8), 3),
                            (2, range(1, 6), 12),
                            (3, range(1, 5), 7)]:
        for N in orders:
            for k in range(reps):
                u = rng.normal(size=d) + 1j * rng.normal(size=d)
                v = rng.normal(size=d) + 1j * rng.normal(size=d)
                if k == 0:
                    v = u.copy()
                elif k == 1:
                    v = -u.copy()
                elif k == 2 and d > 1:
                    v = u[::-1].copy()
                test_cases += check(N, u, v)
    edge_cases = 0
    for N in range(1, 9):
        for a, b in [(0, 0), (0, 3), (2, 0), (1, 1), (3, 5)]:
            B = path_matrix(N, a, b)
            if a == b:
                expected = 2 * a * math.cos(math.pi / (N+2))
                assert np.isclose(np.linalg.norm(B, 2), expected, atol=4e-12)
            if a == 0 or b == 0:
                assert np.isclose(np.linalg.norm(B, 2), max(a,b), atol=3e-12)
            edge_cases += 1
    for N in range(1, 81):
        B = path_matrix(N, 1, 1)
        expected = 2*math.cos(math.pi/(N+2))
        assert np.isclose(np.linalg.norm(B,2), expected, atol=8e-12)
        assert np.isclose(2-expected,4*math.sin(math.pi/(2*(N+2)))**2,atol=1e-14)
    print(f"PASS: {test_cases} mixed-vector finite-Fock norm/chain checks, "
          f"{edge_cases} degenerate/weighted path checks, "
          "80 balanced path and deficit checks.")


if __name__ == '__main__':
    main()
