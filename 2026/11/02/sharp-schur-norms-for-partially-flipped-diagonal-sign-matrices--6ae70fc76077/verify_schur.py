"""Supplementary finite checks for partial diagonal sign-reflection Schur norms.

Requires NumPy. The finite calculations do not prove the all-size theorem;
the proof is contained in the accompanying mathematical note.
"""
import math
import numpy as np


def target(k, extended):
    if k == 0 or (not extended and k == 1):
        return 1.0
    if not extended:
        return 3 - 4 / k
    if k <= 5:
        return 1 + k / (1 + math.sqrt(2 * k))
    return 3 - 4 / k


def sign_matrix(k, extended=True):
    n = k + int(extended)
    M = np.ones((n, n))
    M[np.arange(k), np.arange(k)] = -1
    return M


def certificate(k):
    T = target(k, True)
    if k == 1:
        P = T * np.eye(2)
    else:
        s = T - 1
        v = (k - 1) * s / k if k <= 5 else 1.0
        P = np.empty((k + 1, k + 1), float)
        P[:k, :k] = (T - 2) * np.ones((k, k)) + 2 * np.eye(k)
        P[:k, k] = P[k, :k] = v
        P[k, k] = T
    return P


def witness(k):
    a = ((k + (k - 1) * math.sqrt(2 * k)) /
         (2 * (2 * k - 1))) if k <= 5 else 1.0
    u = np.r_[np.full(k, math.sqrt(a / k)), math.sqrt(max(0, 1 - a))]
    M = sign_matrix(k)
    B = np.diag(u) @ M @ np.diag(u)
    vals, vecs = np.linalg.eigh(B)
    # Spectral sign, with the zero eigenspace mapped to zero.
    A = (vecs * np.sign(vals)) @ vecs.T
    score = u @ (M * A) @ u
    return score, float(np.sum(np.abs(vals)))


def main():
    count = 0
    for k in range(1, 101):
        M = sign_matrix(k)
        T = target(k, True)
        P = certificate(k)
        assert np.max(abs(np.diag(P) - T)) < 1e-12
        for Z in (P + M, P - M):
            assert np.min(np.linalg.eigvalsh(Z)) >= -5e-11, (k, np.min(np.linalg.eigvalsh(Z)))
            count += 1
        score, tr = witness(k)
        assert abs(score - tr) < 2e-11
        assert abs(score - T) < 2e-11, (k, score, T)
        count += 2
        if k >= 2:
            Mk = sign_matrix(k, extended=False)
            Tc = target(k, False)
            Pc = 2 * np.eye(k) + (Tc - 2) * np.ones((k, k))
            assert abs(np.min(np.linalg.eigvalsh(Pc + Mk))) < 2e-10
            assert abs(np.min(np.linalg.eigvalsh(Pc - Mk))) < 2e-10
            assert min(np.min(np.linalg.eigvalsh(Pc + Mk)), np.min(np.linalg.eigvalsh(Pc - Mk))) > -5e-11
            eig = np.linalg.eigvalsh(Mk / k)
            assert abs(np.sum(abs(eig)) - Tc) < 2e-11
            count += 4
    # Distinguish the strict raising phase from the eventual stabilization.
    for k in range(2, 101):
        if k <= 5:
            assert target(k, True) > target(k, False) + 1e-6
        else:
            assert abs(target(k, True) - target(k, False)) < 1e-13
        count += 1
    print(f"PASS: {count} finite numerical assertions; checked k=1..100.")


if __name__ == "__main__":
    main()
