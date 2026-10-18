#!/usr/bin/env python3
"""Exhaustively test DAG signature aliases for transitive forest orders.
Every labelled DAG has some topological labelling; upper-triangular
presentations cover all DAGs up to isomorphism. Finite evidence only.
"""
from itertools import combinations
from collections import defaultdict,Counter

def forest_form(r):
 n=len(r)
 if not all((r[j]&~r[i])==0 for i in range(n) for j in range(i+1,n) if r[i]&(1<<j)):return None
 d=[sum(bool(r[u]&(1<<v)) for u in range(n)) for v in range(n)]
 parents=[]
 for v in range(n):
  pre=[u for u in range(n) if r[u]&(1<<v)]
  if any(not (r[u]&(1<<w) or r[w]&(1<<u)) for u,w in combinations(pre,2)):return None
  parents.append(max(pre,key=lambda z:d[z]) if pre else -1)
 kids=[[] for _ in range(n)]
 for v,p in enumerate(parents):
  if p>=0:kids[p].append(v)
 def code(v):return '('+''.join(sorted(code(w) for w in kids[v]))+')'
 return tuple(sorted(code(v) for v,p in enumerate(parents) if p==-1))

def colors(r,n):
 # nested tuples unique across graphs even with different sizes n but fix n
 c=[0]*n
 for _ in range(n+1):
  keys=[(c[i],tuple(sorted(Counter(c[j] for j in range(n) if r[j]>>i&1).items())),tuple(sorted(Counter(c[j] for j in range(n) if r[i]>>j&1).items()))) for i in range(n)]
  distinct=sorted(set(keys))
  mp={k:i for i,k in enumerate(distinct)}
  c=[mp[k] for k in keys]
 return tuple(sorted(c))

def run(n):
 pairs=list(combinations(range(n),2))
 dag=[]
 for bits in range(1<<len(pairs)):
  r=[0]*n
  for k,(i,j) in enumerate(pairs):
   if bits>>k&1:r[i]|=1<<j
  dag.append(tuple(r))
 # normalize refinement codes across all DAGs to avoid graph-local relabeling
 cc=[(0,)*n for _ in dag]
 form=[forest_form(r) for r in dag]
 for t in range(n+2):
  keys=[]
  for r,c in zip(dag,cc):
   keys.append([(c[i],tuple(sorted(Counter(c[j] for j in range(n) if r[j]>>i&1).items())),tuple(sorted(Counter(c[j] for j in range(n) if r[i]>>j&1).items()))) for i in range(n)])
  distinct=sorted({k for row in keys for k in row});mp={k:i for i,k in enumerate(distinct)}
  cc=[tuple(mp[k] for k in row) for row in keys]
  if t+1==n+2:break
 buckets=defaultdict(list)
 for i,c in enumerate(cc):buckets[tuple(sorted(c))].append(i)
 offenders=[]
 for sig,ids in buckets.items():
  forest=[(i,form[i]) for i in ids if form[i] is not None]
  if not forest:continue
  if any(form[i] is None or form[i]!=forest[0][1] for i in ids):
   offenders.append((forest[0][0],next(i for i in ids if form[i] is None or form[i]!=forest[0][1])))
 print('n',n,'DAG topological presentations',len(dag),'forest presentations',sum(f is not None for f in form),'bad buckets',len(offenders))
 if offenders:
  i,j=offenders[0]
  print('  witness forest',dag[i], 'versus',dag[j])
  return False
 return True
for n in range(1,7):
    result=run(n)
    assert result == (n<=5), ('unexpected boundary outcome',n,result)
print('PASS: the DAG boundary is first reached at six vertices')
