#!/usr/bin/env python3
"""Exact finite certificates for independence complexes of C_m x K_3.

Requires only the Python standard library.  Each simplicial face is a bitmask
with bit 3i+a corresponding to the vertex (i,a), a in {0,1,2}.
All graph products here are categorical, not Cartesian.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations
from math import prod

CYCLE_LENGTHS = (7, 8, 10)
EXPECTED = {
    7: {'face_count': 5281, 'pairs': 2635, 'incidences': 25221,
        'critical': {0: 1, 3: 4, 4: 6}, 'degree': 4,
        'rank': 3, 'lower_betti': 1, 'upper_betti': 3},
    8: {'face_count': 18721, 'pairs': 9353, 'incidences': 104568,
        'critical': {0: 1, 4: 6, 5: 8}, 'degree': 5,
        'rank': 5, 'lower_betti': 1, 'upper_betti': 3},
    10: {'face_count': 216257, 'pairs': 108121, 'incidences': 1502070,
         'critical': {0: 1, 5: 8, 6: 6}, 'degree': 6,
         'rank': 5, 'lower_betti': 3, 'upper_betti': 1},
}


def adjacency(m):
    n = 3*m
    adj = [0]*n
    for i in range(m):
        for a in range(3):
            v = 3*i+a
            for j in ((i-1) % m, (i+1) % m):
                for b in range(3):
                    if a != b:
                        adj[v] |= 1 << (3*j+b)
    assert all(not (adj[v] >> v & 1) for v in range(n))
    assert all(bool(adj[v] >> w & 1) == bool(adj[w] >> v & 1)
               for v in range(n) for w in range(n))
    return adj


def enumerate_faces(adj):
    faces = [0]
    for v, nbrs in enumerate(adj):
        bit = 1 << v
        faces.extend([s | bit for s in faces if not s & nbrs])
    assert len(set(faces)) == len(faces)
    assert all(not s & adj[v] for s in faces
               for v in range(len(adj)) if s & (1 << v))
    return faces


def layer_transfer_face_count(m):
    # Independent enumeration: a layer is any 3-bit color subset.
    # Adjacent occupied layers are compatible only when both are
    # the very same singleton color (otherwise an edge occurs).
    states = range(8)
    compat = [[(s == 0 or t == 0 or
                (s.bit_count() == t.bit_count() == 1 and s == t))
               for t in states] for s in states]
    n = 0
    for s0 in states:
        counts = [0]*8
        counts[s0] = 1
        for _ in range(1, m):
            counts = [sum(counts[s] for s in states if compat[s][t])
                      for t in states]
        n += sum(counts[t] for t in states if compat[t][s0])
    return n


def signed_boundary(simplex):
    t = simplex
    idx = 0
    while t:
        bit = t & -t
        t -= bit
        yield simplex ^ bit, 1 if idx % 2 == 0 else -1
        idx += 1


def matching(faces, n):
    live = set(faces)
    live.remove(0)
    pairs = []
    for v in range(n):
        bit = 1 << v
        for lo in sorted(live):
            hi = lo | bit
            if not lo & bit and hi in live:
                live.remove(lo)
                live.remove(hi)
                pairs.append((lo, hi))
    lower_to_upper = dict(pairs)
    upper_to_lower = {u: l for l, u in pairs}
    assert len(lower_to_upper) == len(upper_to_lower) == len(pairs)
    assert all(u.bit_count() == l.bit_count()+1 and (u & l) == l
               for l, u in pairs)
    assert 2*len(pairs)+len(live) == len(faces)-1
    return sorted(live), lower_to_upper, upper_to_lower


def directed_hasse_acyclicity(faces, lower, upper):
    # Matched Hasse edge lower -> upper; all others upper -> lower.
    indegrees = {f: 0 for f in faces if f}
    incidences = 0
    for hi in indegrees:
        for lo, sign in signed_boundary(hi):
            if not lo:
                continue
            incidences += 1
            if lower.get(lo) == hi:
                indegrees[hi] += 1
            else:
                indegrees[lo] += 1
    queue = deque(f for f, d in indegrees.items() if not d)
    processed = 0
    while queue:
        hi = queue.popleft()
        processed += 1
        for lo, sign in signed_boundary(hi):
            if not lo or upper.get(hi) == lo:
                continue
            indegrees[lo] -= 1
            if indegrees[lo] == 0:
                queue.append(lo)
        if hi in lower:
            up = lower[hi]
            indegrees[up] -= 1
            if indegrees[up] == 0:
                queue.append(up)
    assert processed == len(indegrees), (processed, len(indegrees))
    return incidences


def integral_morse_boundary(critical, lower, upper, high_dim):
    # Degree-d-to-(d-1) differential by exact integer gradient paths.
    low_cells = [s for s in critical if s.bit_count() == high_dim]
    high_cells = [s for s in critical if s.bit_count() == high_dim+1]
    target = {s: i for i, s in enumerate(low_cells)}
    memo = {}
    def project(s):
        if s in memo:
            return memo[s]
        if s in target:
            return {target[s]: 1}
        if s in upper:
            return {}  # matched as an upper cell in this degree
        assert s in lower, ('unmatched noncritical face', s)
        up = lower[s]
        own_sign = None
        other = []
        for r, sign in signed_boundary(up):
            if r == s:
                own_sign = sign
            else:
                other.append((r, sign))
        assert own_sign in (1,-1)
        coeff = defaultdict(int)
        for r, sign in other:
            for i, c in project(r).items():
                coeff[i] -= own_sign*sign*c
        memo[s] = {i: c for i, c in coeff.items() if c}
        return memo[s]
    mat = [[0]*len(high_cells) for _ in low_cells]
    for j, cell in enumerate(high_cells):
        for s, sign in signed_boundary(cell):
            for i, c in project(s).items():
                mat[i][j] += sign*c
    return mat, len(memo)


def exact_rank(mat):
    if not mat:
        return 0
    a = [[Fraction(x) for x in row] for row in mat]
    nr, nc = len(a), len(a[0])
    r = 0
    for c in range(nc):
        k = next((k for k in range(r, nr) if a[k][c]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        pivot = a[r][c]
        for i in range(r+1,nr):
            if a[i][c]:
                f = a[i][c] / pivot
                for j in range(c,nc):
                    a[i][j] -= f*a[r][j]
        r += 1
        if r == nr:
            break
    return r


def determinant(a):
    if len(a) == 0:
        return 1
    # Fraction-free Bareiss, exact integer arithmetic.
    n = len(a)
    assert all(len(row) == n for row in a)
    b = [row[:] for row in a]
    prev = 1
    sign = 1
    for k in range(n-1):
        if b[k][k] == 0:
            r = next((i for i in range(k+1,n) if b[i][k]), None)
            if r is None:
                return 0
            b[r], b[k] = b[k], b[r]
            sign *= -1
        pivot = b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z = b[i][j]*pivot - b[i][k]*b[k][j]
                assert z % prev == 0
                b[i][j] = z // prev
            b[i][k] = 0
        prev = pivot
    return sign*b[-1][-1]


def unit_rank_minor(mat, rank):
    rows, cols = len(mat), len(mat[0])
    for row_ids in combinations(range(rows), rank):
        for col_ids in combinations(range(cols), rank):
            v = determinant([[mat[i][j] for j in col_ids] for i in row_ids])
            if abs(v) == 1:
                return list(row_ids),list(col_ids),v
    raise AssertionError('no unit maximal-rank minor')


def mod_two_betti(faces):
    by_dim = defaultdict(list)
    for f in faces:
        if f:
            by_dim[f.bit_count()-1].append(f)
    ranks = {}
    for d in sorted(by_dim):
        if d == 0:
            continue
        row_index = {f:i for i,f in enumerate(by_dim[d-1])}
        pivots = {}
        for s in by_dim[d]:
            c = 0
            for r, sign in signed_boundary(s):
                c ^= 1 << row_index[r]
            while c:
                k = c.bit_length()-1
                if k in pivots:
                    c ^= pivots[k]
                else:
                    pivots[k] = c
                    break
        ranks[d] = len(pivots)
    betti = {d: len(cells)-ranks.get(d,0)-ranks.get(d+1,0)
             for d,cells in by_dim.items()}
    betti[0] -= 1  # reduced homology
    return {d:r for d,r in betti.items() if r}


def main():
    print('BASIC_FINITE_CYCLE_PRODUCT_CERTIFICATE')
    for m in CYCLE_LENGTHS:
        exp=EXPECTED[m]
        adj=adjacency(m)
        faces=enumerate_faces(adj)
        assert len(faces)-1 == exp['face_count']
        assert len(faces) == layer_transfer_face_count(m)
        critical, lower, upper = matching(faces,3*m)
        assert len(lower) == exp['pairs']
        counts = dict(Counter(s.bit_count()-1 for s in critical))
        assert counts == exp['critical'], (m,counts)
        incidences = directed_hasse_acyclicity(faces,lower,upper)
        assert incidences == exp['incidences']
        d = exp['degree']
        mat, paths = integral_morse_boundary(critical,lower,upper,d)
        assert exact_rank(mat)==exp['rank']
        assert len(mat)-exp['rank']==exp['lower_betti']
        assert len(mat[0])-exp['rank']==exp['upper_betti']
        minor=unit_rank_minor(mat,exp['rank'])
        betti=mod_two_betti(faces)
        assert betti == {d-1:exp['lower_betti'],d:exp['upper_betti']}
        print('cycle',m,'colors 3','faces',len(faces)-1,'pairs',len(lower),
              'incidences',incidences,'critical',sorted(counts.items()),
              'morse_matrix',mat,'unit_rank_minor',minor,
              'projected_lower_faces',paths,'mod2_betti',sorted(betti.items()))
    print('ALL_THREE_INTEGRAL_MORSE_AND_INDEPENDENT_MOD2_CHECKS_PASS')

if __name__ == '__main__':
    main()
