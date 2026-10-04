from fractions import Fraction as F

def simplex_coefficients(a, b):
    return a + 1 - b, a - 1 + b

# Algebraic coefficient check:
# a(P+N) + (1-b)(P-N)
# = (a+1-b)P + (a-1+b)N.
a = F(17, 10)
b = F(1, 2)
cp, cn = simplex_coefficients(a, b)
assert cp == F(11, 5)
assert cn == F(6, 5)

r_plus = 1 / cp
r_minus = -1 / cn
assert r_plus == F(5, 11)
assert r_minus == F(-5, 6)

# Classical simplex:
# (11/5)P + (6/5)N = 1  iff  11P + 6N = 5.
P = F(7, 55)
N = (F(1) - cp * P) / cn
assert cp * P + cn * N == 1
assert 11 * P + 6 * N == 5

# Branch characteristic polynomials.
def q_plus(lam, a, b):
    return lam * lam + a * lam - b

def q_minus(lam, a, b):
    return lam * lam - a * lam - b

assert q_plus(F(0), a, b) < 0
assert q_plus(F(1), a, b) > 0
assert q_plus(F(-1), a, b) < 0

assert q_minus(F(0), a, b) < 0
assert q_minus(F(1), a, b) < 0
assert q_minus(F(-1), a, b) > 0

print("VERIFY_OK")
