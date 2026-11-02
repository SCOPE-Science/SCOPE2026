from fractions import Fraction as F
from itertools import combinations,product
from math import gcd
V=[(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1)]

def area_index(S, w):
  indices=list(S)
  pset=set();detg=0
  for i,j in combinations(indices,2):
    a,b=V[i]; c,d=V[j]; det=a*d-b*c
    detg=gcd(detg,abs(det))
    for si,sj in product([-1,1],repeat=2):
      yi=si*w[i];yj=sj*w[j]
      x=F(yi*d-b*yj,det); y=F(a*yj-yi*c,det)
      if all(abs(A*x+B*y)<=w[k] for k in indices for A,B in [V[k]]):pset.add((x,y))
  pts=sorted(pset)
  if len(pts)<3:raise ValueError((S,pts))
  def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
  lower=[]
  for p in pts:
    while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
    lower.append(p)
  upper=[]
  for p in reversed(pts):
    while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
    upper.append(p)
  hull=lower[:-1]+upper[:-1]
  area=abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[(i+1)%len(hull)][0]*hull[i][1] for i in range(len(hull)))/2)
  return area,detg,hull

def compute(w):
  terms=[];A=B=F(0)
  for s in range(2,len(V)+1):
    for S in combinations(range(len(V)),s):
      ar,g,h=area_index(S,w)
      coeff=ar*g
      terms.append((S,ar,g,coeff))
      A+=(-1)**s*(4-s)*coeff
      B+=(-1)**s*coeff
  return A,B,terms

if __name__ == '__main__':
    from collections import defaultdict
    w=(2,2,2,1,1,1)
    A,B,terms=compute(w)
    by_size=defaultdict(F)
    for S,area,g,hweight in terms:
        by_size[len(S)]+=hweight
        assert all((6*x).denominator==1 and (6*y).denominator==1 for x,y in area_index(S,w)[2])
    assert len(terms)==57
    assert dict(by_size)=={2:F(132),3:F(72),4:F(27),5:F(7),6:F(1)}
    assert (A,B)==(F(197),F(81))
    print('EXACT_57_POLYGON_AREAS_OK',dict(by_size))
