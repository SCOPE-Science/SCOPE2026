#!/usr/bin/env python3
"""Exact, standalone verification of a finite Ferrers-grid modal-depth theorem.

Only Python's standard library is required. The mathematical statement is proved
separately; finite tests do not establish the unrestricted theorem.
"""
from itertools import combinations_with_replacement
from collections import defaultdict


def normalize(values):
    table = {}
    return tuple(table.setdefault(v, len(table)) for v in values)


def depth_partitions(lam, n):
    m = len(lam)
    states = [(i, j) for i in range(m) for j in range(n)]
    color = normalize(tuple(j < lam[i] for i, j in states))
    sizes = []
    for _ in range(m + n + 3):
        sizes.append(len(set(color)))
        rows = tuple(frozenset(color[i * n + j] for j in range(n)) for i in range(m))
        cols = tuple(frozenset(color[i * n + j] for i in range(m)) for j in range(n))
        nxt = normalize(tuple((color[i*n+j], rows[i], cols[j]) for i, j in states))
        if len(set(nxt)) == len(set(color)):
            break
        color = nxt
    return sizes


def predicted(lam, n, t):
    r = len(set(lam))
    c = len({sum(v > j for v in lam) for j in range(n)})
    assert abs(r - c) <= 1
    if r == c:
        return min(r*r, (t+1)*(t+1)+1)
    return min(r*c, (t+1)*(t+1)+int(t % 2 == 0))


def closure_from_generators(masks, universe):
    """Independent Boolean-closure enumeration from generators (not signatures)."""
    full = (1 << universe) - 1
    # Blocks are atoms of the generated Boolean algebra, represented by bit masks.
    blocks = [full]
    for gen in masks:
        blocks = [b & part for b in blocks for part in (gen, full ^ gen)
                  if (b & part)]
    return tuple(blocks)


def direct_depth_counts(lam, n):
    m = len(lam)
    N = m*n
    valuation = sum(1 << (i*n+j) for i in range(m) for j in range(n) if j < lam[i])
    atoms = closure_from_generators([valuation], N)
    answer = [len(atoms)]
    seen = {valuation}
    for _ in range(m+n+2):
        # All subsets definable by previous-depth formulas are unions of atoms.
        unions = [0]
        for atom in atoms:
            unions += [u | atom for u in unions]
        new = set()
        for u in unions:
            rows = [any(u & (1 << (i*n+j)) for j in range(n)) for i in range(m)]
            cols = [any(u & (1 << (i*n+j)) for i in range(m)) for j in range(n)]
            h = sum(1 << (i*n+j) for i in range(m) for j in range(n) if rows[i])
            v = sum(1 << (i*n+j) for i in range(m) for j in range(n) if cols[j])
            new.add(h);new.add(v)
        atoms2 = closure_from_generators([valuation] + list(seen | new), N)
        if len(atoms2) == len(atoms):
            break
        seen |= new
        atoms = atoms2
        answer.append(len(atoms))
    return answer


def run():
    shapes = 0; comparisons = 0; direct = 0; id_cases=0
    for m in range(1, 8):
        for n in range(1, 8):
            for sh in combinations_with_replacement(range(n+1), m):
                lam = sh[::-1]
                a = depth_partitions(lam, n)
                structural_check(lam, n)
                for t in range(m+n+2):
                    want = predicted(lam, n, t)
                    got = a[min(t, len(a)-1)]
                    assert got == want, (lam, n, t, got, want)
                    comparisons += 1
                shapes += 1
    for m in range(1,4):
        for n in range(1,4):
            for sh in combinations_with_replacement(range(n+1),m):
                lam = sh[::-1]
                a = depth_partitions(lam,n)
                b = direct_depth_counts(lam,n)
                assert a == b, (lam,n,a,b)
                direct += 1
    for m,n,lam in [(5,5,(5,4,3,2,1)),(6,5,(5,4,3,2,1,0)),
                    (4,5,(4,2,2,0)),(2,5,(4,4)),(8,8,(8,8,8,6,6,3,1,0))]:
        a=depth_partitions(lam,n)
        assert all(predicted(lam,n,t)==a[min(t,len(a)-1)] for t in range(m+n+3))
        id_cases+=1
    print(f'VERIFY_OK {shapes} Ferrers shapes; {comparisons} depth comparisons; '
          f'{shapes} structural wavefront tests; {direct} direct Boolean-closure cases; {id_cases} further witnesses')

# Additional structural check: number of distinct row and column successor-signatures.
def structural_check(lam, n):
    m=len(lam);r=len(set(lam)); heights=[sum(x>j for x in lam) for j in range(n)];c=len(set(heights))
    states=[(i,j) for i in range(m) for j in range(n)]
    colors=normalize(tuple(j<lam[i] for i,j in states))
    prev=None
    for t in range(m+n+2):
        if t==0:R=C=1
        else:
            R=len({frozenset(prev[i*n+j] for j in range(n)) for i in range(m)})
            C=len({frozenset(prev[i*n+j] for i in range(m)) for j in range(n)})
        if r==c:
            wantR=wantC=min(r,t+1)
        elif r==c+1:
            wantR=min(r,2*((t+1)//2)+1)
            wantC=min(c,2*(t//2)+1)
        else:
            wantR=min(r,2*(t//2)+1)
            wantC=min(c,2*((t+1)//2)+1)
        assert (R,C)==(wantR,wantC),(lam,n,t,(R,C),(wantR,wantC))
        prev=colors
        rows=[frozenset(colors[i*n+j] for j in range(n)) for i in range(m)]
        cols=[frozenset(colors[i*n+j] for i in range(m)) for j in range(n)]
        colors=normalize(tuple((prev[i*n+j],rows[i],cols[j]) for i,j in states))

if __name__ == "__main__":
    run()
