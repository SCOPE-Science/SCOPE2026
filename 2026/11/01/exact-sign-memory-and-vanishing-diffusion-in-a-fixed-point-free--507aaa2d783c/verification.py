"""Exact checks for the four-branch Markov sign-law theorem.

Run: python verification.py
Requires sympy. All assertions are exact rational or symbolic identities.
"""
import sympy as sp

k = sp.symbols('k', integer=True, positive=True)
z = sp.symbols('z')
P = sp.Matrix([
    [0, 1, 0, 0],
    [0, 0, 1 / k, (k - 1) / k],
    [(k - 1) / k, 1 / k, 0, 0],
    [0, 0, 1, 0],
])
pi = sp.Matrix([k - 1, k, k, k - 1]) / (2 * (2 * k - 1))
f = sp.Matrix([-1, -1, 1, 1])
h = sp.Matrix([-(2 * k + 1), -1, 1, 2 * k + 1]) / (2 * k)
W = sp.diag(*pi)

def eq(a, b):
    d = a - b
    if isinstance(d, sp.MatrixBase):
        assert all(sp.factor(t) == 0 for t in d)
    else:
        assert sp.factor(d) == 0, sp.factor(d)

# Branch lengths and their images:
# outer A [-k,-1] -> [-1,0], inner B [-1,0] -> [0,k],
# inner C [0,1] -> [-k,0], outer D [1,k] -> [0,1].
images = [
    ((-k + 1) / (k - 1), (-1 + 1) / (k - 1)),
    (k * (-1 + 1), k * (0 + 1)),
    (k * (0 - 1), k * (1 - 1)),
    ((1 - 1) / (k - 1), (k - 1) / (k - 1)),
]
for got, expect in zip(images, [(-1, 0), (0, k), (-k, 0), (0, 1)]):
    eq(got[0], expect[0]); eq(got[1], expect[1])

# Exactly normalized stationary masses; individual densities are
# pi_j / length(I_j).
eq(sp.Add(*pi), 1)
eq(P.T * pi, pi)
eq((pi.T * f)[0], 0)
for length, prob, density in zip([k-1,1,1,k-1], list(pi),
                                 [1, k, k, 1]):
    eq(prob / length, density / (2 * (2 * k - 1)))

# First return and spectral identities.
expected_char = (z - 1) * (k * z + k - 1) * (k*z*z + z + k - 1) / k**2
eq(P.charpoly(z).as_expr(), expected_char)
eq((sp.eye(4) - P)*h, f)
G = sp.factor((f.T*W*(sp.eye(4)-z*P).inv()*f)[0])
expected_G = (k*(2*k-1)+(k-1)*z) / ((2*k-1)*(k+z+(k-1)*z*z))
eq(G, expected_G)
var = (k - 1) / (k * (2 * k - 1))
eq(2 * G.subs(z, 1) - 1, var)
eq((h.T*W*h - (P*h).T*W*(P*h))[0], var)

# Exact finite-parameter checks and nonnegative conditional variances.
for m in range(3, 51):
    Q = P.subs(k, m)
    v = pi.subs(k, m)
    assert all(x >= 0 for x in Q), m
    assert all(sum(Q.row(j)) == 1 for j in range(4)), m
    assert all(x > 0 for x in Q**6), (m, 'P^6 not positive')
    eq(Q.T*v, v)
    vals = [sp.factor((f.T*sp.diag(*v)*(Q**j)*f)[0]) for j in range(15)]
    expected_coeffs = sp.series(expected_G.subs(k, m), z, 0, 15).removeO()
    for j in range(15):
        eq(vals[j], expected_coeffs.expand().coeff(z,j))
print('PASS: 48 exact rational parameter cases, 720 covariance checks, stationary law,')
print('generating function, spectral factorization, and Poisson/variance identities.')
