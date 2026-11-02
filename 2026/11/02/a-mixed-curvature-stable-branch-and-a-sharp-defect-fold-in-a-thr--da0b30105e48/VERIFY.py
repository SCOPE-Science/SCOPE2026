"""Reproduce finite checks for a periodic three-body phase-oscillator ring."""
import numpy as np
from scipy.optimize import brentq


def ring_laplacian(N):
    L = -2.0 * np.eye(N)
    for i in range(N):
        L[i, (i - 1) % N] += 1
        L[i, (i + 1) % N] += 1
    return L


def predicts_stable(c):
    neg = np.flatnonzero(c < -1e-12)
    zeros = np.flatnonzero(np.abs(c) <= 1e-12)
    if len(neg) == 0:
        return len(zeros) <= 1
    if len(neg) != 1 or len(zeros) != 0:
        return False
    j = neg[0]
    return -c[j] < 1 / np.sum(1 / c[np.arange(len(c)) != j])


def check():
    rng = np.random.default_rng(8317)
    total = 0
    for N in range(3, 16):
        n = N - 1
        L = ring_laplacian(N)
        H = -L
        spectrum, vectors = np.linalg.eigh(H)
        assert abs(spectrum[0]) < 1e-10 and spectrum[1] > 1e-9
        W = vectors[:, 1:]
        for j in range(1300):
            c = rng.uniform(-1, 1, N)
            if j % 67 == 0:
                c[rng.integers(N)] = 0.0
            if j % 89 == 0:
                c[rng.choice(N, size=2, replace=False)] = 0.0
            q = np.linalg.eigvalsh(W.T @ np.diag(c) @ W)
            assert predicts_stable(c) == bool(q[0] > 1e-9), (N, j, c, q)
            total += 1

        tstar = brentq(lambda t: n * np.cos(n * t) + np.cos(t),
                         np.pi / (2 * n), np.pi / n, xtol=1e-14)
        assert np.pi / (2*n) < tstar < np.pi / n
        for t, typ in [(tstar / 2, "stable"),
                       ((np.pi / (2*n) + tstar) / 2, "stable_mixed"),
                       ((tstar + np.pi / n) / 2, "unstable"),
                       (tstar, "fold")]:
            q = np.r_[n*t, np.repeat(-t, n)]
            phi = np.linalg.lstsq(L, q, rcond=None)[0]
            delta = np.sin(n*t) + np.sin(t)
            omega = np.r_[0, np.repeat(delta, n)]
            force = omega + np.sin(L @ phi)
            assert np.max(abs(force - np.sin(n*t))) < 1e-10, (N, t)
            eig = np.sort(np.real(np.linalg.eigvals(np.diag(np.cos(q)) @ L)))
            z = np.sum(abs(eig) < 1e-7)
            pos = np.sum(eig > 1e-7)
            if typ in ("stable", "stable_mixed"):
                assert pos == 0 and z == 1, (N, typ, eig)
            elif typ == "unstable":
                assert pos == 1 and z == 1, (N, typ, eig)
            else:
                assert pos == 0 and z == 2, (N, typ, eig)
            if typ == "stable_mixed":
                assert np.cos(n*t) < 0
        width = np.sin(n*tstar) + np.sin(tstar) - 1 - np.sin(np.pi/(2*n))
        assert width > 0
    print('PASS: %d signed-form classifications, real locked-state residuals,' % total)
    print('      stable mixed branch, unstable upper branch, fold kernel, positive windows')
    for n in (10, 30, 100, 300, 1000):
        tstar = brentq(lambda t: n * np.cos(n*t) + np.cos(t),
                          np.pi/(2*n), np.pi/n, xtol=1e-14)
        width = np.sin(n*tstar) + np.sin(tstar) - 1 - np.sin(np.pi/(2*n))
        assert abs(n*n*width - 0.5) < 2/n
        print('n=%d, scaled-window=%.8f' % (n, n*n*width))


if __name__ == '__main__':
    check()
