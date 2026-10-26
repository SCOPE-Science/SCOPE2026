"""Finite numerical sanity checks for the weighted-cycle observability theorem.

Requires NumPy. Finite testing complements, and never substitutes for, the proof.
"""
import math
import numpy as np


def laplacian(n, w):
    L = np.zeros((n, n), dtype=float)
    for i in range(n-1):
        L[i, i] += 1
        L[i+1, i+1] += 1
        L[i, i+1] -= 1
        L[i+1, i] -= 1
    L[0, 0] += w
    L[-1, -1] += w
    L[0, -1] -= w
    L[-1, 0] -= w
    return L


def predicted(n, w):
    if n % 6 == 0 or abs(w - 1.) < 1.e-9:
        return False
    for k in range(1, (n - 4)//2 + 1):
        special = 0.5 - math.cos(2 * math.pi * k / (n-3))
        if special > 0 and abs(w-special) < 1.e-9:
            return False
    return True


def observed(n, w):
    eig, vec = np.linalg.eigh(laplacian(n, w))
    # A single symmetric-matrix sensor requires a simple spectrum,
    # and a nonzero sensor component of every normalized eigenvector.
    return bool(np.min(np.diff(eig)) > 1.e-8 and
                np.min(np.abs(vec[1, :])) > 5.e-8)


def main():
    rng = np.random.default_rng(456)
    total = 0
    mismatches = []
    for n in range(5, 37):
        ws = [0.03, 0.1, 0.32, 0.5, 0.8, 1., 1.1, 2., 5., 25.]
        ws += [float(rng.uniform(.01, 4)) for _ in range(10)]
        ws += [s for k in range(1, (n-4)//2+1)
               if (s := .5-math.cos(2*math.pi*k/(n-3))) > 0]
        for w in ws:
            total += 1
            if predicted(n, w) != observed(n, w):
                mismatches.append((n, w))
    print('CASES', total, 'MISMATCHES', len(mismatches))
    if mismatches:
        print('Discrepancies:', mismatches[:20])
        raise AssertionError('Numerical theorem check failed')


if __name__ == '__main__':
    main()
