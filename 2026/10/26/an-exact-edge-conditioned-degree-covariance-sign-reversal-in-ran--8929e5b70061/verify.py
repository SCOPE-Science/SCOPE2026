#!/usr/bin/env python3
"""Exact finite-subdiagram certificates for degree dependence in random chord diagrams."""
from fractions import Fraction as F
from itertools import combinations

def double_words(m):
    words = [()]
    for label in range(m):
        out=[]
        for w in words:
            for i,j in combinations(range(len(w)+2),2):
                v=list(w); v.insert(i,label);v.insert(j,label)
                out.append(tuple(v))
        words=out
    return words

def crossing(w,a,b):
    ia=[i for i,t in enumerate(w) if t==a]
    ib=[i for i,t in enumerate(w) if t==b]
    return (ia[0]<ib[0]<ia[1]<ib[1]) or (ib[0]<ia[0]<ib[1]<ia[1])

ws3=double_words(3)
assert len(ws3)==90 and len(set(ws3))==90
ws4=double_words(4)
assert len(ws4)==2520 and len(set(ws4))==2520
for e,den3,den4,q,r,s in [(0,60,1680,F(3,10),F(1,10),F(3,35)),(1,30,840,F(2,5),F(1,5),F(17,105))]:
    b3=[w for w in ws3 if crossing(w,0,1)==bool(e)]
    b4=[w for w in ws4 if crossing(w,0,1)==bool(e)]
    assert len(b3)==den3 and len(b4)==den4
    assert F(sum(crossing(w,0,2) for w in b3),den3)==q
    assert F(sum(crossing(w,0,2) and crossing(w,1,2) for w in b3),den3)==r
    assert F(sum(crossing(w,0,2) and crossing(w,1,3) for w in b4),den4)==s
    for n in range(2,301):
        k=n-2
        c=k*(r-q*q)+k*(k-1)*(s-q*q)
        closed=k*(F(16-3*n,700) if e==0 else F(n+18,525))
        assert c==closed
print('VERIFY_OK: 90 three-chord words, 2520 four-chord words; exact event counts and 598 conditional covariance algebra checks')

# Separate direct full-matching enumeration for n = 2,3,4,5,6.

def mats(v):
 if not v: yield ()
 else:
  a=v[0]
  for idx in range(1,len(v)):
   b=v[idx]
   for rest in mats(v[1:idx]+v[idx+1:]):yield ((a,b),)+rest

def crosses(a,b):
 (p,q),(r,s)=a,b
 return (p<r<q<s) or (r<p<s<q)
for n in range(2,7):
 nums=[0,0];s1=[0,0];s2=[0,0];s12=[0,0]
 count=0
 for m in mats(tuple(range(2*n))):
  count+=1
  adj=[[int(crosses(m[i],m[j])) for j in range(n)] for i in range(n)]
  deg=[sum(q) for q in adj]
  for i in range(n):
   for j in range(n):
    if i==j:continue
    e=adj[i][j];nums[e]+=1;s1[e]+=deg[i];s2[e]+=deg[j];s12[e]+=deg[i]*deg[j]
 for e in (0,1):
  c=F(s12[e],nums[e])-F(s1[e],nums[e])*F(s2[e],nums[e])
  expected=F((n-2)*(16-3*n),700) if not e else F((n-2)*(n+18),525)
  assert c==expected,(n,e,c,expected)
 assert count in (3,15,105,945,10395)
print('VERIFY_MATCHINGS_OK: 3+15+105+945+10395 complete matchings; both conditional covariance formulas')
