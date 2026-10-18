#!/usr/bin/env python3
"""Exact science-only checks of crossing/nesting covariance and joint-CLT premises."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
import sympy as S


def pairings(t):
    if not t:
        yield ()
        return
    first = t[0]
    for j in range(1, len(t)):
        for tail in pairings(t[1:j]+t[j+1:]):
            yield ((first, t[j]),)+tail


def chord_stats(m):
    x=y=0
    for k,(a,b) in enumerate(m):
        for c,d in m[k+1:]:
            x += int(a<c<b<d or c<a<d<b)
            y += int(a<c<d<b or c<a<b<d)
    return x,y


def exact_moments(n):
    s=[0]*5
    count=0
    for m in pairings(tuple(range(2*n))):
        x,y=chord_stats(m)
        s[0]+=x
        s[1]+=y
        s[2]+=x*x
        s[3]+=y*y
        s[4]+=x*y
        count+=1
    ex,ey=F(s[0],count),F(s[1],count)
    return count,ex,ey,F(s[2],count)-ex*ex,F(s[3],count)-ey*ey,F(s[4],count)-ex*ey


def projection_integrals():
    a,b=S.symbols('a b', real=True)
    l=b-a
    pc=2*l*(1-l)
    pn=l**2+2*a*(1-b)
    def E(expr):
        return S.simplify(2*S.integrate(S.integrate(S.expand(expr),(b,a,1)),(a,0,1)))
    checks=[(pc,S.Rational(1,3)),(pn,S.Rational(1,3)),
            (pc**2,S.Rational(2,15)),(pn**2,S.Rational(2,15)),
            (pc*pn,S.Rational(1,9))]
    for expr,expect in checks:
        value=E(expr)
        assert value==expect,(value,expect)
    assert E((pc-S.Rational(1,3))*(pn-S.Rational(1,3)))==0
    assert E((pc-S.Rational(1,3))**2)==S.Rational(1,45)
    assert E((pn-S.Rational(1,3))**2)==S.Rational(1,45)
    return len(checks)+3


def run():
    tests=projection_integrals()
    for n in range(2,8):
        count,ex,ey,vx,vy,co=exact_moments(n)
        assert count==S.factorial2(2*n-1)
        assert ex==ey==F(n*(n-1),6)
        assert vx==vy==F(n*(n-1)*(n+3),45)
        assert co==-F(n*(n-1),18)
        assert F(co,vx)==-F(5,2*(n+3))
        tests+=5
        print(f'n={n}, matchings={count}: exact moments verified')
    for n in range(2,100):
        assert F(n*(n-1)*(n+3),45)==F(2*comb(n,2),9)+F(6*comb(n,3),45)
        assert F(n*(n-1)*(n+3),45)==F(n*(n-1)**2,45)+F(8*comb(n,2),45)
        tests+=2
    print(f'PASS: {tests} exact symbolic, exhaustive and algebraic assertions')

if __name__=='__main__':run()
