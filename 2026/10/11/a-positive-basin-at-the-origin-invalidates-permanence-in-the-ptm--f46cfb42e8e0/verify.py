from fractions import Fraction as F

rho1 = F(2)
rho2 = F(1)
alpha = F(1, 2)
alpha0 = F(1, 2)
delta = F(1, 16)
q = F(3, 4)
A, B, C = F(3), F(1), F(1)

assert rho1 > 1
assert 0 < rho2 <= rho1
assert 0 < alpha0 < 1
assert 0 <= alpha <= 1

# For P <= delta, tanh(P) <= P implies H' <= rho1*delta*H.
coef_H = A * rho1 * delta + B * rho2 + C * alpha
coef_P = C * (1 - alpha)
coef_G = C * alpha0

assert coef_H == F(15, 8)
assert coef_H <= q * A
assert coef_P <= q * B
assert coef_G <= q * C

# DT(0) is lower triangular with diagonal (0, 0, alpha0).
diag = (F(0), F(0), alpha0)
assert diag == (F(0), F(0), F(1, 2))
assert max(abs(x) for x in diag) < 1

print("VERIFY_OK")
