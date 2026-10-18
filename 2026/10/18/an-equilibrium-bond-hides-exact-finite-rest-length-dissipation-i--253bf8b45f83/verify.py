"""Reproducible independent checks of the reversible-bond resolvent identity.

The physical assumptions, proof and limitations are provided in RESULT.md.
"""
from math import pi
import numpy as np
from scipy.integrate import trapezoid
from scipy.linalg import solve_continuous_lyapunov
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


def radial_resolvent(a=1., b=2., D=1., ell=1., N=2500, R=12.):
    """First angular harmonic of (a-L_q)^{-1}F, on a truncated radial grid."""
    h = R/N
    r = np.arange(1,N)*h
    v = (a+b)*r-b*ell
    lower = -2*D/h**2 + D/(h*r) - v/(2*h)
    upper = -2*D/h**2 - D/(h*r) + v/(2*h)
    diag = a+4*D/h**2+2*D/r**2
    matrix = diags([lower[1:],diag,upper[:-1]],[-1,0,1],format='csr')
    rhs = r-ell
    rhs[-1] -= upper[-1]*(R-ell)/(2*a+b)
    g = spsolve(matrix,rhs)
    rr = np.concatenate(([0.],r,[R]))
    gg = np.concatenate(([0.],g,[(R-ell)/(2*a+b)]))
    ff = rr-ell
    prob_weight = rr*np.exp(-(a*rr**2+b*(rr-ell)**2)/(4*D))
    prob_weight /= trapezoid(prob_weight,rr)
    E_ff=trapezoid(prob_weight*ff**2,rr)
    E_fg=trapezoid(prob_weight*ff*gg,rr)
    return E_ff-a*E_fg, E_ff, E_fg


def direct_linear_ou(a,b,D,delta):
    """Independent two-dimensional linear OU covariance calculation, per coordinate."""
    drift=np.array([[-a,delta],[0.,-(a+b)]])
    cov=solve_continuous_lyapunov(drift, -np.diag([D,4*D]))
    # f=q for zero-length spring, in two spatial dimensions.
    expected_dot_f_vr=2*(-a*cov[0,1]+delta*cov[1,1])
    sigma=(2*delta/D)*expected_dot_f_vr
    return sigma, cov


def run():
    for a,b,D,delta in [(1.,3.,.7,.25),(.3,2.1,1.4,.4),(2.,.7,.6,-.3)]:
        expected=8*delta**2/(2*a+b)
        epr,cov=direct_linear_ou(a,b,D,delta)
        assert abs(epr-expected)<1.e-12,(a,b,epr,expected)
        assert abs(cov[1,1]-2*D/(a+b))<1.e-12
        # Radial Poisson calculation should give B=4D/(2a+b).
        B,*_=radial_resolvent(a,b,D,0.,N=2300,R=14.*(D/(a+b))**0.5)
        target=4*D/(2*a+b)
        assert abs(B-target)/target < 2.e-4,(a,b,B,target)
    # Check strictly positive resolvent coefficient for genuinely nonlinear springs
    for ell in [0.4,0.8,1.5]:
        B1,*_=radial_resolvent(1.,2.,1.,ell,N=1800,R=12.)
        B2,*_=radial_resolvent(1.,2.,1.,ell,N=3000,R=12.)
        assert B2>0. and abs(B1-B2)/B2<0.004,(ell,B1,B2)
        print(f'ell={ell:g}: B={B2:.10g}; sigma(delta=.2)={2*.2**2*B2:.10g}')
    print('PASS: 3 independent linear-OU EPR identities, 3 zero-length radial checks, 3 finite-rest-length radial convergence tests')

if __name__=='__main__': run()
