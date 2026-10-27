"""Separate numerical checks for stationary covariance-axis exchanges in a confined active Brownian particle.
Only ordinary deterministic mathematical tests; no external dependencies beyond numpy, scipy, sympy.
"""
import math
import numpy as np
from numpy.polynomial.laguerre import laggauss
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
import sympy as sp


def exact(k, d, r, v=1., D=0.):
    mean = v*r/((r+d)*(r+k))
    s2 = 2*v*v*r/((r+2*k)*(r+k+d)*(r+4*d))
    ab2 = (2*v*v/(r+k+d)+4*D)/(r+2*k)
    sx = (ab2+s2)/2-mean**2
    sy = (ab2-s2)/2
    return mean, sx, sy


def polynomial(k,d,r):
    return r**4+(k-d)*r**3-(2*d*d+6*d*k)*r*r-4*d*k*(d+k)*r+2*d*d*k*k


def rootpair(k,d):
    x=np.roots([1.,k-d,-2*d*d-6*d*k,-4*d*k*(d+k),2*d*d*k*k])
    reals=sorted(z.real for z in x if abs(z.imag)<1.e-6 and z.real>0)
    assert len(reals)==2 and reals[0]<d<reals[1]
    return reals


def independent_angle_age_quadrature(k,d,r,v,D,na=120,ns=100):
    # Renewal-age construction, directly integrating the Gaussian angular
    # two-time kernels, not using the stationary generator/moment equations.
    an,aw=laggauss(na)
    sn,sw=leggauss(ns)
    av_mean=av_z2=av_abs2=0.
    for u,w in zip(an,aw):
        a=u/r
        time=(sn+1)*a/2
        weight=sw*a/2
        G=np.exp(-k*(a-time))
        t1=time[:,None];t2=time[None,:]
        kernel=np.outer(weight*G, weight*G)
        # Theta begins at 0 after a joint reset.
        phase_plus=np.exp(-d*(np.maximum(t1,t2)+3*np.minimum(t1,t2)))
        phase_diff=np.exp(-d*np.abs(t1-t2))
        av_mean += w * v*np.sum(weight*G*np.exp(-d*time))
        av_z2 += w * v*v*np.sum(kernel*phase_plus)
        av_abs2 += w*(v*v*np.sum(kernel*phase_diff)
                       +2*D*(-np.expm1(-2*k*a))/k)
    return (av_mean,(av_abs2+av_z2)/2-av_mean**2,
            (av_abs2-av_z2)/2)


def checks():
    r,k,d=sp.symbols('r k d',positive=True)
    polynomial_sym=sp.expand(2*(r+d)**2*(r+k)**2-r*(r+2*k)*(r+k+d)*(r+4*d))
    assert sp.simplify(polynomial_sym.subs(r,d)+d*d*(2*d*d+9*d*k+2*k*k))==0
    assert all(sp.simplify(u-v)==0 for u,v in zip(sp.Poly(polynomial_sym,r).all_coeffs(),[1,k-d,-2*d*d-6*d*k,-4*d*k*(d+k),2*d*d*k*k]))
    assert sp.factor(polynomial_sym.subs(k,0))==r*r*(r-2*d)*(r+d)
    # Extract asymptotic scaling limits of the polynomial.
    b,y=sp.symbols('b y',positive=True)
    F=polynomial_sym.subs({d:1,k:b})
    assert sp.limit(sp.expand(F.subs(r,b*y))/b**2,b,0)==2-4*y-2*y**2
    assert sp.limit(sp.expand(F)/b**2,b,sp.oo)==2-4*r
    assert sp.limit(sp.expand(F.subs(r,sp.sqrt(b)*y))/b**sp.Rational(5,2),b,sp.oo)==y**3-4*y

    cases=[(.15,1.,.2),(1.,1.,1.),(5.,1.,1.),(3.,.2,2.),(.15,2.,.3),(10.,2.,.3)]
    maximum_absolute_error=0.
    for rr,kk,dd in cases:
        aa=exact(kk,dd,rr,1.7,.25)
        bb=independent_angle_age_quadrature(kk,dd,rr,1.7,.25)
        err=max(abs(x-y) for x,y in zip(aa,bb))
        maximum_absolute_error=max(maximum_absolute_error,err)
        assert err<0.00018,(rr,kk,dd,aa,bb,err)
    for kk,dd in [(1.,1.),(.01,1.),(100.,1.),(1.,.01),(1.,100.),(.7,3.),(4.2,.19)]:
        roots=rootpair(kk,dd)
        values=[polynomial(kk,dd,roots[0]/2),polynomial(kk,dd,dd),polynomial(kk,dd,roots[1]*2)]
        assert values[0]>0 and values[1]<0 and values[2]>0
        for rr in [roots[0]/2, dd, roots[1]*2]:
            _,sx,sy=exact(kk,dd,rr,v=2.,D=10.)
            _,tx,ty=exact(kk,dd,rr,v=2.,D=0.)
            assert abs((sx-sy)-(tx-ty))<1e-12
    # Numerical reference at unit angular diffusion and trap relaxation.
    small,big=rootpair(1.,1.)
    assert abs(small-.207269894659199)<1e-12
    assert abs(big-3.20915394294682)<1e-12
    print('PASS: exact symbolic polynomial and root structure')
    print('PASS: renewal-angle quadrature of mean and covariance, six settings; maximum absolute discrepancy:',maximum_absolute_error)
    print('PASS: root signs, two positive roots and thermal invariance over seven parameter regimes')
    print('reference roots for k=d=1:',small,big)
    print('reference differences at rates 0.1, 1, 5:',[exact(1,1,rr,D=.3)[1]-exact(1,1,rr,D=.3)[2] for rr in (.1,1,5)])

if __name__=='__main__':
    checks()
