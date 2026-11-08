#!/usr/bin/env python3
"""Exact rational polynomial integration for the two-marker Abelian-square limit."""
from fractions import Fraction as F


def plus(a,b):
    o=dict(a)
    for k,v in b.items():o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}

def scale(a,c):return {k:v*c for k,v in a.items() if v*c}

def times(a,b):
    o={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():o[i+k,j+l]=o.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in o.items() if v}

def sq(a):return times(a,a)

ONE={(0,0):F(1)};X={(1,0):F(1)};Z={(0,1):F(1)}
Q0=times(X,Z)
Q1=plus(Q0,scale(sq(plus(plus(X,scale(Z,2)),scale(ONE,-1))),F(-1,2)))
Q2=plus(Q1,scale(sq(plus(plus(scale(X,2),Z),scale(ONE,-1))),F(-1,2)))
H=scale(sq(plus(scale(Z,2),scale(ONE,-1))),F(1,2))

def uadd(a,b):
    o=dict(a)
    for k,v in b.items():o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}

def uscale(a,c):return {k:v*c for k,v in a.items() if v*c}

def umul(a,b):
    o={}
    for k,v in a.items():
        for l,w in b.items():o[k+l]=o.get(k+l,F(0))+v*w
    return {k:v for k,v in o.items() if v}

def upow(a,k):
    t={0:F(1)}
    for _ in range(k):t=umul(t,a)
    return t

ZERO={};UNIT={0:F(1)};UZ={1:F(1)}
def sub(a,b):return uadd(a,uscale(b,-1))


def integrate(poly, zlo,zhi,xlo,xhi):
    u={}
    for (i,j),v in poly.items():
        d=sub(upow(xhi,i+1),upow(xlo,i+1))
        for k,c in d.items():
            u[j+k]=u.get(j+k,F(0))+v*c/F(i+1)
    return sum((c*(zhi**(k+1)-zlo**(k+1))/F(k+1) for k,c in u.items()),F(0))

R=F(1,3);T=F(1,2)
segments=[
 (F(0),R,ZERO,UZ,Q0),
 (R,T,ZERO,sub(UNIT,uscale(UZ,2)),Q0),
 (R,T,sub(UNIT,uscale(UZ,2)),uscale(sub(UNIT,UZ),F(1,2)),Q1),
 (R,T,uscale(sub(UNIT,UZ),F(1,2)),UZ,Q2),
 (T,F(1),ZERO,uscale(sub(UNIT,UZ),F(1,2)),plus(Q1,H)),
 (T,F(1),uscale(sub(UNIT,UZ),F(1,2)),sub(UNIT,UZ),plus(Q2,H))
]

def main():
    totals=[]
    for exponent in (0,1,2):
        terms=[integrate(ONE if exponent==0 else poly if exponent==1 else sq(poly),zl,zh,xl,xh)
               for zl,zh,xl,xh,poly in segments]
        total=4*sum(terms,F(0))
        totals.append(total)
        print('exponent',exponent,'half-simplex integrals',terms,'probability moment',total)
    assert totals==[F(1),F(1,24),F(5,1728)]
    mean=totals[1]/2
    variance=(totals[2]-totals[1]**2)/4
    assert mean==F(1,48) and variance==F(1,3456)
    print('MOMENT_VERIFY_OK',mean,variance)

if __name__=='__main__':main()
