"""Smooth anticanonical genus-one sections of the nonsplit quadric over GF(2)."""
import itertools,collections,sympy as s
xs=s.symbols('x0 x1 x2 x3')
mons=[a for a in itertools.product(range(3),repeat=4) if sum(a)==2]
mi={a:i for i,a in enumerate(mons)}
def idx(i,j):return mi[tuple((int(t==i)+int(t==j)) for t in range(4))]
Q=(1<<idx(0,1))^(1<<idx(2,2))^(1<<idx(2,3))^(1<<idx(3,3))
monvals=[sum(1<<k for k,a in enumerate(mons) if all(a[i]==0 or (pt>>i&1) for i in range(4))) for pt in range(1,16)]
points=[pt for pt,val in enumerate(monvals,1) if (Q&val).bit_count()%2==0]
print('Q mask',Q,'points',points)
assert len(points)==5

def rank(M):
 B=[]
 for x in M:
  for p in B:x=min(x,x^p)
  if x:B.append(x);B.sort(reverse=True)
 return len(B)
base=next(t for t in itertools.combinations(points,4) if rank(t)==4)
print('base',base)
# canonical transformation table: permute 5 projective points and map each selected source basis vector
# solving coordinates in base
def coords(x,b):
 for bits in range(16):
  if __import__('functools').reduce(int.__xor__,(b[i] for i in range(4) if bits>>i&1),0)==x:return bits
 raise AssertionError
std=[coords(1<<i,base) for i in range(4)]
def map_bits(x,columns):
 z=0
 for i in range(4):
  if x>>i&1:z^=columns[i]
 return z

def monsub_rows(T):
 rows=[sum(1<<i for i in range(4) if T[i]>>j&1) for j in range(4)]
 out=[]
 for a in mons:
  S={(0,0,0,0)}
  for j,num in enumerate(a):
   for _ in range(num):
    tt=set()
    for exp in S:
     for i in range(4):
      if rows[j]>>i&1:
       e=list(exp);e[i]+=1;tt.symmetric_difference_update({tuple(e)})
    S=tt
  out.append(sum(1<<mi[e] for e in S))
 return out

def subst(poly,monimages):
 z=0
 while poly:
  k=(poly&-poly).bit_length()-1;poly&=poly-1;z^=monimages[k]
 return z
Gs=[]
for order in itertools.permutations(points):
 tar=[order[points.index(v)] for v in base]
 cols=[map_bits(std[i],tar) for i in range(4)]
 if map_bits(points[0],cols)!=order[0]: continue
 if any(map_bits(p,cols)!=order[j] for j,p in enumerate(points)):continue
 # substitution x_j -> linear form T_j x; T rows are images of individual std basis
 M=monsub_rows(cols)
 if subst(Q,M)==Q:Gs.append(M)
assert len(Gs)==120,len(Gs)
print('Ominus group order',len(Gs))
# quotient by <Q> choose Q highest-set-bit clear.
bit=1<<(Q.bit_length()-1)
def canon(x):return x^Q if x&bit else x
reps=list(x for x in range(1024) if not x&bit)
assert len(reps)==512
orbs=[];seen={0}
for z in reps[1:]:
 if z in seen:continue
 stack=[z];seen.add(z);orbit=[]
 while stack:
  v=stack.pop();orbit.append(v)
  for mat in Gs:
   w=canon(subst(v,mat))
   if w not in seen:seen.add(w);stack.append(w)
 orbs.append((z,len(orbit)))
assert len(seen)==512
print('all section orbits',len(orbs),'sizes',collections.Counter(x[1] for x in orbs))
quadpoly=[sum(s.prod(xs[i]**a[i] for i in range(4)) for k,a in enumerate(mons) if (q>>k)&1) for q in range(1024)]
f=quadpoly[Q];df=[s.diff(f,x) for x in xs]

def smooth(x):
 g=quadpoly[x];dg=[s.diff(g,y) for y in xs]
 minor=[s.expand(df[i]*dg[j]-df[j]*dg[i]) for i in range(4) for j in range(i+1,4)]
 for k in range(4):
  eq=[z.subs(xs[k],1).expand() for z in [f,g]+minor]
  gb=s.groebner(eq,*[xs[j] for j in range(4) if j!=k],order='grevlex',modulus=2)
  if not any(p==1 for p in gb.polys):return False
 return True

def count(x):return sum((x&monvals[p-1]).bit_count()%2==0 for p in points)
records=[]
for z,n in orbs:
 records.append((z,n,smooth(z),count(z)))
 print(z,n,records[-1][2],records[-1][3])
print('smooth count',sum(n for _,n,v,c in records if v),'orbit count',sum(v for _,n,v,c in records))
print('smooth distribution',dict(sorted(collections.Counter({k:sum(n for _,n,v,c in records if v and c==k) for k in range(6)}).items())))
