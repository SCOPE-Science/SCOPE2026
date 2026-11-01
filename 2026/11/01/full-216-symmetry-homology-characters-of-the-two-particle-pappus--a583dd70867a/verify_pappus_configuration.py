"""Exact cubical-chain and automorphism checks for two unordered particles on the Pappus graph.
Requires Python 3 and networkx. Run: python verify_pappus_configuration.py
"""
import networkx as nx, collections, itertools
G=nx.LCF_graph(18,[5,7,-7,7,-7,-5],3)
V=18;E=sorted(tuple(sorted(e))for e in G.edges()); ei={e:i for i,e in enumerate(E)}
verts=list(range(V)); cells0=list(itertools.combinations(verts,2)); c0={x:i for i,x in enumerate(cells0)}
cells1=[(i,v)for i,(a,b) in enumerate(E) for v in verts if v!=a and v!=b]; c1={x:i for i,x in enumerate(cells1)}
cells2=[(i,j)for i,(a,b) in enumerate(E) for j,(c,d) in enumerate(E) if i<j and len({a,b,c,d})==4]; c2={x:i for i,x in enumerate(cells2)}
assert (len(cells0),len(cells1),len(cells2))==(153,432,297)

def b1(e,v):
 a,b=E[e]
 return [ (1,c0[tuple(sorted((b,v)))]),(-1,c0[tuple(sorted((a,v)))]) ]
def b2(i,j):
 a,b=E[i];c,d=E[j]
 return [(1,c1[(j,b)]),(-1,c1[(j,a)]),(-1,c1[(i,d)]),(1,c1[(i,c)])]
# exact boundary squared zero
for (i,j) in cells2:
 s=collections.Counter()
 for coef,row in b2(i,j):
  e,v=cells1[row]
  for cf,r in b1(e,v):s[r]+=coef*cf
 assert all(x==0 for x in s.values())

def f2rank(cols):
 piv={}
 for col in cols:
  while col:
   v=(col&-col).bit_length()-1
   if v not in piv:piv[v]=col;break
   col^=piv[v]
 return len(piv)
r1=f2rank([sum(1<<r for c,r in b1(*x))for x in cells1])
r2=f2rank([sum(1<<r for c,r in b2(*x))for x in cells2])
print('cells',len(cells0),len(cells1),len(cells2),'F2 ranks',r1,r2,'betti',len(cells0)-r1,len(cells1)-r1-r2,len(cells2)-r2)
# A canonical graph cycle generator has a configuration lift keeping any unused spectator vertex fixed
T=nx.bfs_tree(G,0).to_undirected()
non_tree=sorted(set(E)-set(tuple(sorted(e))for e in T.edges()))
assert len(non_tree)==len(E)-len(G)+1==10
for a,b in non_tree:
 path=nx.shortest_path(T,a,b)
 spectator=next((v for v in verts if v not in path),None)
 assert spectator is not None
 chain=collections.Counter()
 traversal=list(zip(path,path[1:]))+[(b,a)]
 for u,v in traversal:
  idx=ei[tuple(sorted((u,v)))];chain[(idx,spectator)]+= (1 if u<v else -1)
 bd=collections.Counter()
 for (i,v),coef in chain.items():
  for cf,r in b1(i,v):bd[r]+=coef*cf
 assert all(x==0 for x in bd.values())
