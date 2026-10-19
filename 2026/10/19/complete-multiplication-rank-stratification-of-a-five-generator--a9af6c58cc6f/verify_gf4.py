"""Independent GF(4) sample verifier for the modular group-algebra rank census.
Run: python3 verify_gf4.py
GF(4)=GF(2)[u]/(u*u+u+1), elements 0,1,u,u+1 encoded 0..3.
"""
from itertools import combinations
from random import Random
from collections import Counter

q=4
mul=[[0]*q for _ in range(q)]
for x in range(q):
 for y in range(q):
  acc=0
  for i in range(2):
   for j in range(2):
    if (x>>i)&1 and (y>>j)&1: acc^=1<<(i+j)
  if acc&8: acc^=0b1110 # x^3 = x^2 + x, in quotient x^2=x+1 => x^3=1
  if acc&4: acc^=0b111
  mul[x][y]=acc
assert mul[2][2]==3 and mul[2][3]==1
inv={1:1,2:3,3:2}
subs={d:[s for s in range(32) if s.bit_count()==d] for d in range(6)}

def matrix_rank(matrix):
 a=[row[:] for row in matrix]; m=len(a);n=len(a[0]);r=0
 for j in range(n):
  pivot=next((i for i in range(r,m) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  scale=inv[a[r][j]]
  for k in range(j,n):a[r][k]=mul[scale][a[r][k]]
  for i in range(m):
   if i==r or not a[i][j]:continue
   factor=a[i][j]
   for k in range(j,n):a[i][k]^=mul[factor][a[r][k]]
  r+=1
  if r==m:break
 return r

def operator_rank(x):
 a=[[0]*32 for _ in range(32)]
 for s,v in enumerate(x):
  if v:
   for t in range(32):
    if not (s&t): a[s|t][t]^=v
 return matrix_rank(a)

def bivector_rank(x,d):
 m=[[0]*5 for _ in range(5)]
 for s in subs[d]:
  v=x[s]
  if not v:continue
  t=s if d==2 else 31^s
  i=(t&-t).bit_length()-1;j=t.bit_length()-1
  m[i][j]^=v;m[j][i]^=v
 return matrix_rank(m)

def predicted(x):
 deg=[sum(v!=0 for s,v in enumerate(x) if s.bit_count()==d) for d in range(6)]
 if deg[1]:return 16
 if deg[2]:
  ar=bivector_rank(x,2)
  if ar==4:return 12
  if ar!=2:raise RuntimeError('bad quadratic rank')
  gamma=0
  for s in subs[2]:gamma^=mul[x[s]][x[31^s]]
  return 10 if gamma else 8
 if deg[3]:return bivector_rank(x,3)+2
 if deg[4]:return 2
 if deg[5]:return 1
 return 0

rng=Random(81213)
cases=[]
for _ in range(160):
 x=[0]*32
 for s in range(1,32):x[s]=rng.randrange(q)
 cases.append(x)
# targeted Q rank 2 perturbations, Q rank 4, cubic rank 2/4, and highest terms.
for sub in [subs[2],subs[3],subs[4],subs[5]]:
 for _ in range(80):
  x=[0]*32
  for s in range(1,32):
   if s.bit_count()>=sub[0].bit_count():x[s]=rng.randrange(q)
  if not any(x[s] for s in sub):x[sub[0]]=1
  cases.append(x)
for _ in range(100):
 x=[0]*32;x[3]=rng.randrange(1,q)
 for s in range(7,32):
  if s.bit_count()>=3:x[s]=rng.randrange(q)
 cases.append(x)
for k,x in enumerate(cases):
 r=operator_rank(x);p=predicted(x)
 assert r==p, (k,r,p,x)
print('VERIFY_OK_GROUP_ALGEBRA_GF4')
print('GF4 independent cases=',len(cases))
