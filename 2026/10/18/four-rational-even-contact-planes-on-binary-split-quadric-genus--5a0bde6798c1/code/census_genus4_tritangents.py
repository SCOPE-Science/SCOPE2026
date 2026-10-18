#!/usr/bin/env python3
"""Exact arithmetic over F2: canonical (3,3) curves and rational tritangents.
Each 16-bit mask encodes F=sum F_{i,j} s^i t^(3-i) r^j w^(3-j).
A rational hyperplane of the Segre embedding is (1,1) on P1xP1.
Its intersection is a tritangent if its divisor on the smooth curve is twice an effective divisor.
Requires Python 3 and SymPy; no third-party research data.
"""
from itertools import product
from collections import Counter,defaultdict
import multiprocessing as mp
import sympy as S
import json,sys

u,v=S.symbols('u v')
GL=[(a,b,c,d) for a,b,c,d in product(range(2),repeat=4) if a*d+b*c==1]
P=[(1,0),(0,1),(1,1)]

def prod_bin(a,b):
 z=0
 while a:
  p=a&(-a);z^=b<<(p.bit_length()-1);a^=p
 return z

def bin_power(a,n):
 z=1
 for _ in range(n):z=prod_bin(z,a)
 return z

def tritangent_constraints():
 cons=[]
 for a,b,c,d in GL:
  r=d|(b<<1);w=c|(a<<1)
  subs=[prod_bin(1<<i,prod_bin(bin_power(r,j),bin_power(w,3-j))) for i in range(4) for j in range(4)]
  masks=tuple(sum(1<<k for k,bits in enumerate(subs) if bits>>m&1) for m in (1,3,5))
  cons.append(("smooth_"+str((a,b,c,d)),masks))
 for px,py in product(P,P):
  A,B=px;C,D=py
  fy=[sum(1<<(4*i+j) for i in range(4) if A**i*B**(3-i)) for j in range(4)]
  fx=[sum(1<<(4*i+j) for j in range(4) if C**j*D**(3-j)) for i in range(4)]
  def cubic_rel(z,p):
   if p==(1,0):return (z[3],z[1])
   if p==(0,1):return (z[2],z[0])
   return(z[3]^z[2],z[1]^z[0])
  cons.append(("reducible_"+str((px,py)),cubic_rel(fy,py)+cubic_rel(fx,px)))
 return cons

CONS=tritangent_constraints()

def tritangents(F):
 return tuple(name for name,masks in CONS if all((F&m).bit_count()%2==0 for m in masks))

def nonsingular(F):
 one=S.groebner([1],u,v,modulus=2)
 for i_chart in (True,False):
  for j_chart in (True,False):
   f=0
   for i in range(4):
    for j in range(4):
     if (F>>(4*i+j))&1:f+=u**(i if i_chart else 3-i)*v**(j if j_chart else 3-j)
   if S.groebner([f,S.diff(f,u),S.diff(f,v)],u,v,modulus=2)!=one:return False
 return True

def worker(start_end):
 start,end=start_end
 totals=Counter();smooth=0;maxima=[]
 for F in range(start,end):
  if not nonsingular(F):continue
  k=len(tritangents(F))
  totals[k]+=1;smooth+=1
  if k>=4:maxima.append(F)
 return (totals,smooth,maxima)

def transform(F,A,B,swap=False):
 def single(M):
  a,b,c,d=M
  return [prod_bin(bin_power((a<<1)|b,i),bin_power((c<<1)|d,3-i)) for i in range(4)]
 sx=single(A);sy=single(B)
 out=0
 for i in range(4):
  for j in range(4):
   if not (F>>(4*i+j))&1:continue
   for k in range(4):
    for h in range(4):
     if sx[i]>>k&1 and sy[j]>>h&1:
      out^=1<<(4*h+k if swap else 4*k+h)
 return out

def orbits(masks):
 vals=set(masks);orb=[]
 while vals:
  f=min(vals)
  orbit={transform(f,A,B,sw) for A,B,sw in product(GL,GL,(False,True))}
  assert orbit<=set(masks),(f,orbit-set(masks))
  vals-=orbit
  orb.append({'representative':f,'size':len(orbit),'stabilizer':72//len(orbit)})
 return orb

