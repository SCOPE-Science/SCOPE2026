#!/usr/bin/env python3
"""Exact finite checks for generalized-theta graphical zonotope fixed points.
All arithmetic is integer, and orientations are exhaustively enumerated.
No external packages are required.
"""
from itertools import product
from math import prod
from collections import Counter

def graph(lengths):
    assert len(lengths)>=3 and min(lengths)>=2
    edges=[]; paths=[]; vertex_count=2
    for length in lengths:
        nodes=[0]+list(range(vertex_count,vertex_count+length-1))+[1]
        vertex_count += length-1
        paths.append(tuple(range(len(edges),len(edges)+length)))
        edges.extend(zip(nodes[:-1],nodes[1:]))
    assert len(set(map(frozenset,edges)))==len(edges)
    return vertex_count,edges,paths

def acyclic(n,arcs):
    indeg=[0]*n;out=[[] for _ in range(n)]
    for u,v in arcs:out[u].append(v);indeg[v]+=1
    stack=[i for i,x in enumerate(indeg) if x==0];seen=0
    while stack:
        u=stack.pop();seen+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:stack.append(v)
    return seen==n

def is_transitive(edge_i,arcs,n):
    source,target=arcs[edge_i]
    out=[[] for _ in range(n)]
    for j,(u,v) in enumerate(arcs):
        if j!=edge_i:out[u].append(v)
    todo=[source];seen={source}
    while todo:
        u=todo.pop()
        for v in out[u]:
            if v==target:return True
            if v not in seen:seen.add(v);todo.append(v)
    return False

def predicted_smooth(bits,paths):
    for sign in (0,1):
        for j,indices in enumerate(paths):
            if all(bits[i]==sign for i in indices):
                if all(sum(bits[i]==sign for i in other)==1
                       for k,other in enumerate(paths) if k!=j):
                    return True
    return False

def check(lengths):
    n,edges,paths=graph(lengths)
    total=smooth=0
    distribution=Counter()
    for bits in product((0,1),repeat=len(edges)):
        arcs=[(v,u) if bit else (u,v) for (u,v),bit in zip(edges,bits)]
        if not acyclic(n,arcs):continue
        total+=1
        redundant=sum(is_transitive(i,arcs,n) for i in range(len(edges)))
        distribution[redundant]+=1
        actual=redundant==len(edges)-n+1
        predict=predicted_smooth(bits,paths)
        assert actual==predict,(lengths,bits,redundant)
        smooth+=actual
    exp_total=2*prod(2**length-1 for length in lengths)-prod(2**length-2 for length in lengths)
    exp_smooth=2*sum(prod(lengths[i] for i in range(len(lengths)) if i!=j) for j in range(len(lengths)))
    assert (total,smooth)==(exp_total,exp_smooth), (lengths,total,smooth,exp_total,exp_smooth)
    def mul(a,b):
        result=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):result[i+j]+=x*y
        return result
    base=[1];withfull=[1]
    for length in lengths:
        base=mul(base,[2**length-2-length,length])
        withfull=mul(withfull,[2**length-1-length,length])
    coeff=[2*(withfull[i]-base[i]) for i in range(len(base))]
    coeff[0]+=prod(2**length-2 for length in lengths)
    assert [distribution[i] for i in range(len(lengths))]==coeff[:len(lengths)]
    assert coeff[-1]==0
    assert sum(coeff)==exp_total
    print(f"lengths={lengths} redundant-edge distribution={tuple(distribution[i] for i in range(len(lengths)))}; acyclic={total} smooth={smooth}: OK")

if __name__=='__main__':
    for lengths in ((2,2,2),(2,2,3),(2,3,3),(2,3,4),(3,3,3),
                    (2,2,2,2),(2,2,2,3),(2,2,3,3),(2,2,2,2,2)):
        check(lengths)
    print('VERIFY_OK')
