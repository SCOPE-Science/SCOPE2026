"""Exact symbolic verification of a separable two-qutrit Pearson witness.

Dependency: sympy (tested with SymPy 1.14). Run: python verify.py
"""
import sympy as sp

R = sp.Rational
omega = R(-1, 2) + sp.sqrt(3) * sp.I / 2
F = sp.Matrix(3, 3, lambda j, k: omega ** ((j * k) % 3) / sp.sqrt(3))
A = sp.diag(-1, 0, 1)
C = sp.simplify(F * A * F.conjugate().T)
psi = sp.Matrix([2, -1, 0]) / sp.sqrt(5)
phi = sp.Matrix([1, 2, 2]) / 3

assert sp.simplify(F * F.conjugate().T) == sp.eye(3)
assert all(sp.simplify(abs(F[j, k]) ** 2 - R(1, 3)) == 0
           for j in range(3) for k in range(3))
assert sp.simplify(C-C.conjugate().T) == sp.zeros(3)

assert sp.simplify((psi.conjugate().T * phi)[0]) == 0
P = psi * psi.conjugate().T
Q = phi * phi.conjugate().T
rho = (sp.kronecker_product(P, P) + sp.kronecker_product(Q, Q)) / 2
rho_A = (P + Q) / 2
assert sp.simplify(sp.trace(P)) == 1
assert sp.simplify(sp.trace(Q)) == 1
assert sp.simplify(sp.trace(rho)) == 1
assert sp.simplify(rho-rho.conjugate().T) == sp.zeros(9)

def mean_second(ket, O):
    return (sp.simplify((ket.conjugate().T * O * ket)[0]),
            sp.simplify((ket.conjugate().T * O * O * ket)[0]))

def pearson(O):
    mu = sp.simplify(sp.trace(rho_A * O))
    variance = sp.simplify(sp.trace(rho_A * O * O) - mu * mu)
    covariance = sp.simplify(sp.trace(rho * sp.kronecker_product(O, O)) - mu * mu)
    assert variance > 0
    return sp.factor(covariance / variance), covariance, variance

assert mean_second(psi, A) == (R(-4, 5), R(4, 5))
assert mean_second(phi, A) == (R(1, 3), R(5, 9))
assert mean_second(psi, C) == (R(2, 5), R(8, 15))
assert mean_second(phi, C) == (R(-8, 9), R(26, 27))
pa, ca, va = pearson(A)
pc, cc, vc = pearson(C)
assert (pa, ca, va) == (R(17, 33), R(289, 900), R(187, 300))
assert (pc, cc, vc) == (R(841, 1394), R(841, 2025), R(1394, 2025))
assert sp.factor(pa + pc) == R(51451, 46002)
assert sp.factor(pa + pc - 1) == R(5449, 46002)

# Full-rank, still classical-classical: identity noise is diagonal in
# the same product basis as the two orthogonal product preparations.
t = R(1, 100)
rho_full = (1-t)*rho + t*sp.eye(9)/9
local_full = (1-t)*rho_A + t*sp.eye(3)/3
def pearson_full(O):
    mu = sp.simplify(sp.trace(local_full * O))
    v = sp.simplify(sp.trace(local_full * O*O) - mu**2)
    c = sp.simplify(sp.trace(rho_full * sp.kronecker_product(O,O)) - mu**2)
    return sp.factor(c/v)
paf = pearson_full(A)
pcf = pearson_full(C)
assert (paf, pcf) == (R(955317, 1872917), R(926431,1549731))
assert paf + pcf > 1

print('VERIFY_OK MUB=passed separable_decomposition=passed '
      'Pearson_A=17/33 Pearson_C=841/1394 excess=5449/46002 full_rank=passed')
