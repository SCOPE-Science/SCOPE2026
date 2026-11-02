#!/usr/bin/env python3
"""Exact small-case moment tests for character restriction to proper cycle colourings."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import cos, pi

def proper(q,n):
    for w in product(range(q),repeat=n):
        if all(w[i]!=w[(i+1)%n] for i in range(n)):
            yield w

def pair_ratio(q,n,d):
    a=q-1
    Z=a**n+a*(-1)**n
    return Fraction((-1)**d*a**(n-d)+(-1)**(n-d)*a**d+(q-2)*(-1)**n,Z)

def lambda_formula(q,n,k):
    a=q-1
    Z=a**n+a*(-1)**n
    D=a**n-(-1)**n
    if k==0:
        return (D*(a-1)/(a+1)+n*(a-1)*(-1)**n)/Z
    return D*(a*a-1)/(Z*(a*a+1+2*a*cos(2*pi*k/n)))

def check():
    cases=0;moment_tests=0;spectral_tests=0;pair_cell_tests=0
    for q in (3,4,5):
        for n in (3,4,5,6):
            W=list(proper(q,n)); Z=len(W)
            assert Z==(q-1)**n+(q-1)*(-1)**n
            for d in range(n):
                same=sum(w[0]==w[d] for w in W)
                empirical=Fraction(q*same-Z,(q-1)*Z)
                expected=pair_ratio(q,n,d)
                assert empirical==expected,(q,n,d,empirical,expected)
                # Check every actual colour-pair cell, including diagonal/off-diagonal uniformity.
                cnt=Counter((w[0],w[d]) for w in W)
                for u in range(q):
                    for v in range(q):
                        target=Fraction(same,q) if u==v else Fraction(Z-same,q*(q-1))
                        assert cnt[u,v]==target,(q,n,d,u,v,cnt[u,v],target)
                        pair_cell_tests+=1
                moment_tests+=1
            for k in range(n):
                val=sum(float(pair_ratio(q,n,d))*complex(cos(-2*pi*k*d/n),__import__('math').sin(-2*pi*k*d/n)) for d in range(n))
                assert abs(val.imag)<1e-9
                assert abs(val.real-lambda_formula(q,n,k))<1e-9,(q,n,k,val,lambda_formula(q,n,k))
                spectral_tests+=1
            cases+=1
    for q in range(3,35):
        for n in range(3,100):
            vs=[lambda_formula(q,n,k) for k in range(n)]
            if q==3 and n==3:
                assert abs(vs[0])<1e-11
            else:
                assert min(vs)>0,(q,n,min(vs))
                cond=max(vs)/min(vs)
                sharp=1.5*(4+5**.5)
                assert cond<=sharp+1e-9,(q,n,cond)
            if q>=4:
                assert max(vs)/min(vs)<=4+1e-8
    print('PASS',cases,'complete enumerations,',moment_tests,'exact pair-moment comparisons,',pair_cell_tests,'exact colour-pair cell checks,',spectral_tests,'DFT checks, 3000+ global-bound spot checks')
if __name__=='__main__':check()
