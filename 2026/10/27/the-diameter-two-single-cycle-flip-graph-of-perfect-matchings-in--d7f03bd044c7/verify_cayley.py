"""Finite primal cycle-space check for triangle-expanded prism matching flips."""
import collections

def check(n):
    vertices=2*n
    edges=sorted({tuple(sorted(p)) for i in range(n) for p in
                  ((i,(i+1)%n),(n+i,n+(i+1)%n),(i,n+i))})
    adj=[[] for _ in range(vertices)]
    for k,(u,v) in enumerate(edges):
        adj[u].append((v,k)); adj[v].append((u,k))
    cycles=set()
    def extend(root,at,visited,mask):
        for nxt,edge in adj[at]:
            if nxt==root and len(visited)>=3:
                cycles.add(mask|(1<<edge))
            elif nxt>root and nxt not in visited:
                extend(root,nxt,visited|{nxt},mask|(1<<edge))
    for root in range(vertices):extend(root,root,{root},0)
    cycle_space=set()
    # Build all even subgraphs from independent fundamental cycles.
    for u,v in edges:pass
    basis={}
    for c in cycles:
        residue=c
        for pivot in sorted(basis,reverse=True):
            if (residue>>pivot)&1:residue^=basis[pivot]
        if residue:basis[residue.bit_length()-1]=residue
    states={0}
    for b in basis.values():states|={s^b for s in tuple(states)}
    assert len(states)==2**(n+1)
    assert len(cycles)==2**n+n*(n-1)
    assert cycles.issubset(states)
    # A cycle XOR another cycle gives all remaining even subgraphs.
    assert all(s in cycles or any((s^c) in cycles for c in cycles)
               for s in states if s)
    print('n=%d vertices=%d cycles=%d distance_counts=(1,%d,%d)'
          %(n,len(states),len(cycles),len(cycles),len(states)-len(cycles)-1))
for n in range(3,10):check(n)
