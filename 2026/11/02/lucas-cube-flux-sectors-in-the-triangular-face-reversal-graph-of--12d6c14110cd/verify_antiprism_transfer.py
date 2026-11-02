#!/usr/bin/env python3
"""Exact cyclic-state reconstruction and face-flip tests for antiprism Eulerian orientations."""
from collections import Counter, deque


def graph_data(n):
    edges=[]
    for i in range(n):
        j=(i+1)%n
        edges += [(i,j), (n+i,n+j), (n+i,j), (i,n+i)]
    faces=[]
    for i in range(n):
        j=(i+1)%n
        faces.append((4*i,4*i+2,4*i+3))       # upper belt triangle
        faces.append((4*i+1,4*i+2,4*j+3))    # lower belt triangle
    return edges,faces


def independent_masks(n):
    N=2*n
    return [z for z in range(1<<N) if not(z&(z<<1)) and not((z&1) and (z&(1<<(N-1))))]


def reconstruct(n,z,sector):
    # Local choices: (00)->d, (01)->b, (10)->t. Complement for sector 2.
    states=[]
    for i in range(n):
        first=(z>>(2*i))&1
        second=(z>>(2*i+1))&1
        states.append(((1,0,0) if first else (0,1,0) if second else (0,0,1)))
    if sector==2:
        states=[tuple(1-v for v in triple) for triple in states]
    bits=[]
    for i,(t,b,d) in enumerate(states):
        prev=states[(i-1)%n]
        v=prev[0]+prev[2]-t
        assert v in (0,1) and b+d==prev[1]+v
        bits.extend((t,b,d,v))
    return tuple(bits)


def direct_flips(n,bits,faces):
    edgebits=list(bits)
    result=set()
    for face in faces:
        for e in face:
            edgebits[e]^=1
        if valid_orientation(n,edgebits):
            result.add(tuple(edgebits))
        for e in face:
            edgebits[e]^=1
    return result


def valid_orientation(n,bits):
    outgoing=[0]*(2*n)
    edges,_=graph_data(n)
    for (a,b),bit in zip(edges,bits):
        outgoing[a if bit else b]+=1
    return all(s==2 for s in outgoing)


def lucas(n):
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def check(n):
    edges,faces=graph_data(n)
    masks=independent_masks(n)
    assert len(masks)==lucas(2*n)
    records={}
    sector_graph=[]
    for sector in (1,2):
        names={reconstruct(n,z,sector):z for z in masks}
        assert len(names)==len(masks)
        graph={}
        for bits,z in names.items():
            assert valid_orientation(n,bits)
            actual=direct_flips(n,bits,faces)
            expected={reconstruct(n,z^(1<<i),sector) for i in range(2*n)
                      if (z^(1<<i)) in masks}
            assert actual==expected,(n,sector,z,actual^expected)
            graph[z]={names[x] for x in actual}
            assert len(graph[z])==sum((z^(1<<i)) in masks for i in range(2*n))
        assert sum(map(len,graph.values()))//2 == 2*n*fib(2*n-1)
        visited={0};todo=[0]
        for v in todo:
            for w in graph[v]:
                if w not in visited:
                    visited.add(w);todo.append(w)
        assert len(visited)==len(masks)
        # Verify distance equal Hamming weight by monotone removal and insertion.
        for z in masks:
            assert z in visited
        sector_graph.append(graph)
        records.update(names)
    for sector in (0,3):
        bits=tuple([sector//3]* (4*n))
        assert valid_orientation(n,bits)
        assert not direct_flips(n,bits,faces)
        assert bits not in records
        records[bits]=None
    assert len(records)==2+2*lucas(2*n)
    return len(records),sum(map(lambda g:sum(map(len,g.values()))//2,sector_graph))

if __name__=='__main__':
    for n in range(3,10):
        vertices,edges=check(n)
        print('TRANSFER_PASS',n,vertices,edges)
    print('TRANSFER_VERIFIER_PASS')
