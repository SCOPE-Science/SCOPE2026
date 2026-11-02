#!/usr/bin/env python3
"""Independent finite-state verification of star exclusion evacuation identities.
Only standard NumPy/SciPy are needed. Run: python check_star.py.
"""
import math
import numpy as np
from scipy.linalg import solve
from scipy.special import loggamma
EULER_GAMMA=0.57721566490153286060651209

def sector_matrix(N,m,a,b,gamma):
    # Transient states E_k (vacant hub, k occupied leaves),
    # H_k (occupied hub, k-1 occupied leaves), for 1 <= k <= m.
    L=2*m
    Q=np.zeros((L,L))
    r=np.zeros(L)
    for k in range(1,m+1):
        E=2*(k-1); H=E+1
        u=k*a; v=(N-k+1)*b
        Q[E,E]=-u; Q[E,H]=u
        Q[H,H]=-(v+gamma); Q[H,E]=v
        if k==1:r[H]=gamma
        else:Q[H,2*(k-2)]=gamma
    return Q,r

def exact_product(N,m,a,b,gamma,s):
    z=1.0+0j
    for k in range(1,m+1):
        z *= k*a*gamma/(s*s+s*(gamma+k*a+(N-k+1)*b)+k*a*gamma)
    return z

def means(N,m,a,b,gamma):
    H=sum(1.0/k for k in range(1,m+1))
    H2=sum(1.0/(k*k) for k in range(1,m+1))
    C=gamma+(N+1)*b
    D=a-b
    mu=(C*H+D*m)/(a*gamma)
    var=(C*C*H2+2*C*D*H+D*D*m)/(a*a*gamma*gamma)-2*H/(a*gamma)
    return mu,var

def chf(N,a,b,gamma,t):
    # Characteristic function of gamma(T-ET)/sqrt(N), using exact product.
    mu,_=means(N,N,a,b,gamma)
    s=-1j*t*gamma/math.sqrt(N)
    k=np.arange(1,N+1,dtype=float)
    den=s*s+s*(gamma+k*a+(N-k+1)*b)+k*a*gamma
    lognum=np.log(k*a*gamma)
    return np.exp(np.sum(lognum-np.log(den))-1j*t*gamma*mu/math.sqrt(N))

def target(t,theta):
    return np.exp(-0.5*t*t+loggamma(1-1j*t*theta)-1j*t*theta*EULER_GAMMA)

def main():
    count=0; max_abs=0.; max_mean=0.; max_var=0.
    for N in range(1,10):
        for m in range(1,N+1):
            for a,b,gamma in ((.7,0.,1.3),(1.2,.3,2.1),(.4,1.6,.9),(2.3,3.4,.6)):
                Q,r=sector_matrix(N,m,a,b,gamma)
                mu,va=means(N,m,a,b,gamma)
                x=solve(-Q,np.ones(2*m),assume_a='gen')
                xx=solve(-Q,2*x,assume_a='gen')
                max_mean=max(max_mean,abs(x[-2]-mu))
                max_var=max(max_var,abs((xx[-2]-x[-2]**2)-va))
                for s in (.07,.3,1.,2.3):
                    f=solve(s*np.eye(2*m)-Q,r,assume_a='gen')
                    err=abs(f[-2]-exact_product(N,m,a,b,gamma,s))
                    max_abs=max(max_abs,err)
                    assert err < 1e-12, (N,m,a,b,gamma,s,err)
                    count+=1
                assert abs(x[-2]-mu)<1e-9, (N,m,a,b,gamma,mu,x[-2])
                assert abs((xx[-2]-x[-2]**2)-va)<1e-8,(N,m,a,b,gamma,va)
    print('EXACT FINITE CTMC: PASS',count,'independent Laplace comparisons; max absolute error',f'{max_abs:.3g}')
    print('MOMENTS: PASS',count//4,'cases; max mean error',f'{max_mean:.3g}','max variance error',f'{max_var:.3g}')
    for theta in (0.,.5,1.,2.):
        for N in (1000,5000,20000):
            b=theta/math.sqrt(N)
            errs=[abs(chf(N,1.,b,1.,t)-target(t,theta)) for t in (.3,.8,1.4)]
            print('CROSSOVER', f'theta={theta:g}',f'N={N}',f'max characteristic-function error={max(errs):.5g}')
        assert max(errs)<.06,(theta,errs)
    for b in (.1,1.,3.):
        N=20000; a=1.; gamma=1.; C=gamma+(N+1)*b; scale=C/(a*gamma)
        mu,_=means(N,N,a,b,gamma)
        s=-1j*0.7/scale
        k=np.arange(1,N+1,dtype=float)
        phi=np.exp(np.sum(np.log(k*a*gamma)-np.log(s*s+s*(gamma+k*a+(N-k+1)*b)+k*a*gamma))-1j*0.7*mu/scale)
        aim=np.exp(loggamma(1-.7j)-.7j*EULER_GAMMA)
        print('GUMBEL',f'b={b:g}',f'N={N}',f'error={abs(phi-aim):.5g}')
        assert abs(phi-aim)<.02
    print('ALL CHECKS PASS')

if __name__=='__main__':main()
