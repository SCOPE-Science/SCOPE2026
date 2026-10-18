"""Independent finite-matrix checks for an absorbing Cartesian-product quantum walk.
Run: python verification.py . Requires numpy, scipy, sympy.
"""
from fractions import Fraction
from math import gcd
import numpy as np
import sympy as sp
from scipy.linalg import eigvals

def closed(m,n,row,col,resonant):
    delta_row=int(row==0); delta_col=int(col==0)
    off = Fraction(1 if delta_row else 1,1 if delta_row else m-1)*Fraction(1 if delta_col else 1,1 if delta_col else n-1)
    if not resonant:return off
    gap=Fraction((m-1)*(n-1),m*n*(m+n-2))*(Fraction(n*delta_col-1,n-1)-Fraction(m*delta_row-1,m-1))**2
    return off-gap

def spectral_projector(H,la,spectrum):
    N=H.rows
    P=sp.eye(N)
    for mu in spectrum:
        if la!=mu:
            P=P*(H-mu*sp.eye(N))/(la-mu)
    return P

def full_matrix(m,n,alpha,beta):
    Am=sp.ones(m)-sp.eye(m);An=sp.ones(n)-sp.eye(n)
    return alpha*sp.kronecker_product(Am,sp.eye(n))+beta*sp.kronecker_product(sp.eye(m),An)

# Distinct spectral-projector polynomials, never the factor-projector derivation of the theorem.
exact_checks=0
for m,n in ((2,2),(2,3),(3,2),(3,3),(3,4),(4,3),(4,4),(2,5),(5,2)):
 for resonant in (False,True):
  alpha,beta=(sp.Rational(n,m),sp.Integer(1)) if resonant else (sp.Integer(1),sp.Rational(m+1,n))
  # Ensure nonresonance (integer m and rational choice might accidentally coincide).
  if not resonant and m*alpha==n*beta:
   beta+=sp.Rational(1,2*n)
  H=full_matrix(m,n,alpha,beta)
  eigs=list(H.eigenvals().keys())
  eigs.sort()
  assert len(eigs)==(3 if resonant else 4)
  projectors=[spectral_projector(H,la,eigs) for la in eigs]
  s=0
  for i in range(m):
   for j in range(n):
    v=i*n+j
    actual=sum((P[v,s]**2/P[s,s] for P in projectors),sp.Integer(0))
    expected=closed(m,n,i,j,resonant)
    assert actual==sp.Rational(expected.numerator,expected.denominator), (m,n,resonant,i,j,actual,expected)
    exact_checks+=1
  assert sum(closed(m,n,i,j,resonant) for i in range(m) for j in range(n))==(3 if resonant else 4)

# Independently diagonalize the full lossy matrix and check the narrow eigenvalue linewidth.
width_checks=0
for m,n,gamma in ((2,2,.7),(2,5,1.5),(3,4,2.4),(4,4,.6),(5,7,1.3),(6,3,3.)):
 beta=1.3;alpha0=n*beta/m
 for delta in (-.002,-.001,.001,.002):
  alpha=alpha0+delta/m
  H=(alpha*np.kron(np.ones((m,m))-np.eye(m),np.eye(n))+
     beta*np.kron(np.eye(m),np.ones((n,n))-np.eye(n))).astype(complex)
  H[0,0]-=1j*gamma/2
  E0=alpha0*(m-1)-beta
  zz=[z for z in eigvals(H) if z.imag < -1e-11]
  near=min(zz,key=lambda z: abs(z.real-E0)+0.2*abs(z.imag))
  pred=4*m*n*(m-1)*(n-1)/(gamma*(m+n-2)**3)*delta**2
  actual=-2*near.imag
  assert abs(actual/pred-1)<.022,(m,n,gamma,delta,actual/pred)
  width_checks+=1
print('VERIFY_OK exact_projector_cases=',exact_checks,'linewidth_cases=',width_checks)
