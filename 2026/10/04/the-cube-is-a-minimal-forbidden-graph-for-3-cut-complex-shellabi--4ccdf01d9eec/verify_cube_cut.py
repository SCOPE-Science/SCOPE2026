#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction
from functools import lru_cache
from collections import Counter, deque


def bitcount(x):
    return x.bit_count()


def vertices(mask):
    return [i for i in range(8) if (mask >> i) & 1]


def cube_edges():
    return {(u, v) if u < v else (v, u)
            for u in range(8) for b in range(3)
            for v in [u ^ (1 << b)] if u < v}

EDGES = cube_edges()


def adjacent(u, v):
    return (min(u, v), max(u, v)) in EDGES


def connected_subset(mask):
    vs = vertices(mask)
    if len(vs) <= 1:
        return True
    seen = {vs[0]}
    q = [vs[0]]
    while q:
        u = q.pop()
        for v in vs:
            if v not in seen and adjacent(u, v):
                seen.add(v)
                q.append(v)
    return len(seen) == len(vs)


def cut_facets(vmask, k=3):
    vs = vertices(vmask)
    if len(vs) < k:
        return []
    out = []
    for S in combinations(vs, k):
        sm = sum(1 << x for x in S)
        if not connected_subset(sm):
            out.append(vmask ^ sm)
    return sorted(set(out))


def all_nonempty_faces(facets):
    fs = set()
    for F in facets:
        sub = F
        while sub:
            fs.add(sub)
            sub = (sub - 1) & F
    return fs


def face_vector(faces):
    c = Counter(bitcount(f)-1 for f in faces)
    return tuple(c[d] for d in range(max(c)+1)) if c else ()


def hasse_covers(faces):
    covers = []
    face_set = set(faces)
    for f in sorted(face_set):
        for v in range(8):
            g = f | (1 << v)
            if g != f and g in face_set and bitcount(g) == bitcount(f)+1:
                covers.append((f, g))
    return covers


def element_matching(faces):
    unmatched = set(faces)
    pairs = []
    for v in range(8):
        b = 1 << v
        for f in sorted(list(unmatched)):
            if f not in unmatched or (f & b):
                continue
            g = f | b
            if g in unmatched:
                pairs.append((f, g))
                unmatched.remove(f)
                unmatched.remove(g)
    return pairs, sorted(unmatched)


def matching_acyclic(faces, pairs):
    matched = {(a,b) for a,b in pairs}
    adj = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    for a,b in hasse_covers(faces):
        # Standard Morse orientation: unmatched cover b -> a; matched cover a -> b.
        if (a,b) in matched:
            u,v = a,b
        else:
            u,v = b,a
        adj[u].append(v)
        indeg[v] += 1
    q = deque([f for f,d in indeg.items() if d == 0])
    seen = 0
    while q:
        u = q.popleft(); seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == len(faces)


