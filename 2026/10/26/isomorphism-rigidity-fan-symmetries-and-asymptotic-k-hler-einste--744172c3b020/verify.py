#!/usr/bin/env python3
"""Exact arithmetic checks for root-twist isomorphism/orbit enumeration."""
from itertools import permutations, product
from math import factorial
from fractions import Fraction

# An oriented 120-degree triple gamma0+gamma1+gamma2=0.
# Root coordinates: gamma0=(1,0), gamma1=(0,1), gamma2=(-1,-1).
roots=((1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1))
assert all((roots[i][0]+roots[i+3][0],roots[i][1]+roots[i+3][1])==(0,0) for i in range(3))

def multisets(k):
    # All possible multisets of k among the 6 roots.
    for a0 in range(k+1):
      for a1 in range(k-a0+1):
       for a2 in range(k-a0-a1+1):
        for b0 in range(k-a0-a1-a2+1):
         for b1 in range(k-a0-a1-a2-b0+1):
          b2=k-a0-a1-a2-b0-b1
          m=(a0,a1,a2,b0,b1,b2)
          if a0-b0==a1-b1==a2-b2:
              yield m

G=[(per,neg) for per in permutations(range(3)) for neg in (0,1)]
assert len(G)==12

def act(m,g):
    per,neg=g
    out=[0]*6
    for i in range(3):
        out[per[i]+3*neg]=m[i]
        out[per[i]+3*(1-neg)]=m[i+3]
    return tuple(out)

def normal(m):
    d=abs(m[0]-m[3]); q=tuple(sorted(min(m[i],m[i+3]) for i in range(3)))
    return (d,)+q

def aut_order(m):
    stab=sum(act(m,g)==m for g in G)
    z=1
    for a in m:z*=factorial(a)
    return (2**sum(m))*z*stab

def formula(k):
    vals=[]
    for d in range(k//3+1):
      rem=k-3*d
      if rem<0 or rem%2: continue
      target=rem//2
      for q0 in range(target//3+1):
        for q1 in range(q0,(target-q0)//2+1):
          q2=target-q0-q1
          if q2<q1:continue
          if (d,q0,q1,q2)==(0,0,0,0):continue
          vals.append((d,q0,q1,q2))
    ke=sum(d==0 or (q0==q1==q2) for d,q0,q1,q2 in vals)
    return len(vals),ke,vals

checks=[]
for k in range(2,15):
   mlist=list(multisets(k)); reps={min(act(m,g) for g in G) for m in mlist}
   normal_forms={normal(m) for m in mlist}
   count,ke,vals=formula(k)
   assert len(reps)==len(normal_forms)==count,(k,len(reps),len(normal_forms),count)
   assert set(vals)==normal_forms
   count_ke=sum(m[0]==m[3] or (m[0]==m[1]==m[2] and m[3]==m[4]==m[5]) for m in reps)
   assert count_ke==ke,(k,count_ke,ke)
   assert all(aut_order(m)>0 for m in reps)
   checks.append((k,len(mlist),count,ke,count-ke))

# Check that the prescribed generating function matches all counts by a wholly
# independent coefficient multiplication, including zero exclusion.
def inv_prod_coeff(parts,degree):
    coeff=[0]*(degree+1);coeff[0]=1
    for p in parts:
      for i in range(p,degree+1):coeff[i]+=coeff[i-p]
    return coeff
b=inv_prod_coeff((3,2,4,6),200)
c=inv_prod_coeff((2,4,6),200)
e=inv_prod_coeff((3,6),200)
for k in range(2,100):
  count,ke,_=formula(k)
  assert count==b[k] and ke==c[k]+(e[k-3] if k>=3 else 0),(k,count,ke,b[k],c[k],e[k-3])
# Group order examples, and all isomorphism classes in small dimension.
examples=[]
for k in (2,3,4,5,6):
  reps=sorted({min(act(m,g) for g in G) for m in multisets(k)})
  examples.append((k,[(normal(m),aut_order(m)) for m in reps]))
print('VERIFY_OK D6_actions=12 orbit_normal_forms_k2_to14=true count_series_k2_to99=true')
print('k multisets orbits KE nonKE')
for row in checks:print(*row)
print('sample_fan_symmetry_orders')
for k,vals in examples:print(k, vals)
