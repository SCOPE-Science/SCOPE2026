import itertools
A=range(3); B=range(3,7); N=7
arcs=tuple((u,v) for u in range(N) for v in (B if u in A else A))
assert len(arcs)==24
arc_index={a:i for i,a in enumerate(arcs)}
options=[[None]+[v for (u,v) in arcs if u==x] for x in range(N)]
faces_by_dim=[[] for x in range(7)]
for tup in itertools.product(*options):
  seen=set(); okay=True
  for x in range(N):
   v=x; path=set()
   while tup[v] is not None:
    if v in path:okay=False;break
    path.add(v); v=tup[v]
   if not okay:break
  if not okay:continue
  face=tuple(sorted(arc_index[(u,v)] for u,v in enumerate(tup) if v is not None))
  if face:faces_by_dim[len(face)-1].append(face)
print('arc count',len(arcs),'fvector',[len(z) for z in faces_by_dim])
assert [len(z) for z in faces_by_dim] == [24,234,1192,3357,4968,3024,0]
chi=sum((-1)**k*len(x) for k,x in enumerate(faces_by_dim));print('Euler reduced',chi-1,'H_top expected',-(chi-1))

def bit_rank(cols):
 basis={}
 for x in cols:
  while x:
   i=x.bit_length()-1
   if i in basis:x^=basis[i]
   else:basis[i]=x; break
 return len(basis)
for j in range(1,6):
 inds={f:i for i,f in enumerate(faces_by_dim[j-1])}
 cols=[]
 for f in faces_by_dim[j]:
  bb=0
  for i in range(len(f)):bb^=1<<inds[f[:i]+f[i+1:]]
  cols.append(bb)
 r=bit_rank(cols)
 print('boundary',j+1,'rank F2',r)
 assert r == (23,211,981,2376,2592)[j-1]
from math import factorial

def cycles_type(p):
 seen=set();ls=[]
 for x in range(len(p)):
  if x in seen:continue
  y=x;k=0
  while y not in seen: seen.add(y);y=p[y];k+=1
  ls.append(k)
 return tuple(sorted(ls,reverse=True))

def signed_trace(g):
 amap=[]
 for u,v in arcs:amap.append(arc_index[(g[u],g[v])])
 total=1  # reduced Lefschetz -> htop = 1 - ordinary chain L
 for d, faces in enumerate(faces_by_dim):
  tr=0
  for f in faces:
   ff=tuple(sorted(amap[i] for i in f))
   if ff!=f:continue
   pos={v:i for i,v in enumerate(f)}
   perm=[pos[amap[i]] for i in f]
   inv=sum(perm[i]>perm[j] for i in range(len(f)) for j in range(i+1,len(f)))
   tr+= (-1)**inv
  total+=(-1)**(d+1)*tr
 return total

s3=list(itertools.permutations(range(3)));s4=list(itertools.permutations(range(4)))
chars={}
for p in s3:
 for q in s4:
  typ=(cycles_type(p),cycles_type(q))
  g=tuple(p)+tuple(qi+3 for qi in q)
  cc=signed_trace(g)
  if typ in chars:assert chars[typ]==cc,(typ,cc,chars[typ])
  else:chars[typ]=cc
assert len(chars) == 15
expected_rows = {
 (1,1,1): [432,-16,4,0,-2],
 (2,1): [0,0,4,0,-2],
 (3,): [-3,-1,1,-3,1],
}
class4=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
assert all(chars[(l,m)] == row[j] for l,row in expected_rows.items() for j,m in enumerate(class4))
print('homology character by classes')
for x in sorted(chars):print(x,chars[x])

def sgnt(p):return (-1)**sum(k-1 for k in p)
def stdt(p):return p.count(1)-1

def chi3(lam,p):
 if lam==(3,):return 1
 if lam==(1,1,1):return sgnt(p)
 return stdt(p)
def chi4(lam,p):
 if lam==(4,):return 1
 if lam==(1,1,1,1):return sgnt(p)
 if lam==(3,1):return stdt(p)
 if lam==(2,1,1):return sgnt(p)*stdt(p)
 if lam==(2,2):return { (1,1,1,1):2, (2,1,1):0,(2,2):2,(3,1):-1,(4,):0 }[p]
 assert False
lam3=[(3,),(2,1),(1,1,1)]
lam4=[(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]
expected_mults={(3,):[2,8,7,9,4],(2,1):[5,17,12,19,8],(1,1,1):[2,8,6,10,3]}
print('decomposition')
for l in lam3:
 for m in lam4:
  x=sum(chi3(l,cycles_type(p))*chi4(m,cycles_type(q))*chars[(cycles_type(p),cycles_type(q))] for p in s3 for q in s4)
  assert x % 144 == 0,(l,m,x)
  c=x//144
  assert c == expected_mults[l][lam4.index(m)]
  if c:print(l,m,c,'dimension',c*chi3(l,(1,1,1))*chi4(m,(1,1,1,1)))
print('VERIFY_OK')
