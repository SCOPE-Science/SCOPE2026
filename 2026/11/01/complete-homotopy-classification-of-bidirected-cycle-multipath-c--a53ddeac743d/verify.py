#!/usr/bin/env python3
"""Independent finite checks for bidirected-cycle multipath complexes.
Run with Python 3.9 or later: python3 verify.py
The infinite homotopy claim is proved mathematically in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations, product


def ternary_faces(m):
    """Enumerate from undirected-edge states 0, forward or backward."""
    out = defaultdict(set)
    out[-1].add(())
    for choices in product((0, 1, 2), repeat=m):
        indeg = [0] * m
        outdeg = [0] * m
        chosen = []
        for i, direction in enumerate(choices):
            if not direction:
                continue
            u, v = (i, (i+1) % m) if direction == 1 else ((i+1) % m, i)
            outdeg[u] += 1
            indeg[v] += 1
            chosen.append(i if direction == 1 else m+i)
        if max(indeg) > 1 or max(outdeg) > 1:
            continue
        # The underlying graph is one simple cycle. Its only possible
        # directed cycles use all edges, with the same orientation.
        if len(chosen) == m:
            continue
        chosen = tuple(sorted(chosen))
        out[len(chosen)-1].add(chosen)
    return {k: sorted(v) for k, v in out.items()}


def direct_faces(m):
    """Different enumeration: all subsets of the directed arcs, with DFS."""
    arcs = [(i, (i+1) % m) for i in range(m)] + [((i+1) % m, i) for i in range(m)]
    out = defaultdict(list)
    out[-1] = [()]
    for k in range(1, m):
        for subset in combinations(range(2*m), k):
            next_at = {}
            targets = set()
            valid = True
            for index in subset:
                u, v = arcs[index]
                if u in next_at or v in targets:
                    valid = False
                    break
                next_at[u] = v
                targets.add(v)
            if not valid:
                continue
            for start in next_at:
                seen = set()
                x = start
                while x in next_at and x not in seen:
                    seen.add(x)
                    x = next_at[x]
                if x in seen:
                    valid = False
                    break
            if valid:
                out[k-1].append(subset)
    return dict(out)


def insert(row, pivots):
    while row:
        j = row.bit_length()-1
        if j in pivots:
            row ^= pivots[j]
        else:
            pivots[j] = row
            return


def mod2_homology(faces, maxdim):
    ranks = {0: 0}
    for d in range(1, maxdim+1):
        lower = {s:i for i,s in enumerate(faces[d-1])}
        pivots = {}
        for simplex in faces[d]:
            row = 0
            for j in range(len(simplex)):
                face = simplex[:j]+simplex[j+1:]
                row ^= 1 << lower[face]
            insert(row, pivots)
        ranks[d] = len(pivots)
    answer = {}
    for d in range(maxdim+1):
        b = len(faces[d]) - ranks[d] - ranks.get(d+1, 0) - (d==0)
        if b:
            answer[d] = b
    return answer


def top_cycles(faces, m):
    top = set(faces[m-2])
    forward = sorted(combinations(range(m), m-1))
    reverse = sorted(combinations(range(m,2*m), m-1))
    assert top == set(forward) | set(reverse)
    for side in (range(m), range(m,2*m)):
        # The signed simplicial boundary of the boundary of a simplex is 0.
        coeffs = {}
        vertices = tuple(side)
        for a in range(m):
            face = vertices[:a]+vertices[a+1:]
            for b in range(m-1):
                sub = face[:b]+face[b+1:]
                coeffs[sub] = coeffs.get(sub, 0) + (-1)**(a+b)
        assert set(coeffs.values()) == {0}


def low_case_checks(faces, m):
    forward = set(range(m))
    reverse = set(range(m,2*m))
    def mixed(f):
        return bool(set(f) & forward) and bool(set(f) & reverse)
    cross = [e for e in faces[1] if mixed(e)]
    mixedtri = [t for t in faces[2] if mixed(t)] if 2 in faces else []
    if m == 3:
        assert not cross and not mixedtri
        assert [len(faces[d]) for d in (0,1)] == [6,6]
        return 'two disconnected boundary triangles'
    if m == 4:
        assert len(cross)==4 and not mixedtri
        assert [len(faces[d]) for d in (0,1,2)] == [8,16,8]
        return 'two boundary tetrahedra linked by four edges'
    if m == 5:
        assert len(cross)==10 and len(mixedtri)==10
        lookup = {e:i for i,e in enumerate(cross)}
        neighbors = {i:set() for i in range(10)}
        for tri in mixedtri:
            bridges = [e for e in combinations(tri,2) if e in lookup]
            assert len(bridges)==2
            a,b = [lookup[e] for e in bridges]
            neighbors[a].add(b)
            neighbors[b].add(a)
        assert all(len(z)==2 for z in neighbors.values())
        seen = {0}
        queue = [0]
        while queue:
            for w in neighbors[queue.pop()]:
                if w not in seen:
                    seen.add(w)
                    queue.append(w)
        assert len(seen)==10
        return 'ten bridge edges identified by ten triangles in one cycle'
    return None


def expected_betti(n):
    if n==2:
        return {0:1,1:2}
    if n%4 == 0:
        low=n//2
    else:
        low=(n-1)//2
    mult=3 if n%4==3 else 1
    return {low:mult,n-1:2}


def main():
    for n in range(2,10):
        m=n+1
        fs=ternary_faces(m)
        if m <= 8:
            other=direct_faces(m)
            assert fs == other
        top_cycles(fs,m)
        betti=mod2_homology(fs,m-2)
        assert betti==expected_betti(n),(n,betti,expected_betti(n))
        extra=low_case_checks(fs,m)
        total=sum(len(z) for z in fs.values())
        print(f'CHECK_OK n={n} base_vertices={m} faces_including_empty={total} '
              f'betti_mod2={betti}' + (f' case={extra}' if extra else ''))
    print('ALL_VERIFY_OK top_sphere_cycles small_n_geometry and_mod2_chain_ranks')

if __name__=='__main__':
    main()
