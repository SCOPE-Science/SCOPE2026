"""Independent exact transversal checker: enumerate symbol bijections and group common-six entries."""
from itertools import permutations,combinations
from collections import defaultdict,Counter,deque

def permutation_sign(seq):
    inv=0
    for x in range(len(seq)):
        for y in range(x):
            if seq[y]>seq[x]:inv^=1
    return 1-2*inv

def verify(n):
    maps=[]
    for symbols in permutations(range(n)):
        cols=tuple((r+symbols[r])%n for r in range(n))
        if len(set(cols))==n: maps.append((cols,symbols))
    maps.sort()
    # For a transversal edge exactly n-3 entries agree: group each object by its n-3 fixed rows.
    buckets=defaultdict(list)
    for vid,(col,sym) in enumerate(maps):
        for rows in combinations(range(n),n-3):
            buckets[(rows, tuple(col[r] for r in rows))].append(vid)
    adj=[set() for _ in maps]
    for block in buckets.values():
        for x,y in combinations(block,2):
            assert sum(maps[x][0][r]!=maps[y][0][r] for r in range(n))==3
            adj[x].add(y);adj[y].add(x)
    assert sum(map(len,adj))%2==0
    par=defaultdict(set)
    for v,(col,sym) in enumerate(maps):par[(permutation_sign(col),permutation_sign(sym))].add(v)
    seen=set(); comps=[]
    for v in range(len(maps)):
        if v in seen:continue
        seen.add(v);q=deque([v]);count=0
        while q:
            u=q.popleft();count+=1
            for w in adj[u]:
                if w not in seen:seen.add(w);q.append(w)
        comps.append(count)
    for k,C in par.items():
        # Connectivity certificate in each class, independent of component processing.
        start=min(C);vis={start};q=[start]
        for u in q:
            for w in adj[u]:
                assert w in C
                if w not in vis:vis.add(w);q.append(w)
        if n==9:assert vis==C
    print('n',n,'orthomorphisms',len(maps),'trades',sum(map(len,adj))//2,
          'parity_sizes',dict(sorted((k,len(v)) for k,v in par.items())),
          'components',dict(sorted(Counter(comps).items())),
          'degree_multiset',dict(sorted(Counter(map(len,adj)).items())))
    return maps,adj,par
if __name__=='__main__':
    for n in (5,7,9):verify(n)
    print('VERIFY_B_OK')
