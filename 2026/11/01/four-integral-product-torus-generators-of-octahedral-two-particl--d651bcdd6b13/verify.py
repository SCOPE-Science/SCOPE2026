"""Exact rational homology and symmetry of unordered two particles on the octahedral graph.
Rebuilds all cubical cells, boundary operators, rational kernel and each of 48 group maps.
Python 3 standard library, exact fractions.
"""
from itertools import permutations, product, combinations
from collections import Counter, defaultdict
from fractions import Fraction
V=[tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (-1,1)]
vid={v:i for i,v in enumerate(V)}
E=[(i,j) for i,j in combinations(range(6),2) if V[j]!=tuple(-x for x in V[i])]
ei={e:i for i,e in enumerate(E)}
C0=list(combinations(range(6),2));c0={x:i for i,x in enumerate(C0)}
C1=[(v,e) for e,(i,j) in enumerate(E) for v in range(6) if v not in (i,j)];c1={x:i for i,x in enumerate(C1)}
C2=[(e,f) for e,f in combinations(range(len(E)),2) if not set(E[e]) & set(E[f])];c2={x:i for i,x in enumerate(C2)}
D1=[[0]*len(C1) for _ in C0];D2=[[0]*len(C2) for _ in C1]
for col,(v,e) in enumerate(C1):
 i,j=E[e]
 D1[c0[tuple(sorted((v,j)))]][col]+=1
 D1[c0[tuple(sorted((v,i)))]][col]-=1
for col,(e,f) in enumerate(C2):
 i,j=E[e];u,v=E[f]
 for cell,coeff in [((j,f),1),((i,f),-1),((v,e),-1),((u,e),1)]:
  D2[c1[cell]][col]+=coeff
assert all(sum(D1[i][k]*D2[k][j] for k in range(len(C1)))==0 for i in range(len(C0)) for j in range(len(C2)))

def rref_kernel(a):
 A=[[Fraction(v) for v in row] for row in a]
 rows=len(A);cols=len(A[0]);piv=[];r=0
 for j in range(cols):
  t=next((i for i in range(r,rows) if A[i][j]),None)
  if t is None:continue
  A[r],A[t]=A[t],A[r]
  q=A[r][j];A[r]=[x/q for x in A[r]]
  for i in range(rows):
   if i!=r and A[i][j]:
    q=A[i][j];A[i]=[x-q*y for x,y in zip(A[i],A[r])]
  piv.append(j);r+=1
  if r==rows:break
 free=[j for j in range(cols) if j not in piv]
 basis=[]
 for j in free:
  b=[Fraction(0)]*cols;b[j]=1
  for i,k in enumerate(piv):b[k]=-A[i][j]
  basis.append(b)
 return len(piv),free,basis
r1,_,_=rref_kernel(D1)
r2,free,basis=rref_kernel(D2)
assert (len(C0),len(C1),len(C2),r1,r2,len(basis))==(15,48,30,14,26,4)
AX=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
axis={v:i for i,v in enumerate(AX)}
def axis_index(v):return axis.get(v,axis.get(tuple(-x for x in v)))
def cycles(p):
 seen=set();out=[]
 for i in range(len(p)):
  if i in seen:continue
  j=i;k=0
  while j not in seen:seen.add(j);k+=1;j=p[j]
  out.append(k)
 return tuple(sorted(out,reverse=True))
# known irreducible S4 characters: trivial and standard (3,1) sum = fixed points of four axes
# H2 is the four-axis permutation representation with sign of central inversion.
chars=defaultdict(set);count=Counter()
for perm in permutations(range(3)):
 for signs in product((1,-1),repeat=3):
  def op(v):return tuple(signs[i]*v[perm[i]] for i in range(3))
  p=tuple(vid[op(v)] for v in V)
  ep={}
  for j,(i,k) in enumerate(E):
   im=(p[i],p[k]);srt=tuple(sorted(im))
   ep[j]=(ei[srt],1 if im==srt else -1)
  action={}
  for j,(e,f) in enumerate(C2):
   e1,s1=ep[e];f1,s2=ep[f]
   image=tuple(sorted((e1,f1)))
   action[j]=(c2[image],s1*s2*(1 if e1<f1 else -1))
  # Exact action on kernel in coordinate set of free columns.
  matrix=[]
  for b in basis:
   y=[Fraction(0)]*len(C2)
   for j,v in enumerate(b):
    t,sgn=action[j];y[t]+=sgn*v
   coords=[y[j] for j in free]
   check=[sum(coords[i]*basis[i][j] for i in range(4)) for j in range(len(C2))]
   assert y==check
   matrix.append(coords)
  trace=sum(matrix[i][i] for i in range(4))
  q=tuple(axis_index(op(v)) for v in AX)
  assert len(set(q))==4
  t=signs[0]*signs[1]*signs[2]
  prediction=t*sum(q[i]==i for i in range(4))
  assert trace==prediction,(perm,signs,trace,prediction)
  key=(cycles(q),t)
  chars[key].add(int(trace));count[key]+=1
assert sum(count.values())==48
print('cells',len(C0),len(C1),len(C2),'ranks',r1,r2,'Betti',1,len(C1)-r1-r2,len(C2)-r2)
for k in sorted(chars,key=str):
 assert len(chars[k])==1
 print('class',k,'count',count[k],'H2 trace',next(iter(chars[k])))
print('VERIFY_OK')
# Four vertex-disjoint opposite-face tori form a rational top-homology basis.
faces=[v for v in product((1,-1),repeat=3) if v[0]*v[1]*v[2]==1]
face_tori=[]
def cyc_edges(vertices):
 ans=[]
 for a,b in zip(vertices,vertices[1:]+vertices[:1]):
  e=tuple(sorted((a,b)));ans.append((ei[e],1 if e==(a,b) else -1))
 return ans
for f in faces:
 pos=[vid[tuple(f[j] if i==j else 0 for i in range(3))] for j in range(3)]
 neg=[vid[tuple(-f[j] if i==j else 0 for i in range(3))] for j in range(3)]
 z=[0]*len(C2)
 for a,sa in cyc_edges(pos):
  for b,sb in cyc_edges(neg):
   z[c2[tuple(sorted((a,b)))]]+=sa*sb*(1 if a<b else -1)
 assert all(sum(row[j]*z[j] for j in range(len(C2)))==0 for row in D2)
 face_tori.append(z)
_,_,kernel_tori=rref_kernel([[x[j] for x in face_tori] for j in range(len(C2))])
# Rank of 4-column torus matrix is four exactly.
rank_tori,_,_=rref_kernel([[z[i] for z in face_tori] for i in range(len(C2))])
assert rank_tori==4
print('four complementary-face tori: rank',rank_tori,'in top H2 (dimension 4)')
print('TORUS_VERIFY_OK')

# Four unique coordinate witnesses give an integral unimodular 4-by-4 minor.
supports=[{j for j,v in enumerate(z) if v} for z in face_tori]
witnesses=[]
for i,S in enumerate(supports):
    unique=sorted(S-set().union(*(supports[j] for j in range(4) if j!=i)))
    assert unique
    witnesses.append(unique[0])
minor=[[face_tori[i][j] for i in range(4)] for j in witnesses]
assert all(minor[i][j]==0 for i in range(4) for j in range(4) if i!=j)
assert all(abs(minor[i][i])==1 for i in range(4))
print('unimodular witness rows',witnesses,'diagonal', [minor[i][i] for i in range(4)])
print('INTEGRAL_BASIS_VERIFY_OK')
