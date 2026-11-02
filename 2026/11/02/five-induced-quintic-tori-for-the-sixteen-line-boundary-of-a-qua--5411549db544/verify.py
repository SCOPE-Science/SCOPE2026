#!/usr/bin/env python3
"""Exact integral graph and Frobenius check for a quartic del Pezzo boundary."""
from collections import Counter, deque
from math import gcd

I=range(5)
Q=('Q',)
E=lambda i:('E', i%5)
L=lambda i,j:('L', tuple(sorted((i%5,j%5))))
V={Q}|{E(i) for i in I}|{L(i,j) for i in I for j in I if i<j}
assert len(V)==16
EDGE=lambda a,b:frozenset((a,b))
G=set()
for i in I:
    G.add(EDGE(Q,E(i)))
    for j in I:
        if j!=i:G.add(EDGE(E(i),L(i,j)))
for i in I:
 for j in I:
  if i>=j:continue
  for k in I:
   for l in I:
    if k>=l or (i,j)>=(k,l):continue
    if len({i,j,k,l})==4:G.add(EDGE(L(i,j),L(k,l)))
assert len(G)==40
assert all(sum(v in e for e in G)==5 for v in V)
assert sum(EDGE(a,b) in G and EDGE(a,c) in G and EDGE(b,c) in G for a in V for b in V for c in V if len({a,b,c})==3)==0
assert sorted(Counter([tuple(sorted([a[0] for a in edge])) for edge in G]).values())==[5,15,20]

def sigma(v):
 if v==Q:return Q
 if v[0]=='E':return E(v[1]+1)
 return L(*(t+1 for t in v[1]))
def shift(e):return EDGE(*(sigma(v) for v in e))
assert {shift(e) for e in G}==G

def orbits(items, action):
 remaining=set(items); out=[]
 while remaining:
  e=next(iter(remaining)); orb=[]; x=e
  while x not in orb:
   orb.append(x); assert x in remaining
   remaining.remove(x); x=action(x)
  assert x==e
  out.append(orb)
 return out

v_orb=orbits(V,sigma)
e_orb=orbits(G,shift)
assert sorted(map(len,v_orb))==[1,5,5,5]
assert sorted(map(len,e_orb))==[5]*8
FLAGS={(e,v) for e in G for v in e}
f_orb=orbits(FLAGS,lambda t:(shift(t[0]),sigma(t[1])))
assert sorted(map(len,f_orb))==[5]*16

A=lambda i:L(i,i+1)
B=lambda i:L(i,i+2)
TREE={EDGE(Q,E(i)) for i in I}|{EDGE(E(i),A(i)) for i in I}|{EDGE(E(i),B(i)) for i in I}
assert len(TREE)==15 and TREE<=G and {shift(e) for e in TREE}==TREE
neighbors={v:set() for v in V}
for ed in TREE:
 a,b=tuple(ed);neighbors[a].add(b); neighbors[b].add(a)
visited={Q}; queue=deque([Q])
while queue:
 v=queue.popleft()
 for u in neighbors[v]-visited:
  visited.add(u);queue.append(u)
assert visited==V
FREE=G-TREE
assert len(FREE)==25
free_orb=orbits(FREE,shift)
assert sorted(map(len,free_orb))==[5]*5

# Orient each non-tree-edge orbit compatibly with the order-five action.
# Each corresponding integral fundamental cycle is permuted, not merely over Q.
orient={}
for orb in free_orb:
 first=orb[0]
 a,b=tuple(first)
 for k,e in enumerate(orb):
  assert EDGE(a,b)==e
  orient[e]=(a,b)
  a,b=sigma(a),sigma(b)
for e,(a,b) in orient.items():
 assert orient[shift(e)]==(sigma(a),sigma(b))

# Construct the fundamental cycle as a signed 1-chain; verify Frobenius
# permutes the integral basis exactly, including signs on tree edges.
all_edges=sorted(G,key=lambda ed:str(sorted(ed)))
base={e:i for i,e in enumerate(all_edges)}
canonical={e:tuple(sorted(e,key=str)) for e in G}
def elementary(u,v):
 e=EDGE(u,v)
 return 1 if canonical[e]==(u,v) else -1

