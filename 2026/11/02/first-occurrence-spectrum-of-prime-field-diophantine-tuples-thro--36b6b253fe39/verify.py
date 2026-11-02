#!/usr/bin/env python3
"""Exhaustive prime-field Diophantine-tuple size certificate, pure Python 3.

Exactness argument: every n-element subset is a clique of the explicitly
constructed graph iff its products+1 are quadratic residues (zero allowed).
The recursive search visits all cliques not eliminated by a *valid* proper
coloring upper bound. All arithmetic and bitsets are unbounded exact integers.
"""
from __future__ import annotations
from hashlib import sha256
from pathlib import Path

LIMIT = 353
THRESHOLDS = (3, 7, 11, 23, 37, 59, 83, 131, 181, 251, 353)


def primes_through(n):
    s = bytearray(b'\1') * (n+1)
    s[:2] = b'\0\0'
    for d in range(2, int(n**0.5)+1):
        if s[d]:
            for j in range(d*d, n+1, d):
                s[j] = 0
    return [i for i in range(3,n+1) if s[i]]


def clique_number(p):
    residues = {r*r%p for r in range(p)}  # contains 0
    adjacency = [0]*(p-1)
    for a in range(1,p):
        for b in range(a+1,p):
            if (a*b+1)%p in residues:
                adjacency[a-1] |= 1 << (b-1)
                adjacency[b-1] |= 1 << (a-1)
    best = ()
    calls = 0
    def explore(pool, chosen):
        nonlocal best, calls
        calls += 1
        order = []
        bound = []
        left = pool
        colors = 0
        while left:
            colors += 1
            available = left
            while available:
                bit = available & -available
                u = bit.bit_length()-1
                order.append(u)
                bound.append(colors)
                left ^= bit
                available ^= bit
                available &= ~adjacency[u]
        # order[0:j+1] is properly colored with bound[j] colors.
        for j in range(len(order)-1,-1,-1):
            if len(chosen)+bound[j] <= len(best):
                return
            u = order[j]
            new_chosen = chosen+(u+1,)
            if len(new_chosen)>len(best):
                best = new_chosen
            nxt = pool & adjacency[u]
            if nxt:
                explore(nxt, new_chosen)
            pool ^= 1 << u
    explore((1<<(p-1))-1,())
    witness=tuple(sorted(best))
    assert len(witness)==len(set(witness))
    assert all(1<=a<p for a in witness)
    assert all((a*b+1)%p in residues for i,a in enumerate(witness) for b in witness[i+1:])
    return len(witness), witness, calls


def main():
    first = {}
    records=[]
    for p in primes_through(LIMIT):
        maximum,witness,calls = clique_number(p)
        records.append((p,maximum,calls,witness))
        for m in range(2,maximum+1):
            first.setdefault(m,p)
    assert tuple(first[m] for m in range(2,13)) == THRESHOLDS, first
    assert records[-1][0]==353 and records[-1][1]==12
    # Value at 353 certified against a potential 13-clique by the same search.
    text='p,M(p),nodes,witness\n'+''.join(
        f'{p},{m},{c},"{",".join(map(str,w))}"\n'
        for p,m,c,w in records)
    output=Path(__file__).with_name('SPECTRUM.csv')
    output.write_bytes(text.encode('ascii'))
    print('PASS: exact prime-field size spectrum for all',len(records),'odd primes <=',LIMIT)
    print('first-prime thresholds for m=2..12:', *(first[m] for m in range(2,13)))
    print('M(353)=12; witness:',records[-1][-1])
    print('SHA256(SPECTRUM.csv):',sha256(output.read_bytes()).hexdigest())

if __name__=='__main__':
    main()
