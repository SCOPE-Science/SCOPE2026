"""Exact Euler-transform coefficients and independent exhaustive conjugacy-orbit checks.

Usage: python3 CHECKER.py (Python standard library only).
"""

import itertools, math
from functools import lru_cache

def compose(t,u):return tuple(u[i] for i in t)

def invperm(p): return tuple(p.index(i) for i in range(len(p)))

def permute(f,p,pi):return tuple(p[f[pi[i]]] for i in range(len(p)))

def direct_orbit_counts(n):
 maps=list(itertools.product(range(n),repeat=n)); ps=list(itertools.permutations(range(n)))
 idem={a for a in maps if compose(a,a)==a}
 allpairs=[]
 for t in maps:
  if compose(compose(t,t),t)!=t: continue
  t2=compose(t,t)
  for e in idem:
   if compose(t,e)!=e or compose(e,t)!=e: continue
   allpairs.append((t,e, len({t,t2,e})==3))
 seen=set(); r3=0; nt=0
 for t,e,flag in allpairs:
  if (t,e) in seen: continue
  nt+=1;r3+=flag
  for p in ps:
   pinv=invperm(p)
   seen.add((permute(t,p,pinv),permute(e,p,pinv)))
 assert len(seen)==len(allpairs),(n,len(seen),len(allpairs))
 return (len(allpairs),nt,r3)

def mul(a,b,N):
 c=[0]*(N+1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:N+1-i]):
    if y:c[i+j]+=x*y
 return c

def geometric(N,k,power=1):
 import math
 a=[0]*(N+1)
 for i in range(N//k+1): a[i*k]=math.comb(power+i-1,i)
 return a

def polys(N):
 base=[0]+[1]*N
 part=[1]+[0]*N
 pair=[1]+[0]*N
 for j in range(1,N+1): part=mul(part,geometric(N,j),N)
 for j in range(2,N+1): pair=mul(pair,geometric(N,j,j//2),N)
 b0=mul(base,part,N)
 b=mul(b0,pair,N)
 def transform(c):
  out=[1]+[0]*N
  for k in range(1,N+1):
   if c[k]:out=mul(out,geometric(N,k,c[k]),N)
  return out
 a=transform(b);a0=transform(b0)
 return b,b0,a,a0,[a[i]-a0[i] for i in range(N+1)]

if __name__=='__main__':
 N=13
 b,b0,a,a0,r=polys(N)
 print('block coefficients',b)
 print('r3 coefficients',r)
 for n in range(1,6):
  x=direct_orbit_counts(n)
  print('n',n,'raw pairs,total orbit,r3 orbit',x,'OGF total',a[n],'r3',r[n]);assert x[1:]==(a[n],r[n])
