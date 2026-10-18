#!/usr/bin/env python3
"""Exact-rational checks for the explicit odd-dimensional capsule Mahler profile."""
from fractions import Fraction as Q
from math import comb, factorial

def polyadd(x,y):
    out=[Q(0)]*max(len(x),len(y))
    for i,v in enumerate(x): out[i]+=v
    for i,v in enumerate(y): out[i]+=v
    return out

def polymul(x,y):
    out=[Q(0)]*(len(x)+len(y)-1)
    for i,v in enumerate(x):
        for j,w in enumerate(y): out[i+j]+=v*w
    return out

def polynomial(m):
    beta=Q((2*m+1)*comb(2*m,m),4**m)
    j=[Q(0)]*(m+1)
    for k in range(m+1):
        weight=Q(comb(m,k)*factorial(k)*factorial(m),factorial(m+k+1))
        factor=[Q(comb(k,h)*(-2)**h) for h in range(k+1)]
        j=polyadd(j,[weight*v for v in factor])
    p=polymul([beta,beta*(beta-1)],j)
    return p,beta

def ev(p,x):
    y=Q(0)
    for v in reversed(p): y=y*x+v
    return y

def deriv(p): return [i*v for i,v in enumerate(p)][1:]

def independent_integral(m,a,beta):
    # q(z) = 1 - 2 a z + (a*a-1) z*z, integrated to 1/(1+a).
    q=[Q(1),-2*a,a*a-1]
    powq=[Q(1)]
    for _ in range(m): powq=polymul(powq,q)
    end=1/(1+a)
    integ=sum(v*end**(i+1)/(i+1) for i,v in enumerate(powq))
    return (1+beta*a)*beta*integ

def main():
    for m in range(1,11):
        p,beta=polynomial(m);d=2*m+1
        assert len(p)==m+2 and ev(p,Q(0))==1
        assert ev(deriv(p),Q(0))==0
        assert ev(p,Q(1))==beta*beta/d
        assert ev(deriv(p),Q(1))==-beta/d
        assert ev(deriv(deriv(p)),Q(0))==-2*(beta*beta-(m+1))<0
        assert ev(deriv(deriv(p)),Q(1))==Q(2)*beta/d*(1-beta/Q(2*m-1))
        if m>=2: assert ev(deriv(deriv(p)),Q(1))>0
        else: assert p==[Q(1),Q(0),Q(-1,4)]
        for a in [Q(0),Q(1,3),Q(1),Q(7,4)]:
            b=a/(1+a)
            assert ev(p,b)==independent_integral(m,a,beta)
    print('PASS: 10 dimensions, exact coefficients, endpoint laws, and 40 independent integrals')
if __name__=='__main__': main()
