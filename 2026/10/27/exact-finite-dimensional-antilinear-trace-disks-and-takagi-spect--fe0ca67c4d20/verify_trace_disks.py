"""Numerical checks for finite-dimensional antilinear trace-disk radii.

Requires NumPy. Checks exact extremal and zero frames for random symmetric
matrices and perturbations by invisible skew-symmetric matrices; samples
additional random frames to check the global radius upper bound.
"""
import numpy as np


def zero_frame(s, k):
    """Return an orthonormal k-frame giving zero symmetric diagonal sum."""
    n = len(s)
    assert n >= 2 and 1 <= k <= n
    z = np.eye(n, dtype=complex)[:, :k].copy()
    if k == 1:
        if s[0] + s[1] > 0:
            z[:, 0] = 0
            z[0, 0] = np.sqrt(s[1] / (s[0] + s[1]))
            z[1, 0] = 1j * np.sqrt(s[0] / (s[0] + s[1]))
        return z
    u = np.eye(k, dtype=complex)
    pair_end = k if k % 2 == 0 else k - 3
    for j in range(0, pair_end, 2):
        u[j:j + 2, j:j + 2] = (np.eye(2) + 1j * np.fliplr(np.eye(2))) / np.sqrt(2)
    if k % 2:
        idx = k - 3
        denom = s[idx] + s[idx + 1]
        cos2 = -s[idx + 2] / denom if denom > 0 else 0.0
        theta = 0.5 * np.arccos(cos2)
        u[idx:idx + 2, idx:idx + 2] = np.cos(theta) * np.eye(2) + 1j * np.sin(theta) * np.fliplr(np.eye(2))
    z[:k, :] = u
    return z


def haar_unitary(n, rng):
    m = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(m)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def check():
    rng = np.random.default_rng(221026)
    cases = checks = 0
    for n in range(2, 10):
        for trial in range(24):
            s = np.sort(rng.uniform(0.0, 6.0, n))[::-1]
            if trial == 0:
                s[:] = 0.0
            elif trial == 1:
                s[-1] = 0.0
            elif trial == 2:
                s[:] = s[0]
            v = haar_unitary(n, rng)
            c = v @ np.diag(s) @ v.T
            skew_raw = rng.normal(size=(n,n)) + 1j * rng.normal(size=(n,n))
            skew = 0.5 * (skew_raw - skew_raw.T)
            m = c + skew
            assert np.max(np.abs(0.5*(m+m.T)-c)) < 5e-14
            for k in range(1, n + 1):
                rad = sum(s[:k]) / k
                max_frame = v.conj()[:, :k]
                min_frame = v.conj() @ zero_frame(s, k)
                for frame, expected in [(max_frame,rad),(min_frame,0.0)]:
                    assert np.max(np.abs(frame.conj().T @ frame-np.eye(k))) < 1e-12
                    values = np.sum(frame * (m @ frame), axis=0)  # trace Z^T M Z
                    assert abs(abs(np.sum(values) / k) - expected) < 1e-10
                    checks += 1
                for _ in range(8):
                    frame = haar_unitary(n, rng)[:, :k]
                    value = np.trace(frame.T @ m @ frame) / k
                    assert abs(value) < rad+1e-10
                    checks += 1
                cases += 1
    print(f"PASS {cases} dimension-rank instances and {checks} checked frames")


if __name__ == '__main__':
    check()
