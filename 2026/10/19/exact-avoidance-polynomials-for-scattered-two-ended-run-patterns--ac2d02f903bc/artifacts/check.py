#!/usr/bin/env python3
"""Reproducible finite tests for bounded-interior scattered-pattern avoidance."""
from itertools import combinations
from collections import defaultdict
from math import comb

def gauss_direct(n,k):
 out=[0]*(k*(n-k)+1)
 for a in combinations(range(n),k):
  c=sum(sum(j>i and j not in a for j in range(n)) for i in a)
  out[c]+=1
 return out

def composition_gaussian(a,k):
 # h_k(z,...,z^(a-1)), direct weak-composition DP
 dp={(0,0):1}
 for i in range(1,a):
  nxt=defaultdict(int)
  for (used,c),ways in dp.items():
   for x in range(k-used+1):nxt[(used+x,c+i*x)]+=ways
  dp=nxt
 out=[0]*(k*(a-1)+1)
 for (used,c),ways in dp.items():
  if used==k:out[c]+=ways
 return out

def avoid_gen(a,b,r):
 out=[0]*(a*b+1)
 if a<2:return gauss_direct(a+b,a)
 for k in range(min(b,r-1)+1):
  coeff=composition_gaussian(a,k)
  for e in range(b-k+1):
   for d,v in enumerate(coeff):out[a*e+d]+=v
 return out

def avoid_direct(a,b,r):
 out=[0]*(a*b+1)
 for aa in combinations(range(a+b),a):
  w=['b']*(a+b)
  for i in aa:w[i]='a'
  c=sum(w[i]=='a' and w[j]=='b' for i in range(a+b) for j in range(i+1,a+b))
  if a<=1 or sum(ch=='b' for ch in w[aa[0]+1:aa[-1]])<r:out[c]+=1
 return out

def main():
 cases=0;words=0
 for a in range(2,8):
  for b in range(0,8):
   for r in range(1,b+3):
    model=avoid_gen(a,b,r); direct=avoid_direct(a,b,r)
    assert model==direct,(a,b,r,model,direct)
    assert model==model[::-1],('palindromicity',a,b,r)
    if r==2:assert model==[1]*(a*b+1)
    if r>b:assert model==gauss_direct(a+b,a)
    words+=comb(a+b,a)
    cases+=1
 for b in range(3,20):
  r=3
  v=[sum(1 for k in range(min(2,b,c,2*b-c)+1) if k%2==c%2) for c in range(2*b+1)]
  assert v==[1,1]+sum(([2,1] for _ in range(b-2)),[])+[2,1,1]
 for b in range(2,28):
  for r in range(2,b+1):
   v=[sum(1 for k in range(min(r-1,b,c,2*b-c)+1) if k%2==c%2) for c in range(2*b+1)]
   assert v==avoid_gen(2,b,r)
 print('PASS: exact generating coefficients vs direct word enumeration:',cases,'parameter cases; total per-case word examinations:',words)
 print('PASS: palindromicity, flat r=2, Gaussian r>B, and A=2 coefficient formula')
 print('PASS: non-unimodal r=3, B>=3 explicit alternating profile verified through B=19')
 print('Example A=2, B=5, r=3:',avoid_gen(2,5,3))
 print('Example A=4, B=5, r=3:',avoid_gen(4,5,3))
if __name__=='__main__':main()
