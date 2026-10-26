#!/usr/bin/env python3
"""Finite prime-field checks for complete multipartite graphical Lie brackets.
Run with Python 3; no third-party packages are used.
"""
from itertools import product
from collections import Counter
from math import comb


def predicted(q, parts):
    N=sum(parts)
    E=sum(a*b for i,a in enumerate(parts) for b in parts[i+1:])
    c=q**E
    lines=(q**N-1)//(q-1)
    part_lines=sum((q**a-1)//(q-1) for a in parts)
    mixed=lines-part_lines
    assert mixed>0
    comp=sorted([q**a-1 for a in parts]+[q-1]*mixed)
    return N,E,c,comp


def inspect(q, parts):
    N,E,c,expect=predicted(q,parts)
    labels=sum(([i]*a for i,a in enumerate(parts)),[])
    edges=[(i,j) for i in range(N) for j in range(i+1,N) if labels[i]!=labels[j]]
    assert len(edges)==E
    V=list(product(range(q),repeat=N))
    V=[v for v in V if any(v)]
    def bracket_zero(u,v):
        return all((u[i]*v[j]-u[j]*v[i])%q==0 for i,j in edges)
    # Only the original bilinear brackets determine adjacency.
    remaining=set(V); actual=[]
    while remaining:
        x=next(iter(remaining))
        seen={x}; frontier=[x]
        while frontier:
            u=frontier.pop()
            more={v for v in remaining-seen if bracket_zero(u,v)}
            seen.update(more); frontier.extend(more)
        remaining.difference_update(seen)
        actual.append(len(seen))
    assert sorted(actual)==expect,(q,parts,sorted(actual),expect)
    # Independently recover the graph's field and its defining part multiset.
    all_count=q**(N+E)
    min_comp=min(actual)*c
    qr=1+min_comp//c
    assert qr==q and (min_comp%c)==0
    recovered_N=0
    val=all_count//c
    while val>1:
        assert val%qr==0
        val//=qr
        recovered_N+=1
    big=[]
    for size,mult in Counter(actual).items():
        if size>qr-1:
            a=1
            while qr**a-1<size:a+=1
            assert qr**a-1==size
            big += [a]*mult
    recovered=sorted(big+[1]*(recovered_N-sum(big)))
    assert recovered==sorted(parts),(q,parts,recovered)
    # Rank/dimension formula via actual bracket kernel count.
    for v in V:
        active={labels[i] for i,x in enumerate(v) if x!=0}
        codim = N-parts[next(iter(active))] if len(active)==1 else N-1
        count=sum(bracket_zero(v,w) for w in product(range(q),repeat=N))
        assert count == q**(N-codim),(q,parts,v,count,codim)
    return len(V),len(actual),E


def main():
    cases=[(3,(1,1)),(3,(2,1)),(3,(1,1,1)),(3,(2,2)),
           (3,(2,1,1)),(5,(1,1)),(5,(2,1)),(5,(1,1,1)),
           (7,(1,1)),(2,(2,1)),(2,(1,1,1)),(2,(2,2))]
    for q,parts in cases:
        count,k,E=inspect(q,parts)
        print('PASS',q,parts,'quotient',count+1,'central dimension',E,'commuting components',k)
    print('VERIFY_OK',len(cases),'independent bracket cases')

if __name__=='__main__':main()
