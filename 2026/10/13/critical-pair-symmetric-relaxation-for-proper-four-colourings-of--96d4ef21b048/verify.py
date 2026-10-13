#!/usr/bin/env python3
from fractions import Fraction
from math import comb

# Polynomials are low-to-high coefficient lists over exact integers/Fractions.
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return trim(out)

def mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def scale(a,c): return trim([c*x for x in a])

def shift_one(poly):
    # p(1+u)
    out=[Fraction(0) for _ in range(len(poly))]
    for k,ck in enumerate(poly):
        for j in range(k+1): out[j]+=ck*comb(k,j)
    return trim(out)

def series_div(n,d,N):
    q=[Fraction(0) for _ in range(N)]
    for k in range(N):
        s=n[k] if k < len(n) else Fraction(0)
        for j in range(1,min(k+1,len(d))): s-=d[j]*q[k-j]
        q[k]=s/d[0]
    return q

# g(r) = N(r)/D(r)
N=[0]*10; D=[0]*10
N[0]=10; N[3]=24; N[6]=30; N[9]=17
D[0]=17; D[3]=30; D[6]=24; D[9]=10
N=list(map(Fraction,N)); D=list(map(Fraction,D))
# Numerator of g-r.
rD=[Fraction(0)]+D
lhs=add(N, scale(rD,Fraction(-1)))
# -(r-1)^3(r+1)(2r^2-r+2)(5r^4+4r^3+4r+5)
rminus=[Fraction(-1),Fraction(1)]
rplus=[Fraction(1),Fraction(1)]
quad=[Fraction(2),Fraction(-1),Fraction(2)]
quart=[Fraction(5),Fraction(4),Fraction(0),Fraction(4),Fraction(5)]
rhs=scale(mul(mul(mul(mul(rminus,rminus),rminus),rplus),mul(quad,quart)),Fraction(-1))
assert trim(lhs)==trim(rhs), (lhs,rhs)
# Taylor series g(1+u) through cubic order.
Ns=shift_one(N); Ds=shift_one(D)
q=series_div(Ns,Ds,5)
assert q[0]==1 and q[1]==1 and q[2]==0 and q[3]==Fraction(-4,3), q
print('VERIFY_OK cubic=-4/3 displacement_factorization=exact')
