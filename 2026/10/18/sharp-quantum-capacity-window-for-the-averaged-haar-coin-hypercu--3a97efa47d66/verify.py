"""Finite checks for the hypercube dephasing-channel capacity profile.

Run with Python 3, NumPy, and SciPy: python verify.py.
The infinite-dimensional asymptotic and quantum-capacity theorem require the
proof; finite computations here do not establish their universal validity.
"""
import itertools
import math
from collections import defaultdict

import numpy as np
from scipy.special import gammaln


def radial_law(d, t):
    """Distribution of Hamming weight for the discrete-time coordinate-flip walk."""
    assert d >= 1 and t >= 0
    q = np.zeros(d + 1)
    q[0] = 1.0
    for _ in range(t):
        v = np.zeros_like(q)
        for w, a in enumerate(q):
            if w < d:
                v[w + 1] += a * (d - w) / d
            if w > 0:
                v[w - 1] += a * w / d
        q = v
    return q


def capacity_from_radial(d, t):
    if t == 0:
        return float(d)
    rw = radial_law(d, t)
    ws = np.arange(d + 1)
    log_stationary = (gammaln(d + 1) - gammaln(ws + 1)
                      - gammaln(d - ws + 1) - (d - 1) * math.log(2))
    live = rw > 0
    dkl_nats = np.sum(rw[live] * (np.log(rw[live]) - log_stationary[live]))
    return 1 + float(dkl_nats) / math.log(2)


def full_error_law(d, t):
    p = np.zeros(1 << d)
    p[0] = 1
    for _ in range(t):
        q = np.zeros_like(p)
        for j in range(d):
            q += p[np.arange(1 << d) ^ (1 << j)] / d
        p = q
    return p


def exact_integer_counts(d, t):
    """Independent integer count of all length-t coordinate-flip words."""
    counts = [0] * (1 << d)
    counts[0] = 1
    for _ in range(t):
        nxt = [0] * (1 << d)
        for mask, count in enumerate(counts):
            for j in range(d):
                nxt[mask ^ (1 << j)] += count
        counts = nxt
    return counts


def capacity_from_full(d, t):
    p = full_error_law(d, t)
    live = p > 0
    return d + float(np.dot(p[live], np.log2(p[live])))


def choi_spectrum(d, t):
    """Independent matrix construction of the Choi state from Kraus operators."""
    dim = 1 << d
    p = full_error_law(d, t)
    z_basis = np.arange(dim)
    choi = np.zeros((dim * dim, dim * dim))
    for mask, prob in enumerate(p):
        if prob < 1.e-17:
            continue
        signs = np.array([(-1.) ** ((int(v) & mask).bit_count() % 2)
                          for v in z_basis])
        ket = np.zeros(dim * dim)
        ket[np.arange(dim) * (dim + 1)] = signs / math.sqrt(dim)
        choi += prob * np.outer(ket, ket)
    return np.linalg.eigvalsh(choi)


def run():
    cases = 0
    for d in range(1, 6):
        for t in range(0, 10):
            cap_radial = capacity_from_radial(d, t)
            cap_full = capacity_from_full(d, t)
            assert abs(cap_radial - cap_full) < 1e-10, (d, t)
            assert 1 - 1e-10 <= cap_radial <= d + 1e-10
            if t > 0 and d in (1, 2):
                assert abs(cap_radial - 1) < 1e-10
            if t > 0 and d >= 3:
                assert cap_radial > 1 + 1e-10
            cases += 1
            if t <= 7:
                c = exact_integer_counts(d, t)
                q = full_error_law(d, t)
                assert sum(c) == d ** t
                assert np.max(np.abs(q - np.array(c) / d ** t)) < 1e-12
                for a in range(1 << d):
                    fhat = sum(c[x] * (-1) ** ((x & a).bit_count() % 2)
                               for x in range(1 << d))
                    assert abs(fhat / d ** t - (1 - 2 * a.bit_count() / d) ** t) < 1e-12
                cases += 1
            if d <= 3 and t <= 4:
                ev = choi_spectrum(d, t)
                expected = np.sort(np.r_[full_error_law(d, t),
                                         np.zeros((1 << d) ** 2 - (1 << d))])
                assert np.max(np.abs(ev - expected)) < 1e-10
                cases += 1
    for d in (24, 48, 96, 192, 384, 768):
        for c in (-0.3, 0.0, 0.4, 0.8):
            t = int(math.floor(0.25 * d * math.log(d) + c * d))
            exact = capacity_from_radial(d, t) - 1
            limit = math.exp(-4 * c) / (2 * math.log(2))
            # Diagnostic only: convergence, not a universal inequality.
            if d >= 384:
                assert abs(exact - limit) < .06, (d, c, exact, limit)
            cases += 1
    for d in range(2, 6):
        vals = [capacity_from_radial(d, t) for t in range(12)]
        assert all(vals[i + 1] <= vals[i] + 1e-10 for i in range(11))
        cases += 1
    for d in (256, 512, 1024):
        t = int(math.floor(d * math.log(d) / 4))
        error = abs(capacity_from_radial(d, t) - 1 - 1/(2*math.log(2)))
        assert error < .025, (d, error)
        cases += 1
    print(f'VERIFY_OK {cases} finite radial/Fourier/Choi/asymptotic checks')
    for d in (64, 256, 1024):
        print(f'd={d} critical excess={capacity_from_radial(d, int(.25*d*math.log(d)))-1:.9f}')
    print(f'critical limit={1/(2*math.log(2)):.9f}')


if __name__ == '__main__':
    run()
