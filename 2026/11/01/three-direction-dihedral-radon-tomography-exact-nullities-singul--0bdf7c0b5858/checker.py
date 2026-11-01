#!/usr/bin/env python3
"""Direct coset-matrix tests of limited-direction dihedral tomography.

The comparisons use incidence matrices built independently of the Fourier
proof. Numeric spectral tests check a finite sample, not the universal theorem.
"""
import math
import numpy as np


def multiply(x, y, n):
    # Canonical coordinate r^j s^t, with s r s = r^{-1}.
    j, t = x
    k, u = y
    return ((j + (1 if t == 0 else -1) * k) % n, (t + u) % 2)


def coset_matrices(n, a):
    elements = [(j, t) for t in (0, 1) for j in range(n)]
    ix = {g: i for i, g in enumerate(elements)}
    groups = [
        [(j, 0) for j in range(n)],
        [(0, 0), (0, 1)],
        [(0, 0), ((-a) % n, 1)],
    ]
    out = []
    for H in groups:
        visited = set()
        rows = []
        for g in elements:
            row_idx = tuple(sorted(ix[multiply(g, h, n)] for h in H))
            if row_idx in visited:
                continue
            visited.add(row_idx)
            row = np.zeros(2 * n, dtype=float)
            row[list(row_idx)] = 1
            rows.append(row)
        out.append(np.stack(rows))
    assert list(map(len, out)) == [2, n, n]
    return out


def formula(n, a, w):
    alpha, beta, gamma = w
    b = beta + gamma
    eigenvalues = [n * alpha + 2 * b, n * alpha]
    for k in range(1, (n - 1) // 2 + 1):
        z = abs(beta + gamma * np.exp(2j * math.pi * k * a / n))
        eigenvalues += [b - z, b - z, b + z, b + z]
    if n % 2 == 0:
        z = abs(beta + gamma * ((-1) ** a))
        eigenvalues += [b - z, b + z]
    assert len(eigenvalues) == 2 * n
    return np.sort(eigenvalues)


def modular_rank(M, prime=1009):
    A = [[int(v) % prime for v in row] for row in M]
    piv = 0
    cols = len(A[0])
    for j in range(cols):
        pivot = next((i for i in range(piv, len(A)) if A[i][j]), None)
        if pivot is None:
            continue
        A[piv], A[pivot] = A[pivot], A[piv]
        inverse = pow(A[piv][j], -1, prime)
        A[piv] = [(inverse * z) % prime for z in A[piv]]
        for i in range(piv + 1, len(A)):
            if A[i][j]:
                mul = A[i][j]
                A[i] = [(v - mul * x) % prime for v, x in zip(A[i], A[piv])]
        piv += 1
        if piv == len(A):
            break
    return piv


def main():
    spectral_tests = 0
    exact_rank_tests = 0
    for n in range(3, 27):
        for a in range(1, n):
            mats = coset_matrices(n, a)
            # Exact finite-field ranks of integer incidence matrices.
            for p in (1009, 1013):
                rank = modular_rank(np.vstack(mats), p)
                assert 2 * n - rank == math.gcd(a, n) - 1
                exact_rank_tests += 1
            weights = [(1., 1., 1.), (.33, .45, 2.1)]
            if math.gcd(a, n) == 1:
                optimal_alpha = 2 * (1 - math.cos(math.pi / n)) / n
                weights.append((optimal_alpha, 1., 1.))
            for w in weights:
                normal = sum(weight * B.T @ B for weight, B in zip(w, mats))
                measured = np.linalg.eigvalsh(normal)
                target = formula(n, a, w)
                assert max(abs(measured - target)) < 2e-10, (n, a, w)
                assert np.count_nonzero(measured < 1e-8) == math.gcd(a, n) - 1
                if math.gcd(a, n) == 1:
                    if w == (1., 1., 1.):
                        assert abs(measured[0] - 2 * (1 - math.cos(math.pi/n))) < 2e-10
                        assert abs(measured[-1] - (n + 4)) < 2e-10
                    elif w[1:] == (1., 1.):
                        sharp = 1 + 2 / (1 - math.cos(math.pi/n))
                        assert abs(measured[-1] / measured[0] - sharp) < 1e-8
                spectral_tests += 1
    limited_tests = 0
    for n in range(3, 17):
        mats = coset_matrices(n, 1)
        for chosen in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
            matrix = np.vstack([mats[i] for i in chosen])
            assert modular_rank(matrix) < 2*n
            limited_tests += 1
    # Test the optimal weights against strictly different reflection ratios.
    comparison_tests = 0
    for n in range(3, 30):
        c = math.cos(math.pi/n)
        optimum = 1 + 2 / (1-c)
        for beta in (.1,.25,.49,.75,1.25,2.,8.):
            gamma = 1.
            b = beta+gamma
            R = math.sqrt(b*b - 4*beta*gamma*math.sin(math.pi/n)**2)
            delta = b-R
            competitor = 1 + 2*b/delta
            assert competitor >= optimum - 2e-10
            comparison_tests += 1
    print(f"PASS: {exact_rank_tests} exact modular rank comparisons")
    print(f"PASS: {spectral_tests} direct Gram-versus-Fourier spectrum comparisons")
    print(f"PASS: {limited_tests} proper direction-subfamily nullity checks")
    print(f"PASS: {comparison_tests} unequal-weight comparisons")
    print("Finite checks are not the proof for general n; see the Fourier/cycle argument.")


if __name__ == '__main__':
    main()
