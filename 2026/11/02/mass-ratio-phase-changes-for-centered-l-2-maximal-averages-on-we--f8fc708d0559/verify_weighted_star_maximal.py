"""Reproduce exact three-point spectral certificates and finite diagnostic checks.

Mathematical proof of arbitrary-size and asymptotic claims is in RESULT.md.
Run: python verify_weighted_star_maximal.py
Dependencies: numpy, sympy.
"""
import itertools
from fractions import Fraction

import numpy as np
import sympy as sp


def selector_matrix(q, h, hub, leaf_modes):
    n = q + 1
    A = np.zeros((n, n), dtype=float)
    mass = np.array([h] + [1.] * q)
    glob = mass / (h + q)
    A[0, :] = np.eye(n)[0, :] if hub == 'I' else glob
    for i, typ in enumerate(leaf_modes, 1):
        if typ == 'I':
            A[i, i] = 1
        elif typ == 'N':
            A[i, 0] = h / (h + 1)
            A[i, i] = 1 / (h + 1)
        elif typ == 'G':
            A[i, :] = glob
        else:
            raise ValueError(typ)
    return A


def weighted_norm2(A, h):
    w = np.array([h] + [1.] * (A.shape[0] - 1))
    B = A * np.sqrt(w[:, None] / w[None, :])
    return np.linalg.svd(B, compute_uv=False)[0] ** 2


def compressed_matrix(q, h, hub, counts):
    """Rows: hub, self leaves, radius-one leaves, global leaves.
    Columns are the same four groups in weighted-orthonormal coordinates.
    Empty leaf groups are deleted in both rows and columns.
    """
    k0, k1, k2 = counts
    assert min(counts) >= 0 and sum(counts) == q
    K = np.array(counts, float)
    B = np.zeros((4, 4))
    if hub == 'I':
        B[0, 0] = 1
    elif hub == 'G':
        B[0, 0] = h / (h + q)
        B[0, 1:] = np.sqrt(h * K) / (h + q)
    else:
        raise ValueError(hub)
    B[1, 1] = 1
    B[2, 0] = np.sqrt(h * k1) / (h + 1)
    B[2, 2] = 1 / (h + 1)
    B[3, 0] = np.sqrt(h * k2) / (h + q)
    B[3, 1:] = np.sqrt(k2 * K) / (h + q)
    keep = [0] + [j + 1 for j in range(3) if counts[j] > 0]
    return B[np.ix_(keep, keep)]


def reduced_norm2(q, h):
    options = []
    for hub in 'IG':
        for k0 in range(q + 1):
            for k1 in range(q - k0 + 1):
                counts = (k0, k1, q - k0 - k1)
                B = compressed_matrix(q, h, hub, counts)
                options.append((np.linalg.svd(B, compute_uv=False)[0] ** 2,
                                hub, counts))
    return max(options)


def exact_selector_three(h, pattern):
    w = sp.Matrix([h, sp.S.One, sp.S.One])
    M = sp.zeros(3)
    full = [w[j] / (h + 2) for j in range(3)]
    if pattern[0] == 'I':
        M[0, 0] = 1
    else:
        for j in range(3):
            M[0, j] = full[j]
    for i in (1, 2):
        if pattern[i] == 'I':
            M[i, i] = 1
        elif pattern[i] == 'N':
            M[i, 0] = h / (h + 1)
            M[i, i] = 1 / (h + 1)
        else:
            for j in range(3):
                M[i, j] = full[j]
    return M


def exact_certificates():
    certs = [
        (sp.Rational(1, 10), 'ING', sp.Rational(1811, 1250), sp.Matrix([13, 4, 1]),
         sp.Poly(53361*sp.Symbol('z')**3-127281*sp.Symbol('z')**2+79300*sp.Symbol('z')-10000)),
        (sp.S.One, 'INN', sp.Rational(31, 20), sp.Matrix([5, 1, 1]),
         sp.Poly(4*sp.Symbol('z')**2-7*sp.Symbol('z')+1)),
        (sp.Integer(100), 'GII', sp.Rational(111, 100), sp.Matrix([1, 9, 9]),
         sp.Poly(2601*sp.Symbol('z')**2-5151*sp.Symbol('z')+2500)),
    ]
    z = sp.Symbol('z')
    for h, winner, threshold, witness, poly in certs:
        W = sp.diag(h, 1, 1)
        mat = exact_selector_three(h, winner)
        rayleigh = sp.cancel((witness.T * mat.T * W * mat * witness)[0]
                             / (witness.T * W * witness)[0])
        assert rayleigh > threshold
        characteristic = sp.factor((z * W - mat.T * W * mat).det() / W.det())
        assert sp.rem(characteristic, poly.as_expr(), z) == 0
        discarded = 0
        for hh, j, k in itertools.product('IG', 'ING', 'ING'):
            pat = hh + j + k
            if pat in (winner, winner[0] + winner[2] + winner[1]):
                continue
            A = exact_selector_three(h, pat)
            positive = threshold * W - A.T * W * A
            for size in (1, 2, 3):
                assert positive[:size, :size].det() > 0, (h, pat, size)
            discarded += 1
        assert discarded >= 16
        print('EXACT_THREE_VERTEX_SELECTOR_SEPARATION_OK', h, winner,
              'bound', threshold, 'witness_ratio', rayleigh)


def phi(t):
    return (2 - t + np.sqrt(t * (4 - 3*t))) / 2


def finite_checks():
    count = 0
    for q in range(2, 7):
        for h in (0.02, 0.1, 1, 3.5, 100):
            a, _, _ = reduced_norm2(q, h)
            b = max(weighted_norm2(selector_matrix(q, h, hub, modes), h)
                    for hub in 'IG' for modes in itertools.product('ING', repeat=q))
            assert abs(a - b) < 5e-12 * max(1, b), (q, h, a, b)
            count += 1
    print('ALL_SELECTOR_COMPRESSION_IDENTITIES_OK', count)

    rng = np.random.default_rng(123456)
    checks = 0
    for q in range(2, 9):
        for h in (0.01, 0.1, 0.7, 1, 5, 50):
            L = reduced_norm2(q, h)[0]
            w = np.array([h] + [1.] * q)
            for _ in range(60):
                f = rng.random(q+1)
                glob = w@f / (h+q)
                z = np.maximum.reduce([f[1:],
                    (h*f[0]+f[1:])/(h+1),np.full(q,glob)])
                y = np.r_[max(f[0],glob),z]
                quotient = np.sum(w*y*y) / np.sum(w*f*f)
                assert quotient <= L + 2e-12, (q,h,quotient,L)
                checks += 1
    print('CENTERED_MAXIMAL_RANDOM_INPUT_BOUNDS_OK',checks)

    for q in (2,3,4,6,9):
        target = max(phi(k/q) for k in range(1,q))
        limit_small = reduced_norm2(q, 1e-9)[0]
        assert abs(limit_small-target)<5e-4, (q,limit_small,target)
        h=1e8
        actual, selector, counts = reduced_norm2(q,h)
        assert selector=='G' and counts==(q,0,0), (q,selector,counts)
        t=q/(h+q)
        assert abs(actual-phi(t))<1e-10
        assert abs((actual-1)/np.sqrt(q/h)-1)<5e-4
    print('SMALL_AND_LARGE_HUB_MASS_LIMIT_DIAGNOSTICS_OK')

if __name__ == '__main__':
    exact_certificates()
    finite_checks()
    print('ALL_WEIGHTED_STAR_MAXIMAL_CHECKS_OK')
