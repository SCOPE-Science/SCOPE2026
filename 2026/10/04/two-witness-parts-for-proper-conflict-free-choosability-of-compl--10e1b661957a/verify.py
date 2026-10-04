#!/usr/bin/env python3
from itertools import combinations, product
from random import Random


def vertices(parts):
    return [(i,j) for i,s in enumerate(parts) for j in range(s)]


def required_size(parts, v, offset):
    n=sum(parts); i,_=v
    return n-parts[i]+offset


def construct(parts, lists, offset):
    """Construct the coloring proved in RESULT.md.

    offset=2 works for every complete multipartite graph with at least two parts.
    offset=1 works when there are at least three parts.
    """
    r=len(parts)
    assert r>=2
    if offset==1:
        assert r>=3
    V=vertices(parts)
    P=[[v for v in V if v[0]==i] for i in range(r)]
    col={}

    # First witness part: force alpha to occur exactly once.
    a=P[0][0]
    alpha=min(lists[a])
    col[a]=alpha
    for v in P[0][1:]:
        avail=sorted(set(lists[v])-{alpha})
        assert avail
        col[v]=avail[0]
    used=set(col[v] for v in P[0])

    # Second witness part: avoid the first part's palette and force beta unique.
    b=P[1][0]
    beta_candidates=sorted(set(lists[b])-used)
    assert beta_candidates
    beta=beta_candidates[0]
    col[b]=beta
    forbidden=used|{beta}
    for v in P[1][1:]:
        avail=sorted(set(lists[v])-forbidden)
        assert avail
        col[v]=avail[0]
    used |= {col[v] for v in P[1]}

    # Later parts only need palette separation from earlier parts.
    for i in range(2,r):
        part_colors=[]
        for v in P[i]:
            avail=sorted(set(lists[v])-used)
            assert avail
            col[v]=avail[0]
            part_colors.append(col[v])
        used |= set(part_colors)
    return col


def check(parts, lists, col):
    V=vertices(parts)
    assert set(col)==set(V)
    for v in V:
        assert col[v] in lists[v]
    for a,b in combinations(V,2):
        if a[0]!=b[0]:
            assert col[a]!=col[b]
    for v in V:
        counts={}
        for u in V:
            if u[0]!=v[0]:
                counts[col[u]]=counts.get(col[u],0)+1
        assert any(mult==1 for mult in counts.values())


def exact_assignments(parts, offset, universe_size):
    V=vertices(parts)
    U=tuple(range(universe_size))
    opts=[]
    for v in V:
        k=required_size(parts,v,offset)
        if k>universe_size:
            return
        opts.append([set(s) for s in combinations(U,k)])
    for choice in product(*opts):
        yield dict(zip(V,choice))


def run_exhaustive(parts, offset, universe_size):
    count=0
    for lists in exact_assignments(parts,offset,universe_size):
        col=construct(parts,lists,offset)
        check(parts,lists,col)
        count+=1
    print(f"exhaustive parts={parts} offset={offset} universe={universe_size} assignments={count}")


def run_random(parts, offset, trials=250):
    rng=Random(20261001+100*offset+sum(parts)*31+len(parts))
    V=vertices(parts)
    maxreq=max(required_size(parts,v,offset) for v in V)
    U=list(range(maxreq+6))
    for _ in range(trials):
        lists={v:set(rng.sample(U,required_size(parts,v,offset))) for v in V}
        col=construct(parts,lists,offset)
        check(parts,lists,col)
    print(f"random parts={parts} offset={offset} trials={trials}")


def main():
    # Exhaustive exact-list tests for the two claims on small multipartite graphs.
    run_exhaustive([2,2],2,5)       # 625 list assignments
    run_exhaustive([3,2],2,5)       # 125 list assignments
    run_exhaustive([1,1,1],1,4)     # 64 list assignments
    run_exhaustive([3,1,1],1,5)     # 1000 list assignments
    run_exhaustive([2,2,1],1,5)     # 625 list assignments

    # Deterministic randomized stress tests for larger profiles.
    for parts in ([6,4],[5,5],[7,2],[4,3,2],[5,1,1,1],[3,3,3],[4,2,2,1]):
        run_random(parts,2)
    for parts in ([4,3,2],[5,1,1,1],[3,3,3],[4,2,2,1],[8,3,1]):
        run_random(parts,1)
    print("ALL CHECKS PASSED")

if __name__=='__main__':
    main()
