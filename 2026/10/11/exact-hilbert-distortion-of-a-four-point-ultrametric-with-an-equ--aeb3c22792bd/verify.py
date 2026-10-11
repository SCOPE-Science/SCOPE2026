#!/usr/bin/env python3
"""Exact-rational tests for a 3D Lipschitz ball family."""
from fractions import Fraction as Q
from itertools import combinations,product

def det(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
         -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
         +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def solve(A,b):
 d=det(A)
 if not d: return None
 return tuple(det([[b[i] if j==k else A[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))

def in_ball(x,t):
 return all(abs(z)<=1 for z in x) and max(x)-min(x)<=t

def Qform(x,r):
 mean=sum(x)/3
 return sum((z-mean)**2 for z in x)+3*r*mean**2

def vertices(t):
 C=[]
 for i in range(3):
  for s in (-1,1):
   row=[Q(0)]*3;row[i]=Q(s);C.append((row,Q(1)))
 for i,j in combinations(range(3),2):
  for s in (-1,1):
   row=[Q(0)]*3;row[i]=Q(s);row[j]=Q(-s);C.append((row,t))
 return {x for co in combinations(C,3) if (x:=solve([e[0] for e in co],[e[1] for e in co])) is not None and in_ball(x,t)}

def test(t):
 vs=vertices(t)
 expected=set()
 for s in (-1,1):
  for v in [(Q(1),)*3,(Q(1),Q(1),Q(1)-t),(Q(1),Q(1)-t,Q(1)-t)]:
   for i in range(3):
    rot=v[i:]+v[:i]
    expected.add(tuple(s*a for a in rot))
 assert vs==expected,(t,len(vs),vs^expected)
 r=t*t/(2*(3-t*t));d2=(7-2*t-t*t)/(3-t*t)
 M=max(map(lambda x: Qform(x,r),vs))
 m=t*t/2
 assert M/m==d2,(t,M,m,d2)
 assert Qform((t/2,-t/2,Q(0)),r)==m
 s=(1-r)/(1+2*r)
 assert Qform((Q(1),s,s),r)==m
 for mult in [Q(1,100),Q(1,2),Q(1),Q(2),Q(7),Q(100)]:
  R=r*mult
  MX=max(Qform(v,R) for v in vs)
  MA=(3*R/(1+2*R)) if R<=t/(3-2*t) else 2*t*t/3+R*(3-2*t)**2/3
  mn=min(t*t/2,MA)
  assert MX/mn>=d2
 return len(vs),d2

if __name__=='__main__':
 arr=[Q(1,20),Q(1,10),Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10),Q(1)]
 for t in arr:
  n,d=test(t);print(f't={t} vertices={n} d_BM^2={d}')
 print(f'ALL_EXACT_CHECKS_PASS {len(arr)} parameter values, 6 alternative ellipsoid scales each')
