"""Reproducible checks of limiting coefficients for a saturating switching population.
Uses independent state variables q=(1-U)^(1-p), normalized composition z.
These are finite numerical checks, not proofs of asymptotic limits.
"""
import numpy as np
from scipy.integrate import solve_ivp
from numpy.linalg import solve, norm

def example(Q, r, p, tmax=4000.):
    n=len(r); Q=np.asarray(Q,float); r=np.asarray(r,float)
    assert n>=2 and np.allclose(np.ones(n)@Q,0)
    A=Q.copy(); A[-1,:]=1
    b=np.zeros(n); b[-1]=1
    psi=solve(A,b)
    assert np.min(psi)>0
    rbar=r@psi
    h=psi*(r-rbar)
    B=Q.copy();B[-1,:]=1
    rhs=-h.copy();rhs[-1]=0
    L=solve(B,rhs)
    assert np.allclose(Q@L+h,0,rtol=0,atol=1e-10)
    assert abs(np.sum(L))<1e-10
    z0=0.3; y0=psi.copy(); y0[0]+=0.05;y0[1]-=0.05
    def f(t, v):
        q=v[0]; y=v[1:]; zz=q**(-1/(p-1)); rr=y@r
        return np.r_[(p-1)*(1-zz)*rr, Q@y+zz**p*(r*y-rr*y)]
    x0=np.r_[(z0**(1-p)),y0]
    sol=solve_ivp(f,(0,tmax),x0,method='DOP853',rtol=5e-13,atol=1e-14,
                  t_eval=[tmax/4,tmax/2,tmax],max_step=1.5)
    assert sol.success
    for t,x in zip(sol.t,sol.y.T):
        q=x[0]; z=q**(-1/(p-1)); yy=x[1:]
        Lest=(yy-psi)/z**p
        print('p',p,'t',t,'mean r inferred',q/((p-1)*t),'target',rbar,
              'Lest',np.round(Lest,8),'L target',np.round(L,8),
              'error',norm(Lest-L))
    return psi,L

if __name__=='__main__':
    psi,L=example([[-1,1],[1,-1]],[3,1],2.)
    assert np.allclose(psi,[0.5,0.5]) and np.allclose(L,[0.25,-0.25])
    psi,L=example([[-1,1],[1,-1]],[3,1],3.,2000.)
    Q=np.array([[-2,1,2],[1,-2,1],[1,1,-3]],float)
    psi,L=example(Q,[4,2,1],2.,2200.)
    print('PASS: three asymptotic numerical consistency checks and all exact linear residual identities')
