#!/usr/bin/env python3
"""Exact integer-arithmetic certificate for two split residual fibres of the 21-line Klein arrangement.
No dependencies beyond Python 3 standard library. All arithmetic is in Z[a]/(a*a+a+2)."""
from itertools import combinations
from collections import Counter,defaultdict
from math import gcd
Z=(0,0); one=(1,0); minus=(-1,0); a=(0,1)
def plus(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def mult(x,y):return x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def sub(x,y):return plus(x,neg(y))
def norm(x):return x[0]**2-x[0]*x[1]+2*x[1]**2
def cross(u,v):return tuple(sub(mult(u[(j+1)%3],v[(j+2)%3]),mult(u[(j+2)%3],v[(j+1)%3])) for j in range(3))
def zero(x):return x==(0,0)
def projective_equal(x,y):return all(zero(c) for c in cross(x,y))
def det(u,v,w):return sum_pairs(cross(u,v),w)
def sum_pairs(x,y):
 z=Z
 for k in range(3):z=plus(z,mult(x[k],y[k]))
 return z
# Bauer et al., Bounded Negativity and Arrangements of Lines, arXiv:1407.2966 section 4.1.
L=[
 [one,Z,Z],[Z,one,one],[a,one,minus],[a,minus,one],[Z,minus,one],
 [one,a,minus],[a,minus,minus],[minus,one,a],[a,one,one],[minus,a,one],
 [minus,minus,a],[one,Z,one],[minus,a,minus],[one,a,one],[minus,Z,one],
 [one,minus,a],[one,one,a],[Z,Z,one],[minus,one,Z],[one,one,Z],[Z,one,Z]]
assert len(L)==21
assert len({tuple(v) for v in L})==21
# Existence and uniqueness of the generic 49 singular point classes.
points=[]; line_incidence=[]
for i,j in combinations(range(21),2):
 v=cross(L[i],L[j]);assert any(not zero(t) for t in v)
 found=next((k for k,w in enumerate(points) if projective_equal(v,w)),None)
 if found is None:
  points.append(v);line_incidence.append(set())
  found=len(points)-1
 line_incidence[found].update((i,j))
assert len(points)==49,len(points)
assert Counter(len(x) for x in line_incidence)==Counter({4:21,3:28})
assert all(sum(k in x for x in line_incidence)==8 for k in range(21))
# All nonzero triple determinant norms are powers of 2, thus arrangement incidence good in every odd residue characteristic.
norm_hist=Counter()
for i,j,k in combinations(range(21),3):
 n=norm(det(L[i],L[j],L[k]));norm_hist[n]+=1
 assert n==0 or n&(n-1)==0, (i,j,k,n)
assert sum(norm_hist.values())==1330
assert norm_hist[0]==112
# Explicit specialization of lines at the two distinct maximal ideals over 2.
def red(x,root):return (x[0]+root*x[1])%2
def reduce_proj(v,root):
 aroot=tuple(red(x,root) for x in v)
 assert any(aroot)
 return aroot

def div_pi(x,root):
 # root=0: uniformizer a, conjugate -1-a, norm 2.
 # root=1: uniformizer 1+a, conjugate -a, norm 2.
 conjugate=(-1,-1) if root==0 else (0,-1)
 t=mult(x,conjugate)
 assert t[0]%2==0 and t[1]%2==0,(x,root,t)
 return t[0]//2,t[1]//2

def point_specialization(v,root):
 w=list(v)
 for _ in range(20):
  if any(red(x,root) for x in w):return reduce_proj(w,root)
  w=[div_pi(x,root) for x in w]
 raise AssertionError('unexpected valuation')

for root in (0,1):
 groups=defaultdict(list)
 for i,row in enumerate(L,1):groups[reduce_proj(row,root)].append(i)
 assert len(groups)==(6 if root==0 else 7)
 multiplicities=Counter(len(z) for z in groups.values())
 assert multiplicities==(Counter({1:3,6:3}) if root==0 else Counter({1:3,2:3,12:1})),multiplicities
 # Every pair of distinct reduced lines meets in one of seven F2-rational projective points.
 support=list(groups)
 inter=defaultdict(list)
 for u,v in combinations(support,2):
  crosspt=tuple((u[(j+1)%3]*v[(j+2)%3]-u[(j+2)%3]*v[(j+1)%3])%2 for j in range(3))
  assert any(crosspt)
  inter[crosspt].append((u,v))
 multiplicity=Counter(sum((sum(pt[j]*line[j] for j in range(3))%2==0) for line in support) for pt in inter)
 assert multiplicity==(Counter({3:4,2:3}) if root==0 else Counter({3:7})),multiplicity
 # All 49 sections of generic intersection point set have unambiguous projective specializations.
 profiles=defaultdict(lambda:[0,0])
 for P,inc in zip(points,line_incidence):
  pt=point_specialization(P,root)
  profiles[pt][0 if len(inc)==4 else 1]+=1
 assert sum(v[0] for v in profiles.values())==21
 assert sum(v[1] for v in profiles.values())==28
 print('root',root,'line groups',sorted((str(k),len(v)) for k,v in groups.items()),'incidence',dict(multiplicity))
 print('root',root,'point specialization profile [quadruple,triple]',dict(sorted(profiles.items())))
 # In char2 Jacobian of local ordinary triple abc=uv(u+v) has ideal (u^2,v^2): tau=4;
 # node uv has Jacobian ideal (u,v): tau=1. Hence tau=19 or 28.
 tau=sum(v*(4 if k==3 else 1) for k,v in multiplicity.items())
 assert tau==(19 if root==0 else 28)
 print('root',root,'reduced support Tjurina length',tau)
print('generic point profile',Counter(map(len,line_incidence)))
print('triple determinant norms',dict(sorted(norm_hist.items())))
print('VERIFY_OK')
