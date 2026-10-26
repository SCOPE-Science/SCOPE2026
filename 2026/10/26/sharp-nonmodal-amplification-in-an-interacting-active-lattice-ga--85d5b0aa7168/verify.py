#!/usr/bin/env python3
"""Replay finite Fourier-mode identities for the active lattice-gas hydrodynamics.

Symbolic identities are algebraic tests, not a substitute for the infinite-dimensional
semigroup proof in RESULT.md. Requirements: sympy, numpy, scipy.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm, svdvals

r, k, pe = sp.symbols('r k pe', real=True)
B = (1-r)*(2*r-1)
assert sp.simplify(r**2-4*B-(3*r-2)**2) == 0
A = sp.Matrix([[-k**2,-sp.I*pe*k*(1-r)],
               [-sp.I*pe*k*(1-2*r),-k**2-2]])
H = sp.simplify((A+A.conjugate().T)/2)
assert sp.simplify(H[0,1]+sp.I*pe*k*r/2) == 0
assert sp.simplify(H.trace()+2*k**2+2) == 0
assert sp.simplify(H.det()-k**2*(k**2+2)+pe**2*k**2*r**2/4) == 0
assert sp.simplify((A+(k**2+1)*sp.eye(2))**2-(1+pe**2*k**2*B)*sp.eye(2)) == sp.zeros(2)
assert sp.simplify(A.subs(r,sp.Rational(2,3))-A.subs(r,sp.Rational(2,3)).conjugate().T)==sp.zeros(2)
assert sp.simplify(A.subs(r,sp.Rational(1,2))[1,0])==0

# Upper-right entry in e^{t A_k} for r=1/2,
# and the exact unique optimum of its scalar envelope.
t = sp.symbols('t', positive=True, real=True)
b = pe*k/4*sp.exp(-k**2*t)*(1-sp.exp(-2*t))
assert sp.simplify(sp.diff(b,t).subs(t,sp.log(1+2/k**2)/2))==0

# Check the spectral eigenvalues, numerical abscissa, and actual finite-time gain.
cases = [(.6,6.,1.,True,True), (2/3,5.,1.,True,False),
         (.5,12.,1.,True,True), (.8,4.9,1.,True,True), (.8,4.,1.,True,False)]
for density,p,w,stable,amplify in cases:
    matrix = np.array([[-w*w,-1j*p*w*(1-density)],
                       [-1j*p*w*(1-2*density),-w*w-2]],dtype=complex)
    herm = (matrix + matrix.conj().T)/2
    abscissa = max(np.linalg.eigvalsh(herm))
    formula = -w*w-1+math.sqrt(1+(p*w*density/2)**2)
    assert abs(abscissa-formula)<1e-12
    spectrum = np.linalg.eigvals(matrix)
    if stable: assert max(spectrum.real)<-1e-8
    grid = np.linspace(0,4,1001)
    max_gain = max(svdvals(expm(matrix*tt))[0] for tt in grid)
    assert (max_gain>1+1e-3) == amplify,(density,p,w,max_gain)
    print(f'r={density:.9f}, Pe={p:.3f}, k={w:.3f}, spectral_abscissa={max(spectrum.real):.8f}, numerical_abscissa={abscissa:.8f}, sampled_peak_norm={max_gain:.8f}')

L=2*math.pi
ks=np.arange(1,1001)*2*math.pi/L
C=(ks/(2*(ks*ks+2)))*(ks*ks/(ks*ks+2))**(ks*ks/2)
idx=int(np.argmax(C))
print(f'L=2pi: maximizing Fourier mode n={idx+1}, sharp half-filling high-Pe coefficient C_L={C[idx]:.12f}')
assert idx == 0
for p in [100,500]:
    k1=1.
    b_peak=p*C[idx]
    t_star=.5*math.log(1+2/k1**2)
    matrix=np.array([[-k1*k1,-1j*p*k1/2],[0,-k1*k1-2]],dtype=complex)
    gain=svdvals(expm(matrix*t_star))[0]
    assert b_peak <= gain <= b_peak + 1+1e-9
    print(f'Pe={p}: lower={b_peak:.9f} gain(t*)={gain:.9f} upper={b_peak+1:.9f}')
print('PASS: symbolic identities, stable nonmodal witnesses, half-filling gain bounds.')
