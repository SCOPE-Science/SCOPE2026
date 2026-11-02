"""Independent symbolic and numerical checks for one-pulse three-site absorption."""
import sympy as s
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

k,g,d=s.symbols('k g d',positive=True,real=True)
I=s.I
H=s.Matrix([[0,1,0],[1,d,1],[0,1,0]])
P2=s.diag(0,1,0); P3=s.diag(0,0,1)
P=2*k*g*g+(k*k+8)*g+2*k
Tm=s.Rational(3,2)*g+(k*k+6)/(2*k)+d*d*k*(6*g+k)/(2*P)
p,q,r,a,b,c,z,e,f=s.symbols('p q r a b c z e f',real=True)
X=s.Matrix([[p,a+I*b,c+I*z],[a-I*b,q,e+I*f],[c-I*z,e-I*f,r]])
L=-I*(H*X-X*H)-g*(P2*X+X*P2-2*P2*X*P2)-k*s.Rational(1,2)*(P3*X+X*P3)
vs=[p,q,r,a,b,c,z,e,f]
E=[]
for ii,jj in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
 E.append(s.expand(s.re(L[ii,jj])))
 if ii!=jj:E.append(s.expand(s.im(L[ii,jj])))
M=s.linear_eq_to_matrix(E,vs)[0]
Y=M.inv()*s.Matrix([-1,0,0,0,0,0,0,0,0])
assert s.simplify(Y[0]+Y[1]+Y[2]-Tm)==0
assert s.simplify(Y[2]-1/k)==0
assert s.simplify(Y[4]-s.Rational(1,2))==0
assert s.simplify(Y[8]-s.Rational(1,2))==0
assert s.simplify(Y[6]+d*(4*g+k)/P)==0
assert s.simplify(Y[3]+d*k*(2*g+k)/(2*P))==0
assert s.simplify(Y[7]-d*g*k/P)==0
print('symbolic integrated Lyapunov equations and 7 identities PASS')
Q=12*g*g+4*k*g+k*k-4
S=k*k+2*k*g-4
R=48*g**3*k+24*g*g*k*k+g*(12*k**3-48*k)+2*k**4-64
Gnum=6*P/(k*S)
assert s.simplify(s.diff(Tm,g)-(3*P**2-d*d*k*k*Q)/(2*P**2))==0
assert s.simplify(Tm-Tm.subs(g,0)-g*(6*P-d*d*k*S)/(4*P))==0
assert s.simplify(2*s.diff(P,g)*Q-P*s.diff(Q,g)-R)==0
assert s.simplify(s.diff(R,g)-12*k*Q)==0
assert s.simplify(s.factor(s.diff(Gnum,g))-6*(s.diff(P,g)*S-2*k*P)/(k*S**2))==0
assert s.simplify(s.diff(P,g)*S-2*k*P-(4*k*k*g*g+4*k*(k*k-4)*g+k**4-32))==0
print('symbolic derivative, global comparison, threshold phase proofs PASS')

# independent 9-dimensional numerical Liouvillian representation and numerical survival integral

def numerical_T(k0,g0,d0):
 h=np.array([[0.,1.,0.],[1.,d0,1.],[0.,1.,0.]])
 p2=np.diag([0.,1.,0.]);p3=np.diag([0.,0.,1.]);ident=np.eye(3)
 Lc=-1j*(np.kron(ident,h)-np.kron(h.T,ident))
 # Vec in column-major; L(A X B)= (B^T kron A)vec(X)
 Ld=-g0*(np.kron(ident,p2)+np.kron(p2.T,ident)-2*np.kron(p2.T,p2))
 Ls=-k0/2*(np.kron(ident,p3)+np.kron(p3.T,ident))
 LL=Lc+Ld+Ls
 rho0=np.zeros((3,3));rho0[0,0]=1
 vec=np.linalg.solve(-LL,rho0.reshape(9,order='F'))
 direct=vec.reshape((3,3),order='F').trace().real
 # sample finite-time evolution for independent exponential matrix checks
 for tt in (0.03,0.2,1.,4.):
  mat=expm(LL*tt).dot(rho0.reshape(9,order='F')).reshape((3,3),order='F')
  assert mat.trace().real>=-1e-9
  assert np.linalg.eigvalsh((mat+mat.conj().T)/2).min()>-1e-9
 return direct

def formula(k0,g0,d0):
 p0=2*k0*g0**2+(k0*k0+8)*g0+2*k0
 return 1.5*g0+(k0*k0+6)/(2*k0)+d0*d0*k0*(6*g0+k0)/(2*p0)

rng=np.random.default_rng(20261025)
for j in range(96):
 k0=float(np.exp(rng.uniform(-1.8,1.8)))
 g0=float(np.exp(rng.uniform(-3,2.5)))
 d0=float(rng.uniform(-15,15))
 error=abs(numerical_T(k0,g0,d0)-formula(k0,g0,d0))
 assert error<2e-9*(1+formula(k0,g0,d0)),(j,k0,g0,d0,error)
print('96 independent 9x9 complex-Liouvillian survival checks PASS')

kc=32**0.25
def th(k0):
 if k0<kc:
  return 3*(16-k0*k0+4*np.sqrt(12-2*k0*k0))/(k0*k0)
 return 12/(k0*k0-4)
def jump(k0):
 return (4-k0*k0+2*np.sqrt(12-2*k0*k0))/(2*k0)

for k0 in [0.3,0.5,1,1.5,1.9,2.,2.1,2.3,2.37,kc,2.4,3,5,10]:
 dt=th(k0)
 for mul in (.8,1.,1.2,2.0):
  dd=np.sqrt(dt*mul)
  # constrained minimizer bounded on large interval with logarithmic grid + local search
  f0=formula(k0,0,dd)
  upper=max(100,10*dd+10*k0)
  grid=np.geomspace(1e-8,upper,3000)
  idx=np.argmin([formula(k0,v,dd) for v in grid])
  if idx in (0,len(grid)-1):
   fg=min(f0,formula(k0,grid[idx],dd))
  else:
   res=minimize_scalar(lambda x:formula(k0,x,dd),bounds=(grid[idx-1],grid[idx+1]),method='bounded',options={'xatol':1e-13})
   fg=min(f0,float(res.fun))
  if mul<1: assert abs(fg-f0)<2e-6*(1+f0),(k0,mul,fg,f0)
  if mul>1: assert fg<f0-1e-6,(k0,mul,fg,f0)
  if mul==1 and k0<kc:
   assert abs(formula(k0,jump(k0),dd)-f0)<1e-8
print('56 global sharp-threshold and coexistence parameter checks PASS')
print('TOTAL all checks PASS')
