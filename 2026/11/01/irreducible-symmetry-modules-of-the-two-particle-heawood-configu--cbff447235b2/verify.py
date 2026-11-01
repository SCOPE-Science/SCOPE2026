import itertools, collections, time
start=time.monotonic()
P=tuple(range(1,8)); L=tuple(sorted({tuple(sorted((a,b,a^b))) for a in P for b in P if a<b}))
V=tuple(('p',p) for p in P)+tuple(('l',j) for j in range(7));VI={v:i for i,v in enumerate(V)}
E=tuple(sorted((VI[('p',p)],VI[('l',j)]) for j,line in enumerate(L) for p in line));assert len(E)==21
VV=tuple(itertools.combinations(range(14),2));ONE=tuple((ei,v) for ei,(a,b) in enumerate(E) for v in range(14) if v not in (a,b));TWO=tuple((i,j) for i in range(21) for j in range(i+1,21) if not set(E[i])&set(E[j]));print('cells',len(VV),len(ONE),len(TWO),flush=True)
J0={x:i for i,x in enumerate(VV)};J1={x:i for i,x in enumerate(ONE)};J2={x:i for i,x in enumerate(TWO)};assert (len(VV),len(ONE),len(TWO))==(91,252,168)
def sign(a,b):return 1 if a<b else -1
# d1 boundary of (e,v): (end,v) - (start,v)
d1=[]
for ei,v in ONE:
 a,b=E[ei];d1.append([(J0[tuple(sorted((b,v)))],1),(J0[tuple(sorted((a,v)))],-1)])
# d2 boundary (ei,ej): (b,ej)-(a,ej)-(ei,d)+(ei,c)
d2=[]
for ei,ej in TWO:
 a,b=E[ei];c,d=E[ej];d2.append([(J1[(ej,b)],1),(J1[(ej,a)],-1),(J1[(ei,d)],-1),(J1[(ei,c)],1)])
for col in d2:
 rd=collections.defaultdict(int)
 for k,coef in col:
  for r,x in d1[k]:rd[r]+=x*coef
 assert not any(rd.values())
# calculate modular reduced column echelon using sparse dicts

def echelon(cols,p):
 pivots={};labels={};free=[]
 for j,col in enumerate(cols):
  v=collections.defaultdict(int)
  for i,c in col:v[i]=(v[i]+c)%p
  v={i:x for i,x in v.items() if x%p}
  while v:
   k=min(v)
   if k not in pivots:break
   q=(v[k]*pow(pivots[k][k],-1,p))%p
   for i,c in pivots[k].items():
    t=(v.get(i,0)-q*c)%p
    if t:v[i]=t
    elif i in v:del v[i]
  if not v:free.append(j)
  else:pivots[min(v)]=v;labels[min(v)]=j
 return len(pivots),free
for pp in [2,3,5,101]:
 print('rank',pp,echelon(d1,pp)[0],echelon(d2,pp)[0],flush=True)
# Fano-collineation graph automorphisms and polarity.
GROUP=[]
for a,b,c in itertools.permutations(P,3):
 if c==a^b:continue
 GROUP.append(tuple((a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0) for x in P))
Jline={line:j for j,line in enumerate(L)}
dot=lambda a,b:(a&b).bit_count()%2
normals={line:next(z for z in P if all(dot(z,x)==0 for x in line)) for line in L}
polarity=tuple(VI[('l',Jline[next(line for line in L if normals[line]==p)])] for p in P)+tuple(VI[('p',normals[line])] for line in L)
assert len(set(polarity))==14 and all(polarity[polarity[i]]==i for i in range(14))
def compose(g,h):return tuple(g[h[i]] for i in range(14))
ID=tuple(range(14))
COLOR=[]
for g in GROUP:
 pmap={p:g[p-1] for p in P}
 COLOR.append(tuple(VI[('p',g[p-1])] for p in P)+tuple(VI[('l',Jline[tuple(sorted(pmap[p] for p in line))])] for line in L))
FULL=tuple(COLOR+[compose(polarity,g) for g in COLOR]);assert len(FULL)==len(set(FULL))==336
EMAP={e:i for i,e in enumerate(E)}

def signed_edge_perm(g):
  z=[]
  for a,b in E:
   x,y=g[a],g[b]
   z.append((EMAP[tuple(sorted((x,y)))],sign(x,y)))
  return z

def face_chi(g):
  # full chain traces and H1 graph action
  trv=sum(g[i]==i for i in range(14))
  pem=signed_edge_perm(g)
  tre=sum(sgn for k,(i,sgn) in enumerate(pem) if i==k)
  h1=tre-trv+1
  tr0=sum(tuple(sorted((g[a],g[b])))==(a,b) for a,b in VV)
  tr1=sum(sgn for (ei,v) in ONE for e2,sgn in [pem[ei]] if e2==ei and g[v]==v)
  tr2=0
  for ei,ej in TWO:
   i,si=pem[ei];j,sj=pem[ej]
   if {i,j}=={ei,ej}:
    tr2+=si*sj*(1 if i<j else -1)
  h2=tr0-tr1+tr2-1+h1
  return trv,tre,h1,tr0,tr1,tr2,h2

