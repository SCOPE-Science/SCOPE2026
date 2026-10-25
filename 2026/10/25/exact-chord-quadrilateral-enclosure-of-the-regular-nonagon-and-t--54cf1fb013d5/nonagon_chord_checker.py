"""Exact rational interval certificate for chord quadrilaterals of the regular nonagon.
Run: python heptagon_chord_checker.py.  Only Python standard library is needed.
"""
from fractions import Fraction as Q
from itertools import combinations

L=Q(18793852415,10**10)
U=Q(18793852417,10**10)
def p(x):return x**3-3*x-1
assert p(L)<0<p(U)
assert 3*L**2-3>0  # p is increasing on the bracket

class Interval:
 def __init__(self,lo,hi=None):
  self.lo=Q(lo);self.hi=Q(lo if hi is None else hi)
  assert self.lo<=self.hi
 def __add__(a,b):
  b=cast(b);return Interval(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return Interval(-a.hi,-a.lo)
 def __sub__(a,b):return a+-cast(b)
 def __rsub__(a,b):return cast(b)+-a
 def __mul__(a,b):
  b=cast(b); vals=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
  return Interval(min(vals),max(vals))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=cast(b);assert not (b.lo<=0<=b.hi)
  vals=[x/y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
  return Interval(min(vals),max(vals))
 def __repr__(a):return f'[{float(a.lo):.12g},{float(a.hi):.12g}]'
def cast(z):return z if isinstance(z,Interval) else Interval(z)
x=Interval(L,U)
C=[Interval(1),x/2]
for i in range(2,9):C.append(x*C[-1]-C[-2])
S=[Interval(0),Interval(1),x]
for i in range(3,9):S.append(x*S[-1]-S[-2])
for d in range(1,9):assert S[d].lo>0
h=[Interval(1),x/2]
term={}
for d in range(1,9):
 for pa in range(2):
  for pb in range(2):
   a,b=h[pa],h[pb]
   term[d,pa,pb]=(a*b-(a*a+b*b)*C[d]/2)/S[d]

def gaps(sub):return [((sub[(i+1)%4]-sub[i])%18) for i in range(4)]
def scaled_area(sub):
 ds=gaps(sub)
 assert max(ds)<9 and sum(ds)==18
 return sum((term[ds[i],sub[i]%2,sub[(i+1)%4]%2] for i in range(4)),Interval(0))
# Seven rotations of one pattern, using cyclic index increments of two.
reference=(0,5,9,13)
winning={tuple(sorted((k+2*j)%18 for k in reference)) for j in range(9)}
assert len(winning)==9
best=scaled_area(reference)
candidate_count=0
bounded_count=0
margin=Q(1,100)
closest=None
for sub in combinations(range(18),4):
 candidate_count+=1
 ds=gaps(sub)
 if max(ds)>=9:continue
 bounded_count+=1
 A=scaled_area(sub)
 if sub in winning:
  # All have the same exact summands in a cyclic permutation.
  assert sorted(zip(ds,[sub[i]%2 for i in range(4)], [sub[(i+1)%4]%2 for i in range(4)])) == sorted(zip(gaps(reference),[reference[i]%2 for i in range(4)], [reference[(i+1)%4]%2 for i in range(4)]))
 else:
  assert A.lo>best.hi+margin, ('not separated',sub,A,best)
  difference=A.lo-best.hi
  closest=difference if closest is None else min(closest,difference)
assert candidate_count==3060
assert bounded_count==1548
# All-edge-parallel quadrilaterals have four odd-indexed outward normals.
edge_reference=(1,5,9,13)
edge_winning={tuple(sorted((k+2*j)%18 for k in edge_reference)) for j in range(9)}
assert len(edge_winning)==9
edge_best=scaled_area(edge_reference)
edge_cases=0
for sub in combinations(range(1,18,2),4):
 if max(gaps(sub))>=9: continue
 edge_cases+=1
 a=scaled_area(sub)
 if sub in edge_winning:
  assert sorted(zip(gaps(sub), [sub[i]%2 for i in range(4)], [sub[(i+1)%4]%2 for i in range(4)])) == sorted(zip(gaps(edge_reference),[edge_reference[i]%2 for i in range(4)], [edge_reference[(i+1)%4]%2 for i in range(4)]))
 else:
  assert a.lo>edge_best.hi+Q(1,10)
assert edge_cases==90
assert edge_best.lo>best.hi+Q(1,100)

print('PASS: cubic-root bracket, positive trigonometric denominators, 3060 subsets, 1548 bounded cases, nine minimizers and nine edge-only minimizers.')
print('Certified common-denominator-scaled gap >1/100; minimum interval lower margin:', float(closest))
