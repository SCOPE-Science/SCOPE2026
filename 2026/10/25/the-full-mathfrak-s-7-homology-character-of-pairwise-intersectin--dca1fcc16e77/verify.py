#!/usr/bin/env python3
"""Exact rational S7-character check for pairwise-intersecting triples on seven points.

Uses only Python's standard library. Its character calculation is a finite,
fully enumerated signed Lefschetz calculation (not a chain-rank calculation).
The published rational Betti numbers are an explicit hypothesis.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import factorial

N = 7
TRIPLES = list(combinations(range(N), 3))
TRIPLE_ID = {a: i for i, a in enumerate(TRIPLES)}
EXPECTED = {
 (1,1,1,1,1,1,1): (-22,7,29),
 (1,1,1,1,1,2): (-6,-5,1),
 (1,1,1,1,3): (5,4,-1),
 (1,1,1,2,2): (-2,3,5),
 (1,1,1,4): (-4,-3,1),
 (1,1,2,3): (-3,-2,1),
 (1,1,5): (3,2,-1),
 (1,2,2,2): (-2,-1,1),
 (1,2,4): (0,1,1),
 (1,3,3): (-4,1,5),
 (1,6): (-2,-1,1),
 (2,2,3): (1,0,-1),
 (2,5): (-1,0,1),
 (3,4): (-1,0,1),
 (7,): (-1,0,1),
}

def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for k in range(minimum, n+1):
            for tail in integer_partitions(n-k, k):
                yield (k,) + tail

def representative(p):
    out = list(range(sum(p)))
    offset = 0
    for block in p:
        for j in range(block):
            out[offset+j] = offset + (j+1)%block
        offset += block
    return tuple(out)

def quotient_graph(g):
    induced = [TRIPLE_ID[tuple(sorted(g[i] for i in t))] for t in TRIPLES]
    used = set()
    valid_orbits = []
    for start in range(len(TRIPLES)):
        if start in used:
            continue
        orb = []
        x = start
        while x not in used:
            used.add(x)
            orb.append(x)
            x = induced[x]
        if all(set(TRIPLES[i]) & set(TRIPLES[j]) for i,j in combinations(orb,2)):
            valid_orbits.append(orb)
    size = len(valid_orbits)
    adjacent = [0]*size
    for i in range(size):
        for j in range(i):
            if any(not (set(TRIPLES[a]) & set(TRIPLES[b]))
                   for a in valid_orbits[i] for b in valid_orbits[j]):
                adjacent[i] |= 1<<j
                adjacent[j] |= 1<<i
    return adjacent

def independent_minus_one(adjacent):
    n = len(adjacent)
    @lru_cache(None)
    def recurse(mask):
        if mask == 0:
            return 1
        # Max-degree pivot is a performance aid, not a mathematical assumption.
        nodes = [v for v in range(n) if mask & (1<<v)]
        v = max(nodes, key=lambda j: (adjacent[j] & mask).bit_count())
        b = 1<<v
        return recurse(mask & ~b)-recurse(mask & ~(adjacent[v]|b))
    return recurse((1<<n)-1)

def brute_independent_minus_one(adjacent):
    n = len(adjacent)
    total = 0
    for mask in range(1<<n):
        ok = all(not (mask & (1<<v)) or not (mask & adjacent[v])
                 for v in range(n))
        if ok:
            total += -1 if mask.bit_count() % 2 else 1
    return total

def chi_pair(p):
    g = representative(p)
    graph = quotient_graph(g)
    score = independent_minus_one(graph)
    chi9 = (-1)**(N-len(p))*p.count(1)
    chi6 = -score+chi9
    return (score,chi9,chi6),graph

def partitions_desc(n):
    return [tuple(reversed(x)) for x in integer_partitions(n)]

@lru_cache(None)
def mn_character(lam, mu):
    if not mu:
        return 1 if not lam else 0
    r = mu[-1]
    total = 0
    for nu in partitions_desc(sum(lam)-r) if sum(lam)>=r else []:
        if len(nu)>len(lam) or any(nu[i]>lam[i] for i in range(len(nu))):
            continue
        cells = {(i,j) for i,t in enumerate(lam) for j in range(t)} - \
                {(i,j) for i,t in enumerate(nu) for j in range(t)}
        if len(cells)!=r:
            continue
        if any((i+1,j) in cells and (i,j+1) in cells and (i+1,j+1) in cells
               for i,j in cells):
            continue
        visited = {next(iter(cells))}
        stack = list(visited)
        while stack:
            i,j = stack.pop()
            for a,b in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if (a,b) in cells and (a,b) not in visited:
                    visited.add((a,b));stack.append((a,b))
        if len(visited)==r:
            total += (-1)**(len({i for i,j in cells})-1)*mn_character(nu,mu[:-1])
    return total

def centralizer_order(cycle_lengths):
    c = Counter(cycle_lengths)
    out = 1
    for length,multiplicity in c.items():
        out *= length**multiplicity * factorial(multiplicity)
    return out

def hook_dimension(lam):
    hooks = 1
    for i,t in enumerate(lam):
        for j in range(t):
            right = t-j-1
            below = sum(j<lam[ii] for ii in range(i+1,len(lam)))
            hooks *= 1 + right + below
    return factorial(sum(lam)) // hooks

def crosspolytope_transposition_degree():
    """Exact orientation degree of (0 1) on the ten-pair crosspolytope."""
    ground = set(range(6))
    triples = list(combinations(range(6),3))
    pair_representatives = sorted(min(t, tuple(sorted(ground-set(t)))) for t in triples)
    pairs = sorted(set(pair_representatives))
    assert len(pairs)==10
    lookup = {a:i for i,a in enumerate(pairs)}
    def pair_of(t):
        complement=tuple(sorted(ground-set(t)))
        return min(t,complement)
    def transposition(t):
        return tuple(sorted(1-x if x<2 else x for x in t))
    permutation = [lookup[pair_of(transposition(t))] for t in pairs]
    assert sorted(permutation)==list(range(10))
    inversions=sum(permutation[i]>permutation[j]
                   for i in range(10) for j in range(i+1,10))
    flipped=sum(
        pair_of(transposition(t))==t and transposition(t)!=t
        for t in pairs
    )
    # For a fixed antipodal pair, mapping a representative to its complement
    # reverses its S^0 orientation.
    assert inversions%2==1 and flipped==0,(inversions,flipped)
    return (-1)**(inversions+flipped)

def verify():
    assert crosspolytope_transposition_degree()==-1
    classes = list(integer_partitions(7))
    shapes = partitions_desc(7)
    assert set(classes)==set(EXPECTED) and len(classes)==len(shapes)==15
    results = {}
    for p in classes:
        actual,adjacent = chi_pair(p)
        assert actual==EXPECTED[p], (p,actual,EXPECTED[p])
        for j,neighbor in enumerate(adjacent):
            assert not ((neighbor>>j)&1)
            assert all(bool((neighbor>>k)&1)==bool((adjacent[k]>>j)&1)
                       for k in range(len(adjacent)))
        if len(adjacent)<=15:
            assert brute_independent_minus_one(adjacent)==actual[0]
        results[p]=actual
    assert results[(1,)*7]==(-22,7,29)
    # Column and row orthogonality: independent exact checks on the MN table.
    for p in classes:
        z = centralizer_order(p)
        assert sum(mn_character(lam,p)**2 for lam in shapes)==z
    for lam in shapes:
        assert mn_character(lam,(1,)*7)==hook_dimension(lam)
        for other in shapes:
            total = sum(mn_character(lam,p)*mn_character(other,p)*factorial(7)//centralizer_order(p)
                        for p in classes)
            assert total==factorial(7)*(lam==other), (lam,other,total)
    def decompose(col):
        return {lam:sum(results[p][col]*mn_character(lam,p)*factorial(7)//centralizer_order(p)
                        for p in classes)//factorial(7) for lam in shapes}
    for col in (1,2):
        for lam in shapes:
            numerator=sum(results[p][col]*mn_character(lam,p)*factorial(7)//centralizer_order(p)
                          for p in classes)
            assert numerator%factorial(7)==0
    d9=decompose(1)
    d6=decompose(2)
    assert {k:v for k,v in d9.items() if v}=={(1,1,1,1,1,1,1):1,(2,1,1,1,1,1):1},d9
    assert {k:v for k,v in d6.items() if v}=={(7,):1,(4,3):1,(2,2,2,1):1},d6
    assert sum(v*hook_dimension(k) for k,v in d6.items())==29
    assert sum(v*hook_dimension(k) for k,v in d9.items())==7
    print('PASS: all 15 classes, quotient graphs, exact independent-set recursion, 12 brute checks, Murnaghan-Nakayama orthogonality, Specht decomposition.')
    print('class cycle-type | I(Q;-1) | H9 | H6')
    for p in classes:
        print(str(p).ljust(23),*(str(x).rjust(4) for x in results[p]))
    print('H6:',{k:v for k,v in d6.items() if v})
    print('H9:',{k:v for k,v in d9.items() if v})

if __name__=='__main__':
    verify()
