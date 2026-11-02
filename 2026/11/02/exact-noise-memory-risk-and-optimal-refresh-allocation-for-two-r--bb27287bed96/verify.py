#!/usr/bin/env python3
"""Exact arithmetic checks for the two-row refreshed-observation Kaczmarz risk law.

Only Python's standard library is used. Finite algebraic tests supplement the proof.
"""
from fractions import Fraction as F
from itertools import product

M = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2),(0,0,0)]

def plus(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def times(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            k=tuple(i[q]+j[q] for q in range(3))
            assert sum(k)<=2
            out[k]=out.get(k,F(0))+x*y
    return {k:v for k,v in out.items() if v}

def scale(a,z):return {k:v*z for k,v in a.items() if v*z}

def atom(k):return {k:F(1)}

def transfer(c,s,r1,r2,sigma1,sigma2):
    t,z1,z2=atom((1,0,0)),atom((0,1,0)),atom((0,0,1))
    u=c*c
    out={mon:{} for mon in M}
    for b1,b2 in product((0,1),repeat=2):
        pr=(r1 if b1 else 1-r1)*(r2 if b2 else 1-r2)
        for e1,e2 in product((-1,1),repeat=2):
            p=pr/F(4)
            zz1=atom((0,0,0)) if b1 else z1
            if b1: zz1=scale(zz1,F(e1*sigma1))
            zz2=atom((0,0,0)) if b2 else z2
            if b2: zz2=scale(zz2,F(e2*sigma2))
            tt=plus(plus(scale(t,u),scale(z2,c*s)),scale(zz1,-s))
            for mon in M:
                a=atom((0,0,0))
                for q in range(mon[0]):a=times(a,tt)
                for q in range(mon[1]):a=times(a,zz1)
                for q in range(mon[2]):a=times(a,zz2)
                out[mon]=plus(out[mon],scale(a,p))
    return out

def predict(c,s,r1,r2,sigma1,sigma2):
    u=c*c; a1=1-r1; a2=1-r2
    v1=F(sigma1*sigma1);v2=F(sigma2*sigma2)
    d1=1-a1*u;d2=1-a2*u
    v=v2+(v1*(1+a1*u)/d1+u*v2*(1+a2*u)/d2)/(1+u)
    q1=-s*v1/d1
    q2=c*s*a2*v2/d2
    return {M[0]:v-v2, M[1]:q1, M[2]:q2,M[3]:v1,M[4]:F(0),M[5]:v2,M[6]:F(1)}

def risk(c,r1,r2,v1,v2):
    u=c*c
    return v2+(v1*(1+u*(1-r1))/(1-u*(1-r1)) + u*v2*(1+u*(1-r2))/(1-u*(1-r2)))/(1+u)

def opt(c,b,sigma1,sigma2):
    u=c*c; a=1-u
    lo=max(F(0),b-1);hi=min(F(1),b)
    d=(2*a+u*b)*sigma1/(sigma1+c*sigma2)
    raw=(d-a)/u
    r1=max(lo,min(hi,raw))
    return r1,b-r1

def main():
    n=0
    # Random-refresh and noise scale cases checked against *independently enumerated*
    # conditional second-moment polynomial transitions.
    for c,s in ((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(12,13),F(5,13)),(F(8,17),F(15,17)),(F(0),F(1))):
        for r1,r2 in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=2):
            for si1,si2 in ((1,1),(2,1),(1,3)):
                op=transfer(c,s,r1,r2,si1,si2)
                stationary=predict(c,s,r1,r2,si1,si2)
                for mon,polynomial in op.items():
                    actual=sum((coeff*stationary[key] for key,coeff in polynomial.items()),F(0))
                    assert actual==stationary[mon],(c,s,r1,r2,si1,si2,mon,actual,stationary[mon])
                    n+=1
    for c,s in ((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(12,13),F(5,13)),(F(8,17),F(15,17))):
        for b in (F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(7,4)):
            for si1,si2 in ((1,1),(1,3),(2,1)):
                a,b2=opt(c,b,F(si1),F(si2))
                v1=F(si1*si1);v2=F(si2*si2)
                value=risk(c,a,b2,v1,v2)
                low=max(F(0),b-1);high=min(F(1),b)
                for j in range(65):
                    x=low+(high-low)*F(j,64)
                    assert value<=risk(c,x,b-x,v1,v2),(c,b,si1,si2,x,a,b2)
                    n+=1
    for c in (F(3,5),F(5,13),F(12,13)):
        u=c*c
        for r in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            assert risk(c,r,r,F(1),F(1))==2/(1-(1-r)*u)
            n+=1
    print('VERIFICATION_OK',n,'exact rational assertions')

if __name__=='__main__':main()
