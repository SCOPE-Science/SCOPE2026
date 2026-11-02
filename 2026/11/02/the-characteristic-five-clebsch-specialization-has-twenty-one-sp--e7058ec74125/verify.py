from itertools import product,combinations,permutations
from collections import Counter
P=5

def norm(v):
 v=[int(x)%P for x in v]
 if not any(v):return None
 u=next(x for x in v if x)
 return tuple(x*pow(u,-1,P)%P for x in v)

def rank(A):
 a=[[int(x)%5 for x in row] for row in A]
 if not a:return 0
 r=0
 for j in range(len(a[0])):
  k=next((i for i in range(r,len(a)) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  inv=pow(a[r][j],-1,5)
  a[r]=[(z*inv)%5 for z in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][j]:
    t=a[i][j]
    a[i]=[(x-t*y)%5 for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r

def lineid(u,v):
 a=[[x%5 for x in row] for row in (u,v)]
 r=0
 for j in range(len(a[0])):
  k=next((i for i in range(r,2) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  inv=pow(a[r][j],-1,5)
  a[r]=[(z*inv)%5 for z in a[r]]
  for i in range(2):
   if i!=r and a[i][j]:
    t=a[i][j];a[i]=[(x-t*y)%5 for x,y in zip(a[i],a[r])]
  r+=1
  if r==2:break
 assert r==2
 return tuple(tuple(v) for v in a)

def emb(u):return tuple(u)+(-sum(u)%5,)
pts=sorted(set(norm(u) for u in product(range(5),repeat=4) if any(u)))
print('P3_F5_POINTS',len(pts))
lines={}
for a,b in combinations(pts,2):
 q=lineid(a,b)
 if q in lines:continue
 u,v=q
 # polynomial on projective line F5
 u5,v5=emb(u),emb(v)
 if all(sum(x**3 for x in (u5[i]*s+v5[i]*t for i in range(5)))%5==0 for s,t in [(1,0),(0,1),(1,1),(1,2)]):
  lines[q]=(u5,v5)
print('CUBIC_LINES_F5',len(lines))
p=(1,1,1,1)
node=[k for k in lines if rank([p,*k])==2]
print('LINES_THROUGH_NODE',len(node))
for k in node:print('NODE_LINE',k)
# all projective directions with x4=0 in tangent at P, sum u_i=0, Q3=R5=0
dir=[]
for a,b,c in product(range(5),repeat=3):
 v=(a,b,c,-a-b-c)
 v=norm(v)
 if v and v not in dir and sum(x*x for x in v)%5==0 and sum(x*x*x for x in v)%5==0:dir.append(v)
print('DIRECTIONS',sorted(dir))
assert len(dir)==6
nodet=[lineid(p,v) for v in dir]
assert set(nodet)==set(node)
# count classical lines
cls=[]
for z in range(5):
 others=[j for j in range(5) if j!=z]
 for pair in [(others[0],others[1],others[2],others[3]),(others[0],others[2],others[1],others[3]),(others[0],others[3],others[1],others[2])]:
  i,j,k,l=pair
  u=[0]*5;v=[0]*5;u[i]=1;u[j]=-1;v[k]=1;v[l]=-1
  # drop fifth coordinate, independent and lying in hyperplane
  cls.append(lineid(u[:4],v[:4]))
print('CLASSICAL_LINES',len(set(cls)),'NODE_INTERSECTION',len(set(cls).intersection(node)),'UNION',len(set(cls).union(node)),'ALL_LINES_MATCH',len(set(cls).union(node))==len(lines))
# S5 action on six lines from all perms
nd=set(node);images=set()
for perm in permutations(range(5)):
 def action(q):
  arr=[]
  for row in q:
   old=emb(row);n=tuple(old[perm.index(i)] for i in range(5))
   arr.append(n[:4])
  return lineid(*arr)
 mp=tuple(node.index(action(q)) for q in node)
 assert set(mp)==set(range(6))
 images.add(mp)
print('S5_SIX_POINT_PERMUTATIONS',len(images),'ORBIT',len({im[0] for im in images}))
# 5-cycle and 3-cycle action cycle type on 6 lines
for perm in [(1,2,3,4,0),(1,2,0,3,4),(1,0,2,3,4)]:
 mp=[]
 for q in node:
  old=[emb(row) for row in q]
  mp.append(node.index(lineid(*[tuple(x[perm.index(i)] for i in range(5))[:4] for x in old])))
 vis=set();cy=[]
 for i in range(6):
  if i not in vis:
   j=i;n=0
   while j not in vis:vis.add(j);j=mp[j];n+=1
   cy.append(n)
 print('S5_GENERATOR',perm,'6LINE_CYCLE_TYPE',sorted(cy))
# line incidences
vals=Counter()
for i,(k,u) in enumerate(lines.items()):
 for j,(l,v) in enumerate(lines.items()):
  if j<=i:continue
  m=rank(list(k)+list(l))<=3
  group=('N' if k in node else 'C')+('N' if l in node else 'C')
  vals[(group, m)]+=1
print('INCIDENCES',vals)
# point counts direct
for q in [5]:
 count=0
 for v in pts:
  a=emb(v)
  if sum(x**3 for x in a)%5==0:count+=1
 print('SURFACE_F5_POINTS',count)
assert len(pts)==156
assert len(lines)==21 and len(node)==6 and len(set(cls))==15
assert len(set(cls).union(node))==21
assert len(images)==120
assert count==56
assert vals[('NN',True)]==15
# Second independent extension-field check over F25 = F5[r]/(r^2-2).
# Explicitly enumerate the projective points; this supports, but does not replace, the resolution proof.
add25=lambda x,y: (x%5+y%5)%5 + 5*((x//5+y//5)%5)
neg25=lambda x: (-x%5)+5*((-(x//5))%5)
def mul25(x,y):
 a,b=x%5,x//5
 c,d=y%5,y//5
 return (a*c+2*b*d)%5+5*((a*d+b*c)%5)
def cube25(x):return mul25(mul25(x,x),x)
c25=0
for pivot in range(4):
 for suffix in product(range(25),repeat=3-pivot):
  x=(0,)*pivot+(1,)+suffix
  x4=neg25(add25(add25(x[0],x[1]),add25(x[2],x[3])))
  if add25(add25(cube25(x[0]),cube25(x[1])),add25(add25(cube25(x[2]),cube25(x[3])),cube25(x4)))==0:
   c25+=1
assert c25==776
print('SURFACE_F25_POINTS',c25)
print('VERIFY_OK')
