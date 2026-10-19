#!/usr/bin/env python3
"""Direct-closure enumerator with generator-orbit breadth-first distance verification."""
import time,collections,itertools,json,hashlib
from seed_direct import check

def orbit_analysis(d, states, jump, slide):
   ids={t:i for i,t in enumerate(states)};n=1<<d
   digest=hashlib.sha256((''.join(','.join(map(str,s))+'\n' for s in states)).encode()).hexdigest()
   print('SEED_SHA256',d,digest,flush=True)
   actions=[]
   for b in range(d):actions.append([x^(1<<b) for x in range(n)])
   for b in range(d-1):
      p=[]
      for x in range(n):
         v=x;db=(x>>b)&1;eb=(x>>(b+1))&1
         if db!=eb:v^=(1<<b)|(1<<(b+1))
         p.append(v)
      actions.append(p)
   perms=[]
   for m in actions:
     pp=[]
     for t in states:pp.append(ids[tuple(sorted(m[x] for x in t))])
     assert len(set(pp))==len(states)
     perms.append(pp)
   oid=[-1]*len(states);orbits=[]
   for i in range(len(states)):
     if oid[i]>=0:continue
     z=len(orbits);oid[i]=z;todo=[i]
     for u in todo:
       for pp in perms:
         v=pp[u]
         if oid[v]<0:oid[v]=z;todo.append(v)
     orbits.append(todo)
   print('ORBITS',d,'sizes',[(len(c),states[c[0]]) for c in orbits],flush=True)
   def bfs(source,g):
     dist=[-1]*len(g);dist[source]=0;todo=[source]
     for v in todo:
       z=dist[v]+1
       for w in g[v]:
         if dist[w]<0:dist[w]=z;todo.append(w)
     return collections.Counter(dist),max(dist)
   ans={}
   for name,g in [('jump',jump),('slide',slide)]:
     results=[]
     for idx,c in enumerate(orbits):
       v=c[0]; layer,ecc=bfs(v,g)
       results.append(dict(size=len(c),example=states[v],degree=len(g[v]),eccentricity=ecc,layers=[layer[x] for x in range(ecc+1)]))
       print(name,idx,results[-1],flush=True)
     ans[name]=dict(edges=sum(map(len,g))//2,orbit_representatives=results,ecc_distribution=dict(sorted(collections.Counter({e:sum(r['size'] for r in results if r['eccentricity']==e) for e in set(x['eccentricity'] for x in results)}).items())))
   print("MACHINE_SUMMARY",d,json.dumps(ans,sort_keys=True))
if __name__=='__main__':
 t=time.monotonic()
 for d in [4,5]:
  s,j,sl=check(d);orbit_analysis(d,s,j,sl)

