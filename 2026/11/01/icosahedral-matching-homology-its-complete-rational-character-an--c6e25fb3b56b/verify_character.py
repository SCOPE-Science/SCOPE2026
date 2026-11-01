import networkx as nx, itertools, collections, math
G=nx.icosahedral_graph()
E=sorted(tuple(sorted(e)) for e in G.edges())
assert len(E)==30
n=len(G)
faces={0:[()]} # nonempty d maps tuples edges indices
for k in range(1,7):
 arr=[]
 for c in itertools.combinations(range(len(E)),k):
  v=[p for j in c for p in E[j]]
  if len(set(v))==2*k:arr.append(c)
 faces[k]=arr
print('faces sizes', [len(faces[k]) for k in range(7)])
mods=1000003
# sparse Gaussian elimination mod prime
ranks={}
for k in range(1,7):
 rowidx={f:i for i,f in enumerate(faces[k-1])}
 pivots={}
 for c in faces[k]:
  a={rowidx[c[:j]+c[j+1:]]: 1 if j%2==0 else mods-1 for j in range(k)}
  while a:
   t=max(a)
   if t not in pivots:
    z=pow(a[t],-1,mods);pivots[t]={q: v*z%mods for q,v in a.items()};break
   b=pivots[t];factor=a[t]
   for q,v in b.items():
    a[q]=(a.get(q,0)-factor*v)%mods
    if not a[q]:a.pop(q,None)
 ranks[k]=len(pivots)
 print('rank boundary degree',k-1,'->',k-2 if k>=2 else '-1',ranks[k],flush=True)
# Actually faces[k] are k vertices, chain dimension k-1. rank[k] = rank boundary_{k-1}
print('betti reduced',[(len(faces[k])-(ranks.get(k,0)+ranks.get(k+1,0))) for k in range(1,7)])
# group permutations
perms=[tuple(f[i] for i in range(n)) for f in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
perms=sorted(set(perms));assert len(perms)==120
pid={v:i for i,v in enumerate(perms)}
idp=tuple(range(n)); idid=pid[idp]
def comp(f,g):return tuple(f[g[i]] for i in range(n))
def exp(f,k):
 p=idp
 for _ in range(k):p=comp(f,p)
 return p
def order(f):
 p=idp
 for i in range(1,121):
  p=comp(f,p)
  if p==idp:return i
 raise ValueError
orders={p:order(p) for p in perms}
# generate subgroup by ALL odd-order elements
odd=[p for p in perms if orders[p]%2==1]
H={idp};queue=[idp]
while queue:
 f=queue.pop()
 for g in odd:
  h=comp(f,g)
  if h not in H:H.add(h);queue.append(h)
print('H size',len(H), 'ordercounts',collections.Counter(orders[p] for p in H))
# find involution central paired at graph diameter 3, only unique distance3
ant=tuple(next(v for v in range(n) if nx.shortest_path_length(G,u,v)==3) for u in range(n))
print('ant central',ant in perms,all(comp(p,ant)==comp(ant,p) for p in perms))
edgeidx={e:i for i,e in enumerate(E)}
face_sets=[set(faces[k]) for k in range(1,7)]
def sign_x(xs):
 return -1 if sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))%2 else 1
# action on each edge for all permutations
tr={}
for p in perms:
 q=tuple(edgeidx[tuple(sorted((p[u],p[v])))] for (u,v) in E)
 Lef=0; chaintr=[]
 for k in range(1,7):
  t=0
  for f in faces[k]:
   im=[q[i] for i in f]
   if tuple(sorted(im))==f:t+=sign_x(im)
  Lef+=(-1)**(k-1)*t
  chaintr.append(t)
 tr[p]=1-Lef # H3 only, so L=1 - tr(H3)
# group χ summary by epsilon and order in H
cc=collections.defaultdict(list)
for p in perms:
 parity='+' if p in H else '-'
 rot=p if p in H else comp(p,ant)
 cc[(parity,orders[rot])].append(tr[p])
for key,vals in sorted(cc.items()):print('class',key,'size',len(vals),'traces',collections.Counter(vals))
# Brought here chars of Q-rational A5 irreps: [1,4,5,6]
irr={ '1':{1:1,2:1,3:1,5:1},'4':{1:4,2:0,3:1,5:-1},'5':{1:5,2:1,3:-1,5:0},'6':{1:6,2:-2,3:0,5:1}}
# Rational degree6 char inner product gives 2* multiplicity (since complex irr 3 and 3')! divide 2
for s in ('+','-'):
 for t,m in irr.items():
  inner=sum(tr[p]*m[orders[p if p in H else comp(p,ant)]]*(1 if p in H else (1 if s=='+' else -1)) for p in perms)/120
  if t=='6':inner/=2
  if abs(inner)>1e-10:print('MUL',s,t,inner)
print('allchar sum',sum(tr.values()),'invariants',sum(tr.values())/120)
print('E=',E)
assert [len(faces[k]) for k in range(1,7)] == [30,315,1400,2535,1482,125]
assert [ranks[k] for k in range(1,7)] == [1,29,286,1114,1357,125]
assert len(H)==60 and len(perms)==120
assert {(z,k): (len(vals),vals[0]) for (z,k),vals in cc.items()} == {('+',1):(1,64),('+',2):(15,0),('+',3):(20,-2),('+',5):(24,-1),('-',1):(1,16),('-',2):(15,0),('-',3):(20,-2),('-',5):(24,1)}
print('VERIFY_CHARACTER_OK')
expected={('+','1'):0,('+','4'):2,('+','5'):4,('+','6'):2,('-','1'):0,('-','4'):2,('-','5'):2,('-','6'):1}
for s in ('+','-'):
 for t,m in irr.items():
  num=sum(tr[p]*m[orders[p if p in H else comp(p,ant)]] * (1 if p in H or s=='+' else -1) for p in perms)
  den=120*(2 if t=='6' else 1)
  assert num==den*expected[(s,t)],(s,t,num,den)
print('VERIFY_MODULES_OK')
