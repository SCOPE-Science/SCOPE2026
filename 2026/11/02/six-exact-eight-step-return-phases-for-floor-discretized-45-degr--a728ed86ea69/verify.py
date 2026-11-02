"""Exact Q(sqrt(2)) interval certificate for eight-step digital rotation.
Run: python3 verify.py (only the Python standard library is needed).
"""
from fractions import Fraction as Q
from math import isqrt

# (u,v) represents u+v*sqrt(2), with rational coordinates.
def E(u=0,v=0): return (Q(u),Q(v))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sign(x):
 a,b=x
 if not a: return (b>0)-(b<0)
 if not b: return (a>0)-(a<0)
 if a>0 and b>0:return 1
 if a<0 and b<0:return -1
 if a>0 and b<0:return (a*a>2*b*b)-(a*a<2*b*b)
 return (2*b*b>a*a)-(2*b*b<a*a)
def cmp(x,y):return sign(sub(x,y))
def floorE(x):
 lo,hi=-128,128
 assert cmp(x,E(lo))>=0 and cmp(x,E(hi))<0
 while lo+1<hi:
  mid=(lo+hi)//2
  if cmp(x,E(mid))>=0:lo=mid
  else:hi=mid
 return lo

S2=E(0,1)
pts=[E(0),E(Q(-1,2),Q(1,2)), E(1,Q(-1,2)), E(-1,1), E(Q(1,2)), E(0,Q(1,2)), E(Q(-1,2),1), E(1)]
assert all(cmp(pts[j],pts[j+1])<0 for j in range(7))

# z=(A,B,C) encodes the exact integer A*a+B*w+C, w=floor(a/sqrt(2)).
def step(x,y,L,R):
 def coord(z):
  m,n,c=z
  assert n%2==0, ('odd coefficient; parity reduction invalid',z)
  # (m*a+n*w+c)/sqrt(2) = (n/2)*a+m*w+B(t).
  # B(t)=(m-n/sqrt(2))*t+c/sqrt(2).
  slope=E(m,Q(-n,2)); offset=E(0,Q(c,2))
  def val(t):return add(mul(slope,t),offset)
  mid=mul(add(L,R),E(Q(1,2)))
  k=floorE(val(mid))
  # By affinity, bounding both ends certifies the floor over ALL t in (L,R).
  assert cmp(val(L),E(k))>=0, (z,L,R,'lower',val(L),k)
  assert cmp(val(L),E(k+1))<=0, (z,L,R,'upperL',val(L),k)
  assert cmp(val(R),E(k))>=0, (z,L,R,'lowerR',val(R),k)
  assert cmp(val(R),E(k+1))<=0, (z,L,R,'upperR',val(R),k)
  return (n//2,m,k)
 return coord(tuple(i-j for i,j in zip(x,y))),coord(tuple(i+j for i,j in zip(x,y)))

expect=[(0,-1),(-1,0),(0,0),(1,-1),(-1,-1),(-1,-1),(-2,0)]
for j in range(7):
 L,R=pts[j:j+2]
 x,y=(1,0,0),(0,0,0)
 traj=[]
 for n in range(8):
  x,y=step(x,y,L,R)
  traj.append((x,y))
 assert x==(1,0,expect[j][0]) and y==(0,0,expect[j][1]),(j,x,y)
 print('interval',j+1,'8-step displacement',expect[j], 'state after 4',traj[3], 'after 8',traj[-1])

# Exact lattice arithmetic, no floating point and no special-case epsilon.
def fdivsqrt2(k):
 if k==0:return 0
 if k<0:return -fdivsqrt2(-k)-1
 return isqrt(2*k*k)//2
def f(x,y):return fdivsqrt2(x-y),fdivsqrt2(x+y)

def compare_integer_to_break(a,endpoint):
 # t={a/sqrt(2)}; w=floor(a/sqrt(2)), so t = a*sqrt2/2-w.
 w=fdivsqrt2(a)
 return cmp(E(-w,Q(a,2)),endpoint)

counts=[0]*7
for a in range(2,20001):
 index=next((i for i in range(7) if compare_integer_to_break(a,pts[i])>0 and compare_integer_to_break(a,pts[i+1])<0),None)
 if index is None:
  assert a==2 and compare_integer_to_break(a,pts[3])==0
  index=2
 counts[index]+=1
 x,y=a,0
 for k in range(8):x,y=f(x,y)
 assert (x-a,y)==expect[index],(a,index,x-a,y)
 if index==2:
  x,y=a,0
  for k in range(8):
   x,y=f(x,y)
   if k in (0,1,3):assert (x,y)!=(a,0)
print('PASS: 7 exact symbolic interval certificates, 19,999 exact integer orbit comparisons')
print('interval counts for 2<=a<=20,000:',counts)
print('boundary check: a=1 is preperiodic to origin; a=2 is an 8-cycle')
assert f(1,0)==(0,0)
assert compare_integer_to_break(2,pts[3])==0
