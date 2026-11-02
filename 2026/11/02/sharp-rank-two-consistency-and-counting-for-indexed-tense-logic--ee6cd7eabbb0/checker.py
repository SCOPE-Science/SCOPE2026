#!/usr/bin/env python3
"""Finite tests for two-step types in indexed modal logics with converse."""
import itertools, random

def all_sets(m):
    return [frozenset(a for a in range(m) if b>>a&1) for b in range(1<<m)]

def one_types(m,r):
    S=all_sets(m)
    return [(c,tuple((S[bits[2*i]],S[bits[2*i+1]]) for i in range(r)))
            for c in range(m) for bits in itertools.product(range(len(S)),repeat=2*r)]

def allowed(sig,r):
    c,A,B=sig
    return all(c in t[1][i][1] for i in range(r) for t in A[i]) and all(c in t[1][i][0] for i in range(r) for t in B[i])

def build(m,r,sig):
    c,A,B=sig
    assert allowed(sig,r)
    colours=[c]
    nodesA=[];nodesB=[]
    for i in range(r):
        a=[];b=[]
        for typ in sorted(A[i],key=repr):
            a.append((len(colours),typ));colours.append(typ[0])
        for typ in sorted(B[i],key=repr):
            b.append((len(colours),typ));colours.append(typ[0])
        nodesA.append(a);nodesB.append(b)
    pools={v:len(colours)+v for v in range(m)}
    colours+=list(range(m))
    edges=[set() for i in range(r)]
    for i in range(r):
        for idx,typ in nodesA[i]:edges[i].add((0,idx))
        for idx,typ in nodesB[i]:edges[i].add((idx,0))
        for idx,typ in nodesA[i]+nodesB[i]:
            for j,(S,T) in enumerate(typ[1]):
                for col in S:
                    if not (i==j and idx in [n for n,_ in nodesB[i]] and col==c):
                        edges[j].add((idx,pools[col]))
                for col in T:
                    if not (i==j and idx in [n for n,_ in nodesA[i]] and col==c):
                        edges[j].add((pools[col],idx))
    return colours,edges

def get_profile(colours,edges,w):
    r=len(edges)
    types=[]
    for x in range(len(colours)):
        types.append((colours[x],tuple((frozenset(colours[b] for a,b in E if a==x),
                                          frozenset(colours[a] for a,b in E if b==x)) for E in edges)))
    A=tuple(frozenset(types[v] for a,v in E if a==w) for E in edges)
    B=tuple(frozenset(types[v] for v,b in E if b==w) for E in edges)
    return (colours[w],A,B)

def exhaust_no_atoms():
    seen=set()
    for n in range(1,5):
        local=set()
        for bits in range(1<<(n*n)):
            E={(i,j) for i in range(n) for j in range(n) if bits>>(i*n+j)&1}
            for w in range(n):
                p=get_profile([0]*n,[E],w)
                assert allowed(p,1)
                local.add(p)
        seen|=local
        print('n',n,'cumulative 2-types',len(seen))
    assert len(seen)==16

def synthetic():
    rng=random.Random(10429)
    for m,r,samples in [(1,1,16),(1,2,100),(2,1,150),(2,2,80),(3,1,100)]:
        ts=one_types(m,r)
        assert len(ts)==m*2**(2*r*m)
        for sample in range(samples):
            c=sample%m
            aa=[frozenset(t for t in ts if c in t[1][i][1] and rng.random() < (0.5 if (m,r)==(1,1) else 0.035)) for i in range(r)]
            bb=[frozenset(t for t in ts if c in t[1][i][0] and rng.random() < (0.5 if (m,r)==(1,1) else 0.035)) for i in range(r)]
            sig=(c,tuple(aa),tuple(bb))
            model=build(m,r,sig)
            actual=get_profile(*model,0)
            assert actual==sig,(m,r,sig,actual)
            assert len(model[0])<=1+m+sum(len(t) for t in aa+bb)
        print('synthetic m,r',m,r,'checked',samples,'one-types',len(ts))
    # Enumerate all 16 admissible rank-two types with no atoms and one converse pair.
    ts=one_types(1,1)
    A=[t for t in ts if 0 in t[1][0][1]]
    B=[t for t in ts if 0 in t[1][0][0]]
    assert len(A)==len(B)==2
    for a in range(4):
        for b in range(4):
            sig=(0,(frozenset(A[i] for i in range(2) if a>>i&1),),(frozenset(B[i] for i in range(2) if b>>i&1),))
            assert get_profile(*build(1,1,sig),0)==sig
    print('all 16 no-atom two-step signatures constructed')

if __name__=='__main__':
    synthetic()
    exhaust_no_atoms()
    print('ALL_CHECKS_OK')
