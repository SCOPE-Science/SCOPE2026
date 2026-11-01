import sympy as sp
from itertools import product
from collections import Counter
E=[(u,v) for u in range(8) for v in range(8) if (u^v).bit_count()==1]
assert len(E)==24
idx={e:i for i,e in enumerate(E)}
N=[[v for v in range(8) if (u^v).bit_count()==1] for u in range(8)]
F=[set() for _ in range(8)]
for x in product(range(4),repeat=8):
 o=[N[u][v] if v<3 else -1 for u,v in enumerate(x)]
 valid=True
 for u in range(8):
  seen=set();v=u
  while v>=0 and v not in seen:
   seen.add(v);v=o[v]
  if v>=0:
   valid=False;break
 if valid:
  face=tuple(sorted(idx[(u,v)] for u,v in enumerate(o) if v>=0))
  if face:F[len(face)-1].add(face)
assert [len(f) for f in F] == [24,240,1296,4080,7488,7424,3072,0]
S=set().union(*F);S.add(())
P=[]
for v in range(len(E)):
 pairs=[]
 for f in list(S):
  if v in f:continue
  g=tuple(sorted((*f,v)))
  if g in S: pairs.append((f,g))
 for a,b in pairs:
  if a in S and b in S:S.remove(a);S.remove(b);P.append((a,b))

assert len(P)==11695 and len(S)==235 and Counter(len(f)-1 for f in S)=={5:50,6:185}
import sys
sys.setrecursionlimit(100000)
from functools import lru_cache
from collections import defaultdict
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
crit5=sorted(f for f in S if len(f)==6);crit6=sorted(f for f in S if len(f)==7)
crit5i={f:i for i,f in enumerate(crit5)}
up56={a:b for a,b in P if len(a)==6}
down45={b for a,b in P if len(b)==6}
assert len(up56)+len(down45)+len(crit5)==len(F[5])
visited=set();inprog=set()
@lru_cache(None)
def psi(x):
 if x in crit5i:return {crit5i[x]:1}
 if x in down45:return {}
 if x in inprog:raise RuntimeError('gradient cycle')
 inprog.add(x)
 beta=up56[x]
 pivot=(-1)**next(i for i in range(len(beta)) if beta[:i]+beta[i+1:]==x)
 res=defaultdict(int)
 for i in range(len(beta)):
  bface=beta[:i]+beta[i+1:]
  if bface==x:continue
  for j,c in psi(bface).items():res[j]-=pivot*((-1)**i)*c
 inprog.remove(x)
 return {j:v for j,v in res.items() if v}
MM=sp.zeros(len(crit5),len(crit6))
for j,beta in enumerate(crit6):
 coeff=defaultdict(int)
 for i in range(len(beta)):
  face=beta[:i]+beta[i+1:]
  for k,c in psi(face).items():coeff[k]+=(-1)**i*c
 for k,c in coeff.items():MM[k,j]=c
assert MM.shape == (50,185) and sum(bool(v) for v in MM)==366 and max(abs(v) for v in MM)==1 and MM.rank()==46
DD=smith_normal_form(MM,domain=ZZ)
ss=Counter(int(abs(DD[i,i])) for i in range(min(DD.shape)) if DD[i,i])
assert ss=={1:46} and (len(crit5)-MM.rank(),len(crit6)-MM.rank())==(4,139)
# Acyclicity on the entire directed face poset including empty face.
from collections import deque
allfaces=set().union(*F);allfaces.add(())
matched={(a,b) for a,b in P}
indeg={f:0 for f in allfaces}
adj={f:[] for f in allfaces}
for f in allfaces:
 for i in range(len(f)):
  a=f[:i]+f[i+1:]
  if (a,f) in matched:
   src,dst=a,f
  else:
   src,dst=f,a
  adj[src].append(dst);indeg[dst]+=1
q=deque(f for f in allfaces if indeg[f]==0);seen=0
while q:
 f=q.popleft();seen+=1
 for b in adj[f]:
  indeg[b]-=1
  if indeg[b]==0:q.append(b)
assert seen==len(allfaces)==23625 and sum(map(len,adj.values()))==124200
# A unimodular 46 x 46 subdeterminant if available.
pivcols=MM.rref()[1]
sub=MM[:,list(pivcols)]
pivrows=sub.T.rref()[1]
minor=sub[list(pivrows),:]
assert minor.det(method='domain-ge')==1
print('face_vector=24,240,1296,4080,7488,7424,3072')
print('full_hasse=23625; incidences=124200; matched_pairs=11695; acyclic=True')
print('critical_cells=(0:1 after empty-pair release,5:50,6:185)')
print('morse_boundary=(50,185); nonzeros=366; rank=46; smith=1x46')
print('unimodular_minor=46x46 det+1; reduced_homology_Z=(H5:Z4,H6:Z139)')
print('VERIFY_OK')
