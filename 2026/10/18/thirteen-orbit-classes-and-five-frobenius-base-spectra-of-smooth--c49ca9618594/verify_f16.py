#!/usr/bin/env python3
"""Independent exact finite-field check of smooth (2,2) pencils over F_2.

Bit k=3*i+j is coefficient of u^(2-i)v^i s^(2-j)t^j, 0<=i,j<=2.
Checks geometric smoothness by evaluating all points over F_16. Completeness
follows since in every affine chart the two partial derivatives are binary
univariate polynomials of degree <=2 in opposite variables. Their roots lie
in F_4; when a partial vanishes identically, the other coordinate solves a
quadratic over F_4 and hence lies in F_16. If both vanish identically, the
local equation is a square and a zero exists in F_16.
"""
from collections import Counter
from itertools import permutations

def mul(a,b):
    ans=0
    while b:
        if b&1: ans ^=a
        b>>=1; a<<=1
        if a&16: a^=0x13
    return ans

mul_tbl=[[mul(a,b) for b in range(16)] for a in range(16)]
def value(z, aa, bb):
    return __import__('functools').reduce(int.__xor__,
      (mul_tbl[aa[i]][bb[j]] for i in range(3) for j in range(3) if z>>(3*i+j)&1),0)

P=[(1,k,mul(k,k)) for k in range(16)]+[(0,0,1)]
# Basis values of (u^2,uv,v^2) at each projective coordinate [1:t] or [t:1];
# derivative of the local basis is always (0,1,0) in characteristic two.
zeros=[]
for z in range(1,512):
    singular=False
    for aa in P:
        if singular: break
        for bb in P:
            f=value(z,aa,bb)
            fx=0;fy=0
            for j in range(3):
                if z>>(3+j)&1:fx^=bb[j]
            for i in range(3):
                if z>>(3*i+1)&1:fy^=aa[i]
            if f==fx==fy==0:
                singular=True; break
    if not singular: zeros.append(z)
S=set(zeros)
assert len(S)==144

rational=[(1,0,0),(0,0,1),(1,1,1)]
from itertools import product
G=list(product(rational,rational))
V={z:sum(value(z,a,b)==0 for a,b in G) for z in S}
E={z:sum((1<<k) for k,(a,b) in enumerate(G) if value(z,a,b)) for z in range(512)}
assert len(set(E.values()))==512
s_eval={E[z] for z in S}
PENS={tuple(sorted([a,b,a^b])) for a in s_eval for b in s_eval if a<b and a^b in s_eval}
assert len(PENS)==804
assert not any(all(d^z in s_eval for z in p) for p in PENS for d in s_eval if d not in p)
patterns=Counter()
base=Counter()
for p in PENS:
    a,b,c=p
    basepts=9-(a|b).bit_count()
    base[basepts]+=1
    patterns[(tuple(sorted([9-a.bit_count(),9-b.bit_count(),9-c.bit_count()])),basepts)]+=1
assert base==Counter({0:84,1:504,2:216})
assert patterns==Counter({((3,4,4),1):216,((2,4,5),1):216,((3,5,5),2):108,((4,4,5),2):108,((3,3,5),1):72,((2,3,4),0):72,((3,3,3),0):12})
perms=list(permutations(range(3)))
# Transformation of the 3x3 grid under the full 72 automorphisms.
transform=[]
for rr in perms:
 for cc in perms:
  for swap in range(2):
   idx=[3*(cc[j] if swap else rr[i])+(rr[i] if swap else cc[j]) for i in range(3) for j in range(3)]
   transform.append(idx)
assert len({tuple(x) for x in transform})==72

def apply(z,p):
    return sum(((z>>t)&1)<<k for k,t in enumerate(p))
remaining=set(PENS); orbs=[]
while remaining:
    p=min(remaining)
    orb={tuple(sorted(apply(z,t) for z in p)) for t in transform}
    assert orb<=remaining
    remaining-=orb
    a,b,c=min(orb)
    n=9-(a|b).bit_count()
    orbs.append((len(orb),n,tuple(sorted([9-a.bit_count(),9-b.bit_count(),9-c.bit_count()]))))
assert len(orbs)==13 and sum(z[0] for z in orbs)==804
assert Counter(z[0] for z in orbs)==Counter({72:10,36:2,12:1})
print('independent field F16 check: smooth 144; pencils 804; no nets; 13 orbits')
print('base counts',sorted(base.items()))
print('point-count and base-point strata',sorted((a,b,n) for (a,b),n in patterns.items()))
print('orbit-strata',sorted(orbs))
print('PASS')
