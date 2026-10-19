#!/usr/bin/env python3
"""Exact rational checks for a two-interval Fourier covariogram identity."""
from fractions import Fraction as Q
from math import sin, cos, pi

def intervals(ell, sep, eta):
    return [((-sep-ell-eta)/2,(-sep+ell+eta)/2),
            ((sep-ell+eta)/2,(sep+ell-eta)/2)]

def cov(sets, t):
    total=Q(0)
    for a,b in sets:
        for c,d in sets:
            total+=max(Q(0), min(b,d+t)-max(a,c+t))
    return total

def breaks(sets):
    return {u-v for a,b in sets for c,d in sets for u in (a,b) for v in (c,d)}

def square_cov_diff(ell,sep,eta):
    S=intervals(ell,sep,eta); T=intervals(ell,sep,Q(0))
    nodes=sorted(breaks(S)|breaks(T)); answer=Q(0)
    for x,y in zip(nodes[:-1],nodes[1:]):
        left=cov(S,x)-cov(T,x)
        right=cov(S,y)-cov(T,y)
        answer+=(y-x)*(left**2+left*right+right**2)/3
    return answer

def predicted(ell,sep,eta):
    a=abs(eta); g=sep-ell
    if g<=a:
        return 4*a*g*g-2*g**3
    if g<=2*a:
        return Q(8,3)*a**3-Q(2,3)*(2*a-g)**3
    return Q(8,3)*a**3

def power_direct(ell,sep,eta,omega):
    if omega==0: return (2*ell)**2
    xi=2*pi*omega
    x=sin(xi*(ell+eta)/2)
    y=sin(xi*(ell-eta)/2)
    return 4*(x*x+y*y+2*x*y*cos(xi*sep))/xi**2

def power_difference(ell,sep,eta,omega):
    if omega==0:return 0.0
    xi=2*pi*omega
    return 4*(1-cos(eta*xi))*(cos(ell*xi)-cos(sep*xi))/xi**2

def main():
    tests=[(Q(1),Q(3),Q(1,10)),(Q(2),Q(5),Q(1,5)),
           (Q(3,2),Q(7,2),Q(1,7)),
           (Q(1),Q(1)+Q(1,25),Q(1,10)),
           (Q(1),Q(11,10),Q(1,10)),
           (Q(1),Q(23,20),Q(1,10)),
           (Q(1),Q(6,5),Q(1,10)),
           (Q(1),Q(13,10),Q(1,10))]
    for ell,sep,eta in tests:
        assert 0<eta<ell<sep
        direct=square_cov_diff(ell,sep,eta)
        exact=predicted(ell,sep,eta)
        assert direct==exact,(ell,sep,eta,direct,exact)
        for w in [0.003,0.12,0.5,1.2,3.1]:
            lhs=power_direct(float(ell),float(sep),float(eta),w)-power_direct(float(ell),float(sep),0.,w)
            rhs=power_difference(float(ell),float(sep),float(eta),w)
            assert abs(lhs-rhs)<3e-11,(ell,sep,eta,w,lhs,rhs)
    print('PASS: 8 exact rational covariogram integrals; 40 direct Fourier checks.')

if __name__=='__main__':main()
