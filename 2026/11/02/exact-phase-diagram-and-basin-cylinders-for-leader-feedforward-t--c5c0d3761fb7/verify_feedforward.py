"""Numerical consistency checks for the feedforward logistic threshold theorem."""
import math, random, itertools
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
rng=random.Random(20261026)
profiles=0; equilibria=0; basin_trials=0; max_error=0.

def L(z):
    if z>=0: return 1/(1+math.exp(-z))
    a=math.exp(z); return a/(1+a)

def roots(beta):
    f=lambda x: L(beta*(x-.5))-x
    q=brentq(f,1e-12,.499999999999,xtol=1e-14)
    return (q,.5,1-q)

for beta in (4.5,5.0,8.0):
    R=roots(beta)
    for s in (1,2,3):
      for f in (0,1,3):
       n=s+f
       for replicate in range(6):
        W=np.zeros((n,n))
        for i in range(s): W[i,i]=1.
        for i in range(s,n):
            a=np.array([rng.random()+.01 for j in range(i)])
            W[i,:i]=a/a.sum()
        for code in itertools.product(range(3),repeat=s):
            x=np.zeros(n)
            for i,k in enumerate(code): x[i]=R[k]
            for i in range(s,n): x[i]=L(beta*(W[i]@x-.5))
            residual=np.max(np.abs(np.array([L(beta*(W[i]@x-.5)) for i in range(n)])-x))
            max_error=max(max_error,residual)
            assert residual<1e-12
            J=np.array([-1.+beta*x[i]*(1-x[i]) if i<s else -1. for i in range(n)])
            assert sum(v>0 for v in J)==code.count(1)
            equilibria+=1
        for t in range(3):
            init=np.array([rng.random() for i in range(n)])
            # explicit recursive limiting equilibrium from its root sign
            dest=np.zeros(n)
            for i in range(s): dest[i]=R[0] if init[i]<.5 else R[2]
            for i in range(s,n): dest[i]=L(beta*(W[i]@dest-.5))
            rhs=lambda tm,x: -x+1/(1+np.exp(-beta*(W@x-.5)))
            T=60 if beta>5 else 160
            sol=solve_ivp(rhs,(0,T),init,rtol=2e-9,atol=2e-11)
            err=float(np.max(np.abs(sol.y[:,-1]-dest)))
            if err>1e-4:
                print('warning slow',beta,s,f,err)
            assert err<1e-3
            basin_trials+=1
        profiles+=1
print('VERIFY_OK', 'profiles',profiles,'equilibria',equilibria,'basin_trials',basin_trials,'max_error',max_error)
