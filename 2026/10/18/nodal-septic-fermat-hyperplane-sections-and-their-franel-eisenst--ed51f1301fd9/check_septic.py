#!/usr/bin/env python3
"""Exact standalone checks of the septic hyperplane-section node enumeration."""
from collections import Counter
from itertools import product, permutations
from math import comb, factorial
import json

V = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
def powz(a,n):
 r=(1,0)
 for _ in range(n): r=mul(r,a)
 return r

def franel(n):return sum(comb(n,k)**3 for k in range(n+1))
def formula(n):return sum(comb(n,k)*(-2)**(n-k)*franel(k) for k in range(n+1))

def dp_return(n):
 states={(0,0):1}
 for _ in range(n):
  nxt={}
  for x,c in states.items():
   for v in V:
    t=add(x,v);nxt[t]=nxt.get(t,0)+c
  states=nxt
 return states.get((0,0),0)

def hist_return(n):
 val=0
 for m in product(range(n+1),repeat=5):
  leftover=n-sum(m)
  if leftover<0:continue
  c=m+(leftover,)
  if sum(c[i]*V[i][0] for i in range(6))!=0:continue
  if sum(c[i]*V[i][1] for i in range(6))!=0:continue
  den=1
  for k in c:den*=factorial(k)
  val+=factorial(n)//den
 return val

def det(M):
 n=len(M); out=(0,0)
 for p in permutations(range(n)):
  inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
  prod=(1,0)
  for i,j in enumerate(p):prod=mul(prod,M[i][j])
  out=add(out,neg(prod) if inv%2 else prod)
 return out

def first_node(n):
 for seq in product(range(6),repeat=n-1):
  if sum(V[i][0] for i in seq)+1 or sum(V[i][1] for i in seq):continue
  return seq+(0,)
 raise AssertionError('no node')

def hessian_check(n):
 seq=first_node(n)
 v=[V[i] for i in seq]
 z5=[V[(5*i)%6] for i in seq]
 d=n-2
 M=[[add(z5[i] if i==j else (0,0),z5[n-2]) for j in range(d)] for i in range(d)]
 got=det(M)
 expected= (1,0)
 for i in range(n-1):expected=mul(expected,v[i])
 expected=neg(powz(expected,5))
 assert got==expected,(n,seq,got,expected)
 return {'sample_exponents':seq,'normalized_hessian_determinant':got}

if __name__=='__main__':
 rows=[]
 for n in range(3,13):
  a=dp_return(n);b=formula(n)
  assert a==b and a%6==0,(n,a,b)
  if n<=7:
   c=hist_return(n)
   assert c==a,(n,a,c)
  q=(comb(n,n//2)//2 if n%2==0 else 0)
  assert (a//6-q)%2==0
  if n<=8:
   # A rational projective node admits a sixth-root normalization with only signs.
   rational=sum(1 for bits in product((-1,1),repeat=n-1) if sum(bits)+1==0)
   assert rational==q,(n,rational,q)
  rows.append({'coordinates':n,'zero_sum_sequences':a,'singular_projective_points':a//6,'rational_nodes':q,'quadratic_closed_points':(a//6-q)//2})
 h={str(n):hessian_check(n) for n in range(5,8)}
 assert rows[2]['singular_projective_points']==60
 assert rows[3]['singular_projective_points']==340
 print(json.dumps({'status':'VERIFY_OK','rows':rows,'hessian_sample_checks':h,'methods':'independent lattice DP, multinomial histogram, Franel binomial transform, exact Hessian determinant'},sort_keys=True,indent=2))
