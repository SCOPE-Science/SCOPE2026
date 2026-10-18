#!/usr/bin/env python3
"""Exact polynomial certificate for truncated four-dimensional cross-polytopes.
Requires a C++17 compiler; uses Python's standard library only.
"""
import collections
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import subprocess
import tempfile

N = 4
A = (2, -6, 10, -6, 0)
B = (0, 4, -4, -4, 4)

# Arithmetic in Q(sqrt(2)), as pairs of exact rational coefficients.
def r(a=0, b=0): return (F(a), F(b))
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def divint(x,n): return (x[0]/n,x[1]/n)
def power(x,n):
 z=r(1)
 for _ in range(n): z=mul(z,x)
 return z

def sign(x):
 a,b=x
 if a==0: return (b>0)-(b<0)
 if b==0 or ((a>0)==(b>0)): return (a>0)-(a<0)
 q=a*a-2*b*b
 if q==0: return 0
 return ((a>0)-(a<0)) * ((q>0)-(q<0))

def evalpoly(c,x):
 z=r()
 for k in range(4,-1,-1): z=add(mul(z,x),r(c[k]))
 return z

def bernstein(c,left,right):
 """Degree-four Bernstein coefficients of c(left+(right-left)*u)."""
 width=sub(right,left)
 monomial=[]
 for j in range(5):
  q=r()
  for k in range(j,5):
   q=add(q,mul(r(c[k]*comb(k,j)),mul(power(left,k-j),power(width,j))))
  monomial.append(q)
 return [sum_q(monomial,j) for j in range(5)]

def sum_q(monomial,j):
 out=r()
 for k in range(j+1):
  out=add(out,divint(mul(monomial[k],r(comb(j,k))),comb(4,k)))
 return out

