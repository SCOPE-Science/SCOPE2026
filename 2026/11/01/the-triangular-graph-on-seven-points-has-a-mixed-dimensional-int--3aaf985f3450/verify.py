"""Finite integral homotopy certificate for the open-neighborhood complex of L(K_7).

Run with Python 3.10+. No nonstandard dependencies. This verifies an acyclic
Forman matching, the exact integral Morse differential, and independent mod-2
simplicial boundary ranks. It is not a proof about other graph sizes.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations


def complex_faces(n):
    vertices = list(combinations(range(n), 2))
    all_faces = {0}
    facets = []
    for a in vertices:
        indices = [i for i, b in enumerate(vertices) if len(set(a) & set(b)) == 1]
        assert len(indices) == 2 * (n-2)
        facet = sum(1 << i for i in indices)
        facets.append(facet)
        subsets = [0]
        for i in indices:
            subsets += [f | (1 << i) for f in subsets]
        all_faces.update(subsets)
    return vertices, facets, all_faces


def matching(faces, number_of_vertices):
    remaining = set(faces)
    pairs = []
    for i in range(number_of_vertices):
        bit = 1 << i
        for f in sorted(remaining):
            if (f & bit) or (f | bit) not in remaining:
                continue
            g = f | bit
            remaining.remove(f)
            remaining.remove(g)
            pairs.append((f, g))
    return pairs, remaining


def oriented_facets(mask):
    indices = [i for i in range(mask.bit_length()) if mask & (1<<i)]
    return [(mask ^ (1<<i), -1 if k % 2 else 1) for k,i in enumerate(indices)]


def verify_acyclic(faces, pairs):
    # Omit empty face and its toggle: an ordinary Forman matching has one
    # unmatched critical zero-cell, represented by the toggle partner of 0.
    ordinary = faces - {0}
    match = {frozenset((f,g)) for f,g in pairs if f}
    edges = []
    indeg = {f: 0 for f in ordinary}
    out = defaultdict(list)
    for high in ordinary:
        if high.bit_count() == 1:
            continue
        for low,_ in oriented_facets(high):
            a,b = (low,high) if frozenset((low,high)) in match else (high,low)
            out[a].append(b)
            indeg[b] += 1
            edges.append((a,b))
    q = deque(f for f,d in indeg.items() if d == 0)
    consumed = 0
    while q:
        x = q.popleft();consumed += 1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert consumed == len(ordinary), ('directed cycle',consumed,len(ordinary))
    return len(edges), consumed


def verify_integral_morse_boundary(pairs, critical):
    lower = {f:g for f,g in pairs}
    upper = {g:f for f,g in pairs}
    crit3 = {f for f in critical if f.bit_count()==4}
    crit4 = {f for f in critical if f.bit_count()==5}
    @lru_cache(None)
    def proj(face):
        # Projection onto critical 3-cells in algebraic cellular cancellation.
        if face in crit3:return {face:1}
        if face in upper:return {}
        assert face in lower, ('unmatched noncritical three-cell',face)
        up=lower[face]
        assert up.bit_count()==5
        bdy=dict(oriented_facets(up));pivot=bdy[face]
        assert pivot in (-1,1)
        out=defaultdict(int)
        for other,coeff in bdy.items():
            if other==face:continue
            for c,a in proj(other).items():
                out[c]-=pivot*coeff*a
        return {c:a for c,a in out.items() if a}
    all_nonzero = []
    for top in sorted(crit4):
        d=defaultdict(int)
        for face,coeff in oriented_facets(top):
            for c,a in proj(face).items():
                d[c]+=coeff*a
        d={c:a for c,a in d.items() if a}
        if d:all_nonzero.append((top,d))
    assert not all_nonzero, all_nonzero
    return len(crit3), len(crit4),proj.cache_info().currsize


def gf2_rank(columns):
    pivot = {}
    for x in columns:
        while x:
            i=x.bit_length()-1
            if i in pivot:x ^= pivot[i]
            else:pivot[i]=x;break
    return len(pivot)


def verify_simplicial_mod2(faces):
    bydim = defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    for arr in bydim.values():arr.sort()
    ranks=[]
    for k in range(1,1+max(bydim)):
        lower = {f:i for i,f in enumerate(bydim[k-1])}
        cols = []
        for f in bydim[k]:
            b=0
            for g,_ in oriented_facets(f):b ^= (1<<lower[g])
            cols.append(b)
        ranks.append(gf2_rank(cols))
    fvector = [len(bydim[k]) for k in range(1+max(bydim))]
    betti=[fvector[k]-(ranks[k-1] if k else 0)-(ranks[k] if k<len(ranks) else 0) for k in range(len(fvector))]
    assert fvector == [21,210,1190,3780,5187,4410,2520,945,210,21], fvector
    assert ranks == [20,190,1000,2534,2646,1764,756,189,21],ranks
    assert betti == [1,0,0,246,7,0,0,0,0,0],betti
    return fvector,ranks,betti


def main():
    verts,facet,faces = complex_faces(7)
    assert len(verts)==21 and len(facet)==21 and len(set(facet))==21
    assert len(faces)==18495
    pairs, crit = matching(faces,len(verts))
    assert len(pairs)==9121 and len(crit)==253
    assert 0 not in crit
    assert all(f.bit_count() in (4,5) for f in crit)
    assert Counter(f.bit_count()-1 for f in crit)=={3:246,4:7}
    edgecount,nodes=verify_acyclic(faces,pairs)
    betti3,betti4,projections=verify_integral_morse_boundary(pairs,crit)
    fv,ranks,betti=verify_simplicial_mod2(faces)
    print('T7_NEIGHBORHOOD_INTEGRAL_WEDGE_VERIFIED')
    print('vertices=21 facet_size=10 augmented_faces=18495 ordinary_faces=18494')
    print('face_vector='+repr(fv))
    print('full_simplicial_boundary_ranks_mod2='+repr(ranks))
    print('simplicial_betti_mod2='+repr(betti))
    print('augmented_morse_pairs=9121 critical_augmented_faces=253')
    print('ordinary_critical_faces=(0:1,3:246,4:7)')
    print(f'hasse_incidences={edgecount} acyclic_toposort_faces={nodes}')
    print(f'integral_morse_boundary_4_to_3=zero ({betti4} by {betti3}); projected_faces={projections}')
    print('homotopy_type=wedge(246,S3)+wedge(7,S4)')
if __name__=='__main__':main()
