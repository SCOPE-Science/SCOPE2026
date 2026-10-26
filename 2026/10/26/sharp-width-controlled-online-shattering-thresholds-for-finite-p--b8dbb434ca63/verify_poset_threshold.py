#!/usr/bin/env python3
"""Finite independent checks for the extremal threshold of order-ideal Littlestone dimension.
No external packages. A naturally labeled poset represents every poset up to relabeling.
"""
from functools import lru_cache
from collections import defaultdict
import math

def lower_threshold(w,k):
    assert 1 <= w <= k
    q,r=divmod(k,w)
    return (w+r)*(1<<q)-w

def closure_relation(n,mask):
    upper=[0]*n
    s=0
    for i in range(n):
      for j in range(i+1,n):
        if mask>>s&1: upper[i]|=1<<j
        s+=1
    # Transitive closure for forward topological order
    for i in range(n-1,-1,-1):
      for j in range(i+1,n):
        if upper[i]>>j&1: upper[i]|=upper[j]
    return tuple(upper)

def ideals(upper):
    n=len(upper)
    down=[0]*n
    for a in range(n):
      for b in range(a+1,n):
        if upper[a]>>b&1:down[b]|=1<<a
    ans=[]
    for mask in range(1<<n):
      if all(not(mask>>i&1) or ((mask&down[i])==down[i]) for i in range(n)):
        ans.append(mask)
    return ans

def width(upper):
    n=len(upper)
    best=0
    for mask in range(1<<n):
      if mask.bit_count()<=best:continue
      if all(not(mask>>i&1) or (mask&upper[i])==0 for i in range(n)):
        best=mask.bit_count()
    return best

def Ldim(sets,n):
    coordinate=[sum(1<<a for a,s in enumerate(sets) if s>>i&1) for i in range(n)]
    @lru_cache(maxsize=None)
    def go(universe):
      return max((1+min(go(universe&yes),go(universe&~yes))
                for yes in coordinate if universe&yes and universe&~yes),default=0)
    return go((1<<len(sets))-1)

def expected_disjoint_balanced(upper,w,k):
    n=len(upper); q,r=divmod(k,w)
    sizes=sorted([2**q-1]*(w-r)+[2**(q+1)-1]*r)
    # Undirected components of comparability graph, no cross-comparabilities.
    unseen=set(range(n)); comps=[]
    while unseen:
      st=[unseen.pop()]; comp=[]
      while st:
        a=st.pop();comp.append(a)
        connected={b for b in unseen if ((upper[a]>>b&1) if a<b else (upper[b]>>a&1))}
        unseen-=connected;st+=list(connected)
      comps.append(comp)
    if sorted(map(len,comps))!=sizes:return False
    return all(all(((upper[a]>>b&1) if a<b else (upper[b]>>a&1))
                   for j,a in enumerate(comp) for b in comp[j+1:]) for comp in comps)

def connected(upper):
    n=len(upper);seen={0};change=True
    while change:
      change=False
      for a in range(n):
        for b in range(a+1,n):
          if upper[a]>>b&1 and ((a in seen) != (b in seen)):
            seen.add(a);seen.add(b);change=True
    return len(seen)==n

def verify(nmax=6):
  for n in range(1,nmax+1):
    distinct=set();posets=[]
    for arcs in range(1<<(n*(n-1)//2)):
      order=closure_relation(n,arcs)
      if order in distinct:continue
      distinct.add(order)
      w=width(order)
      sets=ideals(order)
      d=Ldim(sets,n)
      posets.append((order,w,d,len(sets)))
      assert w<=d<=math.floor(math.log2(len(sets))), (n,order,w,d)
      assert n>=lower_threshold(w,d),(n,order,w,d)
      if n==lower_threshold(w,d):
        assert expected_disjoint_balanced(order,w,d),(n,order,w,d)
    extrema=defaultdict(int)
    for order,w,d,c in posets:extrema[(w,d)]+=1
    print(f'n={n}: {len(posets)} distinct naturally labeled posets; max Ldim by width:',
          [(w,max(d for _,a,d,_ in posets if a==w)) for w in range(1,n+1)],
          'rigidity verified',flush=True)
  # Infinite sharpness parameter arithmetic, complete small grid
  for w in range(1,11):
    for k in range(w,30):
      q,r=divmod(k,w)
      lengths=[(1<<q)-1]*(w-r)+[(1<<(q+1))-1]*r
      assert sum(lengths)==lower_threshold(w,k)
      assert sum((a+1).bit_length()-1 for a in lengths)==k
  print('ALL_POSET_WIDTH_THRESHOLD_CHECKS_PASS',flush=True)
if __name__=='__main__':verify()
