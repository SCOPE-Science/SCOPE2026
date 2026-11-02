"""Symbolic and numerical checks for a shared-switch Brownian work covariance law.

Execute: python checker.py. Requires sympy and numpy.
The finite simulations are diagnostics, not the proof of the asymptotic theorem.
"""
import sympy as sp
import numpy as np

q,k,D,x = sp.symbols('q k D x',positive=True)
h0=k*x*x/2
h1=-k*D/(2*q)
mu=k*D/2
g0=q*k*x*x/2
g1=-q*k*x*x/2
L0 = sp.expand(D*sp.diff(h0,x,2)+q*(h1-h0))
L1 = sp.expand(D*sp.diff(h1,x,2)-k*x*sp.diff(h1,x)+q*(h0-h1))
assert sp.simplify(L0-(mu-g0))==0
assert sp.simplify(L1-(mu-g1))==0
assert sp.simplify(k*x*x/2+h1-h0+k*D/(2*q))==0
assert sp.simplify(-k*x*x/2+h0-h1-k*D/(2*q))==0

mon,moff=sp.symbols('mon moff')
sol=sp.solve([2*D-2*k*mon, D-2*k*mon+q*(moff-mon)], [mon,moff], dict=True)[0]
assert sp.simplify(sol[mon]-D/k)==0
assert sp.simplify(sol[moff]-D/k-D/q)==0
sigma_diag=sp.simplify(2*D*k*k*sol[moff]+k*k*D*D/(4*q))
assert sp.simplify(sigma_diag-2*k*D*D-sp.Rational(9,4)*k*k*D*D/q)==0

# Heterogeneous finite systems: independent continuous drivers, shared jump driver.
params=[(sp.Rational(7,10),sp.Rational(13,10)),(sp.Rational(9,5),sp.Rational(2,5)),(sp.Rational(6,5),sp.Rational(9,10))]
qr=sp.Rational(3,2)
cs=[ki*di/(2*qr) for ki,di in params]
A=sp.diag(*[2*ki*di*di*(1+ki/qr) for ki,di in params])
M=A+qr*sp.Matrix(cs)*sp.Matrix([cs])
assert all(sp.factor(M[i,j]-(params[i][0]*params[i][1]*params[j][0]*params[j][1])/(4*qr))==0
           for i in range(3) for j in range(3) if i!=j)
assert all(sp.factor(M[i,i]-(2*params[i][0]*params[i][1]**2+
                  sp.Rational(9,4)*params[i][0]**2*params[i][1]**2/qr))==0
           for i in range(3))
assert all(sp.factor(M[i,j]*qr/(params[i][0]*params[i][1]*params[j][0]*params[j][1])-sp.Rational(1,4))==0
           for i in range(3) for j in range(3) if i!=j)
assert A.is_positive_definite

# For identical particles, sum of each covariance-matrix entry.
N=sp.symbols('N',integer=True,positive=True)
assert sp.simplify(N*(2*k*D*D*(1+k/q))+N*N*k*k*D*D/(4*q) -
                   (2*N*k*D*D+k*k*D*D*N*(N+8)/(4*q)))==0

# Independent finite-time trajectory diagnostic using exact OU/free Gaussian transitions.
# All particles see identical Poisson switching times, but independent thermal noises.
rng=np.random.default_rng(20261031)
R=18000
T=350.0
qa=1.5
kv=np.array([.7,1.8,1.2]);dv=np.array([1.3,.4,.9]);nn=3
xt=np.zeros((R,nn)); tt=np.zeros(R); s=np.zeros(R,dtype=np.int8)
W=np.zeros((R,nn))
# Start out of stationarity; effect of initial transient is O(1) on variance/T.
for step in range(2200):
    active=tt<T
    if not active.any():
        break
    raw=rng.exponential(1/qa,size=R)
    dt=np.minimum(raw,np.maximum(0,T-tt))
    decay=np.exp(-dt[:,None]*kv[None,:])
    z=rng.standard_normal((R,nn))
    xt=np.where(s[:,None]==1,
                decay*xt+np.sqrt(dv[None,:]/kv[None,:]*(-np.expm1(-2*dt[:,None]*kv[None,:])))*z,
                xt+np.sqrt(2*dv[None,:]*dt[:,None])*z)
    event=active & (raw<=T-tt)
    W[event] += .5*kv[None,:]*xt[event]**2*(1-2*s[event])[:,None]
    s[event]=1-s[event]
    tt+=dt
assert not np.any(tt<T-1e-6)
emp=np.cov(W,rowvar=False,ddof=1)/T
pred=np.diag(2*kv*dv**2*(1+kv/qa))+np.outer(kv*dv,kv*dv)/(4*qa)
rel=np.max(np.abs(emp-pred)/pred)
print('symbolic generator, moment and covariance checks: PASS')
print('finite-trajectory covariance-rate diagnostic: max relative error',round(rel,4))
print('predicted covariance rate:',np.array2string(pred,precision=5))
print('empirical covariance rate:',np.array2string(emp,precision=5))
assert rel<.21, 'finite simulation is too noisy or code/model mismatch'
print('ALL CHECKS PASS')
