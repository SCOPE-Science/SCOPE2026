"""Independent finite checks for correlation and Gram identities of centred Blaschke compositions.

Finite calculations check examples only; general Riesz and entropy statements
are established by analytic arguments.
"""
from fractions import Fraction
import numpy as np
import sympy as sp

z = sp.symbols('z')

def gram(c):
    n = len(c)
    C = sp.eye(n + 1)
    for i in range(n + 1):
        for j in range(i+1, n + 1):
            x = sp.prod(c[k] for k in range(i, j))
            C[j, i] = x
            C[i, j] = sp.conjugate(x)
    return C

def finite_precision(c):
    n = len(c)
    L = sp.eye(n + 1)
    for i in range(1, n+1):
        L[i, i-1] = -c[i-1]
    D_inv = sp.diag(1, *[1/(1-sp.Abs(x)**2) for x in c])
    return sp.simplify(L.conjugate().T * D_inv * L)

ctests = (
    (sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(-1, 4)),
    (sp.Rational(1, 3), sp.Rational(-3, 5), sp.Rational(4, 7), sp.Rational(1, 8)),
    (sp.Rational(0), sp.Rational(1, 2)),
    (sp.Rational(1, 5), sp.Rational(2, 5)*sp.I, sp.Rational(-1, 3)),
)
for c in ctests:
    C = gram(c)
    P = finite_precision(c)
    assert C*P == sp.eye(len(c)+1), (c, C*P)
print('EXACT_GRAM_INVERSE_IDENTITIES_PASS', len(ctests))

# For f_c(z)=z(z+c)/(1+cz), the derivative f_c'(0) equals c.
for c in ctests[:3]:
    F = z
    for pos, d in enumerate(c, 1):
        F = sp.cancel(F * (F+d)/(1+d*F))
        assert sp.cancel(sp.diff(F, z).subs(z, 0) - sp.prod(c[:pos])) == 0
print('EXACT_DERIVATIVE_PRODUCTS_PASS', sum(map(len, ctests[:3])))

# Independent Haar trapezoidal quadrature for maps that avoid pole singularities.
c = [0.25, 0.6, 0.15]
N = 65536
w = np.exp(2j*np.pi*np.arange(N)/N)
Z = [w]
for d in c:
    w = w*(w+d)/(1+d*w)
    Z.append(w)
G_emp = np.array([[np.mean(Z[i]*np.conj(Z[j])) for j in range(4)] for i in range(4)])
G_exact = np.array(gram(tuple(sp.Rational(str(x)) for x in c))).astype(complex)
error = float(np.max(np.abs(G_emp-G_exact)))
assert error < 1e-10, error
print('BOUNDARY_QUADRATURE_CORRELATION_PASS', format(error,'.3g'))

for q in (0.2,0.5,0.8):
    n = 512
    # Toeplitz covariance testing both sharp limits via Rayleigh trial vectors.
    x = np.arange(n)
    T = q**np.abs(x[:,None]-x[None,:])
    a = (-1)**x
    Rminus = float(a@T@a/n)
    Rplus = float(np.sum(T)/n)
    amin = (1-q)/(1+q)
    bmax = (1+q)/(1-q)
    assert amin <= Rminus <= Rplus <= bmax + 1e-10
    assert Rminus-amin < 0.1 and bmax-Rplus < 0.1, (q,Rminus,Rplus)
print('UNIVERSAL_CONSTANT_SHARPNESS_PASS', 3)

for k in range(3, 9):
    n=2**k
    q = 1-sp.Rational(1,2**n)
    # A sparse near-rotation gives an exponentially small pair eigenvalue.
    block = sp.Matrix([[1,q],[q,1]])
    assert min(block.eigenvals()) == sp.Rational(1,2**n)
print('SPARSE_SPIKE_CONDITIONING_OBSTRUCTION_PASS', 6)
print('UNBOUNDED_RIESZ_AND_ENTROPY_CLAIMS_REQUIRE_ANALYTIC_PROOF')
