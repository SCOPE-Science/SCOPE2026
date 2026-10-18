#!/usr/bin/env python3
"""Independent small-order tests for three cycle-convex independence notions.
Uses a graph-theoretic closure algorithm and direct partition tests, not theorem formulas
for computing admissibility. Standard library only.
"""
from itertools import combinations
from math import comb


def graph(parts):
    classes = tuple(p for p, size in enumerate(parts) for _ in range(size))
    n = len(classes)
    adj = [sum((1 << j) for j in range(n) if classes[j] != classes[i])
           for i in range(n)]
    return n, adj


def cc_hull(mask, n, adj):
    full = (1 << n) - 1
    old = -1
    while old != mask:
        old = mask
        # Component decomposition in the *currently induced* graph on mask.
        remaining = mask
        components = []
        while remaining:
            seed = remaining & -remaining
            component = seed
            frontier = seed
            while frontier:
                first = frontier & -frontier
                frontier ^= first
                v = first.bit_length() - 1
                new = (adj[v] & mask) & ~component
                component |= new
                frontier |= new
            components.append(component)
            remaining &= ~component
        for w in range(n):
            bit = 1 << w
            if mask & bit:
                continue
            if any((adj[w] & component).bit_count() >= 2
                   for component in components):
                mask |= bit
    return mask


def independent_flags(mask, n, adj, hulls):
    if not mask:
        return True, True, True
    verts = [i for i in range(n) if mask >> i & 1]
    C = all(not (hulls[mask ^ (1 << v)] & (1 << v)) for v in verts)
    intersection = (1 << n) - 1
    for v in verts:
        intersection &= hulls[mask ^ (1 << v)]
    H = intersection == 0
    R = True
    first = mask & -mask
    sub = (mask - 1) & mask
    while sub:
        if (sub & first) and (hulls[sub] & hulls[mask ^ sub]):
            R = False
            break
        sub = (sub - 1) & mask
    return C,H,R


def predicts(mask, classes, parts):
    n = len(classes)
    active = {classes[i] for i in range(n) if mask >> i & 1}
    size = mask.bit_count()
    r = len(parts)
    if r == 2 and min(parts) == 1:
        return True
    if len(active) <= 1:
        return True
    if r == 2:
        return size <= 3
    return size == 2


def predicted_counts(parts):
    n=sum(parts);r=len(parts)
    if r == 2 and min(parts)==1:
        return tuple(comb(n,j) for j in range(n+1))
    res=[0]*(n+1)
    for j in range(n+1):
        res[j]=sum(comb(a,j) for a in parts if j <= a)
    res[0]=1
    if r == 2:
        a,b=parts
        res[2] += a*b
        res[3] += a*comb(b,2)+b*comb(a,2)
    else:
        res[2] += sum(a*b for a,b in combinations(parts,2))
    return tuple(res)


def gf2_rank(columns):
    pivots={}
    for v in columns:
        while v:
            pivot=v.bit_length()-1
            if pivot in pivots:
                v ^= pivots[pivot]
            else:
                pivots[pivot]=v
                break
    return len(pivots)


def betti(faces,n):
    degree_faces=[]
    for j in range(n):
        degree_faces.append([mask for mask in faces if mask.bit_count()==j+1])
    ranks=[0]
    for k in range(1,n):
        target={f:i for i,f in enumerate(degree_faces[k-1])}
        cols=[]
        for f in degree_faces[k]:
            boundary=0
            for v in range(n):
                if f>>v&1:
                    boundary ^= 1 << target[f ^ (1<<v)]
            cols.append(boundary)
        ranks.append(gf2_rank(cols))
    ranks.append(0)
    result=[len(degree_faces[k])-ranks[k]-ranks[k+1]
                 for k in range(n)]
    result[0] -= 1  # reduced homology of a nonempty connected complex
    return tuple(result)


def test(parts, homology=True):
    n, adj=graph(parts)
    classes=tuple(p for p,a in enumerate(parts) for _ in range(a))
    hulls=[cc_hull(m,n,adj) for m in range(1<<n)]
    faces=[]
    for m in range(1<<n):
        got=independent_flags(m,n,adj,hulls)
        want=predicts(m,classes,parts)
        assert got==(want,want,want), (parts,m,got,want)
        if want:faces.append(m)
    observed=tuple(sum(m.bit_count()==j for m in faces)
                   for j in range(n+1))
    assert observed==predicted_counts(parts),(parts,observed)
    if homology:
        ranks=betti(faces,n)
        if len(parts)==2 and min(parts)==1:
            target={}
        elif len(parts)==2:
            a,b=parts
            target={2:1+a*b*(n-4)//2}
        else:
            target={1:sum(a*b for a,b in combinations(parts,2))-len(parts)+1}
        expected=tuple(target.get(j,0) for j in range(n))
        assert ranks==expected,(parts,ranks,expected)
    return len(faces)


def compositions(n,r):
    if r == 1:
        yield (n,)
    else:
        for a in range(1,n-r+2):
            for sub in compositions(n-a,r-1):
                yield (a,)+sub

if __name__=='__main__':
    tests=0;states=0
    for n in range(2,9):
        for r in range(2,n+1):
            for p in compositions(n,r):
                if tuple(sorted(p))!=p: continue
                states+=test(p)
                tests+=1
    print('PASS',tests,'multipartite instances on 2..8 vertices;',states,
          'independent subsets; all three predicates and mod-2 homology verified')
