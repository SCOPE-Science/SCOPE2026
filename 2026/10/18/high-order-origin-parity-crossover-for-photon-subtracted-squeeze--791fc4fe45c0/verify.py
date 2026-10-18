#!/usr/bin/env python3
"""Numerical checks for high-order parity of photon-subtracted squeezed thermal states.
Uses independent truncated Fock-space exponentiation and high-precision coefficient recurrences.
Finite checks corroborate, but do not prove, any infinite-order asymptotic theorem.
"""
import math
import numpy as np
from scipy.linalg import expm
from mpmath import mp


def coefficients(c, d, max_n):
    """Taylor coefficients of (1+c*t-d*t*t)^(-1/2), exact recurrence."""
    a = [mp.mpf(1), -c/2]
    for n in range(2, max_n+1):
        a.append((-(n-mp.mpf('0.5'))*c*a[n-1]+(n-1)*d*a[n-2])/n)
    return a


def cov_parity(nbar, r, m):
    t = mp.mpf(str(nbar)) + mp.mpf('0.5')
    r = mp.mpf(str(r))
    v, w = t*mp.exp(-2*r), t*mp.exp(2*r)
    c = (v+w-4*v*w)/(4*v*w)
    d = (mp.mpf('.5')-v)*(w-mp.mpf('.5'))/(4*v*w)
    cp = 1-v-w
    dp = (mp.mpf('.5')-v)*(w-mp.mpf('.5'))
    numerator = coefficients(c,d,m)[m] / mp.sqrt(4*v*w)
    denominator = coefficients(cp,dp,m)[m]
    return numerator/denominator


def fock_parity(nbar, r, m, N=90):
    a = np.diag(np.sqrt(np.arange(1,N)), 1).astype(float)
    s = expm(0.5*r*(a@a - a.T@a.T))
    q = nbar/(nbar+1)
    weights = (1-q)*np.power(q, np.arange(N, dtype=float))
    weights /= sum(weights)
    rho = (s*weights)@s.T
    probs = np.diag(rho)
    mass = np.array([math.prod(range(k-m+1,k+1)) if k>=m else 0 for k in range(N)],dtype=float)
    num = sum(probs*mass*(-1.)**(np.arange(N)-m))
    den = sum(probs*mass)
    return num/den


def run():
    mp.dps=100
    count_fock=0
    max_err=0.
    for nbar,r in [(0.05,0.5),(0.12,0.4),(0.30,0.65),(0.33,0.5)]:
        for m in range(1,5):
            f = fock_parity(nbar,r,m,N=90)
            g = float(cov_parity(nbar,r,m))
            err=abs(f-g)
            max_err=max(max_err,err)
            assert err<2e-8,(nbar,r,m,f,g,err)
            count_fock+=1
    # Exact all-order sign and the analytic noise boundary sampled above/below.
    signs=0
    r=mp.mpf('0.5'); crit=mp.sinh(r)**2
    for delta in [mp.mpf('-.14'),mp.mpf('-.02'),mp.mpf('.02'),mp.mpf('.14')]:
        nu=crit+delta
        for m in range(1,31):
            val=cov_parity(nu,r,m)
            expect=-1 if delta<0 and m%2 else 1
            assert mp.sign(val)==expect,(nu,m,val,expect)
            signs+=1
    # Check leading exponential prefactors and uniform two-pole thermal boundary layer.
    leading=0
    for nu in [mp.mpf('.03'),mp.mpf('.1'),mp.mpf('.35'),mp.mpf('.42')]:
        T=nu+mp.mpf('.5');v=T*mp.exp(-2*r);w=T*mp.exp(2*r)
        rho_minus=(mp.mpf('.5')-v)/(2*v*(w-mp.mpf('.5')))
        rho_plus=1/(2*w)
        for m in [40,70,100]:
            got=cov_parity(nu,r,m)
            pred=(((-1)**m)*rho_minus**(m+mp.mpf('.5')) if nu<crit else rho_plus**(m+mp.mpf('.5')))
            assert abs(got/pred-1)<mp.mpf('.02'),(nu,m,got/pred)
            leading+=1
    cross=0
    for scaled in [-mp.mpf('.6'),mp.mpf('0'),mp.mpf('.5')]:
        for m in [100,101,200,201]:
            nu=crit+scaled/m
            T=nu+mp.mpf('.5'); v=T*mp.exp(-2*r);w=T*mp.exp(2*r)
            rm=(mp.mpf('.5')-v)/(2*v*(w-mp.mpf('.5')))
            rp=1/(2*w)
            mean=mp.sqrt(rm*rp)
            got=cov_parity(nu,r,m)/mean**(m+mp.mpf('.5'))
            target=(2*mp.cosh(2*scaled/mp.sinh(2*r)) if m%2==0 else 2*mp.sinh(2*scaled/mp.sinh(2*r)))
            assert abs(got-target)<mp.mpf('.08'),(scaled,m,got,target)
            cross+=1
    print(f'VERIFY_OK fock_cases={count_fock} signs={signs} asymptotics={leading} boundary_layer={cross} max_fock_error={max_err:.3g}')

if __name__=='__main__':run()
