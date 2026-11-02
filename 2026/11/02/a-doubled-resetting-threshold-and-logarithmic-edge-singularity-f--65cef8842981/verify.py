#!/usr/bin/env python3
"""Standalone computations supporting explicit Ising-pair renewal formulas.

Run: python verify.py (requires NumPy, SciPy).
This checks finite examples only; universal statements are established analytically.
"""
import math
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import solve

checks=0

def close(a,b,rel=1e-8,abs_=1e-10):
    global checks
    assert math.isclose(float(a),float(b),rel_tol=rel,abs_tol=abs_), (a,b)
    checks+=1

def params(g,r):
    a=2*(1-g)
    q=g/(1+math.sqrt(1-g*g))
    b=r/(r+a)
    xi=2*g/((r+2)+math.sqrt((r+2)**2-4*g*g))
    return a,q,b,xi

def S(n,t,g):
    # e^{-2t}(I_0(2*g*t)+2 sum_{j=1}^{n-1} I_j + I_n)
    z=2*g*t
    a=2*(1-g)
    return math.exp(-a*t)*(ive(0,z)+ive(n,z)+2*sum(ive(j,z) for j in range(1,n)))

def C(n,t,g):
    a,q,_,_=params(g,1.0)
    return q**n+a*quad(lambda u: S(n,u,g),t,np.inf,epsabs=1e-12,epsrel=1e-11,limit=200)[0]

def S_kernel(n,t,g,M=100):
    z=2*g*t
    a=2*(1-g)
    return math.exp(-a*t)*sum(ive(abs(n-m),z)-ive(n+m,z) for m in range(1,M+1))

for g in [0.15,0.4,0.77]:
 for n in [1,2,3,5]:
  a,q,b,xi=params(g,0.7)
  close(C(n,0,g),1,rel=2e-10)
  for t in [0.03,0.2,1,3,8]:
   close(S(n,t,g),S_kernel(n,t,g,M=65),rel=2e-9,abs_=2e-12)
   v=C(n,t,g)
   assert q**n < v < 1 and C(n,t+0.3,g)<v
   checks+=1
  # independent numerical resetting convolution against stationary difference equation
  for r in [0.15,0.9,2.1]:
   b=r/(r+a)
   xi=2*g/(r+2+math.sqrt((r+2)**2-4*g*g))
   cc=1-a*quad(lambda t:math.exp(-r*t)*S(n,t,g),0,np.inf,epsabs=2e-12,epsrel=2e-11)[0]
   close(cc,b+(1-b)*xi**n,rel=2e-8,abs_=3e-9)
  # large time Bessel coefficient controlled via asymptotic expansion
  for t in [500,900]:
   z=2*g*t
   ratio=(ive(0,z)+ive(n,z)+2*sum(ive(j,z) for j in range(1,n)))*math.sqrt(math.pi*g*t)/n
   assert .97 < ratio < 1.03, (g,n,t,ratio)
   checks+=1

# Explicit finite-volume Glauber generator and reset law, independent of
# the correlation hierarchy and infinite-volume Bessel representation.
for N in [6,8]:
 for gamma,r in [(0.25,0.35),(.7,1.3),(.9,.3)]:
  states=1<<N
  G=lil_matrix((states,states),dtype=float)
  for mask in range(states):
   spins=np.array([1 if mask&(1<<k) else -1 for k in range(N)])
   rate_total=0.0
   for i in range(N):
    rate=.5*(1-(gamma/2)*spins[i]*(spins[(i-1)%N]+spins[(i+1)%N]))
    G[mask^(1<<i),mask]+=rate
    rate_total+=rate
   if mask!=states-1:
    G[states-1,mask]+=r
    rate_total+=r
   G[mask,mask]-=rate_total
  mat=G.tocsc().tolil()
  mat[0,:]=np.ones(states)
  rhs=np.zeros(states);rhs[0]=1
  rho=spsolve(mat.tocsc(),rhs)
  close(sum(rho),1,abs_=1e-10)
  assert min(rho)>-1e-12
  a,q,b,xi=params(gamma,r)
  for n in range(1,N//2+1):
   direct=0.
   for mask in range(states):
    spins=np.array([1 if mask&(1<<k) else -1 for k in range(N)])
    direct+=rho[mask]*sum(spins[i]*spins[(i+n)%N] for i in range(N))/N
   finite=b+(1-b)*(xi**n+xi**(N-n))/(1+xi**N)
   close(direct,finite,rel=2e-10,abs_=2e-10)

# Infinite-temperature exactly solvable boundary gamma=0:
for r in [.2,1,2,3.5]:
 for c in [.01,.3,.9]:
  close((r/2)*c**(r/2-1), r/2*math.exp((r/2-1)*math.log(c)))

print('PASS:',checks,'checks')
