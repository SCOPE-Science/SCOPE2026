import itertools, collections, json
EDGES=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
N=12
adj=[0]*N
for u,v in EDGES:adj[u]|=1<<v;adj[v]|=1<<u

def faces():
 out=[]
 for s in range(1,1<<N):
  rem=s;valid=True
  while rem:
   bit=rem&-rem;cc=bit;todo=bit
   while todo:
    b=todo&-todo;todo^=b;u=b.bit_length()-1
    new=adj[u]&s&~cc;cc|=new;todo|=new
   if cc.bit_count()>2:valid=False;break
   rem &=~cc
  if valid:out.append(s)
 return set(out)
BASE=faces()

def morse(F,verbose=False):
 F=set(F);F.discard(0); avail=set(F);pairs=[]
 for v in range(N):
  bit=1<<v
  for a in sorted(F):
   if a not in avail or a&bit: continue
   b=a|bit
   if b in avail:
    avail.remove(a);avail.remove(b);pairs.append((a,b))
 # Full Hasse sort with matched arrows upwards
 matched=set(pairs)
 ins={a:0 for a in F}; outs={a:[] for a in F};edges=0
 for b in F:
  x=b
  while x:
   bit=x&-x;x-=bit;a=b^bit
   if a not in F:continue
   if (a,b) in matched:u,v=a,b
   else:u,v=b,a
   outs[u].append(v);ins[v]+=1;edges+=1
 q=collections.deque(a for a in ins if not ins[a]);seen=0
 while q:
  a=q.popleft();seen+=1
  for b in outs[a]:
   ins[b]-=1
   if ins[b]==0:q.append(b)
 assert seen==len(F),(seen,len(F))
 # Algebraic Morse cancellation over Z on oriented chain groups.
 # Column d[b] indexed by the boundary faces, with orientation ascending labels.
 d={}
 for b in F:
  bd={}; j=0
  for v in range(N):
   bit=1<<v
   if b&bit:
    a=b^bit
    if a in F:bd[a]=1 if j%2==0 else -1
    j+=1
  d[b]=bd
 active=F.copy();pivots=[]
 for a,b in pairs:
  assert a in active and b in active
  coeff=d[b].get(a,0)
  assert abs(coeff)==1,(a,b,coeff)
  bb=d[b]
  for c in list(active):
   if c==b or c.bit_count()!=b.bit_count():continue
   q=d[c].get(a,0)
   if not q:continue
   fac=q*coeff
   for r,z in bb.items():
    val=d[c].get(r,0)-fac*z
    if val:d[c][r]=val
    else:d[c].pop(r,None)
   assert a not in d[c]
  active.discard(a);active.discard(b)
  for c in active:
   d[c].pop(a,None);d[c].pop(b,None)
  pivots.append(coeff)
 for c in active:
  for b,co in d[c].items():
   assert b in active and b.bit_count()==c.bit_count()-1
  check=collections.defaultdict(int)
  for b,co in d[c].items():
   for a,ca in d[b].items():check[a]+=co*ca
  assert all(z==0 for z in check.values()),('boundary squared',c)
 crit=sorted(active,key=lambda m:(m.bit_count(),m))
 result={'face_count':len(F),'hasse_covers':edges,'matched_pairs':len(pairs),'critical_by_dimension':{str(k-1):sum(x.bit_count()==k for x in crit) for k in sorted(set(x.bit_count() for x in crit))},'critical_faces':crit,'morse_differentials':{str(x):[[b,z] for b,z in sorted(d[x].items()) if z] for x in crit if d[x]}}
 assert all(z in active for v in crit for z in d[v])
 return result

if __name__=='__main__':
 data=[]
 for kind,v in [('full',-1)]+[('deletion',i) for i in range(N)]+[('link',i) for i in range(N)]:
  if kind=='full':S=BASE
  elif kind=='deletion':S={f for f in BASE if not(f&(1<<v))}
  else:S={f^(1<<v) for f in BASE if f&(1<<v)}
  r=morse(S);r.update(kind=kind,vertex=v);data.append(r)
  print(kind,v,r['face_count'],r['critical_by_dimension'],r['morse_differentials'],flush=True)
 assert len(data)==25
 assert data[0]['face_count']==824
 exp_del=[2,2,2,1,2,2,1,3,1,2,2,4]
 exp_link=['S2+2S3','S3','S3','point','S3','S3','S2+S3','2S3','S2+S3','S2+2S3','S3','3S3']
 def classify(r):
  cnt={int(k):v for k,v in r['critical_by_dimension'].items()}
  assert cnt.pop(0)==1
  assert set(cnt).issubset({2,3,4})
  bds=r['morse_differentials'];rank=0
  # Every nonzero Morse matrix has a unit entry, so its rank is one.
  if bds:
   assert len({int(s).bit_count() for s in bds})==1
   assert any(abs(co)==1 for entries in bds.values() for _,co in entries)
   rank=1
  if 4 in cnt:
   assert 2 not in cnt and cnt[4]==1
   return '%sS3'%(cnt[3]-rank)
  if 2 in cnt:
   return ('%sS2+'%(cnt[2]-rank) if cnt[2]-rank else '')+('%sS3'%(cnt.get(3,0)-rank) if cnt.get(3,0)-rank else '')
  if cnt.get(3,0):return '%sS3'%cnt[3]
  return 'point'
 assert classify(data[0])=='1S3'
 for i in range(12):assert classify(data[i+1])=='%sS3'%exp_del[i]
 for i in range(12):
  assert classify(data[i+13]).replace('1S2','S2').replace('1S3','S3')==exp_link[i]
 print('MORSE_ALL_25_OK')
