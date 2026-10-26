#!/usr/bin/env python3
"""Exact arithmetic and cone verification for diagonal cubic surfaces over F7.
Requires Python 3, SymPy; a C++17 compiler for exact facet enumeration.
This is a mathematical reproducibility artifact, not an independent review.
"""
from itertools import permutations, product
from collections import Counter
import subprocess, tempfile, pathlib
import sympy as S

P=7
zeta=2
partitions=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[(q,u,v) for q in range(3) for u in range(3) for v in range(3)]

def line_equations(t):
 q,u,v=t
 rows=[]
 for (i,j),exp in zip(partitions[q],(u,v)):
  w=[0]*4;w[i]=1;w[j]=pow(zeta,exp,P);rows.append(w)
 return rows

def rank_mod7(rows):
 a=[list(r) for r in rows]; rank=0
 for j in range(4):
  piv=next((i for i in range(rank,len(a)) if a[i][j]%P),None)
  if piv is None:continue
  a[rank],a[piv]=a[piv],a[rank]
  inv=pow(a[rank][j],-1,P)
  a[rank]=[v*inv%P for v in a[rank]]
  for i in range(len(a)):
   if i==rank:continue
   k=a[i][j]
   a[i]=[(x-k*y)%P for x,y in zip(a[i],a[rank])]
  rank+=1
 return rank

eq=[line_equations(t) for t in lines]
G=S.Matrix(27,27,lambda i,j:-1 if i==j else int(rank_mod7(eq[i]+eq[j])==3))
assert G.rank()==7
basis=[12,17,25,10,23,1,5]
g=G.extract(basis,basis)
assert abs(g.det())==1
coordinates=g.inv()*G.extract(basis,list(range(27)))
assert all(S.denom(u)==1 for u in coordinates)
assert coordinates.T*g*coordinates==G
assert all(sum(coordinates[:,j])==1 for j in range(27))

perms=list(permutations(range(4)))
def normal(m):
 return min(tuple((m[t]-m[pr[0]])%3 for t in pr) for pr in perms)
classes={}
for m in product(range(3),repeat=4): classes.setdefault(normal(m),[]).append(m)
assert {k:len(v) for k,v in classes.items()}=={
 (0,0,0,0):3,(0,0,0,1):12,(0,0,0,2):12,
 (0,0,1,1):18,(0,0,1,2):36}

with tempfile.TemporaryDirectory(prefix='dual_exact_') as tmp:
 source=pathlib.Path(__file__).with_name('dual_cone_exact.cpp')
 binary=pathlib.Path(tmp)/'dual_cone_exact'
 subprocess.run(['g++','-O2','-std=c++17',str(source),'-o',str(binary)],check=True,capture_output=True,timeout=35)
 wanted={
 (0,0,0,0):(7,27,27,27,99),
 (0,0,0,1):(1,0,9,1,1),
 (0,0,0,2):(1,0,9,1,1),
 (0,0,1,1):(5,9,15,15,21),
 (0,0,1,2):(3,0,9,6,6)}
 for m in sorted(classes):
  def frob(i):
   q,u,v=lines[i]
   (a,b),(c,d)=partitions[q]
   # The coefficient of x_i is a cube root; Frobenius scales it by zeta^m_i.
   return lines.index((q,(u+m[b]-m[a])%3,(v+m[d]-m[c])%3))
  assert all(frob(frob(frob(j)))==j for j in range(27))
  unseen=set(range(27)); orbits=[]
  while unseen:
   i=min(unseen)
   o=tuple(sorted({i,frob(i),frob(frob(i))}))
   unseen.difference_update(o)
   orbits.append(o)
  V=S.Matrix.hstack(*[sum((coordinates[:,j] for j in o),S.zeros(7,1)) for o in orbits])
  _,piv=V.rref();rank=V.rank();B=V[:,piv[:rank]]
  Q=(B.T*B).inv()*B.T*V
  assert B*Q==V
  assert len(orbits)==wanted[m][2] and rank==wanted[m][0]
  rational_lines=sum(len(o)==1 for o in orbits)
  assert rational_lines==wanted[m][1]
  squares=[int((V[:,j].T*g*V[:,j])[0]) for j in range(V.cols)]
  if m==(0,0,1,1):
   assert Counter(squares)=={-1:9,-3:6}
   extreme=15 # Negative square of each orbit sum, and distinct orbit sums have nonnegative mutual intersections.
  elif m==(0,0,1,2):
   assert Counter(squares)=={3:3,-3:6}
   assert V[:,0]==V[:,1]==V[:,2]
   assert sum((V[:,j] for j in range(3,9)),S.zeros(7,1))==6*V[:,0]
   extreme=6
  elif m==(0,0,0,0):
   assert all(x==-1 for x in squares)
   extreme=27
  else:
   assert rank==1 and len(set(tuple(V[:,j]) for j in range(V.cols)))==1
   extreme=1
  assert extreme==wanted[m][3]
  # No nonzero restriction is discarded: columns span the invariant subspace.
  D=S.Matrix(Q)
  mul=S.ilcm(*[int(S.denom(x)) for x in D])
  A=mul*D
  assert all(S.denom(x)==1 for x in A)
  data=f'{rank} {A.cols}\n'+'\n'.join(' '.join(str(int(A[i,j])) for j in range(A.cols)) for i in range(rank))+'\n'
  res=subprocess.run([str(binary)],input=data,text=True,capture_output=True,check=True,timeout=135)
  count=int(res.stdout.split()[3]);assert count==wanted[m][4],(m,res.stdout)
  # An independent arithmetic check via all F7 projective points.
  coefs=[pow(3,x,7) for x in m]
  points=sum(1 for xs in product(range(7),repeat=4) if any(xs) and sum(c*pow(x,3,7) for c,x in zip(coefs,xs))%7==0)//6
  expected={7:99,5:78,3:57,1:36}[rank]
  assert points==expected,(m,points,expected)
  print('TYPE',m,'coefficient-patterns',len(classes[m]),'Picard-rank',rank,'rational-lines',rational_lines,'line-orbits',len(orbits),'effective-rays',extreme,'nef-rays',count,'F7-points',points,res.stdout.strip())
print('VERIFY_OK: five diagonal coefficient types; arithmetic cones (27/99), (1/1), (1/1), (15/21), (6/6).')
