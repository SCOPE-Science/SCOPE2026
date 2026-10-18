"""Supplementary finite-dimensional diagnostics for spectral-tail repair.

This program tests only finite matrix identities and noncommuting random cases;
it is not a proof of the infinite-dimensional theorem.
Requires numpy. Run: python verify.py
"""
import numpy as np

def experiment(N, m, seed):
    rng = np.random.default_rng(seed)
    i = np.arange(1, N + 1, dtype=float)
    # Below-baseline coordinates are deliberately interlaced with above-baseline coordinates.
    vals = np.array([1.0 + 0.2 / (j + 1) if j % 3 == 0
                     else 1.0 - 0.35 / (j + 1) for j in range(N)])
    D = np.diag(vals)
    deficits = np.sort(np.maximum(1.0 - vals, 0.0))[::-1]
    negidx = np.argsort(vals)
    # Optimal repair: keep the m deepest below-baseline eigenvalues, clip all others.
    Bstar = np.diag(np.maximum(vals, 1.0))
    for j in negidx[:m]:
        if vals[j] < 1.0:
            Bstar[j, j] = vals[j]
    star = np.linalg.svd(Bstar - D, compute_uv=False)
    assert np.allclose(star, np.pad(deficits[m:], (0, min(m,N))))
    # Noncommuting competitor with exactly m below-baseline eigenvalues.
    bvals = np.array([1.0 + 0.07 / (j + 1) for j in range(N)])
    bvals[:m] = np.array([0.9 - 0.02 / (j + 1) for j in range(m)])
    X = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    U, _ = np.linalg.qr(X)
    B = U @ np.diag(bvals) @ U.conj().T
    singular = np.linalg.svd(B - D, compute_uv=False)
    assert np.all(singular + 1e-10 >= np.pad(deficits[m:], (0, m)))
    assert np.min(np.linalg.eigvalsh(B)) > 0.0
    return max(abs(star - np.pad(deficits[m:], (0, m))))

if __name__ == '__main__':
    count = 0
    for size in (8, 12, 20):
        for m in (0, 1, 3):
            for seed in (0, 11, 37):
                experiment(size, m, seed)
                count += 1
    print('PASS: exact clipped tails and noncommuting lower bounds on', count, 'finite tests')
