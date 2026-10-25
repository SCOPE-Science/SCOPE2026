"""Minimal exact two-variable Buchberger unit-ideal test over GF(2)."""
from itertools import combinations

def add(a,b): return a.symmetric_difference(b)
def mon_shift(p,i,j):return frozenset((a+i,b+j) for a,b in p)
def lt(p):return max(p)
def divisible(a,b):return a[0]>=b[0] and a[1]>=b[1]
def reduce(p, G):
 p=frozenset(p); rem=frozenset()
 while p:
  m=lt(p)
  g=next((g for g in G if divisible(m,lt(g))),None)
  if g is None:
   rem=add(rem,frozenset((m,)))
   p=add(p,frozenset((m,)))
  else:
   n=lt(g)
   p=add(p,mon_shift(g,m[0]-n[0],m[1]-n[1]))
 return rem

def is_unit(polynomials):
 G=[frozenset(g) for g in polynomials if g]
 if frozenset(((0,0),)) in G:return True
 pairs=list(combinations(range(len(G)),2))
 while pairs:
  a,b=pairs.pop()
  p,q=G[a],G[b]
  m,n=lt(p),lt(q);u,v=max(m[0],n[0]),max(m[1],n[1])
  s=add(mon_shift(p,u-m[0],v-m[1]),mon_shift(q,u-n[0],v-n[1]))
  r=reduce(s,G)
  if r:
   if r==frozenset(((0,0),)):return True
   k=len(G)
   pairs.extend((i,k) for i in range(k))
   G.append(r)
 return False

def derivative(P,i):
 return frozenset((a-1,b) for a,b in P if a&1) if i==0 else frozenset((a,b-1) for a,b in P if b&1)

def smooth(F):
 if not F:return False
 for sx in [False,True]:
  for sy in [False,True]:
   P=frozenset((i if not sx else 2-i,j if not sy else 3-j) for i in range(3) for j in range(4) if (F>>(4*i+j))&1)
   if not is_unit([P,derivative(P,0),derivative(P,1)]):return False
 return True

if __name__ == '__main__':
    S=[i for i in range(1,4096) if smooth(i)]
    print('smooth_sections=',len(S))
    assert len(S)==1116
