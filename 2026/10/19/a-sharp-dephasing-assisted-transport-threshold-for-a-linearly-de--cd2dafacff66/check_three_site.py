#!/usr/bin/env python3
"""Independent algebraic and numerical checks for a three-site Lindblad transport theorem.

Run with Python 3 and sympy, numpy, scipy installed. All units use hopping J=1.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

k, y, g, x = sp.symbols('k y g x', positive=True, real=True)

R = 4*g**3 + 4*k*g**2 + (k**2 + 16*y + 8)*g + 2*k
N = (24*k*g**5
     +(44*k**2+48)*g**4
     +(30*k**3+120*k*y+120*k)*g**3
     +(9*k**4+108*k**2*y+88*k**2+192*y+96)*g**2
     +(k**5+26*k**3*y+24*k**3+96*k*y**2+144*k*y+72*k)*g
     +(k**4*y+2*k**4+16*k**2*y**2+32*k**2*y+12*k**2))
D = 2*k*(2*g+k)*R
T = N/D
P = sp.Poly(sp.expand(sp.diff(N,g)*D - N*sp.diff(D,g)),g)
Q = 256*y**3 + (32*k**2+512)*y**2 + (k**4+24*k**2+288)*y-12*k**2
F1 = 256*y**3 + (64*k**2+640)*y**2 +(3*k**4+28*k**2+256)*y-3*k**4-36*k**2
F2 = -3072*y**3-(256*k**2+3072)*y**2+(28*k**4+416*k**2-768)*y+3*k**6+144*k**4+624*k**2

def assert_zero(z,label):
    assert sp.cancel(z)==0, f'FAILED {label}: {sp.factor(z)}'
    return 1

ncheck=0
ncheck+=assert_zero(P.coeff_monomial(1)+2*k**4*Q,'P constant')
ncheck+=assert_zero(P.coeff_monomial(g)+8*k**3*F1,'P linear')
ncheck+=assert_zero(P.coeff_monomial(g**2)-2*k**2*F2,'P quadratic')
ncheck+=assert_zero(F1-3*Q +512*y**3+(32*k**2+896)*y**2+(44*k**2+608)*y+3*k**4,'sign identity 1')
ncheck+=assert_zero(F2+12*F1-(512*k**2+4608)*y**2-(64*k**4+752*k**2+2304)*y-3*k**6-108*k**4-192*k**2,'sign identity 2')
for power in range(3,9):
    poly=sp.Poly(P.coeff_monomial(g**power),k,y)
    assert all(c>0 for c in poly.coeffs()), (power,poly)
    ncheck+=1
ncheck+=assert_zero(sp.diff(T,g).subs(g,0)+Q/(8*k**2),'zero-noise slope')

# Symbolic nine-component master equation in the ordered matrix-unit basis.
M=sp.zeros(3)
for j in range(3):M[j,j]=j*x
for j in (0,1):M[j,j+1]=1;M[j+1,j]=1
L=sp.zeros(9)
for a in range(3):
 for b in range(3):
  ab=3*a+b
  for c in range(3):
   L[ab,3*c+b]+=-sp.I*M[a,c]
   L[ab,3*a+c]+=sp.I*M[c,b]
  if a!=b:L[ab,ab]-=g
  if a==2:L[ab,ab]-=k*sp.Rational(1,2)
  if b==2:L[ab,ab]-=k*sp.Rational(1,2)
probe=sp.zeros(9,1)
for j in range(3):probe[4*j]=1
X = L.T.inv()*probe
T_from_generator=-X[0]
ncheck+=assert_zero(T_from_generator-T.subs(y,x**2),'exact generator resolvent')

# Separate complex-operator implementation using column-major Kronecker products.
def numerical_T(k_,delta_,g_):
 H=np.array([[0,1,0],[1,delta_,1],[0,1,2*delta_]],complex)
 eye=np.eye(3,dtype=complex)
 pi=np.diag([0.,0.,1.]); damp=np.eye(9)-np.diag(np.eye(3).reshape(-1,order='F'))
 liou=-1j*(np.kron(eye,H)-np.kron(H.T,eye))
 liou-=g_*damp
 liou-=0.5*k_*(np.kron(eye,pi)+np.kron(pi.T,eye))
 rho=np.zeros(9,complex);rho[0]=1
 u=np.linalg.solve(-liou,rho)
 return np.trace(u.reshape(3,3,order='F')).real

f=sp.lambdify((k,y,g),T,'numpy')
for kk,dd,gg in itertools.product((0.3,1.,3.),(0.,0.25,1.,3.),(0.,0.1,1.,4.)):
 calc=numerical_T(kk,dd,gg)
 expected=float(f(kk,dd**2,gg))
 assert np.isclose(calc,expected,rtol=3e-10,atol=3e-10),(kk,dd,gg,calc,expected)
 ncheck+=1

# Parameter-space threshold: no interior optimum below, exactly one above.
for kk in (0.3,1.,3.,10.):
 qc=sp.Poly(Q.subs(k,sp.Rational(str(kk))),y)
 roots=[float(sp.re(v)) for v in sp.nroots(qc) if abs(float(sp.im(v)))<1e-9 and float(sp.re(v))>0]
 assert len(roots)==1, (kk,roots)
 yc=roots[0]
 for mult in (0.25,0.8,1.,1.2,3.):
  yy=mult*yc
  pp=sp.Poly(P.subs({k:kk,y:yy}),g)
  positive=[complex(v) for v in sp.nroots(pp,maxsteps=200) if abs(float(sp.im(v)))<1e-7 and float(sp.re(v))>1e-7]
  expected=1 if mult>1 else 0
  assert len(positive)==expected,(kk,mult,positive)
  ncheck+=1

# Large-gradient asymptotic from an exact polynomial expansion.
z,a=sp.symbols('z a',real=True)
p_exp=sp.Poly(sp.expand(P.as_expr().subs({g:z+a,y:z**2})),z)
ncheck+=assert_zero(p_exp.coeff_monomial(z**7)-6400*k**2*(3*a+k),'high-gradient next order')

# Cross-check integrated survival against direct density matrix propagation.
kk,dd,gg=1.,0.7,0.4
H=np.array([[0,1,0],[1,dd,1],[0,1,2*dd]],complex)
mat=-1j*(np.kron(np.eye(3),H)-np.kron(H.T,np.eye(3)))
mask=np.ones((3,3))-np.eye(3)
mat-=gg*np.diag(mask.reshape(-1,order='F'))
P3=np.diag([0.,0.,1.]);mat-=kk/2*(np.kron(np.eye(3),P3)+np.kron(P3,np.eye(3)))
r0=np.zeros(9);r0[0]=1
# Laplace-transform identity for survival: integral of e^{Lt} equals -L^{-1}.
vec=(-np.linalg.solve(mat,r0));direct=float(np.sum([vec[j+3*j].real for j in range(3)]))
assert abs(direct-float(f(kk,dd**2,gg)))<1e-9
ncheck+=1
print(f'{ncheck} symbolic, coefficient, and independent matrix checks passed')
print('k=1 sharp gradient threshold:',np.sqrt(float([t for t in sp.nroots(Q.subs(k,1)) if abs(float(sp.im(t)))<1e-8 and float(sp.re(t))>0][0])))
print('test T(k=1, delta=1, gamma=1):',float(f(1,1,1)))
