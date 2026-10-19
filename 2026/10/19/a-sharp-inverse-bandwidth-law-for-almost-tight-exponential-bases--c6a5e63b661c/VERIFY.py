#!/usr/bin/env python3
"""Reproduce exact Pell and perturbation identities and high-precision Gram checks.

Scientific proof of the all-bandwidth statements is in RESULT.md.
Requires Python 3, sympy and mpmath.
"""
import sympy as s
import mpmath as mp

p, q = 2, 1
pairs = []
for j in range(9):
    assert p*p - 2*q*q == 2
    assert (p % 3, q % 3) == ((2, 1) if j % 2 == 0 else (1, 2))
    assert q > 0 and p > 0 and p <= 2*q
    pairs.append((p, q))
    p, q = 17*p + 24*q, 12*p + 17*q

zeta = -s.Rational(1,2) + s.I*s.sqrt(3)/2
H = s.Matrix([
    [0, s.I*zeta**2, 2*s.I*zeta],
    [-s.I*zeta, 0, s.I*zeta**2],
    [-2*s.I*zeta**2, -s.I*zeta, 0],
])
assert s.simplify(H-H.conjugate().T) == s.zeros(3)
assert s.simplify(H.trace()) == 0
assert s.simplify(H.det()) == 0
assert s.simplify((H*H).trace()) == 12
x = s.symbols('x')
assert s.simplify(H.charpoly(x).as_expr() - (x**3-6*x)) == 0

mp.mp.dps = 90
heights = (mp.mpf(0), mp.mpf(1), mp.sqrt(2))
limit = 4*mp.pi/(3*mp.sqrt(3))
scaled_errors = []
for p, q in pairs[:7]:
    t = mp.mpf(q)/3
    V = mp.matrix([[mp.exp(2j*mp.pi*col*t*h)/mp.sqrt(3)
                    for col in range(3)] for h in heights])
    G = V.transpose_conj()*V
    eigs = sorted(mp.re(v) for v in mp.eig(G, left=False, right=False))
    assert eigs[0] > 0
    kappa = eigs[-1]/eigs[0]
    assert kappa > 1
    scaled_errors.append(abs(q*(kappa-1)-limit))
    if q >= 41:
        assert abs(q*(kappa-1)-limit) < mp.mpf(4)/q
assert all(a>b for a,b in zip(scaled_errors[1:6],scaled_errors[2:7]))
print('PASS: 9 exact Pell/residue checks, exact Hermitian characteristic polynomial,')
print('      7 high-precision Gram eigensystems and limit convergence.')
print('Pell coefficient limit:', mp.nstr(limit, 25))
print('Last scaled coefficient:', mp.nstr(pairs[6][1] * 0 + limit - scaled_errors[6], 25))
