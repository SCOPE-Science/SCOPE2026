"""Exact finite checks for the two-clique irreversible fractional threshold theorem.
Standalone: Python 3 standard library only. No input files required.
This is a finite diagnostic, not a substitute for the general proof.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb

def threshold(phi, d):
    return (phi.numerator*d+phi.denominator-1)//phi.denominator

def polys(n,phi):
    r=threshold(phi,n-1); R=threshold(phi,n)
    U=Counter(); E=Counter()
    for x in range(n):
        if x>=r-1: U[x+1]+=comb(n-1,x)
        if R<n and x>=r: U[x]+=comb(n-1,x)
    if R==r: E[r-1]+=comb(n-1,r-1)
    elif R==n: E[n-1]+=1
    return U,E,r,R

def mul(A,B):
    r=Counter()
    for i,a in A.items():
        for j,b in B.items(): r[i+j]+=a*b
    return r

def polynomial(a,b,phi):
    UA,EA,ra,Ra=polys(a,phi)
    UB,EB,rb,Rb=polys(b,phi)
    p=mul(UA,UB)
    p.update(mul(UA,EB));p.update(mul(EA,UB))
    return +p

def direct(a,b,phi):
    n=a+b
    nbr=[set() for _ in range(n)]
    for s,t in [(0,a),(a,n)]:
        for i in range(s,t):
            for j in range(i+1,t):
                nbr[i].add(j);nbr[j].add(i)
    nbr[0].add(a);nbr[a].add(0)
    thresh=[threshold(phi,len(nb)) for nb in nbr]
    out=Counter()
    for bits in range(1<<n):
        active={i for i in range(n) if (bits>>i)&1}
        while True:
            new={i for i in range(n) if i not in active and sum(j in active for j in nbr[i])>=thresh[i]}
            if not new:break
            active|=new
        if len(active)==n:out[bits.bit_count()]+=1
    return +out

def disconnected(a,b,phi):
    A=Counter({k:comb(a,k) for k in range(threshold(phi,a-1),a+1)})
    B=Counter({k:comb(b,k) for k in range(threshold(phi,b-1),b+1)})
    return mul(A,B)

checks=0
phis=sorted({Fraction(i,j) for j in range(1,13) for i in range(1,j+1)})
for a in range(3,7):
  for b in range(3,7):
    for phi in phis:
      direct_poly=direct(a,b,phi)
      predicted=polynomial(a,b,phi)
      assert direct_poly==predicted,(a,b,phi,direct_poly,predicted)
      checks+=1
      ua,ea,ra,Ra=polys(a,phi);ub,eb,rb,Rb=polys(b,phi)
      disconnected_poly=disconnected(a,b,phi)
      delta=sum(predicted.values())-sum(disconnected_poly.values())
      if Ra==a and Rb==b:assert delta==-1,(a,b,phi,delta)
      elif Ra==ra or Rb==rb:assert delta>0,(a,b,phi,delta)
      else:assert delta==0,(a,b,phi,delta)
      checks+=1
      min_pred=min(predicted)
      expected=ra+rb-(1 if Ra==ra or Rb==rb else 0)
      assert min_pred==expected,(a,b,phi,min_pred,expected)
      checks+=1

# An explicit sample with gain: a=b=3, phi=1/3, r=1 R=1.
p=polynomial(3,3,Fraction(1,3));base=disconnected(3,3,Fraction(1,3))
assert p==Counter({1:6,2:15,3:20,4:15,5:6,6:1}),p
assert base==Counter({2:9,3:18,4:15,5:6,6:1}),base
checks+=2
# A loss: a=b=3, phi=1; one set of four non-gateways is lost.
p=polynomial(3,3,Fraction(1));base=disconnected(3,3,Fraction(1))
assert base[4]-p[4]==1 and sum(base.values())-sum(p.values())==1
checks+=1
print('PASS',checks,'finite exact assertions; rates',len(phis),'graph pairs 16')
