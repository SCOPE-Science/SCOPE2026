"""Exact, standalone check for two-unordered-particle homology of the Heawood graph.
Python >=3.9; standard library only. Graph = point/line incidence of F_2^3.
"""
from itertools import combinations, product
from collections import Counter
from math import gcd


def dot(a,b): return ((a&b).bit_count() % 2)
V = tuple(range(14))
E = tuple(sorted((p-1,7+n-1) for p in range(1,8) for n in range(1,8) if dot(p,n)==0))
assert len(E)==21
EI={e:i for i,e in enumerate(E)}
F0=tuple(combinations(V,2)); I0={a:i for i,a in enumerate(F0)}
F1=tuple((i,w) for i,(u,v) in enumerate(E) for w in V if w not in (u,v))
I1={a:i for i,a in enumerate(F1)}
F2=tuple((i,j) for i,(a,b) in enumerate(E) for j,(c,d) in enumerate(E) if i<j and len({a,b,c,d})==4)
assert tuple(map(len,(F0,F1,F2)))==(91,252,168)
B1=[]
for i,w in F1:
 u,v=E[i]
 B1.append({I0[tuple(sorted((u,w)))]:-1,I0[tuple(sorted((v,w)))]:1})
B2=[]
for i,j in F2:
 u,v=E[i]; a,b=E[j]
 B2.append({I1[(j,v)]:1,I1[(j,u)]:-1,I1[(i,b)]:-1,I1[(i,a)]:1})
for z in B2:
 out={}
 for i,coef in z.items():
  for k,c in B1[i].items():out[k]=out.get(k,0)+c*coef
 assert all(v==0 for v in out.values())

def rank_mod(cols,p):
 piv={}
 for c in cols:
  x={i:(v%p) for i,v in c.items() if v%p}
  while x:
   k=max(x)
   if k not in piv:
    fac=pow(x[k],-1,p);piv[k]={a:(v*fac)%p for a,v in x.items()};break
   fac=x[k]
   for a,v in piv[k].items():
    b=(x.get(a,0)-fac*v)%p
    if b:x[a]=b
    else:x.pop(a,None)
 return len(piv)

assert (rank_mod(B1,2),rank_mod(B2,2))==(90,153)
assert (rank_mod(B1,3),rank_mod(B2,3))==(90,154)

# Integral Smith certificate by explicit unimodular elimination of unit pivots.
# Columns of B2 become rows; all transformations are signed row and column operations.
R=[{} for _ in F1]
for j,col in enumerate(B2):
 for i,v in col.items():R[i][j]=v
nr=len(R);nc=len(F2); k=0
while k<min(nr,nc):
 # Select a sparse unit pivot, to limit coefficient growth.
 colcounts=Counter(j for i in range(k,nr) for j,v in R[i].items() if j>=k)
 options=[(max(0,len([q for q in row if q>=k])-1)*max(0,colcounts[j]-1),i,j)
          for i,row in enumerate(R[k:],start=k) for j,v in row.items() if j>=k and abs(v)==1]
 if not options:break
 _,i,j=min(options)
 R[k],R[i]=R[i],R[k]
 if j!=k:
  for row in R:
   a=row.pop(k,0);b=row.pop(j,0)
   if a:row[j]=a
   if b:row[k]=b
 if R[k][k]==-1:R[k]={c:-v for c,v in R[k].items()}
 pivotrow=R[k].copy()
 for i in range(k+1,nr):
  v=R[i].get(k,0)
  if not v:continue
  for j,a in pivotrow.items():
   z=R[i].get(j,0)-v*a
   if z:R[i][j]=z
   else:R[i].pop(j,None)
 # This is a column operation: column k has zeros in every other row.
 R[k]={k:1}
 k+=1
assert k==153, k
nonzero=[(i,j,v) for i,row in enumerate(R) if i>=k for j,v in row.items() if j>=k]
assert nonzero and {abs(v) for i,j,v in nonzero}=={2}
i0,j0,v0=nonzero[0]
assert all(R[i].get(j,0)*v0==R[i].get(j0,0)*R[i0].get(j,0) for i in range(k,nr) for j in range(k,nc))
# The remaining rank-one matrix has entry gcd 2, hence SNF: 1^153, 2, 0^14.
assert (nr-(k+1),nc-(k+1))==(98,14)

# The projection to H_1(H) sends every edge+vertex cell to its oriented edge.
aug=[dict(a) for a in B1]
for j,(i,w) in enumerate(F1):aug[j][len(F0)+i]=1
assert rank_mod(aug,3)-rank_mod(B1,3)==8

