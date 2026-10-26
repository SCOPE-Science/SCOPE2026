#!/usr/bin/env python3
"""Finite-field spot checks of the reduced support formula; not an infinite proof."""
from itertools import product, combinations
from math import comb

def e2(vals,p):
 return sum(x*y for x,y in combinations(vals,2))%p
for p in [2,3,5]:
 for n in range(4,9 if p==2 else (7 if p==3 else 6)):
  for d in range(4,n+1):
   k=n-d+2; Q=1; L=k-1
   while L%p==0:Q*=p;L//=p
   planes=Q>2
   diag=comb(k,2)%p==0
   index_sets=list(combinations(range(n),k))
   count=0
   for x in product(range(p),repeat=n):
    actual=all(e2([x[j] for j in I],p)==0 for I in index_sets)
    expect= (any(all(x[j]==x[(i+1)%n] for j in range(n) if j!=i) for i in range(n)) if planes else (sum(v!=0 for v in x)<=1 or (diag and len(set(x))==1)))
    if actual!=expect:
     raise AssertionError((p,n,d,x,actual,expect))
    count+=actual
   print(p,n,d,'planes' if planes else 'axes+diag' if diag else 'axes',count)
print('VERIFY_OK')
