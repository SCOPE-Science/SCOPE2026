from itertools import product,permutations
from collections import Counter,defaultdict
import json,time

# Coordinates x0,x1,x2,x3. Q=x0*x1+x2^2+x2*x3+x3^2.
def qpoint(v):
 a,b,c,d=[v>>i&1 for i in range(4)];return a*b^c^(c*d)^d
PTS=[v for v in range(1,16) if qpoint(v)==0]
assert PTS==[1,2,7,11,15]

# degree-3 monomials modulo Q*linear, normal with not both x0,x1
def degree_mons(d):
 return [(a,b,c,d-a-b-c) for a in range(d+1) for b in range(d+1-a) for c in range(d+1-a-b)]
BASIS=[m for m in degree_mons(3) if not (m[0] and m[1])]
assert len(BASIS)==16
BINDEX={m:i for i,m in enumerate(BASIS)}

# polynomial map represented as set of 4-tuples; scalar GF(2)
def mul(A,B):
 r=set()
 for a in A:
  for b in B:
   m=tuple(a[i]+b[i] for i in range(4))
   if m in r:r.remove(m)
   else:r.add(m)
 return r

def reduce1(m):
 if not (m[0] and m[1]):return [m]
 a,b,c,d=m
 return [(a-1,b-1,c+2,d),(a-1,b-1,c+1,d+1),(a-1,b-1,c,d+2)]
def normal(m):
 stack=[m];r=set()
 while stack:
  t=stack.pop()
  if t[0] and t[1]:stack.extend(reduce1(t))
  elif t in r:r.remove(t)
  else:r.add(t)
 return r

def mask_from_polynomial(p):
 out=0
 for mon in p:
  for m in normal(mon):out^=1<<BINDEX[m]
 return out

def map_cols(col):
 return [{tuple(1 if k==j else 0 for k in range(4)) for j in []}]

def lin(v):
 return {tuple(1 if i==k else 0 for i in range(4)) for k in range(4) if v>>k&1}

def matrix_on_basis(cols):
 out=[]
 for m in BASIS:
  p={(0,0,0,0)}
  for j in range(4):
   for _ in range(m[j]):p=mul(p,lin(cols[j]))
  out.append(mask_from_polynomial(p))
 return out

def act(mask,m):
 out=0
 while mask:
  b=mask&-mask
  out^=m[b.bit_length()-1]
  mask-=b
 return out

def group_from_permutation(perm):
 # solve 4x4 GF2 M with M*PTS[i] == PTS[perm[i]]
 src=PTS[:4]
 trgt=[PTS[perm[i]] for i in range(4)]
 # each column of M = sum of target vectors using coefficients expressed for e_j in source basis
 col=[]
 for j in range(4):
  sol=next(mask for mask in range(16) if __import__('functools').reduce(int.__xor__,(src[k] for k in range(4) if mask>>k&1),0)==(1<<j))
  v=0
  for k in range(4):
   if sol>>k&1:v^=trgt[k]
  col.append(v)
 assert all(__import__('functools').reduce(int.__xor__,(col[k] for k in range(4) if PTS[i]>>k&1),0)==PTS[perm[i]] for i in range(5))
 return col

PERMS=list(permutations(range(5)))
MATRICES=[group_from_permutation(p) for p in PERMS]
for cols in MATRICES:
 # Q(M*x)=Q(x) on all input points
 for v in range(1,16):
  vv=0
  for i in range(4):
   if v>>i&1:vv^=cols[i]
  assert qpoint(v)==qpoint(vv)
GENPERMS=[(1,0,2,3,4),(1,2,3,4,0)]
GENS=[matrix_on_basis(group_from_permutation(p)) for p in GENPERMS]

def eval_mask(mask,v):
 out=0
 for i,m in enumerate(BASIS):
  if mask>>i&1 and all((v>>j&1) or not m[j] for j in range(4)):out^=1
 return out

# fast eval vectors for five rational points
EVALS=[sum((1<<i) for i,m in enumerate(BASIS) if all((v>>j&1) or not m[j] for j in range(4))) for v in PTS]
assert len(set(EVALS))==5

def npoints(mask):return sum((mask&e).bit_count()%2==0 for e in EVALS)

def all_orbits():
 seen=bytearray(1<<16);res=[]
 for m in range(1,1<<16):
  if seen[m]:continue
  orb={m};seen[m]=1;queue=[m]
  for cur in queue:
   for a in GENS:
    nxt=act(cur,a)
    if not seen[nxt]:seen[nxt]=1;orb.add(nxt);queue.append(nxt)
  assert len(orb) in (1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120),len(orb)
  res.append((min(orb),len(orb),npoints(m)))
 return res
