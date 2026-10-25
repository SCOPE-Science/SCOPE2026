"""Exact center-assignment exhaustive check of optimum dissociation exchange for square rook graphs."""
from itertools import combinations
from collections import defaultdict,Counter,deque
from math import comb, factorial

def optima(n):
    assert n%3==0
    k=n//3
    vertices=range(n)
    allm=[]
    # choose center rows/cols then assign leaves as unordered pairs to labeled centers
    def assign(centers,leaves):
        centers=tuple(sorted(centers)); leaves=tuple(sorted(leaves))
        if not centers:
            yield ()
            return
        c=centers[0]
        for pp in combinations(leaves,2):
            remain=tuple(x for x in leaves if x not in pp)
            for rest in assign(centers[1:],remain):
                yield ((c,pp),)+rest
    for A in combinations(vertices,k):
      D=set(vertices)-set(A)
      for B in combinations(vertices,k):
        C=set(vertices)-set(B)
        for fp in assign(A,C):
          left_edges={(a,c) for a,pair in fp for c in pair}
          for gp in assign(B,D):
            E=left_edges|{(d,b) for b,pair in gp for d in pair}
            allm.append(sum(1<<(a*n+b) for a,b in E))
    assert len(set(allm))==len(allm)
    return allm

def graph(n):
    M=optima(n);size=len(M);k=n//3
    idx={m:i for i,m in enumerate(M)}
    adj=[set() for _ in M];reduced=defaultdict(list)
    for i,m in enumerate(M):
      bits=[b for b in range(n*n) if m>>b&1]
      for a,b in combinations(bits,2):
        reduced[m^(1<<a)^(1<<b)].append(i)
    for group in reduced.values():
      for u,v in combinations(group,2):
        if (M[u]^M[v]).bit_count()==4:
          adj[u].add(v);adj[v].add(u)
    counts=Counter(map(len,adj));assert counts==Counter({4*k*k+8*comb(k,2):size}), (n,counts)
    seen={0};todo=[0]
    for u in todo:
        for v in adj[u]:
            if v not in seen:seen.add(v);todo.append(v)
    assert len(seen)==size,(n,len(seen),size)
    expected=comb(n,k)**2*(factorial(2*k)//2**k)**2
    assert size==expected,(size,expected)
    print({'n':n,'maximum_size':4*k,'optima':size,'degree_two_replacements':next(iter(counts)),'components_two_replacements':1,'degree_one_replacements':0})
if __name__=='__main__':
 for n in (3,6):graph(n)
