import numpy as np


def dct2(n):
    beta = np.ones(n)
    beta[0] = 1.0 / np.sqrt(2.0)
    return np.array([
        [np.sqrt(2.0 / n) * beta[j] * np.cos(np.pi * j * (2*k + 1) / (2*n))
         for k in range(n)]
        for j in range(n)
    ])


def generator(n, rho):
    diag = np.array([1.0] + [1.0 + rho*rho] * (n - 2) + [1.0])
    return np.diag(diag) + np.diag([-rho] * (n - 1), 1) + np.diag([-rho] * (n - 1), -1)


def transformed_formula(n, rho):
    C = dct2(n)
    beta = np.ones(n)
    beta[0] = 1.0 / np.sqrt(2.0)
    q = np.sqrt(2.0 / n) * beta * np.cos(np.pi * np.arange(n) / (2*n))
    lam = 2.0 - 2.0 * np.cos(np.pi * np.arange(n) / n)
    d = (1.0 - rho)**2 + rho * lam
    s = (-1.0) ** np.arange(n)
    sigma = rho * (1.0 - rho)
    return np.diag(d) + sigma * (np.outer(q, q) + np.outer(s*q, s*q))


def correction_factor(n, rho):
    C = dct2(n)
    G = C @ generator(n, rho) @ C.T
    even = np.arange(0, n, 2)
    odd = np.arange(1, n, 2)
    Q = np.zeros((n, n))
    for ind in (even, odd):
        if len(ind) == 0:
            continue
        vals, U = np.linalg.eigh(G[np.ix_(ind, ind)])
        Q[np.ix_(ind, ind)] = U.T
    return Q, C


def odd_butterfly(n):
    m = (n - 1) // 2
    rows = []
    for k in range(m):
        r = np.zeros(n)
        r[k] = r[n - 1 - k] = 1.0 / np.sqrt(2.0)
        rows.append(r)
    r = np.zeros(n)
    r[m] = 1.0
    rows.append(r)
    for k in range(m):
        r = np.zeros(n)
        r[k] = 1.0 / np.sqrt(2.0)
        r[n - 1 - k] = -1.0 / np.sqrt(2.0)
        rows.append(r)
    return np.array(rows)


def dct6_core(n):
    # n = 2m+1, core order m+1
    m = (n - 1) // 2
    out = np.empty((m + 1, m + 1))
    for j in range(m + 1):
        beta = 1.0 / np.sqrt(2.0) if j == 0 else 1.0
        for k in range(m + 1):
            gamma = 1.0 / np.sqrt(2.0) if k == m else 1.0
            out[j, k] = 2.0 / np.sqrt(n) * beta * gamma * np.cos(np.pi * j * (2*k + 1) / n)
    return out


def dct8_core(n):
    # n = 2m+1, core order m
    m = (n - 1) // 2
    return np.array([
        [2.0 / np.sqrt(n) * np.cos(np.pi * (2*j + 1) * (2*k + 1) / (2*n))
         for k in range(m)]
        for j in range(m)
    ])

max_formula = 0.0
max_cross_parity = 0.0
max_diag = 0.0
max_orth = 0.0
max_odd_core = 0.0

for n in range(2, 17):
    C = dct2(n)
    for rho in (0.13, 0.37, 0.71, 0.94):
        T = generator(n, rho)
        G = C @ T @ C.T
        F = transformed_formula(n, rho)
        max_formula = max(max_formula, np.linalg.norm(G - F, ord=np.inf))
        mask = (np.add.outer(np.arange(n), np.arange(n)) % 2) == 1
        max_cross_parity = max(max_cross_parity, np.max(np.abs(G[mask])))
        Q, C0 = correction_factor(n, rho)
        W = Q @ C0
        H = W @ T @ W.T
        max_diag = max(max_diag, np.max(np.abs(H - np.diag(np.diag(H)))))
        max_orth = max(max_orth, np.linalg.norm(W @ W.T - np.eye(n), ord=np.inf))
        assert np.all(np.diff(np.diag(H)) > 0.0)

for n in range(3, 18, 2):
    m = (n - 1) // 2
    C = dct2(n)
    B = odd_butterfly(n)
    CBt = C @ B.T
    Cs = dct6_core(n)
    Ca = dct8_core(n)
    err = max(
        np.max(np.abs(CBt[0::2, :m+1] - Cs)),
        np.max(np.abs(CBt[1::2, m+1:] - Ca)),
        np.max(np.abs(CBt[0::2, m+1:])),
        np.max(np.abs(CBt[1::2, :m+1])),
    )
    max_odd_core = max(max_odd_core, err)

print(f"max DCT-basis formula residual: {max_formula:.3e}")
print(f"max opposite-parity entry:      {max_cross_parity:.3e}")
print(f"max diagonalization residual:   {max_diag:.3e}")
print(f"max orthogonality residual:     {max_orth:.3e}")
print(f"max odd DCT-VI/VIII split residual: {max_odd_core:.3e}")
print("all corrected generator diagonals were strictly increasing")
