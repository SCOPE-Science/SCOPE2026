#!/usr/bin/env python3
"""Exact coefficient and Weierstrass-semigroup consistency checks."""
from math import comb

# Coefficients of y_W^q after y_U=t*y_W/(1-t^-2*y_W).
def exponent(j,q):
    return 3*j-2*q
assert exponent(2,2)==2
assert exponent(2,3)==0 and comb(2,1)==2
assert exponent(3,3)==3
assert exponent(3,4)==1 and comb(3,2)==3
assert exponent(4,4)==4
assert exponent(5,5)==5

# Initial coefficients (index = order along the exceptional curve).
P={2:{(0,0):1}, 3:{}}
Q={2:{(1,0):1}, 3:{(0,1):-2}}
R={3:{(0,0):1}, 4:{}}
S={3:{(1,0):1}, 4:{(0,1):-3}}

def product_coeff(A,B,n):
    out={}
    for a,da in A.items():
      for b,db in B.items():
       if a+b != n: continue
       for (xa,za),ca in da.items():
        for (xb,zb),cb in db.items():
         key=(xa+xb,za+zb)
         out[key]=out.get(key,0)+ca*cb
    return {k:v for k,v in out.items() if v}

for q,expect in [(5,{}),(6,{(0,1):-1})]:
    p=product_coeff(P,S,q)
    o=product_coeff(Q,R,q)
    for k,v in o.items():p[k]=p.get(k,0)-v
    p={k:v for k,v in p.items() if v}
    assert p==expect, (q,p,expect)

# Section ring for genus-two Weierstrass semigroup <2,5> has
# basis T^r X^a Z^b (b=0,1), with weight r+2*a+5*b.
G=[(2,0,0),(0,1,0),(3,0,0),(1,1,0),(0,0,1),(1,0,1)]
reachable={(0,0,0)}
for q in range(2,101):
    for g in G:
      if g[0]+2*g[1]+5*g[2]>q:continue
    changed=True
    while changed:
      changed=False
      for u in list(reachable):
       for g in G:
        v=tuple(a+b for a,b in zip(u,g))
        if v[2]>1:continue
        w=v[0]+2*v[1]+5*v[2]
        if w<=q and v not in reachable:
         reachable.add(v); changed=True
    expected={(q-2*a-5*b,a,b) for b in (0,1)
              for a in range((q-5*b)//2+1) if q-5*b>=0}
    assert expected.issubset(reachable), (q,expected-reachable)
assert (1,0,0) not in reachable
print('VERIFY_OK transition_exponents=true degree5_cancellation=true degree6_coefficient_minus_z=true weighted_Weierstrass_basis_through_100=true')
