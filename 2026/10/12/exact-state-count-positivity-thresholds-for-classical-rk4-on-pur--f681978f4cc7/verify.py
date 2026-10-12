from fractions import Fraction as F
from math import factorial

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def smul(c, A):
    return [[c * v for v in row] for row in A]

def mpow(A, k):
    R = eye(len(A))
    for _ in range(k):
        R = mm(R, A)
    return R

def successor(n):
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        P[i][i + 1] = F(1)
    P[n - 1][n - 1] = F(1)
    return P

def rk4_matrix(n, x):
    P = successor(n)
    Q = madd(P, smul(F(-1), eye(n)))
    R = eye(n)
    Qk = eye(n)
    for k in range(1, 5):
        Qk = mm(Qk, Q)
        R = madd(R, smul(x**k / F(factorial(k)), Qk))
    return R

def e_trunc(m, x):
    return sum(((-x)**ell) / F(factorial(ell)) for ell in range(m + 1))

def coeffs(x):
    return [x**j / F(factorial(j)) * e_trunc(4 - j, x) for j in range(5)]

def coeff_matrix(n, x):
    P = successor(n)
    A = [[F(0) for _ in range(n)] for _ in range(n)]
    for j, a in enumerate(coeffs(x)):
        A = madd(A, smul(a, mpow(P, j)))
    return A

for n in range(2, 8):
    for x in [F(1, 3), F(1), F(4, 3), F(3, 2), F(2)]:
        A = rk4_matrix(n, x)
        B = coeff_matrix(n, x)
        assert A == B
        assert all(sum(row) == 1 for row in A)

# Exact formulas for the coefficients.
x = F(3, 2)
a0, a1, a2, a3, a4 = coeffs(x)
assert a3 + a4 == F(-9, 128)
A4 = rk4_matrix(4, x)
assert A4[0][3] == F(-9, 128)

x = F(6, 5)
a0, a1, a2, a3, a4 = coeffs(x)
assert a3 == F(-36, 625)
A5 = rk4_matrix(5, x)
assert A5[0][3] == F(-36, 625)

# Boundary inclusion for N=4 and N>=5.
A4b = rk4_matrix(4, F(4, 3))
assert min(min(row) for row in A4b) >= 0
assert A4b[0][3] == 0

for n in range(5, 8):
    A = rk4_matrix(n, F(1))
    assert min(min(row) for row in A) >= 0
    assert A[0][3] == 0

# Rational brackets for the two unique positive algebraic boundaries.
def g2(q):
    return q**3 - 4*q**2 + 12*q - 24

def g3(q):
    return q**3 - 3*q**2 + 6*q - 6

assert g2(F(2785, 1000)) < 0 < g2(F(2786, 1000))
assert g3(F(1596, 1000)) < 0 < g3(F(1597, 1000))

# Derivative discriminants certify strict monotonicity of the cubics.
# g2' = 3x^2 - 8x + 12 has discriminant -80; g3' = 3((x-1)^2+1).
assert (-8)**2 - 4*3*12 == -80

print("VERIFY_OK")
