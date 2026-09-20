import numpy as np


def nuc(A):
    return np.linalg.svd(A, compute_uv=False).sum()


def omega(Z, z):
    M = np.block([[Z, z[:, None]], [z[None, :], np.array([[np.trace(Z)]])]])
    return max(nuc(Z), 0.5 * nuc(M))


def aggregate(ws, alphas):
    Z = sum(a * np.outer(w, w) for w, a in zip(ws, alphas))
    z = sum(a * w for w, a in zip(ws, alphas))
    return Z, z


def check_random_decompositions(seed=260917654, trials=5000):
    rng = np.random.default_rng(seed)
    min_cost_slack = np.inf
    min_source_slack = np.inf
    for _ in range(trials):
        d = int(rng.integers(2, 7))
        m = int(rng.integers(1, 12))
        W = rng.normal(size=(m, d))
        W /= np.linalg.norm(W, axis=1, keepdims=True)
        alpha = rng.normal(size=m)
        Z, z = aggregate(W, alpha)
        feasible_cost = np.abs(alpha).sum()
        Om = omega(Z, z)
        source_average = 0.5 * (nuc(Z) + np.linalg.norm(z))
        source_nuclear = nuc(Z)
        min_cost_slack = min(min_cost_slack, feasible_cost - Om)
        min_source_slack = min(min_source_slack, Om - max(source_average, source_nuclear))
    return min_cost_slack, min_source_slack


def check_aligned(seed=314159, trials=1000):
    rng = np.random.default_rng(seed)
    max_error = 0.0
    for _ in range(trials):
        d = int(rng.integers(1, 8))
        v = rng.normal(size=d)
        v /= np.linalg.norm(v)
        s, t = rng.normal(size=2)
        Z = s * np.outer(v, v)
        z = t * v
        alpha1 = 0.5 * (s + t)
        alpha2 = 0.5 * (s - t)
        cost = abs(alpha1) + abs(alpha2)
        target = max(abs(s), abs(t))
        max_error = max(max_error, abs(cost - target), abs(omega(Z, z) - target))
    return max_error


def orthogonal_exact(S, T):
    if S == 0:
        return T
    if T == 0:
        return S
    return (S * S + 2 * S * T + 2 * T * T) / (S + 2 * T)


def check_orthogonal(seed=271828, trials=1000):
    rng = np.random.default_rng(seed)
    max_moment_error = 0.0
    max_cost_error = 0.0
    max_dual_violation = 0.0
    for _ in range(trials):
        d = int(rng.integers(2, 8))
        V = rng.normal(size=(d, 2))
        q, _ = np.linalg.qr(V)
        v, u = q[:, 0], q[:, 1]
        S, T = rng.uniform(1e-4, 3.0, size=2)
        r = T / (S + T)
        A = (S + T) ** 2 / (S + 2 * T)
        B = T * T / (S + 2 * T)
        w1 = np.sqrt(1 - r * r) * v + r * u
        w2 = -np.sqrt(1 - r * r) * v + r * u
        w3 = -u
        alphas = np.array([0.5 * A, 0.5 * A, -B])
        Zc, zc = aggregate([w1, w2, w3], alphas)
        Zt = S * np.outer(v, v)
        zt = T * u
        max_moment_error = max(max_moment_error, np.linalg.norm(Zc - Zt), np.linalg.norm(zc - zt))
        cost = np.abs(alphas).sum()
        exact = orthogonal_exact(S, T)
        max_cost_error = max(max_cost_error, abs(cost - exact))
        grid = np.linspace(-1.0, 1.0, 2001)
        p = 1.0 - 2.0 * ((grid - r) / (1.0 + r)) ** 2
        max_dual_violation = max(max_dual_violation, max(0.0, np.max(np.abs(p)) - 1.0))
    return max_moment_error, max_cost_error, max_dual_violation


def strict_example():
    Z = np.diag([1.0, 0.0])
    z = np.array([0.0, 1.0])
    source_nuclear = nuc(Z)
    source_average = 0.5 * (nuc(Z) + np.linalg.norm(z))
    Om = omega(Z, z)
    exact = orthogonal_exact(1.0, 1.0)
    return source_nuclear, source_average, Om, exact


if __name__ == '__main__':
    c1, c2 = check_random_decompositions()
    aligned = check_aligned()
    moment, cost, dual = check_orthogonal()
    n, a, o, e = strict_example()
    print(f'min feasible atomic cost minus omega: {c1:.12e}')
    print(f'min omega minus both source penalties: {c2:.12e}')
    print(f'max aligned-family identity error: {aligned:.12e}')
    print(f'max orthogonal construction moment error: {moment:.12e}')
    print(f'max orthogonal construction cost error: {cost:.12e}')
    print(f'max sampled orthogonal dual-certificate violation: {dual:.12e}')
    print(f'strict example: nuclear={n:.12f}, average={a:.12f}, omega={o:.12f}, exact={e:.12f}')