print('10 independent graph fundamental cycles lift with stationary spectators')
Aut=sorted(tuple(mp[x]for x in verts)for mp in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
I=tuple(verts)
def compose(p,q):return tuple(p[q[i]] for i in verts)
def inverse(p):
 o=[0]*V
 for i,j in enumerate(p):o[j]=i
 return tuple(o)
def cycle_type(perm):
 seen=set();ls=[]
 for i in range(len(perm)):
  if i in seen:continue
  j=i;l=0
  while j not in seen:seen.add(j);l+=1;j=perm[j]
  ls.append(l)
 return tuple(sorted(ls,reverse=True))
def aut_order(p):
 q=I;k=0
 while True:
  q=compose(p,q);k+=1
  if q==I:return k
classes=[];un=set(Aut)
while un:
 p=min(un)
 cl={compose(compose(h,p),inverse(h))for h in Aut}
 assert cl<=un
 un-=cl;classes.append((p,cl))

def char_of(p):
 eperm=[];esign=[]
 for a,b in E:
  x,y=p[a],p[b]
  eperm.append(ei[tuple(sorted((x,y)))]);esign.append(1 if x<y else -1)
 t0=sum(1 for a,b in cells0 if tuple(sorted((p[a],p[b])))==(a,b))
 t1=0
 for i,v in cells1:
  if eperm[i]==i and p[v]==v:t1+=esign[i]
 t2=0
 for i,j in cells2:
  a,b=eperm[i],eperm[j]
  if tuple(sorted((a,b)))==(i,j):
   t2+=esign[i]*esign[j]*(1 if a<b else -1)
 # H1 graph: trace on C1 - trace on C0 + 1
 graph_c0=sum(p[v]==v for v in verts)
 graph_c1=sum(esign[i] for i,j in enumerate(eperm) if i==j)
 h1=graph_c1-graph_c0+1
 h2=t0-t1+t2-1+h1
 return (h1,h2,t0,t1,t2),eperm,esign
vals={p:char_of(p)[0]for p in Aut}
class_rows=[]
for idx,(p,cl) in enumerate(classes,1):
 assert len({vals[h]for h in cl})==1
 val=vals[p]
 ep=char_of(p)[1]
 class_rows.append({'id':idx,'size':len(cl),'order':aut_order(p),'vertex_cycles':cycle_type(p),'edge_cycles':cycle_type(ep),'h1':val[0],'h2':val[1],'traces':val[2:],'rep':list(p)})
print('group',len(Aut),'classes',len(classes),'class table')
for c in class_rows:print(c['id'],c['size'],c['order'],c['vertex_cycles'],c['edge_cycles'],'H1',c['h1'],'H2',c['h2'])
print('invariants H1',sum(r['size']*r['h1'] for r in class_rows)/len(Aut),'H2',sum(r['size']*r['h2']for r in class_rows)/len(Aut))
print('Euler / identity',vals[I])
print('H1 norm',sum(r['size']*r['h1']**2 for r in class_rows)/len(Aut),'H2 norm',sum(r['size']*r['h2']**2 for r in class_rows)/len(Aut))
def frank(cols,p):
 piv={}
 for col in cols:
  vec={row:cf%p for cf,row in col if cf%p}
  while vec:
   i=min(vec)
   if i not in piv:
    # normalize pivot
    aa=pow(vec[i],-1,p)
    piv[i]={k:aa*v%p for k,v in vec.items()}
    break
   a=vec[i]
   for k,x in piv[i].items():
    val=(vec.get(k,0)-a*x)%p
    if val:vec[k]=val
    else:vec.pop(k,None)
 return len(piv)
for prime in (3,5,101):
 rp=frank([b2(*x)for x in cells2],prime)
 print('mod',prime,'rank d2',rp,'H1',len(cells1)-r1-rp,'H2',len(cells2)-rp)
color=nx.algorithms.bipartite.color(G)
P=[p for p in Aut if all(color[p[v]]==color[v] for v in verts)]
print('bip-preserving group',len(P),'invariants',sum(vals[p][0] for p in P)/len(P),sum(vals[p][1] for p in P)/len(P))
for c in class_rows:
 p=tuple(c['rep'])
 c['preserves_bipartition']=all(color[p[v]]==color[v] for v in verts)
print('bip table',[(c['id'],c['size'],c['preserves_bipartition']) for c in class_rows])
# Every cellular action commutes with both boundary maps; verify signed coefficients for each 216 group elements.
def act0(p,x):return (1,c0[tuple(sorted((p[x[0]],p[x[1]])))])
def act1(p,x):
 i,v=x; a,b=E[i];u,w=p[a],p[b]
 return (1 if u<w else -1,c1[(ei[tuple(sorted((u,w)))],p[v])])
def act2(p,x):
 i,j=x;a,b=E[i];c,d=E[j]
 e,f=p[a],p[b];h,k=p[c],p[d]
 ii=ei[tuple(sorted((e,f)))];jj=ei[tuple(sorted((h,k)))]
 s=(1 if e<f else -1)*(1 if h<k else -1)*(1 if ii<jj else -1)
 return s,c2[tuple(sorted((ii,jj)))]
for p in Aut:
 for x in cells1:
  s,j=act1(p,x);lhs=collections.Counter()
  for c,r in b1(*cells1[j]):lhs[r]+=s*c
  rhs=collections.Counter()
  for c,r in b1(*x):
   s2,t=act0(p,cells0[r]);rhs[t]+=c*s2
  assert all(lhs[r]==rhs[r] for r in lhs.keys()|rhs.keys())
 for x in cells2:
  s,j=act2(p,x);lhs=collections.Counter()
  for c,r in b2(*cells2[j]):lhs[r]+=s*c
  rhs=collections.Counter()
  for c,r in b2(*x):
   s2,t=act1(p,cells1[r]);rhs[t]+=c*s2
  assert all(lhs[r]==rhs[r] for r in lhs.keys()|rhs.keys())
print('exact signed cellular equivariance verified for all 216 automorphisms and all nonzero boundary incidences')
print('VERIFY_OK')
