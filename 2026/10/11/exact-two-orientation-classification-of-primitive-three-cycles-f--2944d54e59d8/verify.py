#!/usr/bin/env python3
"""Exact rational diagnostic for three-cycles of the farthest-projection triangle map."""
from fractions import Fraction as F

def p(x,y): return (F(x),F(y))
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(t,x): return (t*x[0],t*x[1])
def dot(x,y): return x[0]*y[0]+x[1]*y[1]
def norm2(x): return dot(x,x)

def check_triangle(u,v):
 A=p(0,0);B=p(1,0);C=p(u,v)
 starts=(A,B,C);dirs=(sub(B,A),sub(C,B),sub(A,C))
 def proj(x,i):
  d=dirs[i]
  return add(starts[i],mul(dot(sub(x,starts[i]),d)/norm2(d),d))
 def farthest(x,i):
  options=[j for j in range(3) if j!=i]
  vals=[(norm2(sub(x,proj(x,j))),j) for j in options]
  if vals[0][0]==vals[1][0]:return x,i
  j=max(vals)[1]
  return proj(x,j),j
 a=u*u+v*v;b=(u-1)**2+v*v;s=a-u+1
 cond0=(a*b>u*u and a>(u-1)**2 and b>(a-u)**2)
 cond1=(a*b>(u-1)**2 and b>u*u and a>(a-u)**2)
 P=((u/s,F(0)),((u+v*v)/s,v*(1-u)/s),(u/s,v/s))
 Q=((a/s,F(0)),(u*u/s,u*v/s),(a/s,v/s))
 for cond,points,itinerary in [(cond0,P,(0,1,2)),(cond1,Q,(0,2,1))]:
  current=points[0];line=itinerary[0]
  matches=True
  for k in range(3):
   current,line=farthest(current,line)
   matches=matches and current==points[(k+1)%3] and line==itinerary[(k+1)%3]
  if cond != matches:
   raise AssertionError((u,v,cond,matches,points,itinerary))
  if cond and len(set(points))!=3:
   raise AssertionError(('not primitive',u,v,points))
 return int(cond0)+int(cond1)

if __name__=='__main__':
 counts=[0,0,0]
 for nu in range(-12,25):
  for nv in range(1,33):
   r=check_triangle(F(nu,8),F(nv,8))
   counts[r]+=1
 assert counts[0]>0 and counts[1]>0 and counts[2]>0
 assert check_triangle(F(1,2),F(1,1))==2
 assert check_triangle(F(-1,5),F(6,5))==1
 assert check_triangle(F(1,2),F(1,4))==0
 print('CHECK_OK exact rational triangles:',sum(counts),'counts',counts)
