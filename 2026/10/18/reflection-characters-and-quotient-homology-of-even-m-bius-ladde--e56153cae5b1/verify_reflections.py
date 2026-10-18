"""Independent finite checks for reflection characters of perfect-matching complexes.
Run: python3 verify_reflections.py. Requires Python 3 standard library only.
"""
from functools import lru_cache


def ladder_edges(n):
    return [tuple(sorted((i, (i+1) % (2*n)))) for i in range(2*n)] + [(i, i+n) for i in range(n)]


def perfect_matchings(n, edges):
    adj = [[] for _ in range(2*n)]
    for j, (u, v) in enumerate(edges):
        adj[u].append((v, j)); adj[v].append((u, j))

    @lru_cache(None)
    def rec(vertices):
        if not vertices:
            return (0,)
        v = (vertices & -vertices).bit_length() - 1
        out = []
        for w, j in adj[v]:
            if vertices & (1 << w):
                out.extend(x | (1 << j) for x in rec(vertices ^ (1 << v) ^ (1 << w)))
        return tuple(out)

    return rec((1 << (2*n)) - 1)


def faces_from_facets(facets):
    faces = {0}
    for facet in facets:
        local = {0}
        rem = facet
        while rem:
            bit = rem & -rem
            rem -= bit
            local.update([face | bit for face in tuple(local)])
        faces.update(local)
    return faces


def conflict_graph(n, edges):
    adj = [set() for _ in edges]
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            shared = bool(set(edges[i]) & set(edges[j]))
            extra = i < 2*n and j < 2*n and (j-i) in (n-1, n+1)
            if shared or extra:
                adj[i].add(j); adj[j].add(i)
    return adj


def enumerate_independent_sets(adj):
    # Iteration uses only the pairwise incompatibility graph; no perfect-matchings data.
    selected = [(0, 0)]
    for j in range(len(adj)):
        bit = 1 << j
        forbidden = sum(1 << x for x in adj[j])
        additions = [(f | bit, q | forbidden) for f, q in selected if not (q & bit)]
        selected.extend(additions)
    return {f for f, _ in selected}


def permutation(n, edges, a):
    lookup = {edge:j for j, edge in enumerate(edges)}
    return [lookup[tuple(sorted(((a-u) % (2*n), (a-v) % (2*n))))] for u,v in edges]


def orbit_count(face, permutation_map):
    if face == 0:
        return 0
    unseen = face
    count = 0
    while unseen:
        bit = unseen & -unseen
        j = bit.bit_length() - 1
        assert face & (1 << permutation_map[j])
        unseen &= ~(1 << j)
        unseen &= ~(1 << permutation_map[j])
        count += 1
    return count


def direct_homology_trace(n, faces, edges, a):
    perm = permutation(n, edges, a)
    signed_sum = 0
    count = 0
    for face in faces:
        image = 0
        rest = face
        while rest:
            bit = rest & -rest; rest -= bit
            image |= 1 << perm[bit.bit_length()-1]
        if image != face:
            continue
        count += 1
        signed_sum += (-1) ** orbit_count(face, perm)
    return -((-1) ** (n//2-1)) * signed_sum, count


def orbit_graph(n, edges, adj, a):
    perm = permutation(n, edges, a)
    seen = set()
    orbits = []
    names = []
    for i in range(len(edges)):
        if i in seen:
            continue
        orbit = sorted({i, perm[i]})
        seen.update(orbit)
        if len(orbit) == 2 and orbit[0] in adj[orbit[1]]:
            continue
        orbits.append(orbit)
        names.append('/'.join(('E'+str(j) if j<2*n else 'S'+str(j-2*n)) for j in orbit))
    reduced = [set() for _ in orbits]
    for i in range(len(orbits)):
        for j in range(i+1, len(orbits)):
            if any(y in adj[x] for x in orbits[i] for y in orbits[j]):
                reduced[i].add(j); reduced[j].add(i)
    return names, reduced


def verify_fold(n, edges, adj):
    m = n//2
    names, gr = orbit_graph(n, edges, adj, 1)
    assert len(names) == 3*m + 1
    for j in range(1,m):
        assert gr[j] == gr[n-j] and (n-j not in gr[j])
    surviving = list(range(m+1)) + list(range(n+1, len(names)))
    assert len(surviving)==2*m+1
    old_to_new = {v:i for i,v in enumerate(surviving)}
    actual = {tuple(sorted((old_to_new[i], old_to_new[j])))
              for i in surviving for j in gr[i] if j in old_to_new}
    expected = set()
    for i in range(m):
        expected.update((tuple(sorted((i,i+1))),
                         tuple(sorted((i,m+1+i))),
                         tuple(sorted((i+1,m+1+i)))))
    assert actual == expected


def mod2_reduced_betti(faces):
    by_dim = {}
    for f in faces:
        by_dim.setdefault(f.bit_count()-1,[]).append(f)
    ranks = {}
    maxd = max(by_dim)
    for d in range(maxd, -1, -1):
        sources = by_dim.get(d, [])
        targets = {f:i for i,f in enumerate(by_dim.get(d-1, []))}
        pivots = {}
        for face in sources:
            bnd = 0
            rem = face
            while rem:
                bit = rem & -rem; rem -= bit
                bnd ^= 1 << targets[face ^ bit]
            while bnd:
                p = bnd.bit_length()-1
                if p in pivots:
                    bnd ^= pivots[p]
                else:
                    pivots[p]=bnd;break
        ranks[d]=len(pivots)
    betti = {d: len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)
             for d in by_dim if d>=0}
    return {d:b for d,b in betti.items() if b}


def predicted(n, a):
    if a%2 == 0 or n%4 == 0:return 0
    return 2*((-1)**((n-2)//4))


def main():
    checks = {'full_flag_faces':0,'full_mod2':0,'direct_traces':0,'folds':0}
    for n in range(4,13,2):
        E=ladder_edges(n)
        A=conflict_graph(n,E)
        verify_fold(n,E,A)
        checks['folds']+=1
        PM=perfect_matchings(n,E)
        faces=faces_from_facets(PM)
        for a in (0,1):
            got,count=direct_homology_trace(n,faces,E,a)
            assert got==predicted(n,a),(n,a,got,count)
            checks['direct_traces']+=1
        if n <= 10:
            flag_faces=enumerate_independent_sets(A)
            assert faces==flag_faces,(n, len(faces),len(flag_faces))
            checks['full_flag_faces']+=1
        if n <= 8:
            assert mod2_reduced_betti(faces)=={n//2-1:2}
            checks['full_mod2']+=1
    for n in range(14,41,2):
        E=ladder_edges(n);A=conflict_graph(n,E)
        verify_fold(n,E,A)
        checks['folds']+=1
    print('checks:',checks)
    print('direct odd-axis character n=4,6,8,10,12: 0,-2,0,2,0')
    print('VERIFY_OK')

if __name__=='__main__':main()