def validate():
 with tempfile.TemporaryDirectory() as td:
  exe=Path(td)/'enumerate'
  subprocess.run(['g++','-std=c++17','-O2',str(Path(__file__).with_name('enumerate.cpp')),'-o',str(exe)],check=True)
  data=subprocess.check_output([str(exe)],text=True)
 lines=data.splitlines()
 assert lines[0]=='c0\tc1\tc2\tc3\tc4\tcount\ta\tb\tc\td'
 profiles={}
 for row in lines[1:]:
  v=tuple(map(int,row.split('\t')))
  assert len(v)==10
  co=v[:5]
  assert co not in profiles
  assert v[5]>0 and all(0<=i<48 for i in v[6:])
  profiles[co]=(v[5],v[6:])
 assert len(profiles)==258,(len(profiles))
 assert sum(x[0] for x in profiles.values())==comb(47,4)
 # Positive interval certificates, exactly in Q(sqrt(2))
 zero=r();root=r(-1,1);half=r(F(1,2))
 for polynomial,(count,indices) in profiles.items():
  for target,left,right in [(A,zero,root),(B,root,half)]:
   for flip in [-1,1]:
    deficit=[target[k]+flip*polynomial[k] for k in range(5)]
    coeffs=bernstein(deficit,left,right)
    assert all(sign(z)>=0 for z in coeffs),(polynomial,deficit,left,right,coeffs)
  # The two sides have no other ties at the interior breakpoint.
  val=evalpoly(polynomial,root)
  ma=evalpoly(A,root)
  assert sign(sub(ma,val))>0 and sign(add(ma,val))>0 or polynomial in [tuple(-a for a in A),tuple(-a for a in B),A,B],polynomial
 # Strict interior inequality for each nonwinning profile:
 for target in (A,B):
  count=0
  for polynomial,(multiplicity,_) in profiles.items():
   if polynomial==target or polynomial==tuple(-v for v in target):count+=multiplicity
  assert count==(20 if target==A else 10),(target,count)
 # Explicit candidate quintuple gives the alleged determinant polynomial.
 assert profiles[(-2,6,-10,6,0)][1] == (6,20,34,47)
 assert profiles[(0,-4,4,4,-4)][1] == (6,20,41,47)
 # Signed-coordinate permutation orbits and single-vertex mobility.
 vertices=[(i,si,j,sj) for i in range(4) for si in (-1,1) for j in range(4) if j!=i for sj in (-1,1)]
 assert len(vertices)==48
 lookup={v:k for k,v in enumerate(vertices)}
 def orbit(witness):
  out=set()
  for perm in permutations(range(4)):
   for sg in product((-1,1),repeat=4):
    out.add(tuple(sorted(lookup[(perm[vertices[k][0]],vertices[k][1]*sg[perm[vertices[k][0]]],perm[vertices[k][2]],vertices[k][3]*sg[perm[vertices[k][2]]])] for k in witness)))
  return out
 left_orbit=orbit((0,6,20,34,47))
 right_orbit=orbit((0,6,20,41,47))
 assert len(left_orbit)==192 and len(right_orbit)==96 and not(left_orbit&right_orbit)
 assert len(left_orbit)==48*20//5 and len(right_orbit)==48*10//5
 def faces(sets):
  incidence=collections.defaultdict(list)
  for simplex in sets:
   for shared in combinations(simplex,4):
    incidence[shared].append(next(k for k in simplex if k not in shared))
  return incidence
 import collections
 left_faces=faces(left_orbit)
 right_faces=faces(right_orbit)
 transition_faces=faces(left_orbit|right_orbit)
 assert max(map(len,left_faces.values()))==1
 assert collections.Counter(map(len,right_faces.values()))=={1:384,2:48}
 degree=collections.Counter()
 for shared,extras in right_faces.items():
  if len(extras)==2:
   for k in extras: degree[tuple(sorted((*shared,k)))]+=1
 assert len(degree)==96 and set(degree.values())=={1}
 assert collections.Counter(map(len,transition_faces.values()))=={1:960,2:240}
 # Pairwise shared-face sign agreement checked by exact rational 4x4 determinants.
 def coords(index,t):
  i,si,j,sj=vertices[index];out=[F(0)]*4
  out[i]=si*(1-t);out[j]=sj*t
  return out
 def det4(rows):
  # Permutation formula independent of the C++ polynomial engine.
  value=F(0)
  for perm in permutations(range(4)):
   parity=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
   prodv=F(-1 if parity%2 else 1)
   for i in range(4): prodv*=rows[i][perm[i]]
   value+=prodv
  return value
 def signed(shared,other,t):
  origin=coords(shared[0],t)
  mat=[[x-y for x,y in zip(coords(k,t),origin)] for k in (*shared[1:],other)]
  return det4(mat)
 for shared,extras in right_faces.items():
  if len(extras)==2:
   values=[signed(shared,k,F(9,20)) for k in extras]
   assert values[0]==values[1] and values[0]!=0
 # Independent determinant spot check of all 258 representatives at t=1/3.
 for poly,(_,others) in profiles.items():
  value=signed((0,*others[:3]),others[3],F(1,3))
  expected=sum(F(poly[k])*F(1,3)**k for k in range(5))
  assert value in (expected,-expected),(poly,others,value,expected)
 # Endpoint, overlap and strict phase comparison: A-B=-2(t-1)(2t-1)(t^2+2t-1).
 # Root in (0,1/2), positive first and negative second.
 assert evalpoly([A[i]-B[i] for i in range(5)],root)==zero
 assert sign(evalpoly([A[i]-B[i] for i in range(5)],r(F(1,4))))>0
 assert sign(evalpoly([A[i]-B[i] for i in range(5)],r(F(9,20))))<0
 assert evalpoly(A,half)==evalpoly(B,half)==r(F(3,4))
 assert evalpoly(A,zero)==r(2)
 print('PASS: 178365 vertex-anchored determinants, 258 polynomial profiles,')
 print('1,032 exact Bernstein expansions (5 coefficients each), and equality profiles.')
 print('Phases: 192 maximizing simplices (left), 288 (transition), 96 (right).')
 print('Face incidences: no left shared faces, 48 right movable-apex segments.')

if __name__=='__main__': validate()
