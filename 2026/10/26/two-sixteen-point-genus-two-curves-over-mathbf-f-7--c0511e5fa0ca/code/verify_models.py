#!/usr/bin/env python3
"""Independent model checks: branch degrees, F_7 and F_49 point counts.
F_49=F_7[u]/(u^2-3); no external packages.
"""
from itertools import product
Q=7
A=[(1,0,0,0,0,0,1),(4,0,3,0,3,0,1)]

def mul(x,y):
 a,b=x;c,d=y
 return ((a*c+3*b*d)%Q,(a*d+b*c)%Q)

def add(x,y):return ((x[0]+y[0])%Q,(x[1]+y[1])%Q)

def exp(x,n):
 o=(1,0)
 while n:
  if n%2:o=mul(o,x)
  x=mul(x,x);n//=2
 return o

field=list(product(range(7),repeat=2))
assert len(set(field))==49
assert all(exp(x,49)==x for x in field)
squares={mul(y,y) for y in field}
assert len(squares)==25

def evaluate(a,x):
 v=(0,0)
 for t in reversed(a):v=add(mul(v,x),(t,0))
 return v

def count(a,base):
 s={mul(y,y) for y in base}
 total=2 # leading coefficient 1 is a square, both infinity points
 for x in base:
  v=evaluate(a,x)
  total+=1 if v==(0,0) else 2 if v in s else 0
 return total

def tr(p):
 p=[a%7 for a in p]
 while p and p[-1]==0:p.pop()
 return p

def modpol(f,g):
 f=tr(f);g=tr(g)
 while len(f)>=len(g):
  c=f[-1]*pow(g[-1],-1,7)%7
  for j in range(len(g)):f[len(f)-len(g)+j]=(f[len(f)-len(g)+j]-c*g[j])%7
  f=tr(f)
 return f

def mulpol(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%7
 return tr(z)

def powpol(a,n,m):
 o=[1]
 while n:
  if n&1:o=modpol(mulpol(o,a),m)
  a=modpol(mulpol(a,a),m);n//=2
 return o

def gcd(f,g):
 f=tr(f);g=tr(g)
 while g:f,g=g,modpol(f,g)
 return f

for i,a in enumerate(A):
 assert count(a,[(j,0) for j in range(7)])==16
 n49=count(a,field)
 print('class',i+1,'N7',16,'N49',n49,'Weil_middle',(14+n49)//2)
 assert n49==(46 if i==0 else 44)
 if i==0:
  p=mulpol(mulpol([1,0,1],[2,0,1]),[4,0,1])
  assert tuple(p)==a
  for c in [1,2,4]:assert (-c)%7 not in {1,2,4}
  print('branch_factors=[x²+1,x²+2,x²+4] degrees=[2,2,2]')
 else:
  f=list(a)
  # Rabin irreducibility test for degree 6: x^(7^6)=x,
  # gcd(x^(7^(6/r))-x,f)=1 for distinct primes r=2,3.
  assert powpol([0,1],7**6,f)==[0,1]
  for k in [2,3]:
   z=powpol([0,1],7**k,f)
   z[1]=(z[1]-1)%7
   assert len(gcd(f,z))==1
  print('branch_factor_degrees=[6] Rabin_test=passed')
print('MODEL_CHECK_OK')
