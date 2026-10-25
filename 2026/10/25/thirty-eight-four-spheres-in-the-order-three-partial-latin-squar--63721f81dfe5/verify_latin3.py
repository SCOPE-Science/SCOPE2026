#!/usr/bin/env python3
"""Exact finite certificate for the order-three partial Latin-square complex.

Uses only the Python standard library. Each face is a 27-bit integer whose
bit (9*r+3*c+s) represents the assignment (r,c,s), for r,c,s in {0,1,2}.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd
from sys import setrecursionlimit

N = 3
V = [(r,c,s) for r in range(N) for c in range(N) for s in range(N)]
FORBIDDEN = [sum(1 << j for j in range(27)
                 if j != i and sum(V[j][q] == V[i][q] for q in range(3)) >= 2)
             for i in range(27)]

def faces():
    a = {}   # mask -> number of vertices
    def extend(mask, candidates, n):
        assert mask not in a
        a[mask] = n
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            i = bit.bit_length() - 1
            extend(mask | bit, candidates & ~FORBIDDEN[i], n + 1)
    extend(0, (1 << 27) - 1, 0)
    return a

def boundary(mask):
    """Signed codimension-one faces in increasing global vertex order."""
    order = 0
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        yield mask ^ bit, 1 if order % 2 == 0 else -1
        order += 1

def matching(size):
    unmatched = set(size)
    pairs = []
    stage = []
    for v in range(27):
        cnt = 0
        for a in sorted(unmatched):
            b = a | (1 << v)
            if b != a and b in unmatched:
                unmatched.remove(a)
                unmatched.remove(b)
                pairs.append((a,b))
                cnt += 1
        stage.append(cnt)
    assert pairs[0] == (0, 1)
    # Unmatch the empty face and one vertex, retaining a genuine 0-cell.
    pairs.remove((0,1))
    unmatched.add(0)
    unmatched.add(1)
    return pairs, unmatched, stage

def check_acyclic(size, pairs):
    upward = {a:b for a,b in pairs}
    indegree = defaultdict(int)
    adjacency = defaultdict(list)
    count = 0
    for b in size:
        for a,_ in boundary(b):
            assert a in size
            # Reverse exactly the Hasse edges corresponding to matching pairs.
            source, target = (b,a) if upward.get(a) == b else (a,b)
            adjacency[source].append(target)
            indegree[target] += 1
            count += 1
    queue = deque(s for s in size if indegree[s] == 0)
    seen = 0
    while queue:
        x = queue.popleft()
        seen += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert seen == len(size), (seen,len(size))
    return count

def morse_coefficients(size, pairs, critical):
    up = {a:b for a,b in pairs}
    down = {b:a for a,b in pairs}
    critical_3 = [m for m in critical if size[m] == 4]
    critical_4 = sorted(m for m in critical if size[m] == 5)
    assert len(critical_3) == 1 and len(critical_4) == 39
    critical_3 = critical_3[0]
    setrecursionlimit(50000)
    visiting = set()
    @lru_cache(None)
    def projection(a):
        assert size[a] == 4
        if a in critical:
            return int(a == critical_3)
        if a in down:
            return 0
        assert a in up
        assert a not in visiting, 'closed alternating gradient path'
        visiting.add(a)
        b = up[a]
        d = dict(boundary(b))
        assert abs(d[a]) == 1
        value = -sum(inc * projection(face) for face,inc in d.items()
                     if face != a) // d[a]
        visiting.remove(a)
        return value
    coeffs = [sum(inc * projection(face) for face,inc in boundary(b))
              for b in critical_4]
    assert set(coeffs) == {-1,0,1}
    assert gcd(*coeffs) == 1
    return critical_3, critical_4, coeffs

def rank_f2_columns(size, degree):
    levels = [[m for m in sorted(size) if size[m] == k] for k in range(10)]
    ranks = [0] * 10
    for k in range(1,10):
        base = {m:i for i,m in enumerate(levels[k-1])}
        pivots = {}
        for b in levels[k]:
            column = 0
            for a,_ in boundary(b):
                column ^= 1 << base[a]
            while column:
                p = column.bit_length() - 1
                if p not in pivots:
                    pivots[p] = column
                    break
                column ^= pivots[p]
        ranks[k] = len(pivots)
    assert ranks[1:] == [1,26,244,1034,2044,1752,660,96,12]
    betti = [len(levels[k]) - ranks[k] - (ranks[k+1] if k < 9 else 0)
             for k in range(10)]
    assert betti == [0,0,0,0,0,38,0,0,0,0], betti
    return ranks,betti

def main():
    size = faces()
    count = Counter(size.values())
    assert [count[k] for k in range(10)] == [1,27,270,1278,3078,3834,2412,756,108,12]
    facets = Counter()
    for m,n in size.items():
        if all((m | (1 << v)) not in size for v in range(27) if not (m >> v) & 1):
            facets[n] += 1
    assert facets == Counter({5:54,7:324,9:12}), facets
    pairs,critical,stages = matching(size)
    assert len(pairs) == 5867 and len(critical) == 42 # includes empty
    assert Counter(size[x]-1 for x in critical if x) == Counter({4:39,3:1,0:1})
    arcs = check_acyclic(size,pairs)
    assert arcs == 56619
    critical_3,critical_4,coefficients = morse_coefficients(size,pairs,critical)
    assert Counter(coefficients) == Counter({0:23,1:9,-1:7})
    ranks,betti = rank_f2_columns(size,0)
    print('FACE_COUNTS_BY_SIZE', ' '.join(f'{k}:{count[k]}' for k in range(10)))
    print('FACET_COUNTS_BY_SIZE',dict(sorted(facets.items())))
    print('MATCHED_PAIRS',len(pairs),'CRITICAL_NONEMPTY_DIMENSIONS',dict(sorted(Counter(size[x]-1 for x in critical if x).items())))
    print('HASSE_ARCS',arcs,'ACYCLIC_YES')
    print('MORSE_BOUNDARY_4_TO_3',dict(sorted(Counter(coefficients).items())))
    print('MORSE_BOUNDARY_GCD',gcd(*coefficients),'CRITICAL_3_MASK',critical_3)
    print('MOD_2_BOUNDARY_RANKS',ranks[1:])
    print('MOD_2_REDUCED_BETTI',betti[1:])
    print('INTEGRAL_HOMOTOPY','wedge_of_38_four_spheres')
    print('VERIFY_OK_LATIN3_PARTIAL_SQUARE_HOMOTOPY')

if __name__ == '__main__':
    main()
