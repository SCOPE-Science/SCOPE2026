"""Exact cellular and equivariant verification for the two-point icosahedral graph configuration space.
Only Python 3 standard-library modules are used.
"""
import itertools, collections, json, hashlib
V=tuple(range(12))
E=[(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),(4,6),
(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),
(9,10),(10,11)]
E=sorted(E);EI={x:i for i,x in enumerate(E)}
adj={v:set() for v in V}
for a,b in E:adj[a].add(b);adj[b].add(a)
assert len(E)==30 and all(len(adj[v])==5 for v in V)

def automorphisms():
    order=[0];seen={0}
    for v in order:
        for w in sorted(adj[v]):
            if w not in seen:order.append(w);seen.add(w)
    assert len(order)==len(V)
    assigned={};used=set();res=[]
    def visit(k):
        if k==len(order):res.append(dict(assigned));return
        u=order[k]
        for v in V:
            if v in used:continue
            if all((w in adj[u])==(t in adj[v]) for w,t in assigned.items()):
                assigned[u]=v;used.add(v);visit(k+1);used.remove(v);del assigned[u]
    visit(0)
    return res

F=sorted(tuple(x) for x in itertools.combinations(V,3) if all(b in adj[a] for a,b in itertools.combinations(x,2)))
print('E',len(E),'F',len(F))
Fpair=sorted((i,j) for i in range(len(F)) for j in range(i+1,len(F)) if not(set(F[i])&set(F[j])))
print('face pairs',len(Fpair))
C0=list(itertools.combinations(V,2)); I0={v:i for i,v in enumerate(C0)}
C1=sorted((i,v) for i,e in enumerate(E) for v in V if v not in e); I1={v:i for i,v in enumerate(C1)}
C2=sorted((i,j) for i in range(len(E)) for j in range(i+1,len(E)) if not(set(E[i])&set(E[j]))); I2={v:i for i,v in enumerate(C2)}
print('cells',len(C0),len(C1),len(C2))
D1=[{I0[tuple(sorted((E[i][1],v)))]:1,I0[tuple(sorted((E[i][0],v)))]:-1} for i,v in C1]
D2=[]
for i,j in C2:
 a,b=E[i];c,d=E[j]
 D2.append({I1[(j,b)]:1,I1[(j,a)]:-1,I1[(i,d)]:-1,I1[(i,c)]:1})
for col in D2:
 check=collections.defaultdict(int)
 for k,s in col.items():
  for z,t in D1[k].items():check[z]+=s*t
 assert all(v==0 for v in check.values())
def rank2(cols):
 piv={}
 for col in cols:
  x=set(k for k,v in col.items() if v&1)
  while x:
   a=max(x)
   if a not in piv:piv[a]=x;break
   x=x.symmetric_difference(piv[a])
 return len(piv)
print('boundary rank mod2',rank2(D1),rank2(D2))
def edgechain(face):
 a,b,c=face;out={}
 for x,y in [(a,b),(b,c),(c,a)]:
  i=EI[tuple(sorted((x,y)))];out[i]=1 if x<y else -1
 return out
fc=[edgechain(f) for f in F]
Z=[]
for i,j in Fpair:
 col={}
 for ei,si in fc[i].items():
  for ej,sj in fc[j].items():
   a,b=sorted((ei,ej));col[I2[(a,b)]]=si*sj*(1 if ei<ej else -1)
 check=collections.defaultdict(int)
 for k,s in col.items():
  for z,t in D2[k].items():check[z]+=s*t
 assert all(v==0 for v in check.values()),(i,j,check)
 Z.append(col)
print('face cycle independent mod2',rank2(Z))
A=automorphisms();print('automorphisms',len(A))
PF={f:i for i,f in enumerate(F)}; PFP={p:i for i,p in enumerate(Fpair)}
T1=[];T2=[];T0=[];TG=[];Tpair=[];M=[]
for g in A:
 # graph C1 first tr
 ct1=0;ct0=0;ct2=0
 for k,(a,b) in enumerate(C0):
  if tuple(sorted((g[a],g[b])))==(a,b):ct0+=1
 for k,(i,v) in enumerate(C1):
  a,b=E[i]; jj=EI[tuple(sorted((g[a],g[b])))];v2=g[v]
  if (jj,v2)==(i,v):ct1+=(1 if g[a]<g[b] else -1)
 for k,(i,j) in enumerate(C2):
  a,b=E[i];c,d=E[j]
  ii=EI[tuple(sorted((g[a],g[b])))];jj=EI[tuple(sorted((g[c],g[d])))]
  if tuple(sorted((ii,jj)))==(i,j):ct2+=(1 if g[a]<g[b] else -1)*(1 if g[c]<g[d] else -1)*(1 if ii<jj else -1)
 T0.append(ct0);T1.append(ct1);T2.append(ct2)
 # face orientation g induced sign via oriented edge coefficients
 action=[];chr2=0
 for n,(fi,fj) in enumerate(Fpair):
  af=PF[tuple(sorted(g[v] for v in F[fi]))];bf=PF[tuple(sorted(g[v] for v in F[fj]))]
  s=[]
  for orig, dest in [(fi,af),(fj,bf)]:
   a,b,c=F[orig];uu,vv=g[a],g[b];old=EI[tuple(sorted((a,b)))];new=EI[tuple(sorted((uu,vv)))];
   s.append((1 if uu<vv else -1)*fc[orig][old]*fc[dest][new])
  pair=tuple(sorted((af,bf)));si=s[0]*s[1]*(1 if af<bf else -1)
  action.append((PFP[pair],si));chr2+=si if pair==(fi,fj) else 0
 assert sorted(k for k,s in action)==list(range(len(Z)))
 Tpair.append(chr2)
 # verify g action of first one cycle by orbit? all 100 for all120 cheap
 for idx,z in enumerate(Z):
  mapped={}
  for k,coef in z.items():
   i,j=C2[k]; a,b=E[i];c,d=E[j];ii=EI[tuple(sorted((g[a],g[b])))];jj=EI[tuple(sorted((g[c],g[d])))];mm=I2[tuple(sorted((ii,jj)))];si=(1 if g[a]<g[b] else -1)*(1 if g[c]<g[d] else -1)*(1 if ii<jj else -1);mapped[mm]=coef*si
  k,si=action[idx];assert mapped=={p:v*si for p,v in Z[k].items()},(idx, k, si)
