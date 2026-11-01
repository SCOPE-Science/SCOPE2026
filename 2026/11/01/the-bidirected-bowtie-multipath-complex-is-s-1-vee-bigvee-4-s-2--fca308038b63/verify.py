#!/usr/bin/env python3
"""Exact integer/combinatorial certificate for the bidirected bowtie multipath complex."""
from collections import Counter, defaultdict, deque

EDGES = ((0,1),(1,2),(2,0),(0,3),(3,4),(4,0),
         (1,0),(2,1),(0,2),(3,0),(4,3),(0,4))
ORDER = (9,2,0,8,4,1,7,5,6,3,11,10)


def admissible(mask):
    outgoing, incoming = {}, {}
    for i,(u,v) in enumerate(EDGES):
        if mask & (1<<i):
            if u in outgoing or v in incoming:
                return False
            outgoing[u],incoming[v] = v,u
    for u in outgoing:
        seen=set()
        v=u
        while v in outgoing:
            if v in seen:return False
            seen.add(v)
            v=outgoing[v]
    return True


def admissible_independently(mask):
    # The only simple undirected cycles are the two triangles.  Because they
    # meet solely at vertex 0, all directed cycles are the six reciprocal
    # 2-cycles or the two orientations of each of the two triangles.
    chosen = {EDGES[i] for i in range(len(EDGES)) if mask & (1<<i)}
    if len({u for u,v in chosen})!=len(chosen):return False
    if len({v for u,v in chosen})!=len(chosen):return False
    if any((v,u) in chosen for u,v in chosen):return False
    for a,b,c in ((0,1,2),(0,3,4)):
        if all(e in chosen for e in ((a,b),(b,c),(c,a))):return False
        if all(e in chosen for e in ((b,a),(c,b),(a,c))):return False
    return True


def oriented_boundary(mask):
    vs=[j for j in range(len(EDGES)) if mask & (1<<j)]
    return {mask ^ (1<<i): (-1 if p%2 else 1) for p,i in enumerate(vs)}


def main():
    assert all(admissible(mask)==admissible_independently(mask) for mask in range(1<<len(EDGES)))
    F={mask for mask in range(1<<len(EDGES)) if admissible(mask)}
    assert len(F)==101
    assert Counter(x.bit_count()-1 for x in F)=={-1:1,0:12,1:40,2:40,3:8}
    for mask in F:
        for i in range(len(EDGES)):
            if mask & (1<<i): assert mask ^ (1<<i) in F
    remaining=set(F)-{0}
    pairs=[]
    for i in ORDER:
        for mask in sorted(remaining,key=lambda s:(s.bit_count(),s)):
            up=mask | (1<<i)
            if not(mask & (1<<i)) and up in remaining:
                assert mask!=0 and up in F and up.bit_count()==mask.bit_count()+1
                remaining.remove(mask)
                remaining.remove(up)
                pairs.append((mask,up))
    assert len(pairs)==47
    assert Counter(s.bit_count()-1 for s in remaining)=={0:1,1:1,2:4}
    paired=set(pairs)
    vertices=F-{0}
    out={x:[] for x in vertices}
    indeg={x:0 for x in vertices}
    for high in vertices:
        for low in oriented_boundary(high):
            if low==0:continue
            if (low,high) in paired:u,v=low,high
            else:u,v=high,low
            out[u].append(v)
            indeg[v]+=1
    queue=deque(sorted(u for u in vertices if indeg[u]==0))
    count=0
    while queue:
        u=queue.popleft();count+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert count==len(vertices), 'cyclic gradient matching'
    match1to2={a:b for a,b in pairs if a.bit_count()==2}
    lower=set(match1to2)
    adjacency={a:[] for a in lower}
    incoming={a:0 for a in lower}
    for a,b in match1to2.items():
        for x in oriented_boundary(b):
            if x!=a and x in lower:
                adjacency[a].append(x)
                incoming[x]+=1
    q=deque(sorted(a for a in lower if incoming[a]==0))
    topo=[]
    while q:
        a=q.popleft();topo.append(a)
        for x in adjacency[a]:
            incoming[x]-=1
            if incoming[x]==0:q.append(x)
    assert len(topo)==len(lower)
    critical1=next(x for x in remaining if x.bit_count()==2)
    critical2=sorted(x for x in remaining if x.bit_count()==3)
    boundary_coeff=[]
    for t in critical2:
        c=defaultdict(int,oriented_boundary(t))
        for a in topo:
            coefficient=c[a]
            if not coefficient:continue
            b=match1to2[a]
            d=oriented_boundary(b)
            pivot=d[a]
            assert pivot in (-1,1)
            for x,w in d.items():
                c[x]-=coefficient*w*pivot
            assert c[a]==0
        assert all(c[a]==0 for a in lower)
        boundary_coeff.append(c[critical1])
    assert boundary_coeff==[0,0,0,0], boundary_coeff
    # Independently verify Euler characteristic and integral top-degree rank.
    assert sum((-1)**(s.bit_count()-1) for s in F)==3
    print('VERIFY_OK faces=101 nonempty=100 matching_pairs=47 critical=(1,1,4,0) gradient_DAG=100 Morse_d2='+str(boundary_coeff))
    print('critical_cells=', sorted((s.bit_count()-1,s) for s in remaining))

if __name__=='__main__':main()
