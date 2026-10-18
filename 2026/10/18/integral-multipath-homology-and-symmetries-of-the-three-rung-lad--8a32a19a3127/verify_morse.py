import collections
ARCS=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5),(1,0),(2,1),(4,3),(5,4),(3,0),(4,1),(5,2)]
ORDER=[5,6,8,1,3,9,12,0,7,13,2,11,4,10]
N=6

def faces():
 ret={}
 for mask in range(1,1<<len(ARCS)):
  indeg=[-1]*N;outdeg=[-1]*N;valid=True
  for j,(u,v) in enumerate(ARCS):
   if mask>>j&1:
    if indeg[v]!=-1 or outdeg[u]!=-1:valid=False;break
    indeg[v]=u;outdeg[u]=v
  if not valid:continue
  for x in range(N):
   v=x;seen=set()
   while v!=-1 and v not in seen:
    seen.add(v);v=outdeg[v]
   if v!=-1:valid=False;break
  if valid:ret[mask]=mask.bit_count()-1
 return ret

def match(F):
 rem=set(F);pairs=[]
 for j in ORDER:
  bit=1<<j
  for x in sorted(tuple(rem)):
   if not x&bit and x|bit in rem:
    rem.remove(x);rem.remove(x|bit)
    pairs.append((x,x|bit))
 return pairs,rem

def bd(face):
 pos=[i for i in range(len(ARCS)) if face>>i&1]
 return {face^(1<<j):(-1)**k for k,j in enumerate(pos)} if len(pos)>1 else {}

def reduced_boundary(F,pairs):
 # Sparse columns of integral simplicial chain differential, ignoring augmentation.
 dd={f:bd(f) for f in F}
 for step,(s,t) in enumerate(pairs):
  assert s in dd and t in dd,(step,s,t)
  coeff=dd[t].get(s,0)
  if abs(coeff)!=1:raise AssertionError(('non-unit',step,s,t,coeff))
  # update columns having the lower cell s as incidence, exactly the Schur complement
  for x in list(dd):
   if x in (s,t):continue
   lam=dd[x].get(s,0)
   if lam:
    assert F[x]==F[t]
    for y,a in dd[t].items():
     if y==s:continue
     nv=dd[x].get(y,0)-lam*a//coeff
     if nv:dd[x][y]=nv
     else:dd[x].pop(y,None)
    dd[x].pop(s)
  del dd[s];del dd[t]
  for x in dd:dd[x].pop(t,None)
  assert all(s not in v and t not in v for v in dd.values())
 return dd

def topo(F,pairs):
 # Hasse graph: unmatched high->low, matched low->high
 targets=set(pairs); arrows=collections.defaultdict(set);indeg=collections.Counter()
 for x,d in F.items():
  if d<1:continue
  for j in range(len(ARCS)):
   if x>>j&1:
    s=x^(1<<j)
    if (s,x) in targets:u,v=s,x
    else:u,v=x,s
    if v not in arrows[u]:arrows[u].add(v);indeg[v]+=1
 q=collections.deque(x for x in F if indeg[x]==0);top=0
 while q:
  x=q.popleft();top+=1
  for y in arrows[x]:
   indeg[y]-=1
   if indeg[y]==0:q.append(y)
 return top,sum(len(z) for z in arrows.values())

if __name__=='__main__':
 F=faces();pairs,crit=match(F)
 print('arcs',ARCS)
 print('face_count',len(F),'f_vector',dict(sorted(collections.Counter(F.values()).items())))
 print('match_pairs',len(pairs),'critical',[(x,F[x]) for x in sorted(crit)])
 print('topological_sort',topo(F,pairs))
 d=reduced_boundary(F,pairs)
 print('Morse_boundaries_nonzero',[(x,b) for x,b in d.items() if b])
 print('Morse_cell_vector',dict(sorted(collections.Counter(F[x] for x in d).items())))

if __name__=='__main__':
 import json
 from pathlib import Path
 cert=json.loads(Path(__file__).with_name('matching_certificate.json').read_text(encoding='utf-8'))
 assert cert['arc_order']==[list(x) for x in ARCS]
 assert cert['toggle_order']==ORDER
 assert cert['matched_pairs']==[list(x) for x in pairs]
 assert cert['critical_faces']==sorted(crit)
 ranking={x:i for i,x in enumerate(cert['face_poset_topological_order'])}
 assert len(ranking)==len(F) and set(ranking)==set(F)
 mset=set(pairs)
 for high,dim in F.items():
  for j in range(len(ARCS)):
   if high>>j&1 and dim>=1:
    low=high^(1<<j)
    u,v=(low,high) if (low,high) in mset else (high,low)
    assert ranking[u]<ranking[v]
 assert len(pairs)==140 and len(F)==290
 assert dict(sorted(__import__('collections').Counter(F[x] for x in crit).items()))=={0:1,2:3,3:4,4:2}
 assert not any(reduced_boundary(F,pairs).values())
 print('explicit_matching_certificate_verified',len(pairs),'arrows',876)
