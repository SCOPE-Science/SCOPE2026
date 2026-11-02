#!/usr/bin/env python3
"""Independent GF(11^2) direct Cartier-coefficient census for three quotients.

Field is F_11[t]/(t^2-2), stored as a+11*b. Polynomial powers are
computed directly from input branch polynomials; no symbolic Hasse formula
or factorization is used in this checker.
"""
from collections import Counter
P=11
N=121

def add(x,y):return ((x%P+y%P)%P)+11*((x//P+y//P)%P)
def neg(x):return (-(x%P))%P+11*((-(x//P))%P)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x%P,x//P;c,d=y%P,y//P
 return (a*c+2*b*d)%P+11*((a*d+b*c)%P)
def power(x,n):
 v=1
 while n:
  if n&1:v=mul(v,x)
  x=mul(x,x);n//=2
 return v

def pmul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  if not ai:continue
  for j,bj in enumerate(b):
   if bj:z[i+j]=add(z[i+j],mul(ai,bj))
 return z
def ppow(a,n):
 z=[1]
 while n:
  if n&1:z=pmul(z,a)
  if n>1:a=pmul(a,a)
  n>>=1
 return z

def det2(a,b,c,d):return sub(mul(a,d),mul(b,c))

def squarefree_valid(u):return u not in (0,2,9)

def M2(u):
 q=[1,neg(u),1]
 f=pmul([10,0,0,0,1],q)
 poly=ppow(f,5)
 return (poly[10],poly[9],poly[21],poly[20])
def H1(u,v):
 f=pmul([1,neg(u),1],[1,neg(v),1])
 return ppow(f,5)[10]

m_cache={u:M2(u) for u in range(N) if squarefree_valid(u)}
for u,M in m_cache.items():
 d=det2(*M)
 if u in (5,6):assert M==(0,0,0,0)
 else:assert d!=0, ('unexpected genus2 Cartier rank',u,M)

# Independent arithmetic census: extract the matrices and elliptic Hasse
# coefficients from the polynomials in each field, then compare with the
# predicted rank stratification only after computing them independently.
counts=Counter(); field11=Counter(); isolated=[]; rank2=[]
for u in m_cache:
 for v in m_cache:
  if u==v:continue
  mu=m_cache[u];mv=m_cache[v]
  gen2rank=(0 if mu==(0,0,0,0) else 2)+(0 if mv==(0,0,0,0) else 2)
  ell=H1(u,v)
  rank=gen2rank+(ell!=0)
  an=(5-rank)
  exp=5-2*(u in (5,6))-2*(v in (5,6))-(ell==0)
  assert rank==exp
  counts[rank]+=1
  if u<11 and v<11:field11[rank]+=1
  if rank==1:isolated.append((u,v,ell))
  if rank==2:rank2.append((u,v))
assert sorted((u,v) for u,v,_ in isolated)==[(5,6),(6,5)]
assert all(e==4 for u,v,e in isolated)
assert len(rank2)==16
assert sum(counts.values())==118*117
assert set(counts)=={1,2,3,4,5}
assert sum(field11.values())==8*7
print('GF121_DIRECT_GENUS5_CARTIER_RANKS_16_2_OK')
print('GF121_COUNTS',dict(sorted(counts.items())))
print('GF11_COUNTS',dict(sorted(field11.items())))
print('RANK1_PAIRS',isolated)
print('RANK2_COUNT',len(rank2))
