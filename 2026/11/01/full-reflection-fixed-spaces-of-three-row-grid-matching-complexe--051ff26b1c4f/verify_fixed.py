#!/usr/bin/env python3
"""Reconstruct simultaneous grid-reflection fixed complexes from edge orbits.

Uses only Python's standard library.  No externally supplied face lists.
"""
from itertools import combinations


def edges(n):
    V = [(r,c) for r in range(3) for c in range(n)]
    return {tuple(sorted((a,b))) for a,b in combinations(V,2)
            if abs(a[0]-b[0])+abs(a[1]-b[1]) == 1}


def action(e, n, which):
    if which == 'R':
        return tuple(sorted(((2-r,c) for r,c in e)))
    return tuple(sorted(((r,n-1-c) for r,c in e)))


def is_matching(edge_list):
    endpoints = [x for e in edge_list for x in e]
    return len(endpoints)==len(set(endpoints))


def fixed_orbits(n):
    es=edges(n)
    unused=set(es)
    admissible=[]
    rejected=0
    while unused:
        start=next(iter(unused))
        orb={start}
        queue=[start]
        while queue:
            e=queue.pop()
            for g in ('R','C'):
                t=action(e,n,g)
                assert t in es
                if t not in orb:
                    orb.add(t)
                    queue.append(t)
        unused-=orb
        if is_matching(orb):
            admissible.append(frozenset(orb))
        else:
            rejected+=1
    return admissible,rejected


def key(orb):
    assert all(a[0]==b[0] for a,b in orb), 'nonhorizontal admissible orbit'
    rs={a[0] for a,b in orb}
    assert rs in ({0,2},{1})
    return (0 if rs=={0,2} else 1,
            min(min(a[1],b[1]) for a,b in orb))


def orbit_conflict_graph(n):
    obs,rej=fixed_orbits(n)
    ids={key(o):o for o in obs}
    q=n//2 if n%2==0 else (n-3)//2
    assert set(ids)=={(r,j) for r in (0,1) for j in range(q)}, (n,sorted(ids))
    # Check every orbit pair, including edges with the same orientation / middle row.
    for a,b in combinations(ids,2):
        clash=not is_matching(ids[a]|ids[b])
        expected=(a[0]==b[0] and abs(a[1]-b[1])==1)
        assert clash==expected,(n,a,b,clash,expected)
    return ids,rej,q


def faces(n):
    ids,rej,q=orbit_conflict_graph(n)
    vs=list(sorted(ids))
    result=[]
    for mask in range(1<<len(vs)):
        sel=[vs[i] for i in range(len(vs)) if mask>>i&1]
        is_face=all(is_matching(ids[a]|ids[b]) for a,b in combinations(sel,2))
        standard=all(not (a[0]==b[0] and abs(a[1]-b[1])==1)
                     for a,b in combinations(sel,2))
        assert is_face==standard,(n,mask)
        if is_face:result.append(mask)
    return vs,result,q


def rank_f2(columns):
    pivots={}
    for col in columns:
        while col:
            k=col.bit_length()-1
            if k not in pivots:
                pivots[k]=col
                break
            col^=pivots[k]
    return len(pivots)


def reduced_betti(faces_by_size):
    max_k=max(faces_by_size)
    ranks={1:1 if faces_by_size.get(1) else 0}
    for k in range(2,max_k+2):
        current=faces_by_size.get(k,[])
        lower={f:i for i,f in enumerate(faces_by_size.get(k-1,[]))}
        cols=[]
        for f in current:
            boundary=0
            bit=f
            while bit:
                lowest=bit&(-bit)
                boundary ^= (1<<lower[f^lowest])
                bit-=lowest
            cols.append(boundary)
        ranks[k]=rank_f2(cols)
    return {k-1:len(fs)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,fs in faces_by_size.items() if k>=1
            and len(fs)-ranks.get(k,0)-ranks.get(k+1,0)>0}


def expected_betti(q):
    if q==0 or q%3==1:return {}
    if q%3==0: return {2*(q//3)-1:1}
    return {(2*q-1)//3:1}


def main():
    tested_orbits=0
    tested_subsets=0
    for n in range(2,91):
        ids,rej,q=orbit_conflict_graph(n)
        tested_orbits+=len(ids)+rej
        if n<=13:
            vs,valid,qq=faces(n)
            tested_subsets+=(1<<len(vs))
            if n<=12:
                by_size={}
                for mask in valid:
                    by_size.setdefault(mask.bit_count(),[]).append(mask)
                # The empty fixed space is encoded by just the empty simplex.
                observed=reduced_betti(by_size)
                want=expected_betti(q)
                assert observed==want,(n,q,observed,want)
                print(f'n={n:2d} q={q:2d} admissible_orbits={len(ids):2d} faces={len(valid):4d} reduced_Betti={observed}')
    print('VERIFY_OK: widths 2..90; orbit classes',tested_orbits,
          '; checked candidate faces',tested_subsets,'; homology widths 2..12')

if __name__=='__main__':main()
