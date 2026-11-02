"""Independent numerical and algebraic checks for two-state switching-diffusivity exit laws.
Requires numpy and scipy. No external data.
"""
import numpy as np
from scipy.linalg import expm
from scipy.sparse import diags, bmat, eye, csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.special import logsumexp


def telegraph_factor(t, gamma, amp):
    # amp=positive diffusion contrast times Dirichlet eigenvalue
    z = np.hypot(gamma, amp)
    return np.exp(-gamma*t) * (np.cosh(z*t) + gamma*np.sinh(z*t)/z)

def exact_time(x, length, dm, dp, gamma):
    m=(dm+dp)/2; h=(dp-dm)/2
    z=np.sqrt(2*gamma*m/(dm*dp))
    # stable expression for 1-cosh(z*(x-L/2))/cosh(z*L/2)
    f=1-np.cosh(z*(x-length/2))/np.cosh(z*length/2)
    return x*(length-x)/(2*m)+h*h/(2*gamma*m*m)*f

def solve_time_fd(length, dm, dp, gamma, n):
    dx=length/(n+1)
    lap=diags([np.ones(n-1),-2*np.ones(n),np.ones(n-1)],[-1,0,1],format='csc')/dx**2
    ident=eye(n,format='csc')
    gen=bmat([[dm*lap-gamma*ident,gamma*ident],[gamma*ident,dp*lap-gamma*ident]],format='csc')
    times=spsolve(-gen,np.ones(2*n))
    return np.arange(1,n+1)*dx,(times[:n]+times[n:])/2

def check():
    n_exp=0; worst_exp=0.0
    for dm,dp in [(1.,3.),(.31,2.7),(4.,8.)]:
      for gamma in [.07,.4,1.6,6.]:
       for lam in [.2,.9,2.4,5.]:
        for t in [.05,.23,1.1]:
         mat=np.array([[-gamma-lam*dm,gamma],[gamma,-gamma-lam*dp]])
         direct=np.array([.5,.5])@expm(t*mat)@np.ones(2)
         m=(dm+dp)/2; h=(dp-dm)/2
         closed=np.exp(-lam*m*t)*telegraph_factor(t,gamma,lam*h)
         err=abs(direct-closed)
         worst_exp=max(worst_exp,err);n_exp+=1
         assert err < 1e-11,(dm,dp,gamma,lam,t,err)
    worst_fd=0.0;n_fd=0
    for dm,dp,gamma,L in [(1.,3.,.1,1.),(.4,2.1,4.,1.7),(2.,9.,.8,2.1)]:
      for n in [150,250]:
       x,model=solve_time_fd(L,dm,dp,gamma,n)
       exact=exact_time(x,L,dm,dp,gamma)
       err=np.max(np.abs(model-exact))
       worst_fd=max(worst_fd,err);n_fd+=1
       assert err<7e-5,(dm,dp,gamma,L,n,err)
    strict=0
    for dm,dp in [(1.,3.),(.5,5.)]:
      m=(dm+dp)/2;h=(dp-dm)/2
      for t in [.02,.1,.4,1.3]:
       for lam in [.4,1.,6.]:
        vals=[np.exp(-lam*m*t)*telegraph_factor(t,g,lam*h) for g in [0.,.07,.6,5.,80.]]
        assert all(a>b for a,b in zip(vals,vals[1:])),(dm,dp,lam,t,vals)
        assert vals[-1]>np.exp(-lam*m*t)
        strict+=1
    print(f'PASS: {n_exp} independent matrix exponential comparisons; max absolute error {worst_exp:.3g}')
    print(f'PASS: {n_fd} independent coupled finite-difference problems; max absolute error {worst_fd:.3g}')
    print(f'PASS: {strict} strict ordered mode families, each at five rates')

if __name__=='__main__':
    check()
