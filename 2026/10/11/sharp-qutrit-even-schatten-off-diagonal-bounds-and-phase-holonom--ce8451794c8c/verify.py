"""Reproducible checks for qutrit off-diagonal Schatten moments.

Requirements: Python 3.10+ and NumPy. Finite checks supplement the analytic proof.
"""
from fractions import Fraction
from math import pi, sqrt, cos
import numpy as np


def add_scaled(out, p, factor, da, db):
    for (a, b), c in p.items():
        key = (a + da, b + db)
        out[key] = out.get(key, Fraction()) + factor * c


def trace_polynomials(up_to=32):
    polys = [{(0, 0): Fraction(3)}, {}, {(1, 0): Fraction(1)}]
    for k in range(3, up_to + 1):
        out = {}
        add_scaled(out, polys[k - 2], Fraction(1, 2), 1, 0)
        add_scaled(out, polys[k - 3], Fraction(1, 3), 0, 1)
        polys.append({key: x for key, x in out.items() if x})
    return polys


checks = 0
polys = trace_polynomials(32)
for k in range(2, 33):
    poly = polys[k]
    assert all(c >= 0 and 2*a+3*b == k for (a,b),c in poly.items())
    val = sum(c * Fraction(6)**a * Fraction(6)**b for (a,b),c in poly.items())
    assert val == Fraction(2**k+2*(-1)**k)
    if k % 2 == 0:
        assert all(b % 2 == 0 for a,b in poly)
    checks += 1
for m in range(3,17):
    assert any(b == 2 and c > 0 for (a,b), c in polys[2*m].items())
    assert sum(c * Fraction(6)**a * Fraction(-6)**b for (a,b), c in polys[2*m].items()) == 2**(2*m)+2
    checks += 2
assert polys[6] == {(3,0):Fraction(1,4),(0,2):Fraction(1,3)}
checks += 1

rng = np.random.default_rng(20261010)
for j in range(3500):
    Z = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    rho = Z @ Z.conj().T
    rho /= np.trace(rho).real
    t = float(np.trace(rho @ rho).real)
    B = rho - np.diag(np.diag(rho))
    eigen = np.linalg.eigvalsh(B)
    u = float(np.sum(eigen**2))
    v = float(np.sum(eigen**3))
    assert u <= t - 1/3 + 2e-12
    assert v*v <= u**3/6 + 2e-12
    assert abs(float(np.sum(eigen**6)) - (u**3/4+v*v/3)) < 2e-10
    for m in (3,4,5,7,10):
        pp = 2*m
        left = sum(abs(eigen)**pp)**(1/pp)
        right = ((2**pp+2)**(1/pp))/sqrt(6)*sqrt(max(0,t-1/3))
        assert left <= right + 4e-10
    checks += 8

for s in np.linspace(0.015,1,67):
    a=s/3
    for theta in np.linspace(0,2*pi,65):
        # The oriented edge product B[0,1]*B[1,2]*B[2,0] is a^3 exp(i theta).
        B=np.zeros((3,3),dtype=complex)
        B[0,1]=a; B[1,2]=a; B[2,0]=a*np.exp(1j*theta)
        B=B+B.conj().T
        rho=np.eye(3)/3+B
        eig=np.linalg.eigvalsh(rho)
        is_psd = eig[0] >= -3e-13
        permitted = 1-3*s*s+2*s**3*cos(theta) >= -3e-13
        assert is_psd == permitted
        if permitted:
            t = float(np.trace(rho @ rho).real)
            assert abs(t-(1/3+2*s*s/3)) < 1e-12
            assert abs(np.sum(np.abs(B))-2*s) < 1e-12
        checks += 3

for s in (0.02,0.1,0.4,0.5,0.7,0.99,1.0):
    w=np.ones(3)/sqrt(3)
    M=np.outer(w,w)-np.eye(3)/3
    t=1/3+2*s*s/3
    for sign in (1,-1):
        rho=np.eye(3)/3+sign*s*M
        feasible = np.linalg.eigvalsh(rho)[0] >= -2e-13
        assert feasible == (sign==1 or s <= 0.5)
        if feasible:
            B=rho-np.diag(np.diag(rho))
            ee=np.linalg.eigvalsh(B)
            for m in (3,4,5,7,10):
                p=2*m
                observed=sum(abs(ee)**p)**(1/p)
                target=s/3*(2**p+2)**(1/p)
                assert abs(observed-target)<2e-12
                checks += 1
            assert abs(float(np.trace(rho@rho).real)-t)<2e-12
            checks += 1
        checks += 1
print(f'VERIFY_OK checks={checks} exact_trace_recursion=60 random_density_matrices=3500 phase_grid=4355')
