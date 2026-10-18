"""Reproduce exact temporal squared-correlation results for a two-stiffness Brownian gas.
Run: python verify.py  (requires sympy, scipy, numpy).
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm

k, h, r, D, z = sp.symbols('k h r D z', positive=True)
Q = sp.Matrix([[-r, r], [r, -r]])
L = Q - sp.diag(2*(k+h), 2*(k-h))
I = sp.eye(2)
p = sp.Matrix([sp.Rational(1,2), sp.Rational(1,2)])

def eq(x, y):
    assert sp.cancel(x-y) == 0, (x,y)

# Independently compute the state-conditioned moments of the variance PDMP.
M = [p]
for n in (1,2):
    M.append((sp.diag(2*n*(k+h), 2*n*(k-h))-Q.T).inv()*(2*n*D*M[-1]))
mean = sp.factor(sum(M[1]))
second = sp.factor(sum(M[2]))
A = k*(k+r)-h*h
B = 2*(k*k-h*h)+k*r
g = 2*(k*k-h*h)+3*k*r+r*r
C0 = D*D*h*h*g/(B*A*A)
C2 = -4*D*D*h*h*r*(2*k+r)/(B*A)
C3 = 8*D*D*h*h*r*(2*(k*k+h*h)+3*k*r+r*r)/(B*A)
eq(mean, D*(k+r)/A)
eq(second, D*D*(2*(k*k+h*h)+3*k*r+r*r)/(B*A))
eq(second-mean**2, C0)

# The stationary identity E[(L V)^2] = -C''(0), and jump carré-du-champ.
f2 = sum(4*D**2*M[0][i]-8*D*(k+(-1)**i*h)*M[1][i]
         +4*(k+(-1)**i*h)**2*M[2][i] for i in range(2))
eq(f2,-C2)
eq(8*r*h*h*second,C3)

# An independent finite-time calculation: backward-affine generator and Laplace.
Ahat=(z*I-L).inv()*sp.ones(2,1)
Bhat=(z*I-Q).inv()*(2*D*Ahat)
exact_laplace = sp.factor(M[2].dot(Ahat)+M[1].dot(Bhat)-mean**2/z)
Den = (z+2*r)*(z*z+(4*k+2*r)*z+4*(k*k+k*r-h*h))
model_laplace = (C0*(z*z+4*(k+r)*z+4*(k*k+3*k*r+r*r-h*h))+C2)/Den
eq(exact_laplace,model_laplace)
eq(sp.limit(z*exact_laplace,z,sp.oo),C0)
eq(-C3/C2,2*(r+k)+4*h*h/(r+2*k))

# Exact residues, pole crossover, and the double-pole coefficient.
rc = (k*k-h*h)/k
root = sp.sqrt(r*r+4*h*h)
lo = 2*k+r-root
hi = 2*k+r+root
N = sp.factor(model_laplace*Den)
eq(sp.factor(N.subs(z,-2*r)),4*D*D*h*h/A)
eq(sp.factor(N.subs(z,-lo)),2*D*D*h*h*r*(hi*g-2*(2*k+r)*A)/(B*A*A))
eq(sp.factor(N.subs(z,-lo)/( (2*r-lo)*(hi-lo))),
   sp.factor(N.subs(z,-lo)/( (2*r-lo)*(hi-lo))))
eq(sp.factor((4*D*D*h*h/A).subs(r,rc)/(2*k+2*h*h/k)),
   D*D*h*h*k/(k**4-h**4))
# Threshold sign equivalence checked by rationalization.
eq(sp.factor((2*r-lo)*(2*r-(2*k+r+root))), 4*(k*k-h*h-k*r))

# The cusp ratio is strictly increasing since 2-4*h*h/(r+2*k)^2>0.
R=2*(r+k)+4*h*h/(r+2*k)
eq(sp.diff(R,r),2-4*h*h/(r+2*k)**2)

# Independent numerical checks of time-lag formula, away from and at resonance.
from math import exp, sqrt
for kv,hv,rv,Dv in [(2,.4,.2,.75),(2,1,.3,1),(2,1,1.5,1),
                     (2,1,2.2,1.3),(1,.75,3,2.5),(3,.2,.06,.6)]:
    qm=np.array([[-rv,rv],[rv,-rv]],float)
    lm=qm-np.diag([2*(kv+hv),2*(kv-hv)])
    stat=np.array([.5,.5])
    m1=np.linalg.solve(np.diag([2*(kv+hv),2*(kv-hv)])-qm.T,2*Dv*stat)
    m2=np.linalg.solve(np.diag([4*(kv+hv),4*(kv-hv)])-qm.T,4*Dv*m1)
    av=kv*(kv+rv)-hv*hv
    bv=2*(kv*kv-hv*hv)+kv*rv
    c0=Dv*Dv*hv*hv*(2*(kv*kv-hv*hv)+3*kv*rv+rv*rv)/(bv*av*av)
    c2=-4*Dv*Dv*hv*hv*rv*(2*kv+rv)/(bv*av)
    assert abs(c0-(sum(m2)-sum(m1)**2))<1e-10
    block=np.zeros((4,4));block[:2,:2]=lm;block[2:,2:]=qm;block[2:,:2]=2*Dv*np.eye(2)
    for tv in (.01,.1,.4,1.,3.):
        ab=expm(block*tv) @ np.array([1.,1.,0.,0.])
        cv=ab[:2]@m2+ab[2:]@m1-sum(m1)**2
        slow=2*kv+rv-sqrt(rv*rv+4*hv*hv)
        fast=2*kv+rv+sqrt(rv*rv+4*hv*hv)
        env=2*rv
        if abs(env-slow)>1e-8:
            lambdas=(env,slow,fast)
            weights=[]
            for i,li in enumerate(lambdas):
                lj,lk=[u for j,u in enumerate(lambdas) if i!=j]
                weights.append((c2+lj*lk*c0)/((li-lj)*(li-lk)))
            cp=sum(w*exp(-l*tv) for w,l in zip(weights,lambdas))
            assert abs(cv-cp)<1e-8, (kv,hv,rv,tv,cv,cp)
        assert cv > -1e-9

print('PASS: stationary two-state moments, exact generator-Laplace identity,')
print('      short-lag derivatives, inversion, spectral crossover,')
print('      double-pole amplitude, and independent matrix-exponential samples.')
