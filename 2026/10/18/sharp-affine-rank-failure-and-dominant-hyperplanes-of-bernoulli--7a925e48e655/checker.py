from fractions import Fraction
from itertools import combinations,product
from collections import Counter
from math import gcd, comb

def plane_normal(points):
    # row-reduced exact fractions n rows, n+1 columns, normal (a,b) with a*x+b=0
    n=len(points[0]); m=[[Fraction(1)]+[Fraction(v) for v in p] for p in points]
    pivots=[];r=0
    for c in range(n+1):
      k=next((i for i in range(r,n) if m[i][c]), None)
      if k is None:continue
      m[r],m[k]=m[k],m[r]
      z=m[r][c];m[r]=[x/z for x in m[r]]
      for j in range(n):
        if j!=r and m[j][c]:
          f=m[j][c];m[j]=[m[j][i]-f*m[r][i] for i in range(n+1)]
      pivots.append(c);r+=1
      if r==n:break
    if r!=n:return None
    free=next(k for k in range(n+1) if k not in pivots)
    v=[Fraction(0)]*(n+1);v[free]=1
    for i,p in enumerate(pivots):v[p]=-m[i][free]
    from math import lcm
    den=lcm(*(z.denominator for z in v));z=[int(z*den) for z in v]
    g=gcd(*z);z=tuple(x//g for x in z)
    if next(x for x in z if x)!=abs(next(x for x in z if x)):z=tuple(-x for x in z)
    return z

for n in [2,3,4]:
 V=list(product((0,1),repeat=n));N=len(V); planes=set()
 for pts in combinations(V,n):
   v=plane_normal(pts)
   if v:planes.add(v)
 counts=Counter(sum(v[0]+sum(a*x for a,x in zip(v[1:],p))==0 for p in V) for v in planes)
 biggest=N//2
 print(n,len(planes),counts,'max',max(counts),'number max',counts[biggest],'expected',n*(n+1))
 assert max(counts)==biggest
 assert counts[biggest]==n*(n+1)
 if n>=3:assert max(k for k in counts if k<biggest)<=3*N//8

# Dominant hyperplanes uniformly exact combinatorial intersections
for n in [3,4,5]:
 V=list(product((0,1),repeat=n));dominants=[]
 for i in range(n):
  for b in (0,1):dominants.append({v for v in V if v[i]==b})
 for i,j in combinations(range(n),2):
  for parity in (0,1):dominants.append({v for v in V if (v[i]+v[j])%2==parity})
 assert len(dominants)==n*(n+1)
 assert len({tuple(sorted(H)) for H in dominants})==len(dominants)
 assert all(len(H)==2**(n-1) for H in dominants)
 inter=Counter(len(H & G) for H,G in combinations(dominants,2))
 print('intersection',n,inter)
 assert max(inter)<=2**(n-2)
print('all exact checks passed')
# Exhaustively enumerate every retention pattern for n<=4 (p=1/2).
for n in [3,4]:
 V=list(product((0,1),repeat=n));N=len(V)
 planes=set()
 for pts in combinations(V,n):
  h=plane_normal(pts)
  if h:planes.add(h)
 masks=[]
 for h in planes:
  mask=sum((1<<i) for i,v in enumerate(V) if h[0]+sum(a*x for a,x in zip(h[1:],v))==0)
  masks.append(mask)
 dominant=[]
 for i in range(n):
  for b in (0,1):
   dominant.append(sum((1<<k) for k,v in enumerate(V) if v[i]==b))
 for i,j in combinations(range(n),2):
  for a in (0,1):
   dominant.append(sum((1<<k) for k,v in enumerate(V) if (v[i]+v[j])%2==a))
 # Index zero-to-(2*n-1) is coordinate type, all later pair constraints.
 dcoord=set(dominant[:2*n]);dpair=set(dominant[2*n:])
 count_def=count_c=count_p=count_other=0
 for pattern in range(1<<N):
  cs=[H for H in masks if pattern & ~H==0]
  if cs:
   count_def+=1
   if len(cs)==1:
    if cs[0] in dcoord:count_c+=1
    elif cs[0] in dpair:count_p+=1
    else:count_other+=1
 rho_prior=None
 if n==3:
  # 2-cube full affine dimension can be enumerated similarly.
  W=list(product((0,1),repeat=2));Hs=[]
  for pts in combinations(W,2):
   h=plane_normal(pts)
   if h:Hs.append(sum((1<<j) for j,v in enumerate(W) if h[0]+sum(a*x for a,x in zip(h[1:],v))==0))
  rho_prior=Fraction(sum(any(mask & ~H==0 for H in Hs) for mask in range(1<<4)),(1<<4))
 elif n==4:
  W=list(product((0,1),repeat=3));Hs=[]
  for pts in combinations(W,3):
   h=plane_normal(pts)
   if h:Hs.append(sum((1<<j) for j,v in enumerate(W) if h[0]+sum(a*x for a,x in zip(h[1:],v))==0))
  rho_prior=Fraction(sum(any(mask & ~H==0 for H in Hs) for mask in range(1<<8)),(1<<8))
 per_H=(1<<(N//2))*(1-rho_prior) # total 2^(N) patterns times probability q^(N/2)*(1-rho)
 assert count_c == round(2*n*per_H)
 assert count_p == round(n*(n-1)*per_H)
 print('Bernoulli half',n,'deficient patterns',count_def,'coordinate-spanned',count_c,'diagonal-spanned',count_p,'other hyperplanes',count_other,'rho_prev',rho_prior)
assert True
