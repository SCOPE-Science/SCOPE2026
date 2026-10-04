#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, Counter

VERTICES = tuple(range(2,14))
FACETS = [
(2,3,4,7),(2,3,4,10),(2,3,7,10),(2,4,5,7),(2,4,5,10),(2,5,7,13),(2,5,8,10),(2,5,8,13),
(2,6,9,11),(2,6,11,13),(2,6,12,13),(2,7,8,10),(2,7,8,11),(2,7,11,13),(2,8,9,11),(2,8,9,12),
(2,8,12,13),(3,4,6,7),(3,4,6,10),(3,5,8,13),(3,5,9,11),(3,5,9,13),(3,6,7,12),(3,6,10,13),
(3,6,12,13),(3,7,10,12),(3,8,9,11),(3,8,9,12),(3,8,12,13),(3,9,10,12),(3,9,10,13),(4,5,6,7),
(4,5,6,10),(5,6,7,9),(5,6,9,11),(5,6,10,11),(5,7,9,13),(6,10,11,13)
]

ALL_FACES=set()
for F in FACETS:
    for r in range(1,5):
        ALL_FACES.update(tuple(sorted(s)) for s in combinations(F,r))

def rank_mod2(row_masks):
    rows=[r for r in row_masks if r]
    rank=0
    while rows:
        pivot=max(rows)
        p=pivot.bit_length()-1
        rank+=1
        nxt=[]
        skipped=False
        for r in rows:
            if not skipped and r==pivot:
                skipped=True
                continue
            if (r>>p)&1:
                r ^= pivot
            if r:
                nxt.append(r)
        rows=nxt
    return rank

def betti(keep):
    keep=set(keep)
    bydim=defaultdict(list)
    for f in ALL_FACES:
        if set(f) <= keep:
            bydim[len(f)-1].append(f)
    if not bydim:
        return ()
    for d in bydim:
        bydim[d].sort()
    maxd=max(bydim)
    dims=[len(bydim.get(d,())) for d in range(maxd+1)]
    ranks=[0]*(maxd+2)
    for d in range(1,maxd+1):
        low={f:i for i,f in enumerate(bydim.get(d-1,()))}
        cols=bydim.get(d,())
        rows=[0]*len(low)
        for j,f in enumerate(cols):
            for sub in combinations(f,d):
                rows[low[tuple(sorted(sub))]] |= 1<<j
        ranks[d]=rank_mod2(rows)
    b=tuple(dims[d]-ranks[d]-ranks[d+1] for d in range(maxd+1))
    # Euler cross-check over F2 dimensions/ranks.
    chi_faces=sum(((-1)**d)*dims[d] for d in range(maxd+1))
    chi_betti=sum(((-1)**d)*b[d] for d in range(maxd+1))
    assert chi_faces==chi_betti
    return b

def acyclic(keep):
    b=betti(keep)
    return bool(b) and b[0]==1 and all(x==0 for x in b[1:])

def main():
    full=frozenset(VERTICES)
    acyclic_states=set()
    by_size_all=Counter()
    for mask in range(1,1<<len(VERTICES)):
        K=frozenset(VERTICES[i] for i in range(len(VERTICES)) if (mask>>i)&1)
        if acyclic(K):
            acyclic_states.add(K)
            by_size_all[len(K)] += 1
    assert len(acyclic_states)==585

    reachable={full}
    paths={full:1}
    layer_counts={12:1}
    for size in range(12,1,-1):
        nxt=set()
        for K in [S for S in reachable if len(S)==size]:
            for v in K:
                C=frozenset(set(K)-{v})
                if C in acyclic_states:
                    nxt.add(C)
                    paths[C]=paths.get(C,0)+paths.get(K,0)
        reachable |= nxt
        if nxt:
            layer_counts[size-1]=len(nxt)
    terminals=[]
    for K in reachable:
        if not any(frozenset(set(K)-{v}) in acyclic_states for v in K):
            terminals.append(K)
    terminals.sort(key=lambda S:(-len(S),tuple(sorted(S))))
    term_hist=Counter(map(len,terminals))
    maximal_paths=sum(paths[K] for K in terminals)
    paths_by_terminal_size=Counter()
    for K in terminals:
        paths_by_terminal_size[len(K)] += paths[K]

    expected_layers={12:1,11:11,10:36,9:52,8:31,7:3}
    assert layer_counts==expected_layers, layer_counts
    assert len(reachable)==134
    assert term_hist==Counter({8:17,7:3})
    assert maximal_paths==532
    assert paths_by_terminal_size==Counter({8:292,7:240})

    paper_kept={
        frozenset({2,3,6,7,9,12,13}),
        frozenset({2,3,6,7,8,9,13}),
        frozenset({2,3,5,8,10,11,13}),
    }
    terminal7={K for K in terminals if len(K)==7}
    assert terminal7==paper_kept

    terminal8=[sorted(K) for K in terminals if len(K)==8]
    assert len(terminal8)==17

    print('VERIFY_OK',
          'acyclic_all=585',
          'reachable=134',
          'layers=12:1,11:11,10:36,9:52,8:31,7:3',
          'terminals=8:17,7:3',
          'maximal_paths=532',
          'path_split=8:292,7:240',
          'paper_terminal7=match')
    print('TERMINAL8='+';'.join(','.join(map(str,K)) for K in terminal8))

if __name__=='__main__':
    main()
