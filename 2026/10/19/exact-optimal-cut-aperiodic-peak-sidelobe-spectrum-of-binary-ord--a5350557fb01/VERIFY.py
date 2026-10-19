#!/usr/bin/env python3
"""Exhaustive, independent certificates for phase-cut aperiodic PSL on binary order-five de Bruijn cycles."""
from collections import Counter
from fractions import Fraction
N=32
EXPECTED={4:32,5:344,6:476,7:666,8:236,9:174,10:20,11:8,12:20,15:64,16:8}

def canon(bits):
    s=''.join(map(str,bits))
    assert len(s)==N
    starts=[i for i in range(N) if ''.join(s[(i+j)%N] for j in range(5))=='00000']
    assert len(starts)==1, (s,starts)
    i=starts[0]
    t=s[i:]+s[:i]
    assert {''.join(t[(k+j)%N] for j in range(5)) for k in range(N)}=={f'{h:05b}' for h in range(N)}
    return t

def euler_dfs():
    cycles=set()
    def recur(vertex, used, out):
        if used.bit_count()==N:
            if vertex==0:
                s=canon(out)
                assert s not in cycles
                cycles.add(s)
            return
        for b in (0,1):
            e=vertex*2+b
            if not used>>e&1:
                recur(e&15, used|1<<e, out+[b])
    recur(0,1,[0])  # anchor the unique edge 00000
    return cycles

def edge_pairings():
    cycles=set()
    for mask in range(1<<16):
        successor=[0]*N
        for v in range(16):
            c=(mask>>v)&1
            successor[v]=2*v+c
            successor[v+16]=2*v+1-c
        e=0
        seen=0
        edges=[]
        for _ in range(N):
            if (seen>>e)&1:
                break
            seen|=1<<e
            edges.append(e)
            e=successor[e]
        if len(edges)==N and e==0:
            s=canon([edge&1 for edge in edges])
            assert s not in cycles, (mask,s)
            cycles.add(s)
    return cycles

def all_phase_psls(s):
    signs=[1 if b=='0' else -1 for b in s]
    return tuple(max(abs(sum(signs[(r+j)%N]*signs[(r+j+h)%N] for j in range(N-h))) for h in range(1,N)) for r in range(N))

def psl_from_disagreements(s):
    vals=[]
    for r in range(N):
        word=s[r:]+s[:r]
        lagmax=0
        for h in range(1,N):
            disagreements=sum(word[j]!=word[j+h] for j in range(N-h))
            lagmax=max(lagmax,abs((N-h)-2*disagreements))
        vals.append(lagmax)
    return tuple(vals)

def main():
    a=euler_dfs()
    b=edge_pairings()
    assert len(a)==len(b)==2048
    assert a==b
    second_hist=Counter(min(psl_from_disagreements(s)) for s in b)
    assert dict(sorted(second_hist.items()))==EXPECTED
    hist=Counter()
    cutmult=Counter()
    best_w={}
    for s in a:
        vals=all_phase_psls(s)
        p=min(vals)
        hist[p]+=1
        cutmult[(p,vals.count(p))]+=1
        best_w[s]=p
        # Boundary consistency check: cyclic sidelobe is sum of complementary aperiodic sidelobes.
        spins=[1 if x=='0' else -1 for x in s]
        for h in range(1,N):
            period=sum(spins[j]*spins[(j+h)%N] for j in range(N))
            x=sum(spins[j]*spins[j+h] for j in range(N-h))
            y=sum(spins[j]*spins[j+N-h] for j in range(h))
            assert x+y==period
    assert dict(sorted(hist.items()))==EXPECTED, sorted(hist.items())
    assert cutmult[(4,1)]==24 and cutmult[(4,2)]==8
    assert sum(v for (k,c),v in cutmult.items() if k==4)==32
    total=sum(k*v for k,v in hist.items())
    mean=Fraction(total,2048)
    var=Fraction(sum(k*k*v for k,v in hist.items()),2048)-mean*mean
    min_example=min(s for s,v in best_w.items() if v==4)
    max_example=min(s for s,v in best_w.items() if v==16)
    print('PHASE_APERIODIC_PSL_DB5_PASS cycles=2048 switch_profiles=65536 exact_hist='+str(sorted(hist.items())))
    print('mean=',mean,'variance=',var)
    print('min_example=',min_example,'max_example=',max_example)
    print('minimum_phase_multiplicities=',sorted((c,v) for (k,c),v in cutmult.items() if k==4))
    transform=lambda s:(canon(s),canon(s[::-1]),canon(''.join('1' if c=='0' else '0' for c in s)),canon(''.join('1' if c=='0' else '0' for c in s[::-1])))
    for extremum in (4,16):
        group=set(s for s,p in best_w.items() if p==extremum)
        orbit_lengths=Counter()
        while group:
            x=min(group)
            orbit=set(transform(x))
            assert orbit<=group
            group-=orbit
            orbit_lengths[len(orbit)]+=1
        print('extreme_symmetry_orbits=',extremum,sorted(orbit_lengths.items()))
if __name__=='__main__': main()
