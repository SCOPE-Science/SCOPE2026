#!/usr/bin/env python3
"""Reproduce exact checks for finite-path outbreak moment-source ambiguity.
Requires Python 3 and SymPy 1.14; prints a deterministic JSON certificate.
"""
import json
from fractions import Fraction
from itertools import product
from math import isqrt
import sympy as s


def summary(n, source, p):
    # source is a one-based path index
    x = s.Integer(0) if isinstance(p, s.Basic) else Fraction(0)
    mu = 1 + sum(p**i for i in range(1,source)) + sum(p**i for i in range(1,n-source+1))
    def armvar(L):
        tail = sum((p**i for i in range(1,L+1)), x)
        sq = sum(((2*i-1)*p**i for i in range(1,L+1)), x)
        return sq-tail**2
    return mu, armvar(source-1)+armvar(n-source)


def brute(n, source, p):
    one = Fraction(1)
    E = Fraction(0); E2 = Fraction(0)
    for edges in product((0,1), repeat=n-1):
        weight = p**sum(edges)*(one-p)**(n-1-sum(edges))
        a = source-1
        while a>0 and edges[a-1]: a-=1
        b = source-1
        while b<n-1 and edges[b]: b+=1
        size = b-a+1
        E += weight*size; E2 += weight*size*size
    return E, E2-E*E


def main():
    count=0
    for n in range(2,10):
        for k in range(1,n+1):
            for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                assert brute(n,k,p)==summary(n,k,p), (n,k,p)
                count+=1
    p,q=s.symbols('p q')
    v3end=summary(3,1,p)[1]
    v3mid=summary(3,2,(p+p*p)/2)[1]
    assert s.expand(v3end-v3mid-p**2*(1-p)*(p+3)/2)==0
    m4end,v4end=summary(4,1,p)
    m4mid,v4mid=summary(4,2,q)
    me=m4end-1;mi=m4mid-1
    asserted=2*(p**2+2*p**3-2*q**2-q**3)-(me-mi)*(me+mi-1)
    assert s.expand(v4end-v4mid-asserted)==0
    m52,v52=summary(5,2,p)
    m53,v53=summary(5,3,q)
    F=s.expand(m52-m53);G=s.expand(v52-v53)
    poly=s.Poly(p**9+5*p**8+11*p**7+7*p**6-8*p**5+56*p**3+88*p**2+32*p-32,p)
    assert s.factor(s.resultant(F,G,q)) == 4*p**2*(p-1)*poly.as_expr()
    lo=s.Rational(411971,1000000);hi=s.Rational(411973,1000000)
    assert poly.eval(lo)<0<poly.eval(hi)
    # The derivative is strictly positive on (0,1):
    # 168p^2-40p^4 >= 128p^2, all other derivative terms are nonnegative.
    assert s.expand(s.diff(poly.as_expr(),p)-(9*p**8+40*p**7+77*p**6+42*p**5-40*p**4+168*p**2+176*p+32))==0
    assert poly.eval(0)<0<poly.eval(1)
    # For every n>=5, compare variance/mean-deficit slopes near p=1.
    # A1-A2=m-2 and B1-B2=m^2-4 for m=n-2.
    for n in range(5,601):
        m=n-2
        A2=3+sum(range(1,m)); B2=5+sum(i*i for i in range(1,m))
        A1=1+sum(range(1,m+1)); B1=1+sum(i*i for i in range(1,m+1))
        assert A1-A2==m-2 and B1-B2==m*m-4
        assert B1*A2>B2*A1
    # Independent exact low-p expansion check on finite representatives.
    for n in range(5,14):
        p,q=s.symbols('p q')
        mu2,va2=summary(n,2,p);mu3,va3=summary(n,3,q)
        qser=p-p**2/2
        assert s.expand(mu2-mu3.subs(q,qser)).series(p,0,3).removeO()==0
        assert s.simplify((va2-va3.subs(q,qser)).series(p,0,3).removeO()+2*p*p)==0
    result={
      'model':'independent Bernoulli bond retention on labeled paths',
      'checker':'exact enumeration + symbolic identities + exact rational inequalities',
      'sympy_version':s.__version__,
      'enumerated_cases':count,
      'small_order_distinction':'n=3 and n=4 identities exact',
      'five_vertex_resultant':str(s.factor(s.resultant(F,G,q))),
      'five_vertex_unique_root_interval':['411971/1000000','411973/1000000'],
      'near_zero_variance_gap_leading_term':'-2*p**2',
      'near_one_ratio_checked_integer_orders':[5,600],
      'limitation':'finite enumerations and symbolic certificates supplement, not replace, the all-n analytic proof'
    }
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
