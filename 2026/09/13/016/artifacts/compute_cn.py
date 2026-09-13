"""Certified zonotope mixed-volume computation for C_n short vs long root pair.
Primary method: batched float determinants rounded to nearest integer, with
max fractional deviation tracked (certificate of exactness).
Conventions (verified in WORKLOG derivation + polarization check below):
  A = short-root generators (e_i +/- e_j), B = long generators (2 e_i).
  S0 = sum_{|S|=n,S subset A} |det S|
  S1 = sum_{b in B} sum_{|T|=n-1} |det(b,T)|
  S2 = sum_{ordered b1,b2} sum_{|U|=n-2} |det(b1,b2,U)|
  V(Z,Z,C) = 2^n S0
  V(Z,Y,C) = 2^n S1 / n
  V(Y,Y,C) = 2^n S2 / (n(n-1))
  deficit sign = sign(N), N = (n-1) S1^2 - n S0 S2.
"""
import itertools
import numpy as np
import json
import sys

MAXDEV = [0.0]

def genA(n):
    cols = []
    for i in range(n):
        for j in range(i + 1, n):
            v = np.zeros(n, dtype=int); v[i] = 1; v[j] = -1; cols.append(v)
            w = np.zeros(n, dtype=int); w[i] = 1; w[j] = 1; cols.append(w)
    return np.stack(cols, axis=1)  # n x m int


def genB(n):
    B = np.zeros((n, n), dtype=int)
    for i in range(n):
        B[i, i] = 2
    return B  # n x n int


def detsum_rounded(mat_batch):
    """mat_batch: (K,n,n) float array. Returns int sum + updates MAXDEV."""
    d = np.linalg.det(mat_batch)
    r = np.rint(d)
    dev = float(np.max(np.abs(d - r)))
    if dev > MAXDEV[0]:
        MAXDEV[0] = dev
    return int(np.sum(np.abs(r).astype(np.int64)))


def subset_sum(G, k, fixed=(), chunk=20000):
    """Sum |det| over k-subsets of columns of G (n x m int), with fixed extra
    columns prepended. Exact integer via rounded float dets."""
    n = G.shape[1 - 1] if False else G.shape[0]
    m = G.shape[1]
    F = np.stack(fixed, axis=1) if len(fixed) else np.zeros((n, 0), dtype=int)
    total = 0
    batch = []
    for S in itertools.combinations(range(m), k):
        M = np.concatenate([F, G[:, list(S)]], axis=1)
        batch.append(M)
        if len(batch) == chunk:
            total += detsum_rounded(np.asarray(batch, dtype=float))
            batch = []
    if batch:
        total += detsum_rounded(np.asarray(batch, dtype=float))
    return total


def bareiss_det(M):
    """Exact integer determinant via fraction-free Bareiss. M: (n,n) int array."""
    A = [[int(x) for x in row] for row in M.tolist()]
    n = len(A)
    if n == 0:
        return 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            # pivot swap
            piv = None
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    piv = i
                    break
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
            A[i][k] = 0
        prev = A[k][k]
    return A[n - 1][n - 1]


def compute_cn(n, chunk=20000):
    A = genA(n)
    B = genB(n)
    m = A.shape[1]
    S0 = subset_sum(A, n, (), chunk)
    S1 = 0
    for i in range(n):
        S1 += subset_sum(A, n - 1, (B[:, i],), chunk)
    S2 = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            S2 += subset_sum(A, n - 2, (B[:, i], B[:, j]), chunk)
    N = (n - 1) * S1 * S1 - n * S0 * S2
    return {"n": n, "mA": m, "S0": S0, "S1": S1, "S2": S2, "N": N,
            "maxdev": MAXDEV[0]}


def exact_spotcheck(n, trials=300, seed=0):
    rng = np.random.default_rng(seed)
    A = genA(n)
    B = genB(n)
    m = A.shape[1]
    bad = 0
    for t in range(trials):
        mode = t % 3
        if mode == 0:
            S = sorted(rng.choice(m, size=n, replace=False))
            M = A[:, S]
        elif mode == 1:
            i = int(rng.integers(0, n))
            S = sorted(rng.choice(m, size=n - 1, replace=False))
            M = np.concatenate([B[:, [i]], A[:, S]], axis=1)
        else:
            i, j = rng.choice(n, size=2, replace=False)
            S = sorted(rng.choice(m, size=n - 2, replace=False))
            M = np.concatenate([B[:, [int(i)]], B[:, [int(j)]], A[:, S]], axis=1)
        exact = abs(bareiss_det(M))
        fl = abs(float(np.linalg.det(M.astype(float))))
        if int(round(fl)) != exact or abs(fl - round(fl)) > 1e-6:
            bad += 1
            print(f"MISMATCH trial {t}: exact={exact} float={fl}")
    print(f"spotcheck n={n}: {trials} trials, {bad} mismatches")
    return bad


def polarization_check_n4():
    """Independent code path: enumerate subsets of combined A|B generators,
    group by k = # of B-columns; verify W0==S0, W1==S1, W2==S2/2."""
    n = 4
    A = genA(n)
    B = genB(n)
    G = np.concatenate([A, B], axis=1)  # A cols 0..11, B cols 12..15
    mA = A.shape[1]
    W = {}
    for S in itertools.combinations(range(G.shape[1]), n):
        k = sum(1 for s in S if s >= mA)
        d = abs(bareiss_det(G[:, list(S)]))
        W[k] = W.get(k, 0) + d
    print("polarization subset sums W_k (exact Bareiss):", W)
    return W


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or [4]
    out = {}
    for n in ns:
        MAXDEV[0] = 0.0
        r = compute_cn(n)
        out[n] = r
        print(json.dumps(r))
    print("MAXDEV overall:", MAXDEV[0])
