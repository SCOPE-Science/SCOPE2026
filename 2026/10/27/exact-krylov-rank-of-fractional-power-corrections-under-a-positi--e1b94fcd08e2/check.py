"""Reproducible finite consistency checks for fractional-power spike correction."""
from math import sqrt, exp
import numpy as np
import sympy as sp


def fractional(M, alpha):
    w, Q = np.linalg.eigh(M)
    assert min(w) > 0
    return (Q * w**alpha) @ Q.T


def rank_spectral_support(lam, u):
    return sum(bool(np.linalg.norm(u[np.isclose(lam, v)]) > 1e-12)
               for v in sorted(set(lam)))


def run():
    tests = 0
    z=sp.sqrt(13)
    D=sp.Matrix([[5/z-1,1/z],[1/z,8/z-2]])
    assert sp.simplify(sp.trace(D)-(z-3)) == 0; tests+=1
    assert sp.simplify(D.det()-(5-18/z)) == 0; tests+=1
    assert sp.simplify(25*13-18*18)==1; tests+=1
    cases=[
      ([1., 1., 4., 4., 9.],[1.,2.,0.,0.,3.]),
      ([1., 2., 3., 4.],[1.,1.,1.,1.]),
      ([3., 3., 3., 3.],[1.,-2.,3.,1.]),
      ([1., 2., 2., 4., 4.],[0.,1.,2.,0.,0.]),
      ([1., 2., 4.],[1.,0.,1.]),
    ]
    for lam_list,u_list in cases:
      lam=np.array(lam_list)
      u=np.array(u_list)
      n=len(lam)
      A=np.diag(lam)
      expected=rank_spectral_support(lam,u)
      for tau in (0.25, 1., 3.):
        B=A+tau*np.outer(u,u)
        for alpha in (0.25, 0.5, 0.75):
          pos=fractional(B,alpha)-fractional(A,alpha)
          neg=fractional(A,-alpha)-fractional(B,-alpha)
          for mat in (pos,neg):
            eig=np.linalg.eigvalsh(mat)
            # Projected support: eigenvalues can be below standard floating rank resolution
            tol=2e-8
            assert np.min(eig)>-tol, (lam_list,u_list,tau,alpha,eig)
            assert sum(eig>tol)==expected, (lam_list,u_list,tau,alpha,expected,eig)
            assert np.linalg.norm(mat-mat.T,ord=np.inf)<tol
            tests+=3
    # Check integral formula against spectral calculation for a nontrivial 3x3 case.
    import scipy.integrate as si
    A=np.diag([1.,2.,5.]);u=np.array([1.,2.,1.]);tau=1.3; B=A+tau*np.outer(u,u)
    for s in (.25,.5,.75):
      for power,weight in ((s, s),(-s,-s)):
        # Negative powers reverse the update difference; the target below handles the sign.
        v=[]
        for i in range(3):
          row=[]
          for j in range(3):
            def integ(z):
              t=exp(z)
              w=u/(np.diag(A)+t)
              return exp(weight*z)*tau*w[i]*w[j]/(1+tau*np.dot(u,w))*t
            val,_=si.quad(integ,-120,120,epsabs=2e-10,epsrel=1e-10,limit=300)
            row.append(np.sin(np.pi*s)/np.pi*val)
          v.append(row)
        target=(fractional(B,s)-fractional(A,s)) if power>0 else (fractional(A,-s)-fractional(B,-s))
        assert np.allclose(v,target,atol=5e-8,rtol=1e-7), (s,power,np.array(v),target)
        tests+=1
    print('PASS',tests,'finite checks; universal claim rests on analytic proof')

if __name__=='__main__':
    run()
