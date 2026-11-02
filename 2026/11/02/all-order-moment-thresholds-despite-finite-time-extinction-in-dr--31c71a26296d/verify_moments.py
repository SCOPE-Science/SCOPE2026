from fractions import Fraction as F
from math import comb,sqrt
from itertools import product

def matrix(k, M, w):
 b=[[F(0) for _ in range(k+1)] for __ in range(k+1)]
 for i in range(k):
  for h in range(k-i+1): b[i][h]=w*(M/2)**(k-i)*comb(k-i,h)
 b[k][0]=1
 return b

def mv(B,v): return [sum(x*y for x,y in zip(row,v)) for row in B]

nchecks=0
for k in range(1,7):
 for M in [F(1,2),F(1),F(3,2),F(3)]:
  for w in [F(1,4),F(1,2),F(3,4)]:
   B=matrix(k,M,w)
   v=[F(1)]*(k+1)
   for n in range(1,8):
    v=mv(B,v)
    exact=[F(0)]*(k+1)
    for bits in product((0,1),repeat=n):
     y0=F(1);ym1=F(1)
     prob=F(1)
     for bit in bits:
      yt= (M/F(2))*(y0+ym1) if bit else F(0)
      prob*=w if bit else 1-w
      ym1,y0=y0,yt
     for i in range(k+1): exact[i]+=prob*y0**(k-i)*ym1**i
    assert exact==v,(k,M,w,n,exact,v)
    nchecks+=k+1
print('PASS',nchecks,'exact moment identities')

for w in [F(1,4),F(1,2),F(3,4)]:
 for M in [F(1,2),F(1),F(3,2),F(2),F(4)]:
  b=matrix(2,M,w)
  # determinant of (I-B_2)
  d=[[int(i==j)-b[i][j] for j in range(3)] for i in range(3)]
  D=d[0][0]*(d[1][1]*d[2][2]-d[1][2]*d[2][1])-d[0][1]*(d[1][0]*d[2][2]-d[1][2]*d[2][0])+d[0][2]*(d[1][0]*d[2][1]-d[1][1]*d[2][0])
  assert D==1-w*(M*M+M)/2
  nchecks+=1
print('VERIFY_OK',nchecks,'exact rational checks')
