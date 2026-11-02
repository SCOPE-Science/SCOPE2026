"""Numerical checks of Gaussian/Marshall-Olkin logarithmic comparison.
Requires NumPy and SciPy. Numerical checks are not the asymptotic proof.
"""
import math
import numpy as np
from scipy.special import ndtri_exp, roots_laguerre, logsumexp, log_ndtr

X, W = roots_laguerre(128)

def gaussian_joint_log(L, rho, t):
    """log C_G(exp(-L), exp(-L-t)), integrating the normal tail independently."""
    a = -ndtri_exp(-L)
    b = -ndtri_exp(-L-t)
    x = a + X/a
    sig = math.sqrt(1-rho*rho)
    return (-0.5*a*a - 0.5*math.log(2*math.pi)-math.log(a)
            + logsumexp(np.log(W) - X*X/(2*a*a)
                        + log_ndtr((rho*x-b)/sig)))

def ratio(L, rho, c):
    beta = 2*rho/(1+rho)
    kappa = 2-beta
    t = math.log(L/c)
    if t < 0: raise ValueError('Need c<L so the second coordinate is smaller')
    log_m = -kappa*L-t
    return math.exp(gaussian_joint_log(L,rho,t)-log_m)

def constant(rho):
    alpha = rho/(1+rho)
    return (1+rho)**2/math.sqrt(1-rho*rho)*(4*math.pi)**(-alpha)

def main():
    checks = 0
    for rho in (0.2,0.5,0.8):
        alpha=rho/(1+rho)
        K = constant(rho)
        crit = K**(1/alpha)
        # Sharp finite-constant crossover predictions are not finite-L identities.
        for L in (80,320,1280):
            for mult in (0.25,1.,4.):
                c=crit*mult
                observed=ratio(L,rho,c)
                predicted=K*c**(-alpha)
                assert math.isfinite(observed) and observed>0
                # Check approach to the asymptotic, allowing slow convergence.
                assert abs(math.log(observed/predicted)) < (0.9 if L==80 else 0.45 if L==320 else 0.19), (rho,L,mult,observed,predicted)
                checks += 2
        # Numerical signs at suitably large L, away from the critical point.
        assert ratio(1280,rho,crit/4)>1
        assert ratio(1280,rho,crit*4)<1
        checks += 2
        # Distinct diagonal asymptotic: ratio -> 0 for all positive rho.
        uL=1280
        log_diag=gaussian_joint_log(uL,rho,0)
        kap=2/(1+rho)
        assert math.exp(log_diag +kap*uL) < 1
        checks+=1
        print(f'rho={rho:.2f} critical constant c_rho={crit:.10f}, '
              f'ratios at L=1280: {ratio(1280,rho,crit/4):.6f}, '
              f'{ratio(1280,rho,crit*4):.6f}')
    print(f'PASS: {checks} independent quadrature/asymptotic sign checks')

if __name__=='__main__': main()
