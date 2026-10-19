#!/usr/bin/env python3
"""Exact integer enumeration of bounded Gaussian-integer coefficient vectors."""
from collections import defaultdict
from itertools import product
Z=[complex(x,y) for x in range(-2,3) for y in range(-2,3)]
ROOTS=(1,1j,-1,-1j)
def abs2(z):return int(z.real)**2+int(z.imag)**2
def data(p):
 a,b,c=p
 return tuple(t for z in ROOTS for t in (abs2(a+b*z+c*z*z),abs2(b+2*c*z)))
def phase_eq(p,q):
 # Same measurement plus matching rank-one matrices means global phase equivalence.
 return all(p[i]*q[j]==p[j]*q[i] for i in range(3) for j in range(i+1,3)) and sum(abs2(z) for z in p)==sum(abs2(z) for z in q)
groups=defaultdict(list)
for p in product(Z,repeat=3): groups[data(p)].append(p)
maxclasses=0
for G in groups.values():
 reps=[]
 for p in G:
  if not any(phase_eq(p,q) for q in reps):reps.append(p)
 assert len(reps)<=3,(len(reps),reps)
 maxclasses=max(maxclasses,len(reps))
print('PASS: 15,625 exact Gaussian-integer coefficient vectors;',len(groups),'measurement classes; maximal distinct-phase multiplicity',maxclasses)
