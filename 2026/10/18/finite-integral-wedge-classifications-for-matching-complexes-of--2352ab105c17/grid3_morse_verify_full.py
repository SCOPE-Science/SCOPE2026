#!/usr/bin/env python3
"""Exhaustive finite discrete-Morse certificates for matching complexes of
3-by-n rectangular grids, widths 2 through 8. Standard Python only.
"""
from collections import Counter, deque
from functools import lru_cache
from math import gcd
from functools import reduce
from time import monotonic

EXPECTED = {2: 2, 3: 5, 4: 9, 5: 16, 6: 31, 7: 55}

def grid_edges(n):
    # Vertices (row,column), row 0..2, column 0..n-1.
    E = []
    for r in range(3):
        for c in range(n):
            if r + 1 < 3:
                E.append(((r,c),(r+1,c)))
            if c + 1 < n:
                E.append(((r,c),(r,c+1)))
    return sorted(tuple(sorted(x)) for x in E)

def complete_faces(edges, n):
    # Each edge can be selected if both endpoints are unused.
    V = {(r,c):3*c+r for r in range(3) for c in range(n)}
    vertex_masks = [(1<<V[a]) | (1<<V[b]) for a,b in edges]
    F = set()
    def extend(start, occupied, mask):
        F.add(mask)
        for i in range(start,len(edges)):
            if occupied & vertex_masks[i] == 0:
                extend(i+1,occupied | vertex_masks[i],mask | (1<<i))
    extend(0,0,0)
    return F

def pair_in_order(F, edges):
    # All row-parallel edges first, followed by all column-parallel edges.
    # Within each group, the order is the lexicographic edge ordering.
    order = sorted(range(len(edges)), key=lambda i:
                   (edges[i][0][0] != edges[i][1][0], edges[i]))
    remaining = set(F)
    lower_to_upper = {}
    upper_to_lower = {}
    for i in order:
        bit = 1 << i
        for low in sorted(tuple(remaining)):
            top = low | bit
            if top != low and top in remaining:
                remaining.remove(low)
                remaining.remove(top)
                lower_to_upper[low] = top
                upper_to_lower[top] = low
    return remaining, lower_to_upper, upper_to_lower

def check_acyclic(F, lower_to_upper, upper_to_lower):
    # Orient matched Hasse edges upward and every other cover downward.
    # Exact topological sorting of the *entire* directed Hasse graph.
    indegree = {f:0 for f in F}
    for higher in F:
        u = higher
        while u:
            bit = u & -u
            lower = higher ^ bit
            if lower_to_upper.get(lower) == higher:
                indegree[higher] += 1
            else:
                indegree[lower] += 1
            u ^= bit
    queue = deque(f for f,deg in indegree.items() if deg == 0)
    processed = 0
    while queue:
        f = queue.popleft()
        processed += 1
        matched_upper = lower_to_upper.get(f)
        if matched_upper is not None:
            indegree[matched_upper] -= 1
            if indegree[matched_upper] == 0:
                queue.append(matched_upper)
        x = f
        while x:
            bit = x & -x
            lower = f ^ bit
            if lower_to_upper.get(lower) != f:
                indegree[lower] -= 1
                if indegree[lower] == 0:
                    queue.append(lower)
            x ^= bit
    assert processed == len(F), ('gradient directed cycle', processed, len(F))
    return processed

def verify(n):
    begin = monotonic()
    edges = grid_edges(n)
    assert len(edges) == 5*n-3
    F = complete_faces(edges,n)
    critical, lows, highs = pair_in_order(F,edges)
    assert len(F) == 2*len(lows) + len(critical)
    assert set(lows).isdisjoint(highs)
    assert 0 not in critical and 0 in lows
    hist = Counter(mask.bit_count()-1 for mask in critical)
    assert hist == {n-1:EXPECTED[n]}, (n,hist)
    acyclic_vertices = check_acyclic(F,lows,highs)
    assert acyclic_vertices == len(F)
    # Removing the (empty,vertex) pair leaves one ordinary critical vertex.
    # Other pairs constitute a valid acyclic matching on nonempty simplices.
    vertex = lows[0]
    assert vertex.bit_count() == 1
    print('n=%d edges=%d faces_including_empty=%d pairs=%d'
          ' critical_top=%d critical_dimension=%d directed_Hasse_DAG_nodes=%d'
          ' seconds=%.3f' %
          (n,len(edges),len(F),len(lows),len(critical),n-1,
           acyclic_vertices,monotonic()-begin),flush=True)

def verify_eight():
    n = 8
    edges = grid_edges(n)
    F = complete_faces(edges, n)
    horizontals = [i for i,e in enumerate(edges) if e[0][0] == e[1][0]]
    verticals = [i for i,e in enumerate(edges) if e[0][0] != e[1][0]]
    horizontals.sort(key=lambda i:(edges[i][0][1] % 2,
                                   edges[i][0][1], edges[i][0][0]))
    remaining = set(F)
    low_to_high = {}
    high_to_low = {}
    for i in horizontals + verticals:
        bit = 1 << i
        for low in tuple(remaining):
            high = low | bit
            if high != low and high in remaining:
                remaining.remove(low)
                remaining.remove(high)
                low_to_high[low] = high
                high_to_low[high] = low
    assert len(F) == 1222550
    assert len(low_to_high) == 611227
    assert Counter(x.bit_count()-1 for x in remaining) == {7:95,8:1}
    assert 0 in low_to_high
    # The full directed face-poset Hasse graph is checked, not sampled.
    assert check_acyclic(F,low_to_high,high_to_low) == len(F)
    top = next(x for x in remaining if x.bit_count()==9)
    critical_lower = {x for x in remaining if x.bit_count()==8}
    def boundary(U):
        b=U
        i=0
        while b:
            t=b&-b
            yield U^t, (-1)**i
            b ^= t
            i += 1
    @lru_cache(None)
    def project(L):
        if L in critical_lower:
            return {L:1}
        if L in high_to_low:
            return {}  # Paired above a six-cell: no seven-critical projection.
        assert L in low_to_high
        U = low_to_high[L]
        assert U.bit_count()==9
        column = dict(boundary(U))
        pivot = column[L]
        output = {}
        for J,s in column.items():
            if J==L: continue
            for T,v in project(J).items():
                output[T] = output.get(T,0)-pivot*s*v
        return {T:v for T,v in output.items() if v}
    result={}
    for L,c in boundary(top):
        for T,v in project(L).items():
            result[T] = result.get(T,0) + c*v
    result={T:v for T,v in result.items() if v}
    expected={2755666018:1,36544987234:1,2753634376:1,
              36542940232:1,36509401192:-1}
    assert result == expected, ('integral Morse boundary mismatch',result)
    assert reduce(gcd,(abs(c) for c in result.values())) == 1
    print('n=8 edges=37 faces_including_empty=1222550 pairs=611227'
          ' critical_dim7=95 critical_dim8=1 DAG_nodes=1222550'
          ' integral_boundary=' + repr(sorted(result.items())),flush=True)
    print('n=8 integral CW attaching map primitive; homotopy type wedge of 94 seven-spheres',flush=True)

if __name__ == '__main__':
    for n in EXPECTED:
        verify(n)
    verify_eight()
    print('ALL CERTIFICATES PASSED',flush=True)
