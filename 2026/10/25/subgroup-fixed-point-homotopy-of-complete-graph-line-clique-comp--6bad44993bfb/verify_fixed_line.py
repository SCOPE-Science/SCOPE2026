import itertools, collections

def closure(n,gens):
 ident=tuple(range(n)); G={ident};todo=[ident]
 while todo:
  p=todo.pop()
  for g in gens:
   q=tuple(p[g[i]] for i in range(n))
   if q not in G:G.add(q);todo.append(q)
 return G

def orbit_partition(domain, G, act):
 unseen=set(domain); orbs=[]
 while unseen:
  x=min(unseen);o=frozenset(act(g,x) for g in G); assert o<=unseen
  unseen-=o;orbs.append(o)
 return orbs

def gf2_rank(cols):
 piv={}
 for x in cols:
  while x:
   k=x.bit_length()-1
   if k not in piv:piv[k]=x;break
   x^=piv[k]
 return len(piv)

def compute(n,gens):
 G=closure(n,gens); E=list(itertools.combinations(range(n),2))
 orbs=orbit_partition(E,G,lambda g,e:tuple(sorted((g[e[0]],g[e[1]]))))
 vo=orbit_partition(range(n),G,lambda g,x:g[x]);a=sum(len(o)==1 for o in vo);b=sum(len(o)==2 for o in vo);c=sum(len(o)==3 for o in vo)
 permitted=[o for o in orbs if all(len(set(e)&set(f))>0 for e,f in itertools.combinations(o,2))]
 edges=list(range(len(permitted)))
 comp=lambda o,p:all(len(set(e)&set(f))>0 for e in o for f in p)
 adj={i:{j for j in edges if j!=i and comp(permitted[i],permitted[j])} for i in edges}
 faces_by={}
 def cliques(prefix,candidates):
  if prefix:faces_by.setdefault(len(prefix)-1,[]).append(tuple(prefix))
  for idx,v in enumerate(candidates):cliques(prefix+[v],[w for w in candidates[idx+1:] if w in adj[v]])
 cliques([],edges)
 dims={k:len(v) for k,v in faces_by.items()};bound={};
 for k in sorted(faces_by):
  if not k: continue
  prev={f:i for i,f in enumerate(faces_by[k-1])}
  cols=[sum(1<<prev[f[:i]+f[i+1:]] for i in range(len(f))) for f in faces_by[k]]
  bound[k]=gf2_rank(cols)
 betti={k:dims[k]-bound.get(k,0)-bound.get(k+1,0) for k in dims}
 if betti: betti[0]-=1
 prediction={0:c if a else b+c-1,1:b*(a-1) if a else 0,2:max(0,(a-1)*(a-2)*(a-3)//6) if a else 0}
 if not permitted:prediction={-1:1};betti={-1:1}
 if {k:v for k,v in betti.items() if v}!={k:v for k,v in prediction.items() if v}:
  raise ValueError((n,gens,a,b,c,betti,prediction,orbs,permitted))
 return (n,len(G),a,b,c,len(permitted),sum(dims.values()))

cases=0
for n in range(3,8):
 perms=list(itertools.permutations(range(n)))
 typ={}
 for p in perms:
  x=tuple(sorted(len(o) for o in orbit_partition(range(n),closure(n,[p]),lambda g,x:g[x])))
  if x not in typ:typ[x]=p
 for p in typ.values():
  if n<=6 or len(closure(n,[p]))<=3:
   r=compute(n,[p]);print('single',r);cases+=1
 if n<=6:
  P=list(typ.values());
  for p in P:
   for q in P:
    if len(closure(n,[p,q]))<=100:
     compute(n,[p,q]);cases+=1
print('ALL',cases,'SUBGROUP SAMPLE CASES PASSED')
