#!/usr/bin/env python3
"""Exact arithmetic certificate for rational Gauss bijections in binary plane curves.
Python 3 + SymPy. Enumerates incidence assignments and all relevant jets.
"""
import itertools
import collections
from functools import lru_cache
import sympy as sp

P=[p for p in itertools.product(range(2),repeat=3) if any(p)]
X=sp.symbols('x y z')

def mons(d):return [(i,j,d-i-j) for i in range(d+1) for j in range(d+1-i)]
def ev(m,p,v):
 if v is not None and not (m[v]&1):return 0
 return int(all((m[j]-(int(v==j)) if v is not None else m[j])==0 or p[j] for j in range(3)))

def line(p,vals):
 k=next(i for i,b in enumerate(p) if b)
 other=[i for i in range(3) if i!=k]
 g=[0]*3
 for i,v in zip(other,vals):g[i]=v
 g[k]=sum(p[i]*g[i] for i in other)%2
 return sum(w<<i for i,w in enumerate(g))

MATCH=[]
for vals in itertools.product(((0,1),(1,0),(1,1)),repeat=7):
 ls=tuple(line(p,t) for p,t in zip(P,vals))
 if len(set(ls))==7:
  jet=sum((b<<(3*i+1)) | (c<<(3*i+2)) for i,(b,c) in enumerate(vals))
  MATCH.append((ls,jet))
assert len(MATCH)==24
print('Fano incidence bijections:',len(MATCH))

def jet_space(d):
 M=mons(d);J=[]
 for p in P:
  k=next(i for i,b in enumerate(p) if b)
  J.append((p,None))
  J.extend((p,i) for i in range(3) if i!=k)
 col=[sum(ev(m,p,v)<<i for i,(p,v) in enumerate(J)) for m in M]
 piv={};ker=[]
 for i,w in enumerate(col):
  t=w;c=1<<i
  while t:
   j=t.bit_length()-1
   if j in piv:t^=piv[j][0];c^=piv[j][1]
   else:piv[j]=(t,c);break
  if not t:ker.append(c)
 def solve(target):
  a=0;t=target
  while t:
   j=t.bit_length()-1
   if j not in piv:return None
   t^=piv[j][0];a^=piv[j][1]
  return a
 return M,len(piv),ker,solve

def polynomial(d,mask):
 return sum((X[0]**a*X[1]**b*X[2]**c for i,(a,b,c) in enumerate(mons(d)) if mask>>i&1),sp.Integer(0))

def geometric_smooth(d,mask,show=False):
 F=polynomial(d,mask); data=[]
 for k in range(3):
  v=[X[i] for i in range(3) if i!=k]
  f=sp.Poly(F.subs(X[k],1),*v,modulus=2)
  gb=sp.groebner([f.as_expr(),f.diff(v[0]).as_expr(),f.diff(v[1]).as_expr()],*v,order='lex',modulus=2)
  ps=tuple(str(h.as_expr()) for h in gb.polys)
  data.append(ps)
  if not any(h.as_expr()==1 for h in gb.polys) and not show:return False
 if show:return data
 return True

for d in (3,4,5):
 M,rank,K,solve=jet_space(d)
 compatible=[solve(t) for lines,t in MATCH]
 accepted=[mask for mask in compatible if mask is not None and geometric_smooth(d,mask)]
 print('degree',d,'coefficients',len(M),'jet-rank',rank,'matching-compatible',sum(m is not None for m in compatible),'geometrically smooth',len(accepted),'first-mask',hex(compatible[0]) if compatible[0] is not None else '-',flush=True)
 if d in (4,5):
  print('degree',d,'representative polynomial:',polynomial(d,compatible[0]))
  print('degree',d,'representative chart GB:',geometric_smooth(d,compatible[0],True),flush=True)
 assert (len(accepted) == (24 if d==4 else 0))

D=6
M,rank,K,solve=jet_space(D)
assert rank==21 and len(K)==7
A=solve(MATCH[0][1]); assert A is not None
L=[0]
for u in K:L=L+[v^u for v in L]
assert len(L)==128
SMOOTH=[];SING=[]
for k in L:
 m=A^k
 (SMOOTH if geometric_smooth(6,m) else SING).append(m)
print('degree 6 rank',rank,'kernel',len(K),'smooth-lifts',len(SMOOTH),'singular-lifts',len(SING),flush=True)
print('singular degree-6 coefficient mask',hex(SING[0]))
assert len(SMOOTH)==127 and len(SING)==1
w=min(SMOOTH)
print('smooth sextic witness',hex(w),polynomial(6,w),'chart GB',geometric_smooth(6,w,True),flush=True)

# Exact GL3(F2) action, three elementary generating substitutions.
IDX={m:i for i,m in enumerate(M)}
@lru_cache(None)
def substitution(m,forms):
 ps={(0,0,0):1}
 for i,n in enumerate(m):
  for _ in range(n):
   ns=collections.defaultdict(int)
   for e,c in ps.items():
    if c:
     for j in range(3):
      if forms[i]>>j&1:
       a=list(e);a[j]+=1;ns[tuple(a)]^=1
   ps={a:c for a,c in ns.items() if c}
 return sum(1<<IDX[a] for a,c in ps.items() if c)
GEN=((2,1,4),(3,2,4),(1,4,2))
ACT=[[substitution(m,g) for m in M] for g in GEN]
def transformed(mask,act):
 n=0
 while mask:
  bit=mask&-mask;n^=act[bit.bit_length()-1];mask-=bit
 return n
seen=set();orbits=[]
for seed in SMOOTH:
 if seed in seen:continue
 todo=[seed];orb={seed}
 while todo:
  m=todo.pop()
  for act in ACT:
   q=transformed(m,act)
   if q not in orb:orb.add(q);todo.append(q)
 seen.update(orb);orbits.append((min(orb),len(orb)))
assert len(seen)==24*127
assert all(geometric_smooth(6,m) for m in SMOOTH)
print('degree 6 smooth total',len(seen),'orbits',len(orbits),'orbit-size-distribution',sorted(collections.Counter(n for a,n in orbits).items()),flush=True)
print('degree 6 orbit representatives',[(hex(m),n) for m,n in sorted(orbits)])
