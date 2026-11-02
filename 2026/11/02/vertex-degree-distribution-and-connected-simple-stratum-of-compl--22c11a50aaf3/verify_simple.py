from itertools import permutations,product
from collections import Counter,deque
from math import factorial,comb

def analyze(r,s):
    vs=[]
    for perm in permutations(range(r)):
      for gaps in product(range(r+1),repeat=s):
        c=[gaps.count(i) for i in range(r+1)]
        if all(v<=1 for v in c[1:r]):vs.append((perm,gaps))
    V=set(vs)
    start=next(iter(V)); todo=deque([start]); seen={start}
    while todo:
      p,g=todo.popleft()
      ns=[]
      for j in range(r-1):
        if j+1 not in g:
          q=list(p);q[j],q[j+1]=q[j+1],q[j];ns.append((tuple(q),g))
      for a in range(s):
        for b in (g[a]-1,g[a]+1):
          if 0<=b<=r:
            h=list(g);h[a]=b;ns.append((p,tuple(h)))
      for z in ns:
        if z in V and z not in seen: seen.add(z);todo.append(z)
    num=factorial(r)*sum(comb(r-1,j)*factorial(s)//factorial(s-j)*2**(s-j) for j in range(min(s,r-1)+1))
    assert len(V)==num,(r,s,len(V),num)
    assert len(seen)==num,(r,s,len(seen),num)
    print('PASS',r,s,num)
for r in range(2,6):
 for s in range(1,5): analyze(r,s)
