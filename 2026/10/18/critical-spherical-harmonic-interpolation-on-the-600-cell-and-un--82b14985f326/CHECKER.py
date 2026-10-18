"""Exact rational-golden arithmetic for the 600-cell harmonic sampling claim.

Uses only Python's standard library. No floating point or remote dependencies.
Run: python CHECKER.py
"""
from itertools import permutations, product
from fractions import Fraction
from collections import Counter

# A pair (a,b) represents the algebraic integer a+b*phi, phi^2=phi+1.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+x[1]*y[1], x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def scale(k,x): return (k*x[0],k*x[1])
zero=(0,0); one=(1,0)
# Vertices are stored as coordinates 2*x, represented in Z[phi].
points=[]
for axis in range(4):
 for sign in (-1,1):
  v=[zero]*4;v[axis]=(2*sign,0);points.append(tuple(v))
for signs in product((-1,1),repeat=4):
 points.append(tuple((s,0) for s in signs))
def even(perm):
 return sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2==0
for perm in permutations(range(4)):
 if not even(perm):continue
 for signs in product((-1,1),repeat=3):
  s,t,u=signs
  raw=[zero,(s,0),(0,t),(-u,u)] # 1, phi, phi^{-1}=phi-1
  points.append(tuple(raw[i] for i in perm))
assert len(points)==120 and len(set(points))==120
# Distinct possible inner products t=(a+b*phi)/2, ordered increasingly.
levels=[(-2,0),(0,-1),(-1,0),(1,-1),(0,0),(-1,1),(1,0),(0,1),(2,0)]
identity=levels.index((2,0));lookup={u:i for i,u in enumerate(levels)}
def dot_label(x,y):
 v=zero
 for a,b in zip(x,y):v=add(v,mul(a,b))
 assert v[0]%2==0 and v[1]%2==0
 return lookup[(v[0]//2,v[1]//2)]
N=len(points); index=[[dot_label(x,y) for y in points] for x in points]
assert all(index[i][i]==identity for i in range(N))
assert sorted(Counter(index[0]).values())==sorted([1,1,12,12,12,12,20,20,30])
# For each distance class k, the integer structure constants c[k][i][j]
# satisfy A_i A_j = sum_k c[k][i][j] A_k.
reps=[next((x,y) for x in range(N) for y in range(N) if index[x][y]==k) for k in range(9)]
c=[[[0]*9 for _ in range(9)] for k in range(9)]
for k,(x,y) in enumerate(reps):
 for z in range(N):c[k][index[x][z]][index[z][y]]+=1
# Exact exhaustive closure verification over every ordered pair.
for x in range(N):
 for y in range(N):
  k=index[x][y];h=[[0]*9 for _ in range(9)]
  for z in range(N):h[index[x][z]][index[z][y]]+=1
  assert h==c[k],('not closed',x,y)
def vadd(a,b):return [add(x,y) for x,y in zip(a,b)]
def vneg(a):return [neg(x) for x in a]
def vmul(a,b):
 out=[]
 for k in range(9):
  z=zero
  for i in range(9):
   for j in range(9):
    if c[k][i][j]:z=add(z,scale(c[k][i][j],mul(a[i],b[j])))
  out.append(z)
 return out
I=[zero]*9;I[identity]=one
# Return B_L=120 R_L R_L^*: K_L(t) = sum_{n=0}^{L-1}(n+1)U_n(t).
def B(L):
 out=[zero]*9; prev=[one]*9;curr=list(levels)
 for n in range(L):
  V=prev if n==0 else curr
  out=vadd(out,[scale(n+1,v) for v in V])
  if n>0:prev,curr=curr,[add(mul(levels[j],curr[j]),neg(prev[j])) for j in range(9)]
 return out

def polyzero(L, eigenvalues):
 x=B(L);q=I
 for val in eigenvalues:q=vmul(q,vadd(x,vneg([scale(val,z) for z in I])))
 assert q==[zero]*9,(L,q)

def spectrum(L,eigs):
 x=B(L)
 powers=[I]
 for r in range(1,len(eigs)):
  powers.append(vmul(powers[-1],x))
 traces=[N*p[identity][0] for p in powers]
 assert all(p[identity][1]==0 for p in powers)
 # Vandermonde system for rational integer multiplicities.
 a=[[Fraction(z**r) for z in eigs]+[Fraction(traces[r])] for r in range(len(eigs))]
 for j in range(len(eigs)):
  k=next(k for k in range(j,len(eigs)) if a[k][j]);a[j],a[k]=a[k],a[j]
  d=a[j][j];a[j]=[v/d for v in a[j]]
  for k in range(len(eigs)):
   if k!=j:
    d=a[k][j];a[k]=[v-d*w for v,w in zip(a[k],a[j])]
 vals=[row[-1] for row in a]
 assert all(v.denominator==1 and v>=0 for v in vals)
 assert sum(vals)==N
 print('L=',L,'unnormalized eigs/mults=',list(zip(eigs,map(int,vals))))
 return list(map(int,vals))
for L in range(1,7):
 b=B(L)
 assert vmul(b,b)==[scale(120,z) for z in b]
 eigs=[0,120]
 polyzero(L,eigs)
 mm=spectrum(L,eigs)
 assert mm==[120-sum(n*n for n in range(1,L+1)),sum(n*n for n in range(1,L+1))]
polyzero(7,[0,120,210,280]);assert spectrum(7,[0,120,210,280])==[4,91,16,9]
polyzero(8,[120,210,280,480]);assert spectrum(8,[120,210,280,480])==[55,16,45,4]
counts=Counter(index[0]);row_sum=(0,0)
for j,z in enumerate(B(8)):row_sum=add(row_sum,scale(counts[j],z))
assert row_sum==(120,0),row_sum # constant vector eigenvalue 1 for the normalized Gram matrix
# Explicit degree-three inverse polynomial, certified without numerical inversion.
x=B(8);x2=vmul(x,x);x3=vmul(x2,x)
invnum=vadd(vadd([scale(441*120**3,z) for z in I],[scale(-342*120**2,z) for z in x]),vadd([scale(109*120,z) for z in x2],[scale(-12,z) for z in x3]))
assert vmul(x,invnum)==[scale(196*120**4,z) for z in I]
print('PASS exact closure, polynomial identities, all claimed ranks and spectra')
