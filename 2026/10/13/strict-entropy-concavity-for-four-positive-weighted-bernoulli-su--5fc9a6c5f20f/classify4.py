import itertools, math
from fractions import Fraction

def determinant3(A):
 a,b,c=A
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def nullvec(rows):
 v=[(-1)**j*determinant3([[r[i] for i in range(4) if i!=j] for r in rows]) for j in range(4)]
 if not any(v):return None
 s=sum(v)
 if s==0:return None
 if s<0:v=[-x for x in v];s=-s
 if not (0<=v[0]<=v[1]<=v[2]<=v[3]):return None
 return tuple(Fraction(x,s) for x in v)

def canonical(t):
 vals={}
 for mask in range(16):
  s=sum(t[i] for i in range(4) if mask>>i&1)
  vals.setdefault(s,[0]*5)[mask.bit_count()]+=1
 return tuple(sorted(map(tuple,vals.values())))

normals=set()
for coefs in itertools.product((-1,0,1),repeat=4):
 if any(coefs):
  z=next(x for x in coefs if x)
  normals.add(tuple(z*c for c in coefs))
normals=sorted(normals)
extra=[(-1,0,0,0),(1,-1,0,0),(0,1,-1,0),(0,0,1,-1)]
print('N',len(normals),flush=True)
vertices=set()
for rows in itertools.combinations(normals+extra,3):
 v=nullvec(rows)
 if v:vertices.add(v)
vertices=sorted(vertices)
print('vertices',len(vertices),flush=True)
# Distinct equality subspaces represented by RREF of row triples;
# use canonical nullspace via rational row reduction

def rref(rows):
 m=[list(map(Fraction,r)) for r in rows]
 res=[]
 for j in range(4):
  k=next((k for k in range(len(m)) if m[k][j]),None)
  if k is None:continue
  pivot=m.pop(k); a=pivot[j];pivot=[z/a for z in pivot]
  m=[[v-z*pivot[i] for i,v in enumerate(vv)] if (z:=vv[j]) else vv for vv in m]
  res.append(tuple(pivot))
  if not m:break
 return tuple(res)

rrefs={}
for j in (0,1,2,3):
 for rows in itertools.combinations(normals,j):
  key=rref(rows)
  if len(key)==4:continue
  rrefs[key]=True
print('subspaces',len(rrefs),flush=True)
patterns={}
for key in rrefs:
 ok=[v for v in vertices if all(sum(a*b for a,b in zip(row,v))==0 for row in key)]
 if not ok:continue
 v=tuple(sum((10**12)**j*t[i] for j,t in enumerate(ok))/sum((10**12)**j for j in range(len(ok))) for i in range(4))
 if v[0]<=0:continue
 pat=canonical(v)
 old=patterns.get(pat)
 if old is None or max(v)<max(old):patterns[pat]=v
print('patterns',len(patterns),flush=True)


# Independent integer representatives provide an exact cross-check.
small={}
for ww in itertools.combinations_with_replacement(range(1,9),4): small.setdefault(canonical(ww),ww)
assert len(patterns)==23 and set(patterns)==set(small)
print("CLASSIFICATION VERIFIED: 23 patterns represented by weights <=8")
