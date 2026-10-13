import numpy as np

def replay(diag, rank, gap):
    W = np.diag(np.array(diag, dtype=float))
    m = len(diag)
    projector = None
    history = []
    max_steps = (m // rank - 1) * gap + 1
    for t in range(max_steps):
        G = W.copy()
        if t % gap == 0:
            U, s, Vt = np.linalg.svd(G, full_matrices=True)
            projector = U[:, :rank]
        compact = projector.T @ G
        projected = projector @ compact
        history.append((t, W.copy(), G.copy(), projector.copy(), compact.copy(), projected.copy()))
        W = W - projected
    return W, history

cases = [
    ([8,7,6,5], 1, 3),
    ([12,11,10,9,8,7], 2, 5),
    ([20,19,18,17,16,15,14,13], 2, 2),
    ([15,14,13,12,11,10,9,8,7], 3, 4),
]

for diag, r, T in cases:
    m = len(diag)
    assert m % r == 0
    K = m // r
    W, hist = replay(diag, r, T)
    assert np.linalg.norm(W) < 1e-12
    assert len(hist) == (K-1)*T + 1

    for k in range(K):
        t = k*T
        W_before = hist[t][1]
        compact = hist[t][4]
        assert np.linalg.norm(compact) > 0.0

        W_after = W_before - hist[t][5]
        expected = np.diag([0.0 if i < (k+1)*r else float(diag[i]) for i in range(m)])
        assert np.linalg.norm(W_after - expected) < 1e-10

        if k < K-1:
            for j in range(1, T):
                tt = t+j
                G = hist[tt][2]
                compact = hist[tt][4]
                assert np.linalg.norm(G) > 0.0
                assert np.linalg.norm(compact) < 1e-12
                assert np.linalg.norm(compact)/np.linalg.norm(G) < 1e-12

for diag, _, _ in cases:
    W0 = np.diag(np.array(diag, dtype=float))
    W1 = W0 - W0
    assert np.linalg.norm(W1) == 0.0

print("verification passed")
