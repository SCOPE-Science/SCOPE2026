"""Finite-difference, transform, and Levy-exponent checks for a resetting diffusion.

Dependencies: numpy, scipy, mpmath, sympy. Run: python check_joint.py
All claims and mathematical definitions are in RESULT.md.
"""
import math
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
import mpmath as mp
import sympy as sp


def transform(r, D, a, s, u, v):
    k = math.sqrt((r + s) / D)
    kv = math.sqrt((r + s + v) / D)
    coeff = math.sinh(k * a) / (D * k)
    return 1.0 / ((r + s * math.cosh(k * a)) / (r + s) + coeff * (u + (s + v) / kv))


def discrete(r, D, a, s, u, v, h=0.015, xmax=10.0):
    ia = int(round(a / h))
    h = a / ia
    n = int(round(xmax / h))
    A = lil_matrix((n + 1, n + 1))
    b = np.zeros(n + 1)
    A[0, 0] = 1
    b[0] = 1
    for j in range(1, n):
        x = j * h
        A[j, j - 1] = D / h**2
        A[j, j] = -2 * D / h**2 - r - s - (v if x > a else 0) - (u / h if j == ia else 0)
        A[j, j + 1] = D / h**2
        A[j, ia] += r
    A[n, n] = 1.0
    A[n, ia] = -r / (r + s + v)
    sol = spsolve(A.tocsr(), b)
    return sol[ia]

# Algebraic checks from independent differentiation, not just numerical fitting.
A, D, r, q = sp.symbols('A D r q', positive=True)
phi = sp.sqrt(D) * q / sp.sqrt(r + q)
F = 1 / (1 + A * phi)
mu_R = sp.simplify(-sp.diff(F, q).subs(q, 0))
second_R = sp.simplify(sp.diff(F, q, 2).subs(q, 0))
assert sp.simplify(mu_R - A * sp.sqrt(D / r)) == 0
assert sp.simplify(second_R - (A * sp.sqrt(D) / r**sp.Rational(3, 2) + 2 * A**2 * D / r)) == 0
assert sp.simplify(sp.diff(phi, q).subs(q, 0) - sp.sqrt(D/r)) == 0
assert sp.simplify(sp.diff(phi, q, 2).subs(q, 0) + sp.sqrt(D)/r**sp.Rational(3,2)) == 0
print('Symbolic derivative identities: 4 passed')

cases = [
    (0.9, 0.5, 1.0, 0.0, 0.15, 0.35),
    (1.7, 1.3, 0.8, 0.23, 0.41, 0.72),
    (2.6, 0.75, 1.0, 0.91, 0.55, 0.27),
    (1.2, 1.0, 1.0, 0.46, 0.0, 0.52),
    (2.0, 0.5, 1.0, 0.65, 0.36, 0.0),
]
for idx,(rr,dd,aa,ss,uu,vv) in enumerate(cases,1):
    exact = transform(rr,dd,aa,ss,uu,vv)
    approximate = discrete(rr,dd,aa,ss,uu,vv, h=0.01, xmax=12.0)
    relative = abs(approximate/exact - 1)
    assert relative < 0.025, (idx, exact, approximate, relative)
    k = math.sqrt((rr+ss)/dd)
    margT = (rr+ss)/(rr+ss*math.exp(k*aa))
    assert abs(transform(rr,dd,aa,ss,0,0) - margT) < 1e-12
    s_ = math.sinh(aa*math.sqrt(rr/dd))
    margR = math.sqrt(rr*(rr+vv))/(math.sqrt(rr*(rr+vv))+vv*s_)
    assert abs(transform(rr,dd,aa,0,0,vv) - margR) < 1e-12
    print(f'Case {idx}: PDE relative error {relative:.6g}; two published marginals matched')

mp.mp.dps = 40
for rr,dd,vv in [(0.6,0.8,0.2),(2.1,1.3,0.85),(3.3,0.5,2.6)]:
    R,Dm,V = map(mp.mpf,(str(rr),str(dd),str(vv)))
    def levy_integrand(z):
        if z == 0:
            return V*mp.sqrt(Dm)/mp.sqrt(mp.pi)
        t=z*z
        return (1-mp.exp(-V*t))*mp.sqrt(Dm)*mp.exp(-R*t)*(1+2*R*t)/(mp.sqrt(mp.pi)*t)
    value=mp.quad(levy_integrand,[0,1,4,mp.inf])
    target=mp.sqrt(Dm)*V/mp.sqrt(R+V)
    assert abs(value-target)<mp.mpf('1e-17'), (value,target)
print('Three Levy integral checks: passed')

for rr,dd,aa in [(0.2,0.5,1),(1,0.7,1),(7,1.3,0.9)]:
    k=math.sqrt(rr/dd)
    S=math.sinh(aa*k)
    factor=S/math.sqrt(dd*rr)
    phi_prime=math.sqrt(dd/rr)
    cov=factor**2*phi_prime
    varL=factor**2
    varR=(S+S*S)/(rr*rr)
    corr=cov/math.sqrt(varL*varR)
    assert abs(corr-math.sqrt(S/(1+S)))<1e-12
print('Correlation identities: 3 passed; all checks successful')
