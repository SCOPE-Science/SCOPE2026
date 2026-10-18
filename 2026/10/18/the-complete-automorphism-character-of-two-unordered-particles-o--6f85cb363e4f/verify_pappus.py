import networkx as nx,itertools,collections, math
P=nx.Graph();P.add_nodes_from(range(18))
for x in range(3):
 for y in range(3):
  for m in range(3):
   b=(y-m*x)%3
   P.add_edge(3*x+y,9+3*m+b)
n=len(P);edges=sorted((min(a,b),max(a,b)) for a,b in P.edges());m=len(edges); es={e:i for i,e in enumerate(edges)}
autos=[tuple(a[i] for i in range(n)) for a in nx.algorithms.isomorphism.GraphMatcher(P,P).isomorphisms_iter()]
assert len(autos)==216
v2=list(itertools.combinations(range(n),2)); c0={a:i for i,a in enumerate(v2)}
cells1=[(e,v) for e in edges for v in range(n) if v not in e];c1={x:i for i,x in enumerate(cells1)}
cells2=[(e,f) for e,f in itertools.combinations(edges,2) if not set(e)&set(f)];c2={x:i for i,x in enumerate(cells2)}
print('cells',len(c0),len(c1),len(c2),'Euler',len(c0)-len(c1)+len(c2),flush=True)

def modprank(columns,p):
 # columns sparse dict coeff rows; pivots dict idx -> normalized column dict
 piv={}
 for v in columns:
  v={i:c%p for i,c in v.items() if c%p}
  while v:
   i=min(v)
   if i in piv:
    fac=v[i];u=piv[i]
    for j,t in u.items():
     x=(v.get(j,0)-fac*t)%p
     if x:v[j]=x
     elif j in v:del v[j]
   else:
    fac=pow(v[i],-1,p);piv[i]={j:c*fac%p for j,c in v.items()};break
 return len(piv)

cols1=[]
for (e,x) in cells1:
 a,b=e;cols1.append({c0[tuple(sorted((b,x)))]:1,c0[tuple(sorted((a,x)))]:-1})
cols2=[]
for (e,f) in cells2:
 a,b=e;c,d=f
 cols2.append({c1[(f,b)]:1,c1[(f,a)]:-1,c1[(e,d)]:-1,c1[(e,c)]:1})
for p in (2,3,5,101):
 r1=modprank(cols1,p);r2=modprank(cols2,p)
 print('ranks p',p,r1,r2,'betti',len(c0)-r1,len(c1)-r1-r2,len(c2)-r2,flush=True)

def mapped(e,p):
 x,y=p[e[0]],p[e[1]]
 return (min(x,y),max(x,y)),(1 if x<y else -1)

def trace(p):
 t0=sum(1 for e in v2 if tuple(sorted((p[e[0]],p[e[1]])))==e)
 t1=sum(mapped(e,p)[1] for e,x in cells1 if mapped(e,p)[0]==e and p[x]==x)
 t2=0
 for e,f in cells2:
  ee,se=mapped(e,p);ff,sf=mapped(f,p)
  if (ee==e and ff==f): t2+=se*sf
  elif (ee==f and ff==e):t2-=se*sf
 tedge=sum(mapped(e,p)[1] for e in edges if mapped(e,p)[0]==e)
 tvert=sum(1 for i in range(n) if p[i]==i)
 return t0-t1+t2+tedge-tvert,(t0,t1,t2,tedge,tvert)

def compose(p,q):return tuple(p[q[i]] for i in range(n))
def order(p):
 x=tuple(range(n));v=0
 while True:
  v+=1;x=compose(x,p)
  if x==tuple(range(n)):return v
color=nx.bipartite.color(P)
chars={p:trace(p)[0] for p in autos};print('chi2 distribution',collections.Counter((order(p),chars[p],int(color[p[0]]!=color[0])) for p in autos))
print('chi2 norm',sum(v*v for v in chars.values())/216,'full inv',sum(chars.values())/216,'G+inv',sum(chars[p] for p in autos if color[p[0]]==color[0])/108)
rem=set(autos);classes=[]
while rem:
 p=next(iter(rem));cl={compose(compose(q,p),tuple(q.index(i) for i in range(n))) for q in autos};rem-=cl
 classes.append((len(cl),order(p),chars[p],int(color[p[0]]!=color[0]),trace(p)[1],p))
