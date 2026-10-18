"""Independent finite-dimensional numerical checks for cycle-chord 2-summing screening.
Requirements: Python 3, numpy, scipy. Does not replace the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize


def radius(n, k):
    return sum(math.cos((2*j+1)*math.pi/(2*n))/math.sin((2*j+1)*math.pi/(2*n)) for j in range(k))


def threshold(n, k):
    return math.sqrt((1/math.tan(math.pi/(2*n)))/radius(n, k))


def traceopt(n, extras, numerical=True):
    U=null_space(np.ones((1,n)))
    E=[]
    for i in range(n):
        b=np.zeros(n);b[i]=1;b[(i+1)%n]=-1
        E.append(b)
    for u,v,scale in extras:
        b=np.zeros(n);b[u]=scale;b[v]=-scale;E.append(b)
    T=np.array(E)@U
    # F and gradient on the connected region
    def fg(w):
        L=(T.T*w)@T
        vals,Q=np.linalg.eigh(L)
        if min(vals)<1e-11:
            raise ArithmeticError('singular trial Laplacian')
        f=np.sqrt(vals).sum()
        inv=(Q/np.sqrt(vals))@Q.T
        grads=0.5*np.einsum('ij,jk,ik->i',T,inv,T)
        return f,grads
    uniform=np.r_[np.repeat(1/n,n),np.zeros(len(extras))]
    F0,g0=fg(uniform)
    if not numerical: return F0,g0
    start=np.r_[np.repeat(0.9/n,n),np.repeat(0.1/max(len(extras),1),len(extras))] if extras else uniform
    def obj(w):
        f,g=fg(w)
        return -f
    def jac(w):
        f,g=fg(w)
        return -g
    res=minimize(obj,start,jac=jac,bounds=[(1e-7,1) for _ in range(n)]+[(0,1) for _ in extras],
                 constraints=[{'type':'eq','fun':lambda w:w.sum()-1,'jac':lambda w:np.ones(len(w))}],
                 method='SLSQP',options={'maxiter':600,'ftol':1e-12})
    return F0,g0,-res.fun,res.success, res.x[-len(extras):] if extras else []


def run():
    checks=0
    for n in (5,6,7,8,10,14,21):
      for k in sorted(set((2,n//2))):
        c=threshold(n,k)
        F0,g0=traceopt(n,[(0,k,1)],False)
        assert abs(F0-2/math.sqrt(n)/math.tan(math.pi/(2*n)))<1e-10
        assert abs(g0[n]/g0[0]-1/c**2)<1e-10
        for factor in (0.82,0.99,1,1.02,1.1):
          scale=c*factor
          F0,gr,found,success,weights=traceopt(n,[(0,k,scale)])
          assert success,(n,k,scale)
          if factor<=1:
            assert found-F0<5e-8,(n,k,factor,found-F0)
          else:
            assert found-F0>1e-7,(n,k,factor,found-F0)
          checks+=1
    # Two-chord simultaneous test: when both derivatives are below cycle value,
    # the whole feasible spectral simplex has unchanged optimum.
    for n in (7,9,11,13):
      k1=2;k2=n//2
      tests=(
        (0.95*threshold(n,k1),0.95*threshold(n,k2),False),
        (1.08*threshold(n,k1),0.95*threshold(n,k2),True),
        (0.95*threshold(n,k1),1.08*threshold(n,k2),True),
      )
      for a,b,strict in tests:
        F0,_,found,success,_=traceopt(n,[(0,k1,a),(1,(1+k2)%n,b)])
        assert success
        assert ((found-F0>1e-7) if strict else (found-F0<5e-8)),(n,a,b,found-F0)
        checks+=1
    print('FINITE_NUMERICAL_CHECKS_PASSED',checks)

if __name__=='__main__':run()