print('action verified')
H2=Tpair;H1=[1+h2-c0+c1-c2 for c0,c1,c2,h2 in zip(T0,T1,T2,H2)]
print('Euler χ',len(C0)-len(C1)+len(C2),'Betti0',1,'Betti1',H1[0],'Betti2',H2[0]);assert H2[0]==100 and H1[0]==20
print('classes freq',collections.Counter((h1,h2,c0,c1,c2) for h1,h2,c0,c1,c2 in zip(H1,H2,T0,T1,T2)))
print('global invariants',sum(H1)//len(A),sum(H2)//len(A))
# group center inversion unique automorphism with no fixed nodes commuting with all
cent=[i for i,g in enumerate(A) if all(all(g[h[v]]==h[g[v]] for v in V) for h in A)]
print('center indices',cent)
for i in cent:print('central',i,H1[i],H2[i])
# The order-three and order-five elements generate the rotation subgroup.
KA={tuple(g[v] for v in V):i for i,g in enumerate(A)}
I=KA[tuple(V)]
def compose(i,j):return KA[tuple(A[i][A[j][v]] for v in V)]
rotset={I};front=[I]
# subgroup generated by all elements of order3,5
ids=[]
for i in range(len(A)):
 k=I;ord=0
 while True:
  k=compose(i,k);ord+=1
  if k==I:break
 if ord in (3,5):ids.append(i)
while front:
 a=front.pop()
 for b in ids:
  c=compose(a,b)
  if c not in rotset:rotset.add(c);front.append(c)
print('rot order',len(rotset),'rot invariants H1,H2',sum(H1[i] for i in rotset)//len(rotset),sum(H2[i] for i in rotset)//len(rotset))
print('center+/- spaces', [((H1[I]+H1[i])//2,(H1[I]-H1[i])//2,(H2[I]+H2[i])//2,(H2[I]-H2[i])//2) for i in cent if i!=I])
# calculate induced cycles on faces for all group elements and classify by order & central coset, rational chars
z=next(i for i in cent if i!=I)
rotconj={}
for i in rotset:
 klass=frozenset(compose(compose(j,i),next(k for k in range(len(A)) if compose(j,k)==I)) for j in rotset)
 rotconj[tuple(sorted(klass))]=1
print('rot conjugacy counts',[(len(c), H1[c[0]],H2[c[0]], sum(1 for a in V if A[c[0]][a]==a)) for c in rotconj])
for c in sorted(rotconj,key=lambda c:(-len(c),c[0])):
 i=c[0];cz=compose(z,i)
 order=next(o for o in [1,2,3,5] if __import__('functools').reduce(compose,[i]*o,I)==I)
 print('rotation class',len(c),'element order',order,'H1/H2',H1[i],H2[i],'central-twist H1/H2',H1[cz],H2[cz])
assert sorted((len(c),H1[c[0]],H2[c[0]],H1[compose(z,c[0])],H2[compose(z,c[0])]) for c in rotconj)==sorted([(1,20,100,0,-10),(12,0,0,0,0),(12,0,0,0,0),(15,0,-8,-4,2),(20,2,1,0,-1)])
assert (sum(H1)//120,sum(H2)//120)==(0,0)
assert (sum(H1[i] for i in rotset)//60,sum(H2[i] for i in rotset)//60)==(1,0)
print('ALL CHECKS PASSED')
# Rational A5 irreducibles: character norms 1, 1, 1, 2, respectively.
char_irreps={'1':(1,1,1,1),'V4':(4,0,1,-1),'V5':(5,1,-1,0),'V6':(6,-2,0,1)}
char_norms={'1':1,'V4':1,'V5':1,'V6':2}
expected={('H1',1):{'1':0,'V4':1,'V5':0,'V6':1},
          ('H1',-1):{'1':1,'V4':1,'V5':1,'V6':0},
          ('H2',1):{'1':0,'V4':3,'V5':3,'V6':3},
          ('H2',-1):{'1':0,'V4':4,'V5':3,'V6':4}}
for name,chi in [('H1',H1),('H2',H2)]:
 for parity in (1,-1):
  chars={}
  for c in rotconj:
   i=c[0];j=compose(z,i)
   n=next(v for v in (1,2,3,5) if __import__('functools').reduce(compose,[i]*v,I)==I)
   v=(chi[i]+parity*chi[j])//2
   assert (chi[i]+parity*chi[j])%2==0
   if n in chars:assert chars[n]==v
   chars[n]=v
  assert set(chars)=={1,2,3,5}
  vals=[chars[q] for q in (1,2,3,5)]
  sizes=[1,15,20,24]
  for lab,v in char_irreps.items():
   inner=sum(a*b*c for a,b,c in zip(sizes,vals,v))
   assert inner%(60*char_norms[lab])==0
   multiplicity=inner//(60*char_norms[lab])
   assert multiplicity==expected[(name,parity)][lab],(name,parity,lab,multiplicity)
  print(name,'central sector',parity,'character',vals,'rational module',expected[(name,parity)])
print('IRREDUCIBLE DECOMPOSITIONS VERIFIED')
