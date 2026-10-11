#!/usr/bin/env python3
"""Independent finite checks of intrinsic graph Cech nerves on complete multipartite graphs.
No external packages. This checks examples, not the unbounded-family proof.
"""
from itertools import combinations
from math import prod

CASES = [(2,2),(3,2),(3,3),(2,2,2),(3,2,2),(3,3,2),(2,2,2,2),(3,2,2,2)]

def rank_binary(columns):
    pivots = {}
    for x in columns:
        while x:
            p = x.bit_length()-1
            if p not in pivots:
                pivots[p] = x
                break
            x ^= pivots[p]
    return len(pivots)

def build(parts, r):
    sizes = list(parts)
    colors = sum(([i]*s for i,s in enumerate(sizes)), [])
    n = len(colors)
    near = []
    for i in range(n):
        near.append({j for j in range(n) if i != j and colors[i] != colors[j]})
    if r == 0:
        generators = [frozenset((i,)) for i in range(n)]
    elif r == 1:
        generators = [frozenset((i,j)) for i in range(n) for j in near[i] if i<j]
    elif r == 2:
        generators = [frozenset(near[i]|{i}) for i in range(n)]
    elif r == 3:
        generators = [frozenset(near[i]|near[j]|{i,j}) for i in range(n) for j in near[i] if i<j]
    else:
        raise ValueError(r)
    faces = set()
    for f in generators:
        t = tuple(sorted(f))
        for k in range(1,len(t)+1):
            faces.update(combinations(t,k))
    return colors,faces

def reduced_betti(faces):
    bydim = {}
    for f in faces:
        bydim.setdefault(len(f)-1,[]).append(f)
    for v in bydim.values(): v.sort()
    maxdim = max(bydim)
    ranks = {0: 1} # augmented boundary C_0 -> C_-1, for connected or disconnected
    for d in range(1,maxdim+1):
        rows = {f:i for i,f in enumerate(bydim[d-1])}
        cols = []
        for f in bydim[d]:
            bit = 0
            for j in range(len(f)):
                bit ^= (1 << rows[f[:j]+f[j+1:]])
            cols.append(bit)
        ranks[d] = rank_binary(cols)
    ranks[maxdim+1]=0
    return {d:len(bydim[d])-ranks[d]-ranks[d+1] for d in range(maxdim+1) if len(bydim[d])-ranks[d]-ranks[d+1]}

def main():
    for parts in CASES:
        n=sum(parts);k=len(parts)
        expected_e=sum(a*b for a,b in combinations(parts,2))
        outcomes={}
        for r in range(4):
            colors,faces=build(parts,r)
            observed = reduced_betti(faces)
            expected={0:n-1} if r==0 else ({1: expected_e-n+1} if r==1 else ({2*k-2:prod(a-1 for a in parts)} if r==2 else {}))
            assert observed==expected,(parts,r,observed,expected)
            if r==2:
                for s in faces:
                    good=any(sum(colors[v]==i for v in s)<=1 for i in range(k))
                    assert good, (parts,r,s)
                # Exhaustively compare to the independently stated min-part-occupancy condition.
                for mask in range(1,1<<n):
                    s=tuple(i for i in range(n) if mask>>i & 1)
                    good=any(sum(colors[v]==i for v in s)<=1 for i in range(k))
                    assert (s in faces)==good,(parts,s)
            outcomes[r]=(len(faces),observed)
        print(parts,outcomes)
    print('VERIFY_OK')

if __name__=='__main__': main()
