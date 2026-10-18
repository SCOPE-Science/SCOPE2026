"""Independent algebraic and finite-time Markov generator checks for periodic telegraph-driver transport spectroscopy."""
import numpy as np
from scipy.linalg import expm
import sympy as s

D, q, v, a = s.symbols('D q v a', positive=True, real=True)
I=s.I
L = s.Matrix([[-D*q*q-a+I*v*q,a],[a,-D*q*q-a-I*v*q]])
e=s.Matrix([1,1])
res=s.simplify((e.T*(-L).inv()*e)[0]/2)
expected=(D*q*q+2*a)/(q*q*(D*D*q*q+2*D*a+v*v))
assert s.simplify(res-expected)==0,(res,expected)
assert s.simplify(s.diff(expected,a)-2*v*v/(q*q*(v*v+D*D*q*q+2*D*a)**2))==0
assert s.simplify((1/(D*q*q)-expected)-v*v/(D*q*q*(v*v+D*D*q*q+2*D*a)))==0

rng=np.random.default_rng(44223)
count=0
for _ in range(16):
    dv=float(rng.uniform(.08,2.0)); vv=float(rng.uniform(.1,5)); aa=float(rng.uniform(.04,2)); qq=float(rng.uniform(.3,6))
    Z=np.array([[-dv*qq*qq-aa+1j*vv*qq,aa],[aa,-dv*qq*qq-aa-1j*vv*qq]],complex)
    value=0.5*np.array([1,1])@np.linalg.solve(-Z,np.array([1,1])); assert abs(value.real-float(expected.subs({D:dv,v:vv,a:aa,q:qq})))<1e-11
    ts=np.linspace(0,80/(dv*qq*qq),6001)
    # Analytic generator diagonalization independent of closed-form rational resolvent.
    vals,P=np.linalg.eig(Z); coefs=np.linalg.solve(P,np.array([1,1])); c=.5*np.array([1,1])@P
    vals_at=(c[:,None]*coefs[:,None]*np.exp(vals[:,None]*ts[None,:])).sum(axis=0).real
    approx=np.trapezoid(vals_at,ts)
    assert abs(approx-value.real)/(1+value.real)<0.005, (approx,value)
    count+=1

# Finite-rate recovery with unrelated positive amplitude weights, including an unknown Brownian base diffusion.
for n in range(1,5):
    dv=float(rng.uniform(.1,2)); vv=float(rng.uniform(.1,5)); period=float(rng.uniform(3,10)); base=float(rng.uniform(0,2))
    qs=2*np.pi*np.arange(1,n+1)/period
    powers=rng.uniform(.05,2,size=n)
    rates=np.sort(rng.uniform(.02,5,size=n+1))
    B=vv*vv+dv*dv*qs**2
    def E(aa): return base+np.sum(powers*(dv*qs**2+2*aa)/(qs**2*(B+2*dv*aa)))
    obs=np.array([E(x) for x in rates])
    rhs=(obs[1:]-obs[0])/(2*vv*vv*(rates[1:]-rates[0]))
    mat=1/(B[None,:]+2*dv*rates[1:,None])
    z=np.linalg.solve(mat,rhs)
    recovered=z*qs**2*(B+2*dv*rates[0]); rel=np.max(np.abs(recovered-powers)/(1+powers)); assert rel<1e-5,(n,rel)
    count+=1
print('PASS: generator resolvent, derivative, high-rate deficit identities; 16 time-kernel quadratures; four finite-rate Cauchy reconstructions; total',count)

# Exact rational Cauchy reconstruction at six harmonics (ill-conditioned in floating point, algebraically invertible).
N=6; Ds=s.Rational(3,2); vs=s.Rational(5,4); Ll=2*s.pi; qs=[s.Integer(i) for i in range(1,N+1)]
ps=[s.Rational(1+i,9+i) for i in range(1,N+1)]; aa=[s.Rational(1+i,4) for i in range(N+1)]
B=[vs*vs+Ds*Ds*q*q for q in qs]
def Eff(r):
 return s.Rational(7,3)+sum(ps[j]*(Ds*qs[j]**2+2*r)/(qs[j]**2*(B[j]+2*Ds*r)) for j in range(N))
o=[Eff(x) for x in aa]
rhs=s.Matrix([(o[i]-o[0])/(2*vs*vs*(aa[i]-aa[0])) for i in range(1,N+1)])
M=s.Matrix([[1/(B[j]+2*Ds*aa[i]) for j in range(N)] for i in range(1,N+1)])
assert M.det()!=0
z=M.inv()*rhs
assert all(s.simplify(z[j]*qs[j]**2*(B[j]+2*Ds*aa[0])-ps[j])==0 for j in range(N))
print('PASS: exact rational 6-mode inverse Cauchy system and nonzero determinant')
