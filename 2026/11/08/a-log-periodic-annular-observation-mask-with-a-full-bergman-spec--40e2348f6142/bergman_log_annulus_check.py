#!/usr/bin/env python3
"""Independent finite checks of analytic Bergman logarithmic-annulus formulas.

Requires Python 3.10+, numpy, scipy. Numerical checks do not certify limits.
"""
from math import exp, log, pi
import numpy as np
from scipy.special import gammaln, loggamma, betainc

COUNT = 0

def check(cond, msg):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(msg)

def eigenvalue_by_annuli(n, beta, L, tau, k_max=120):
    """Independently integrate the disjoint annuli using regularized beta CDF."""
    acc = 0.
    for j in range(k_max):
        low = -np.expm1(-j*L)
        high = -np.expm1(-j*L-tau)
        inc = float(betainc(n+1,beta,high) - betainc(n+1,beta,low))
        acc += inc
        if (j+1)*L*beta > 48 and j > 12:
            break
    return acc

def fourier_coeff(k, L, tau):
    if k == 0:
        return tau/L
    omega = 2*pi/L
    return -np.expm1(-1j*k*omega*tau)/(1j*k*omega*L)

def response(s,beta,L,tau,K=64):
    omega = 2*pi/L
    res = tau/L
    for k in range(1,K+1):
        ck = fourier_coeff(k,L,tau)
        g = np.exp(loggamma(beta-1j*k*omega)-gammaln(beta))
        res += 2*(ck*g*np.exp(1j*k*omega*s)).real
    return float(res)

def exact_fourier(n,beta,L,tau,K=64):
    omega = 2*pi/L
    res=tau/L
    for k in range(1,K+1):
        ck=fourier_coeff(k,L,tau)
        g=np.exp(loggamma(beta-1j*k*omega)-gammaln(beta)+gammaln(n+beta+1)-loggamma(n+beta+1-1j*k*omega))
        res += 2*(ck*g).real
    return float(res)

def main():
    L=log(3.)
    tau=.43*L
    for beta in (.5,1.,2.5):
        for n in (0,1,3,10,30,100,500):
            a=eigenvalue_by_annuli(n,beta,L,tau)
            b=exact_fourier(n,beta,L,tau)
            check(abs(a-b)<(3e-3 if n==0 else (1e-5 if n==1 else 5e-6)), f'exact beta-fourier mismatch: {beta},{n},{a},{b}')
            check(0<a<1,'concentration bound')
            if n >= 10:
                approx=response(log(n+1),beta,L,tau)
                check(abs(a-approx)<.25/(n+1),f'gamma limit: {beta} {n}, {a}, {approx}')
    for beta in (.06,.12,.24):
        s=np.linspace(0,L,200,endpoint=False)
        v=np.array([response(float(z),beta,L,tau) for z in s])
        check(v.min()>0 and v.max()<1,'strict gamma smoothing')
        check(v.max()-v.min()>0,'nonconstant gamma filter')
    # Endpoint collapse is linear with beta; compare widths at two nearby beta values.
    s=np.linspace(0,L,400,endpoint=False)
    widths=[]
    for beta in (.02,.04,.08):
        vals=np.array([response(float(z),beta,L,tau) for z in s])
        widths.append(float(np.ptp(vals)))
    check(abs(widths[0]/.02-widths[1]/.04)<.015,'linear width collapse I')
    check(abs(widths[1]/.04-widths[2]/.08)<.025,'linear width collapse II')
    print(f'BERGMAN_LOG_PERIODIC_CHECKS_PASS {COUNT}')

if __name__=='__main__':main()
