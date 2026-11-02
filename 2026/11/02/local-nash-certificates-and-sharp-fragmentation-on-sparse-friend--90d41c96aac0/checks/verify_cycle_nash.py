#!/usr/bin/env python3
"""Separate exact-integer comparison of Nash deviations with the local certificate.

This is finite corroboration, not an infinite proof.
"""
from collections import Counter
from itertools import product


def partitions(n):
    if not n:
        yield ()
    else:
        for p in partitions(n - 1):
            for k in range(len(p)):
                q = list(p)
                q[k] = p[k] + (n - 1,)
                yield tuple(q)
            yield p + ((n - 1,),)


def graph_paths_cycles(spec):
    # spec: ('P',l) or ('C',l) for vertex-disjoint components.
    edges=set()
    offset=0
    for kind,length in spec:
        assert (kind == 'P' and length >= 2) or (kind == 'C' and length >= 3)
        for i in range(length - 1):
            edges.add((offset+i,offset+i+1))
        if kind == 'C':
            edges.add((offset,offset+length-1))
        offset += length
    return offset,edges


def labels(p,n):
    groups=[set(g) for g in p]
    lab=[None]*n
    for j,g in enumerate(groups):
        for v in g:lab[v]=j
    return groups,lab


def brute(p,n,edges):
    groups,lab=labels(p,n)
    neighbors=[set() for _ in range(n)]
    for a,b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    for v in range(n):
        own=lab[v]
        same=sum(lab[w]==own for w in neighbors[v])
        for j,g in enumerate(groups):
            if j==own:continue
            new=sum(lab[w]==j for w in neighbors[v])
            if new*len(groups[own])>same*(len(g)+1):return False
    return True


def certificate(p,n,edges):
    groups,lab=labels(p,n)
    neighbors=[set() for _ in range(n)]
    for a,b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    if any(not any(lab[w]==lab[v] for w in neighbors[v]) for v in range(n)):
        return False
    return all(lab[a]==lab[b] or abs(len(groups[lab[a]])-len(groups[lab[b]]))<=1 for a,b in edges)


def components(g,n,edges):
    s=set(g)
    todo=set(s)
    count=0
    while todo:
        count+=1
        seen={todo.pop()}
        stack=list(seen)
        while stack:
            v=stack.pop()
            for a,b in edges:
                if a==v and b in todo:
                    todo.remove(b);stack.append(b)
                if b==v and a in todo:
                    todo.remove(a);stack.append(a)
    return count


def verify(spec,cycle=False):
    n,edges=graph_paths_cycles(spec)
    c=Counter()
    for p in partitions(n):
        a=brute(p,n,edges)
        b=certificate(p,n,edges)
        assert a==b,(spec,p,a,b)
        c['tested']+=1
        if a:
            c['stable']+=1
            if cycle:
                comp=max(components(g,n,edges) for g in p)
                c['max_comp']=max(c['max_comp'],comp)
                if comp>1:c['disconnected']+=1
    if cycle:
        assert c['max_comp']==max(1,n//4),(n,c)
        assert (c['disconnected']>0)==(n>=8),(n,c)
    return c

if __name__ == '__main__':
    total=0
    for n in range(3,11):
        c=verify([('C',n)],cycle=True)
        print(f"C{n}: {c['tested']} partitions, {c['stable']} stable, {c['disconnected']} with disconnected coalition, max {c['max_comp']} components")
        total+=c['tested']
    for n in range(2,10):
        c=verify([('P',n)])
        total+=c['tested']
    disjoint_specs=[ [('P',2),('P',2)], [('P',2),('P',3)], [('P',2),('P',4)], [('P',2),('P',2),('P',2)], [('P',3),('P',3)], [('C',3),('P',2)], [('C',3),('C',3)], [('C',4),('P',2)], [('C',4),('P',3)], [('C',5),('P',2)], [('C',3),('P',2),('P',2)] ]
    for spec in disjoint_specs:
        c=verify(spec)
        total+=c['tested']
    print(f'PASS: {total} unrestricted partitions on paths, cycles and disjoint degree-two graphs; no singleton or adjacency omissions')
