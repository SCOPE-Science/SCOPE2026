"""Exact combinatorial fixed loci of the seven-by-seven graph-metric Rips complex at radius four."""
from itertools import product
from collections import Counter
import heapq
import json

N=7;R=4
POINTS=tuple(product(range(N),repeat=2))
def d(x,y):
 return sum(min((a-b)%N,(b-a)%N) for a,b in zip(x,y))

def action(e1,e2,a,b,sw):
 def f(p):
  x,y=p
  if sw:x,y=y,x
  return ((e1*x+a)%N,(e2*y+b)%N)
 return f

def orbits(f):
 seen=set();out=[]
 for p in POINTS:
  if p not in seen:
   v=[];z=p
   while z not in seen:
    v.append(z);seen.add(z);z=f(z)
   out.append(tuple(v))
 return out

def orbit_graph(f):
 O=orbits(f)
 eligible=[o for o in O if all(d(p,q)<=R for p in o for q in o)]
 nbr=[]
 for i,o in enumerate(eligible):
  mask=0
  for j,u in enumerate(eligible):
   if i!=j and all(d(p,q)<=R for p in o for q in u):mask|=1<<j
  nbr.append(mask)
 return O,eligible,nbr

def faces(nbr):
 result=set()
 def visit(s,P):
  if s:result.add(s)
  while P:
   bit=P&-P;P-=bit;i=bit.bit_length()-1
   visit(s|bit,P&nbr[i])
 visit(0,(1<<len(nbr))-1)
 return result

def elementary_collapse(initial):
 faceset=set(initial)
 supers={f:set() for f in faceset}
 for s in faceset:
  if s.bit_count()>=2:
   p=s
   while p:
    bit=p&-p;p-=bit
    supers[s^bit].add(s)
 heap=[]
 def consider(f):
  if f not in faceset or len(supers[f])!=1:return
  co=next(iter(supers[f]))
  if supers[co]:return
  heapq.heappush(heap,(-f.bit_count(),f,co))
 for s in faceset:consider(s)
 pairs=[]
 while heap:
  _,a,b=heapq.heappop(heap)
  if a not in faceset or b not in faceset or supers[a]!={b} or supers[b]:continue
  pairs.append((a,b));faceset.remove(a);faceset.remove(b)
  touched=set()
  for s in (a,b):
   p=s
   while p:
    bit=p&-p;p-=bit;t=s^bit
    if t in faceset:
     supers[t].discard(s);touched.add(t)
  for t in touched:
   consider(t)
   p=t
   while p:
    bit=p&-p;p-=bit;u=t^bit
    if u in faceset:consider(u)
 return faceset,pairs

def classify_core(core):
 if not core:return 'empty'
 vc=[s for s in core if s.bit_count()==1]
 ec=[s for s in core if s.bit_count()==2]
 tc=[s for s in core if s.bit_count()==3]
 if len(core)==2 and len(vc)==2 and not ec and not tc:return 'S0'
 if len(tc)==0 and len(core)==2*len(vc) and len(vc)>=3:
  if all(sum(bool(e&v) for e in ec)==2 for v in vc):
   seen={vc[0]};todo=[vc[0]]
   while todo:
    v=todo.pop()
    for e in ec:
     if e&v:
      u=e^v
      if u not in seen:seen.add(u);todo.append(u)
   if len(seen)==len(vc):return 'S1'
 if len(core)==len(vc)+len(ec)+len(tc) and tc:
  if len(vc)-len(ec)+len(tc)==2 and all(sum(t& e==e for t in tc)==2 for e in ec):
   verts_adj={v:set() for v in vc}
   for e in ec:
    vv=[v for v in vc if e&v]
    for v in vv:verts_adj[v].update(w for w in vv if w!=v)
   seen={vc[0]};todo=[vc[0]]
   while todo:
    v=todo.pop()
    for u in verts_adj[v]:
     if u not in seen:seen.add(u);todo.append(u)
   # connected closed triangulated surface with Euler 2 -> sphere;
   # verify each vertex link a simple cycle.
   def cycle_link(v):
    subedges=[t^v for t in tc if t&v]
    verts=[w for w in vc if any(e&w for e in subedges)]
    if not (len(subedges)==len(verts) and all(sum(bool(e&w) for e in subedges)==2 for w in verts)):
     return False
    if not verts:
     return False
    reached={verts[0]}; todo=[verts[0]]
    while todo:
     cur=todo.pop()
     for e in subedges:
      if e&cur:
       u=e^cur
       if u not in reached: reached.add(u);todo.append(u)
    return len(reached)==len(verts)
   if len(seen)==len(vc) and all(cycle_link(v) for v in vc):return 'S2'
 return 'unknown'