# Construct all 168 Fano-plane collineations and their 168 point-line dualities.
def action(cols,p):
 a,b,c=cols
 return (a if p&1 else 0)^(b if p&2 else 0)^(c if p&4 else 0)
def dual_line(cols,n):
 for q in range(1,8):
  if all(dot(q,action(cols,p))==dot(n,p) for p in (1,2,4)):return q
 raise AssertionError('dual linear action missing')
polarity=tuple(list(range(7,14))+list(range(7)))
def compose(g,h):return tuple(g[h[i]] for i in V)
auts=set()
for cols in product(range(1,8),repeat=3):
 a,b,c=cols
 if b==a or c in (a,b,a^b):continue
 g=tuple([action(cols,p)-1 for p in range(1,8)]+[7+dual_line(cols,n)-1 for n in range(1,8)])
 auts.add(g);auts.add(compose(polarity,g))
assert len(auts)==336
for g in auts:
 assert {tuple(sorted((g[u],g[v]))) for u,v in E}==set(E)


def graph_chi(g):
 return 1-sum(g[i]==i for i in V)+sum(1 if (g[u],g[v])==(u,v) else -1
          for u,v in E if {g[u],g[v]}=={u,v})
def cell_chi(g):
 t0=sum({g[a],g[b]}=={a,b} for a,b in F0)
 t1=0
 for i,w in F1:
  a,b=E[i]
  if g[w]==w and {g[a],g[b]}=={a,b}:
   t1+=(1 if g[a]<g[b] else -1)
 t2=0
 for i,j in F2:
  a,b=E[i];u,v=E[j]
  ia=EI[tuple(sorted((g[a],g[b])))];ib=EI[tuple(sorted((g[u],g[v])))]
  if {ia,ib}!={i,j}:continue
  t2+=(1 if g[a]<g[b] else -1)*(1 if g[u]<g[v] else -1)*(1 if ia<ib else -1)
 return t0,t1,t2

def order(g):
 e=V;h=g;k=1
 while h!=e:
  h=compose(g,h);k+=1
 return k
inv={}
for g in auts:
 h=[0]*14
 for i,v in enumerate(g):h[v]=i
 inv[g]=tuple(h)
cls=[];remaining=set(auts)
while remaining:
 g=min(remaining)
 orbit={compose(compose(t,g),inv[t]) for t in auts}
 assert orbit<=remaining
 remaining-=orbit
 a,b,c=cell_chi(g);q=graph_chi(g);s=a-b+c-1+q
 for h in orbit:
  x,y,z=cell_chi(h)
  assert (x-y+z-1+graph_chi(h),graph_chi(h))==(s,q)
 cls.append((order(g),len(orbit),int(set(g[:7])!=set(range(7))),q,s,g))
cls.sort()
profile=[row[:5] for row in cls]
expected=[(1,1,0,8,14),(2,21,0,0,-2),(2,28,1,-2,-2),
          (3,56,0,-1,-1),(4,42,0,0,2),(6,56,1,1,1),
          (7,48,0,1,0),(8,42,1,0,0),(8,42,1,0,0)]
assert profile==expected,(profile,expected)
assert sum(size for _,size,*_ in cls)==336
chi8=[row[3] for row in cls];chi14=[row[4] for row in cls]
chi6=[a-b for a,b in zip(chi14,chi8)]
def inner(x,y):return sum(row[1]*a*b for row,a,b in zip(cls,x,y))
assert (inner(chi8,chi8),inner(chi6,chi6),inner(chi8,chi6))==(336,336,0)
assert sum(row[1]*row[3] for row in cls)==sum(row[1]*row[4] for row in cls)==0
c7=next(x for x in cls if x[0]==7)
assert ((8+6*c7[3])//7,(14+6*c7[4])//7)==(2,2)
assert (8+graph_chi(polarity))//2==3 and (14+(cell_chi(polarity)[0]-cell_chi(polarity)[1]+cell_chi(polarity)[2]-1+graph_chi(polarity)))//2==6
print('HEAWOOD_2CONFIG_FULL_336_CHARACTER_AND_INTEGRAL_SMITH_OK')
print('cells',tuple(map(len,(F0,F1,F2))),'boundary_ranks_Q',90,154,'SNF_D2',{'unit':153,'two':1,'zero':14})
print('character_table: (order, class_size, duality, H1, H2)')
for row in profile:print(row)
print('irreducibility inner products unnormalized',inner(chi8,chi8),inner(chi6,chi6),inner(chi8,chi6))
