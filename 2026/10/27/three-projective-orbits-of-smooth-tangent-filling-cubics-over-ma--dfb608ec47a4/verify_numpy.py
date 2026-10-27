"""Standalone independent incidence sieve for tangent-filling ternary cubics over F3."""
import numpy as np
from collections import Counter
Q=3
pts=[]
for a in range(3):
 for b in range(3):
  for c in range(3):
   if a==b==c==0:continue
   w=(a,b,c);k=next(t for t in w if t)
   w=tuple(v*(1 if k==1 else 2)%3 for v in w)
   if w not in pts:pts.append(w)
pts=np.array(pts,dtype=np.int64)
assert pts.shape==(13,3)
exps=[(a,b,3-a-b) for a in range(4) for b in range(4-a)]
M=np.array([[np.prod([int(pt[j])**e for j,e in enumerate(m)])%3 for m in exps] for pt in pts],dtype=np.int64)
D=np.array([[[e[j]*np.prod([int(pt[k])**(e[k]-(k==j)) for k in range(3)])%3 if e[j] else 0 for j in range(3)] for e in exps] for pt in pts],dtype=np.int64)
C=np.array([[i//(3**j)%3 for j in range(10)] for i in range(1,3**10)],dtype=np.int64)
mask=np.zeros(27,dtype=np.int32)
for g in range(1,27):
 x=(g//9,(g//3)%3,g%3)
 mask[g]=sum(1<<i for i,pt in enumerate(pts) if sum(u*v for u,v in zip(x,pt))%3==0)
full=(1<<13)-1
covers=np.zeros(len(C),dtype=np.int32)
rsm=np.ones(len(C),dtype=bool)
for i in range(13):
 hit=(C@M[i])%3==0
 grad=(C@D[i])%3
 k=9*grad[:,0]+3*grad[:,1]+grad[:,2]
 rsm &= ~(hit & (k==0))
 covers|=np.where(hit,mask[k],0)
valid=np.where(rsm & (covers==full))[0]+1
print('all nonzero equations',len(C))
print('smooth at rational points',int(rsm.sum()))
print('tangent filling with rational smoothness',len(valid))
print('independent coeff codes match',valid.tolist()==sorted(int(x) for x in open('candidate_codes.txt')))
print('point counts',Counter(((C[valid-1]@M.T)%3==0).sum(axis=1)))
