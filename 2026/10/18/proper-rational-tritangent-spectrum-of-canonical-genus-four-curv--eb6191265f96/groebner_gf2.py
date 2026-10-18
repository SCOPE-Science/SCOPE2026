"""Self-contained exact Groebner engine over F2 for 3-var affine charts."""
from nonsplit_genus4 import BASIS
from itertools import combinations
import json,time,collections
Q={(1,1,0,0),(0,0,2,0),(0,0,1,1),(0,0,0,2)}

def add(p,q):return p.symmetric_difference(q)
def mul(p,q):
 r=set()
 for a in p:
  for b in q:
   z=tuple(a[i]+b[i] for i in range(3))
   if z in r:r.remove(z)
   else:r.add(z)
 return r

def diff(p,i):return {tuple(a[j]-(j==i) for j in range(3)) for a in p if a[i]%2}

def affine_form(p,j):
 r=set()
 for a in p:
  z=a[:j]+a[j+1:]
  if z in r:r.remove(z)
  else:r.add(z)
 return r

def lm(p):return max(p,key=lambda t:(sum(t),*t))
def div(a,b):return all(x>=y for x,y in zip(a,b))
def shift(p,t):return {tuple(a[i]+t[i] for i in range(3)) for a in p}

def reduction(f,G):
 out=set();f=set(f)
 while f:
  t=lm(f)
  for g,head in G:
   if div(t,head):
    f.symmetric_difference_update(shift(g,tuple(t[i]-head[i] for i in range(3))))
    break
  else:
   f.remove(t);out.add(t)
 return out

def groebner_unit(polys):
 G=[];pairs=[]
 for f in polys:
  if not f:continue
  f=reduction(f,G)
  if f:
   if f=={(0,0,0)}:return True
   h=lm(f);G.append((f,h))
   pairs.extend((i,len(G)-1) for i in range(len(G)-1))
 while pairs:
  i,j=pairs.pop()
  f,a=G[i];g,b=G[j]
  # product criterion: coprime monomial leading terms
  if all(min(a[k],b[k])==0 for k in range(3)):continue
  L=tuple(max(a[k],b[k]) for k in range(3))
  sp=add(shift(f,tuple(L[k]-a[k] for k in range(3))),shift(g,tuple(L[k]-b[k] for k in range(3))))
  r=reduction(sp,G)
  if r:
   if r=={(0,0,0)}:return True
   h=lm(r);pairs.extend((i,len(G)) for i in range(len(G)))
   G.append((r,h))
 return False

MONS=[{m} for m in BASIS]

def geom_smooth(mask):
 F=set()
 for i,m in enumerate(BASIS):
  if mask>>i&1:F.add(m)
 for chart in range(3):
  q=affine_form(Q,chart);f=affine_form(F,chart)
  dq=[diff(q,i) for i in range(3)];df=[diff(f,i) for i in range(3)]
  minors=[add(mul(dq[i],df[j]),mul(dq[j],df[i])) for i,j in combinations(range(3),2)]
  if not groebner_unit([q,f,*minors]):return False
 return True
