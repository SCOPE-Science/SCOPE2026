"""Standalone finite checks for an antipodal gain/loss quantum ring.

Dependencies: Python 3, sympy, numpy, scipy.  Analytic proof is in RESULT.md.
"""
import math
import sympy as sp
import numpy as np
from scipy.linalg import expm


def matrix(m, gamma):
    size = 2*m
    A = sp.zeros(size)
    for j in range(size):
        A[j, (j+1) % size] = 1
        A[(j+1) % size, j] = 1
    A[0, 0] = sp.I*gamma
    A[m, m] = -sp.I*gamma
    return A


def predicted(m, gamma, z):
    return sp.expand((z*z+gamma*gamma-4)*sp.chebyshevu(m-1,z/2)**2)


def nullity(A):
    return A.rows - A.rank()


z, g = sp.symbols('z g')
checks=0
for m in range(2, 7):
    A=matrix(m,g)
    cp=A.charpoly(z).as_expr()
    assert sp.simplify(cp-predicted(m,g,z))==0, ('characteristic polynomial',m)
    checks+=1
    A=matrix(m,sp.Integer(2))
    if m%2==0:
        expected=(2,3,4)
    else:
        expected=(1,2,2)
    actual=tuple(nullity(A**j) for j in (1,2,3))
    assert actual==expected,(m,'gamma2 Jordan',actual,expected)
    checks+=1

for m,k in [(3,1),(4,1),(5,1),(6,1),(6,2)]:
    q=sp.simplify(2*sp.cos(sp.pi*k/m))
    gamma=sp.simplify(sp.sqrt(4-q*q))
    A=matrix(m,gamma)
    for ev in (q,-q):
        X=A-ev*sp.eye(2*m)
        assert (nullity(X),nullity(X**2))==(2,3),(m,k,ev,'embedded Jordan')
        checks+=1

# Non-asymptotic numeric exponential corroboration (not a substitute for proof).
for m, gamma, power in [(3,2.,1),(4,2.,2),(3,math.sqrt(3),1)]:
    A=np.asarray(matrix(m,sp.Float(gamma)),dtype=np.complex128)
    scale=[]
    for t in (20.,40.,80.):
        norm=np.linalg.norm(expm(-1j*t*A),2)
        scale.append(norm / t**power)
    assert all(np.isfinite(scale)) and 1e-5<min(scale)<max(scale)<1e4,(m,gamma,scale)
    checks+=1

print(f'PASS: {checks} independent polynomial, nullity, and propagator checks.')
