#!/usr/bin/env python3
"""Finite reproducibility checks for two distinguishable reacting walkers on a star.
This file is an ordinary numerical corroboration, not a proof for arbitrary L.
"""
import numpy as np
from scipy.linalg import eigh, expm, svd


def model(L, a, b):
    n = L + 1
    adjacency = np.zeros((n, n), dtype=float)
    adjacency[0, 1:] = adjacency[1:, 0] = 1.
    return a * np.kron(adjacency, np.eye(n)) + b * np.kron(np.eye(n), adjacency)


def spectral_bright(H, L):
    n = L + 1
    eigenvalues, eigenvectors = eigh(H)
    sinks = [i * n + i for i in range(n)]
    bright = np.zeros_like(H)
    rank = 0
    groups = []
    for i, val in enumerate(eigenvalues):
        if i == 0 or abs(val - eigenvalues[groups[-1][-1]]) > 1.e-7:
            groups.append([i])
        else:
            groups[-1].append(i)
    for inds in groups:
        E = eigenvectors[:, inds]
        overlaps = E[sinks, :]
        _u, singular, adjoint = svd(overlaps, full_matrices=False)
        r = np.count_nonzero(singular > 1.e-8)
        if r:
            V = E @ adjoint[:r, :].conj().T
            bright += V @ V.conj().T
            rank += int(r)
    return bright, rank


def prediction(L, equal):
    n = L + 1
    out = np.ones((n, n))
    out[0, 1:] = out[1:, 0] = .5 if equal else 1.
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                out[i, j] = (1. / (L-1) if equal else (2*L-1) / (L*(L-1)))
    return out, (3 * L + 1 if equal else 5 * L)


def run():
    cases = 0
    entries = 0
    projectors = 0
    for L in range(3, 8):
        for a, b in [(1., 1.), (1., 1.4), (1., 2.), (2., 1.), (1., 3.)]:
            H = model(L, a, b)
            P, rank = spectral_bright(H, L)
            expected, dim = prediction(L, abs(a - b) < 1.e-12)
            actual = np.diag(P).reshape(L+1, L+1)
            assert rank == dim, (L, a, b, rank, dim)
            assert np.max(abs(actual-expected)) < 1.e-8, (L, a, b, np.max(abs(actual-expected)))
            assert np.linalg.norm(P@P-P) < 1.e-7
            cases += 1
            entries += (L+1)**2
            projectors += 1
    loss_tests = 0
    for L in (3, 4):
        for a, b in ((1., 1.), (1., 1.7)):
            n = L + 1
            H = model(L, a, b)
            rates = np.array([.7, 1.3, 1.9] + [1.1] * max(0,n-3))
            K = np.zeros_like(H)
            for j in range(n):
                K[j*n+j, j*n+j] = rates[j] / 2.
            evolution = expm((-1.j*H-K)*3000.)
            P, _ = spectral_bright(H, L)
            for i, j in ((0,1), (1,2), (0,0)):
                col = i*n+j
                survival = np.linalg.norm(evolution[:, col])**2
                target = 1.-P[col,col]
                assert abs(survival-target) < 2.e-5, (L,a,b,i,j,survival,target)
                loss_tests += 1
    print('VERIFY_OK spectral_cases=%d sitewise_probabilities=%d projector_idempotence=%d loss_dynamics=%d' %
          (cases, entries, projectors, loss_tests))


if __name__ == '__main__':
    run()
