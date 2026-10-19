"""Numerical and numerical-identity checks for the critical multistage epidemic theorem.
The arguments in RESULT.md, not these finite diagnostics, prove the theorem.
Run: python3 verify.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from numpy.linalg import solve,eigvals,norm

def one_case(M,P,beta,mu=1.0,force_silent=False):
    M=np.array(M,dtype=float);P=np.array(P,dtype=float);beta=np.array(beta,dtype=float)
    q=solve(M,P)
    r=beta@q
    assert r>0
    Sstar=1/r
    nu=mu*Sstar
    d=beta@solve(M,q)
    ell=solve(M.T,beta)
    A=Sstar*np.outer(P,beta)-M
    assert norm(A@q)<1e-11 and norm(ell@A)<1e-11
    ev=eigvals(A)
    assert abs(min(abs(ev)))<1e-9
    assert sum(abs(x)<1e-9 for x in ev)==1
    assert all(x.real<-1e-6 for x in ev if abs(x)>1e-9)
    target=Sstar*Sstar*mu*d*q
    if force_silent:
        x0=np.zeros(len(P));x0[-1]=.45
        assert abs(ell@x0)<1e-12
    else:
        x0=np.ones(len(P))*.2
        assert ell@x0>1e-12
    Sinit=Sstar*1.3
    def f(t,z):
        S=z[0]; x=z[1:]
        return np.r_[nu-mu*S-S*(beta@x), S*P*(beta@x)-M@x]
    sol=solve_ivp(f,[0,200000],np.r_[Sinit,x0],rtol=5e-11,atol=1e-13,method='BDF',dense_output=False)
    assert sol.success
    S=sol.y[0,-1]; x=sol.y[1:,-1]; T=sol.t[-1]
    if force_silent:
        assert norm(x)<1e-6
        assert abs(S-Sstar)<1e-8
        print('silent-face exponential agreement',norm(x),S-Sstar)
        return
    scale=T*x/target
    Sscale=T*(Sstar-S)/(Sstar*Sstar*d)
    lambdascale=T*(beta@x)/(mu*Sstar*d)
    print('n=',len(P),'q=',q,'d=',d,'scale=',scale,'Sscale=',Sscale,'lambdascale=',lambdascale)
    assert max(abs(scale-1))<0.02 and abs(Sscale-1)<0.02 and abs(lambdascale-1)<0.02
    # Exact Lyapunov derivative identity at arbitrary interior states.
    for f0 in [0.05,0.25,0.8,1.3]:
        Ss=f0*Sstar; xx=x0*1.4
        L=beta@xx
        sdot=nu-mu*Ss-Ss*L
        xdot=Ss*P*L-M@xx
        Udot=(1-Sstar/Ss)*sdot+Sstar*(ell@xdot)
        assert abs(Udot+mu*(Ss-Sstar)**2/Ss)<1e-10
one_case([[3]], [1], [1.5]);
one_case([[2,-1],[-1,3]], [1,0], [1,1]);
one_case([[2,0,0],[-1,3,0],[0,-1,2]], [1,0,0], [0,1,0]);
one_case([[2,0,0],[-1,3,0],[0,-1,2]], [1,0,0], [0,1,0],force_silent=True)
print('ALL CHECKS PASSED')
