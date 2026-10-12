#!/usr/bin/env python3
"""Independent exhaustive recursion for all linear binary order-four universal partial words."""
from collections import Counter
from itertools import product
from pathlib import Path
A = ('0', '1', '*')
TARGET = set(map(''.join, product('01', repeat=4)))

def covered(window):
    return {''.join(v) for v in product('01', repeat=4)
            if all(x == '*' or x == y for x, y in zip(window, v))}

def is_upword(s):
    counts=Counter(v for i in range(len(s)-3) for v in covered(s[i:i+4]))
    return set(counts)==TARGET and all(k==1 for k in counts.values())

def enumerate_upwords():
    out=[]
    nodes=0
    def visit(s,used):
        nonlocal nodes
        nodes += 1
        if len(used)==16:
            out.append(s)
            return
        for ch in A:
            t=s+ch
            newly=covered(t[-4:])
            if not used.isdisjoint(newly):
                continue
            visit(t, used | newly)
    for prefix in map(''.join,product(A, repeat=3)):
        visit(prefix, set())
    return out,nodes

if __name__=='__main__':
    from sys import argv
    words,nodes=enumerate_upwords()
    histogram=Counter((len(s),s.count('*')) for s in words)
    expected={(4,4):1,(8,3):4,(11,2):4,(11,3):16,(14,2):8,(15,1):16,
              (16,1):8,(17,1):8,(18,1):64,(19,0):256}
    assert histogram == expected, (histogram, expected)
    assert len(words)==385 and nodes==15840
    assert all(is_upword(s) for s in words)
    assert len(set(words))==len(words)
    inv=lambda s:''.join({'0':'1','1':'0','*':'*'}[c] for c in s)
    S=set(words)
    assert all(s[::-1] in S and inv(s) in S for s in S)
    unvisited=set(S);orbits=Counter()
    while unvisited:
        s=next(iter(unvisited));orbit={s,s[::-1],inv(s),inv(s)[::-1]};assert orbit<=S
        unvisited-=orbit;orbits[len(orbit)]+=1
    print('NODES',nodes,'WORDS',len(words),'ORBITS',dict(sorted(orbits.items())))
    reps=sorted({min(s,s[::-1],inv(s),inv(s)[::-1]) for s in S if 0<s.count('*')<len(s)})
    assert len(reps)==32
    if '--check' in argv:
        target=Path(argv[argv.index('--check')+1]);assert target.read_text().splitlines()==sorted(words)
    if '--write-reps' in argv:
        target=Path(argv[argv.index('--write-reps')+1]);target.write_text(''.join(s+'\n' for s in reps))
    if '--check-reps' in argv:
        target=Path(argv[argv.index('--check-reps')+1]);assert target.read_text().splitlines()==reps
    print('HISTOGRAM',*(f'{a} {b} {n}' for (a,b),n in sorted(histogram.items())),sep='\n')
    if '--write' in argv:
        dest=Path(argv[argv.index('--write')+1]);dest.write_text(''.join(s+'\n' for s in sorted(words)))
    print('VERIFY_OK')
