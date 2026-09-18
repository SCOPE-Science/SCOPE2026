import numpy as np

def equality_graph(part_masses):
    r = len(part_masses)
    A = sum(part_masses[0])
    assert r >= 2 and A > 0
    for block in part_masses:
        assert block and all(x > 0 for x in block)
        assert abs(sum(block) - A) < 1e-12

    masses = np.array([x for block in part_masses for x in block], dtype=float)
    blocks = []
    start = 0
    for block in part_masses:
        blocks.append(range(start, start + len(block)))
        start += len(block)

    W = np.zeros((len(masses), len(masses)))
    for i in range(r):
        for j in range(i + 1, r):
            for u in blocks[i]:
                for v in blocks[j]:
                    W[u, v] = W[v, u] = masses[u] * masses[v] / ((r - 1) * A)
    return W, masses

def check(part_masses):
    W, prescribed = equality_graph(part_masses)
    d = W.sum(axis=1)
    if not np.allclose(d, prescribed, atol=1e-12):
        raise AssertionError("weighted degrees do not equal prescribed masses")
    Dm = np.diag(1 / np.sqrt(d))
    M = Dm @ W @ Dm
    eig = np.linalg.eigvalsh(M)[::-1]
    r = len(part_masses)
    n = len(d)
    target = np.array([1.0] + [0.0] * (n-r) + [-1/(r-1)] * (r-1))
    target = np.sort(target)[::-1]
    if not np.allclose(eig, target, atol=1e-10):
        raise AssertionError((eig, target))
    K = sum(1/(1-x) for x in eig[1:])
    target_K = n - 2 + 1/r
    if abs(K - target_K) > 1e-10:
        raise AssertionError((K, target_K))
    return n, r, K

cases = [
    [[1], [1]],
    [[1], [0.2, 0.3, 0.5]],
    [[0.4, 0.6], [0.25, 0.75]],
    [[1], [0.3, 0.7], [0.2, 0.3, 0.5]],
    [[0.25, 0.75], [0.1, 0.2, 0.3, 0.4], [1], [0.4, 0.1, 0.2, 0.3]],
]

for case in cases:
    n, r, K = check(case)
    print(f"n={n}, r={r}, K={K:.12g}, target={n-2+1/r:.12g}")
print("all checks passed")
