#!/usr/bin/env python3
"""Exact rational checks for triple-sinc Fourier radial densities.

These tests do not replace the analytic proof in RESULT.md.
Run with: python3 triple_sinc_checker.py
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def slopes(a,b,c):
    a,b,c = map(Q,(a,b,c)); L=abs(a-b); U=a+b; R=U+c
    knots={Q(0),c,L+c,U+c,abs(L-c),abs(U-c),R}
    xs=sorted(x for x in knots if 0<=x<=R)
    def H(r):return max(Q(0),min(U,r+c)-max(L,abs(r-c)))
    pieces=[]
    for lo,hi in zip(xs,xs[1:]):
        if lo==hi:continue
        flo,fhi=H(lo),H(hi)
        alpha=(fhi-flo)/(hi-lo);beta=flo-alpha*lo
        mid=(lo+hi)/2
        assert H(mid)==alpha*mid+beta,(a,b,c,lo,hi,H(mid),alpha,beta)
        pieces.append((lo,hi,alpha,beta))
    return pieces


def moments3(a,b,c,pieces,k):
    return sum((al*(hi**(2*k+3)-lo**(2*k+3))/(2*k+3)
                +be*(hi**(2*k+2)-lo**(2*k+2))/(2*k+2))
               for lo,hi,al,be in pieces)/(4*a*b*c)


def moments5(a,b,c,pieces,k):
    return sum(be*(hi**(2*k+2)-lo**(2*k+2))/(2*k+2)
               for lo,hi,al,be in pieces)/(12*a*b*c)


def product_sinc_coeff(a,b,c,k):
    return sum(a**(2*i)*b**(2*j)*c**(2*h)
               /Q(factorial(2*i+1)*factorial(2*j+1)*factorial(2*h+1))
               for i in range(k+1) for j in range(k+1-i)
               for h in [k-i-j])


def verify(a,b,c):
    a,b,c=map(Q,(a,b,c))
    pieces=slopes(a,b,c)
    triangle=max(a,b,c)<=a+b+c-max(a,b,c)
    for k in range(7):
        coeff=product_sinc_coeff(a,b,c,k)
        assert moments3(a,b,c,pieces,k)==coeff*factorial(2*k+1)
        assert moments5(a,b,c,pieces,k)==coeff*Q(factorial(2*k+3),6*(k+1))
    assert moments3(a,b,c,pieces,0)==1
    assert moments5(a,b,c,pieces,0)==1
    if triangle:
        assert all(beta>=0 for lo,hi,alpha,beta in pieces)
        assert any(beta>0 for lo,hi,alpha,beta in pieces)
        assert pieces[0][3]==0 # spectral hole in the five-dimensional density
    else:
        assert any(beta<0 for lo,hi,alpha,beta in pieces)
        assert any(lo==0 and alpha==0 and beta==0 for lo,hi,alpha,beta in pieces)
    return triangle,len(pieces)


def main():
    tests=[(1,1,1),(1,2,2),(1,1,2),(1,1,3),(1,1,Q(1,10)),
           (2,3,4),(1,2,3),(2,3,6),(3,4,5),(2,3,3),
           (3,3,1),(3,5,8),(3,5,9),(3,4,Q(7,2))]
    for a,b,c in tests:
        print(f'{a},{b},{c}: triangle={verify(a,b,c)[0]}, pieces={verify(a,b,c)[1]}')
    print(f'PASS: {len(tests)} exact rational cases; 7 Taylor moments for each of the 3D and 5D spectral measures; normalization; signed-density boundaries.')

if __name__=='__main__':main()
