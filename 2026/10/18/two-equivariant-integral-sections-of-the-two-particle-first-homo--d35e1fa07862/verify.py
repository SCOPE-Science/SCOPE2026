from itertools import combinations
from collections import deque
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def analyze(name,n,edges,gens):
 edges=sorted(tuple(sorted(e)) for e in edges);m=len(edges)
 mids={e:n+i for i,e in enumerate(edges)};V=list(range(n+m))
 E=sorted(tuple(sorted((a,mids[e]))) for e in edges for a in e)
 vv=list(combinations(V,2));vvi={v:i for i,v in enumerate(vv)}
 cc1=sorted((w,e) for e in E for w in V if w not in e);c1i={c:i for i,c in enumerate(cc1)}
 cc2=[(a,b) for a,b in combinations(E,2) if set(a).isdisjoint(b)]
 par=list(range(len(vv)))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 tree=[];co=[];adj=[[] for _ in vv]
 for i,(w,(a,b)) in enumerate(cc1):
  v0=vvi[tuple(sorted((w,a)))];v1=vvi[tuple(sorted((w,b)))];x,y=root(v0),root(v1)
  if x!=y:par[x]=y;tree.append(i);adj[v0].append((v1,i));adj[v1].append((v0,i))
  else:co.append(i)
 assert len(tree)==len(vv)-1
 coidx={e:i for i,e in enumerate(co)}
 B=[0]*len(cc2);Ai=[]
 for k,(a,b) in enumerate(cc2):
  u,v=a;x,y=b
  z=0
  for cell in [(v,b),(u,b),(y,a),(x,a)]:
   i=c1i[cell]
   if i in coidx:z^=1<<coidx[i]
  B[k]=z
 piv={}
 def red(z,record=False):
  if not record:
   for i in sorted(piv,reverse=True):
    if z>>i&1:z^=piv[i]
   return z
  while z:
   i=z.bit_length()-1
   if i not in piv:
    piv[i]=z
    return z
   z^=piv[i]
  return 0
 for z in B:red(z,True)
 free=[i for i in range(len(co)) if i not in piv]
 def toH(z):
  r=red(z)
  assert not r&sum(1<<i for i in piv)
  return sum(1<<j for j,i in enumerate(free) if r>>i&1)
 path=[None]*len(vv);path[0]=0;q=deque([0]);
 while q:
  v=q.popleft()
  for w,e in adj[v]:
   if path[w] is None:path[w]=path[v]^(1<<e);q.append(w)
 fc=[]
 for e in co:
  w,(a,b)=cc1[e];x=vvi[tuple(sorted((w,a)))];y=vvi[tuple(sorted((w,b)))]
  fc.append((1<<e)^path[x]^path[y])
 # underlying graph cycle basis
 par2=list(V)
 def rt(i):
  while par2[i]!=i:i=par2[i]
  return i
 gt=[];gc=[]
 for i,(a,b) in enumerate(E):
  x,y=rt(a),rt(b)
  if x!=y:par2[x]=y;gt.append(i)
  else:gc.append(i)
 gcidx={e:i for i,e in enumerate(gc)}
 gproj=[E.index(e) for w,e in cc1]
 def tog(z):
  out=0
  while z:
   b=z&-z;i=b.bit_length()-1;z-=b
   if gproj[i] in gcidx:out^=1<<gcidx[gproj[i]]
  return out
 P=[tog(fc[i]) for i in free]
 geadj=[[] for _ in V]
 for e in gt:
  a,b=E[e];geadj[a].append((b,e));geadj[b].append((a,e))
 gp=[None]*len(V);gp[0]=0;q=deque([0]);
 while q:
  a=q.popleft()
  for b,e in geadj[a]:
   if gp[b] is None:gp[b]=gp[a]^(1<<e);q.append(b)
 gfund=[(1<<e)^gp[E[e][0]]^gp[E[e][1]] for e in gc]
 Gidx={e:i for i,e in enumerate(E)}
 def act(col,z):
  out=0
  while z:
   b=z&-z;i=b.bit_length()-1;z-=b;out^=col[i]
  return out
 def mapcols(g):
  vm={i:g[i] for i in range(n)}
  for a,m0 in mids.items():vm[m0]=mids[tuple(sorted((g[a[0]],g[a[1]])))]
  e_map=[c1i[(vm[w],tuple(sorted((vm[a],vm[b]))))] for w,(a,b) in cc1]
  ge_map=[Gidx[tuple(sorted((vm[a],vm[b])))] for a,b in E]
  T=[];U=[]
  for i in free:
   zz=act([1<<j for j in e_map],fc[i]);zc=sum((1<<coidx[j]) for j in co if zz>>j&1);T.append(toH(zc))
  for z in gfund:
   zz=act([1<<j for j in ge_map],z);U.append(sum((1<<gcidx[j]) for j in gc if zz>>j&1))
  assert all(act(P,act(T,1<<i))==act(U,act(P,1<<i)) for i in range(len(free)))
  return T,U
 tu=[mapcols(g) for g in gens]
 # linear system modulo two for equivariant section
 dim=len(free);r=len(gc);d=dim*r
 EQ=[]
 for a in range(r):
  for rr in range(r):
   mask=sum(1<<(a*dim+j) for j in range(dim) if (P[j]>>rr)&1)
   EQ.append(mask|((a==rr)<<d))
 for T,U in tu:
  for a in range(r):
   for rr in range(dim):
    mask=sum(1<<(a*dim+j) for j in range(dim) if (T[j]>>rr)&1)
    for b in range(r):
     if (U[a]>>b)&1:mask^=1<<(b*dim+rr)
    EQ.append(mask)
 piv2={};bad=0
 for z in EQ:
  while z&((1<<d)-1):
   k=(z&((1<<d)-1)).bit_length()-1
   if k not in piv2:piv2[k]=z;break
   z^=piv2[k]
  else:
   if z>>d:bad+=1
 if name=='K5':
  assert (len(vv),len(cc1),len(cc2),len(co),len(piv),dim,r)==(105,260,150,156,149,7,6)
  assert P==[7,25,42,4,16,1,3]
  assert len(piv2)==41 and not bad
  print('K5 certificates P',P,'T/U',tu,flush=True)
  if not bad:
   freevar=[i for i in range(d) if i not in piv2]
   print('freevar',freevar,flush=True)
   for choice in [0,1]:
    sol=choice<<freevar[0] if freevar else 0
    for i in sorted(piv2):
     z=piv2[i];rhs=(z>>d)&1
     other=(z&((1<<d)-1))^(1<<i)
     bit=rhs^((sol&other).bit_count()&1)
     if bit:sol|=1<<i
    S=[(sol>>(a*dim))&((1<<dim)-1) for a in range(r)]
    assert all(act(P,S[i])==(1<<i) for i in range(r))
    assert all(act(T,S[i])==act(S,U[i]) for T,U in tu for i in range(r))
    assert S==([[32,41,65,50,89,86],[105,96,8,123,16,31]][choice])
    print('section',choice,S,flush=True)
 print(name,'counts',list(map(len,[vv,cc1,cc2])),'graph beta',r,'rank B2 over F2',len(piv),'H1F2',dim,'section?',bad==0,'eq rank',len(piv2),'incons',bad,flush=True)
 # Smith exact
 if len(cc2)<220:
  AA=sp.zeros(len(co),len(cc2))
  for j,z in enumerate(B):
   while z:
    b=z&-z;i=b.bit_length()-1;z-=b;AA[i,j]=1
  # signs lost: recompute
  for j,(a,b) in enumerate(cc2):
   u,v=a;x,y=b
   for cell,s in [((v,b),1),((u,b),-1),((y,a),-1),((x,a),1)]:
    i=c1i[cell]
    if i in coidx:AA[coidx[i],j]+=s-1 # correcting initial 1 mod2 for each term
  S=smith_normal_form(AA,domain=ZZ)
  diag=[abs(S[i,i]) for i in range(min(S.shape)) if S[i,i]]
  if name=='K5': assert len(diag)==150 and diag.count(1)==149 and diag.count(2)==1
  print('SNF',len(diag),'tors',[d for d in diag if d>1],'free',len(co)-len(diag),flush=True)
 return (name,dim,r, bad==0)


if __name__=="__main__":
 from itertools import combinations
 generators=[(1,0,2,3,4),(1,2,3,4,0)]
 result=analyze("K5",5,list(combinations(range(5),2)),generators)
 assert result==("K5",7,6,True)
 print("ALL CHECKS PASS")
