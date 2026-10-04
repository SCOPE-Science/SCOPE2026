def m_series(z, beta, terms=200):
    s = 0.0
    for j in range(1, terms + 1):
        s += ((-1.0) ** j) * beta * (z ** j) / (1.0 + j * beta)
    return s

for beta in (0.4, 1.0, 2.5):
    target = beta / (1.0 + 2.0 * beta)
    for sign in (-1.0, 1.0):
        z = sign * 1e-4
        ratio = (m_series(z, beta) + beta * z / (1.0 + beta)) / (z * z)
        if abs(ratio - target) > 5e-4:
            raise SystemExit("series coefficient check failed")

alpha = 1.7
beta = 0.8
c = -0.6
lam = 200.0
n = 10**12
const = 2.0 * (1.0 + 2.0 * beta) ** 2 / (alpha * alpha * beta * beta * c ** 4)
k = (const * lam) ** (1.0 / (4.0 * beta + 1.0)) * n ** (4.0 * beta / (4.0 * beta + 1.0))
A = -beta * c * (k / n) ** beta
recovered = k * alpha * alpha * A ** 4 / (2.0 * beta * beta * (1.0 + 2.0 * beta) ** 2)
if abs(recovered / lam - 1.0) > 1e-10:
    raise SystemExit("threshold inversion check failed")

print("VERIFY_OK")
