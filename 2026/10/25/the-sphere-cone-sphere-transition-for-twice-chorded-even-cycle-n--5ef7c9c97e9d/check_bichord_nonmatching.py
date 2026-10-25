"""Independent finite checks for nonmatching complexes of two-chorded even cycles.

Run: python3 check_bichord_nonmatching.py
Only Python standard library is required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def graph_edges(t, stage):
    n = 2*t
    edges = [tuple(sorted((i, (i+1)%n))) for i in range(n)]
    if stage >= 1:
        edges.append((0,2))
    if stage >= 2:
        edges.append((1,3))
    assert len(set(edges)) == len(edges)
    return edges


def perfect_matchings(edges, t):
    out=[]
    for ids in combinations(range(len(edges)), t):
        endpoints=[]
        for j in ids:
            endpoints.extend(edges[j])
        if len(set(endpoints)) == 2*t:
            out.append(sum(1<<j for j in ids))
    return out


def faces_by_dimension(edge_count, forbidden):
    faces={}
    for mask in range(1<<edge_count):
        if all((mask & f)!=f for f in forbidden):
            d=mask.bit_count()-1
            faces.setdefault(d,[]).append(mask)
    return faces


def rank_mod_two_columns(columns):
    pivots={}
    for x in columns:
        v=x
        while v:
            p=v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p]=v
                break
    return len(pivots)


def reduced_betti(faces):
    dims=sorted(faces)
    ranks={-1:0}
    for d in dims:
        if d<0:
            continue
        lower={mask:i for i,mask in enumerate(faces[d-1])}
        columns=[]
        for simplex in faces[d]:
            boundary=0
            bits=simplex
            while bits:
                low=bits & -bits
                bits ^= low
                boundary ^= 1<<lower[simplex ^ low]
            columns.append(boundary)
        ranks[d]=rank_mod_two_columns(columns)
    return {d:len(faces[d])-ranks[d]-ranks.get(d+1,0)
            for d in dims if d>=0 and len(faces[d])-ranks[d]-ranks.get(d+1,0)}


def run():
    total=0
    for t in range(2,8):
        A=sum(1<<i for i in range(0,2*t,2))
        B=sum(1<<i for i in range(1,2*t,2))
        C=sum(1<<i for i in range(4,2*t,2)) | (1<<(2*t)) | (1<<(2*t+1))
        for stage in (0,1,2):
            edges=graph_edges(t,stage)
            actual=perfect_matchings(edges,t)
            expected=[A,B]+([C] if stage==2 else [])
            assert sorted(actual)==sorted(expected), (t,stage,actual,expected)
            faces=faces_by_dimension(len(edges),actual)
            count=sum(len(v) for v in faces.values())
            chi_tilde=sum((-1)**d * len(row) for d,row in faces.items())
            want_chi=(-1)**(2*t-3) if stage==0 else (0 if stage==1 else (-1)**(2*t-2))
            assert chi_tilde == want_chi,(t,stage,chi_tilde,want_chi)
            if stage==1:
                assert all((s | 1<<(2*t)) in set(faces[s.bit_count()])
                           for d,row in faces.items() for s in row if d>=0 and not(s & 1<<(2*t)))
            betti = reduced_betti(faces) if t<=5 else None
            if betti is not None:
                want_betti=({2*t-3:1} if stage==0 else ({} if stage==1 else {2*t-2:1}))
                assert betti==want_betti,(t,stage,betti,want_betti)
            total+=count-1
            print(f't={t} stage={stage} edges={len(edges)} perfect_matchings={len(actual)} faces_nonempty={count-1} reduced_euler={chi_tilde} mod2_betti={betti if betti is not None else "not_computed"}')
    print(f'REPLAY_OK total_nonempty_faces={total}; cases=18; full_mod2_homology_cases=12')


if __name__=='__main__':
    run()
