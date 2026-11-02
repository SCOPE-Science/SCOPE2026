#!/usr/bin/env python3
"""Reproduce binary cut-rank and matching-fault laws for finite projective-plane incidence graph states."""
from itertools import combinations
from collections import Counter
from random import Random
import json

MOD = {1:0b11, 2:0b111, 3:0b1011, 4:0b10011}

def prod(a,b,degree):
    modulus=MOD[degree]
    result=0
    for _ in range(degree):
        if b & 1: result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree): a ^= modulus
    return result

def divide(a,b,degree):
    q=1 << degree
    return prod(a, next(z for z in range(1,q) if prod(z,b,degree)==1),degree)

def representatives(degree):
    q=1 << degree
    out=[]
    for x in range(q):
        for y in range(q):
            for z in range(q):
                v=(x,y,z)
                if not any(v): continue
                pivot=next(a for a in v if a)
                u=tuple(divide(a,pivot,degree) for a in v)
                if u not in out:out.append(u)
    return sorted(out)

def plane(degree):
    vectors=representatives(degree)
    q=1 << degree
    def dot(x,y):
        v=0
        for a,b in zip(x,y):v ^= prod(a,b,degree)
        return v
    matrix=[sum(1<<j for j,lin in enumerate(vectors) if dot(pt,lin)==0)
            for pt in vectors]
    return vectors,matrix

def rank(rows):
    basis={}
    for z in rows:
        while z:
            top=z.bit_length()-1
            if top not in basis:
                basis[top]=z
                break
            z ^= basis[top]
    return len(basis)

def graph_rank(rows,matching):
    work=list(rows)
    for i,j in matching:work[i]^=1<<j
    return rank(work)

def prediction(rows,matching,baseline,q):
    k=len(matching)
    if k<=q: return baseline+k
    assert k==q+1
    pmask=sum(1<<i for i,_ in matching)
    lmask=sum(1<<j for _,j in matching)
    points_collinear=any((pmask & ~sum(1<<i for i,row in enumerate(rows) if row>>j&1)) == 0
                          for j in range(len(rows)))
    lines_concurrent=any((lmask & ~row)==0 for row in rows)
    return baseline+k-int(points_collinear or lines_concurrent)

def enumerate_small(rows):
    n=len(rows)
    edges=[(i,j) for i,row in enumerate(rows) for j in range(n) if (row>>j)&1]
    count=Counter()
    for k in range(0,4):
        for selected in combinations(edges,k):
            if len({i for i,_ in selected})<k or len({j for _,j in selected})<k:continue
            observed=graph_rank(rows,selected)
            expected=prediction(rows,selected,rank(rows),2)
            assert observed==expected,(selected,observed,expected)
            count[str(k)]+=1
    return dict(count)

def random_matching(rows,k,rng):
    edges=[(i,j) for i,row in enumerate(rows) for j in range(len(rows)) if row>>j&1]
    rng.shuffle(edges)
    used_p=set();used_l=set();out=[]
    for i,j in edges:
        if i in used_p or j in used_l:continue
        used_p.add(i);used_l.add(j);out.append((i,j))
        if len(out)==k:return out
    return None

def critical_examples(rows,q):
    n=len(rows)
    line=0
    chosen_points=[i for i in range(n) if rows[i]>>line&1]
    outside=[i for i in range(n) if i not in chosen_points]
    assert len(chosen_points)==q+1 and len(outside)>1
    # First type: collinear point support and concurrent line support.
    z=outside[0]
    matching=[]
    for p in chosen_points:
        candidates=[j for j in range(n) if rows[p]>>j&1 and rows[z]>>j&1]
        assert len(candidates)==1
        matching.append((p,candidates[0]))
    assert len({j for _,j in matching})==q+1
    yield 'critical_dependent',matching
    # Second type: noncollinear support on both sides.
    z=outside[0];pstar=outside[1]
    matching=[]
    for p in chosen_points[:-1]:
        j=next(j for j in range(n) if rows[p]>>j&1 and rows[z]>>j&1)
        matching.append((p,j))
    extra=next(j for j in range(n) if rows[pstar]>>j&1 and not (rows[z]>>j&1))
    matching.append((pstar,extra))
    assert len({j for _,j in matching})==q+1
    yield 'critical_independent',matching

def main():
    rng=Random(20261101)
    summaries=[]
    for degree,attempts in [(1,0),(2,2000),(3,350),(4,45)]:
        q=1<<degree
        vectors,rows=plane(degree)
        n=q*q+q+1
        assert len(vectors)==n
        baseline=rank(rows)
        assert baseline==3**degree+1,(q,baseline)
        assert all(row.bit_count()==q+1 for row in rows)
        assert all((rows[i]&rows[j]).bit_count()==1 for i in range(n) for j in range(i))
        categories=Counter()
        for typ,matching in critical_examples(rows,q):
            observed=graph_rank(rows,matching)
            expected=prediction(rows,matching,baseline,q)
            assert observed==expected,(degree,typ,observed,expected)
            categories[typ+'_gain_'+str(observed-baseline)]+=1
        if q==2:
            categories.update({f'fano_exhaustive_{k}':v for k,v in enumerate_small(rows).items()})
        for trial in range(attempts):
            k=1+trial%(q+1)
            edges=random_matching(rows,k,rng)
            if edges is None:continue
            exp=prediction(rows,edges,baseline,q)
            obs=graph_rank(rows,edges)
            assert obs==exp,(degree,edges,obs,exp)
            categories[f'matching_{k}_gain_{obs-baseline}']+=1
        summaries.append({'q':q,'vertices_per_side':n,'binary_rank':baseline,'tests':dict(categories)})
    print(json.dumps({'status':'PASS','results':summaries},sort_keys=True))
if __name__=='__main__':main()
