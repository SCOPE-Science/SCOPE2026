from itertools import product
import json
V=[]
for x in product(range(3),repeat=3):
 if any(x) and next(i for i,a in enumerate(x) if a)!=None and x[next(i for i,a in enumerate(x) if a)]==1:V.append(x)
assert len(V)==13
mats=[]
for i,j in [(0,1),(1,0),(1,2),(2,1)]:
 m=[[int(a==b) for b in range(3)]for a in range(3)];m[i][j]=1;mats.append(m)
def mult(a,b):return tuple(tuple(sum(a[i][k]*b[k][j]for k in range(3))%3 for j in range(3))for i in range(3))
def inv(a):
 for b in product(range(3),repeat=9):
  b=tuple(tuple(b[3*i:3*i+3])for i in range(3));
  if mult(a,b)==I:return b
 raise ValueError
I=tuple(tuple(int(i==j) for j in range(3))for i in range(3))
matrices=[tuple(tuple(r) for r in m)for m in mats]
group={I};Q=[I]
for a in Q:
 for b in matrices:
  c=mult(a,b)
  if c not in group:group.add(c);Q.append(c)
print('SL3 group order',len(group))
assert len(group)==5616

def normalize(x):
 a=next(t for t in x if t)
 return tuple(t*pow(a,-1,3)%3 for t in x)

def apply(m,v):return normalize([sum(m[i][k]*v[k]for k in range(3))%3 for i in range(3)])
info=[]
for m in matrices:
 mi=inv(m); mt=tuple(tuple(mi[j][i] for j in range(3))for i in range(3))
 # points map M; lines dual inverse transpose
 pmap=[V.index(apply(m,v)) for v in V]
 lmap=[V.index(apply(mt,v)) for v in V]
 info.append((pmap,lmap))
with open('generators.json','w') as f:json.dump(info,f)
print(info)
