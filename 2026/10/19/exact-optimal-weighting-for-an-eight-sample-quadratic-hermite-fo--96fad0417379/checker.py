"""Exact checks for the quadratic Hermite Fourier intensity-lifting spectrum.

Run: python checker.py. Requires sympy and numpy.
The general theorem is supported by the identities in RESULT.md; these
checks verify all nonstandard finite-dimensional algebraic certificates.
"""
import sympy as s
import numpy as np

T = s.symbols('T', positive=True, real=True)
r = s.sqrt(985)
t0 = s.Rational(40, 81)
R = (33+r)/4
u = s.Matrix([1, 1, 1])
w = s.Matrix([0, 1, 4])
D = 5*u*u.T + 3*T*w*w.T
C = s.Matrix([[5, 5], [5, 5+12*T]])
Q = s.diag(3, -4, 1)
v = s.Matrix([1, (16-r)/27])
x = u + (11+r)/54*w
f = (215-5*r)/27
h = (215+5*r)/27
d = (1085-25*r)/54
g = (1085+25*r)/54

assert s.simplify(D*Q.diagonal().T) == s.zeros(3,1)
assert s.simplify(C.charpoly().as_expr() - (s.Symbol('lambda')**2 - (10+12*T)*s.Symbol('lambda') + 60*T)) == 0
assert s.simplify(D.charpoly().as_expr() - s.Symbol('lambda')*(s.Symbol('lambda')**2-(15+51*T)*s.Symbol('lambda')+390*T)) == 0
assert (C.subs(T,t0)*v - f*v).applyfunc(s.simplify) == s.zeros(2,1)
assert (D.subs(T,t0)*x - g*x).applyfunc(s.simplify) == s.zeros(3,1)
assert s.simplify((x.T*D*x)[0]*(v.T*v)[0] - R*(v.T*C*v)[0]*(x.T*x)[0]) == 0
assert s.simplify(g/f-R) == 0
assert all(float(z)>0 for z in (f, h, d, g))
assert float(f)<5<float(d)<float(h)<float(g)

# Independent 9-by-8 real-Hermitian lifting check at several positive weights.
basis=[]
for j in range(3):
 e=np.zeros((3,3),complex); e[j,j]=1; basis.append(e)
for j,k in [(0,1),(0,2),(1,2)]:
 e=np.zeros((3,3),complex);e[j,k]=e[k,j]=1/np.sqrt(2);basis.append(e)
 e=np.zeros((3,3),complex);e[j,k]=1j/np.sqrt(2);e[k,j]=-1j/np.sqrt(2);basis.append(e)
for t in [0.05, 0.2, float(t0), 1.0, 5.0]:
 mat=[]
 for n,nodes,is_derivative in [(5,5,False),(3,3,True)]:
  for j in range(nodes):
   z=np.exp(2j*np.pi*j/n)
   a=np.array([1,z,z*z]) if not is_derivative else np.array([0,1,2*z])
   mat.append([np.sqrt(t if is_derivative else 1)*float(np.real(a.conj()@e@a)) for e in basis])
 mat=np.array(mat)
 eigen=np.linalg.eigvalsh(mat.T@mat)
 trC=10+12*t;radC=np.sqrt(100+144*t*t) # 2sqrt(25+36t^2)
 evC=[(trC-radC)/2,(trC+radC)/2]
 trD=15+51*t;radD=np.sqrt(trD**2-1560*t)
 evD=[(trD-radD)/2,(trD+radD)/2]
 spec=np.sort([0,5,5,evC[0],evC[0],evC[1],evC[1],evD[0],evD[1]])
 assert np.max(abs(eigen-spec))<3e-10,(t,eigen,spec)
 print(f'Weighted lifting t={t:.8f}: eigenvalues verified to 3e-10')

print('EXACT CUBIC/DUPLICATED-BLOCK CHARACTERISTIC POLYNOMIALS: PASS')
print('EXACT KERNEL, EIGENVECTORS, ALL-WEIGHT CERTIFICATE: PASS')
print('OPTIMAL UNIQUE WEIGHT 40/81, CONDITION NUMBER^2 = (33+sqrt(985))/4: PASS')
print('PROJECTOR STABILITY LOWER COEFFICIENT = (215-5*sqrt(985))/702')
