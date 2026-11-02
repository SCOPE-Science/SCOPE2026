from itertools import permutations, product
from collections import Counter
from fractions import Fraction
from math import factorial,comb

def count_direct(profiles, n, t):
  z=0
  for allocation in permutations(range(n)):
    ranks=[ [{v:p.index(v) for v in range(n)} for p in ps] for ps in profiles]
    if all(not all(r[a]<r[allocation[s]] for r in ranks[s])
           for s in range(n) for a in allocation[s+1:]):
      z+=1
  return z

def count_recursive(profiles,n):
  ranks=[ [{v:p.index(v) for v in range(n)} for p in ps] for ps in profiles]
  def f(s,remaining):
    if not remaining: return 1
    return sum(f(s+1,tuple(b for b in remaining if b != a)) for a in remaining if all(
       not all(r[b]<r[a] for r in ranks[s]) for b in remaining if b!=a))
  return f(0,tuple(range(n)))

for n,t in [(2,2),(3,2),(2,3)]:
  ps=list(permutations(range(n)))
  cnt=Counter()
  num=0
  for orders in product(ps, repeat=t*n):
    profiles=[orders[t*i:t*(i+1)] for i in range(n)]
    v=count_direct(profiles,n,t)
    w=count_recursive(profiles,n)
    assert v==w,(n,t,profiles,v,w)
    cnt[v]+=1;num+=1
  expected=Fraction(sum(k*v for k,v in cnt.items()),num)
  unique=Fraction(cnt[1],num)
  mu=lambda m:sum(Fraction((-1)**(j-1)*comb(m,j),j**(t-1)) for j in range(1,m+1))
  target=Fraction(1)
  for m in range(1,n+1):target*=mu(m)
  assert expected==target and unique==Fraction(1,factorial(n)**(t-1))
  print('n,t=',n,t,'profiles=',num,'hist=',dict(sorted(cnt.items())),'mean=',str(expected),'unique=',str(unique),'var=',str(Fraction(sum(k*k*v for k,v in cnt.items()),num)-expected*expected))
