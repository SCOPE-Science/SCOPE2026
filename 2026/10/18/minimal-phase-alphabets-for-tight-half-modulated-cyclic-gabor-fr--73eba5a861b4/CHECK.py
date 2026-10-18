"""Checks for the finite cyclic Gabor phase-alphabet theorem.

Only finite checks are performed; the universal result is proved in RESULT.md.
Run: python CHECK.py  (requires NumPy).
"""
import itertools
from math import gcd
import numpy as np


def construct(n, k, alphabet):
    m = n // 2
    if k % 2:
        raise ValueError('odd translation count has no tight flat window')
    if m % 2 == 0 and alphabet == 2:
        desired = np.array([(-1) ** j for j in range(m)], complex)
    elif m % 2 == 1 and alphabet in (3, 4):
        h = gcd(m, k // 2)
        if alphabet == 3:
            if h % 3:
                raise ValueError('ternary resonance does not hold')
            omega = np.exp(2j * np.pi / 3)
            first = np.array([1] * (h // 3) + [omega] * (2 * h // 3), complex)
            base = np.concatenate([first, np.conjugate(first)])
        else:
            base = np.array([1j] * h + [-1j] * h)
        desired = base[np.arange(m) % (2 * h)]
    else:
        raise ValueError('invalid construction case')
    return np.concatenate([desired, np.ones(m)]) / np.sqrt(n)


def direct_spectrum(n, k, g):
    x = np.arange(n)
    columns = [np.exp(2j * np.pi * ell * x / n) * np.roll(g, t)
               for ell in range(0, n, 2) for t in range(k)]
    f = np.column_stack(columns)
    return np.linalg.eigvalsh(f @ f.conj().T)


def predicted_extremes(n, k, g):
    m = n // 2
    w = n * g * np.conj(np.roll(g, -m))
    sums = sum(np.roll(w, t) for t in range(k))
    radius = np.max(np.abs(sums))
    return (k - radius) / 2, (k + radius) / 2


def expected_min_order(n, k):
    if k % 2:
        return None
    m = n // 2
    if m % 2 == 0:
        return 2
    return 3 if gcd(m, k // 2) % 3 == 0 else 4


def finite_exhaustive():
    # Entire phase-alphabet space modulo the free half-shift correlations,
    # at small dimensions. No finite enumeration proves the general theorem.
    cases = 0
    for n in (2, 4, 6, 8, 10, 12):
        m = n // 2
        for k in range(1, n + 1):
            for r in (1, 2, 3, 4):
                roots = np.exp(2j * np.pi * np.arange(r) / r)
                exists = False
                for indices in itertools.product(range(r), repeat=m):
                    q = roots[np.array(indices)]
                    w = np.concatenate([q, np.conj(q)])
                    moving = sum(np.roll(w, j) for j in range(k))
                    if np.max(np.abs(moving)) < 1e-10:
                        exists = True
                        break
                if k % 2:
                    expected = False
                elif r == 1:
                    expected = False
                elif r == 2:
                    expected = (m % 2 == 0)
                elif r == 3:
                    d = gcd(n, k)
                    h = d // 2
                    expected = (m // h) % 2 == 1 and h % 3 == 0
                else:  # r == 4; binary or quadrature construction
                    expected = True
                if exists != expected:
                    raise AssertionError((n, k, r, exists, expected))
                cases += 1
    return cases


def main():
    constructions = 0
    spectra = 0
    for n in range(2, 42, 2):
        for k in range(1, n + 1):
            r = expected_min_order(n, k)
            if r is not None:
                g = construct(n, k, r)
                spectrum = direct_spectrum(n, k, g)
                assert np.max(np.abs(spectrum - k / 2)) < 3e-12, (n, k, r)
                constructions += 1
            if k in (1, 2, 3, n // 2, n):
                rng = np.random.default_rng(n * 101 + k)
                g = np.exp(2j * np.pi * rng.random(n)) / np.sqrt(n)
                spec = direct_spectrum(n, k, g)
                lo, hi = predicted_extremes(n, k, g)
                assert abs(spec[0] - lo) < 3e-12, (n, k, 'lo')
                assert abs(spec[-1] - hi) < 3e-12, (n, k, 'hi')
                spectra += 1
    exhaustive = finite_exhaustive()
    print('PASS explicit tight PSK constructions:', constructions)
    print('PASS exact spectral endpoint comparisons:', spectra)
    print('PASS finite exhaustive alphabet cases:', exhaustive)


if __name__ == '__main__':
    main()
