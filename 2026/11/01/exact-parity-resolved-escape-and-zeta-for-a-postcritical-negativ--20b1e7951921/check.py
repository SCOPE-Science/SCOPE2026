#!/usr/bin/env python3
"""Exact transfer, symbolic and periodic-point checks for the negative-doubling hole."""
from fractions import Fraction as Q
import sympy as s

A=s.Matrix([[0,0,0,0,1,1],
[0,0,1,1,0,0],
[0,1,0,0,0,0],
[0,0,0,0,1,0],
[0,0,1,1,0,0],
[1,1,0,0,0,0]])
I=[(Q(0),Q(1,6)),(Q(1,6),Q(1,3)),(Q(1,3),Q(5,12)),
   (Q(7,12),Q(2,3)),(Q(2,3),Q(5,6)),(Q(5,6),Q(1))]
for i,(l,r) in enumerate(I):
    yl,yr=(1-2*r,1-2*l) if i<=2 else (2-2*r,2-2*l)
    for j,(u,v) in enumerate(I):
        assert A[i,j]==int(yl<=u and v<=yr),(i,j,yl,yr)
lam=s.Symbol('lam');z=s.Symbol('z')
assert s.expand(A.charpoly(lam).as_expr()-lam**2*(lam-1)*(lam+1)*(lam**2-2))==0
ell=s.Matrix([[s.Rational(1,6),s.Rational(1,6),s.Rational(1,12),s.Rational(1,12),s.Rational(1,6),s.Rational(1,6)]])
V=s.ones(6,1)
G=s.factor((ell*(s.eye(6)-z*A.T/2).inv()*V)[0])
formula=(s.Rational(7,6)+s.Rational(5,6)*z)/(1-z*z/2)-(s.Rational(1,3)+z/6)/(1-z*z/4)
assert s.factor(G-formula)==0
for n in range(1,21):
    got=(ell*(A.T/2)**(n-1)*V)[0]
    if n%2:
        k=(n-1)//2
        expect=s.Rational(7,6)/2**k-s.Rational(1,3)/4**k
    else:
        k=n//2
        expect=s.Rational(5,3)/2**k-s.Rational(2,3)/4**k
    assert got==expect,(n,got,expect)

# Exact solve on each branch itinerary. Rational endpoints are treated as points,
# so a boundary-fixed point is deduplicated, unlike in a Markov graph trace.
def step(x):return Q(1)-2*x if x<Q(1,2) else Q(2)-2*x
for n in range(1,13):
    pts=set()
    for mask in range(1<<n):
        slope=Q(1); shift=Q(0)
        # At each step x_next=shift+slope*x; recover exact fixed-point candidate.
        branch=[]
        for k in range(n):
            bit=(mask>>k)&1
            shift=(Q(1)+bit)-2*shift
            slope=-2*slope
            branch.append(bit)
        if slope==1: continue
        x=shift/(1-slope)
        if not (0<=x<=1):continue
        cur=x;valid=True
        for k,bit in enumerate(branch):
            if (cur>=Q(1,2))!=bool(bit) or Q(5,12)<cur<Q(7,12):
                valid=False;break
            cur=step(cur)
        if valid and cur==x:pts.add(x)
    expected=2 if n%2 else 2**(n//2+1)
    assert len(pts)==expected,(n,len(pts),expected)
    trace=s.trace(A**n)
    assert trace==(0 if n%2 else expected+2)
print('PASS: exact interval images, polynomial, survival generating function, steps 1-20, periodic-point counts 1-12')
