"""Finite verification of minimum-domination exchange for rook graphs.
Usage: python3 verify_bruteforce.py
No external dependencies.
"""
from itertools import combinations
from collections import Counter, deque, defaultdict
from math import factorial, comb

def run(n):
    vertices=range(n*n)
    dom=[]
    for tup in combinations(vertices,n):
        selected=set(tup)
        if all((i in selected or any(i//n==j//n or i%n==j%n for j in selected)) for i in vertices):
            dom.append(sum(1<<i for i in tup))
    lookup={s:i for i,s in enumerate(dom)}
    neigh=[set() for s in dom]
    for i,s in enumerate(dom):
        for old in vertices:
            if not (s>>old)&1: continue
            t=s^(1<<old)
            for new in vertices:
                if new==old or ((t>>new)&1):continue
                j=lookup.get(t | (1<<new))
                if j is not None:neigh[i].add(j)
    assert all(i in neigh[j] for i,nn in enumerate(neigh) for j in nn)
    assert len(dom)==2*n**n-factorial(n)
    assert sum(map(len,neigh))//2==n*(n-1)*n**n+factorial(n)*n*(n-1)**2
    degrees=Counter(map(len,neigh))
    wanted=Counter()
    wanted[2*n*(n-1)]+=factorial(n)
    wanted[(n+2)*(n-1)]+=2*factorial(n)*comb(n,2)
    wanted[n*(n-1)]+=len(dom)-factorial(n)-2*factorial(n)*comb(n,2)
    assert degrees==wanted,(n,degrees,wanted)
    def bfs(root):
        ds=[-1]*len(dom); ds[root]=0; todo=deque([root])
        while todo:
            u=todo.popleft()
            for v in neigh[u]:
                if ds[v]==-1:ds[v]=ds[u]+1;todo.append(v)
        assert -1 not in ds
        return max(ds)
    if n<=4:
        e=[bfs(i) for i in range(len(dom))]
        assert min(e)==n and max(e)==max(n,2*n-3)
        freq=dict(sorted(Counter(e).items()))
    else:
        # One representative of each orbit under independent row/column permutations and transpose.
        classes={}
        for i,s in enumerate(dom):
            cell=[(k//n,k%n) for k in vertices if s>>k&1]
            rows=Counter(r for r,c in cell); cols=Counter(c for r,c in cell)
            if len(rows)==n:
                t=tuple(sorted(cols.values(),reverse=True))
            else:
                t=tuple(sorted(rows.values(),reverse=True))
            classes.setdefault(t,i)
        e={p:bfs(i) for p,i in classes.items()}
        assert min(e.values())==n and max(e.values())==2*n-3
        freq=e
    print('BRUTE_PASS',n,'vertices',len(dom),'edges',sum(map(len,neigh))//2,'degree_frequency',dict(sorted(degrees.items())),'ecc',freq)

for n in range(2,6):run(n)
print('ROOK_BRUTEFORCE_PASS')

def rectangular(m,n):
    assert m<n
    verts=range(m*n)
    sol=[]
    for cells in combinations(verts,m):
        s=set(cells)
        if all(any((q//n==i//n or q%n==i%n) for q in s) for i in verts):
            sol.append(frozenset(s))
    idx={v:i for i,v in enumerate(sol)}
    assert len(sol)==n**m
    degree=[]
    for s in sol:
        neighbors=set()
        for out in s:
            for x in verts:
                if x in s: continue
                t=(s-{out})|{x}
                if frozenset(t) in idx:neighbors.add(idx[frozenset(t)])
        degree.append(len(neighbors))
    assert set(degree)=={m*(n-1)}
    print('RECTANGLE_PASS',m,n,len(sol),sum(degree)//2)
for a,b in [(2,3),(2,4),(3,4),(3,5)]:rectangular(a,b)
