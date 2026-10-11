from itertools import combinations,permutations,product
from collections import Counter,defaultdict
n=4
facets=[]
for v in range(1<<n):
 for i in range(n):
  w=v^(1<<i)
  if v>w:continue
  S=set()
  for u in (v,w):
   S.add(u)
   for j in range(n): S.add(u^(1<<j))
  facets.append(tuple(sorted(S)))
faces=defaultdict(set)
for f in facets:
 for k in range(1,9):faces[k].update(combinations(f,k))

def invperm(v,p):return sum(((v>>i)&1)<<p[i] for i in range(n))
def sign_perm(a,b):
 t={x:i for i,x in enumerate(a)}
 z=[t[x] for x in b]
 return -1 if sum(z[i]>z[j] for i in range(len(z)) for j in range(i+1,len(z)))%2 else 1

def lef(g):
 L=0
 for k,ss in faces.items():
  for f in ss:
   mapped=tuple(g[x] for x in f)
   if set(mapped)==set(f):
    L+= (-1)**(k-1)*sign_perm(tuple(sorted(mapped)),mapped)
 return L-1  # reduced

def signed_type(p,b):
 cycles=[];used=set()
 for i in range(n):
  if i in used: continue
  cur=[];j=i
  while j not in used:
   used.add(j);cur.append(j);j=p[j]
  cycles.append((len(cur),sum((b>>x)&1 for x in cur)%2))
 return tuple(sorted(cycles))
q=Counter();classdata={}
for p in permutations(range(n)):
 for b in range(1<<n):
  g=tuple(invperm(v,p)^b for v in range(1<<n))
  cl=signed_type(p,b)
  t=lef(g)
  if cl not in classdata:classdata[cl]=t
  assert classdata[cl]==t
  q[cl]+=1
print('N_CLASSES',len(q))
for cl in sorted(q):print(cl,'count',q[cl],'L',classdata[cl])
print('irreps 1d')
for parityb, parityp in product([0,1], repeat=2):
 tot=0
 for p in permutations(range(n)):
  ps= (-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
  for b in range(1<<n):
   cl=signed_type(p,b)
   chi= (-1)**(parityb*(b.bit_count()%2)) * (ps if parityp else 1)
   tot+=classdata[cl]*chi
 print((parityb,parityp),tot,'/384=',tot/384)
import itertools, math
S={
 0:{():{():1}},
 1:{(1,):{(1,):1}},
 2:{(2,):{(1,1):1,(2,):1},(1,1):{(1,1):1,(2,):-1}},
 3:{(3,):{(1,1,1):1,(2,1):1,(3,):1},(2,1):{(1,1,1):2,(2,1):0,(3,):-1},(1,1,1):{(1,1,1):1,(2,1):-1,(3,):1}},
 4:{(4,):{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},(3,1):{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},(2,2):{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0},(2,1,1):{(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},(1,1,1,1):{(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1}}
}
def irreps_ch(lam,mu,cl):
 out=0
 for select in itertools.product([0,1], repeat=len(cl)):
  if sum(c[0] for c,b in zip(cl,select) if b==0)!=sum(lam):continue
  a=tuple(sorted((c[0] for c,b in zip(cl,select) if b==0),reverse=True))
  b=tuple(sorted((c[0] for c,b in zip(cl,select) if b==1),reverse=True))
  s=(-1)**sum(c[1] for c,b in zip(cl,select) if b==1)
  out+=s*S[sum(lam)][lam][a]*S[sum(mu)][mu][b]
 return out

def det(cl):return (-1)**(sum(c[1]+c[0]-1 for c in cl))
char4={cl:L+det(cl) for cl,L in classdata.items()}
chi3={cl:det(cl) for cl in classdata}
print('H4 char',[(cl,char4[cl]) for cl in sorted(q)])
print('Irreducible decomposition:')
for a in range(5):
 b=4-a
 for lam in S[a]:
  for mu in S[b]:
   numerator=sum(q[cl]*char4[cl]*irreps_ch(lam,mu,cl) for cl in q)
   assert numerator%384==0,(lam,mu,numerator)
   m=numerator//384
   degree=irreps_ch(lam,mu,tuple([(1,0)]*4))
   if m:print((lam,mu),'multiplicity',m,'degree',degree)


# Separate exact mod-two boundary-rank reconstruction, independent of traces.
from itertools import combinations
from collections import defaultdict

def faces_cech4():
 F=[]
 for v in range(16):
  for bit in range(4):
   w=v^(1<<bit)
   if v>w: continue
   nodes=set()
   for u in (v,w):
    nodes.add(u)
    for i in range(4): nodes.add(u^(1<<i))
   F.append(tuple(sorted(nodes)))
 assert len(F)==32 and len(set(F))==32
 faces=defaultdict(set)
 for facet in F:
  for k in range(1,9):faces[k-1].update(combinations(facet,k))
 return {k:sorted(v) for k,v in faces.items()}

def rank2(columns):
 pivot={}
 for col in columns:
  while col:
   i=col.bit_length()-1
   if i in pivot:col ^= pivot[i]
   else:pivot[i]=col;break
 return len(pivot)

def verify():
 fs=faces_cech4()
 rank={0:0,8:0}
 for d in range(1,8):
  idx={s:i for i,s in enumerate(fs[d-1])}
  cols=[]
  for s in fs[d]:
   c=0
   for sub in combinations(s,d):c^=1<<idx[sub]
   cols.append(c)
  rank[d]=rank2(cols)
 bettis={d:len(fs[d])-rank.get(d,0)-rank.get(d+1,0)-(d==0) for d in fs}
 print('face counts',[(d,len(fs[d])) for d in fs])
 print('boundary ranks over F2',rank)
 print('reduced bettis F2',bettis)
 assert bettis=={0:0,1:0,2:0,3:1,4:24,5:0,6:0,7:0}
 print('VERIFY_HOMOLOGY_OK')

# Reconstruct the full rational character table and test pairwise orthogonality.
reps=[(a,b) for k in range(5) for a in S[k] for b in S[4-k]]
assert len(reps)==20 and len(q)==20 and sum(q.values())==384
for i,rr in enumerate(reps):
 for j,ss in enumerate(reps):
  scalar=sum(q[c]*irreps_ch(*rr,c)*irreps_ch(*ss,c) for c in q)
  assert scalar==384*int(i==j),(i,j,scalar)
assert sum(irreps_ch(*r,((1,0),)*4)**2 for r in reps)==384
assert sum(q[c]*char4[c] for c in q)==384*0
assert sum(q[c]*det(c) for c in q)==0
assert [char4[c] for c in sorted(q)]==[24,6,-4,4,4,-6,-2,-2,0,0,0,0,0,0,0,0,0,0,0,0]
assert [(a,b) for a,b in reps if sum(q[c]*char4[c]*irreps_ch(a,b,c) for c in q)==384] == [((2,), (2,)), ((2,), (1, 1)), ((3,), (1,)), ((2,1), (1,))]
verify()
print('VERIFY_OK: 384 group elements, 20 signed classes, complete character orthogonality, mod-two ranks')
