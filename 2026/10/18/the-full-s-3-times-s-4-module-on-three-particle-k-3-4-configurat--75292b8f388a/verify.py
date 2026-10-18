import itertools, collections, functools
from collections import defaultdict
A=tuple(range(3));B=tuple(range(3,7));V=A+B
E=[(i,j) for i in A for j in B];eid={e:i for i,e in enumerate(E)};ne=len(E)
incident={v:sorted(i for i,e in enumerate(E) if v in e) for v in V}
loc={v:[(incident[v][k],incident[v][0]) for k in range(1,len(incident[v]))] for v in V}
def expmon(s,n=ne):
 if n==1:yield(s,);return
 for k in range(s+1):
  for x in expmon(s-k,n-1):yield (k,)+x
def basis(k):
 return [(subset,inds,exps) for subset in itertools.combinations(V,k) for inds in itertools.product(*(range(len(loc[v])) for v in subset)) for exps in expmon(3-k)]
bases=[basis(k) for k in range(4)];idx=[{x:i for i,x in enumerate(b)} for b in bases];print('SIZES',list(map(len,bases)),flush=True)
def boundary(k):
 cols=[]
 for ss,inds,ex in bases[k]:
  dd=defaultdict(int)
  for j,v in enumerate(ss):
   f,b=loc[v][inds[j]];nss=ss[:j]+ss[j+1:];ninds=inds[:j]+inds[j+1:]
   for edge,c in ((f,1),(b,-1)):
    nexp=list(ex);nexp[edge]+=1;dd[idx[k-1][(nss,ninds,tuple(nexp))]]+=c*(-1)**j
  cols.append({r:c for r,c in dd.items() if c})
 return cols
mat={k:boundary(k) for k in range(1,4)}
def rankmod(cols,p):
 piv={}
 for col in cols:
  v={r:c%p for r,c in col.items() if c%p}
  while v:
   j=min(v)
   if j not in piv:
    a=pow(v[j],-1,p);piv[j]={r:c*a%p for r,c in v.items() if c*a%p};break
   coeff=v[j]
   for r,c in piv[j].items():
    w=(v.get(r,0)-coeff*c)%p
    if w:v[r]=w
    else:v.pop(r,None)
 return len(piv)
for p in (2,3,101):
 rr=[rankmod(mat[k],p) for k in range(1,4)]
 assert rr==([363,956,491] if p==2 else [363,957,491])
 print('RANK',p,rr,flush=True)
S3=list(itertools.permutations(range(3)));S4=list(itertools.permutations(range(4)))
autos=[(a,b,tuple(a)+tuple(3+x for x in b)) for a in S3 for b in S4]
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def cyc(p):
 seen=set();ls=[]
 for x in range(len(p)):
  if x not in seen:
   n=0;j=x
   while j not in seen:seen.add(j);j=p[j];n+=1
   ls.append(n)
 return tuple(sorted(ls,reverse=True))
@functools.lru_cache(maxsize=None)
def cmap(g):
 ep=tuple(eid[tuple(sorted((g[u],g[v])))] for u,v in E);L={}
 for v in V:
  vv=g[v];base=incident[vv][0];target=incident[vv][1:]
  for i,(f,b) in enumerate(loc[v]):
   d=defaultdict(int)
   for e,c in ((ep[f],1),(ep[b],-1)):
    if e!=base:d[target.index(e)]+=c
   L[(v,i)]={z:c for z,c in d.items() if c}
 return ep,L
def chaintr(g):
 ep,L=cmap(g);out=[]
 for k in range(4):
  tot=0
  for ss,ids,ex in bases[k]:
   if tuple(sorted(g[v] for v in ss))!=ss:continue
   nx=[0]*ne
   for e,c in enumerate(ex):nx[ep[e]]=c
   if tuple(nx)!=ex:continue
   prod=(-1)**sum(g[ss[i]]>g[ss[j]] for i in range(k) for j in range(i+1,k))
   for v,i in zip(ss,ids):prod*=L[(v,i)].get(ids[ss.index(g[v])],0)
   tot+=prod
  out.append(tot)
 return out
def ch1(g):
 return sum(g[v]==v for v in V)*(-1)+1+sum(eid[tuple(sorted((g[u],g[v]))) ]==j for j,(u,v) in enumerate(E))
data=[]
for a,b,g in autos:
 tr=chaintr(g);h1=ch1(g);h2=sum((-1)**k*tr[k] for k in range(4))-1+h1;data.append((a,b,g,tr,h1,h2))
rep={}
for a,b,g,tr,h1,h2 in data:
 key=(cyc(a),cyc(b))
 if key in rep:assert rep[key]==(h1,h2)
 rep[key]=(h1,h2)
