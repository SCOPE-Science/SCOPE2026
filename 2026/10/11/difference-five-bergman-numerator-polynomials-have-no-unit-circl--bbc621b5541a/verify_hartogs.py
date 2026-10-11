#!/usr/bin/env python3
"""Exact rational certificate for the difference-five Bergman numerator theorem.

Run with Python 3 (standard library only).  This is a finite algebraic
certificate used together with the degree-three block-sum argument in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path
import json

# Coefficients in ascending monomial degree x^0,...,x^5.
B = {
 1: [65, -169, -288, 652, 1056, 304],
 2: [71, -238, -324, 856, 1392, 448],
 3: [89, -301, -432, 1108, 1824, 592],
 4: [119, -358, -612, 1408, 2352, 736],
}
C = {
 1: [14, -26, -44, 96, 144, 32],
 2: [15, -48, -40, 144, 208, 64],
 3: [20, -64, -68, 208, 320, 96],
 4: [33, -80, -136, 304, 480, 128],
}


def p_add(p, v):
    n=max(len(p),len(v))
    return [(p[i] if i<len(p) else 0)+(v[i] if i<len(v) else 0)
            for i in range(n)]


def p_mul(p, v):
    a=[0]*(len(p)+len(v)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(v):
            a[i+j]+=x*y
    return a


def p_scale(p, scalar):
    return [x*scalar for x in p]


def chebyshev(degree):
    if degree==0: return [1]
    if degree==1: return [0,1]
    p0,p1=[1],[0,1]
    for _ in range(2,degree+1):
        p0,p1=p1,p_add(p_scale(p_mul([0,1],p1),2),p_scale(p0,-1))
    return p1


def numerator_diagonal_coefficients(n):
    """Specialize source Theorem 1.3 at m=n+5, returning c_0,...,c_10."""
    m=n+5
    assert n>=1 and gcd(m,n)==1
    coeff=[0]*11
    coeff[5]+=m*m
    for t in range(1,m):
        h=(5*t-1)//m
        aa=m*(h+1)-5*t
        bb=5*t-m*h
        assert 0<=h<=4 and aa>0 and bb>0
        coeff[h]+=t*aa
        coeff[h+1]+=t*bb
        coeff[5+h]+=(m-t)*aa
        coeff[6+h]+=(m-t)*bb
    assert coeff==coeff[::-1]
    return coeff


def R_coeff(n):
    a=numerator_diagonal_coefficients(n)
    p=[a[5]]
    for k in range(1,6):
        p=p_add(p,p_scale(chebyshev(k),2*a[5-k]))
    return p+[0]*(6-len(p))


# A direct expansion of (x+2)(4x^2+2x-1)^2.
core=p_mul([2,1],p_mul([-1,2,4],[-1,2,4]))
assert len(core)==6


def prediction(q,r):
    # B has a factor 1/3, as does the leading coefficient 5/3.
    return p_add(
        p_add(p_scale(core,F(5*q**3,3)+(r+5)*q*q),
              p_scale([F(v,3) for v in B[r]],q)),
        C[r])


def bernstein_coefficients(coefficient):
    # Intervals [-1+j/4,-1+(j+1)/4], j=0,...,7.
    coefficients=[]
    for interval in range(8):
        a=F(-1)+F(interval,4)
        b=F(1,4)
        # P(a+b*u)= sum_d Taylor[d] u^d.
        power=[sum(F(coefficient[k])*comb(k,d)*a**(k-d)*b**d
                   for k in range(d,len(coefficient))) for d in range(6)]
        for j in range(6):
            beta=sum(power[d]*F(comb(j,d),comb(5,d))
                     for d in range(j+1))
            assert beta>0, ('Bernstein coefficient not positive',interval,j,beta)
            coefficients.append(beta)
    return coefficients


def main():
    certificate=json.loads(Path(__file__).with_name("BERNSTEIN_CERTIFICATE.json").read_text(encoding="utf-8"))
    assert certificate["domain"]=="[-1,1]" and certificate["subintervals"]==8
    for r in range(1,5):
        # For fixed r, the source coefficient block sums are polynomials in q
        # of degree <=3. Consequently four exact nodes prove the identity.
        for q in range(4):
            n=5*q+r
            assert R_coeff(n)==prediction(q,r), ('identity',q,r)
        bvalues=bernstein_coefficients([F(v,3) for v in B[r]])
        cvalues=bernstein_coefficients(C[r])
        assert certificate["r"+str(r)]["B"]==[str(b) for b in bvalues]
        assert certificate["r"+str(r)]["C"]==[str(b) for b in cvalues]
        bmin=min(bvalues);cmin=min(cvalues)
        print('r=',r,'  B-min=',str(bmin),'  C-min=',str(cmin))
    print('PASS: all 16 exact polynomial identities and all 384 Bernstein coefficients strictly positive')


if __name__=='__main__':
    main()