print('classes',len(classes));
for row in sorted(classes,key=lambda x:(x[1],x[0],x[2])):print('class',row[:5], 'rep',row[-1])

# Verify the graph-cycle map on rational first homology using a mod-3 rank certificate.
augmented=[]
for (edge,stationary),col in zip(cells1,cols1):
    new=col.copy()
    new[len(c0)+es[edge]]=1
    augmented.append(new)
assert modprank(augmented,3)==162
assert modprank(cols1,3)==152 and modprank(cols2,3)==270
assert len(c0)-152==1 and len(c1)-152-270==10 and len(c2)-270==27
for col in cols2:
    d={}
    for j,s in col.items():
        for i,t in cols1[j].items():d[i]=d.get(i,0)+s*t
    assert all(x==0 for x in d.values())

# An independent exact class-algebra certificate for the six irreducible constituents.
from fractions import Fraction as F
remaining=set(autos);conjugacy=[]
while remaining:
    p=next(iter(remaining))
    cl={compose(compose(q,p),tuple(q.index(i) for i in range(n))) for q in autos}
    remaining-=cl
    conjugacy.append(sorted(cl))
conjugacy.sort(key=lambda cl:(order(cl[0]),len(cl),chars[cl[0]],cl[0]))
assert len(conjugacy)==13
sizes=[len(cl) for cl in conjugacy]
assert sizes==[1,9,18,18,2,12,12,18,18,36,36,18,18]
expected=[27,3,-3,-3,0,0,0,3,0,0,0,0,0]
assert [chars[cl[0]] for cl in conjugacy]==expected
where={p:k for k,cl in enumerate(conjugacy) for p in cl}
products={}
for i,A in enumerate(conjugacy):
    for j,B in enumerate(conjugacy):
        tally=[0]*len(conjugacy)
        for p in A:
            for q in B:tally[where[compose(p,q)]]+=1
        assert all(tally[k]%sizes[k]==0 for k in range(len(sizes)))
        products[i,j]=[tally[k]//sizes[k] for k in range(len(sizes))]

# Character values are exact pairs (a,b) representing a+b*sqrt(3).
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,t):return (x[0]*t,x[1]*t)
roots=[
[1,1,-1,-1,1,1,1,1,1,-1,-1,1,1],
[4,0,0,-2,4,-2,1,0,0,0,1,0,0],
[4,0,-2,0,4,1,-2,0,0,1,0,0,0],
[6,-2,0,0,-3,0,0,2,1,0,0,-1,-1],
[6,2,0,0,-3,0,0,0,-1,0,0,(0,1),(0,-1)],
[6,2,0,0,-3,0,0,0,-1,0,0,(0,-1),(0,1)]
]
R=[[(F(v),F(0)) if isinstance(v,int) else (F(v[0]),F(v[1])) for v in row] for row in roots]
assert [sum(row[k][0] for row in R) for k in range(13)]==expected
assert all(sum(row[k][1] for row in R)==0 for k in range(13))
for row in R:
    d=row[0][0]
    lambdas=[scale(row[k],F(sizes[k],1)/d) for k in range(13)]
    for i in range(13):
        for j in range(13):
            rhs=(F(0),F(0))
            for k,c in enumerate(products[i,j]):rhs=add(rhs,scale(lambdas[k],c))
            assert mul(lambdas[i],lambdas[j])==rhs
for a,row in enumerate(R):
    for b,other in enumerate(R):
        ip=(F(0),F(0))
        for k,z in enumerate(row):ip=add(ip,scale(mul(z,other[k]),sizes[k]))
        assert ip==(F(216 if a==b else 0),F(0))
print('ALL EXACT CERTIFICATES PASSED: 216 actions, 13 classes, six absolutely irreducible complex characters, rational dimensions 1+4+4+6+12.')
