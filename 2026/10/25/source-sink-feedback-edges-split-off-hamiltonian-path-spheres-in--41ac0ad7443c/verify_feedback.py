#!/usr/bin/env python3
"""Finite verification for a feedback-edge multipath-complex theorem.
Uses only Python standard library; not a substitute for the all-parameter proof."""
from itertools import permutations
from math import factorial


def top_paths(n, edges):
    """All directed spanning paths, represented by ordered arc tuples."""
    e=set(edges)
    return [tuple(zip(p,p[1:])) for p in permutations(range(n))
            if all((u,v) in e for u,v in zip(p,p[1:]))]


def rank2(cols):
    pivots={}
    for c in cols:
        while c:
            k=c.bit_length()-1
            if k in pivots:c ^= pivots[k]
            else:pivots[k]=c;break
    return len(pivots)


def check(n, edges, full=False):
    s,t=0,n-1
    E=set(edges)
    assert all(v!=s for _,v in E) and all(u!=t for u,_ in E)
    assert (t,s) not in E
    b=(t,s)
    H=top_paths(n,E)
    G=top_paths(n,E|{b})
    assert all(p[0][0]==s and p[-1][1]==t for p in H)
    assert all(len(p)==n-1 for p in G)
    assert all((b in p) or (p in H) for p in G)
    assert len(set(G))==len(G)
    rows={}
    cols=[]
    for p in G:
        bits=0
        ps=frozenset(p)
        for a in p:
            f=ps-{a}
            if f not in rows:rows[f]=len(rows)
            bits ^= 1<<rows[f]
        cols.append(bits)
    nullity=len(G)-rank2(cols)
    assert nullity==len(H), (n,len(E),len(H),len(G),nullity)
    if full:
        all_E=sorted(E|{b}); pos={e:i for i,e in enumerate(all_E)}
        top_face_sets={frozenset(q) for q in G}
        for p in H:
            cycle=frozenset(p+(b,))
            assert len(cycle)==n
            F=sorted(cycle,key=pos.__getitem__)
            chains={}
            for i,a in enumerate(F):
                face=tuple(x for x in F if x!=a)
                assert frozenset(face) in top_face_sets, (n,E,face)
                chains[frozenset(face)]=(-1)**i
            boundary={}
            for face,coef in chains.items():
                f=sorted(face,key=pos.__getitem__)
                for j,a in enumerate(f):
                    key=frozenset(face-{a})
                    boundary[key]=boundary.get(key,0)+coef*(-1)**j
            assert all(v==0 for v in boundary.values())
            assert chains[frozenset(p)] in (-1,1)
            assert all((q==p) == (frozenset(q) in chains) for q in H)
    return len(H),len(G),len(rows)


def source_sink_allowed(n):
    return [(u,v) for u in range(n) for v in range(n)
            if u!=v and v!=0 and u!=n-1]


def exhaustive(n):
    allowed=source_sink_allowed(n)
    outcomes={}
    for mask in range(1<<len(allowed)):
        E=[e for i,e in enumerate(allowed) if mask>>i&1]
        h,g,f=check(n,E)
        outcomes[h]=outcomes.get(h,0)+1
    print('EXHAUSTIVE',n,'graphs',1<<len(allowed),'Hamiltonian-count histogram',sorted(outcomes.items()),flush=True)


def transitive(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def two_way_middle(n):
    return ([(0,i) for i in range(1,n-1)]
            +[(i,n-1) for i in range(1,n-1)]
            +[(i,j) for i in range(1,n-1) for j in range(1,n-1) if i!=j])

if __name__=='__main__':
    for n in (3,4,5):exhaustive(n)
    for n in range(3,9):
        h,g,f=check(n,transitive(n),full=True)
        assert h==1
        print('REV_TRANSITIVE',n,'Hamiltonian',h,'top simplices',g,'codim-one faces',f,flush=True)
    for n in range(4,8):
        h,g,f=check(n,two_way_middle(n),full=True)
        assert h==factorial(n-2)
        print('BIDIRECTED_INTERIOR',n,'Hamiltonian',h,'top simplices',g,'codim-one faces',f,flush=True)
    print('FEEDBACK_MULTIPATH_TOP_HOMOLOGY_CHECKS_OK')
