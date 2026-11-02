#!/usr/bin/env python3
"""Exact certificate for centered Hilbert maximal norms on paths P3,P5,P7.

Standard-library only. Reconstructs every allowable ball choice and certifies
strict positive definiteness below a rational separating threshold using
fraction-free leading-principal-minor elimination. Also checks exact
characteristic polynomial identities and strict ball selection via rational
root enclosures. No floating-point computations occur.
"""
from itertools import product
from fractions import Fraction as F
from math import lcm

DATA = {
 3: {
  'threshold': F(199,125), 'selections':[(1,0,1)],
  'bracket':(F(15930702,10**7), F(15930704,10**7)),
  'poly':[1,-7,4], # p(lambda)=4lambda^2-7lambda+1, ascending order
  'witness':[F(186,1000),F(1),F(186,1000)],
 },
 5: {
  'threshold':F(823,500),'selections':[(1,0,1,2,3),(3,2,1,0,1)],
  'bracket':(F(16463806,10**7),F(16463808,10**7)),
  'poly':[2,-56,359,-672,288],
  'witness':[F(179,1000),F(1),F(214,1000),F(214,1000),F(117,1000)],
 },
 7: {
  'threshold':F(3387,2000),'selections':[(3,2,1,0,1,2,3)],
  'bracket':(F(16937159,10**7),F(16937161,10**7)),
  'poly':[-2,47,-149,72],
  'witness':[F(1123,10000),F(2048,10000),F(2048,10000),F(1),F(2048,10000),F(2048,10000),F(1123,10000)],
 },
}

def ball_options(n):
 return [[tuple(j for j in range(n) if abs(i-j)<=r) for r in range(max(i,n-1-i)+1)] for i in range(n)]

def mat_from_selection(n,opts,selection):
 return [[F(int(j in opts[i][r]),len(opts[i][r])) for j in range(n)] for i,r in enumerate(selection)]

def gram(A):
 n=len(A)
 return [[sum(A[k][i]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def determinant(M):
 A=[list(row) for row in M];n=len(A);s=1;d=1
 if n==1:return A[0][0]
 for k in range(n-1):
  if A[k][k]==0:
   for i in range(k+1,n):
    if A[i][k]!=0:A[k],A[i]=A[i],A[k];s=-s;break
   else:return 0
  piv=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    val=piv*A[i][j]-A[i][k]*A[k][j]
    assert val%d==0
    A[i][j]=val//d
  for i in range(k+1,n):A[i][k]=0
  d=piv
 return s*A[-1][-1]

def poly_value(coeff,x):
 return sum(c*x**i for i,c in enumerate(coeff))

def verify_charpoly(n,opts,sel):
 A=mat_from_selection(n,opts,sel)
 D=lcm(*range(1,n+1))
 G=gram(A)
 X=[[int(G[i][j]*D*D) for j in range(n)] for i in range(n)]
 for k in range(n+1):
  # Both sides are monic degree-n polynomials: interpolation at n+1 integers
  val=F(determinant([[(D*D*k if i==j else 0)-X[i][j] for j in range(n)] for i in range(n)]),D**(2*n))
  if n==3: right=F(4*k-1,4)*F(4*k*k-7*k+1,4)
  elif n==5: right=F(k*(288*k**4-672*k**3+359*k*k-56*k+2),288)
  else: right=F(k*k*(72*k*k-43*k+2)*(72*k**3-149*k*k+47*k-2),5184)
  assert val==right,(n,k,val,right)

def exact_pd_enumeration(n,threshold,expected):
 D=lcm(*range(1,n+1)); p=threshold.numerator;q=threshold.denominator
 pairs=[(i,j) for i in range(n) for j in range(i,n)]
 opts=ball_options(n)
 contributions=[]
 for i in range(n):
  rows=[]
  for ball in opts[i]:
   assert D%len(ball)==0
   v=[D//len(ball) if j in ball else 0 for j in range(n)]
   rows.append(tuple(v[a]*v[b] for a,b in pairs))
  contributions.append(rows)
 def positive_definite(g):
  A=[[0]*n for _ in range(n)]
  for h,(i,j) in enumerate(pairs):
   A[i][j]=A[j][i]=(p*D*D if i==j else 0)-q*g[h]
  den=1
  for k in range(n):
   pivot=A[k][k]
   if pivot<=0:return False
   if k==n-1:return True
   for i in range(k+1,n):
    aik=A[i][k]
    for j in range(i,n):
     v=pivot*A[i][j]-aik*A[k][j]
     quo,rem=divmod(v,den)
     assert rem==0
     A[i][j]=A[j][i]=quo
   den=pivot
  return True
 exceptional=[];count=0
 for sel in product(*(range(len(c)) for c in contributions)):
  g=[0]*len(pairs)
  for i,r in enumerate(sel):
   arr=contributions[i][r]
   for j,x in enumerate(arr):g[j]+=x
  if not positive_definite(g):exceptional.append(sel)
  count+=1
 assert set(exceptional)==set(expected),(n,exceptional,expected)
 return count,len(exceptional)

def rational_rayleigh(n,opts,sel,w):
 A=mat_from_selection(n,opts,sel)
 v=[sum(a*b for a,b in zip(row,w)) for row in A]
 return sum(x*x for x in v)/sum(x*x for x in w)

def coord_intervals(n,lo,hi):
 def d(x):return 72*x*x-43*x+2
 assert d(lo)>0 and d(hi)>=d(lo)
 # For positive, increasing numerator and denominator on the enclosures.
 def band(num):return (num(lo)/d(hi),num(hi)/d(lo))
 a=(F(1)/(4*hi-1),F(1)/(4*lo-1))
 b=band(lambda x:17*x-1)
 c=band(lambda x:9*x)
 if n==3:return [a,(F(1),F(1)),a]
 if n==5:return [a,(F(1),F(1)),b,b,c]
 return [c,b,b,(F(1),F(1)),b,b,c]

def verify_active(n,opts,sel,vecbands):
 minimum=None;checked=0
 for i,r0 in enumerate(sel):
  chosen=opts[i][r0]
  clow=sum(vecbands[j][0] for j in chosen)/len(chosen)
  for r,b in enumerate(opts[i]):
   if r==r0:continue
   high=sum(vecbands[j][1] for j in b)/len(b)
   gap=clow-high
   assert gap>0,(n,i,r0,r,gap)
   if minimum is None or gap<minimum:minimum=gap
   checked+=1
 return checked,minimum

def main():
 for n,data in DATA.items():
  opts=ball_options(n);sel=data['selections'][0]
  lo,hi=data['bracket'];p=data['poly'];th=data['threshold']
  assert th<lo<hi
  assert poly_value(p,lo)*poly_value(p,hi)<0,(n,'root bracket')
  B=gram(mat_from_selection(n,opts,sel))
  trace=sum(B[i][i] for i in range(n))
  assert trace<2*th,(n,'trace')
  ray=rational_rayleigh(n,opts,sel,data['witness'])
  assert ray>th,(n,'Rayleigh',ray)
  verify_charpoly(n,opts,sel)
  cnt,exceptions=exact_pd_enumeration(n,th,data['selections'])
  checks,mingap=verify_active(n,opts,sel,coord_intervals(n,lo,hi))
  print(f'CERTIFICATE_OK P{n} selections={cnt} exceptional={exceptions} charpoly=exact root_isolated=exact Rayleigh_above_threshold=exact active={checks} min_active_gap_gt={float(mingap):.7f}')
 print('ALL_EXACT_CERTIFICATES_OK')

if __name__=='__main__':main()
