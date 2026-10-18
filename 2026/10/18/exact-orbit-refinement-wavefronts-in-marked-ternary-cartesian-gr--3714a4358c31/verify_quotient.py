"""Independent multiplicity-weighted orbit quotient test for rooted P3 Cartesian powers.

Usage: python verify_quotient.py
"""
from collections import Counter, defaultdict


def quotient(d):
    states = [(b,c) for b in range(d+1) for c in range(d-b+1)]
    arcs = {}
    for b,c in states:
        a = d-b-c
        n = Counter()
        if a:
            n[b+1,c] += a
        if b:
            n[b-1,c] += b
            n[b-1,c+1] += b
        if c:
            n[b+1,c-1] += c
        assert sum(n.values()) == d+b
        arcs[b,c] = n
    return states,arcs


def expected_equivalence(d,t):
    states,_ = quotient(d)
    def key(s):
        b,c=s
        if t==0: return ('root',) if s==(0,0) else ('other',)
        if b+2*c<=t:return ('reached',b,c)
        return ('not_reached',b)
    return {s:key(s) for s in states}


def same_partition(c,e,states):
    forward = {}
    backward = {}
    for s in states:
        if c[s] in forward and forward[c[s]]!=e[s]:return False
        if e[s] in backward and backward[e[s]]!=c[s]:return False
        forward[c[s]]=e[s]
        backward[e[s]]=c[s]
    return True


def run(d):
    states,arcs=quotient(d)
    colors={s:int(s==(0,0)) for s in states}
    assert same_partition(colors,expected_equivalence(d,0),states)
    stable=None
    for t in range(1,2*d+2):
        signatures={}
        for s in states:
            counts=Counter()
            for dest,m in arcs[s].items(): counts[colors[dest]]+=m
            signatures[s]=(colors[s],tuple(sorted(counts.items())))
        palette={z:i for i,z in enumerate(sorted(set(signatures.values())))}
        new={s:palette[signatures[s]] for s in states}
        assert same_partition(new,expected_equivalence(d,t),states),(d,t)
        if len(set(new.values()))==len(set(colors.values())) and stable is None:
            stable=t-1
        colors=new
    assert stable==2*d-2,(d,stable)
    assert len(set(colors.values()))==(d+1)*(d+2)//2
    return stable


if __name__ == '__main__':
    for d in list(range(2,19))+[20,25,30,35,40,50,60]:
        print(f'quotient d={d} cells={(d+1)*(d+2)//2} depth={run(d)} PASS')
    print('QUOTIENT CHECK PASSED')
