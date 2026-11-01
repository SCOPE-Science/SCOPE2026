#!/usr/bin/env python3
"""Finite integral homotopy certificates for ordinary cut complexes of cycle squares.

Runs without third-party packages on Python 3.9+.  The claimed domain is
8 <= n <= 35; no assertion for n > 35 is made.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import comb

FIRST_N = 8
LAST_N = 35


def vertices_of(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def graph(n):
    return [sum(1 << ((v + d) % n) for d in (-2, -1, 1, 2)) for v in range(n)]


def disconnected_complement(f, n, adj):
    surviving = ((1 << n) - 1) ^ f
    reach = surviving & -surviving
    while True:
        nxt = reach
        for u in vertices_of(reach):
            nxt |= adj[u] & surviving
        if nxt == reach:
            return reach != surviving
        reach = nxt


def has_two_long_gaps(f, n):
    # A maximal run of deleted vertices starts at i when its predecessor
    # survives. It is long if the successor is also deleted.
    runs = 0
    for i in vertices_of(f):
        if not (f & (1 << ((i - 1) % n))) and (f & (1 << ((i + 1) % n))):
            runs += 1
    return runs >= 2


def complex_faces(n):
    adj = graph(n)
    facets = []
    for vs in combinations(range(n), 5):
        f = sum(1 << v for v in vs)
        is_facet = has_two_long_gaps(f, n)
        # An independent connectedness implementation checks all 5-sets
        # in the smaller half of the prescribed range.
        if n <= 18:
            assert is_facet == disconnected_complement(f, n, adj)
        if is_facet:
            facets.append(f)
    assert len(facets) == n * comb(n-5, 2), (n, len(facets))
    faces = set()
    for f in facets:
        s = f
        while s:
            faces.add(s)
            s = (s - 1) & f
    return faces, facets


def matching(faces, n):
    unmatched = set(faces)
    pairs = []
    # Stage-v pivot matching, the standard element matching.  The
    # complete acyclicity of the resulting directed Hasse diagram is
    # checked separately, without assuming the pivot lemma.
    for v in range(n):
        b = 1 << v
        for f in sorted(unmatched):
            top = f | b
            if not (f & b) and f in unmatched and top in unmatched:
                unmatched.remove(f)
                unmatched.remove(top)
                pairs.append((f, top))
    return unmatched, pairs


def verify_hasse_dag(faces, pairs):
    lower_to_upper = dict(pairs)
    upper_to_lower = {u: l for l, u in pairs}
    assert len(lower_to_upper) == len(upper_to_lower) == len(pairs)
    assert not set(lower_to_upper).intersection(upper_to_lower)
    indeg = {f: 0 for f in faces}
    incidences = 0
    for u in faces:
        if u.bit_count() == 1:
            continue
        for v in vertices_of(u):
            l = u ^ (1 << v)
            assert l in indeg
            incidences += 1
            if upper_to_lower.get(u) == l:
                indeg[u] += 1
            else:
                indeg[l] += 1
    queue = deque(f for f,d in indeg.items() if d == 0)
    count = 0
    while queue:
        f = queue.popleft()
        count += 1
        if f in lower_to_upper:
            u = lower_to_upper[f]
            indeg[u] -= 1
            if indeg[u] == 0:
                queue.append(u)
        if f.bit_count() > 1:
            match_lower = upper_to_lower.get(f)
            for v in vertices_of(f):
                l = f ^ (1 << v)
                if l == match_lower:
                    continue
                indeg[l] -= 1
                if indeg[l] == 0:
                    queue.append(l)
    assert count == len(faces), (count, len(faces))
    return incidences


def incidence(top, bottom):
    assert (top & bottom) == bottom and (top ^ bottom).bit_count() == 1
    missing = top ^ bottom
    return -1 if (top & (missing - 1)).bit_count() & 1 else 1


def morse_matrix(pairs, critical):
    lower_to_upper = dict(pairs)
    upper_set = {u for l,u in pairs}
    small = sorted(f for f in critical if f.bit_count() == 4)
    large = sorted(f for f in critical if f.bit_count() == 5)
    ids = {f:i for i,f in enumerate(small)}

    @lru_cache(maxsize=None)
    def reduce_face(f):
        # Algebraically eliminate all (3,4)-dimensional matched pairs.
        # Matched upper faces of dimension 3 project to zero.
        if f in ids:
            return {ids[f]:1}
        if f in upper_set:
            return {}
        assert f in lower_to_upper, (f, f.bit_count())
        top = lower_to_upper[f]
        coef = -incidence(top, f)
        accum = defaultdict(int)
        for v in vertices_of(top):
            g = top ^ (1 << v)
            if g == f:
                continue
            for i,c in reduce_face(g).items():
                accum[i] += coef * incidence(top, g) * c
        return {i:c for i,c in accum.items() if c}

    columns = []
    for h in large:
        accum = defaultdict(int)
        for v in vertices_of(h):
            f = h ^ (1 << v)
            for i,c in reduce_face(f).items():
                accum[i] += incidence(h,f) * c
        columns.append({i:c for i,c in accum.items() if c})
    return small, large, columns


def mod2_boundary_ranks(faces):
    levels = defaultdict(list)
    for f in faces:
        levels[f.bit_count()].append(f)
    rank = {}
    for size in range(2,6):
        loc = {f:i for i,f in enumerate(levels[size-1])}
        pivots = {}
        for top in levels[size]:
            x = 0
            for v in vertices_of(top):
                x ^= 1 << loc[top ^ (1 << v)]
            while x:
                b = x.bit_length()-1
                if b in pivots:
                    x ^= pivots[b]
                else:
                    pivots[b] = x
                    break
        rank[size-1] = len(pivots)
    return rank


def test(n):
    faces,facets = complex_faces(n)
    critical,pairs = matching(faces,n)
    incidences = verify_hasse_dag(faces,pairs)
    crit = Counter(f.bit_count()-1 for f in critical)
    beta = n*(n-8)*(n-7)//6
    assert crit == ({0:1,3:n-7,4:beta+n-8} if n>8 else {0:1,3:1}), (n,crit)
    assert len(faces) == 2*len(pairs)+len(critical)
    small,large,columns = morse_matrix(pairs,critical)
    assert len(small) == n-7 and len(large) == beta+n-8
    nonzero = [c for c in columns if c]
    assert len(nonzero) == n-8, (n,len(nonzero))
    assert sorted(nonzero,key=lambda c:next(iter(sorted(c)))) == [
        {i:1, n-8:-1} for i in range(n-8)
    ], (n,nonzero)
    assert sum((-1)**(f.bit_count()-1) for f in faces) == 1 + beta - 1  # Euler = beta
    if n in (8,9,10,11,12,13,14,16,20):
        rank = mod2_boundary_ranks(faces)
        f = Counter(x.bit_count() for x in faces)
        b3 = f[4]-rank[3]-rank[4]
        b4 = f[5]-rank[4]
        assert (b3,b4) == (1,beta), (n,b3,b4)
    return dict(n=n,k=n-5,facets=len(facets),faces=len(faces),pairs=len(pairs),critical_3=n-7,
                critical_4=beta+n-8,boundary_unit_rank=n-8,beta_4=beta,hasse_incidences=incidences)


def main():
    totals=Counter()
    for n in range(FIRST_N,LAST_N+1):
        r=test(n)
        for x in ('facets','faces','pairs','hasse_incidences'):
            totals[x]+=r[x]
        print('n={n:02} k={k:02} facets={facets:5} faces={faces:6} pairs={pairs:6} '
              'crit3={critical_3:2} crit4={critical_4:5} unit_rank={boundary_unit_rank:2} '
              'beta4={beta_4:5} hasse={hasse_incidences:6}'.format(**r),flush=True)
    print('CASES',LAST_N-FIRST_N+1,'TOTALS',dict(totals),flush=True)
    print('BORDERLINE_SQUARED_CYCLE_FINITE_INTEGRAL_HOMOTOPY_VERIFIED',flush=True)

if __name__=='__main__':
    main()
