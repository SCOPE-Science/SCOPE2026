#!/usr/bin/env python3
"""Deterministic finite verification of weighted Bergman carrier bounds.

Checks do not constitute proofs of the infinite-parameter asymptotics.
"""
import math
import numpy as np
from scipy.special import gammaln
from scipy.optimize import brentq


def M(k, a):
    return math.exp(gammaln(a)+gammaln(k+1)-gammaln(k+a))


def fourth(coeff, m, a, r):
    b = np.convolve(coeff, coeff)
    return sum(abs(v)**2 * M(2*m+j, a)*r**(4*m+2*j) for j,v in enumerate(b))


def ratio(coeff, m, a, r):
    z = sum(abs(v)**2*M(m+j,a) for j,v in enumerate(coeff))
    return fourth(coeff,m,a,r)/z**2


def circH(coeff):
    b=np.convolve(coeff,coeff)
    return sum(abs(v)**2 for v in b)/sum(abs(v)**2 for v in coeff)**2


def test():
    count=0
    for a in (1.2, 2., 3.7):
        for m in (10, 40, 250):
            for L in (1, 2, 3, 5, 9):
                rr=np.random.default_rng(int(a*100)+m+L)
                for r in (.6, .9, .992):
                    for _ in range(4):
                        c=rr.normal(size=L)+1j*rr.normal(size=L)
                        q=ratio(c,m,a,r)
                        h=circH(c)
                        lo=h*r**(4*(m+L-1))*M(2*m+2*L-2,a)/M(m,a)**2
                        up=h*r**(4*m)*M(2*m,a)/M(m+L-1,a)**2
                        assert lo<=q*(1+4e-12) and q<=(1+4e-12)*up,(a,m,L,r,q,lo,up)
                        count+=1
    # Exact known three-frequency fourth-moment witnesses.
    c=np.array([math.sqrt(2/7),math.sqrt(3/7),math.sqrt(2/7)])
    assert abs(circH(c)-15/7)<1e-12
    c=np.array([1/math.sqrt(3),1/math.sqrt(3),0,1/math.sqrt(3)])
    assert abs(circH(c)-5/3)<1e-12
    count+=2
    # For a single monomial, the sharp cutoff is analytic.
    for a in (1.5,2.,3.):
        for m in (10,100,300):
            root=(M(m,a)**2/M(2*m,a))**(1/(4*m))
            assert abs(ratio(np.array([1.0]),m,a,root)-1)<1e-10
            pred=(a-1)*math.log(m)+(1-a)*math.log(2)-gammaln(a)
            obs=4*m*math.log(1/root)
            assert abs(obs-pred)<10.0/m,(obs,pred)
            count+=1
    print(f'PASS: {count} deterministic finite checks')


if __name__=='__main__':test()
