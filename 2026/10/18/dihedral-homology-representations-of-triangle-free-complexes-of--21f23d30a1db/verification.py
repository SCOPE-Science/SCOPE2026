"""Finite checks of a dihedral homology character for cyclic triple-avoidance complexes.
Run: python3 verification.py ; standard library only. Infinite statements use the proof.
"""
from collections import defaultdict
from itertools import combinations, product
from math import gcd

M=((1,-1,0,0),(0,0,1,-1),(1,-1,0,0),(0,0,1,0))
A=(1,-1,-1,0)
B=(1,1,1,0)

def mv(mat,vec): return tuple(sum(x*y for x,y in zip(row,vec)) for row in mat)
def dot(u,v): return sum(x*y for x,y in zip(u,v))
def trace(M,g):
 total=0
 for i in range(4):
  x=tuple(int(i==j) for j in range(4))
  for _ in range(g):x=mv(M,x)
  total+=x[i]
 return total

def f_ell(ell):
 x=B
 for _ in range(ell-2):x=mv(M,x)
 return dot(A,x)

def dimension(n):
 q,t=divmod(n,4)
 return (2*q-1 if t in (0,1) else 2*q if t==2 else 2*q+1)

def pred(n,s,ref):
 q,t=divmod(n,4)
 if not ref:
  return (1+(2 if s%4==0 else -2 if s%4==2 else 0)) if t==0 else ((-1)**s if t==2 else 1)
 if t==0:return (-1)**q
 if t==1:return (-1)**q
 if t==2:return (-1)**(q+s)
 return (-1)**(q+1)

def admissible(n,mask):
 return all(not all(mask>>((i+j)%n)&1 for j in range(3)) for i in range(n))

def z_orbits(n,perm):
 unseen=set(range(n));orbits=[]
 while unseen:
  j=min(unseen);orb=[]
  while j in unseen:
   unseen.remove(j);orb.append(j);j=perm[j]
  orbits.append(sum(1<<v for v in orb))
 z=0
 for k in range(1<<len(orbits)):
  mask=0
  for j in range(len(orbits)):
   if k>>j&1:mask|=orbits[j]
  if admissible(n,mask):z+=(-1)**k.bit_count()
 return z

def direct_lefschetz(n,perm):
 ans=-1
 for mask in range(1,1<<n):
  if not admissible(n,mask):continue
  support=[i for i in range(n) if mask>>i&1]
  mapped=[perm[i] for i in support]
  if set(support)!=set(mapped):continue
  inversions=sum(mapped[a]>mapped[b] for a in range(len(mapped)) for b in range(a+1,len(mapped)))
  ans+=(-1)**(len(support)-1+inversions)
 return ans

def mod2_rank(columns):
 basis={}
 for v in columns:
  while v:
   j=v.bit_length()-1
   if j in basis:v^=basis[j]
   else:
    basis[j]=v;break
 return len(basis)

def betti(n):
 faces=defaultdict(list)
 for mask in range(1<<n):
  if admissible(n,mask):faces[mask.bit_count()-1].append(mask)
 hi=max(faces)
 ranks={}
 for d in range(hi+1):
  lookup={f:j for j,f in enumerate(faces[d-1])}
  cols=[sum(1<<lookup[f^(1<<i)] for i in range(n) if f>>i&1) for f in faces[d]]
  ranks[d]=mod2_rank(cols)
 return {d:len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(hi+1) if len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)}

# All triples in the square of a long enough cycle must be consecutive.
for n in range(7,15):
 triples={frozenset((i,(i+1)%n,(i+2)%n)) for i in range(n)}
 squares=lambda i,j:min(abs(i-j),n-abs(i-j))<=2
 actual={frozenset(t) for t in combinations(range(n),3) if all(squares(i,j) for i,j in combinations(t,2))}
 assert triples==actual,(n,'graph identification')
print('GRAPH: triangles exactly the cyclic triples for n=7..14')

# Matrix calculations underpin the exact infinite transfer argument.
assert [trace(M,j) for j in range(1,13)]==[1,-1,1,3]*3
assert [f_ell(j) for j in range(2,18)]==[-1,-1,1,1]*4
for ell in range(2,20): assert f_ell(ell+2)==-f_ell(ell)
# Exact finite-dimensional matrix identities used for the infinite recurrence.
for i in range(4):
 e=tuple(int(i==j) for j in range(4))
 powers=[e]
 for _ in range(4): powers.append(mv(M,powers[-1]))
 assert all(powers[4][j]-powers[3][j]+powers[2][j]-powers[1][j]==0 for j in range(4))
x=tuple(mv(M,mv(M,B))[j]+B[j] for j in range(4))
for _ in range(4):
 assert dot(A,x)==0
 x=mv(M,x)
for n in range(7,14):
 dim=dimension(n)
 sg=(-1)**(dim+1)
 for shift in range(n):
  r=[(i+shift)%n for i in range(n)]
  t=[(shift-i)%n for i in range(n)]
  zr=z_orbits(n,r);zt=z_orbits(n,t)
  ell=((n+1)//2 if n%2 else n//2+int(shift%2==0))
  assert zr==trace(M,gcd(n,shift))
  assert zt==f_ell(ell)
  assert sg*zr==pred(n,shift,False)
  assert sg*zt==pred(n,shift,True)
  if n<=11:
   assert direct_lefschetz(n,r)==-zr
   assert direct_lefschetz(n,t)==-zt
 print('DIHEDRAL n=',n,'rank=',3 if n%4==0 else 1,'degree=',dim,'all 2n elements PASS')
for n in range(7,13):
 found=betti(n)
 expected={dimension(n):3 if n%4==0 else 1}
 assert found==expected,(n,found,expected)
 print('MOD2 n=',n,'Betti=',found)
print('ALL CHECKS PASSED')
