#!/usr/bin/env python3
"""Finite graph checks for Moore-graph four-variable back-and-forth theorem.
Python standard library only; the computations are finite checks, not the infinite proof.
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter


def petersen():
    vs = list(combinations(range(5), 2))
    n = len(vs)
    return [{j for j in range(n) if i != j and not (set(vs[i]) & set(vs[j]))} for i in range(n)]


def hoffman_singleton():
    adj = [set() for _ in range(50)]
    def edge(u, v):
        if u != v:
            adj[u].add(v); adj[v].add(u)
    for h in range(5):
        for j in range(5):
            edge(5*h+j, 5*h+(j+1)%5)
    for i in range(5):
        for k in range(5):
            edge(25+5*i+k, 25+5*i+(k+2)%5)
    for h in range(5):
        for j in range(5):
            for i in range(5):
                edge(5*h+j,25+5*i+(h*i+j)%5)
    return adj


def triple_type(adj, xyz):
    x,y,z=xyz
    e = (int(y in adj[x]),int(z in adj[x]),int(z in adj[y]))
    common = int(bool(adj[x] & adj[y] & adj[z]))
    return (*e, common)


def fourth_signature(adj,xyz,w):
    x,y,z = xyz
    return (
        int(w in adj[x]),int(w in adj[y]),int(w in adj[z]),
        int(bool(adj[x] & adj[y] & adj[w])),
        int(bool(adj[x] & adj[z] & adj[w])),
        int(bool(adj[y] & adj[z] & adj[w])),
    )


def scan(adj):
    n=len(adj); d=len(adj[0]); assert all(len(nb)==d for nb in adj)
    assert n==d*d+1
    edge_pairs = 0; nonedge_pairs=0
    for u in range(n):
        for v in range(u+1,n):
            common=len(adj[u]&adj[v]); want=0 if v in adj[u] else 1
            assert common==want,(u,v,common,want)
            if want: nonedge_pairs+=1
            else: edge_pairs+=1
    profiles=defaultdict(set)
    counts=defaultdict(int)
    for xyz in permutations(range(n),3):
        t=triple_type(adj,xyz)
        sigs=frozenset(fourth_signature(adj,xyz,w) for w in range(n) if w not in xyz)
        profiles[t].add(sigs)
        counts[t]+=1
    assert all(len(s)==1 for s in profiles.values())
    assert all(t[3]==0 for t in profiles if sum(t[:3])>0)
    patterns={t:len(next(iter(vals))) for t,vals in profiles.items()}
    special = any(t==(0,0,0,1) and (0,0,0,0,0,0) in next(iter(vals)) for t,vals in profiles.items())
    return n,d,edge_pairs,nonedge_pairs,profiles,patterns,special


def canonical(profiles):
    return {t:next(iter(vals)) for t,vals in profiles.items()}


def main():
    P=petersen(); H=hoffman_singleton()
    NP,dP,ep,np,PP,pt,sp=scan(P)
    NH,dH,eh,nh,HP,ht,sh=scan(H)
    assert (NP,dP,ep,np)==(10,3,15,30)
    assert (NH,dH,eh,nh)==(50,7,175,1050)
    expected_p={
      (0,0,0,0):7,(0,0,0,1):4,
      (0,0,1,0):7,(0,1,0,0):7,(1,0,0,0):7,
      (0,1,1,0):4,(1,0,1,0):4,(1,1,0,0):4,
    }
    expected_h={
      (0,0,0,0):13,(0,0,0,1):6,
      (0,0,1,0):8,(0,1,0,0):8,(1,0,0,0):8,
      (0,1,1,0):4,(1,0,1,0):4,(1,1,0,0):4,
    }
    assert pt==expected_p,(pt,expected_p)
    assert ht==expected_h,(ht,expected_h)
    assert sp is False and sh is True
    # Compare independent actual profile multiplicities on one representative of
    # each triple type to symbolic counts (not merely existence supports).
    for adj,degree in [(P,3),(H,7)]:
        expected={
           'nonstar':[1]*6+[degree-3]*6+[(degree-3)**2+1],
           'star':[1,degree-3]+[degree-1]*3+[(degree-1)*(degree-3)],
           'oneedge':[1]*2+[degree-2]*5+[(degree-2)*(degree-3)],
           'path':[degree-2,degree-1,degree-1,(degree-1)*(degree-2)],
        }
        seen=set()
        for triple in permutations(range(len(adj)),3):
            t=triple_type(adj,triple)
            if t in seen: continue
            seen.add(t)
            k=sum(t[:3])
            name='nonstar' if k==0 and t[3]==0 else ('star' if k==0 else ('oneedge' if k==1 else 'path'))
            got=sorted(Counter(fourth_signature(adj,triple,w) for w in range(len(adj)) if w not in triple).values())
            want=sorted(x for x in expected[name] if x)
            assert got==want,(degree,t,got,want)
        assert len(seen)==8
    # Check exact support common to all ordered nonstar triples after permuting coordinates.
    # For every distinct triple, its full extended type is independent of the triple choice.
    for tag,t in [('Petersen',pt),('Hoffman-Singleton',ht)]:
      print(tag,'support_sizes='+str(sorted((str(k),v) for k,v in t.items())))
    print('Petersen: n=10 degree=3 edges=15 nonedges=30; Moore parameters PASS')
    print('Hoffman-Singleton: n=50 degree=7 edges=175 nonedges=1050; Moore parameters PASS')
    print('All ordered-distinct-triple enhanced extension profiles uniform: PASS')
    print('Six-bit profile support sizes and multiplicities for d=3 and d=7: PASS')
    print('Rank-four separating star-and-anticommon-neighbor formula: Petersen=FALSE, Hoffman-Singleton=TRUE')
    print('Finite graph verification: PASS')

if __name__=='__main__':main()
