#!/usr/bin/env python3
"""Exact small-case checks for a cyclic Fourier--Sobolev coefficient formula.

Requires only the Python standard library; finite checks are not a proof
of the all-order circle rearrangement step.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import sin,pi,sqrt

def green(n):
    return [Q(n*n-1,12*n)-Q(r*(n-r),2*n) for r in range(n)]

def formula(n):
    return (Q(n*(n*n+8),48) if n%2==0
            else Q((n*n-1)*(n*n+7),48*n))

def energy(n,g,selected):
    return 4*sum((g[(i-j)%n] for i in selected for j in selected),Q(0))

def block_value(n,m):
    return Q(m*(n-m)*(m*(n-m)+2),3*n)

def check():
    greens=0
    cells=0
    blocks=0
    signs=0
    profiles=0
    for n in range(3,61):
        g=green(n)
        assert sum(g)==0
        for r in range(n):
            delta=2*g[r]-g[(r-1)%n]-g[(r+1)%n]
            assert delta==Q(int(r==0),1)-Q(1,n)
            greens+=1
        h0=Q(n,12)-(Q(n,3)-Q(1,6))/Q(2*n)
        assert h0==g[0]-Q(n-1,6*n)
        cells+=1
        for r in range(1,n):
            hr=Q(n,12)-(r*(n-r)-Q(1,6))/Q(2*n)
            assert hr==g[r]+Q(1,6*n)
            cells+=1
        for m in range(1,n):
            assert energy(n,g,range(m))==block_value(n,m)
            blocks+=1
        m=n//2
        sig=[1 if j<m else -1 for j in range(n)]
        a=[sum((g[(j-k)%n]*sig[k] for k in range(n)),Q(0)) for j in range(n)]
        assert sum(a)==0
        grad=sum(((a[(j+1)%n]-a[j])**2 for j in range(n)),Q(0))
        l1=sum((abs(v) for v in a),Q(0))
        assert grad==formula(n) and l1*l1==formula(n)*grad
        profiles+=1
    for n in range(3,14):
        g=green(n)
        best=Q(-1)
        for mask in range(1,1<<n):
            chosen=[i for i in range(n) if mask>>i&1]
            e=energy(n,g,chosen)
            if e>best:best=e
            signs+=1
        assert best==formula(n)
    for n in range(3,300):
        complex_lambda=n/(4*sin(pi/n)**2)
        real_lambda=float(formula(n))
        assert real_lambda<=complex_lambda*(1+1e-12)
        if n!=4:
            assert real_lambda<complex_lambda-1e-9
    assert abs(pi/sqrt(12)-0.9068996821)<1e-9
    print(f'VERIFY_OK {greens} exact Green identities; {cells} unit-cell integration identities; {blocks} exact block energies; '
          f'{signs} exhaustive sign vectors; {profiles} exact extremal profiles; '
          '297 spectral comparisons')

if __name__=='__main__':check()
