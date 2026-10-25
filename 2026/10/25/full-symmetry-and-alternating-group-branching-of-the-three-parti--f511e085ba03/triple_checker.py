#!/usr/bin/env python3
"""Exact oriented CW checker for UConf_3(K_2,4), genus-three surface."""
import itertools,collections
from fractions import Fraction
V=tuple(range(6)); E=tuple((h,i) for h in (4,5) for i in range(4))
c0=list(itertools.combinations(V,3))
c1=[(e,vs) for e in E for vs in itertools.combinations((v for v in V if v not in e),2)]
c2=[(e,f,v) for a,e in enumerate(E) for f in E[a+1:] if set(e).isdisjoint(f) for v in V if v not in e and v not in f]
i0={c:i for i,c in enumerate(c0)}; i1={c:i for i,c in enumerate(c1)}; i2={c:i for i,c in enumerate(c2)}
d1=[[0]*len(c1) for _ in c0]; d2=[[0]*len(c2) for _ in c1]
for j,(e,vs) in enumerate(c1):
  for x,s in [(e[1],+1),(e[0],-1)]:d1[i0[tuple(sorted((x,)+vs))]][j]+=s
for j,(e,f,v) in enumerate(c2):
  for ec,vc,s in ((f,(e[1],v),1),(f,(e[0],v),-1),(e,(f[1],v),-1),(e,(f[0],v),1)):
    d2[i1[(ec,tuple(sorted(vc)))]][j]+=s
assert [len(c0),len(c1),len(c2)]==[20,48,24]
assert all(sum(d1[i][k]*d2[k][j] for k in range(len(c1)))==0 for i in range(len(c0)) for j in range(len(c2)))
# closed oriented pseudomanifold: each 1-cell in precisely 2 2-cells, with opposite incidences in global cycle
assert {sum(bool(x) for x in row) for row in d2}=={2}
# Check that the CW complex is genuinely a closed surface: every vertex link
# is a single combinatorial cycle, not a disjoint union of cycles.
for vt in c0:
 adjacent={}
 for e,vs in c1:
  if tuple(sorted((e[0],)+vs))==vt or tuple(sorted((e[1],)+vs))==vt:
   adjacent[(e,vs)]=set()
 for e,f,v in c2:
  for x in e:
   for y in f:
    if tuple(sorted((x,y,v)))!=vt:continue
    one=(e,tuple(sorted((y,v))));two=(f,tuple(sorted((x,v))))
    adjacent[one].add(two);adjacent[two].add(one)
 assert all(len(neighbors)==2 for neighbors in adjacent.values()),vt
 seen={next(iter(adjacent))}; stack=list(seen)
 while stack:
  for target in adjacent[stack.pop()]:
   if target not in seen:seen.add(target);stack.append(target)
 assert len(seen)==len(adjacent),vt
rowcols=[[j for j,x in enumerate(row) if x] for row in d2]
cycle={0:1}; todo=[0]
while todo:
 j=todo.pop()
 for row,(a,b) in zip(d2,rowcols):
  if j not in (a,b):continue
  other=b if j==a else a
  val=-cycle[j]*row[j]//row[other]
  if other in cycle:assert cycle[other]==val
  else:cycle[other]=val;todo.append(other)
assert len(cycle)==24
z=[cycle[i] for i in range(24)]
assert all(sum(d2[k][j]*z[j] for j in range(24))==0 for k in range(48))

def rank(a,p=1009):
 b=[[x%p for x in row] for row in a];r=0
 for j in range(len(b[0])):
  k=next((k for k in range(r,len(b)) if b[k][j]),None)
  if k is None:continue
  b[r],b[k]=b[k],b[r];x=pow(b[r][j],-1,p)
  b[r]=[(t*x)%p for t in b[r]]
  for k in range(r+1,len(b)):
   if b[k][j]:
    w=b[k][j];b[k]=[(x-w*y)%p for x,y in zip(b[k],b[r])]
  r+=1
  if r==len(b):break
 return r
assert rank(d1)==19 and rank(d2)==23

def mapcell(cell,dimension,alpha):
 if dimension==0:return tuple(sorted(alpha[u] for u in cell)),1
 if dimension==1:
  e,vs=cell
  return ((alpha[e[0]],alpha[e[1]]),tuple(sorted(alpha[u] for u in vs))),1
 e,f,v=cell
 a=(alpha[e[0]],alpha[e[1]]); b=(alpha[f[0]],alpha[f[1]])
 return ((a,b,alpha[v]),1) if E.index(a)<E.index(b) else ((b,a,alpha[v]),-1)

def cycletype(pi):
 seen=set();a=[]
 for i in range(4):
  if i in seen:continue
  j=i;k=0
  while j not in seen:seen.add(j);j=pi[j];k+=1
  a.append(k)
 return tuple(sorted(a,reverse=True))
rows=collections.defaultdict(set)
for perm in itertools.permutations(range(4)):
 for hub in (0,1):
  alpha={i:perm[i] for i in range(4)};alpha[4]=4+hub;alpha[5]=5-hub
  traces=[]
  for dim,cs in enumerate((c0,c1,c2)):
   tr=sum(s for c in cs for cc,s in (mapcell(c,dim,alpha),) if cc==c)
   traces.append(tr)
  zimage=[0]*24
  for j,c in enumerate(c2):
   cc,sgn=mapcell(c,2,alpha);zimage[i2[cc]]+=sgn*z[j]
  assert zimage==z or zimage==[-v for v in z]
  orient=1 if zimage==z else -1
  chiH1=1+orient-traces[0]+traces[1]-traces[2]
  rows[(cycletype(perm),hub)].add((orient,chiH1,*traces))
for (typ,h),values in sorted(rows.items()):
 assert len(values)==1
 print('type',typ,'hub',h,'[H2,H1,C0,C1,C2]',next(iter(values)))
print('PASS 20,48,24 cells; rank(d1)=19 rank(d2)=23; 48 symmetry actions; primitive orientation cycle; chain boundary')
