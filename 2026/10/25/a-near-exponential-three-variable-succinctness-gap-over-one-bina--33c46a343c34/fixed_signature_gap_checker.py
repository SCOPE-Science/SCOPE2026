"""Finite tests for a binary-coded one-relation interpretation of relational vocabularies."""
from itertools import product
from random import Random
from math import ceil, log2


def encode(n, relations):
    r = len(relations)
    assert r >= 2 and n >= 1
    t = (r - 1).bit_length()
    tags = [('root',)]
    for i in range(r):
        for j in range(1, t + 2):
            tags.append(('layer', i, j))
        for j in range(1, t + 1):
            if (i >> (t-j)) & 1:
                tags.append(('marker', i, j))
    nodes = [(a,tag) for a in range(n) for tag in tags]
    adj = {x:set() for x in nodes}
    root = ('root',)
    for a in range(n):
        adj[(a,root)].add((a,root))
    for i in range(r):
        for a in range(n):
            adj[(a,root)].add((a,('layer',i,1)))
            for j in range(1,t+1):
                x=(a,('layer',i,j))
                if j<t:
                    adj[x].add((a,('layer',i,j+1)))
                if (i >> (t-j)) & 1:
                    marker=(a,('marker',i,j))
                    adj[x].add(marker)
                    adj[marker].add(marker)
            adj[(a,('layer',i,t+1))].add((a,root))
        for a,b in relations[i]:
            adj[(a,('layer',i,t))].add((b,('layer',i,t+1)))
    return tags, adj


def marker_bit(v, adj):
    return any(u!=v and u in adj[u] for u in adj[v])


def detect_anchor(v,adj):
    return v in adj[v] and any(w!=v for w in adj[v])


def coded_path(a,b,i,t,adj):
    source=(a,('root',)); target=(b,('root',))
    reachable={source}
    for step in range(1,t+3):
        nexts=set()
        for x in reachable:
            for y in adj[x]:
                if step<t+2:
                    if y in adj[y]:
                        continue
                    if step<=t and marker_bit(y,adj)!=bool((i>>(t-step))&1):
                        continue
                    nexts.add(y)
                elif detect_anchor(y,adj):
                    nexts.add(y)
        reachable=nexts
    return target in reachable


def compose(A,B,n):
    return {(a,c) for a in range(n) for c in range(n)
            if any((a,b) in A and (b,c) in B for b in range(n))}


def split_blocks(R,tags,n):
    return {(u,v): {(a,b) for a in range(n) for b in range(n)
                    if ((a,u),(b,v)) in R} for u in tags for v in tags}


def block_compose(A,B,tags,n):
    return {(u,v):set().union(*(compose(A[u,w],B[w,v],n) for w in tags))
            for u in tags for v in tags}


def randomized_test():
    rng=Random(517271)
    checks=0
    for r in range(2,6):
        t=(r-1).bit_length()
        for n in range(1,3):
            for iteration in range(5):
                rels=[]
                for i in range(r):
                    rels.append({(a,b) for a in range(n) for b in range(n)
                                 if rng.randrange(2)})
                tags,adj=encode(n,rels)
                assert {v for v in adj if detect_anchor(v,adj)} == {(a,('root',)) for a in range(n)}
                for i in range(r):
                    for a in range(n):
                        for b in range(n):
                            assert coded_path(a,b,i,t,adj) == ((a,b) in rels[i]), (n,r,i,a,b)
                            checks+=1
                if r%2==0:
                    k=r//2
                    for a in range(n):
                        for b in range(n):
                            def holds(j,c,encoded=False):
                                def edge(i,u,v):
                                    return coded_path(u,v,i,t,adj) if encoded else (u,v) in rels[i]
                                return (edge(2*j,a,c) and edge(2*j,c,b)) or (edge(2*j+1,a,c) and edge(2*j+1,c,b))
                            base=any(all(holds(j,c) for j in range(k)) for c in range(n))
                            code=any(all(holds(j,c,True) for j in range(k)) for c in range(n))
                            assert base == code
                            checks+=1
                # The entire one-relation adjacency is a tag block matrix.
                universe=set(adj)
                universe2={(x,y) for x in universe for y in universe}
                R={(x,y) for x,ys in adj.items() for y in ys}
                I={(x,x) for x in universe}
                expr=[R,I,universe2,set()]
                nblocks=[split_blocks(s,tags,n) for s in expr]
                small_univ={(a,b) for a in range(n) for b in range(n)}
                for iteration2 in range(6):
                    ia=rng.randrange(len(expr)); ib=rng.randrange(len(expr))
                    A=expr[ia];B=expr[ib]
                    BA=nblocks[ia];BB=nblocks[ib]
                    op=rng.choice(['compose','union','intersect','complement','transpose'])
                    if op=='compose':
                        C={(x,z) for x in universe for z in universe if any((x,y) in A and (y,z) in B for y in universe)}
                        BC=block_compose(BA,BB,tags,n)
                    elif op=='union':
                        C=A|B; BC={(u,v):BA[u,v]|BB[u,v] for u in tags for v in tags}
                    elif op=='intersect':
                        C=A&B; BC={(u,v):BA[u,v]&BB[u,v] for u in tags for v in tags}
                    elif op=='complement':
                        C=universe2-A; BC={(u,v):small_univ-BA[u,v] for u in tags for v in tags}
                    else:
                        C={(y,x) for x,y in A}; BC={(u,v):{(b,a) for a,b in BA[v,u]} for u in tags for v in tags}
                    assert BC==split_blocks(C,tags,n),(n,r,op)
                    checks+=1
                    expr.append(C);nblocks.append(BC)
    print('FIXED_SIGNATURE_CODE_AND_BLOCK_SIMULATION_OK',checks)


if __name__=='__main__':
    randomized_test()