def rank_q(matrix):
    if not matrix:
        return 0
    A = [list(map(Fraction, row)) for row in matrix]
    m, n = len(A), len(A[0]) if A else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r,m) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        p = A[r][c]
        A[r] = [x/p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                a = A[i][c]
                A[i] = [A[i][j] - a*A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def boundary_matrix(faces, d):
    cols = sorted([f for f in faces if bitcount(f) == d+1])
    rows = sorted([f for f in faces if bitcount(f) == d])
    ridx = {f:i for i,f in enumerate(rows)}
    M = [[0]*len(cols) for _ in rows]
    for j,f in enumerate(cols):
        ordered = [v for v in range(8) if f & (1<<v)]
        for pos,v in enumerate(ordered):
            g = f ^ (1<<v)
            M[ridx[g]][j] = -1 if pos % 2 else 1
    return M


def betti_q(faces):
    dims = Counter(bitcount(f)-1 for f in faces)
    maxd = max(dims) if dims else -1
    ranks = {}
    for d in range(1,maxd+1):
        ranks[d] = rank_q(boundary_matrix(faces,d))
    betti = []
    for d in range(maxd+1):
        nd = dims[d]
        rd = ranks.get(d,0)
        rnext = ranks.get(d+1,0)
        betti.append(nd-rd-rnext)
    return tuple(betti), tuple(ranks.get(d,0) for d in range(1,maxd+1))


def maximal_by_inclusion(masks):
    uniq = sorted(set(masks), key=lambda x:(bitcount(x),x), reverse=True)
    out=[]
    for m in uniq:
        if not any((m | a) == a for a in out):
            out.append(m)
    return out


def shelling_valid(facets, order):
    if not facets:
        return order == []
    if sorted(order) != list(range(len(facets))):
        return False
    r = bitcount(facets[0])
    if any(bitcount(F) != r for F in facets):
        return False
    earlier=[]
    for jidx in order:
        F = facets[jidx]
        if earlier:
            inter = [F & facets[i] for i in earlier]
            maximal = maximal_by_inclusion(inter)
            # Pure codimension-one intersection. For r=1, the empty face has size 0.
            if any(bitcount(x) != r-1 for x in maximal):
                return False
        earlier.append(jidx)
    return True


def find_shelling(facets):
    m=len(facets)
    if m == 0:
        return []
    r=bitcount(facets[0])
    assert all(bitcount(F)==r for F in facets)
    full=(1<<m)-1

    @lru_cache(None)
    def dfs(sel):
        if sel == full:
            return ()
        earlier=[i for i in range(m) if (sel>>i)&1]
        for j in range(m):
            if (sel>>j)&1:
                continue
            if not earlier:
                ok=True
            else:
                ints=[facets[j] & facets[i] for i in earlier]
                maximal=maximal_by_inclusion(ints)
                ok=all(bitcount(x)==r-1 for x in maximal)
            if ok:
                tail=dfs(sel | (1<<j))
                if tail is not None:
                    return (j,)+tail
        return None
    ans=dfs(0)
    return None if ans is None else list(ans)


def verify_cube_connectivity():
    full=(1<<8)-1
    for r in (0,1,2):
        for rem in combinations(range(8),r):
            rm=sum(1<<x for x in rem)
            if not connected_subset(full ^ rm):
                return False
    return True


def main():
    full=(1<<8)-1
    facets=cut_facets(full,3)
    faces=all_nonempty_faces(facets)
    fv=face_vector(faces)
    covers=hasse_covers(faces)
    pairs,critical=element_matching(faces)
    assert len(facets)==32, len(facets)
    assert len(faces)==188, len(faces)
    assert fv==(8,28,56,64,32), fv
    assert len(covers)==640, len(covers)
    assert len(pairs)==91, len(pairs)
    assert matching_acyclic(faces,pairs)
    critical_by_dim=Counter(bitcount(f)-1 for f in critical)
    assert critical_by_dim==Counter({4:4,3:1,0:1}), critical_by_dim
    expected_crit={1,46,124,188,218,230}
    assert set(critical)==expected_crit, [tuple(vertices(x)) for x in critical]

    betti,ranks=betti_q(faces)
    assert ranks==(7,21,35,28), ranks
    assert betti==(1,0,0,1,4), betti
    assert verify_cube_connectivity()

    checked=0
    nontrivial=0
    hist=Counter()
    for sm in range(0,full):
        if sm==full:
            continue
        n=bitcount(sm)
        if n==8:
            continue
        facets_h=cut_facets(sm,3)
        order=find_shelling(facets_h)
        assert order is not None, (vertices(sm),len(facets_h))
        assert shelling_valid(facets_h,order), (vertices(sm),order)
        checked += 1
        if n>=4:
            nontrivial += 1
            hist[(n,len(facets_h))]+=1
    assert checked==255, checked
    assert nontrivial==162, nontrivial
    expected_hist={
        (4,0):6,(4,1):8,(4,2):24,(4,3):24,(4,4):8,
        (5,4):24,(5,7):32,
        (6,10):12,(6,12):12,(6,14):4,
        (7,20):8,
    }
    assert dict(hist)==expected_hist, hist

    print('cube_facets=32')
    print('cube_faces=188')
    print('cube_f_vector=(8,28,56,64,32)')
    print('cube_hasse_covers=640')
    print('morse_pairs=91')
    print('critical_by_dimension={0:1,3:1,4:4}')
    print('boundary_ranks_Q=(7,21,35,28)')
    print('betti_Q=(1,0,0,1,4)')
    print('proper_induced_subgraphs_checked=255')
    print('proper_induced_subgraphs_order_4_to_7=162')
    print('all_proper_cut_complexes_shellable=True')
    print('cube_vertex_connectivity_at_least_3=True')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
