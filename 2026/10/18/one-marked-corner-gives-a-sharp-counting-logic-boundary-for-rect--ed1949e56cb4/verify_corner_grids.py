"""Finite cross-checks for one-corner-coloured Cartesian grids.
Run: python3 verify_corner_grids.py (Python >=3.8, standard library only).
Proofs for arbitrary sizes are given separately; finite tests are not a proof.
"""
from collections import defaultdict, Counter


def grid(m,n):
    adj=[set() for _ in range(m*n)]
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for a,b in ((i+1,j),(i,j+1)):
                if a<m and b<n:
                    v=a*n+b;adj[u].add(v);adj[v].add(u)
    return adj


def refine(graphs):
    """Canonical, jointly encoded 1-WL colours, with vertex zero distinguished."""
    starts=[[(0 if v==0 else 1) for v in range(len(g))] for g in graphs]
    colors=starts
    for _ in range(1000):
        signs=[[(colors[k][u],tuple(sorted(colors[k][v] for v in g[u])))
                for u in range(len(g))] for k,g in enumerate(graphs)]
        code={s:i for i,s in enumerate(sorted(set(s for ss in signs for s in ss)))}
        nxt=[[code[s] for s in ss] for ss in signs]
        if nxt==colors:
            return colors
        colors=nxt
    raise AssertionError('refinement did not stabilize')


def switch(g,n):
    h=[set(x) for x in g]
    a=0*n+2;b=0*n+3;c=2*n+0;d=3*n+0
    assert b in h[a] and d in h[c] and d not in h[a] and b not in h[c]
    for x,y in ((a,b),(c,d)):
        h[x].remove(y);h[y].remove(x)
    for x,y in ((a,d),(c,b)):
        h[x].add(y);h[y].add(x)
    return h


def connected(g):
    seen={0};todo=[0]
    for x in todo:
        for y in g[x]-seen:
            seen.add(y);todo.append(y)
    return len(seen)==len(g)


def cyc4(g,sets):
    # Exactly one vertex from each specified stable colour class, in order.
    A,B,C,D=sets;answer=0
    for a in A:
      for b in B:
       if b not in g[a]:continue
       for c in C:
        if c not in g[b]:continue
        for d in D:
         if d in g[c] and a in g[d]:answer+=1
    return answer

count=0
for m in range(2,13):
 for n in range(m,15):
    g=grid(m,n)
    c=refine([g])[0]
    cells=defaultdict(set)
    for v,col in enumerate(c): cells[col].add((v//n,v%n))
    got={frozenset(x) for x in cells.values()}
    if m<n:
        exp={frozenset({(i,j)}) for i in range(m) for j in range(n)}
    else:
        exp={frozenset({(i,j),(j,i)}) for i in range(n) for j in range(i,n)}
    assert got==exp,(m,n,'wrong refinement partition')
    if m==n and m>=4:
        h=switch(g,n)
        c0,c1=refine([g,h]);assert Counter(c0)==Counter(c1),(m,'WL mismatch')
        assert connected(h),(m,'switched disconnected')
        def classverts(pair):
            i,j=pair
            return {i*n+j,j*n+i}
        S=[classverts(pair) for pair in ((0,2),(0,3),(1,3),(1,2))]
        assert cyc4(g,S)==2 and cyc4(h,S)==0,(m,'cycle witness failure')
    count+=1
print('PASS:',count,'grid sizes; canonical partitions, switched witnesses, connectivity and colour-sensitive four-cycle counts')
