#!/usr/bin/env python3
"""Exhaustive maximal binary non-overlap code catalogue (pure Python 3)."""
from collections import Counter
from hashlib import sha256
import sys

N=9

def unbordered(x):
    return all(x >> (N-k) != (x & ((1<<k)-1)) for k in range(1,N))

def compatible(x,y):
    return all(x >> (N-k) != (y & ((1<<k)-1)) and
               y >> (N-k) != (x & ((1<<k)-1)) for k in range(1,N))

def rev(x):
    return int(format(x,'09b')[::-1],2)

def main():
    words=[x for x in range(1<<N) if unbordered(x)]
    edges=[0]*len(words)
    for i in range(len(words)):
        for j in range(i):
            if compatible(words[i],words[j]):
                edges[i]|=1<<j
                edges[j]|=1<<i
    count=Counter(); catalogue=[]; orbitseen=set(); symtypes=Counter()
    def visit(sel):
        code=tuple(words[i] for i in sel)
        assert len(code)==len(set(code))
        assert all(compatible(x,y) for j,x in enumerate(code) for y in code[:j])
        assert all(not all(compatible(v,w) for w in code) for v in words if v not in code)
        catalogue.append(code);count[len(code)]+=1
    def rec(P,X,R):
        if not P and not X:
            visit(R);return
        # Tomita pivot: a maximal clique containing R must contain one
        # vertex in P outside the chosen pivot's neighbourhood.
        union=P|X
        if union:
            pivot=max((i for i in range(len(words)) if union>>i&1),
                      key=lambda i:(P & edges[i]).bit_count())
            choices=P & ~edges[pivot]
        else: choices=P
        while choices:
            bit=choices&-choices;choices-=bit
            i=bit.bit_length()-1
            rec(P&edges[i],X&edges[i],R+(i,))
            P-=bit;X|=bit
    rec((1<<len(words))-1,0,())
    codes={tuple(sorted(C)) for C in catalogue}
    assert len(codes)==len(catalogue)
    for C in codes:
        orbit={tuple(sorted(((rev(x) if r else x)^(511 if b else 0)) for x in C))
               for r in (0,1) for b in (0,1)}
        if C not in orbitseen:
            assert orbit<=codes
            symtypes[(len(C),len(orbit))]+=1
            orbitseen.update(orbit)
    assert orbitseen==codes
    print('unbordered',len(words),'edges',sum(x.bit_count() for x in edges)//2)
    print('histogram',sorted(count.items()))
    print('symmetry_orbits',sorted(symtypes.items()))
    assert count=={1:4,4:12,5:20,6:48,7:200,8:588,9:1712,10:5056,11:13520,12:23136,13:16832,14:1152}
    assert len(codes)==62280 and len(orbitseen)==62280
    if '--catalog' in sys.argv:
        with open('catalog_python.txt','w',encoding='ascii',newline='\n') as f:
            for c in sorted(codes): f.write(' '.join(format(x,'09b') for x in c)+'\n')
    print('PASS')
if __name__=='__main__':main()
