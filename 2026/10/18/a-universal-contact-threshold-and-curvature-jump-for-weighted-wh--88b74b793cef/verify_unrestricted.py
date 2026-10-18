#!/usr/bin/env python3
"""Optional unrestricted SPD maximization for small weighted wheel Lipschitz balls.

Requires NumPy and SciPy. Does not impose circulant or diagonal shape.
"""
import math
import numpy as np
from scipy.optimize import minimize
from verify import construct

def verify(m,t):
    q,a,b,_,_,z,_=construct(m,t)
    cycle=np.zeros((m,m))
    for k in range(m):
        cycle[k,k]+=2
        cycle[k,(k+1)%m]-=1
        cycle[(k+1)%m,k]-=1
    target=np.linalg.inv(a*np.eye(m)+b*cycle)
    ix=np.triu_indices(m)
    def matrix(y):
        A=np.zeros((m,m)); A[ix]=y; A[(ix[1],ix[0])]=y
        return A
    def obj(y):
        v,log=np.linalg.slogdet(matrix(y))
        return -log if v>0 else 1e5
    def cons(y):
        A=matrix(y)
        vals=[t*t-A[i,i] for i in range(m)]
        vals.extend(1-A[i,i]-A[(i+1)%m,(i+1)%m]+2*A[i,(i+1)%m] for i in range(m))
        vals.append(np.linalg.eigvalsh(A)[0]-1e-9)
        return np.asarray(vals)
    y0=(0.7*target)[ix]
    r=minimize(obj,y0,method='SLSQP',constraints=[{'type':'ineq','fun':cons}],options={'ftol':1e-9,'maxiter':2000})
    assert r.success, (m,t,r.message)
    assert abs(r.fun+z)<2e-6,(m,t,r.fun,-z)
    assert np.max(np.abs(matrix(r.x)-target))<1e-4,(m,t)
    return r.nit

if __name__=='__main__':
    c=0
    for m in [3,4,5,6]:
        for t in [0.6,0.8,1.0,1.4,2.0]:
            verify(m,t);c+=1
    print('UNRESTRICTED_OK',c,'full symmetric-matrix optimizations')
