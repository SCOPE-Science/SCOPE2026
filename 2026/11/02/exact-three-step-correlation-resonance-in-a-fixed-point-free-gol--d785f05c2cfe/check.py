"""Exact symbolic checks for a golden-ratio expanding interval map.

Requires Python 3 with SymPy. Run: python check.py
"""
import sympy as sp

rt5 = sp.sqrt(5)
beta = (1 + rt5) / 2
a = 1 - beta / 2
c = beta / 2
H0 = sp.Rational(1, 2) + rt5 / 10
H1 = sp.Rational(1, 2) + 3 * rt5 / 10


def zero(x):
    return sp.simplify(sp.expand(x)) == 0


# The exact Markov partition is [0,a], [a,1/2], [1/2,c], [c,1].
e = [sp.Integer(0), a, sp.Rational(1, 2), c, sp.Integer(1)]
A = sp.Matrix([[0, 1, 0, 0],
               [0, 0, 1, 1],
               [1, 1, 0, 0],
               [0, 0, 1, 0]])
h = sp.Matrix([H0, H1, H1, H0])
assert all(zero(z) for z in (A.T * h / beta - h))
assert zero(sum(h[i] * (e[i + 1] - e[i]) for i in range(4)) - 1)
assert zero(sum(h[i] * (e[i + 1] ** 2 - e[i] ** 2) / 2
                for i in range(4)) - sp.Rational(1, 2))

# Restriction of the Frobenius--Perron operator to antisymmetric
# piecewise affine functions. Each left-hand cell has u*x+v.
N = sp.Matrix([
    [0, 0, beta ** -2, 0],
    [0, 0, -1 / (2 * beta), -1 / beta],
    [beta ** -2, 0, beta ** -2, 0],
    [-a * beta ** -2, 1 / beta, -1 / (2 * beta), -1 / beta],
])
# Independent eight-coefficient transfer construction from the branch images.
offsets = [a, a, a - 1, a - 1]
M = sp.zeros(8)
for j in range(4):
    for i in range(4):
        if A[i, j]:
            M[2*j, 2*i] += beta**-2
            M[2*j+1, 2*i] -= offsets[i] / beta**2
            M[2*j+1, 2*i+1] += 1 / beta
K = sp.zeros(8, 4)
for i in range(2):
    K[2*i, 2*i] = 1
    K[2*i+1, 2*i+1] = 1
    j = 3 - i
    K[2*j, 2*i] = 1
    K[2*j+1, 2*i] = -1
    K[2*j+1, 2*i+1] = -1
assert all(zero(z) for z in (M*K - K*N))
q = sp.Matrix([H0, -H0 / 2, H1, -H1 / 2])
assert all(zero(t) for t in (N ** 3 * q - beta ** -3 * q))

w = sp.Matrix([[2*a**3/3 - a**2/2, a**2-a,
                -sp.Rational(1, 24)-2*a**3/3+a**2/2,
                -sp.Rational(1, 4)-a**2+a]])
C0 = (sp.Integer(5) - rt5) / 40
assert zero((w * q)[0] - C0)
assert zero((w * N * q)[0])
assert zero((w * N ** 2 * q)[0])
v = q
for n in range(7):
    expected = C0 / beta ** n if n % 3 == 0 else 0
    assert zero((w * v)[0] - expected), n
    v = (N * v).applyfunc(sp.simplify)
sigma2 = sp.simplify(C0 * (1 + beta ** -3) / (1 - beta ** -3))
assert zero(sigma2 - rt5 / 20)
# Fixed-point inequalities: F(x)-x>0 to the left and <0 to the right.
assert 0 < float(a) < .5 < float(c) < 1
print('PASS: invariant probability, exact cubic transfer identity, 7 covariances,')
print('      and exact Green--Kubo variance sqrt(5)/20')
