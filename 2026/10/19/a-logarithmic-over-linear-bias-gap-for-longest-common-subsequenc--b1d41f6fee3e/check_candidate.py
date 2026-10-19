#!/usr/bin/env python3
"""Finite independent tests for the geometric-word bound; no asymptotic proof claims."""
from itertools import product
from fractions import Fraction
from math import exp,log,log1p,expm1

def is_subseq(w,x):
 j=0
 for a in x:
  if j<len(w) and a==w[j]:j+=1
 return j==len(w)

def enumerate_embedding_prob(p,n,w):
 q=len(p); total=Fraction(0,1)
 for x in product(range(q),repeat=n):
  if is_subseq(w,x):
   prob=Fraction(1,1)
   for a in x:prob*=p[a]
   total+=prob
 return total

def rate(p,d):
 p=sorted(p,reverse=True); gap=1/p[1]-1/p[0]
 t=log(d)/(d*gap)
 L=[log1p(expm1(t)/a) for a in p]
 a=max([-d*u for u in L]); lsum=a+log(sum(exp(-d*u-a) for u in L))
 return (-d*t/lsum),t

p=(Fraction(7,10),Fraction(3,10))
for n in range(1,7):
 for m in range(1,min(n,4)+1):
  for w in product((0,1),repeat=m):
   exact=enumerate_embedding_prob(p,n,w)
   for t in (0.03,0.2,0.7):
    rhs=exp(t*n)
    for a in w:
     rhs*=float(p[a])/(float(p[a])+expm1(t))
    assert float(exact)<=rhs+1e-12,(n,m,w,float(exact),rhs)
print('PASS: all binary target words up to length 4 against all source strings of lengths 1..6; three Laplace parameters')

for law in [(0.7,0.3),(0.7,0.2,0.1),(0.55,0.3,0.15)]:
 gap=1/law[1]-1/law[0]
 coeff=(1-law[0])/(2*gap)
 vals=[]
 for d in (500,5000,50000,500000):
  r,t=rate(law,d)
  assert r>=law[0]
  vals.append(round((r-law[0])*d/log(d),8))
 print('law',law,'theorem coefficient',round(coeff,8),'scaled rigorous bounds',vals)
 assert abs(vals[-1]-coeff)<.05
print('PASS: finite-rate expressions and asymptotic expansion corroborated')

# Independent brute-force LCS-event verification against the full union bound.
def lcs_length(x,y):
 prev=[0]*(len(y)+1)
 for a in x:
  cur=[0]*(len(y)+1)
  for j,b in enumerate(y,1):
   cur[j]=prev[j-1]+1 if a==b else max(prev[j],cur[j-1])
  prev=cur
 return prev[-1]

law=(Fraction(7,10),Fraction(3,10)); t=0.16
for n in range(2,6):
 weighted=[]
 for s in product(range(2),repeat=n):
  v=Fraction(1)
  for a in s:v*=law[a]
  weighted.append((s,v))
 S=sum((float(p)/(float(p)+expm1(t)))**2 for p in law)
 for ell in range(1,n+1):
  exact=Fraction(0)
  for x,px in weighted:
   for y,py in weighted:
    if lcs_length(x,y)>=ell:exact+=px*py
  bound=exp(2*t*n)*S**ell
  assert float(exact)<=bound+1e-12,(n,ell,exact,bound)
print('PASS: complete two-string LCS-event enumeration for lengths 2..5 and every threshold')
