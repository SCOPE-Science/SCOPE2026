"""Supplementary numerical checks for the inverse-boundary radial chirp theorem.

Run: python3 verify_chirp.py (requires NumPy and SciPy).
Finite numerical checks corroborate, but do not prove, the asymptotic theorem.
"""
import numpy as np
from scipy.integrate import quad, quad_vec
from scipy.special import beta, gamma, gammaln, kv


def direct_eigenvalue(n, alpha, c):
    """Independent oscillatory quadrature after the substitution v=(1-t)^(-1)."""
    def f(v):
        return (1.0-1.0/v)**n*v**(-alpha-2.0)
    re=quad(f,1.0,np.inf,weight='cos',wvar=c,epsabs=2e-11,limit=300)[0]
    im=quad(f,1.0,np.inf,weight='sin',wvar=c,epsabs=2e-11,limit=300)[0]
    return (re+1j*im)/beta(n+1.0,alpha+1.0)


def bessel_gamma_eigenvalue(n, alpha, c):
    """Numerical gamma average of the exact Macdonald-function representation."""
    a=-1j*c
    v=n+alpha+2.0
    def f(s):
        pdf=np.exp((v-1.0)*np.log(s)-s-gammaln(v))
        return pdf*2.0*(a/s)**((alpha+1.0)/2.0)*kv(alpha+1.0,2.0*np.sqrt(a*s))
    lo=max(1.e-4,v-13.*np.sqrt(v))
    hi=v+13.*np.sqrt(v)
    integral,_=quad_vec(f,lo,hi,epsabs=2e-14,epsrel=2e-10)
    return np.exp(1j*c+gammaln(v)-gammaln(n+1.)-gammaln(alpha+1.))*integral


def asymptotic(n,alpha,c):
    a=-1j*c
    return (np.sqrt(np.pi)/gamma(alpha+1.0))*a**((2.*alpha+1.)/4.)*n**((2.*alpha+1.)/4.)*np.exp(1j*c/2.0-2.0*np.sqrt(a*n))


def main():
    short=0
    for alpha,c in [(0.,1.),(-.5,1.),(1.5,-2.)]:
        for n in (6,10,16):
            z=direct_eigenvalue(n,alpha,c)
            w=bessel_gamma_eigenvalue(n,alpha,c)
            assert abs(z-w)<2.e-8+1.e-8*abs(z),(n,alpha,c,z,w)
            short+=1
    large=0
    for alpha,c in [(0.,1.),(-.5,1.),(1.5,2.),(0.,-1.)]:
        ratios=[]
        for n in (100,300,1000):
            z=bessel_gamma_eigenvalue(n,alpha,c)
            ratios.append(abs(z/asymptotic(n,alpha,c)-1))
            large+=1
        assert ratios[-1]<0.10,(alpha,c,ratios)
        assert ratios[-1]<ratios[0],(alpha,c,ratios)
    print(f'VERIFY_OK independent_oscillatory_vs_bessel={short} asymptotic_comparisons={large}')


if __name__=='__main__':
    main()
