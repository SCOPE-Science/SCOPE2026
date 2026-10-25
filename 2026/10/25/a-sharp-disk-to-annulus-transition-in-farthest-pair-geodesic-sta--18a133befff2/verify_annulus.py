"""Numerical diagnostics for intrinsic-distance tails on concentric annuli.

Requires NumPy.  Finite quadrature tests support but do not replace the proof.
"""
from math import atan, pi, sqrt
from numpy.polynomial.legendre import leggauss
import numpy as np


def crossover_integral(a):
    if a <= 1 / sqrt(2):
        return 4 / 15 * (4 * (1 - a*a)**2.5 + 5*a**3 - 4*a**5)
    return 1 / (3*a)


def angular_tail_threshold(R, r, eps, rho, sig):
    K = R*R-r*r
    diam = 2*sqrt(K)+2*r*atan(r/sqrt(K)) if r else 2*R
    t = diam-eps
    direct = (rho*rho+sig*sig-t*t)/(2*rho*sig)
    theta_direct = np.arccos(np.clip(direct,-1,1))
    if not r:
        return np.where(direct < -1,pi,theta_direct)
    alpha = np.arccos(np.clip(r/rho,0,1))
    beta = np.arccos(np.clip(r/sig,0,1))
    straight = np.sqrt(rho*rho-r*r)+np.sqrt(sig*sig-r*r)
    g = straight -r*(alpha+beta)
    theta_detour = (t-g)/r
    theta = np.where(t>=straight,theta_detour,theta_direct)
    return np.clip(theta,0,pi)


def quadrature_tail(R,r,eps,n=200):
    K = R*R-r*r
    c = sqrt(K)/R
    nodes,weights=leggauss(n)
    # Near the diameter, the radial defect is at most eps/c to first order.
    max_scaled_defect=min((R-r)/eps,2.5/max(c,0.01))
    xx=(nodes+1)*max_scaled_defect/2
    ww=weights*max_scaled_defect/2
    u,v=np.meshgrid(xx,xx,indexing='ij')
    rho=R-eps*u
    sigma=R-eps*v
    theta=angular_tail_threshold(R,r,eps,rho,sigma)
    return float(np.sum(ww[:,None]*ww[None,:]*4*rho*sigma*eps*eps/K**2*(pi-theta)/pi))


def run():
    cases=0
    for a in (0,0.2,0.5,1/sqrt(2),1,2):
        for eps in ((0.0015,0.0005) if a==2 else (0.005,0.0015)):
            R=1.
            r=a*sqrt(R*eps)
            actual=quadrature_tail(R,r,eps)
            predicted=2*crossover_integral(a)*eps**2.5/(pi*R**2.5)
            ratio=actual/predicted
            print(f"Crossover a={a:.6g}, eps={eps:g}: observed/predicted={ratio:.7f}")
            assert abs(ratio-1)<0.035
            cases+=1
    for r in (0.2,0.6,0.9):
        for eps in (0.003,0.001):
            R=1.
            K=R*R-r*r
            actual=quadrature_tail(R,r,eps)
            predicted=2*R**4*eps**3/(3*pi*r*K**3)
            ratio=actual/predicted
            print(f"Fixed hole r={r:g}, eps={eps:g}: observed/predicted={ratio:.7f}")
            assert abs(ratio-1)<0.03
            cases+=1
    print(f"PASS: {cases} approximate endpoint-law cases; no infinite proof is inferred.")

if __name__ == '__main__':
    run()
