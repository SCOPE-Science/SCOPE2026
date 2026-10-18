"""Independent vertex-level check of rooted cyclic-clique products; stdlib only."""
from collections import Counter, defaultdict

def verify(n,m):
    V=[(a,b) for a in range(n) for b in range(m)]
    neighbours={v: tuple(sorted(set([((v[0]+1)%n,v[1]),((v[0]-1)%n,v[1])] + [(v[0],j) for j in range(m) if j!=v[1]]))) for v in V}
    c={v: int(v==(0,0)) for v in V}
    def cls(col):
        dd=defaultdict(set)
        for v,k in col.items():dd[k].add(v)
        return frozenset(frozenset(s) for s in dd.values())
    def step(col):
        sig={v:(col[v], tuple(sorted(Counter(col[w] for w in neighbours[v]).items()))) for v in V}
        sig_values=sorted(set(sig.values()))
        key={k:i for i,k in enumerate(sig_values)}
        return {v:key[sig[v]] for v in V}
    orbits=defaultdict(set)
    for a,b in V:orbits[(min(a,n-a), b!=0)].add((a,b))
    expected=frozenset(frozenset(s) for s in orbits.values())
    prev=cls(c)
    for t in range(n*m+1):
        if prev==expected:
            assert cls(step(c))==prev,(n,m,t,'unstable')
            return t,len(prev)
        c=step(c)
        new=cls(c)
        assert len(new)>len(prev),(n,m,t,'premature stabilization')
        prev=new
    raise AssertionError('no convergence')

total=0
pairs=0
for n in range(5,61):
    for m in range(2,9):
        t,cells=verify(n,m)
        d=n//2
        target=d+int(n==5 and m==2)
        assert t==target,(n,m,t,target)
        assert cells==2*(d+1),(n,m,cells)
        pairs+=1;total+=n*m
print(f'VERTEX_PASS pairs={pairs} vertices={total} n=5..60 m=2..8')
