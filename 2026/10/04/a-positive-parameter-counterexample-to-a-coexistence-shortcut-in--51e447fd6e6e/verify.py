from fractions import Fraction as F

r = K = m = beta = gamma = beta1 = beta2 = beta3 = A_model = F(1)
alpha = F(2)
gamma1 = F(2)
eta = F(1, 10)

params = [r, K, m, beta, gamma, beta1, beta2, beta3, A_model, alpha, gamma1, eta]
assert all(p > 0 for p in params)

C1 = gamma + beta2 * A_model + beta3 * eta
C2 = beta2 - gamma1
L = K * (1 - (alpha + m * beta1 * eta) / (r * m))
L0 = max(F(0), L)
U = K * (1 - beta1 * eta / r)
Theta = K * (alpha - m * r + m * beta1 * eta)

assert r > beta1 * eta
assert gamma1 > beta2
assert beta < C1
assert C1 == F(21, 10)
assert C2 == -1
assert L == F(-11, 10)
assert L0 == 0
assert U == F(9, 10)
assert Theta == F(11, 10)

Aq = beta * (r * m) ** 2 + alpha * K * r * C2
Bq = (2 * beta * r * m * Theta
      - alpha * K * r * m * C1
      - alpha * K**2 * (r - beta1 * eta) * C2)
Cq = beta * Theta**2 - alpha * K * Theta * C1

assert Aq == -1
assert Bq == F(-1, 5)
assert Cq == F(-341, 100)

def f(u):
    return Aq * u * u + Bq * u + Cq

assert f(L) == F(-22, 5)
assert f(U) == F(-22, 5)
assert Aq < 0 and Bq < 0 and Cq < 0
# For every u>0, Aq*u^2, Bq*u, and Cq are all strictly negative.
print('VERIFY_OK')
