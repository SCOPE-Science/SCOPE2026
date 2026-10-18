#!/usr/bin/env python3
"""Check explicit rich-neighbor edge colorings of cyclic cubic ladders.

Only standard-library Python is required.  A finite check supports the proof;
the infinite assertion rests on the transition lemma and arithmetic coverage.
"""
from collections import defaultdict

# Each generator gives (rim-edge colors, rung-edge colors), indexed by column.
BLOCKS = {
    5: ([1,2,3,4,0], [3,4,0,1,2]),
    6: ([1,2,0,1,2,0], [3,4,3,4,3,4]),
    8: ([1,2,0,4,2,1,4,0], [3,4,3,1,3,0,3,2]),
    9: ([1,2,0,1,3,0,1,4,0], [3,4,3,4,2,4,2,3,2]),
}
# Entire coloring: top rim, bottom rim, then rungs.  Colors are integers 0..4.
EXCEPTIONAL = {
 (3, 0): [0,4,1, 0,4,1, 2,3,2],
 (3, 1): [0,4,1, 0,4,1, 2,3,2],
 (4, 0): [0,4,2,1, 1,2,0,3, 2,3,1,4],
 (4, 1): [0,3,2,0, 1,2,3,1, 2,4,1,4],
 (7, 0): [0,4,3,1,2,4,1, 0,4,3,1,2,4,1, 2,1,2,0,3,0,3],
 (7, 1): [0,4,3,1,2,4,1, 0,4,3,1,2,4,1, 2,1,2,0,3,0,3],
}

def good_transition(first, second):
    x, y, z = first
    u, v, w = second
    return y == u and len({u,v,w}) == 3 and len({x,v,z,w}) == 4

def block_states(a, c):
    return [(a[(i-1) % len(a)], a[i], c[i]) for i in range(len(a))]

def validate_blocks():
    for length,(a,c) in BLOCKS.items():
        s=block_states(a,c)
        assert len(a)==len(c)==length
        assert s[0] == (0,1,3), (length,s[0])
        assert all(len(set(state))==3 for state in s)
        assert all(good_transition(s[i],s[(i+1)%length]) for i in range(length)), length

def decomposition(n):
    if n in (5,6): return [n]
    if n < 8: raise ValueError(n)
    b=8+(n-8)%5
    starts={8:[8],9:[9],10:[5,5],11:[5,6],12:[6,6]}
    assert n>=b
    return starts[b]+[5]*((n-b)//5)

def coloring(n, twist):
    if (n,twist) in EXCEPTIONAL:
        return list(EXCEPTIONAL[(n,twist)])
    lengths=decomposition(n)
    a=sum((BLOCKS[k][0] for k in lengths),[])
    c=sum((BLOCKS[k][1] for k in lengths),[])
    assert len(a)==len(c)==n
    # A concatenation of cycles with a common state remains a cycle.
    s=block_states(a,c)
    assert all(good_transition(s[i],s[(i+1)%n]) for i in range(n))
    return a+a+c

def edges(n,twist):
    # Independent, directly topological construction; top and bottom wrap
    # to the opposite layer when twist==1.
    out=[]
    for row in (0,1):
        for i in range(n):
            endpoint=(1-row,0) if twist and i==n-1 else (row,(i+1)%n)
            out.append(((row,i),endpoint))
    for i in range(n):out.append(((0,i),(1,i)))
    return out

def inspect(n, twist, colors):
    E=edges(n,twist)
    assert len(E)==3*n==len(colors)
    assert len({frozenset(e) for e in E}) == len(E)
    assert all(v != w for v,w in E)
    assert set(colors) == set(range(5))
    incident=defaultdict(list)
    for idx,(v,w) in enumerate(E):
        incident[v].append(idx)
        incident[w].append(idx)
    assert len(incident)==2*n and all(len(incident[v])==3 for v in incident)
    neighbor=[(set(incident[v]) | set(incident[w]))-{i} for i,(v,w) in enumerate(E)]
    for i in range(len(E)):
        assert len(neighbor[i])==4
        assert all(colors[i]!=colors[j] for j in neighbor[i]), (n,twist,i)
    rich={i for i in range(len(E)) if len({colors[j] for j in neighbor[i]}) == 4}
    assert all(neighbor[i] & rich for i in range(len(E))), (n,twist,rich)
    return rich

if __name__=='__main__':
    validate_blocks()
    print('Four common-state block cycles: OK (5, 6, 8, 9)')
    print('Every length n>=8 decomposes into base 8..12 plus copies of 5; n=5,6 direct')
    for (n,twist),table in sorted(EXCEPTIONAL.items()):
        rich=sorted(inspect(n,twist,table))
        print('exception',n,'twisted' if twist else 'untwisted','rich edge indices:',','.join(map(str,rich)))
    examined=0
    for n in range(3,501):
        for twist in (0,1):
            inspect(n,twist,coloring(n,twist))
            examined +=1
    print(f'Exact witness check: PASS for {examined} graph instances (3 <= n <= 500, both closures)')
    print('VERIFIER_OK')
