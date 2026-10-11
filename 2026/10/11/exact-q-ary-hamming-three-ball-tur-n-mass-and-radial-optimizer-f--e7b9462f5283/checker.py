"""Exact reproducibility checks for the radius-three q-ary Hamming Turan theorem.
Uses only Python's standard library; run python radius3_checker.py.
"""
from fractions import Fraction as F
from math import comb
from itertools import product

checks=0
for q in [2,3,4,5,7,8,9,11,13]:
 p=F(q-1,q)
 for d in range(3,36):
  n=(d-1)*(q-1)
  r=n//q
  theta=F(n%q,q)
  assert 1 <= r <= d-2
  prob=[F(comb(d,t)*(q-1)**t,q**d) for t in range(d+1)]
  poly=lambda t:(d-t)*(t-r)*(t-r-1)
  avg=sum(prob[t]*poly(t) for t in range(d+1))
  predicted=d*(1-p)*((d-1)*p*(1-p)-theta*(1-theta))
  assert avg==predicted and avg>0
  T=F(poly(0),1)/avg
  assert T == F(r*(r+1),1)/((1-p)*((d-1)*p*(1-p)-theta*(1-theta)))
  L0=lambda t:F((r-t)*(r+1-t)*(d-t),r*(r+1)*d)
  Lr=lambda t:F(t*(t-r-1)*(t-d),r*(d-r))
  Lr1=lambda t:F(-t*(t-r)*(t-d),(r+1)*(d-r-1))
  Ld=lambda t:F(t*(t-r)*(t-r-1),d*(d-r)*(d-r-1))
  weights=[sum(prob[t]*L(t) for t in range(d+1)) for L in [L0,Lr,Lr1,Ld]]
  assert all(w>=0 for w in weights) and sum(weights)==1 and weights[0]==1/T
  
  if (weights[1]==0)!=((d-2)%q==0):print("BAD",q,d,r,theta,weights);raise AssertionError
  for k in range(4):
   assert sum(prob[t]*t**k for t in range(d+1))==sum(w*s**k for w,s in zip(weights,[0,r,r+1,d]))
  if (d-2)%q==0:
   P2=lambda t:(d-t)*(t-r-1)*(t-r-2)
   assert all(P2(t)>=0 for t in range(d+1))
   assert F(P2(0),sum(prob[t]*P2(t) for t in range(d+1)))==T
  # Krawtchouk inversion: f has weight support at most 3.
  if q<=5 and d<=7:
   for j in range(4,d+1):
    inv=0
    for t in range(d+1):
     K=sum((-1)**s*(q-1)**(t-s)*comb(j,s)*comb(d-j,t-s)
           for s in range(t+1) if s<=j and t-s<=d-j)
     inv+=F(poly(t),1)*K
    assert inv==0
  checks+=1

# Direct full transform from inverse Fourier on q=3, d<=5 using exact complex sums
# is redundant to the exact Hamming-scheme identities checked above.
print('PASS:',checks,'parameter pairs; all cubic quadrature identities and Fourier-support checks exact')
