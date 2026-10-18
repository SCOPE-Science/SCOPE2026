"""Finite consistency checks for ancestor-Cesaro singular spectra on regular trees.

Usage: python checker.py
Requires NumPy; does not numerically certify asymptotic statements.
"""
import math
import numpy as np

checks = 0

def verify(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)


def vertices(b, depth):
    levels = [[()]]
    for _ in range(depth):
        levels.append([v + (c,) for v in levels[-1] for c in range(b)])
    return [v for layer in levels for v in layer]


def direct_matrix(b, N):
    vv = vertices(b, N)
    index = {v: i for i, v in enumerate(vv)}
    mat = np.zeros((len(vv), len(vv)))
    for row, v in enumerate(vv):
        for k in range(len(v) + 1):
            mat[row, index[v[:k]]] = 1.0 / (len(v) + 1)
    return mat


def radial_matrix(b, N):
    return np.array([[b ** ((j-k)/2.0) / (j+1) if k <= j else 0.0
                      for k in range(N+1)] for j in range(N+1)])


def block_singulars(b, N):
    a = radial_matrix(b, N)
    spectra = [np.linalg.svd(a, compute_uv=False)]
    for k in range(1, N+1):
        v = np.linalg.svd(a[k:, k:], compute_uv=False)
        spectra.extend([v] * ((b-1)*b**(k-1)))
    return np.sort(np.concatenate(spectra))[::-1]


for b, depthmax in [(2, 6), (3, 4), (4, 3)]:
    for N in range(0, depthmax+1):
        direct = np.linalg.svd(direct_matrix(b, N), compute_uv=False)
        blocks = block_singulars(b, N)
        verify(len(direct)==len(blocks), f"dimension b={b}, N={N}")
        verify(np.allclose(direct, blocks, rtol=1e-10, atol=1e-10),
               f"all singular values b={b}, N={N}")
        a = radial_matrix(b, N)
        verify(abs(direct[0] - np.linalg.svd(a, compute_uv=False)[0])<1e-10,
               f"radial norm b={b}, N={N}")
        if N>=1:
            verify(direct[0] > np.linalg.svd(a[1:, 1:], compute_uv=False)[0],
                   f"strict top singular b={b}, N={N}")

for b in (2, 3, 5):
    for N in (40, 80, 120):
        a = radial_matrix(b, N)
        normalization = (N+1)*b**(-N/2)
        top = np.linalg.svd(a, compute_uv=False)[:2]*normalization
        lim = b/(b-1)
        verify(abs(top[0]-lim) < 0.2, f"top limiting scale b={b}, N={N}")
        verify(top[1] < 0.02, f"second radial singular vanishes b={b}, N={N}")
        for k in range(1, min(4, N+1)):
            sv = np.linalg.svd(a[k:, k:], compute_uv=False)[:2]*normalization
            verify(abs(sv[0]-lim*b**(-k/2)) < 0.2,
                   f"wavelet block leading scale b={b}, k={k}, N={N}")
            verify(sv[1] < 0.02,
                   f"wavelet block second singular b={b}, k={k}, N={N}")

print(f"PASS: {checks} finite consistency assertions")