def path(start,end):
 parent={start:None}; queue=deque([start])
 while queue and end not in parent:
  u=queue.popleft()
  for v in neighbors[u]:
   if v not in parent:parent[v]=u;queue.append(v)
 assert end in parent
 result=[];current=end
 while parent[current] is not None:
  result.append((parent[current],current))
  current=parent[current]
 return list(reversed(result))

def cycle(e):
 a,b=orient[e]
 c={e:elementary(a,b)}
 for u,v in path(b,a):
  edge=EDGE(u,v);c[edge]=elementary(u,v)
 return c

def map_chain(c):
 result={}
 for ed,coef in c.items():
  a,b=canonical[ed]
  aa,bb=sigma(a),sigma(b)
  dest=shift(ed)
  result[dest]=coef*elementary(aa,bb)
 return result
for e in FREE:
 assert map_chain(cycle(e))==cycle(shift(e))

# Zeta factor verification by closed point orbit data.
def fixed(orb,n):return sum(len(x) for x in orb if n%len(x)==0)
for q in [2,3,4,5,7,11]:
 for n in range(1,21):
  Lcount=fixed(v_orb,n)
  Ecount=fixed(e_orb,n)
  Fcount=fixed(f_orb,n)
  nD=(q**n+1)*Lcount+Ecount-Fcount
  nS=q**(2*n)+q**n+1+(5*q**n if n%5==0 else 0)
  nU=nS-nD
  assert nD== ((16*q**n-24) if n%5==0 else (q**n+1))
  assert nU== ((q**n-5)**2 if n%5==0 else q**(2*n))
  assert nD>=0 and nU>=0
  assert nU==q**(2*n)+(5-2*q**n)*(5 if n%5==0 else 0)
 print('q=',q,'surface=',q*q+q+1,'boundary=',q+1,'complement=',q*q,'torus_card=',(q**5-1)**5)

# A degree-five closed blowup centre exists over every finite field: the
# five Frobenius conjugates of any degree-five element on XZ=Y^2.
# All five points are distinct, and every line meets this nonsingular
# conic in at most two geometric points (Bezout), so general position holds.
print('VERTEX_ORBITS',sorted(map(len,v_orb)))
print('EDGE_ORBITS',sorted(map(len,e_orb)))
print('BRANCH_ORBITS',sorted(map(len,f_orb)))
print('TREE_EDGE_COUNT',len(TREE),'FREE_EDGE_ORBITS',len(free_orb))
print('CHARACTER_LATTICE','Z[C5]^5','RANK',len(FREE))
print('GENUS',len(G)-len(V)+1)

# Independent realization of the Clebsch graph in the even half-cube.
EVEN={mask for mask in range(32) if mask.bit_count()%2==0}
def vect(v):
 if v==Q:return 0
 if v[0]=='E':return 31^(1<<v[1])
 return sum(1<<i for i in v[1])
assert len({vect(v) for v in V})==16
assert {frozenset((vect(a),vect(b))) for a,b in [tuple(e) for e in G]}=={
 frozenset((a,b)) for a in EVEN for b in EVEN if a<b and (a^b).bit_count()==4
}
def cycle_bits(x):return sum(((x>>i)&1)<<((i+1)%5) for i in I)
assert all(vect(sigma(v))==cycle_bits(vect(v)) for v in V)
# Any even signed lift of a 5-cycle is conjugate to the pure cycle
# by an even signed translation, since 1+sigma has no kernel on EVEN.
for signs in EVEN:
 conjugators=[delta for delta in EVEN if delta^cycle_bits(delta)==signs]
 assert len(conjugators)==1
print('EVEN_SIGNED_FIVE_CYCLE_LIFTS',len(EVEN),'ALL_ONE_CONJUGACY_CLASS')

print('VERIFY_OK')
