#!/usr/bin/env python3
"""Exact finite-word validation for two Markov-switched binary holes."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

def mm(v,M):
    return [sum(v[i]*M[i][j] for i in range(len(v))) for j in range(len(M[0]))]

def transfer(p,n):
    A=[[F(1,2),F(1,2)],[p/2,(1-p)/2]]
    B=[[F(1,4),F(1,2),F(1,4)],[p/4,F(1,4),(1-p)/4],[p/4,F(0),(1-p)/4]]
    u=[F(1,2),F(1,2)]; v=[F(1,4),F(1,2),F(1,4)]
    for _ in range(n):
        u=mm(u,A);v=mm(v,B)
    return sum(u),sum(v)

def brute(p,n):
    first=second=F(0)
    for ee in product((0,1),repeat=n):
        w=F(1,2)
        for j in range(1,n):w*=p if ee[j]==ee[j-1] else 1-p
        survive=0
        for bits in product((0,1),repeat=n+1):
            if all(not (bits[j]==bits[j+1]==ee[j]) for j in range(n)):
                survive+=1
        q=F(survive,2**(n+1))
        first+=w*q;second+=w*q*q
    return first,second

def main():
    count=0
    for p in [F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]:
        for n in range(1,8):
            x,y=transfer(p,n)
            z,t=brute(p,n)
            assert (x,y)==(z,t),(p,n,x,y,z,t)
            if p==0: assert x==F(n+2,2**(n+1)) and y==x*x
            if p==1:assert y==x*x
            if p==F(1,2):assert x==F(3,4)**n
            count+=1
    from math import sqrt
    for i in range(1,1000):
        p=i/1000
        q=(2-p+sqrt(p*(p+4)))/4
        polynomial=lambda s:64*s**3+(16*p-48)*s*s+(12-20*p)*s+2*p-1
        ident=4*p*(p-1)*q*(q-1)*(4*q*q-3)
        assert abs(polynomial(q*q)-ident)<2e-13
        assert ident<0
    print(f'VERIFY_OK: {count} exact independent first/second survival moments; 999 positive spectral-gap witnesses')
if __name__=='__main__':main()
