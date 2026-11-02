from itertools import permutations, product
from math import factorial
from fractions import Fraction
from collections import Counter

def weak_orders(n):
  for k in range(1,n+1):
    for a in product(range(k),repeat=n):
      if len(set(a))==k:yield a

def parts(n):
  # restricted-growth strings
  def rec(a):
    if len(a)==n:
      yield tuple(a);return
    for v in range(max(a)+2):
      yield from rec(a+[v])
  return list(rec([0]))

def trans(g, p):return tuple(g[v] for v in p)

def canonical_cycles(p):
  n=len(p);used=set();cy=[]
  for i in range(n):
    if i not in used:
      j=i;c=[]
      while j not in used:used.add(j);c.append(j);j=p[j]
      cy.append(c)
  return cy

def blocks_join(n,rels):
  f=list(range(n))
  def root(x):
    while f[x]!=x:x=f[x]
    return x
  def union(x,y):f[root(x)]=root(y)
  for a in rels:
    for i in range(n):
      for j in range(i):
        if a[i]==a[j]:union(i,j)
  return len({root(i) for i in range(n)})

def power(g,k):
  out=list(range(len(g)))
  for _ in range(k):out=[g[v] for v in out]
  return tuple(out)

def forb(n,g,p,ell):
  a=[]
  for j in range(ell):
    gj=power(g,j);a.append(tuple(p[gj[i]] for i in range(n)))
  gl=power(g,ell)
  # g^ell orbits force equality
  a.append(tuple(min(c) for c in [next(c for c in canonical_cycles(gl) if i in c) for i in range(n)]))
  return blocks_join(n,a)

def mublocks(p):
  from math import factorial
  res=1
  for v in set(p):
    b=p.count(v);res*=(-1)**(b-1)*factorial(b-1)
  return res

def fub(n):
  from math import comb
  v=[1]
  for k in range(1,n+1):v.append(sum(comb(k,j)*v[k-j] for j in range(1,k+1)))
  return v[n]

def formula(n,r):
  groups=list(permutations(range(n)));permsr=list(permutations(range(r)));P=parts(n)
  acc=0
  for g in groups:
    for pi in permsr:
      t=0
      for p in P:
        term=mublocks(p)
        for cyc in canonical_cycles(pi):term*=fub(forb(n,g,p,len(cyc)))
        t+=term
      acc+=t
  return Fraction(acc,factorial(n)*factorial(r))

def brute(n,r):
  orders=list(weak_orders(n));norders=len(orders);valid=[]
  for tup in product(orders,repeat=r):
    if all(any(o[i]!=o[j] for o in tup) for i in range(n) for j in range(i)):valid.append(tup)
  unseen=set(valid);orbits=[]
  while unseen:
    t=next(iter(unseen));cl=set()
    for g in permutations(range(n)):
      for pi in permutations(range(r)):
        cl.add(tuple(tuple(t[pi[c]][g[i]] for i in range(n)) for c in range(r)))
    assert cl <= set(valid)
    unseen-=cl;orbits.append(len(cl))
  return len(orbits),len(valid),Counter(orbits)
if __name__=='__main__':
    expected = {(1,2):1,(2,2):3,(3,2):15,(4,2):108,(5,2):1045,
                (1,3):1,(2,3):5,(3,3):80,(4,3):3053,(5,3):216879,
                (2,4):8,(3,4):320}
    for (n,r), answer in expected.items():
        observed = formula(n,r)
        assert observed == answer, (n,r,observed,answer)
    for n,r in [(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(2,4),(3,4)]:
        orbit_count,number_of_configs,orbit_lengths=brute(n,r)
        assert orbit_count==expected[(n,r)]
        assert sum(size*mult for size,mult in orbit_lengths.items())==number_of_configs
    print('ALL_CHECKS_OK formula_cases=%d brute_cases=8'%len(expected))
