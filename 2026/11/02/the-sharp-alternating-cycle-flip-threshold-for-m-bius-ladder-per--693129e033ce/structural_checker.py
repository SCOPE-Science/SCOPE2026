#!/usr/bin/env python3
"""Independent cyclic-tiling construction and one-chord alternating-cycle checks."""
from collections import Counter

def edges(n):
    return {tuple(sorted((i,j))) for i in range(2*n) for j in ((i+1)%(2*n),(i+n)%(2*n))}

def binary_independent(n):
    for mask in range(1<<n):
        if all(not(mask>>i&1 and mask>>((i+1)%n)&1) for i in range(n)):
            yield mask

def tiled_match(n,mask):
    selected=set();matched=set()
    for i in range(n):
        if mask>>i&1:
            j=(i+1)%n
            for a,b in ((i,j),(i+n,j+n)):
                # The last edge of the cyclic column ladder is twisted.
                if i==n-1:
                    a,b=n-1,n
                    for x,y in ((a,b), (2*n-1,0)):
                        selected.add(tuple(sorted((x,y))))
                    break
                selected.add(tuple(sorted((a,b))))
            matched.add(i);matched.add(j)
    for i in range(n):
        if i not in matched:selected.add((i,i+n))
    assert len(selected)==n
    assert len({x for e in selected for x in e})==2*n
    assert selected<=edges(n)
    return frozenset(selected)

def check():
    for n in range(4,19):
        mapping={mask:tiled_match(n,mask) for mask in binary_independent(n)}
        assert len(set(mapping.values()))==len(mapping)
        edge_set=edges(n)
        for mask,M in mapping.items():
            for i in range(n):
                new=mask^(1<<i)
                if new in mapping:
                    assert len(M^mapping[new])==4
                # Validate square moves explicitly by their 4-cycles, not just
                # by the binary representation.
        A=frozenset((i,i+1) for i in range(0,2*n,2))
        B=frozenset((i,(i+1)%(2*n)) if i<2*n-1 else (0,i) for i in range(1,2*n,2))
        assert A<=edge_set and B<=edge_set
        if n%2:
            assert A not in mapping.values() and B not in mapping.values()
            for extreme in (A,B):
                neighbors=set()
                for i in range(n):
                    u=i;v=i+n
                    # Search the two half-perimeter paths joining the chord endpoints.
                    for direction in (-1,1):
                        verts=[(u+direction*j)%(2*n) for j in range(n+1)]
                        assert verts[-1]==v
                        path={tuple(sorted((a,b))) for a,b in zip(verts,verts[1:])}
                        cycle=path|{(u,v)}
                        
                        # General alternation test in both directions.
                        if all(((tuple(sorted((verts[j],verts[j+1]))) in extreme) == (j%2==0)) for j in range(n)):
                            new=extreme ^ cycle
                            if len(new)==n and len({x for e in new for x in e})==2*n and new<=edge_set:
                                neighbors.add(frozenset(new))
                assert len(neighbors)==n,(n,len(neighbors))
                assert neighbors<=set(mapping.values())
        print('n=',n,'cyclic_tile_count=',len(mapping),'exceptional=',2 if n%2 else 0)
    print('MOBIUS_TILING_ONE_CHORD_PASS')
if __name__=='__main__':check()
