#!/usr/bin/env python3
"""Finite checks for the two-particle configuration complex of a rose."""
from collections import deque
from itertools import combinations, permutations, product
from math import comb, factorial


def model(m):
    vertices = list(range(2*m+1))
    # Vertex zero is central. Loop i has outer vertices 2*i+1 and 2*i+2.
    edges = []
    types = []
    for i in range(m):
        a, b = 2*i+1, 2*i+2
        edges.extend([(0,a), (0,b), (a,b)])
        types.extend([('radial',i),('radial',i),('peripheral',i)])
    c0 = set(combinations(vertices,2))
    c1 = {(v,e) for v in vertices for e,(p,q) in enumerate(edges) if v not in (p,q)}
    c2 = {pair for pair in combinations(range(len(edges)),2)
          if set(edges[pair[0]]).isdisjoint(edges[pair[1]])}
    return vertices, edges, types, c0, c1, c2


def square_faces(edges, square):
    i,j = square
    return {(v,i) for v in edges[j]} | {(v,j) for v in edges[i]}


def check_collapses(m, data):
    vertices,edges,types,c0,c1,c2 = data
    active2 = set(c2)
    active1 = set(c1)
    stage1 = 0
    stage2 = 0

    for sq in sorted(c2):
        i,j=sq
        if types[i][0] == 'radial' and types[j][0] == 'peripheral':
            radial,peripheral=i,j
        elif types[j][0] == 'radial' and types[i][0] == 'peripheral':
            radial,peripheral=j,i
        else:
            continue
        loop=types[peripheral][1]
        face=(2*loop+1,radial)
        assert face in active1 and face in square_faces(edges,sq)
        assert [s for s in active2 if face in square_faces(edges,s)] == [sq]
        active1.remove(face)
        active2.remove(sq)
        stage1 += 1

    for sq in sorted(active2):
        i,j=sq
        assert types[i][0]==types[j][0]=='peripheral'
        face=(2*types[j][1]+1,i)
        assert face in active1 and face in square_faces(edges,sq)
        assert [s for s in active2 if face in square_faces(edges,s)] == [sq]
        active1.remove(face)
        active2.remove(sq)
        stage2 += 1

    assert not active2
    assert stage1==2*m*(m-1)
    assert stage2==comb(m,2)
    assert len(active1)==len(c1)-len(c2)
    # Connectivity of the remaining graph, not merely Euler characteristic.
    adjacency={c:set() for c in c0}
    for v,e in active1:
        p,q=edges[e]
        x=tuple(sorted((v,p)))
        y=tuple(sorted((v,q)))
        assert x in c0 and y in c0 and x!=y
        adjacency[x].add(y)
        adjacency[y].add(x)
    root=min(c0)
    seen={root}
    todo=deque([root])
    while todo:
        for v in adjacency[todo.popleft()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    assert len(seen)==len(c0)
    rank=len(active1)-len(c0)+1
    assert rank==1+3*comb(m,2)
    return len(c0),len(c1),len(c2),stage1,stage2,rank


def map_vertices(m,perm,flips):
    g={0:0}
    for i in range(m):
        j=perm[i]
        g[2*i+1]=2*j+1+flips[i]
        g[2*i+2]=2*j+2-flips[i]
    assert sorted(g.values())==list(range(2*m+1))
    return g


def predicted_trace(m,perm,flips):
    a=sum(perm[i]==i and flips[i]==0 for i in range(m))
    b=sum(perm[i]==i and flips[i]==1 for i in range(m))
    r=sum(i<perm[i] and perm[perm[i]]==i for i in range(m))
    numerator=3*a*a+2*a*b-b*b-3*a-3*b
    assert numerator%2==0
    return 1+numerator//2-r


def chain_trace(m,data,perm,flips):
    vertices,edges,types,c0,c1,c2=data
    g=map_vertices(m,perm,flips)
    eindex={frozenset(e):i for i,e in enumerate(edges)}
    im=[]
    signs=[]
    for p,q in edges:
        gp,gq=g[p],g[q]
        target=eindex[frozenset((gp,gq))]
        im.append(target)
        signs.append(1 if (gp,gq)==edges[target] else -1)
    t0=sum(tuple(sorted((g[v],g[w])))==(v,w) for v,w in c0)
    t1=sum(signs[e] for v,e in c1 if g[v]==v and im[e]==e)
    t2=0
    for i,j in c2:
        if {im[i],im[j]}=={i,j}:
            orientation=1 if im[i]==i else -1
            t2+=orientation*signs[i]*signs[j]
    return t0,t1,t2


def main():
    tested=0
    for m in range(1,6):
        data=model(m)
        stats=check_collapses(m,data)
        permutations_count=0
        symmetric_total=0
        all_total=0
        for p in permutations(range(m)):
            permutations_count+=1
            for flips in product((0,1),repeat=m):
                value=predicted_trace(m,p,flips)
                c0,c1,c2=chain_trace(m,data,p,flips)
                assert value==1-c0+c1-c2,(m,p,flips,value,c0,c1,c2)
                all_total+=value
                tested+=1
                if not any(flips):
                    symmetric_total+=value
        assert permutations_count==factorial(m)
        assert all_total==0
        assert symmetric_total==(1 if m==1 else 2)*factorial(m)
        print('m={} cells=({},{},{}) collapses=({},{}) rank={} sym_invariants={} full_invariants={} elements={}'.format(
            m,*stats[:5],stats[5],symmetric_total//factorial(m),0,factorial(m)*(2**m)))
    print('character_checks={}'.format(tested))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