def expected_type(e1,e2,a,b,sw):
 if not sw:
  typ1='ref' if e1==-1 else ('rot' if a else 'id')
  typ2='ref' if e2==-1 else ('rot' if b else 'id')
  types=tuple(sorted([typ1,typ2]))
  lookup={('id','id'):'S3',('id','rot'):'S1',('rot','rot'):'empty',('id','ref'):'S2',('ref','rot'):'S0',('ref','ref'):'S1'}
  return lookup[types]
 # square acts via one product in D7: if e1*e2=+ and translation e1*b+a mod 7 nonzero -> rotation.
 sign=e1*e2
 trans=(e1*b+a)%N
 return 'S0' if sign==-1 else ('S1' if trans==0 else 'empty')

def run():
 count=Counter();maxfaces=0;largest={};unknown=[];allstats=Counter()
 for e1,e2,a,b,sw in product((1,-1),(1,-1),range(N),range(N),(0,1)):
  f=action(e1,e2,a,b,sw)
  O,E,adj=orbit_graph(f)
  expected=expected_type(e1,e2,a,b,sw)
  # Every affine coordinate operation is a genuine permutation of the 49 metric points.
  assert len(set(f(p) for p in POINTS))==49
  assert all(d(f(p),f(q))==d(p,q) for p in POINTS for q in POINTS)
  if expected=='S3':
   assert e1==e2==1 and a==b==0 and not sw
   count[(expected,'published')]+=1
   continue
  fs=faces(adj)
  maxfaces=max(maxfaces,len(fs))
  core,pairs=elementary_collapse(fs)
  got=classify_core(core)
  count[(expected,got)]+=1
  allstats[(expected,len(E),len(fs),len(pairs),len(core),len(O))]+=1
  # Independently check reduced Lefschetz signs through the clique Euler sum.
  chi=sum((-1)**(s.bit_count()-1) for s in fs)
  expected_chi={'empty':0,'S0':2,'S1':0,'S2':2}[expected]
  if chi!=expected_chi:raise AssertionError(('Euler discrepancy',e1,e2,a,b,sw,chi,expected_chi))
  if expected!=got:unknown.append((e1,e2,a,b,sw,expected,got,len(fs),len(core),len(E)))
  if got not in largest or len(fs)>largest[got][0]:
   largest[got]=(len(fs),(e1,e2,a,b,sw),len(E),len(pairs),Counter(s.bit_count()-1 for s in core),len(O))
 print('count',count)
 print('largest',largest)
 print('fails',unknown[:30], 'n',len(unknown))
 print('stats',sorted(allstats.items(),key=lambda a:a[0])[:120])
 assert not unknown
 assert sum(count.values())==392
 return {
  'ambient_vertices':49,'metric_radius':4,'symmetry_elements':392,
  'fixed_locus_type_counts':{k:sum(v for (typ,got),v in count.items() if typ==k) for k in ['S3','S2','S1','S0','empty']},
  'nonidentity_elements_certified_by_elementary_collapses':391,
  'maximum_fixed_orbit_complex_faces':maxfaces,
  'largest_representative_reductions':{
   k:{'initial_nonempty_faces':v[0],'group_element':list(v[1]),'orbit_vertices':v[2],
      'elementary_collapse_pairs':v[3],'remaining_faces_by_dimension':dict(sorted(v[4].items())),
      'original_point_orbits':v[5]} for k,v in largest.items()
  },
  'other_types':{str(k):v for k,v in allstats.items()}
 }
if __name__=='__main__':
 output=run()
 print('SUCCESS ALL 392 ELEMENTS')
 print(json.dumps(output,indent=2,sort_keys=True))
