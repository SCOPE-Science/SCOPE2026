#!/usr/bin/env python3
"""Exact standard-library checks for signed-permutation symmetries and orbits."""
from itertools import permutations,product
from collections import Counter
from math import factorial,prod

# Homogeneous sextic: (X^2+Y^2+Z^2)^3-27X^2Y^2Z^2.
def poly_q():
    a={}
    for i in range(4):
        for j in range(4-i):
            k=3-i-j
            m=factorial(3)//(factorial(i)*factorial(j)*factorial(k))
            a[(2*i,2*j,2*k)]=m- (27 if (i,j,k)==(1,1,1) else 0)
    return {e:c for e,c in a.items() if c}
Q=poly_q()
F={(e[0]+1,e[1]+1,e[2]+1):v for e,v in Q.items()}
assert Q[(6,0,0)]==1 and Q[(4,2,0)]==3 and Q[(2,2,2)]==-21
assert len(Q)==10
sym=[]
for p in permutations(range(3)):
 for sign in product((-1,1),repeat=3):
  if sign[0]!=1: continue # projective scalar normalization
  sym.append((p,sign))
  T={}
  for e,c in F.items():
   new=[0,0,0]
   for j in range(3):new[p[j]]=e[j]
   new=tuple(new)
   T[new]=T.get(new,0)+c*prod(sign[j]**e[j] for j in range(3))
  assert T==F or T=={e:-v for e,v in F.items()}
assert len(sym)==24
# Points represented by triples of Gaussian integer pairs (a,b) standing for a+b*i.
zero=(0,0); one=(1,0); minus=(-1,0); im=(0,1); negim=(0,-1)
nodes4={(one,a,b) for a,b in product((one,minus),repeat=2)}
vertices={(one,zero,zero),(zero,one,zero),(zero,zero,one)}
cusps={(zero,one,s) for s in (im,negim)}|{(one,zero,s) for s in (im,negim)}|{(one,s,zero) for s in (im,negim)}
assert len(nodes4)==4 and len(vertices)==3 and len(cusps)==6

def norm(pt):
 # normalize first nonzero Gaussian coordinate to 1 (handles all points here)
 idx=next(i for i,a in enumerate(pt) if a!=zero)
 a,b=pt[idx]
 denom=a*a+b*b
 assert denom>0
 out=[]
 for c,d in pt:
  u=c*a+d*b;v=d*a-c*b
  assert u%denom==0 and v%denom==0
  out.append((u//denom,v//denom))
 return tuple(out)
def act(g,pt):
 p,sign=g
 z=[zero,zero,zero]
 for i in range(3): z[p[i]]=(sign[i]*pt[i][0],sign[i]*pt[i][1])
 return norm(z)
for pts in (nodes4,vertices,cusps):
 reps={norm(x) for x in pts}
 orbit={act(g,next(iter(reps))) for g in sym}
 assert orbit==reps,(orbit,reps)
 stabilizer=sum(act(g,next(iter(reps)))==next(iter(reps)) for g in sym)
 assert stabilizer==24//len(reps)
print('VERIFY_OK: 24 exact signed permutations; nonic invariance; singular orbits 6,4,3 and stabilizers 4,6,8')
