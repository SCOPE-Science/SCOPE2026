import itertools, collections, math
from functools import reduce
P=list(range(7));
# 7 Fano lines, translation cyclic difference {0,1,3}
lines=[tuple(sorted((i+j)%7 for j in (0,1,3))) for i in range(7)]
edges=tuple(sorted((a,7+j) for j,L in enumerate(lines) for a in L)); n=14
edgeindex={e:i for i,e in enumerate(edges)}
V2=list(itertools.combinations(range(n),2)); ix0={c:i for i,c in enumerate(V2)}
E1=[(v,e) for e in edges for v in range(n) if v not in e]; ix1={c:i for i,c in enumerate(E1)}
F2=[(e,f) for e,f in itertools.combinations(edges,2) if set(e).isdisjoint(f)]; ix2={c:i for i,c in enumerate(F2)}
assert (len(V2),len(E1),len(F2))==(91,252,168)
# differential 1 : product sorted v and (a,b) oriented e
b1=[]
for v,(a,b) in E1:b1.append(((ix0[tuple(sorted((v,b)))],1),(ix0[tuple(sorted((v,a)))],-1)))
# differential 2 oriented product edge e then f (e<f), endpoint signs
b2=[]
for e,f in F2:
 a,b=e;c,d=f
 # [b,f]-[a,f]-[d,e]+[c,e] (edge order coordinate e then f)
 b2.append(((ix1[(b,f)],1),(ix1[(a,f)],-1),(ix1[(d,e)],-1),(ix1[(c,e)],1)))
# boundary composition verify
for col in b2:
 ss=collections.Counter()
 for j,k in col:
  for i,s in b1[j]:ss[i]+=k*s
 assert all(v==0 for v in ss.values())

def rankmod(cols,nrows,p):
 piv={}
 for col in cols:
  x={i:(v%p) for i,v in col if v%p}
  while x:
   k=min(x)
   if k not in piv:
    r=pow(x[k],-1,p); piv[k]={i:(v*r)%p for i,v in x.items()}; break
   fac=x[k]
   for i,v in piv[k].items():
    z=(x.get(i,0)-fac*v)%p
    if z: x[i]=z
    else:x.pop(i,None)
 return len(piv)
print('FANO_LINES',lines,'CELLS',len(V2),len(E1),len(F2),flush=True)
for p in (2,3,5,7,101):
 r1=rankmod(b1,len(V2),p);r2=rankmod(b2,len(E1),p)
 print('FIELD',p,'ranks',r1,r2,'Betti',(len(V2)-r1,len(E1)-r1-r2,len(F2)-r2),flush=True)
# automorphisms of Fano incidence: brute permutations of 7 points 5040, induce unique permutation on lines, plus duality
line_lookup={frozenset(L):i for i,L in enumerate(lines)}
pres=[]
for perm in itertools.permutations(range(7)):
 try: pl=tuple(line_lookup[frozenset(perm[v] for v in L)] for L in lines)
 except KeyError: continue
 pres.append(tuple(perm)+(tuple(7+j for j in pl)))
assert len(pres)==168
# standard fixed duality based on Fano cyclic incidence, use incidence symmetric condition? 
# construct line-to-point dual via a polarity matching: find 7x7 integer incidence symmetric via index shift.
pol=None
for q in itertools.permutations(range(7)):
 # f point i -> line q[i], f line j -> point q^{-1}[j]
 inv=[None]*7
 for a,b in enumerate(q):inv[b]=a
 if all((a in lines[j])==(inv[j] in lines[q[a]]) for a in range(7) for j in range(7)):
  pol=tuple(7+q[a] for a in range(7))+tuple(inv[j] for j in range(7));break
assert pol is not None
print('POLARITY',pol,flush=True)
autos=pres+[tuple(pol[x] for x in p) for p in pres]
assert len(set(autos))==336
assert all(tuple(sorted((g[a],g[b]))) in edgeindex for g in autos for a,b in edges)
assert all(all(g[a] != g[b] for a,b in edges) for g in autos)

def celltraces(g):
 t0=sum(set(g[x] for x in vv)==set(vv) for vv in V2)
 t1=0
 for v,e in E1:
  a,b=e
  if g[v]!=v or set([g[a],g[b]])!=set(e):continue
  t1+=1 if g[a]<g[b] else -1
 t2=0
 for e,f in F2:
  a,b=e;c,d=f
  ge=tuple(sorted((g[a],g[b])));gf=tuple(sorted((g[c],g[d])))
  if set((ge,gf))!=set((e,f)):continue
  s=(1 if g[a]<g[b] else -1)*(1 if g[c]<g[d] else -1)*(1 if ge<gf else -1)
  t2+=s
 gv0=sum(g[v]==v for v in range(n))
 gv1=sum((1 if g[a]<g[b] else -1) for a,b in edges if (min(g[a],g[b]),max(g[a],g[b]))==(a,b))
 # H1 trace graph gv1-gv0+1; H2 via Euler chain and map
 h1=gv1-gv0+1
 h2=t0-t1+t2-1+h1
 return (t0,t1,t2,gv0,gv1,h1,h2)

def order(g):
 x=tuple(range(n));z=x
 for k in range(1,100):
  z=tuple(g[a] for a in z)
  if z==x:return k
 raise ValueError
hist=collections.defaultdict(lambda:0)
for g in autos:
 p=tuple(celltraces(g)); k=order(g);swap=g[0]>=7
 hist[(k,swap,p)]+=1
for (k,swap,p),count in sorted(hist.items()):print('AUTOS',k,swap,p,'count',count)
assert sum(hist.values())==336
print('INVARIANT_B2',(sum(num*p[-1] for (k,swap,p),num in hist.items())/336),flush=True)
print('INVARIANT_B1',(sum(num*p[-2] for (k,swap,p),num in hist.items())/336),flush=True)
print('PRESERVING_B2_AVERAGE',sum(num*p[-1] for (k,swap,p),num in hist.items() if not swap)/168,flush=True)
# Check surjectivity on rational first homology: rank([d1;projection])-rank(d1)=8
mapcols=[]
for j,(v,e) in enumerate(E1):mapcols.append(tuple(b1[j])+((91+edgeindex[e],1),))
for p in (2,3,5,101):print('PROJECTION_RANK',p,rankmod(mapcols,112,p)-rankmod(b1,91,p),flush=True)
