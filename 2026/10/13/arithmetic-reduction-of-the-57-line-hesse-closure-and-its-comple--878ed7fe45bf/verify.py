#!/usr/bin/env python3
"""Exact deterministic arithmetic and incidence verification for the
57-line Hesse closure in Pokora--Roulleau, arXiv:2403.20024.
The input is the 57 lines in the paper's Section 2, each triplet encoded
by its coefficients in Z[e], e^2+e+1=0. Lines 8,10,13,17,36,37,54,56,57
are scaled by 2 to avoid denominator 2. Only Python standard library required.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import combinations
# Projective linear forms as three pairs (a,b) for coefficients a+b*e.
lines=[((1, 0), (-1, -1), (0, 1)), ((0, 0), (1, 0), (1, 0)), ((1, 0), (0, -2), (0, 1)), ((1, 0), (0, 1), (0, -2)), ((1, 0), (0, 1), (2, 2)), ((1, 0), (0, 0), (-1, -1)), ((1, 0), (0, 1), (-2, 0)), ((2, 0), (0, -1), (0, -1)), ((1, 0), (1, 0), (-2, 0)), ((2, 0), (-1, 0), (-1, 0)), ((0, 0), (1, 0), (0, 1)), ((1, 0), (1, 1), (0, 0)), ((2, 0), (1, 1), (0, -1)), ((1, 0), (2, 2), (0, 1)), ((1, 0), (2, 2), (-1, -1)), ((1, 0), (0, 1), (0, 0)), ((2, 0), (-1, 0), (1, 1)), ((0, 0), (0, 0), (1, 0)), ((1, 0), (1, 0), (1, 0)), ((1, 0), (1, 0), (0, 1)), ((1, 0), (0, 0), (0, -1)), ((1, 0), (0, 1), (0, 1)), ((1, 0), (-1, 0), (0, 0)), ((1, 0), (0, 1), (1, 0)), ((1, 0), (-1, -1), (0, -2)), ((1, 0), (0, 1), (-1, -1)), ((1, 0), (-1, -1), (1, 0)), ((1, 0), (-2, 0), (0, 1)), ((1, 0), (-1, -1), (-1, -1)), ((1, 0), (1, 0), (-1, -1)), ((1, 0), (0, -1), (0, 0)), ((0, 0), (1, 0), (0, 0)), ((0, 0), (1, 0), (1, 1)), ((1, 0), (0, 0), (1, 1)), ((1, 0), (1, 0), (2, 2)), ((2, 0), (1, 1), (-1, 0)), ((2, 0), (0, -1), (1, 1)), ((0, 0), (1, 0), (0, -1)), ((1, 0), (-2, 0), (1, 0)), ((1, 0), (0, 0), (0, 0)), ((0, 0), (1, 0), (-1, 0)), ((1, 0), (0, 0), (-1, 0)), ((1, 0), (1, 0), (0, 0)), ((1, 0), (0, -2), (1, 0)), ((1, 0), (-2, 0), (-1, -1)), ((1, 0), (0, -2), (-1, -1)), ((0, 0), (1, 0), (-1, -1)), ((1, 0), (0, 0), (0, 1)), ((1, 0), (2, 2), (1, 0)), ((1, 0), (-1, -1), (-2, 0)), ((1, 0), (-1, -1), (0, 0)), ((1, 0), (1, 0), (0, -2)), ((1, 0), (0, 0), (1, 0)), ((2, 0), (-1, 0), (0, -1)), ((1, 0), (-1, -1), (2, 2)), ((2, 0), (1, 1), (1, 1)), ((2, 0), (0, -1), (-1, 0))]
Z=(0,0)
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c-b*d,a*d+b*c-b*d)
def det(x,y,z):
 return add(sub(mul(x[0],sub(mul(y[1],z[2]),mul(y[2],z[1]))),mul(x[1],sub(mul(y[0],z[2]),mul(y[2],z[0])))),mul(x[2],sub(mul(y[0],z[1]),mul(y[1],z[0]))))
def cross(x,y):return (sub(mul(x[1],y[2]),mul(x[2],y[1])),sub(mul(x[2],y[0]),mul(x[0],y[2])),sub(mul(x[0],y[1]),mul(x[1],y[0])))
def norm(x):
 a,b=x;return a*a-a*b+b*b
def div(x,y):
 a,b=x;c,d=y
 nm=norm(y)
 return (F(a*(c-d)+b*d,nm),F(-a*d+b*c,nm))
def canonical(x):
 k=next(v for v in x if v!=Z)
 return tuple(div(v,k) for v in x)
def conj(x):return(x[0]-x[1],-x[1])
def conjugate(point):
 return canonical(tuple(conj(v) for v in point))
def finite_profile(p):
 if p%3==1:
  rr=[r for r in range(p) if (r*r+r+1)%p==0]
  assert len(rr)==2
  def one_profile(r):
   def cv(x):return (x[0]+x[1]*r)%p
   def addf(x,y):return (x+y)%p
   def negf(x):return (-x)%p
   def mulf(x,y):return (x*y)%p
   def invf(x):return pow(x,-1,p)
   def crossf(x,y):return ((x[1]*y[2]-x[2]*y[1])%p,(x[2]*y[0]-x[0]*y[2])%p,(x[0]*y[1]-x[1]*y[0])%p)
   zero=0
   def normalf(x):
    k=next((v for v in x if v),None)
    if k is None:return None
    ik=invf(k)
    return tuple(v*ik%p for v in x)
   red=[normalf(tuple(map(cv,L))) for L in lines]
   assert all(v is not None for v in red)
   pp=defaultdict(set)
   for i,j in combinations(range(len(red)),2):
    pt=normalf(crossf(red[i],red[j]))
    if pt is None:continue
    pp[pt].update((i,j))
   pairs=sum(len(inc)*(len(inc)-1)//2 for inc in pp.values())
   return len(set(red)),len(pp),Counter(map(len,pp.values())),pairs
  return [(r,one_profile(r)) for r in rr]
 else:
  # p=2 mod3; irreducible polynomial x²+x+1, operations in Fp²
  def cv(x):return(x[0]%p,x[1]%p)
  def mulf(x,y):return tuple(q%p for q in mul(x,y))
  def negf(x):return((-x[0])%p,(-x[1])%p)
  def addf(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
  def subf(x,y):return((x[0]-y[0])%p,(x[1]-y[1])%p)
  def invf(x):
   a,b=x;nm=norm(x)%p
   assert nm
   return (((a-b)*pow(nm,-1,p))%p,((-b)*pow(nm,-1,p))%p)
  def crossf(x,y):return(subf(mulf(x[1],y[2]),mulf(x[2],y[1])),subf(mulf(x[2],y[0]),mulf(x[0],y[2])),subf(mulf(x[0],y[1]),mulf(x[1],y[0])))
  zero=(0,0)
  def normalf(x):
   k=next((v for v in x if v!=zero),None)
   if k is None:return None
   ik=invf(k)
   return tuple(mulf(v,ik) for v in x)
  red=[normalf(tuple(map(cv,L))) for L in lines]
  assert all(v is not None for v in red)
  pp=defaultdict(set)
  for i,j in combinations(range(57),2):
   pt=normalf(crossf(red[i],red[j]))
   if pt is None:continue
   pp[pt].update((i,j))
  return [(None,(len(set(red)),len(pp),Counter(map(len,pp.values())),sum(len(inc)*(len(inc)-1)//2 for inc in pp.values())))]

def check():
    assert len(lines)==57
    assert len({canonical(L) for L in lines})==57
    points=defaultdict(set)
    for (i,L),(j,M) in combinations(enumerate(lines),2):
        P=canonical(cross(L,M))
        points[P].update((i,j))
    assert len(points)==453
    assert Counter(map(len,points.values()))==Counter({2:252,3:108,4:72,8:21})
    assert sum(len(s)*(len(s)-1)//2 for s in points.values())==1596
    line_lookup={canonical(L):i for i,L in enumerate(lines)}
    assert all(canonical(tuple(conj(v) for v in L)) in line_lookup for L in lines)
    fL=sum(canonical(tuple(conj(v) for v in L))==canonical(L) for L in lines)
    fP=sum(conjugate(P)==P for P in points)
    assert (fL,fP)==(13,31)
    assert Counter(len(inc) for p,inc in points.items() if p==conjugate(p))==Counter({2:12,3:6,4:6,8:7})
    # Every triple determinant is enumerated. Factoring positive integer norms
    # proves the exact exceptional-prime support, not just sampled primes.
    norm_primes=set()
    norm_prime_count=Counter()
    nonzero=0
    maximal_norm=0
    for ix in combinations(range(57),3):
        d=det(*(lines[i] for i in ix))
        if d==(0,0):continue
        nonzero+=1
        n=norm(d)
        assert n>0
        maximal_norm=max(maximal_norm,n)
        t=n
        for q in range(2,int(t**0.5)+2):
            if t%q==0:
                norm_primes.add(q)
                norm_prime_count[q]+=1
                while t%q==0:t//=q
        if t>1:
            norm_primes.add(t)
            norm_prime_count[t]+=1
    assert nonzero==27688
    assert maximal_norm==171
    assert norm_primes=={2,3,7,13,19}
    assert norm_prime_count==Counter({2:6984,3:21252,7:3240,13:864,19:144})
    baskets={
       5:Counter({2:252,3:108,4:72,8:21}),
       7:Counter({8:57}),
       11:Counter({2:252,3:108,4:72,8:21}),
       13:Counter({2:36,4:72,5:54,8:21}),
       17:Counter({2:252,3:108,4:72,8:21}),
       19:Counter({2:36,3:180,4:72,8:21}),
       23:Counter({2:252,3:108,4:72,8:21}),
       31:Counter({2:252,3:108,4:72,8:21})
    }
    for p,basket in baskets.items():
        pp=finite_profile(p)
        for root,(lc,ptc,mults,pairs) in pp:
            assert (lc,ptc,mults,pairs)==(57,sum(basket.values()),basket,1596),(p,root,lc,ptc,mults,pairs)
        if p%3==1:
            assert len(pp)==2
        else:
            assert len(pp)==1
    # At p=7 the 57 reduced line normals exhaust all 57 points of the dual plane.
    for r in [2,4]:
        def norm7(v):
            v=[(a+b*r)%7 for a,b in v]
            k=next(t for t in v if t)
            return tuple(t*pow(k,-1,7)%7 for t in v)
        actual={norm7(L) for L in lines}
        whole=set()
        for a in range(7):
            for b in range(7):
                whole.add((1,a,b))
        for a in range(7): whole.add((0,1,a))
        whole.add((0,0,1))
        assert actual==whole and len(actual)==57
    print('VERIFY_OK 57 lines; generic 453 pts; 13 Q-lines and 31 Q-points; bad primes >=5: 7,13,19; PG(2,7) full; 13=183,19=309')
if __name__=='__main__': check()
