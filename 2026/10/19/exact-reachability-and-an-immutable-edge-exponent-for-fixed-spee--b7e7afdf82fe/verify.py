"""Independent finite-moment and edge-normalization checks for RTP control.

This script checks finite-dimensional consequences of the exact PDE and
geometric arguments. The accompanying proof supplies the infinite-dimensional
statements; numerical integration is not used to certify them.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.special import gamma


def smooth(u):
    return u**3*(10-15*u+6*u*u)


def smooth_prime(u):
    return 30*u*u*(u-1)**2


def run(ri, rf, beta, v, T):
    assert (rf-ri) < v*T
    def R(t): return ri+(rf-ri)*smooth(t/T)
    def Rp(t): return (rf-ri)/T*smooth_prime(t/T)
    def rates(t):
        radius=R(t)
        kappa=(v-Rp(t))/radius
        alpha=2*(beta+1)*v/radius
        return kappa,alpha
    def exact_moments(t):
        rr=R(t)
        d=2*beta+3
        return np.array([rr*rr/d,rr/d,3*rr**4/(d*(d+2)),3*rr**3/(d*(d+2))])
    def rhs(t,y):
        k,a=rates(t)
        m2,m1s,m4,m3s=y
        return [-2*k*m2+2*v*m1s, -(k+a)*m1s+v,
                -4*k*m4+4*v*m3s,-(3*k+a)*m3s+3*v*m2]
    t=np.linspace(0,T,301)
    z=solve_ivp(rhs,(0,T),exact_moments(0),t_eval=t,atol=1e-12,rtol=1e-11)
    assert z.success
    err=max(np.max(np.abs(z.y[:,j]-exact_moments(t[j]))) for j in range(len(t)))
    rmin=min(rates(float(tt))[0] for tt in t)
    assert rmin>0 and err<1e-8, (err,rmin)
    return float(err),float(rmin)


def edge(beta,kappa,small):
    z=math.sqrt(math.pi)*gamma(beta+1)/gamma(beta+1.5)
    r=1/kappa
    density=lambda x: 0.5*(1+kappa*x)*kappa/z * max(0.,1-(kappa*x)**2)**beta
    integral=quad(density,r-small,r,epsabs=1e-11,epsrel=1e-10,points=[r])[0]
    coefficient=(2**beta)*kappa**(beta+1)/((beta+1)*z)
    return integral/(coefficient*small**(beta+1))


def main():
    experiments=[(0.8,1.4,0.4,1.,2.), (1.4,0.8,-0.7,1.,0.6),
                 (1.0,0.5,2.1,0.8,0.3), (0.5,1.0,0.,1.2,1.0),
                 (0.6,1.2,3.0,1.0,1.3)]
    for j,args in enumerate(experiments):
        err,kmin=run(*args)
        print('moment_test',j,'max_error',format(err,'.3e'),'min_stiffness',format(kmin,'.4f'))
    for beta in (-0.5,0.,0.75,2.):
        x=edge(beta,1.3,1e-4)
        assert abs(x-1)<.005, (beta,x)
        print('edge_test',beta,'coefficient_ratio_at_1e-4',format(x,'.8f'))
    print('ALL FINITE TESTS PASSED')

if __name__=='__main__':main()
