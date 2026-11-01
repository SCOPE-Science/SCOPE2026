"""Generate a finite proof certificate for a graph-power clique complex.
Only Python standard library is used.
"""
import collections,json,random,pathlib

def graph():
 e=set()
 for i in range(8):
  for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
   e.add(tuple(sorted((a,b))))
 return sorted(e)

def distances():
 adj=[set() for _ in range(16)]
 for u,v in graph():adj[u].add(v);adj[v].add(u)
 result=[]
 for s in range(16):
  ds=[99]*16;ds[s]=0;q=collections.deque([s])
  while q:
   v=q.popleft()
   for w in sorted(adj[v]):
    if ds[w]==99:ds[w]=ds[v]+1;q.append(w)
  result.append(ds)
 return result

def all_faces(r):
 d=distances();close=[sum(1<<j for j in range(16) if j!=i and d[i][j]<=r) for i in range(16)]
 ans=set()
 for m in range(1,65536):
  q=m;ok=True
  while q:
   v=(q&-q).bit_length()-1;q&=q-1
   if q & ~close[v]:ok=False;break
  if ok:ans.add(m)
 return ans

def generate():
 F=all_faces(2);facets={x:[x&~(1<<i) for i in range(16) if x>>i&1] for x in F}
 upper={x:set() for x in F}
 for t,fs in facets.items():
  for f in fs:
   if f in F:upper[f].add(t)
 alive=set(F);rng=random.Random(0);steps=[]
 def remove(x):
  alive.remove(x)
  for f in facets[x]:
   if f in alive:upper[f].remove(x)
 while alive:
  pairs=[(f,next(iter(upper[f]))) for f in alive if len(upper[f])==1 and not upper[next(iter(upper[f]))]]
  if pairs:
   d=max(t.bit_count() for f,t in pairs)
   options=[(f,t) for f,t in pairs if t.bit_count()==d]
   f,t=rng.choice(options)
   remove(f);remove(t);steps.append({'kind':'pair','lower':f,'upper':t})
  else:
   maxima=[t for t in alive if not upper[t]]
   d=max(t.bit_count() for t in maxima)
   t=rng.choice([t for t in maxima if t.bit_count()==d]);remove(t)
   steps.append({'kind':'critical','cell':t})
 return {'graph':'GP(8,3)','vertex_labels':[f'u{i}' for i in range(8)]+[f'v{i}' for i in range(8)],'face_counts':[16,72,112,48], 'steps':steps}

if __name__=='__main__':
 p=pathlib.Path(__file__).parent/'certificates'/'r2_matching.json';p.write_text(json.dumps(generate(),separators=(',',':'),ensure_ascii=False)+'\n')
 print('written',len(generate()['steps']))
