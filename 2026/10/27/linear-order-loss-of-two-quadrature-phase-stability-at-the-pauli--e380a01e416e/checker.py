"""Numerical checks for quantitative fractional-Fourier intensity stability on three Hermite modes."""
import numpy as np
from math import pi,sqrt
from numpy.polynomial.hermite import hermgauss

# Real basis for Hermitian 3x3 matrices, with Frobenius-orthonormal columns.
E=[]
for j in range(3):
 M=np.zeros((3,3),complex);M[j,j]=1;E.append(M)
for j,k in ((0,1),(0,2),(1,2)):
 M=np.zeros((3,3),complex);M[j,k]=M[k,j]=1/sqrt(2);E.append(M)
 M=np.zeros((3,3),complex);M[j,k]=1j/sqrt(2);M[k,j]=-1j/sqrt(2);E.append(M)

def basis(x):
 h0=pi**(-.25)*np.exp(-x*x/2)
 return np.vstack((h0,sqrt(2)*x*h0,(2*x*x-1)/sqrt(2)*h0))

def out_matrix(delta):
 # Hermite quadrature integrates squared intensities: exp(-2x²) polynomial deg <=8.
 z,w=hermgauss(14);x=z/sqrt(2);W=w/sqrt(2)
 b=basis(x)
 res=[]
 for theta in (0,delta):
  phase=np.exp(-1j*np.arange(3)*theta)
  row=[]
  for H in E:
   y=np.einsum('jn,jk,kn->n',b*phase[:,None],H,b*np.conj(phase[:,None])).real
   row.append(y)
  res.append(np.array(row).T*np.sqrt(W)[:,None]*np.exp(x*x)[:,None])
 return np.vstack(res)

def K(delta):
 c=np.cos(delta); H=np.zeros((3,3),complex)
 H[0,0]=sqrt(2)*c;H[1,1]=-sqrt(2)*c
 H[0,2]=np.exp(-1j*delta);H[2,0]=np.conj(H[0,2])
 return H

def coords(H):
 return np.array([np.trace(H@F).real for F in E])

for angle in (.23,.7,1.1,pi/2-.02,pi/2,pi/2+.02):
 M=out_matrix(angle);sing=np.linalg.svd(M,compute_uv=False)
 residual=np.linalg.norm(M@coords(K(angle)))
 assert len(sing)==9 and sing[-1]<1e-12 and sing[-2]>.01
 assert residual<5e-14
 eig=np.linalg.eigvalsh(K(angle))
 assert np.isclose(np.linalg.det(K(angle)).real,sqrt(2)*np.cos(angle),atol=1e-12)
 print(f'angle={angle:.12f} rank=8 null_residual={residual:.3e} next_singular={sing[-2]:.6f} detK={np.linalg.det(K(angle)).real:.6f}')
H0=K(pi/2)
for eps in (0.01,0.001,0.0001):
 angle=pi/2+eps
 ratio=np.linalg.norm(out_matrix(angle)@coords(H0))/np.linalg.norm(H0)
 hproduct=np.sqrt(3/(8*np.sqrt(2*pi)))
 expected=sqrt(2)*abs(np.sin(2*angle))*hproduct
 assert abs(ratio-expected)<1e-10
 print(f'delta_minus_pi_over_2={eps} witness_ratio={ratio:.12e} divided_by_gap={ratio/eps:.9f}')
print('PASS: exact null direction, fixed rank, determinant, and linear witness checked')
