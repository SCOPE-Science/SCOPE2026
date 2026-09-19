import numpy as np


def instance(N: int):
    if N < 2:
        raise ValueError('N must be at least 2')
    n = N + 2
    q, b = 0, n - 1
    G = np.arange(1, N + 1)

    R = np.zeros((n, n), dtype=float)
    R[np.ix_(G, G)] = 1.0
    R[b, b] = 1.0

    s = N ** 0.25
    v = np.zeros(n)
    v[q] = 2.0 * s
    v[b] = s
    A = R + np.outer(v, v)
    return A, R, v, q, G, b


def scores(A, R):
    """Full-neighborhood weighted-mass scores m_i=sum_j (R_jj A_ji)^2."""
    d = np.diag(R)
    return np.sum((d[:, None] * A) ** 2, axis=0)


def update(R, p):
    c = R[:, p]
    return R - np.outer(c, c) / R[p, p]


def frob_gain(R, p):
    Rp = update(R, p)
    return np.linalg.norm(R, 'fro')**2 - np.linalg.norm(Rp, 'fro')**2


def best_rank2_error(N):
    # A is the direct sum of J_N and the 2x2 (q,b) block.
    # The third singular value is the smaller eigenvalue of this block.
    r = np.sqrt(N)
    return 0.5 * (5.0 * r + 1.0 - np.sqrt(25.0 * N - 6.0 * r + 1.0))


for N in [2, 4, 16, 100, 1000]:
    A, R_target, v, q, G, b = instance(N)
    m0 = scores(A, A)
    first = int(np.argmax(m0))
    R1 = update(A, first)

    m1 = scores(A, R1)
    m1[first] = -np.inf
    second = int(np.argmax(m1))

    R_bad = update(R1, second)
    g = int(G[0])
    R_good = update(R1, g)
    err_bad = np.linalg.norm(R_bad, 'fro')
    err_good = np.linalg.norm(R_good, 'fro')
    opt2 = best_rank2_error(N)

    print(f'N={N}')
    print(f'  first pivot = {first} (q={q})')
    print(f'  ||R1-R_target||_F = {np.linalg.norm(R1-R_target, "fro"):.3e}')
    print(f'  second pivot = {second} (b={b})')
    print(f'  second scores: good={scores(A,R1)[g]:.12g}, bad={scores(A,R1)[b]:.12g}')
    print(f'  residual norms: chosen={err_bad:.12g}, good={err_good:.12g}')
    print(f'  chosen/good ratio = {err_bad/err_good:.12g}')
    print(f'  best rank-2 SVD error = {opt2:.12g}')
    print(f'  chosen/SVD ratio = {err_bad/opt2:.12g}')
    print(f'  one-step gains: chosen={frob_gain(R1,b):.12g}, good={frob_gain(R1,g):.12g}')
    print(f'  ||vv^T||_2 / ||R_target||_2 = {np.dot(v,v)/N:.12g}')
