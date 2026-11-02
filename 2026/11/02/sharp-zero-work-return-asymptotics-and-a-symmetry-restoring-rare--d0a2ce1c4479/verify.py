#!/usr/bin/env python3
"""Independent finite-cycle dynamic-programming checks of a work-return asymptotic.

Run: python3 verify.py
Uses only Python's standard library. Finite diagnostics do not prove asymptotics.
"""
import math


def coefficients(p, q):
    a, c = 1-p*q, p*q
    b, d = 1-(1-p)*q, (1-p)*q
    A, B = math.sqrt(a*d), math.sqrt(b*c)
    L = A+B
    V = A/B
    S = math.sqrt(a*c/(b*d))
    rate = -math.log(L)
    phi = B/L
    return (a,b,c,d,L,V,S,rate,phi)


def return_probability(p, q, n):
    a,b,c,d,_,_,_,_,_ = coefficients(p,q)
    positive = {0:1.0}
    negative = {}
    for _ in range(n):
        pos2, neg2 = {}, {}
        for k,mass in positive.items():
            pos2[k+1] = pos2.get(k+1,0)+mass*a
            neg2[k-1] = neg2.get(k-1,0)+mass*c
        for k,mass in negative.items():
            pos2[k+1] = pos2.get(k+1,0)+mass*b
            neg2[k-1] = neg2.get(k-1,0)+mass*d
        positive,negative=pos2,neg2
    return positive.get(0,0)+negative.get(0,0)


def asymptotic(p,q,n):
    _,_,_,_,L,V,S,_,_=coefficients(p,q)
    return (1+S)*L**n/math.sqrt(2*math.pi*V*n)


def divergence(phi,a,b,c,d):
    return ((1-phi)*math.log((1-phi)/math.sqrt(a*d))
            +phi*math.log(phi/math.sqrt(b*c)))


def checks():
    assertions = 0
    for p,q in [(0.2,0.8),(0.33,0.5),(0.1,0.6),(0.45,0.95),(0.25,0.25)]:
        a,b,c,d,L,V,S,rate,phi=coefficients(p,q)
        assert abs(a+c-1)<1e-12 and abs(b+d-1)<1e-12
        assert all(x>0 for x in (a,b,c,d)) and L<1
        assert abs(divergence(phi,a,b,c,d)-rate)<1e-12
        assertions+=3
        for trial in (phi-0.05,phi+0.05):
            if 0<trial<1:
                assert divergence(trial,a,b,c,d)>rate
                assertions+=1
        exact=return_probability(p,q,800)
        approx=asymptotic(p,q,800)
        assert abs(exact/approx-1)<0.018, (p,q,exact/approx)
        assertions+=1
        assert return_probability(p,q,79)==0
        assertions+=1
    for p in [0.15,0.2,0.35,0.45]:
        eps=0.002
        L=coefficients(p,1-eps)[4]
        rate=coefficients(p,1-eps)[7]
        assert abs(rate/(eps*eps)-1/(8*p*(1-p)))<0.02
        assertions+=1
    for p,u,n in [(0.2,0.6,1200),(0.3,1.1,1200),(0.2,0,1200)]:
        q=1-u/math.sqrt(n)
        exact=return_probability(p,q,n)
        asym=math.sqrt(2*p/(math.pi*(1-p)*n))*math.exp(-u*u/(8*p*(1-p)))
        assert abs(exact/asym-1)<0.023,(p,u,n,exact/asym)
        assertions+=1
    print('PASS:',assertions,'analytic-identity and finite-cycle diagnostics')
    print('Representative (p=0.2,q=0.8,n=800) exact/asymptotic:',
          return_probability(.2,.8,800)/asymptotic(.2,.8,800))

if __name__=='__main__':
    checks()
