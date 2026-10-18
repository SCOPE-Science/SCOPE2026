#!/usr/bin/env python3
"""Reproduce exact identities and finite sanity checks for scaled Cauchy quadrature."""
import math
import sympy as sp
import mpmath as mp


def transformed_mass(a, c, n):
    """Direct, continuously extended transformed rule at all n circle nodes."""
    z = mp.mpf('0')
    for j in range(1, n + 1):
        t = mp.pi*j/n
        den = a*a*(mp.sin(t)**2) + c*c*(mp.cos(t)**2)
        z += a*c/den/n
    return z


def alias_mass(a, c, n):
    q = (a-c)/(a+c)
    return (1 + q**n)/(1 - q**n)


def mass_mixture(scales, weights, c, n):
    return sum(w*alias_mass(a, c, n) for a,w in zip(scales, weights))


def verify():
    mp.mp.dps=90
    counts = {'direct_circle_matches':0,'convexity_identities':0,
              'parity_classifications':0,'two_scale_extrema':0,
              'asymptotic_ratios':0}
    for a in [mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf('0.5')]:
        for c in [mp.mpf('0.6'),mp.mpf(1),mp.mpf('1.5'),mp.mpf(3),mp.mpf(6)]:
            for n in range(1,10):
                assert abs(transformed_mass(a,c,n)-alias_mass(a,c,n)) < mp.mpf('1e-75')
                counts['direct_circle_matches']+=1
    u=sp.symbols('u', real=True)
    for n in range(2,22,2):
        Fn=(1+u**n)/(1-u**n)
        derivative=lambda f: sp.diff(f,u)*(1-u*u)/2
        N=(n-1)-(n+1)*u**2+(n+1)*u**n-(n-1)*u**(n+2)
        d2=n*sp.Rational(1,2)*u**(n-2)*(1-u*u)*N/(1-u**n)**3
        assert sp.simplify(derivative(derivative(Fn))-d2)==0
        m=n//2
        bracket=(2*m-1)*(1+u**(2*m))-2*sum((u**(2*j) for j in range(1,m)),sp.Integer(0))
        assert sp.expand(N-(1-u*u)*bracket)==0
        counts['convexity_identities']+=2
    scales=[mp.mpf(1),mp.mpf(2),mp.mpf(6)]
    weights=[mp.mpf('0.2'),mp.mpf('0.3'),mp.mpf('0.5')]
    for n in range(1,12,2):
        f=lambda s:mass_mixture(scales,weights,mp.exp(s),n)-1
        root=mp.findroot(f,(mp.log(1),mp.log(6)),solver='bisect') if False else mp.findroot(f,(mp.log(1),mp.log(6)))
        assert mp.log(1)-mp.mpf('1e-40')<root<mp.log(6)+mp.mpf('1e-40')
        assert abs(f(root))<mp.mpf('1e-60')
        for ds in [mp.mpf('0.001'),mp.mpf('0.05'),mp.mpf('0.2')]:
            assert f(root-ds)>0 and f(root+ds)<0
            counts['parity_classifications']+=1
    for n in range(2,12,2):
        for c in [mp.mpf('0.5'),mp.mpf(1),mp.mpf(2),mp.mpf(3),mp.mpf(10)]:
            assert mass_mixture(scales,weights,c,n)>=1
            counts['parity_classifications']+=1
    a,b=mp.mpf(1),mp.mpf(4); g=mp.sqrt(a*b)
    r=(mp.sqrt(b)-mp.sqrt(a))/(mp.sqrt(b)+mp.sqrt(a))
    for n in [2,4,6,8,10,12,16]:
        exact=2*r**n/(1-r**n)
        assert abs(mass_mixture([a,b],[mp.mpf('.5')]*2,g,n)-1-exact)<mp.mpf('1e-70')
        for c in [mp.mpf('.4'),mp.mpf('1.4'),mp.mpf('3'),mp.mpf(8)]:
            assert mass_mixture([a,b],[mp.mpf('.5')]*2,c,n)>=1+exact
            counts['two_scale_extrema']+=1
    for n in [3,5,7,9,11,15]:
        f=lambda s:mass_mixture([a,b],[mp.mpf('.5')]*2,g*mp.exp(s),n)-1
        z=2*r**(n+1)/(n*(1-r*r))
        root=mp.findroot(f,(z*mp.mpf('.8'),z*mp.mpf('1.2')))
        assert root>0 and abs(f(root))<mp.mpf('1e-70')
        assert abs(root/z-1)<mp.mpf('.001')
        counts['asymptotic_ratios']+=1
    print('VERIFIED',counts,'TOTAL',sum(counts.values()))

if __name__=='__main__':
    verify()
