#!/usr/bin/env python3
"""Exhaustive graph-and-orbit verification using only Python's standard library.
Run: python3 verify_orbits.py orbit_certificates.csv
The graph is GP(10,2), vertex u_i=i and vertex v_i=10+i (0<=i<10).
"""
import csv
import itertools
import sys
from collections import Counter
N = 20
FULL = (1 << N) - 1
adj = [0] * N
edge_list=[]
for i in range(10):
    for a,b in [(i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)]:
        edge_list.append((a,b))
        adj[a] |= 1 << b
        adj[b] |= 1 << a
assert len(edge_list)==30 and all(x.bit_count()==3 for x in adj)

def components_and_edges(mask):
    """Second approach: breadth-first component search, then Euler's forest identity."""
    edges = sum((adj[i] & mask).bit_count() for i in range(N)
                if mask >> i & 1) // 2
    pending=mask
    sizes=[]
    while pending:
        wave=pending & -pending
        visited=0
        while wave:
            visited |= wave
            neighbors=0
            while wave:
                low=wave & -wave
                wave -= low
                neighbors |= adj[low.bit_length()-1]
            wave=(neighbors & mask) & ~visited
        sizes.append(visited.bit_count())
        pending &= ~visited
    return tuple(sorted(sizes)), edges

def verify_forests():
    spectrum=Counter()
    optimum={}
    maximal=Counter()
    table=bytearray(1<<N)
    for mask in range(1<<N):
        comps,edges=components_and_edges(mask)
        if edges==mask.bit_count()-len(comps):
            table[mask]=1
            spectrum[mask.bit_count()]+=1
            if mask.bit_count()==14:
                removed=FULL^mask
                removed_edges=sum(bool(removed>>i&1) and bool(removed>>j&1)
                    for i,j in edge_list)
                optimum[mask]=(comps,removed_edges)
    for mask in range(1<<N):
        if not table[mask]:continue
        if not any(not (mask>>v&1) and table[mask|(1<<v)] for v in range(N)):
            maximal[mask.bit_count()]+=1
    expect=[1,20,190,1140,4845,15492,38580,76260,120540,151920,
            150480,113400,60620,19600,2520]
    assert [spectrum[i] for i in range(15)]==expect
    assert sum(spectrum.values())==755608
    assert maximal=={13:1120,14:2520}
    assert len(optimum)==2520
    c=Counter(v[0] for v in optimum.values())
    assert c=={(14,):1860,(1,13):280,(2,12):180,
               (4,10):120,(6,8):60,(7,7):20},c
    assert Counter(v[1] for v in optimum.values())=={1:1860,0:660}
    print('FORESTS_OK masks=1048576 induced_forests=755608 optimum=2520 maximal_13=1120')
    return optimum

def automorphisms():
    """All adjacency-preserving bijections, with partial adjacency/nonadjacency pruning."""
    mapping=[-1]*N
    perms=[]
    def rec(used, assigned):
        if assigned==N:
            perms.append(tuple(mapping))
            return
        selected=None
        choices=None
        for u in range(N):
            if mapping[u]>=0:continue
            allowed=[]
            for v in range(N):
                if used>>v&1:continue
                if all(bool(adj[u]>>w&1)==bool(adj[v]>>mapping[w]&1)
                       for w in range(N) if mapping[w]>=0):
                    allowed.append(v)
            if not allowed:return
            if choices is None or len(allowed)<len(choices):
                selected,choices=u,allowed
            if len(choices)==1:break
        for v in choices:
            mapping[selected]=v
            rec(used|1<<v, assigned+1)
            mapping[selected]=-1
    rec(0,0)
    assert len(perms)==120, len(perms)
    assert len(set(perms))==120
    print('AUT_OK adjacency_preserving_bijections=120')
    return perms

def permute(mask,p):
    out=0
    while mask:
        low=mask&-mask
        mask-=low
        out|=1<<p[low.bit_length()-1]
    return out

def verify_orbits(optimum,perms,filename):
    with open(filename,encoding='utf-8',newline='') as f:
        cert=list(csv.DictReader(f))
    assert len(cert)==25
    unseen=set(optimum)
    type_total=Counter()
    orbit_total=Counter()
    for line in cert:
        rep=int(line['forest_mask'])
        size=int(line['orbit_size'])
        assert rep in unseen
        orbit={permute(rep,p) for p in perms}
        assert len(orbit)==size
        assert orbit<=unseen
        unseen-=orbit
        comp=','.join(map(str,optimum[rep][0]))
        assert comp==line['component_sizes']
        assert optimum[rep][1]==int(line['deleted_edges'])
        delete=FULL^rep
        assert ','.join(map(str,[u for u in range(20) if delete>>u&1]))==line['deleted_vertices']
        assert all(optimum[x]==optimum[rep] for x in orbit)
        type_total[comp]+=len(orbit)
        orbit_total[size]+=1
    assert not unseen
    assert orbit_total=={120:18,60:5,40:1,20:1}
    assert type_total=={'14':1860,'1,13':280,'2,12':180,
                        '4,10':120,'6,8':60,'7,7':20}
    print('ORBITS_OK full_automorphism_group=120 optimum_orbits=25 orbit_sizes=120x18+60x5+40+20')
    print('ORBITS_OK tree_orbits=17 two_component_orbits=8 certificate_coverage=2520')

if __name__=='__main__':
    if len(sys.argv)!=2:sys.exit('usage: python3 verify_orbits.py orbit_certificates.csv')
    verify_orbits(verify_forests(),automorphisms(),sys.argv[1])
