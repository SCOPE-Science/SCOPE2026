import math

def reg_norm(z, N):
    x, y = z
    return max(
        x * math.cos(2 * math.pi * j / N)
        + y * math.sin(2 * math.pi * j / N)
        for j in range(N)
    )

# The proof is symbolic; these are independent numerical reconstruction checks.
for n in range(1, 31):
    N = 4 * n
    alpha = math.pi / N
    R = 1 / math.cos(alpha)
    target = R * R

    # Deterministic checks of the norm sandwich on Euclidean directions.
    for j in range(12 * N):
        th = 2 * math.pi * j / (12 * N)
        z = (math.cos(th), math.sin(th))
        q = reg_norm(z, N)
        assert q <= 1 + 3e-13
        assert 1 <= R * q + 3e-13

    # Balanced equality pair.
    x = (R * math.cos(alpha), R * math.sin(alpha))
    y = (R * math.cos(alpha), -R * math.sin(alpha))
    assert abs(reg_norm(x, N) - 1) < 3e-12
    assert abs(reg_norm(y, N) - 1) < 3e-12
    A = reg_norm((x[0] + y[0], x[1] + y[1]), N)
    B = reg_norm((x[0] - y[0], x[1] - y[1]), N)
    val = (A * A + B * B) / 4
    assert abs(val - target) < 5e-12

    # Odd-half-step facet resonances.
    x = (R * math.cos(alpha), R * math.sin(alpha))
    y = (
        R * math.cos(alpha + math.pi / 2),
        R * math.sin(alpha + math.pi / 2),
    )
    assert abs(reg_norm(x, N) - 1) < 3e-12
    assert abs(reg_norm(y, N) - 1) < 3e-12

    for k in range(n):
        phi = (2 * k + 1) * alpha
        lam = math.cos(phi)
        mu = math.sin(phi)
        u = (lam * x[0] + mu * y[0], lam * x[1] + mu * y[1])
        v = (mu * x[0] - lam * y[0], mu * x[1] - lam * y[1])
        A = reg_norm(u, N)
        B = reg_norm(v, N)
        val = (A * A + B * B) / 2
        assert abs(A - R) < 5e-12
        assert abs(B - R) < 5e-12
        assert abs(val - target) < 8e-12

# Closed low-order checks.
assert abs((1 / math.cos(math.pi / 8)) ** 2 - (4 - 2 * math.sqrt(2))) < 2e-14
assert abs((1 / math.cos(math.pi / 12)) ** 2 - (8 - 4 * math.sqrt(3))) < 2e-14

print("VERIFY_OK n=1..30 balanced=30 odd_resonances=465 ceiling=sec^2(pi/(4n))")