print('CLASSES',len(rep),flush=True)
for k,v in sorted(rep.items(),key=str):print('CLASS',k,v,flush=True)
# S4 irreducible chars: T, sign, standard, sign*standard, matching-augmentation 2D
T3={'T':lambda p:1,'S':lambda p:sign(p),'U':lambda p:sum(p[i]==i for i in range(3))-1}
matchings=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))]
def U4(p):return sum(i==p[i] for i in range(4))-1
def M4(p):return sum(frozenset(frozenset(p[x] for x in pair) for pair in matching)==matching for matching in matchings)-1
T4={'T':lambda p:1,'S':lambda p:sign(p),'V':U4,'VS':lambda p:sign(p)*U4(p),'M':M4}
reps={}
for a_name,f in T3.items():
 for b_name,h in T4.items():
  vals=[f(a)*h(b) for a,b,*_ in data]
  dot=sum(v*d[-1] for v,d in zip(vals,data))
  assert dot%144==0
  reps[a_name+b_name]=(vals,dot//144)
print('REP_MULTS',[(k,v[0][0],v[1]) for k,v in reps.items()],flush=True)
expected={'SV':1,'SVS':1,'SM':2,'US':1,'UV':1,'UVS':1,'UM':1}
assert {k:v[1] for k,v in reps.items() if v[1]}==expected
assert all(sum(x*y for x,y in zip(u[0],v[0]))==(144 if k==l else 0) for k,u in reps.items() for l,v in reps.items())
print('CHAR_ORTHOGONAL_OK',flush=True)
# Independent trace via vertex and edge orbit cycle formula.
def permcyc(elements,f):
 seen=set();out=[]
 for x in elements:
  if x in seen:continue
  y=x;cc=[]
  while y not in seen:seen.add(y);cc.append(y);y=f(y)
  assert y==x;out.append(cc)
 return out
def mul(a,b):return [sum(a[j]*b[i-j] for j in range(max(0,i-len(b)+1),min(i,len(a)-1)+1)) for i in range(4)]
def orbittrace(g):
 ep,L=cmap(g);a=[1,0,0,0]
 for o in permcyc(range(ne),lambda i:ep[i]):
  a=mul(a,[int(i%len(o)==0) for i in range(4)])
 for o in permcyc(V,lambda v:g[v]):
  v=o[0];LENGTH=len(o);fix=0
  for e in incident[v]:
   f=e
   for j in range(LENGTH):f=ep[f]
   fix+=int(f==e)
  factor=[1,0,0,0]
  if LENGTH<=3:factor[LENGTH]=-(fix-1)
  a=mul(a,factor)
 return a[3]
for a,b,g,tr,h1,h2 in data:assert orbittrace(g)==sum((-1)**k*tr[k] for k in range(4))
print('ORBIT_TRACE_OK',flush=True)
def action(k,g,lab):
 ss,ids,ex=lab;ep,L=cmap(g);nss=tuple(sorted(g[v] for v in ss))
 prod={(): (-1)**sum(g[ss[i]]>g[ss[j]] for i in range(k) for j in range(i+1,k))}
 for v,i in zip(ss,ids):
  nxt=defaultdict(int)
  for old,c in prod.items():
   for j,z in L[(v,i)].items():nxt[old+((g[v],j),)]+=c*z
  prod=nxt
 nex=[0]*ne
 for i,z in enumerate(ex):nex[ep[i]]=z
 out=defaultdict(int)
 for tuples,c in prod.items():
  d=dict(tuples);newids=tuple(d[v] for v in nss)
  out[idx[k][(nss,newids,tuple(nex))]]+=c
 return {r:c for r,c in out.items() if c}
def compose(k,col):
 out=defaultdict(int)
 for j,c in col.items():
  for i,z in mat[k][j].items():out[i]+=c*z
 return {j:c for j,c in out.items() if c}
for k in (2,3):
 for col in mat[k]:assert not compose(k-1,col)
print('D_SQUARED_ZERO',flush=True)
gens=[]
for a,b,g,tr,h1,h2 in data:
 ca=cyc(a);cb=cyc(b)
 if (a==S3[0] and sum(b[i]!=i for i in range(4))==2) or (b==S4[0] and sum(a[i]!=i for i in range(3))==2):gens.append((a,b,g))
assert len(gens)==9
for a,b,g in gens:
 for k in (1,2,3):
  for i,col in enumerate(mat[k]):
   left=defaultdict(int);right=defaultdict(int)
   for x,c in col.items():
    for y,d in action(k-1,g,bases[k-1][x]).items():left[y]+=c*d
   for x,c in action(k,g,bases[k][i]).items():
    for y,d in mat[k][x].items():right[y]+=c*d
   assert {x:y for x,y in left.items() if y}=={x:y for x,y in right.items() if y}
print('ALL_GENERATOR_EQUIVARIANCE_OK',len(gens),flush=True)
print('VERIFY_OK',flush=True)
