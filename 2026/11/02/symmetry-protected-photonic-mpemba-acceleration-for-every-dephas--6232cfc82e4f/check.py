"""Reproduce the three-site dephasing-walk spectral and relaxation identities.

Requires Python 3, SymPy, NumPy, SciPy. The symbolic identities constitute
finite-dimensional algebra checks; the analytic root arguments appear in
RESULT.md. The numeric sampling is corroborative only.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

q,b=sp.symbols('q b',real=True)
z,w=sp.symbols('z w')
E=lambda i,j:sp.eye(3)[:,i]*sp.eye(3)[j,:]
H=E(0,1)+E(1,0)+E(1,2)+E(2,1)
a12=sp.I*(E(0,1)-E(1,0))
a23=sp.I*(E(1,2)-E(2,1))
P=E(0,0)-2*E(1,1)+E(2,2)
A=a12-a23
C=E(0,2)+E(2,0)
U=E(0,0)-E(2,2)
V=a12+a23
Z=E(0,1)+E(1,0)-E(1,2)-E(2,1)
W=sp.I*(E(0,2)-E(2,0))
basis=[sp.eye(3),H,P,A,C,U,V,Z,W]
B=sp.Matrix.hstack(*[M.reshape(9,1) for M in basis])
assert B.det()!=0

def L(M):
    return -sp.I*(H*M-M*H)-q*(M-sp.diag(*[M[j,j] for j in range(3)]))
M=B.inv()*sp.Matrix.hstack(*[L(X).reshape(9,1) for X in basis])
expected=sp.diag(0,-q)
even3=sp.Matrix([[0,-2,0],[3,-q,1],[0,-2,-q]])
odd2=sp.Matrix([[0,-2],[1,-q]])
other2=sp.Matrix([[-q,-1],[2,-q]])
expected=sp.diag(0,-q,even3,odd2,other2)
assert M==expected
p=z**3+2*q*z**2+(q**2+8)*z+6*q
assert sp.factor(even3.charpoly(z).as_expr()-p)==0
assert sp.factor(odd2.charpoly(z).as_expr()-(z*z+q*z+2))==0
assert sp.factor(other2.charpoly(z).as_expr()-((z+q)**2+2))==0
assert sp.simplify(sp.discriminant(p,z)+4*(2*q**4-61*q*q+512))==0
assert sp.simplify(p.subs(z,-2*q/3)+2*q*(q-3)*(q+3)/27)==0
# The cubic's Hurwitz stability after shifting its roots by the odd spectral abscissa.
def hcoeff(a):
 pp=sp.Poly(sp.expand(p.subs(z,w+a)),w)
 return [sp.factor(t) for t in pp.all_coeffs()]
cf=hcoeff(-q/2)
assert all(sp.simplify(a-b)==0 for a,b in zip(cf,[1,q/2,(32-q*q)/4,q*(16-q*q)/8]))
assert sp.factor(cf[1]*cf[2]-cf[3])==2*q
cf=hcoeff(-b).copy()
cf=[sp.factor(c.subs(q,b+2/b)) for c in cf]
assert all(sp.simplify(a-d)==0 for a,d in zip(cf,[1,(4-b*b)/b,4*(b*b+1)/b**2,2*(4-b*b)/b]))
assert sp.simplify(cf[1]*cf[2]-cf[3]-2*(4-b*b)*(b*b+2)/b**3)==0

# Generator is independently assembled directly from 3x3 matrix units.
def generator(t):
    h=np.array(H,dtype=complex)
    d=np.array([1 if (i==j) else 0 for j in range(3) for i in range(3)])
    return -1j*(np.kron(np.eye(3),h)-np.kron(h.T,np.eye(3))) - t*np.diag(1-d)

def rate_odd(t):
    if t <= 2*math.sqrt(2):return -t/2
    return (-t+math.sqrt(t*t-8))/2

def rate_even(t):
    roots=np.roots([1,2*t,t*t+8,6*t])
    rr=float(roots[np.argmin(abs(roots.imag))].real)
    return (-t-rr/2) if t<=3 else rr

checks=12
for t in np.geomspace(0.003,300,65):
    actual=np.linalg.eigvals(generator(t))
    expected_roots=np.r_[0,-t,np.roots([1,2*t,t*t+8,6*t]),np.roots([1,t,2]),-t+1j*np.sqrt(2),-t-1j*np.sqrt(2)]
    assert len(actual)==9
    assert np.max(np.min(abs(actual[:,None]-expected_roots[None,:]),axis=1))<2e-7*max(1,t)
    e,o=rate_even(t),rate_odd(t)
    assert e<o-1e-10*min(t,1/t)
    checks+=3

for t in [0.05,0.2,0.5,1.,2.,2*np.sqrt(2),3.,5.,10.,30.]:
    G=generator(t)
    R=np.diag([1,-2,1]).astype(complex)
    R=-R/3
    O=np.diag([1,0,-1]).astype(complex)*0.12
    for tm in [0.2,1.0,2.0]:
        m=expm(G*tm)
        ev=(m@R.flatten('F')).reshape((3,3),order='F')
        ov=(m@O.flatten('F')).reshape((3,3),order='F')
        assert np.allclose(ev,ev.conj().T,atol=1e-11)
        assert np.allclose(ov,ov.conj().T,atol=1e-11)
        assert abs(np.trace(ev))<1e-11
        assert abs(np.trace(ov))<1e-11
        assert np.all(np.linalg.eigvalsh(np.eye(3)/3+ev)>=-1e-10)
        assert np.all(np.linalg.eigvalsh(np.eye(3)/3+ov)>=-1e-10)
        assert np.max(abs(ev-ev[::-1,::-1]))<1e-10
        assert np.max(abs(ov+ov[::-1,::-1]))<1e-10
        checks+=6
print('PASS',checks,'symbolic, spectral, positivity and symmetry checks')
for t in [0.01,1.,2*np.sqrt(2),3.,8.,100.]:
    print('q=',round(t,6),'even envelope=',round(rate_even(t),8),'odd envelope=',round(rate_odd(t),8),'acceleration=',round(rate_even(t)/rate_odd(t),6))
