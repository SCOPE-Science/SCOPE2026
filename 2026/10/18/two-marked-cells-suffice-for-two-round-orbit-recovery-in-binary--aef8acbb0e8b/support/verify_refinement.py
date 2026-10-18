#!/usr/bin/env python3
"""Independent counting-refinement test for binary addition-table 3-nets."""
from collections import Counter, defaultdict

def profile(x, y, H):
    return tuple(z if z in H else None for z in (x, y, x ^ y))

def refine(d, u, v):
    n = 1 << d
    V = [(x, y) for x in range(n) for y in range(n)]
    cols = [1 if p == (0, 0) else 2 if p == (u, v) else 0 for p in V]
    stages = []
    for step in range(5):
        groups = defaultdict(list)
        for ix, c in enumerate(cols): groups[c].append(ix)
        stages.append([frozenset(c) for c in groups.values()])
        # Sum color multiplicities on each named equivalence class, including the point itself.
        row = defaultdict(Counter)
        column = defaultdict(Counter)
        diagonal = defaultdict(Counter)
        for (x, y), c in zip(V, cols):
            row[x][c] += 1
            column[y][c] += 1
            diagonal[x ^ y][c] += 1
        signs = [(c, tuple(sorted(row[x].items())), tuple(sorted(column[y].items())),
                  tuple(sorted(diagonal[x ^ y].items()))) for (x, y), c in zip(V, cols)]
        labels = {s: i for i, s in enumerate(sorted(set(signs)))}
        nxt = [labels[s] for s in signs]
        if len(set(nxt)) == len(set(cols)):
            break
        cols = nxt
    H = {0, u, v, u ^ v}
    expected = defaultdict(set)
    for i, (x, y) in enumerate(V): expected[profile(x, y, H)].add(i)
    observed = {frozenset(s) for s in stages[-1]}
    target = {frozenset(s) for s in expected.values()}
    assert observed == target, (d, u, v, len(observed), len(target))
    r = len(H).bit_length()-1
    should = len(H)**2 + (3*len(H) if d>r else 0) + (1 if d>=r+2 else 0)
    assert len(observed)==should, (d, u, v, len(observed), should)
    min_step = len(stages)-1
    expect_step = 1 if (d==1 or (d==2 and r==1)) else 2
    assert min_step == expect_step, (d, u, v, [len(s) for s in stages], expect_step)
    return len(V), [len(s) for s in stages]

tests=0; total_vertices=0
for d in range(1,6):
    Bs=[(0,1),(1,0),(1,1)]
    if d>=2: Bs += [(1,2),(1,3),(2,3)]
    for u,v in Bs:
        n, counts=refine(d,u,v)
        print(f'd={d} marked=({u},{v}) vertices={n} rounds={counts}')
        tests+=1;total_vertices+=n
print('PASS: refinement equals linear stabilizer profile for',tests,
      'marked configurations and',total_vertices,'vertex instances')
