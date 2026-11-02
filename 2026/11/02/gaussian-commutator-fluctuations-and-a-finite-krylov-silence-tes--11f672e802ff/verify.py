"""Standalone reproducibility checks for antithetic implicit splitting, NumPy/SymPy."""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad_vec

# Exact stage-product algebra for a noncommuting positive pair.
S0=sp.Matrix([[2,sp.Rational(1,2)],[sp.Rational(1,2),1]])
T0=sp.Matrix([[2,-sp.Rational(1,2)],[-sp.Rational(1,2),1]])
zz=sp.symbols('z', positive=True)
I=sp.eye(2)
RS=(I+zz*S0).inv()
RT=(I+zz*T0).inv()
P=sp.simplify((RT*RS+RS*RT)/2)
D=sp.simplify((RT*RS-RS*RT)/2)
C=(T0*S0-S0*T0)/2
assert C==sp.Matrix([[0,sp.Rational(1,2)],[-sp.Rational(1,2),0]])
assert (D-zz**2*C).applyfunc(lambda e: sp.limit(e/zz**3,zz,0)).shape==(2,2)
assert D != sp.zeros(2)
for h in (sp.Rational(1,10),sp.Rational(1,3),sp.Rational(1,100)):
 rS=(I+h*S0).inv();rT=(I+h*T0).inv()
 assert P.subs(zz,h)==sp.simplify((rT*rS+rS*rT)/2)
 assert D.subs(zz,h)==sp.simplify((rT*rS-rS*rT)/2)

S=np.asarray(S0,dtype=float);T=np.asarray(T0,dtype=float)
H=(S+T)/2
Cnp=(T@S-S@T)/2
x0=np.array([1.,0.]);L=1.0
assert np.min(np.linalg.eigvalsh(S))>0 and np.min(np.linalg.eigvalsh(T))>0

def limiting_covariance(H,C,x,L):
 def f(t):
  v=expm(-(L-t)*H)@C@expm(-t*H)@x
  return np.outer(v,v).reshape(-1)/2
 arr, _=quad_vec(f,0,L,epsabs=1e-12)
 return arr.reshape((len(x),len(x)))

sigma=limiting_covariance(H,Cnp,x0,L)
expected=(.5**2)/4*np.exp(-2*L)*(1-np.exp(-2*L))
assert np.allclose(sigma[1,1],expected,atol=1e-12)
assert abs(sigma[0,0])<1e-12 and abs(sigma[0,1])<1e-12

errors=[]
for n in (40,80,160,320,640):
 h=L/(2*n)
 rS=np.linalg.inv(np.eye(2)+h*S)
 rT=np.linalg.inv(np.eye(2)+h*T)
 p=(rT@rS+rS@rT)/2
 d=(rT@rS-rS@rT)/2
 m=x0.copy();cov=np.zeros((2,2))
 for _ in range(n):
  cov=p@cov@p.T+d@cov@d.T+np.outer(d@m,d@m)
  m=p@m
 limit_cov=cov/h**3
 e=np.linalg.norm(limit_cov-sigma)
 errors.append(e)
 print(f'COV n={n} h={h:.8g} scaled_var={limit_cov[1,1]:.10f} target={sigma[1,1]:.10f} error={e:.3e}')
 assert e<.004
assert all(errors[j+1]<errors[j] for j in range(len(errors)-1)),errors

# Commuting operators have identically zero random ordering noise.
A=np.diag([1.,2.,3.]);B=np.diag([.25,1.2,5.])
rA=np.linalg.inv(np.eye(3)+.1*A);rB=np.linalg.inv(np.eye(3)+.1*B)
assert np.linalg.norm(rA@rB-rB@rA)<1e-14
assert np.linalg.norm((B@A-A@B)/2)<1e-14

# Zero covariance for a particular initial vector need not imply commutation.
U=np.zeros((3,3));U[:2,:2]=S
V=np.zeros((3,3));V[:2,:2]=T
U[2,2]=.4;V[2,2]=.9
HU=(U+V)/2;CU=(V@U-U@V)/2
e3=np.array([0.,0.,1.])
assert np.linalg.norm(CU)>0
assert np.linalg.norm(CU@e3)<1e-14
assert np.linalg.norm(limiting_covariance(HU,CU,e3,1.))<1e-14
print('VERIFY_OK exact resolvent products; Gaussian covariance limit; commuting and Krylov-null boundaries')
