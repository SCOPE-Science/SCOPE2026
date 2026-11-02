#!/usr/bin/env python3
"""Reproduce exact stationary correlations and singular Bell-scaling identities."""
import sympy as s
import numpy as np

a,r,q,y=s.symbols('a r q y',positive=True,real=True)
I=s.I
D=(1+r*r)**2+4*a*a*r*r
E=4*a*a+r*r+4
T=s.Matrix([[0,-2*a*r/D,2*a*r*r/D],[-2*a*r/D,2/E,-r/E],[2*a*r*r/D,-r/E,(4*a*a+r*r+2)/E]])

# Solve the reduced stationary Liouville equation by direct substitution.
H=s.Matrix([[-a,0,0],[0,-a,1],[0,1,a]])
rho0=s.Matrix([[s.Rational(1,2),-s.Rational(1,2),0],[-s.Rational(1,2),s.Rational(1,2),0],[0,0,0]])
x0=s.Rational(1,2)
x1=(4*a*a+r*r+2)/(2*E)
x2=1/E
z01=-r*r*(4*a*a+r*r+1)/(2*D)+I*a*r/D
z02=a*r*r/D-I*r*(r*r+1)/(2*D)
z12=-a/E+I*r/(2*E)
rho=s.Matrix([[x0,z01,z02],[s.conjugate(z01),x1,z12],[s.conjugate(z02),s.conjugate(z12),x2]])
assert all(s.factor(x)==0 for x in (r*(rho-rho0)+I*(H*rho-rho*H)))
assert s.factor(s.trace(rho)-1)==0

# Pauli correlations independently from the density matrix in the Bell basis.
sq=s.sqrt(2)
U=s.Matrix([[1/sq,1/sq,0],[0,0,1/sq],[0,0,1/sq],[-1/sq,1/sq,0]])
sx=s.Matrix([[0,1],[1,0]])
sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1)
P=[sx,sy,sz]
for j in range(3):
 for k in range(3):
  product=U.H*s.kronecker_product(P[j],P[k])*U
  assert s.factor(s.trace(rho*product)-T[j,k])==0,(j,k)

# Exact singular correlation limit and its CHSH spectrum.
limit=T.applyfunc(lambda x:s.limit(x.subs(r,q/(2*a)),a,s.oo))
expected=s.Matrix([[0,-q/(1+q*q),0],[-q/(1+q*q),0,0],[0,0,1]])
assert limit==expected
assert s.factor(expected.det())==-(q/(1+q*q))**2

# A rational CHSH witness and proof-equivalent factorization.
Ppoly=256*y**5-640*y**4-688*y**3-160*y**2-20*y-1
Rspecial=s.Rational(1,2)/a
witness=s.factor((T[2,2]**2+T[0,1]**2-1).subs(r,Rspecial))
fac=16*y*(4*y+1)**2*Ppoly/((16*y*y+16*y+1)**2*(32*y*y+8*y+1)**2)
assert s.factor(witness-fac.subs(y,a*a))==0
assert s.factor(Ppoly.subs(y,4))>0
assert s.factor((T[2,2]**2+T[0,1]**2).subs({a:2,r:s.Rational(1,4)})-1)>0

# Independent energy-basis Laplace transform, not reusing the reduced resolvent.
xx=np.array([[0,1],[1,0]],dtype=complex)
yy=np.array([[0,-1j],[1j,0]],dtype=complex)
zz=np.diag([1.,-1.]); eye=np.eye(2)
for aa,rr in [(2.,.25),(5.,.1),(.5,1.),(3.2,.001)]:
 Hamiltonian=-aa*np.kron(zz,zz)+.5*(np.kron(xx,eye)+np.kron(eye,xx))
 energies,vec=np.linalg.eigh(Hamiltonian)
 psi=np.array([0.,0.,0.,1.],dtype=complex)
 b=vec.conj().T@psi
 state_e=np.outer(b,b.conj())*(rr/(rr+1j*(energies[:,None]-energies[None,:])))
 state=vec@state_e@vec.conj().T
 measured=np.array([[np.trace(state@np.kron(p,t)).real for t in (xx,yy,zz)] for p in (xx,yy,zz)])
 closed=np.array(T.subs({a:aa,r:rr}),dtype=float)
 assert np.max(np.abs(measured-closed))<3e-10
 assert abs(np.trace(state)-1)<3e-10
print('PASS: stationary generator, Pauli correlations, singular scaling, rational positivity, and independent energy-basis checks')
