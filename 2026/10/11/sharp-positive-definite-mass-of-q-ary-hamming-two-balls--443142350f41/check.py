#!/usr/bin/env python3
"""Exact rational verification of the degree-two q-ary Hamming Turan certificates.
Run: python check.py. No third-party packages are needed.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product

def K(j,k,d,q):
    return sum((-1)**h * (q-1)**(j-h) * comb(k,h) * comb(d-k,j-h)
               for h in range(j+1) if h<=k and j-h<=d-k)

def test(q,d):
    mu=Q(d*(q-1),q)
    r=mu.numerator//mu.denominator
    theta=mu-r
    sigma2=Q(d*(q-1),q*q)
    den=sigma2-theta*(1-theta)
    assert den>0 and 1<=r<d
    P=lambda k:Q((k-r)*(k-r-1),1)/den
    a=2*(Q(q-1,q)-theta)/(q*den)
    b=Q(2,q*q)/den
    assert a>=0 and b>0
    assert all(P(k)>=0 for k in range(d+1))
    assert all(P(k)==1+a*K(1,k,d,q)+b*K(2,k,d,q) for k in range(d+1))
    weights=[comb(d,k)*(q-1)**k for k in range(d+1)]
    assert sum(weights[k]*P(k) for k in range(d+1))==q**d
    M=P(0)
    alpha=M*(r+1-mu)-(r+1)
    beta=M*(mu-r)+r
    assert alpha>=0 and beta>0
    for j in range(3):
        lhs=M*sum(weights[k]*k**j for k in range(d+1))/q**d - (0**j if j else 1)
        rhs=alpha*r**j+beta*(r+1)**j
        assert lhs==rhs
    if d%q==1:
        assert alpha==0
        den_alt=sigma2+(mu-r-1)*(mu-r-2)
        P_alt=lambda k:Q((k-r-1)*(k-r-2),1)/den_alt
        assert P_alt(0)==M
        assert all(P_alt(k)>=0 for k in range(d+1))
        assert sum(weights[k]*P_alt(k) for k in range(d+1))==q**d
    else:
        assert alpha>0
    return M

def direct_check(q,d):
    # Prime fields, and q=4 realized as the additive group of F_2^2.
    assert q in (3,4,5)
    mu=Q(d*(q-1),q);r=mu.numerator//mu.denominator
    theta=mu-r;den=Q(d*(q-1),q*q)-theta*(1-theta)
    a=2*(Q(q-1,q)-theta)/(q*den);b=Q(2,q*q)/den
    elements=list(product(range(q),repeat=d))
    for y in elements:
        total=0j
        for x in elements:
            wt=sum(xi!=0 for xi in x)
            val=(1 if wt==0 else a if wt==1 else b if wt==2 else 0)
            if q==4:
                phase=(-1)**sum(((xi&1)*(yi&1) + ((xi>>1)&1)*((yi>>1)&1)) for xi,yi in zip(x,y))
            else:
                import cmath
                phase=cmath.exp(-2j*cmath.pi*sum(xi*yi for xi,yi in zip(x,y))/q)
            total+=float(val)*phase
        expected=Q((sum(t!=0 for t in y)-r)*(sum(t!=0 for t in y)-r-1),1)/den
        assert abs(total-float(expected))<1e-8,(q,d,y,total,expected)

if __name__=='__main__':
    tests=0
    for q in (3,4,5,7,8,9,11,13,16):
        for d in range(3,65):
            test(q,d);tests+=1
    for q,d in ((3,3),(3,4),(3,5),(4,3),(4,4),(5,3)):
        direct_check(q,d)
    print('PASS: exact rational certificates for',tests,'(q,d) pairs and direct character transforms for 6 small spaces')
