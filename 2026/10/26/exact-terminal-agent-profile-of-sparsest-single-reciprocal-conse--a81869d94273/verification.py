from itertools import combinations
from collections import Counter
from math import comb

def formula(N):
 F={2:1}
 for n in range(3,N+1):
  F[n]=sum((-1)**(r+1)*comb(n-2,r)*F[n-r]*((n-r)*(n-r-1))**r for r in range(1,n-1))
 return F

def removable(E,n):
 return [v for v in range(2,n) if sum((u,v) in E for u in range(n) if u!=v)==1 and sum((v,u) in E for u in range(n) if u!=v)==1 and next(u for u in range(n) if (u,v) in E)!=next(u for u in range(n) if (v,u) in E)]

def generated(n):
 states={(frozenset([0,1]), frozenset([(0,1),(1,0)]))}
 for _ in range(2,n):
  nxt=set()
  for active,E in states:
   for v in range(2,n):
    if v in active:continue
    for u in active:
     for w in active:
      if u!=w: nxt.add((active|{v},E|{(u,v),(v,w)}))
  states=nxt
 return {E for active,E in states}

def brute(n):
 core=frozenset({(0,1),(1,0)})
 other=[(u,v) for u in range(n) for v in range(n) if u!=v and (u,v) not in core]
 result=set()
 for choice in combinations(other,2*(n-2)):
  E=core | set(choice)
  if any((u,v) in E and (v,u) in E for u in range(n) for v in range(u+1,n) if (u,v)!=(0,1)):
   continue
  # Exist a valid reverse-elimination sequence for each graph (small n).
  def reduce(V,E):
   if len(V)==2:return E==core
   for v in V:
    if v in (0,1):continue
    ind=[u for u in V if (u,v) in E]
    out=[u for u in V if (v,u) in E]
    if len(ind)==len(out)==1 and ind[0]!=out[0]:
     if reduce(V-{v},frozenset((u,w) for (u,w) in E if v not in (u,w))):return True
   return False
  if reduce(frozenset(range(n)),E): result.add(E)
 return result

F=formula(9)
print('formula',F)
for n in range(3,7):
 G=generated(n)
 hist=Counter(len(removable(E,n)) for E in G)
 pred={k:comb(n-2,k)*sum((-1)**j*comb(n-2-k,j)*F[n-k-j]*((n-k-j)*(n-k-j-1))**(k+j) for j in range(n-1-k)) for k in range(1,n-1)}
 assert len(G)==F[n],(n,len(G),F[n])
 assert dict(sorted(hist.items()))==pred,(n,hist,pred)
 print('n',n,'distinct',len(G),'hist',dict(sorted(hist.items())))
 if n<=5:
  B=brute(n)
  assert G==B,('brute_difference',n,len(G),len(B))
  print('brute check n',n,'OK')
print('ALL OK')
