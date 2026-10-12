"""Reproducible finite checks for sharp same-score dependence envelopes.

Run: python longla_spectral_checker.py
Requires Python 3.10+, numpy, sympy. The analytical proof is in RESULT.md.
"""
from fractions import Fraction
from math import cos, pi, sqrt
import numpy as np
import sympy as sp

checks = 0

def make_matrices(lam, n):
    d = len(lam) + 1
    T = np.zeros((d, d))
    for i, v in enumerate(lam):
        T[i, i+1] = v
    J = []
    for k in range(1, d):
        A = np.zeros((d, d))
        for i in range(d-k):
            w = float(np.prod(lam[i:i+k]))
            A[i, i+k] = A[i+k, i] = w/2
        J.append(A)
    H = np.eye(d)
    W = np.eye(d)
    for k, A in enumerate(J, 1):
        H += 2*A
        W += 2*max(0, 1-k/n)*A
    return T, J, H, W

rng = np.random.default_rng(2026)
for m in range(1, 9):
    lam = [(-1)**i*(i+1)/(16*m*m) for i in range(m)]
    d = m+1
    for n in (1, 2, m+1, m+5, 30):
        T, J, H, W = make_matrices(lam, n)
        assert np.max(np.abs(np.linalg.matrix_power(T, m+1))) < 1e-13
        checks += 1
        for k in range(1, m+1):
            assert np.allclose(J[k-1],(np.linalg.matrix_power(T,k)+np.linalg.matrix_power(T,k).T)/2)
            ev = np.linalg.eigvalsh(J[k-1])
            assert abs(ev[0]+ev[-1]) < 2e-12
            a = rng.normal(size=d); a /= np.linalg.norm(a)
            assert abs(a@J[k-1]@a-a@np.linalg.matrix_power(T,k)@a)<1e-12
            checks += 3
        a=rng.normal(size=d); a/=np.linalg.norm(a)
        finite_var = 1 + 2*sum((1-k/n)*a@J[k-1]@a for k in range(1,min(m,n-1)+1))
        assert abs(a@W@a-finite_var)<1e-12
        assert np.linalg.eigvalsh(W)[0] <= 1+1e-12 <= np.linalg.eigvalsh(W)[-1]+1e-12
        assert np.linalg.eigvalsh(H)[0] <= 1+1e-12 <= np.linalg.eigvalsh(H)[-1]+1e-12
        checks += 3

for m in range(1, 10):
    t = 1/(4*m)
    T,J,H,W = make_matrices([t]*m, 300)
    got = np.linalg.eigvalsh(J[0])[-1]
    predicted = t*cos(pi/(m+2))
    assert abs(got-predicted) < 1e-12
    checks += 1

r=sp.Rational(1,4)
J=sp.Matrix([[0,r/2,0],[r/2,0,r/2],[0,r/2,0]])
a=sp.Matrix([sp.Rational(1,2), sp.sqrt(2)/2, sp.Rational(1,2)])
assert sp.simplify((a.T*a)[0]-1)==0
assert sp.simplify((a.T*J*a)[0]-sp.sqrt(2)/8)==0
assert sp.sqrt(2)/8 > sp.Rational(1,8)
H=sp.Matrix([[1,r,r*r],[r,1,r],[r*r,r,1]])
assert set(H.eigenvals())=={sp.Rational(15,16),(33+sp.sqrt(129))/32,(33-sp.sqrt(129))/32}
checks += 4
# Independent two-dimensional Gauss-Legendre quadrature of the actual copula densities.
x0,w0=np.polynomial.legendre.leggauss(144)
x=(x0+1)/2; w=w0/2
phi=np.column_stack([np.sqrt(2)*np.sin(2*np.pi*x),
                     np.sqrt(2)*np.cos(2*np.pi*x),
                     np.sqrt(2)*np.sin(4*np.pi*x)])
f=phi@np.array([.5,1/np.sqrt(2),.5])
c1=1+.25*np.outer(phi[:,0],phi[:,1])+.25*np.outer(phi[:,1],phi[:,2])
c2=1+.0625*np.outer(phi[:,0],phi[:,2])
assert np.min(c1)>=-1e-12
assert abs(np.dot(w,f))<1e-12
assert abs(np.dot(w,f*f)-1)<1e-12
assert abs((w*f)@c1@(w*f)-float(sp.sqrt(2)/8))<1e-12
assert abs((w*f)@c2@(w*f)-float(sp.Rational(1,64)))<1e-12
checks+=5
print(f"PASS: {checks} finite matrix, Rayleigh-quotient, and exact symbolic assertions")
print("Lag-one witness =",sp.sqrt(2)/8,"; published bound =",sp.Rational(1,8))
print("Long-run variance spectral endpoints =",(33-sp.sqrt(129))/32,(33+sp.sqrt(129))/32)