def order_perm(g):
  h=ID
  for i in range(1,337):
   h=compose(g,h)
   if h==ID:return i
  assert 0
records=collections.defaultdict(list)
for k,g in enumerate(FULL):
 chi=face_chi(g)
 records[(k<168,order_perm(g),chi[2],chi[6])].append(g)
print('H2 character table',flush=True)
for z in sorted(records):print(z,len(records[z]),'C',face_chi(records[z][0]),flush=True)
print('H2 character norm',sum(len(v)*k[3]**2 for k,v in records.items()),'/',336)
print('H2 invariant dim',sum(len(v)*k[3] for k,v in records.items()),'/',336)
print('H1 char norm',sum(len(v)*k[2]**2 for k,v in records.items()),'/',336)
print('H2 total',sum(len(v) for v in records.values()),flush=True)
ADJ={i:set() for i in range(14)}
for a,b in E:ADJ[a].add(b);ADJ[b].add(a)
CYC={}
for a in range(14):
 def dfs(path):
  x=path[-1]
  if len(path)==6:
   if a in ADJ[x]:
    path0=tuple(path)
    cyc=min(tuple(path0[i:]+path0[:i]) for i in range(6))
    rev=tuple(reversed(path0))
    cyc=min(cyc,min(tuple(rev[i:]+rev[:i]) for i in range(6)))
    vec=[]
    for i in range(6):
     u,v=path0[i],path0[(i+1)%6]
     vec.append((EMAP[tuple(sorted((u,v)))],sign(u,v)))
    CYC[cyc]=vec
   return
  for y in ADJ[x]:
   if y not in path:dfs(path+[y])
 dfs([a])
cyc_cols=list(CYC.values());rank6=echelon(cyc_cols,3)[0]
print('six cycles',len(CYC),'span graph H1 rank',rank6,'(needed 8)',flush=True)
assert len(CYC)==28 and rank6==8
# Independent top-kernel representation check modulo 101.
p=101
rows=[[0]*len(TWO) for _ in range(len(ONE))]
for j,col in enumerate(d2):
 for r,v in col:rows[r][j]=(rows[r][j]+v)%p
rank=0;pivcol=[]
for col in range(len(TWO)):
 pivot=next((i for i in range(rank,len(ONE)) if rows[i][col]),None)
 if pivot is None:continue
 rows[rank],rows[pivot]=rows[pivot],rows[rank]
 coeff=pow(rows[rank][col],-1,p)
 rows[rank]=[(x*coeff)%p for x in rows[rank]]
 for i in range(len(ONE)):
  if i==rank:continue
  v=rows[i][col]
  if v:
   rows[i]=[(x-v*y)%p for x,y in zip(rows[i],rows[rank])]
 pivcol.append(col);rank+=1
freecols=[j for j in range(len(TWO)) if j not in pivcol]
assert rank==154 and len(freecols)==14
K=[]
for f in freecols:
 vec=[0]*len(TWO);vec[f]=1
 for i,c in enumerate(pivcol):vec[c]=(-rows[i][f])%p
 for col in d2:
  pass
 z=[0]*len(ONE)
 for j,v in enumerate(vec):
  if v:
   for r,sgn in d2[j]:z[r]=(z[r]+v*sgn)%p
 assert not any(z)
 K.append(vec)
for g in FULL:
 em=signed_edge_perm(g)
 action=[]
 for ei,ej in TWO:
  x,sx=em[ei];y,sy=em[ej]
  action.append((J2[tuple(sorted((x,y)))],sx*sy*(1 if x<y else -1)))
 trace=0
 for f,vec in zip(freecols,K):
  trace+=sum(s*vec[j] for j,(i,s) in enumerate(action) if i==f)
 assert trace%p==face_chi(g)[6]%p,(order_perm(g),trace%p,face_chi(g)[6])
print('INDEPENDENT_KERNEL_CHARACTER_VERIFY_OK for all 336 group elements, 14-vector basis mod 101',flush=True)
# Separate the previously-independent eight-dimensional graph cycle module
# from the 14-dimensional two-particle top homology character.
csq6=0; cross=0;sum6=0
for key,elems in records.items():
 preserve,ordr,h1,h2=key
 u=h2-h1
 csq6+=len(elems)*u*u
 cross+=len(elems)*u*h1
 sum6+=len(elems)*u
assert csq6==336 and cross==0 and sum6==0
print('H2 = V8 plus V6: V8 and V6 are orthogonal absolute irreducible characters; dimensions 8 and 6')
print('VERIFY_OK')
