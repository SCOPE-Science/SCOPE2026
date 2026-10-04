import numpy as np


def trace_distance(a, b):
    vals = np.linalg.eigvalsh(a - b)
    return 0.5 * float(np.sum(np.abs(vals)))


def random_density(rng, dim):
    x = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    a = x @ x.conj().T
    return a / np.trace(a)


def random_projector(rng, dim, rank):
    x = rng.normal(size=(dim, rank)) + 1j * rng.normal(size=(dim, rank))
    q, _ = np.linalg.qr(x)
    return q @ q.conj().T


def check_random_instances():
    rng = np.random.default_rng(20260927)
    for dim in (3, 4, 6):
        for _ in range(300):
            rho = random_density(rng, dim)
            sigma = random_density(rng, dim)
            rank = int(rng.integers(1, dim))
            proj = random_projector(rng, dim, rank)
            p = float(np.trace(proj @ rho).real)
            q = float(np.trace(proj @ sigma).real)
            if min(p, q) < 1e-12:
                continue
            rho_p = proj @ rho @ proj / p
            sigma_p = proj @ sigma @ proj / q
            eps = trace_distance(rho, sigma)
            cond = trace_distance(rho_p, sigma_p)
            bound = min(1.0, eps / max(p, q))
            if cond > bound + 2e-10:
                raise AssertionError((dim, eps, p, q, cond, bound))


def check_sharp_family():
    cases = [
        (0.9, 0.1, 0.8),
        (0.9, 0.1, 0.85),
        (0.6, 0.4, 0.3),
        (0.6, 0.4, 0.59),
        (0.6, 0.4, 0.8),
        (0.5, 0.5, 0.2),
        (0.7, 0.65, 0.1),
    ]
    proj = np.diag([1.0, 1.0, 0.0])
    for p, q, tau in cases:
        if q > p:
            p, q = q, p
        if tau + 1e-14 < p - q:
            raise AssertionError("infeasible test budget")
        c = min(1.0, tau / p)
        rho = np.diag([p * c, p * (1.0 - c), 1.0 - p])
        sigma = np.diag([0.0, q, 1.0 - q])
        rho_p = proj @ rho @ proj / p
        sigma_p = proj @ sigma @ proj / q
        eps = trace_distance(rho, sigma)
        cond = trace_distance(rho_p, sigma_p)
        if abs(cond - c) > 1e-12:
            raise AssertionError(("conditional", p, q, tau, cond, c))
        if eps > tau + 1e-12:
            raise AssertionError(("global", p, q, tau, eps))
        exact = max(p - q, p * c)
        if abs(eps - exact) > 1e-12:
            raise AssertionError(("formula", p, q, tau, eps, exact))


if __name__ == "__main__":
    check_random_instances()
    check_sharp_family()
    print("VERIFY_OK")
