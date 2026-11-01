#!/usr/bin/env python3
"""Self-contained checks of the finite-colouring Fourier spectrum and its limits.

Only numpy and scipy are required. Finite checks supplement the written proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import cos, pi, sqrt
import numpy as np
from scipy.linalg import eigh_tridiagonal

CHECKS = 0

def close(x, y, tol=1e-9):
    global CHECKS
    CHECKS += 1
    if not np.allclose(x, y, rtol=tol, atol=tol):
        raise AssertionError(f"Mismatch: {x} versus {y}")


def parent_depth(b, h):
    parent = [-1]
    depth = [0]
    cursor = 0
    for level in range(h):
        level_nodes = [i for i, dep in enumerate(depth) if dep == level]
        for i in level_nodes:
            for _ in range(b):
                parent.append(i)
                depth.append(level + 1)
    return parent, depth


def vertices_kernel(parent, depth, a):
    n = len(parent)
    paths = []
    for v in range(n):
        chain = set()
        w = v
        while w >= 0:
            chain.add(w)
            w = parent[w]
        paths.append(chain)
    K = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            z = max(paths[i] & paths[j], key=lambda x: depth[x])
            K[i, j] = a ** (depth[i] + depth[j] - 2 * depth[z])
    return K


def radial_block(b, h, a):
    t = sqrt(b) * a
    diag = np.array([1 + (b - 1) * a * a] + [1 + t * t] * (h - 1) + [1.0])
    off = np.repeat(-t, h)
    return diag, off


def contrast_block(m, t):
    return (np.array([1.0 + t * t] * (m - 1) + [1.0]), np.repeat(-t, m - 1))


def spectrum_blocks(b, h, a):
    t = sqrt(b) * a
    dr, er = radial_block(b, h, a)
    values = list((1 - a * a) / eigh_tridiagonal(dr, er, eigvals_only=True))
    for ell in range(h):
        mult = (b - 1) * (b ** ell)
        dc, ec = contrast_block(h - ell, t)
        for eig in eigh_tridiagonal(dc, ec, eigvals_only=True):
            values.extend([(1 - a * a) / eig] * mult)
    return np.sort(np.array(values))


def exact_kernel_inverse(parent, depth, q):
    global CHECKS
    a = Fraction(1, q - 1)
    n = len(parent)
    paths = []
    for v in range(n):
        s = set()
        while v >= 0:
            s.add(v)
            v = parent[v]
        paths.append(s)
    K = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    # Depth of LCA is maximal among common ancestors.
    for i in range(n):
        for j in range(n):
            lca = max(paths[i] & paths[j], key=lambda x: depth[x])
            K[i][j] = a ** (depth[i] + depth[j] - 2 * depth[lca])
    Q = [[Fraction(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        d = sum(1 for j in range(n) if parent[j] == i) + int(parent[i] >= 0)
        Q[i][i] = 1 + a * a * (d - 1)
        if parent[i] >= 0:
            Q[i][parent[i]] = -a
            Q[parent[i]][i] = -a
    for i in range(n):
        for j in range(n):
            prod = sum(K[i][k] * Q[k][j] for k in range(n))
            CHECKS += 1
            assert prod == (1 - a * a if i == j else 0)


def coloring_gram(parent, q):
    n = len(parent)
    columns = [np.ones(1, dtype=complex)]
    all_colors = []
    for root in range(q):
        for labels in product(range(q - 1), repeat=n - 1):
            colors = [root]
            for v in range(1, n):
                p = colors[parent[v]]
                colors.append((p + 1 + labels[v - 1]) % q)
            all_colors.append(colors)
    X = np.array(all_colors, dtype=float)
    functions = [np.ones(len(X), dtype=complex)]
    for freq in range(1, q):
        for v in range(n):
            functions.append(np.exp(2j * pi * freq * X[:, v] / q))
    F = np.stack(functions, axis=1)
    return (F.conj().T @ F) / len(X), len(X)


def checks_small():
    for b, q, h in [(2, 3, 1), (2, 3, 2), (2, 4, 2), (3, 3, 1), (3, 3, 2),
                    (4, 3, 1), (4, 3, 2), (5, 3, 1), (9, 4, 1)]:
        parent, depth = parent_depth(b, h)
        n = len(parent)
        a = 1 / (q - 1)
        K = vertices_kernel(parent, depth, a)
        Q = np.diag([1 + (sum(p == i for p in parent[1:]) + int(parent[i] >= 0) - 1) * a * a
                     for i in range(n)])
        for v in range(1, n):
            Q[parent[v], v] = Q[v, parent[v]] = -a
        close(K @ Q, np.eye(n) * (1 - a * a), 1e-11)
        expected = spectrum_blocks(b, h, a)
        actual = np.sort(np.linalg.eigvalsh(K))
        close(actual, expected, 1e-9)
        dr, er = radial_block(b, h, a)
        evr = eigh_tridiagonal(dr, er, eigvals_only=True)
        close(actual[0], (1 - a * a) / evr[-1], 1e-8)
        close(actual[-1], (1 - a * a) / evr[0], 1e-8)
        close(np.prod(evr), 1 - a * a, 1e-8)
        if (b, q, h) in [(2, 3, 1), (2, 3, 2), (2, 4, 2), (3, 3, 1), (3, 3, 2)]:
            G, sample_count = coloring_gram(parent, q)
            assert sample_count == q * ((q - 1) ** (n - 1))
            block = np.zeros((1 + (q - 1) * n, 1 + (q - 1) * n), dtype=complex)
            block[0, 0] = 1
            sign = np.array([(-1)**d for d in depth])
            signed = K * np.outer(sign, sign)
            for freq in range(q - 1):
                idx = slice(1 + n * freq, 1 + n * (freq + 1))
                block[idx, idx] = signed
            close(G, block, 1e-10)
            close(np.sort(np.linalg.eigvalsh(G)),
                  np.sort(np.r_[1.0, np.tile(expected, q-1)]), 1e-8)
    for b, q, h in [(2, 3, 2), (4, 3, 2), (3, 4, 2)]:
        p, d = parent_depth(b, h)
        exact_kernel_inverse(p, d, q)


def checks_asymptotics():
    for b, q, h in [(2, 3, 160), (3, 4, 160), (2, 4, 160)]:
        a = 1/(q-1)
        t = sqrt(b)*a
        dr, er = radial_block(b, h, a)
        vals = eigh_tridiagonal(dr, er, eigvals_only=True)
        close(vals[0], (1-t)**2, tol=2e-3)
        close(vals[-1], (1+t)**2, tol=2e-3)
        close(vals[-1]/vals[0], ((1+t)/(1-t))**2, tol=6e-3)
    for b, q in [(4, 3), (9, 4)]:
        a = 1 / (q-1)
        for h in [120, 240, 480]:
            d, e = radial_block(b, h, a)
            vals = eigh_tridiagonal(d, e, eigvals_only=True)
            close(h*h*vals[0], pi*pi/4, tol=.05)
            close(vals[-1], 4.0, tol=.025)
            close((vals[-1]/vals[0])/(h*h), 16/pi**2, tol=.06)
    for b, q in [(5, 3), (10, 4), (16, 3)]:
        a = 1/(q-1)
        t = sqrt(b)*a
        u = t*t
        A = u*(u-a*a) / ((1-a*a) * (u-1)**2)
        for h in [40, 80, 120]:
            T = sum(u**k for k in range(h+1))/(1-a*a) + sum((h-k)*u**k for k in range(h))
            close(T/u**h, A, tol=.07 if h == 40 else .003 if h == 80 else .001)
        for h in [8, 12, 16]:
            d, e = radial_block(b, h, a)
            vals = eigh_tridiagonal(d, e, eigvals_only=True)
            T = sum(u**k for k in range(h+1))/(1-a*a) + sum((h-k)*u**k for k in range(h))
            close(T, np.sum(1/vals), tol=.002)
            close(vals[-1], (1+t)**2, tol=.15)
            if b == 16 and h == 12:
                close(vals[0] * T, 1, tol=.01)

if __name__ == '__main__':
    checks_small()
    checks_asymptotics()
    print(f'PASS: {CHECKS} reproducible assertions')
