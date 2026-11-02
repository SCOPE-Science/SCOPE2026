"""Independent executable checks of the exact stationary concurrence at a resonant two-qubit gate.

Run: python verify.py
Requires Python, SymPy, NumPy, and SciPy. All cases are deterministic.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as s
from scipy.linalg import expm

I=s.I; a=s.sqrt(2); q=s.symbols('q', positive=True, real=True); z=s.symbols('z')
H=s.Matrix([[2-a,2-a,-I-a,I-a],
            [2-a,2-a,I-a,-I-a],
            [I-a,-I-a,2+a,2+a],
            [-I-a,I-a,2+a,2+a]])
unit=s.eye(4)
U=s.zeros(4)
for ell in [-2,0,2,8]:
    projector=s.eye(4)
    for other in [-2,0,2,8]:
        if other!=ell:
            projector=projector*(H-other*unit)/(ell-other)
    U += {-2:-I,0:1,2:I,8:1}[ell]*projector
U=U.applyfunc(s.simplify)
U_expected=s.Matrix([[1,1,1,-1],[1,1,-1,1],[-1,1,1,1],[1,-1,1,1]])/2
assert U==U_expected
assert U**4==unit
v=s.Matrix([1,0,0,0]); orbit=[]
for _ in range(4):
    orbit.append(v)
    v=U*v
assert v==orbit[0]
expected=[s.Matrix([1,0,0,0]),s.Matrix([1,1,-1,1])/2,
          s.Matrix([0,1,0,0]),s.Matrix([1,1,1,-1])/2]
assert orbit==expected
rho=sum([q**j*orbit[j]*orbit[j].conjugate().T for j in range(4)],s.zeros(4))/(1+q+q**2+q**3)
assert s.simplify(s.trace(rho))==1
sigmay=s.Matrix([[0,-I],[I,0]])
S=s.kronecker_product(sigmay,sigmay)
R=s.simplify(rho*S*rho.conjugate()*S)
trace_formula=q*(2*q**4-q**3+q**2+q+1)/(2*(q+1)*(q*q+1)**2)
product_formula=q*q*(q**3+3*q*q-q+1)**2/(16*(q+1)**2*(q*q+1)**4)
assert s.simplify(s.trace(R)-trace_formula)==0
assert s.simplify((s.trace(R)**2-s.trace(R**2))/2-product_formula)==0
assert s.cancel(R.charpoly(z).as_expr()-z*z*(z*z-trace_formula*z+product_formula))==0
concurrence_squared=(q*(1-q)/(1+q*q))**2
positive_sqrt_product=q*(q**3+3*q*q-q+1)/(4*(q+1)*(q*q+1)**2)
assert s.simplify(positive_sqrt_product**2-product_formula)==0
assert s.factor(trace_formula-2*positive_sqrt_product-concurrence_squared)==0
# Both odd quarter turns have the same spin-flip characteristic polynomial.
v0=s.Matrix([1,0,0,0])
for power in [1,3]:
    sequence=[(U**(power*j))*v0 for j in range(4)]
    rpow=sum([q**j*sequence[j]*sequence[j].conjugate().T for j in range(4)],s.zeros(4))/(1+q+q*q+q**3)
    Rpow=s.simplify(rpow*S*rpow.conjugate()*S)
    assert s.factor(s.trace(Rpow)-trace_formula)==0
    assert s.factor((s.trace(Rpow)**2-s.trace(Rpow**2))/2-product_formula)==0
assert U**2==s.kronecker_product(s.eye(2),s.Matrix([[0,1],[1,0]]))
assert s.factor(s.diff(q*(1-q)/(1+q*q),q)-(1-2*q-q*q)/(1+q*q)**2)==0
qstar=s.sqrt(2)-1
assert s.simplify(qstar*(1-qstar)/(1+qstar*qstar)-(s.sqrt(2)-1)/2)==0

# Numerical check independently reconstructs U from a floating-point matrix exponential,
# and the stationary state from a finite geometric series, not from the closed formula.
H_num=np.array(H.evalf(),dtype=complex)
U_num=expm(1j*np.pi/4*H_num)
S_num=np.kron(np.array([[0,-1j],[1j,0]]),np.array([[0,-1j],[1j,0]]))
assert np.linalg.norm(U_num-np.array(U_expected,dtype=complex))<1e-12
rates=[0.02,0.07,0.13,0.25,0.4,2-math.sqrt(2),0.7,0.8,0.94,0.98]
for p in rates:
    decay=1-p; v=np.array([1,0,0,0],dtype=complex); rn=np.zeros((4,4),complex)
    n=0
    while decay**n>2e-14:
        rn += p*decay**n*np.outer(v,v.conj())
        v=U_num@v
        n+=1
    eig=np.sqrt(np.maximum(0,np.real(np.linalg.eigvals(rn@S_num@rn.conj()@S_num))))
    eig.sort()
    c=max(0,float(eig[-1]-eig[-2]-eig[-3]-eig[-4]))
    formula=decay*(1-decay)/(1+decay*decay)
    assert abs(c-formula)<1e-7,(p,c,formula)
print('PASS: exact spectral projectors, quarter-turn classification, four-cycle, spin-flip traces, characteristic polynomial, concurrence, unique optimizer, and 10 independent numerical stationary reconstructions')
