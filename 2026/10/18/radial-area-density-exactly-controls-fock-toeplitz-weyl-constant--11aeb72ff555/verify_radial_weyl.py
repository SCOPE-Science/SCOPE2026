#!/usr/bin/env python3
"""Finite numerical checks for radial weighted-Fock moment asymptotics.
These checks are not an infinite-dimensional proof.
"""
from math import sin, cos, log, exp, sqrt
from scipy.optimize import brentq
from scipy.integrate import quad

BETA = 1.6

def profile(kind,r):
    if kind == 'gaussian':
        return .5*r*r, r, 1.0
    if kind == 'oscillating_hessian':
        return .5*r*r+.2*(1-cos(r)), r+.2*sin(r), 1+.2*sin(r)/r if r else 1.2
    if kind == 'oscillating_slope':
        q=log(1+r*r)
        phi=.5*r*r+.05*((1+r*r)*(sin(q)-cos(q))+1)
        b=1+.2*sin(q)
        return phi,r*b,b
    raise ValueError(kind)

def moment(kind,n):
    def critical(r):
        return r*profile(kind,r)[1]-(n+.5)
    root=brentq(critical,1e-8,5*sqrt(n+1),xtol=1e-12)
    peak=(2*n+1)*log(root)-2*profile(kind,root)[0]
    def kern(r):
        if r<=0: return 0.
        return exp((2*n+1)*log(r)-2*profile(kind,r)[0]-peak)
    low=max(1e-8,root-19)
    hi=root+19
    den=quad(kern,low,hi,epsabs=1e-11,epsrel=1e-10,limit=200)[0]
    num=quad(lambda r:kern(r)*(1+r*r)**(-BETA/2),low,hi,epsabs=1e-12,epsrel=1e-10,limit=200)[0]
    lam=num/den
    pred=profile(kind,root)[2]**(BETA/2)
    scaled=(n+1)**(BETA/2)*lam
    return root,scaled,pred

def main():
    all_checks=0
    for kind in ('gaussian','oscillating_hessian','oscillating_slope'):
        for n in (40,100,400,1600):
            r,scaled,pred=moment(kind,n)
            err=abs(scaled-pred)
            assert err<4/sqrt(n), (kind,n,r,err,scaled,pred)
            all_checks+=1
            print(kind,n, 'r',format(r,'.5f'), 'scaled',format(scaled,'.8f'),
                  'slope',format(pred,'.8f'), 'delta',format(err,'.6f'))
    for r in (2,6,20,200):
        phi,phip,b=profile('oscillating_slope',r)
        approx=(profile('oscillating_slope',r+.0001)[0]-profile('oscillating_slope',r-.0001)[0])/.0002
        assert abs(approx-phip) < 2e-5
        assert abs(phip/r-b) < 1e-12
        all_checks+=2
    print('RADIAL_FOCK_WEYL_MOMENT_CHECKS_OK checks='+str(all_checks))
if __name__=='__main__':main()
