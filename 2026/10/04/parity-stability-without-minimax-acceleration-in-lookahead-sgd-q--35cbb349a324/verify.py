import math

def p(h, k, alpha):
    return 1 - alpha + alpha * (1 - h) ** k

def stability_ceiling(k, alpha):
    if k % 2 == 0:
        return 2.0
    return 1.0 + (2.0 / alpha - 1.0) ** (1.0 / k)

# Sharp parity boundaries.
for k in range(1, 9):
    for alpha in (0.2, 0.5, 0.8, 1.0):
        c = stability_ceiling(k, alpha)
        inside = p(c * (1 - 1e-8), k, alpha)
        boundary = p(c, k, alpha)
        outside = p(c * (1 + 1e-8), k, alpha)
        assert abs(inside) < 1
        if k % 2 == 0:
            assert abs(boundary - 1.0) < 1e-9
            assert outside > 1
        else:
            assert abs(boundary + 1.0) < 1e-9
            assert outside < -1

def rho_interval(mu, L, eta, k, alpha):
    # For odd k the polynomial is monotone; for even k its inner power is U-shaped,
    # so the maximum after positive interpolation occurs at an interval endpoint.
    p_mu = 1 - alpha + alpha * (1 - eta * mu) ** k
    p_L = 1 - alpha + alpha * (1 - eta * L) ** k
    return max(abs(p_mu), abs(p_L))

# Exact optimum at the classical equioscillating GD step.
for kappa in (1.2, 2.0, 5.0, 10.0, 100.0):
    mu, L = 1.0, kappa
    q = (L - mu) / (L + mu)
    eta_star = 2.0 / (L + mu)
    for k in range(1, 9):
        target = q ** k
        got = rho_interval(mu, L, eta_star, k, 1.0)
        assert abs(got - target) < 1e-12

# Dense search guard: no fixed interpolation beats q^k.
for kappa in (1.5, 2.0, 5.0, 10.0):
    mu, L = 1.0, kappa
    q = (L - mu) / (L + mu)
    for k in (1, 2, 3, 4, 5, 7):
        target = q ** k
        best = 10.0
        # Include a broad supercritical range because odd k can be stabilized there.
        for i in range(1, 501):
            eta = (4.0 / L) * i / 500.0
            for j in range(1, 201):
                alpha = j / 200.0
                best = min(best, rho_interval(mu, L, eta, k, alpha))
        # The grid may miss the exact optimum, so it may only be larger.
        assert best + 2e-3 >= target
        # Direct optimum is exact.
        assert abs(rho_interval(mu, L, 2/(L+mu), k, 1.0) - target) < 1e-12

# k=1 has the nonunique product alpha*eta optimum.
mu, L = 1.0, 7.0
target_eta = 2.0 / (L + mu)
q = (L - mu) / (L + mu)
for alpha in (0.2, 0.5, 0.8, 1.0):
    eta = target_eta / alpha
    assert abs(rho_interval(mu, L, eta, 1, alpha) - q) < 1e-12

# Common alpha=1/2, k=5 numerical ceiling.
assert abs(stability_ceiling(5, 0.5) - (1 + 3 ** (1/5))) < 1e-15

print("verification passed")
