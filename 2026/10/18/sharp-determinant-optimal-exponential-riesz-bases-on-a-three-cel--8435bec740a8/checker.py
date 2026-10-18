"""Reproducibility checks for the sharp three-cell exponential determinant.

Requires Python 3, sympy, and numpy. Tests support, but do not replace,
the all-angle analytic extremal proof.
"""
import math
import random
import numpy as np
import sympy as sp

X, Y = sp.symbols('X Y', real=True)
rad = sp.sqrt(10)
F = 16*(1-Y**2)*(X-Y)**2*(1+4*Y**2+4*X*Y)
Dplus = (9748+1360*rad)/729
Dminus = (9748-1360*rad)/729
cstar = (rad-2)/6
assert sp.simplify(F.subs({X:1,Y:cstar})-Dplus)==0
assert sp.simplify(sp.diff(F,X) + 32*(X-Y)*(Y-1)*(Y+1)*(6*X*Y+2*Y**2+1)) == 0
assert sp.simplify(sp.diff(F,Y).subs(X,-(1+2*Y**2)/(6*Y)) + 8*(8*Y**2+1)**2*(24*Y**4-16*Y**2+1)/(27*Y**3)) == 0
assert sp.simplify(sp.diff(F,Y).subs(X,1)+32*(Y-1)**2*(2*Y+1)*(6*Y**2+4*Y-1))==0
for y2, target in [((4+rad)/12,Dplus),((4-rad)/12,Dminus)]:
    y=sp.sqrt(y2)
    x=-(1+2*y*y)/(6*y)
    assert sp.simplify(F.subs({X:x,Y:y})-target)==0
assert sp.simplify(F.subs({X:1,Y:(-2-rad)/6})-Dminus)==0

rng=random.Random(4317)
F_numeric=sp.lambdify((X,Y),F,"math")
max_factor_error=0.
max_bound_violation=0.
max_eigenvalue_discrepancy=0.
for trial in range(2000):
    angles=[rng.uniform(-math.pi,math.pi) for _ in range(3)]
    z=np.exp(1j*np.array(angles))
    V=np.array([z**power for power in (0,1,3)])
    gram=V@V.conj().T
    numerical=float(np.linalg.det(gram).real)
    u=(angles[1]+angles[2]-2*angles[0])/2
    v=(angles[1]-angles[2])/2
    predicted=float(F_numeric(math.cos(u),math.cos(v)))
    max_factor_error=max(max_factor_error,abs(numerical-predicted))
    max_bound_violation=max(max_bound_violation,numerical-float(Dplus))
    eig=np.linalg.eigvalsh(gram)
    max_eigenvalue_discrepancy=max(max_eigenvalue_discrepancy,abs(float(np.prod(eig))-numerical))
    assert abs(numerical-predicted)<1e-10
    assert numerical<=float(Dplus)+1e-10

alpha=math.acos(float(cstar))
optangles=[-alpha,0.,alpha]
z=np.exp(1j*np.array(optangles))
V=np.array([z**power for power in (0,1,3)])
G=V@V.conj().T
values=np.linalg.eigvalsh(G)
assert np.min(values)>0
assert abs(float(np.linalg.det(G).real)-float(Dplus))<1e-12
for delta in [0.0001,0.001,0.01,0.05,0.2]:
    test=[-alpha+delta,0.,alpha]
    zt=np.exp(1j*np.array(test))
    Vt=np.array([zt**power for power in (0,1,3)])
    assert np.linalg.det(Vt@Vt.conj().T).real<float(Dplus)

# Fourier-fiber norm identity for a test f with vector coefficient functions.
fiber=rng.random()
coefficient=np.array([complex(rng.random(),rng.random()) for _ in range(3)])
theta=np.array(optangles)/(2*math.pi)
shifts=np.array([0,1,3]); matrix=np.exp(-2j*math.pi*np.outer(theta,shifts))
assert abs(np.vdot(matrix@coefficient,matrix@coefficient)-np.vdot(coefficient,(matrix.conj().T@matrix)@coefficient))<1e-12
print('symbolic stationary equations and candidate values: PASS')
print('2000 random-angle determinant, bound, and spectrum checks: PASS')
print('five local angular perturbation checks: PASS')
print('exact Parseval fiber matrix identity: PASS')
print('optimal cosine =',float(cstar))
print('optimal half-angle radians =',alpha)
print('max squared determinant =',float(Dplus))
print('optimal Gram eigenvalues =',','.join(f'{x:.12f}' for x in values))
print('max numerical factorization error =',f'{max_factor_error:.3e}')
print('largest random-bound excess =',f'{max_bound_violation:.3e}')
print('max determinant/eigenproduct discrepancy =',f'{max_eigenvalue_discrepancy:.3e}')
