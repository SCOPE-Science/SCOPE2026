import itertools,collections,functools,time,hashlib,json
P=list(itertools.permutations(range(3)))
E=(0,1,2);pindex={p:i for i,p in enumerate(P)}
def mul(a,b): return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
conj=lambda t,a:mul(mul(t,a),inv(t))
cl={p: 0 if p==E else 1 if mul(p,p)==E else 2 for p in P}
cls=[cl[p] for p in P]
atoms=[('eq',i,j) for i in range(4) for j in range(i+1,4)]+[('mul',i,j,k) for i in range(4) for j in range(4) for k in range(4)]
ALL=(1<<len(atoms))-1
@functools.lru_cache(None)
def mask(a,b,c):
 v=[E,a,b,c]
 return sum(1<<k for k,t in enumerate(atoms) if (v[t[1]]==v[t[2]] if t[0]=='eq' else mul(v[t[1]],v[t[2]])==v[t[3]]))
canonpair={};reps=[]
for a in P:
 for b in P:
  orbit=[(conj(t,a),conj(t,b)) for t in P]
  rep=min(orbit,key=lambda ab:(pindex[ab[0]],pindex[ab[1]]))
  if rep not in reps:reps.append(rep)
  canonpair[a,b]=rep
reps.sort(key=lambda ab:(pindex[ab[0]],pindex[ab[1]]))
T=len(reps)
marg=[cl[a] for a,b in reps]
choices=[sorted(set(mask(a,b,c) for c in P)) for a,b in reps]
print('local pair orbit types',T,'marg',marg,'extension choice sizes',[len(t) for t in choices],flush=True)
@functools.lru_cache(None)
def extension(counts):
 if sum(counts)==0:return frozenset([ALL])
 i=next(j for j,x in enumerate(counts) if x)
 p=list(counts);p[i]-=1
 return frozenset(a&b for a in extension(tuple(p)) for b in choices[i])
def compositions(n,d):
 if d==1:yield(n,);return
 for i in range(n+1):
  for rest in compositions(n-i,d-1):yield(i,)+rest
signatures={}
for n in range(1,6):
 t0=time.monotonic()
 profiles_by_x=collections.defaultdict(set)
 for tcounts in compositions(n,T):
  xcounts=tuple(sum(tcounts[j] for j in range(T) if marg[j]==c) for c in range(3))
  profiles_by_x[xcounts].add(extension(tcounts))
 signatures[n]=frozenset(frozenset(s) for s in profiles_by_x.values())
 eq=[m for m in range(1,n) if signatures[m]==signatures[n]]
 canonical=tuple(sorted(tuple(sorted(tuple(sorted(msk)) for msk in pptype)) for pptype in signatures[n]))
 h=hashlib.sha256(json.dumps(canonical,separators=(',',':')).encode()).hexdigest()
 print('n',n,'#pointed types',len(signatures[n]),'#pair orbit profiles',sum(len(v) for v in profiles_by_x.values()),'#pair masks',sum(len(p) for vs in profiles_by_x.values() for p in vs),'previous eq',eq,'SHA256 canonical',h,'time',round(time.monotonic()-t0,2),flush=True)
assert [len(signatures[j]) for j in range(1,6)]==[3,6,9,10,10]
assert len(set(signatures[j] for j in range(1,5)))==4
assert signatures[4]==signatures[5]
print('PASS: exactly four rank-three theory types n=1,2,3,>=4 via product preservation')
