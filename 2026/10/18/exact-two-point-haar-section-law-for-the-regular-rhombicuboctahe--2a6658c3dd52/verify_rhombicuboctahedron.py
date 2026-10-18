#!/usr/bin/env python3
"""Exact algebraic sign-chamber checks for central rhombicuboctahedron sections."""
from itertools import combinations,product
from collections import Counter
from math import sqrt,acos,atan,pi

def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return a*c+2*b*d,a*d+b*c
def sgn(x):
 a,b=x
 if not a and not b:return 0
 if a>=0 and b>=0:return 1
 if a<=0 and b<=0:return -1
 return (a*a>2*b*b)-(a*a<2*b*b) if a>0 else (2*b*b>a*a)-(2*b*b<a*a)
def dot(v,w):
 z=(0,0)
 for a,b in zip(v,w):z=add(z,mul(a,b))
 return z
one=(1,0);rr=(1,1);zero=(0,0)
def make_vertices():
 v=[]
 for k in range(3):
  for signs in product([-1,1],repeat=3):
   row=[(signs[j],0) for j in range(3)]
   row[k]=rr if signs[k]>0 else neg(rr)
   v.append(tuple(row))
 return v

def check():
 V=make_vertices();assert len(set(V))==24
 R2=dot(V[0],V[0]);assert R2==(5,2)
 E=[]
 for i,j in combinations(range(len(V)),2):
  d=tuple(sub(x,y) for x,y in zip(V[i],V[j]))
  assert sgn(sub(dot(d,d),(4,0)))>=0
  if dot(d,d)==(4,0):E.append((i,j))
 assert len(E)==48
 assert all(sum(i in e for e in E)==4 for i in range(24))
 assert all(dot(V[i],V[j])==(3,2) for i,j in E)
 # Sorted nonnegative normals a>b>c>0, normalized to a=100.
 # The six sign combinations exhaust A<B,E; A<C<E; B<E, with B,C unordered.
 witnesses=[(100,20,10),(100,40,15),(100,40,25),(100,60,10),(100,60,30),(100,90,85)]
 wanted=[((1,1,1,1),8),((-1,1,1,1),12),((-1,1,-1,1),12),((-1,-1,1,1),12),((-1,-1,-1,1),12),((-1,-1,-1,-1),12)]
 outputs=[]
 for (a,b,c),(pattern,expected_n) in zip(witnesses,wanted):
  assert a>b>c>0
  A=sub(sub((a,0),mul(rr,(b,0))),(c,0))
  B=add(sub((a,0),mul(rr,(b,0))),(c,0))
  C=sub(sub((a,0),(b,0)),mul(rr,(c,0)))
  H=sub(add((a,0),(b,0)),mul(rr,(c,0)))
  got=tuple(sgn(x) for x in [A,B,C,H])
  assert got==pattern,(got,pattern)
  u=((a,0),(b,0),(c,0))
  sg=[sgn(dot(v,u)) for v in V]
  assert all(t!=0 for t in sg)
  n=sum(sg[i]!=sg[j] for i,j in E)
  assert n==expected_n,(pattern,n)
  outputs.append((pattern,n))
 # A<C, A<B, B<H, C<H follow directly from a>b>c>0;
 # hence the only possible strict patterns are the six above.
 assert len(set(k for k,n in outputs))==6
 r=1+sqrt(2)
 theta=acos((7+4*sqrt(2))/17)
 p8=3-12*theta/pi;p12=1-p8
 den=sqrt(r*r+1)*sqrt((r+1)**2+2)+r*sqrt((r+1)**2+2)+(r+1)*sqrt(r*r+1)+r*(r+1)+1
 p8_solid=24/pi*atan(1/den)
 assert abs(p8-p8_solid)<1e-13
 assert abs(8*p8+12*p12-48*theta/pi)<1e-13
 assert 0<p8<1
 print('EXACT_SIGN_CHAMBERS_OK')
 print('vertices=24 edges=48 edge_squared_length=4')
 print('sign_pattern_to_section_sides='+repr(outputs))
 print('angle='+repr(theta),'P8='+repr(p8),'P12='+repr(p12))
 print('independent_cone_check='+repr(p8_solid))
if __name__=='__main__':check()
