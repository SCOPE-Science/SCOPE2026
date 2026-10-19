#!/usr/bin/env python3
"""Exact-rational checks for a two-variable composite quadratic family."""
from fractions import Fraction as F


def data(n):
    assert isinstance(n,int) and n >= 3
    d=F(1,n); h=2-d; q=h*d*d
    p2=F(n*n); v=(d,-q); s=(q,d)
    grad=(-(1+d),1-d)
    dot=lambda x,y:sum(a*b for a,b in zip(x,y))
    f=lambda x:F(1,2)*dot(x,x)+dot(grad,x)+abs(x[0]+x[1])
    K=dot(v,v); D=d*d+h*q
    C=dot(grad,s); S=d+q
    alpha=D/K
    output=(alpha*v[0],alpha*v[1])
    assert 0<q<d and h-q>0
    # Exact P-normalized nonsmooth proximal stationarity.
    assert (grad[0]+v[0]+1,grad[1]+p2*v[1]+1)==(0,0)
    assert v[0]+v[1]>0
    # Conjugacy, rank, one-sided slope tests and unique scalar minima.
    assert dot(v,s)==0 and v[0]*s[1]-v[1]*s[0]==K>0
    assert S-C==d*d+(2+d)*q>0
    assert S+C==d*(h-q)>0
    assert dot(grad,v)+(d-q)==-D
    assert dot(grad,v)-(d-q)==-D-2*(d-q)
    assert f((F(0),F(0)))==0
    assert f(output)==-D*D/(2*K)
    assert f(s)==F(1,2)*K+C+S
    assert f((-s[0],-s[1]))==F(1,2)*K-C+S
    # Independent full-model stationarity with subgradient d of |x1+x2|.
    xstar=(F(1),F(-1))
    assert (xstar[0]+grad[0]+d,xstar[1]+grad[1]+d)==(0,0)
    assert abs(d)<1 and sum(xstar)==0 and f(xstar)==-1
    ratio=-f(output)
    expected=d*d*(1+h*h)**2/(2*(1+h*h*d*d))
    assert ratio==expected>0
    return ratio


def main():
    for n in range(3,257):
        data(n)
    assert data(3)==F(289,477)
    assert data(4)==F(845,1952)
    assert data(10)==F(212521,2072200)
    assert data(100)==F(2460259201,2000792020000)
    # Uniform analytic limit estimate from the explicit closed formula.
    # With d=1/n and 5/3<=h<2 for n>=3, n^2*R is positive and <25/2.
    for n in range(3,257):
        assert 0<n*n*data(n)<F(25,2)
    print('VERIFY_OK exact_family_cases=254 exact_endpoint_witnesses=4 metric_and_line_certificates=254 limit_envelope_cases=254')


if __name__=='__main__':
    main()
